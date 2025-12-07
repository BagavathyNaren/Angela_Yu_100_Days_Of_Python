import tkinter as tk
from tkinter import font as tkfont

class DisappearingTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Editor")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a1a")
        
        self.time_left = 5.0
        self.timer_active = False
        self.timer_id = None
        
        # Header
        header_frame = tk.Frame(root, bg="#1a1a1a")
        header_frame.pack(pady=20, padx=20, fill="x")
        
        title_label = tk.Label(
            header_frame,
            text="⚠️ Disappearing Text Editor",
            font=("Arial", 24, "bold"),
            bg="#1a1a1a",
            fg="#ff4444"
        )
        title_label.pack(anchor="w")
        
        subtitle = tk.Label(
            header_frame,
            text="Keep typing or lose everything. Stop for 5 seconds and it's gone.",
            font=("Arial", 11),
            bg="#1a1a1a",
            fg="#888888"
        )
        subtitle.pack(anchor="w")
        
        # Stats and timer frame
        stats_frame = tk.Frame(root, bg="#1a1a1a")
        stats_frame.pack(pady=10, padx=20, fill="x")
        
        self.word_count_label = tk.Label(
            stats_frame,
            text="Words: 0",
            font=("Courier", 12),
            bg="#1a1a1a",
            fg="#ffffff"
        )
        self.word_count_label.pack(side="left", padx=(0, 20))
        
        self.char_count_label = tk.Label(
            stats_frame,
            text="Characters: 0",
            font=("Courier", 12),
            bg="#1a1a1a",
            fg="#ffffff"
        )
        self.char_count_label.pack(side="left")
        
        self.timer_label = tk.Label(
            stats_frame,
            text="",
            font=("Courier", 20, "bold"),
            bg="#1a1a1a",
            fg="#00ff00"
        )
        self.timer_label.pack(side="right")
        
        # Progress bar
        self.progress_canvas = tk.Canvas(
            root,
            height=8,
            bg="#2a2a2a",
            highlightthickness=0
        )
        self.progress_canvas.pack(pady=(0, 10), padx=20, fill="x")
        
        self.progress_bar = self.progress_canvas.create_rectangle(
            0, 0, 0, 8,
            fill="#00ff00",
            outline=""
        )
        
        # Text area
        text_frame = tk.Frame(root, bg="#1a1a1a")
        text_frame.pack(pady=(0, 20), padx=20, fill="both", expand=True)
        
        self.text_area = tk.Text(
            text_frame,
            font=("Courier", 14),
            bg="#2a2a2a",
            fg="#ffffff",
            insertbackground="#ffffff",
            relief="flat",
            padx=20,
            pady=20,
            wrap="word"
        )
        self.text_area.pack(fill="both", expand=True)
        self.text_area.focus_set()
        
        # Bind typing event
        self.text_area.bind("<KeyPress>", self.on_key_press)
        
        # Initial placeholder
        self.show_placeholder()
        self.text_area.bind("<FocusIn>", self.remove_placeholder)
    
    def show_placeholder(self):
        if not self.text_area.get("1.0", "end-1c"):
            self.text_area.insert("1.0", "Start typing... don't stop for more than 5 seconds or everything disappears.")
            self.text_area.config(fg="#666666")
    
    def remove_placeholder(self, event=None):
        if self.text_area.get("1.0", "end-1c") == "Start typing... don't stop for more than 5 seconds or everything disappears.":
            self.text_area.delete("1.0", "end")
            self.text_area.config(fg="#ffffff")
    
    def on_key_press(self, event=None):
        # Remove placeholder on first keypress
        if self.text_area.cget("fg") == "#666666":
            self.text_area.delete("1.0", "end")
            self.text_area.config(fg="#ffffff")
        
        # Schedule stats update after key is processed
        self.root.after(10, self.update_stats)
        
        # Reset timer
        self.reset_timer()
    
    def update_stats(self):
        text = self.text_area.get("1.0", "end-1c")
        
        # Word count
        words = [w for w in text.split() if w]
        word_count = len(words)
        
        # Character count
        char_count = len(text)
        
        self.word_count_label.config(text=f"Words: {word_count}")
        self.char_count_label.config(text=f"Characters: {char_count}")
    
    def reset_timer(self):
        self.time_left = 5.0
        
        if not self.timer_active:
            self.timer_active = True
            self.update_timer()
    
    def update_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        
        text = self.text_area.get("1.0", "end-1c")
        
        # If text is empty, stop timer
        if not text or text == "Start typing... don't stop for more than 5 seconds or everything disappears.":
            self.timer_active = False
            self.timer_label.config(text="")
            self.progress_canvas.coords(self.progress_bar, 0, 0, 0, 8)
            return
        
        # Update timer display
        self.timer_label.config(text=f"Time: {self.time_left:.1f}s")
        
        # Update color based on time left
        if self.time_left > 3:
            color = "#00ff00"
        elif self.time_left > 1:
            color = "#ffaa00"
        else:
            color = "#ff0000"
        
        self.timer_label.config(fg=color)
        self.progress_canvas.itemconfig(self.progress_bar, fill=color)
        
        # Update progress bar
        canvas_width = self.progress_canvas.winfo_width()
        bar_width = (self.time_left / 5.0) * canvas_width
        self.progress_canvas.coords(self.progress_bar, 0, 0, bar_width, 8)
        
        # Countdown
        self.time_left -= 0.1
        
        if self.time_left <= 0:
            # Delete everything
            self.text_area.delete("1.0", "end")
            self.timer_active = False
            self.update_stats()
            self.show_placeholder()
            self.timer_label.config(text="")
            self.progress_canvas.coords(self.progress_bar, 0, 0, 0, 8)
        else:
            # Continue countdown
            self.timer_id = self.root.after(100, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextEditor(root)
    root.mainloop()