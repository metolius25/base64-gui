# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
import base64
from io import BytesIO
from PIL import Image, ImageTk

class Base64ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 Converter")

        # Text Entry
        self.text_entry_label = tk.Label(root, text="Enter Text:")
        self.text_entry_label.pack()
        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack()

        # File Entry
        self.file_entry_label = tk.Label(root, text="Select File:")
        self.file_entry_label.pack()
        self.file_entry_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.file_entry_button.pack()

        # Result Display
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()
        self.result_text = tk.Text(root, height=10, width=40)
        self.result_text.pack()

        # Buttons
        self.encode_button = tk.Button(root, text="Encode Text", command=self.encode_text)
        self.encode_button.pack()

        self.decode_button = tk.Button(root, text="Decode Text", command=self.decode_text)
        self.decode_button.pack()

        self.encode_file_button = tk.Button(root, text="Encode File", command=self.encode_file)
        self.encode_file_button.pack()

        self.decode_file_button = tk.Button(root, text="Decode File", command=self.decode_file)
        self.decode_file_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_entry_button.config(text=file_path)

    def encode_text(self):
        text_to_encode = self.text_entry.get()
        encoded_text = base64.b64encode(text_to_encode.encode()).decode()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, encoded_text)

    def decode_text(self):
        encoded_text = self.text_entry.get()
        decoded_text = base64.b64decode(encoded_text).decode()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, decoded_text)

    def encode_file(self):
        file_path = self.file_entry_button.cget("text")
        with open(file_path, "rb") as file:
            encoded_file = base64.b64encode(file.read())
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, encoded_file.decode())

    def decode_file(self):
        file_path = self.file_entry_button.cget("text")
        encoded_text = self.result_text.get(1.0, tk.END)
        decoded_file = base64.b64decode(encoded_text.encode())
        
        # For image files, display the decoded image
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(BytesIO(decoded_file))
            img.show()

        # You can add similar handling for other file types (e.g., audio, video) if needed.

# Create and run the app
root = tk.Tk()
app = Base64ConverterApp(root)
root.mainloop()
