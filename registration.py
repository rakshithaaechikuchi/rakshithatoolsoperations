import tkinter as tk
from tkinter import messagebox

def submit_form():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    # You can add validation and processing here
    if username and password and email:
        messagebox.showinfo("Registration Successful", f"Welcome, {username}!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry fields
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Register", command=submit_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
