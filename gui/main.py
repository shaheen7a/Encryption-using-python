from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

# Create the Tkinter app
app = tk.Tk()
app.title("File Encryption App")

# Change the background color
app.config(bg="#F1F6F9")

# Create a custom font
app_font = ("Helvetica", 12, "bold")

# Set the font for all widgets in the app
app.option_add("*Font", app_font)

#------------------------------------
# Create the key

key_label = tk.Label(app, text="No Key Generated Yet")
key_label.pack(side="top", pady=10)

def generate_key():
    key = Fernet.generate_key()
    with open('enc_key.key', 'wb') as enc_key:
        enc_key.write(key)
    key_label.config(text="Key Generated Successfully", fg="green")

key_button = tk.Button(app, text="Generate Key", command=generate_key)
key_button.pack(side="top", pady=10)

#------------------------------------
#Load the key

load_label = tk.Label(app, text="No Key Loaded Yet")
load_label.pack(side="top", pady=10)

def load_key():
    global key
    file_path = filedialog.askopenfilename(title="Select the key file")
    with open(file_path, 'rb') as enc_key:
        key = enc_key.read()
    load_label.config(text="Key Loaded Successfully", fg="green")

load_button = tk.Button(app, text="Load Key", command=load_key)
load_button.pack(side="top", pady=10)

#------------------------------------
#encryption

encrypt_label = tk.Label(app, text="No File Encrypted Yet")
encrypt_label.pack(side="top", pady=10)

def encrypt_file():
    f = Fernet(key)
    file_path = filedialog.askopenfilename(title="Select a file to encrypt")
    with open(file_path, 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open ('enc_personal_data.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    encrypt_label.config(text="File Encrypted Successfully", fg="green")

encrypt_button = tk.Button(app, text="Encrypt File", command=encrypt_file)
encrypt_button.pack(side="top", pady=10)

#------------------------------------
#Decryption

decrypt_label = tk.Label(app, text="No File Decrypted Yet")
decrypt_label.pack(side="top", pady=10)

def decrypt_file():
    f = Fernet(key)
    file_path = filedialog.askopenfilename(title="Select a file to decrypt")
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('dec_personal_data.csv', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    decrypt_label.config(text="File Decrypted Successfully", fg="green")

decrypt_button = tk.Button(app, text="Decrypt File", command=decrypt_file)
decrypt_button.pack(side="top", pady=10)

# Run the Tkinter app
app.mainloop()
