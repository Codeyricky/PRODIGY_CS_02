import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

KEY = 200

def encrypt_decrypt_image(image_path, output_path):
    try:
        img = Image.open(image_path)
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    r ^ KEY,
                    g ^ KEY,
                    b ^ KEY
                )
        img.save(output_path)
        return True
    except Exception as e:
        print("Error:", e)
        return False

def select_image(encrypting=True):
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )
    if not file_path:
        return

    output_suffix = "_encrypted" if encrypting else "_decrypted"
    base, ext = os.path.splitext(file_path)
    output_path = base + output_suffix + ext

    if encrypt_decrypt_image(file_path, output_path):
        messagebox.showinfo("Success", f"Image saved to:\n{output_path}")
    else:
        messagebox.showerror("Error", "Failed to process the image.")


root = tk.Tk()
root.title("Image Encryption & Decryption")
root.geometry("400x200")

title_label = tk.Label(root, text="Image Encryption Tool", font=("Arial", 16))
title_label.pack(pady=10)

encrypt_btn = tk.Button(root, text="Encrypt Image", command=lambda: select_image(True), width=25)
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(root, text="Decrypt Image", command=lambda: select_image(False), width=25)
decrypt_btn.pack(pady=10)

root.mainloop()
