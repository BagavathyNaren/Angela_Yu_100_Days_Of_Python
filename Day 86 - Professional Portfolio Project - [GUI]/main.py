import tkinter as tk
from timeit import default_timer as timer
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test - WPM Calculator")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f0f0")
        
        # Expanded list of sample texts
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a powerful programming language for GUI development.",
            "Typing speed improves with consistent daily practice.",
            "Tkinter provides simple yet effective tools for desktop apps.",
            "Average typing speed is 40 words per minute for most people.",
            "Practice regularly to reach speeds of 100 words per minute.",
            "GUI applications enhance user experience significantly.",
            "Words per minute measures typing efficiency accurately."
        ]
        
        self.start_time = None
        self.high_score = 0
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the complete UI with title, sample text, input, controls, and results."""
        # Title
        title_label = tk.Label(self.root, text="Typing Speed Test", 
                              font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)
        
        # Instructions
        info_label = tk.Label(self.root, text="Type the text below exactly. Press 'Done' when finished.", 
                             font=("Arial", 12), bg="#f0f0f0")
        info_label.pack(pady=5)
        
        # Sample text display
        self.sentence = random.choice(self.sentences)
        self.sentence_label = tk.Label(self.root, text=self.sentence, 
                                      font=("Consolas", 14), wraplength=600, 
                                      bg="white", relief="solid", padx=10, pady=10)
        self.sentence_label.pack(pady=20)
        
        # Input field
        self.entry = tk.Entry(self.root, width=60, font=("Consolas", 14), 
                             relief="solid", bd=2)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda e: self.check_result())
        self.entry.focus()
        
        # Buttons frame
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=10)
        
        self.done_btn = tk.Button(btn_frame, text="Done", command=self.check_result,
                                 width=12, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.done_btn.pack(side=tk.LEFT, padx=5)
        
        self.reset_btn = tk.Button(btn_frame, text="New Text", command=self.reset_test,
                                  width=12, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        self.reset_btn.pack(side=tk.LEFT, padx=5)
        
        # Results display
        self.result_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"),
                                    bg="#f0f0f0")
        self.result_label.pack(pady=20)
        
        # High score display
        self.high_score_label = tk.Label(self.root, text=f"Best Score: {self.high_score} WPM", 
                                        font=("Arial", 12), bg="#f0f0f0", fg="#666")
        self.high_score_label.pack()
        
        self.start_time = timer()
    
    def check_result(self):
        """Calculate WPM and display results with accuracy check."""
        typed_text = self.entry.get().strip()
        
        if typed_text == self.sentence:
            end_time = timer()
            time_taken = round(end_time - self.start_time, 2)
            words = len(self.sentence.split())
            wpm = round((words / time_taken) * 60, 1)
            
            # Update high score
            if wpm > self.high_score:
                self.high_score = wpm
                self.high_score_label.config(text=f"New Best: {self.high_score} WPM!", fg="#4CAF50")
            else:
                self.high_score_label.config(text=f"Best Score: {self.high_score} WPM", fg="#666")
            
            result_text = f"✓ Perfect! Time: {time_taken}s | Speed: {wpm} WPM"
            self.result_label.config(text=result_text, fg="#4CAF50")
        else:
            accuracy = round((sum(1 for a, b in zip(typed_text, self.sentence) if a == b) / len(self.sentence)) * 100, 1)
            self.result_label.config(text=f"✗ Try again! Accuracy: {accuracy}%", fg="#f44336")
    
    def reset_test(self):
        """Reset test with new random sentence."""
        self.sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = timer()
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()