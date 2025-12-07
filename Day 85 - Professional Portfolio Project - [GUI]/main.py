import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark Tool")
        self.root.geometry("800x600")

        self.image = None  # Original image
        self.watermarked_image = None  # Image with watermark
        self.logo_path = None  # Path to logo if chosen

        # GUI elements
        self.label = tk.Label(root, text="Upload an image to start")
        self.label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=5)
        self.text_entry.insert(0, "Enter watermark text (e.g., yourwebsite.com)")

        self.add_text_btn = tk.Button(root, text="Add Text Watermark", command=self.add_text_watermark)
        self.add_text_btn.pack(pady=5)

        self.upload_logo_btn = tk.Button(root, text="Upload Logo", command=self.upload_logo)
        self.upload_logo_btn.pack(pady=5)

        self.add_logo_btn = tk.Button(root, text="Add Logo Watermark", command=self.add_logo_watermark)
        self.add_logo_btn.pack(pady=5)

        self.save_btn = tk.Button(root, text="Save Watermarked Image", command=self.save_image)
        self.save_btn.pack(pady=5)

        self.preview_label = tk.Label(root)
        self.preview_label.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if file_path:
            try:
                self.image = Image.open(file_path).convert("RGBA")
                self.watermarked_image = self.image.copy()
                self.display_preview(self.watermarked_image)
                self.label.config(text="Image uploaded successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {e}")

    def upload_logo(self):
        self.logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])  # PNG for transparency
        if self.logo_path:
            self.label.config(text="Logo uploaded successfully")

    def add_text_watermark(self):
        if not self.image:
            messagebox.showerror("Error", "Upload an image first")
            return

        text = self.text_entry.get()
        if not text:
            messagebox.showerror("Error", "Enter some text")
            return

        self.watermarked_image = self.image.copy()
        draw = ImageDraw.Draw(self.watermarked_image)

        try:
           font = ImageFont.truetype("arial.ttf", 15)
        except IOError:
           font = ImageFont.load_default()

        # Get text size
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Position at bottom-right with padding
        width, height = self.watermarked_image.size
        x = width - text_width - 10
        y = height - text_height - 10

        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white
        self.display_preview(self.watermarked_image)
        self.label.config(text="Text watermark added")

    def add_logo_watermark(self):
        if not self.image:
            messagebox.showerror("Error", "Upload an image first")
            return
        if not self.logo_path:
            messagebox.showerror("Error", "Upload a logo first")
            return

        self.watermarked_image = self.image.copy()
        try:
            logo = Image.open(self.logo_path).convert("RGBA")
            logo = logo.resize((100, 100))  # Resize logo to fixed size; adjust as needed

            # Position at bottom-right with padding
            width, height = self.watermarked_image.size
            logo_width, logo_height = logo.size
            x = width - logo_width - 10
            y = height - logo_height - 10

            self.watermarked_image.paste(logo, (x, y), logo)  # Use logo as mask for transparency
            self.display_preview(self.watermarked_image)
            self.label.config(text="Logo watermark added")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add logo: {e}")

    def display_preview(self, img):
        # Resize for preview if too large
        preview_size = (400, 400)
        preview_img = img.copy()
        preview_img.thumbnail(preview_size)
        tk_img = ImageTk.PhotoImage(preview_img)
        self.preview_label.config(image=tk_img)
        self.preview_label.image = tk_img  # Keep reference

    def save_image(self):
        if not self.watermarked_image:
            messagebox.showerror("Error", "No watermarked image to save")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if file_path:
            try:
                if file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg'):
                    self.watermarked_image.convert("RGB").save(file_path)
                else:
                    self.watermarked_image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()