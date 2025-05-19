# PRODIGY_CS_02
 Image Encryption & Decryption Tool (Python + Tkinter)

This project is part of my internship at **Prodigy InfoTech** under the role of **Cyber Security Intern**.  
The task involved developing an **Image Encryption and Decryption tool** using **Python** and a simple **Tkinter GUI** by manipulating pixel values.

---

 What It Does

This tool allows users to:
- Select an image from their system
- Encrypt the image using a simple pixel-wise XOR operation
- Decrypt the encrypted image using the same reversible technique
- Save the encrypted/decrypted image locally

---

 Features

- User-friendly GUI using Tkinter
- Simple and reversible encryption (XOR logic)
- Supports most common image formats (`.png`, `.jpg`, `.jpeg`)
- Fast and lightweight

---

 Note

This tool uses **XOR-based pixel encryption** with a static key, which is **not secure for real-world applications**.  
It is intended for **educational and demonstrational purposes only**.

---

 How It Works

- Each pixel's RGB values are XOR’ed with a fixed key (e.g., `123`)
- This operation is reversible:
  - Encrypt: `pixel = pixel_value ^ key`
  - Decrypt: `pixel = pixel_value ^ key`

---

