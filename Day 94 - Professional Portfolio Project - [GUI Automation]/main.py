"""
Chrome Dinosaur Game Bot - Advanced Version
Uses OpenCV template matching and adaptive timing
"""

import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab
import mss

# Disable PyAutoGUI failsafe
pyautogui.FAILSAFE = False


class DinoBot:
    def __init__(self):
        # Game coordinates (will be calibrated)
        self.game_region = None
        self.dino_region = None
        self.scan_region = None
        
        # Detection parameters
        self.obstacle_threshold = 0.6  # Template match confidence
        self.min_jump_interval = 0.4  # Minimum time between jumps
        self.last_jump_time = 0
        
        # Game state
        self.game_speed = 1.0  # Multiplier for reaction time
        self.score = 0
        
        # Screen capture
        self.sct = mss.mss()
        
    def calibrate(self):
        """Interactive calibration of game region"""
        print("\n" + "=" * 60)
        print("CALIBRATION")
        print("=" * 60)
        print("\nInstructions:")
        print("1. Open chrome://dino/ in Chrome")
        print("2. Press Space to start the game")
        print("3. Let the dino die once (to see full game area)")
        print("4. Position the game window where you want it")
        print("\nPress ENTER when ready...")
        input()
        
        print("\nMove mouse to TOP-LEFT corner of game canvas")
        print("(Where the score counter is)")
        print("Press ENTER...")
        input()
        x1, y1 = pyautogui.position()
        
        print("\nMove mouse to BOTTOM-RIGHT corner of game canvas")
        print("(Below the ground line)")
        print("Press ENTER...")
        input()
        x2, y2 = pyautogui.position()
        
        # Calculate regions
        width = x2 - x1
        height = y2 - y1
        
        self.game_region = {"top": y1, "left": x1, "width": width, "height": height}
        
        # Dino is typically around 10-15% from left, 60-70% from top
        dino_x = x1 + int(width * 0.12)
        dino_y = y1 + int(height * 0.65)
        dino_w = int(width * 0.08)
        dino_h = int(height * 0.25)
        
        self.dino_region = {"top": dino_y, "left": dino_x, "width": dino_w, "height": dino_h}
        
        # Scan region is ahead of dino
        scan_x = x1 + int(width * 0.25)
        scan_y = y1 + int(height * 0.5)
        scan_w = int(width * 0.35)
        scan_h = int(height * 0.4)
        
        self.scan_region = {"top": scan_y, "left": scan_x, "width": scan_w, "height": scan_h}
        
        print(f"\n✓ Game region: {width}x{height}")
        print(f"✓ Dino region: {dino_w}x{dino_h}")
        print(f"✓ Scan region: {scan_w}x{scan_h}")
        
        # Capture reference dino image
        self._capture_dino_template()
        
        print("\n✓ Calibration complete!")
        
    def _capture_dino_template(self):
        """Capture the dino as a template (optional for advanced detection)"""
        print("\nCapturing dino reference...")
        time.sleep(0.5)
        if self.dino_region is not None:
            img = np.array(self.sct.grab(self.dino_region))
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
            self.dino_template = img
        
    def capture_scan_region(self):
        """Capture the area ahead of the dino"""
        if self.scan_region is None:
            raise ValueError("Scan region is not set. Please calibrate first.")
        img = np.array(self.sct.grab(self.scan_region))
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        return gray
    
    def capture_game_region(self):
        """Capture entire game region"""
        if self.game_region is None:
            raise ValueError("Game region is not set. Please calibrate first.")
        img = np.array(self.sct.grab(self.game_region))
        gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        return gray
    
    def detect_obstacle_advanced(self, img):
        """
        Advanced obstacle detection using edge detection and contours
        Returns: (obstacle_detected, obstacle_type, distance)
        """
        # Apply threshold to get binary image
        _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        
        # Find contours
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if not contours:
            return False, None, None
        
        # Find the leftmost significant contour (closest obstacle)
        obstacles = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 20:  # Filter out noise
                x, y, w, h = cv2.boundingRect(cnt)
                obstacles.append((x, y, w, h, area))
        
        if not obstacles:
            return False, None, None
        
        # Sort by x position (distance from dino)
        obstacles.sort(key=lambda o: o[0])
        
        # Get closest obstacle
        x, y, w, h, area = obstacles[0]
        
        # Determine obstacle type by aspect ratio
        aspect_ratio = h / w if w > 0 else 0
        
        # Flying obstacle (pterodactyl) is wider than tall
        # Ground obstacle (cactus) is taller than wide
        if aspect_ratio < 0.8 and y < img.shape[0] * 0.4:
            obstacle_type = "flying"
        else:
            obstacle_type = "ground"
        
        # Distance is x position
        distance = x
        
        return True, obstacle_type, distance
    
    def detect_obstacle_simple(self, img):
        """
        Simple but fast obstacle detection
        Checks for dark pixel clusters in scan region
        """
        # Create binary image
        _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        
        # Check left portion of scan region (closest to dino)
        height, width = binary.shape
        left_section = binary[:, :width//3]
        
        # Count white pixels (obstacles in inverted image)
        white_pixels = np.sum(left_section == 255)
        
        # If significant white pixels, obstacle is near
        if white_pixels > 100:
            # Check if obstacle is in top half (flying) or bottom half (ground)
            top_half = binary[:height//2, :width//3]
            bottom_half = binary[height//2:, :width//3]
            
            top_pixels = np.sum(top_half == 255)
            bottom_pixels = np.sum(bottom_half == 255)
            
            if top_pixels > bottom_pixels * 1.5:
                return True, "flying", width//3
            else:
                return True, "ground", width//3
        
        return False, None, None
    
    def should_jump(self):
        """Check if enough time has passed since last jump"""
        current_time = time.time()
        if current_time - self.last_jump_time > self.min_jump_interval:
            return True
        return False
    
    def jump(self):
        """Execute jump"""
        if self.should_jump():
            pyautogui.press('space')
            self.last_jump_time = time.time()
    
    def duck(self):
        """Execute duck"""
        pyautogui.keyDown('down')
        time.sleep(0.3)
        pyautogui.keyUp('down')
    
    def is_game_over(self):
        """Detect game over screen (simple check for 'GAME OVER' region)"""
        img = self.capture_game_region()
        # Game over screen has distinct pattern - check middle of screen
        h, w = img.shape
        center_region = img[h//3:2*h//3, w//3:2*w//3]
        
        # Game over screen is lighter (more white pixels)
        white_ratio = np.sum(center_region > 200) / center_region.size
        
        return white_ratio > 0.3
    
    def restart_game(self):
        """Restart game after game over"""
        print("Game over detected. Restarting...")
        time.sleep(0.5)
        pyautogui.press('space')
        time.sleep(0.5)
    
    def run(self, use_advanced=False, visualize=False):
        """
        Main game loop
        use_advanced: Use contour-based detection (slower but more accurate)
        visualize: Show detection window (for debugging)
        """
        if not self.game_region:
            print("ERROR: Run calibrate() first!")
            return
        
        print("\n" + "=" * 60)
        print("STARTING BOT")
        print("=" * 60)
        print(f"Detection mode: {'Advanced' if use_advanced else 'Simple'}")
        print(f"Visualization: {'On' if visualize else 'Off'}")
        print("\nStarting in 3 seconds...")
        print("Press Ctrl+C to stop\n")
        time.sleep(3)
        
        # Start the game
        pyautogui.press('space')
        time.sleep(0.5)
        
        frame_count = 0
        jump_count = 0
        duck_count = 0
        start_time = time.time()
        
        try:
            while True:
                # Capture scan region
                img = self.capture_scan_region()
                
                # Detect obstacles
                if use_advanced:
                    detected, obs_type, distance = self.detect_obstacle_advanced(img)
                else:
                    detected, obs_type, distance = self.detect_obstacle_simple(img)
                
                # React to obstacle
                if detected:
                    if obs_type == "flying":
                        self.duck()
                        duck_count += 1
                    elif obs_type == "ground":
                        self.jump()
                        jump_count += 1
                
                # Visualization
                if visualize:
                    display_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                    if detected:
                        color = (0, 255, 255) if obs_type == "flying" else (0, 255, 0)
                        label = obs_type.upper() if obs_type is not None else "OBSTACLE"
                        cv2.putText(display_img, f"{label}", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                    cv2.imshow("Dino Bot Vision", display_img)
                    cv2.waitKey(1)
                
                frame_count += 1
                
                # Check for game over every 100 frames
                if frame_count % 100 == 0:
                    if self.is_game_over():
                        elapsed = time.time() - start_time
                        print(f"\n{'=' * 60}")
                        print(f"Run ended after {elapsed:.1f}s")
                        print(f"Frames: {frame_count} | Jumps: {jump_count} | Ducks: {duck_count}")
                        print(f"FPS: {frame_count/elapsed:.1f}")
                        print(f"{'=' * 60}\n")
                        
                        self.restart_game()
                        frame_count = 0
                        jump_count = 0
                        duck_count = 0
                        start_time = time.time()
                
                # Small delay for CPU
                time.sleep(0.005)
                
        except KeyboardInterrupt:
            print(f"\n\nBot stopped by user")
            elapsed = time.time() - start_time
            print(f"Final stats:")
            print(f"  Time: {elapsed:.1f}s")
            print(f"  Frames: {frame_count}")
            print(f"  Jumps: {jump_count}")
            print(f"  Ducks: {duck_count}")
            print(f"  Average FPS: {frame_count/elapsed:.1f}")
            
            if visualize:
                cv2.destroyAllWindows()


def main():
    print("\n" + "=" * 60)
    print("CHROME DINOSAUR GAME BOT v2.0")
    print("=" * 60)
    print("\nREQUIREMENTS:")
    print("  pip install opencv-python numpy pillow pyautogui mss")
    print("\nFEATURES:")
    print("  ✓ Adaptive obstacle detection")
    print("  ✓ Distinguishes ground vs flying obstacles")
    print("  ✓ Auto-restart on game over")
    print("  ✓ Performance statistics")
    print("=" * 60)
    
    bot = DinoBot()
    
    # Calibration
    bot.calibrate()
    
    # Configuration
    print("\n" + "=" * 60)
    print("CONFIGURATION")
    print("=" * 60)
    
    mode = input("\nUse advanced detection? (slower but better) [y/N]: ").lower()
    use_advanced = mode == 'y'
    
    viz = input("Enable visualization? (shows what bot sees) [y/N]: ").lower()
    visualize = viz == 'y'
    
    # Run
    bot.run(use_advanced=use_advanced, visualize=visualize)


if __name__ == "__main__":
    main()