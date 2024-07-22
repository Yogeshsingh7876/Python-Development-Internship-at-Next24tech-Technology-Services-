# Task 1 sample registration from 
import tkinter as tk
from tkinter import messagebox

def submit_fields():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # You can add your own logic to store the user data here
    print("Registration successful!")
    print("Name:", name)
    print("Email:", email)
    print("Age:", age)
    print("Phone:", phone)
    print("Address:", address)
    print("Password:", password)

root = tk.Tk()
root.title("Student Registration Form")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, padx=5, pady=5)
age_entry = tk.Entry(root, width=30)
age_entry.grid(row=2, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=3, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0, padx=5, pady=5)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=4, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=5, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=5, column=1, padx=5, pady=5)

confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.grid(row=6, column=0, padx=5, pady=5)
confirm_password_entry = tk.Entry(root, width=30, show="*")
confirm_password_entry.grid(row=6, column=1, padx=5, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_fields)
submit_button.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()
