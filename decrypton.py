from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

def generate_key():
    key = Fernet.generate_key()
    with open("decrypton_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("decrypton_key.key", "rb").read()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

try:
    key = load_key()
except FileNotFoundError:
    print("Key not found... Generating new key...")
    generate_key()
    key = load_key()

root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()

mode = input("Choose one:\n1. Encyption\n2. Decrypion\n")
if mode == "1":
    encrypt_file(filename, key)
    print("File has been encrypted.")
elif mode == "2":
    decrypt_file(filename, key)
    print("File has been decrypted.")
else:
    print("choose 1 or 2")
