Day 85 - Professional Portfolio Project - [GUI]

This is a complete Python script for a desktop application using Tkinter and Pillow (PIL) to add watermarks to images.

To run this, you need to install Pillow if not already installed: pip install pillow

The program allows uploading an image, adding either text or a logo watermark, previewing it, and saving the result.

It keeps things simple: text watermark at bottom-right, logo at bottom-right with transparency if the logo has alpha.

No fancy positioning options to avoid overcomplicating; if you need more, extend it yourself.

 Flaws: Assumes images are in common formats; doesn't handle errors gracefully everywhere; GUI is basic and not responsive.

 If your images are huge, it might be slow—optimize if needed.