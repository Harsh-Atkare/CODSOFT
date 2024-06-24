import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip  # Import pyperclip for clipboard operations

# Function to generate a random password
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Function to handle button click event for generating password
def generate_password_click():
    global generated_password
    try:
        length = int(entry_password_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return
        
        generated_password = generate_password(length)
        label_password["text"] = "Generated Password: " + generated_password
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Function to handle button click event for copying password to clipboard
def copy_to_clipboard():
    if generated_password:
        pyperclip.copy(generated_password)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showerror("Error", "No password generated yet.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label and entry for password length input
label_length = tk.Label(root, text="Enter Password Length:")
label_length.pack(pady=10)

entry_password_length = tk.Entry(root, width=30)
entry_password_length.pack()

# Create a button to generate password
button_generate = tk.Button(root, text="Generate Password", command=generate_password_click)
button_generate.pack(pady=10)

# Create a label to display generated password
label_password = tk.Label(root, text="")
label_password.pack()

# Create a button to copy generated password to clipboard
button_copy = tk.Button(root, text="Copy Password", command=copy_to_clipboard)
button_copy.pack(pady=10)

# Variable to store generated password globally
generated_password = None

# Run the main event loop
root.mainloop()
