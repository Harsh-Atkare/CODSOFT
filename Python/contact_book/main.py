import tkinter as tk
from tkinter import messagebox

# Contact class to store contact details
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        new_contact = Contact(name, phone, email, address)
        contacts.append(new_contact)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Name and Phone number are required.")

# Function to update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact.name} | {contact.phone}")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to search for contacts
def search_contact():
    search_term = search_entry.get()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            contact_listbox.insert(tk.END, f"{contact.name} | {contact.phone}")

# Function to get selected contact index
def get_selected_contact_index():
    try:
        return contact_listbox.curselection()[0]
    except IndexError:
        return None

# Function to populate entry fields with selected contact details
def populate_entries(event):
    selected_index = get_selected_contact_index()
    if selected_index is not None:
        selected_contact = contacts[selected_index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, selected_contact.name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, selected_contact.phone)
        email_entry.delete(0, tk.END)
        email_entry.insert(0, selected_contact.email)
        address_entry.delete(0, tk.END)
        address_entry.insert(0, selected_contact.address)

# Function to update selected contact details
def update_contact():
    selected_index = get_selected_contact_index()
    if selected_index is not None:
        contacts[selected_index].name = name_entry.get()
        contacts[selected_index].phone = phone_entry.get()
        contacts[selected_index].email = email_entry.get()
        contacts[selected_index].address = address_entry.get()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "No contact selected.")

# Function to delete selected contact
def delete_contact():
    selected_index = get_selected_contact_index()
    if selected_index is not None:
        del contacts[selected_index]
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Selection Error", "No contact selected.")

# Initialize the main window
root = tk.Tk()
root.title("Contact Book")

# Contact list
contacts = []

# Create the main interface
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
contact_listbox.bind('<<ListboxSelect>>', populate_entries)

tk.Label(root, text="Search").grid(row=6, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1, padx=10, pady=5)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=7, column=0, columnspan=2, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=8, column=0, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=8, column=1, pady=10)

# Run the main loop
root.mainloop()
