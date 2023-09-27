import tkinter as tk
import string
import random
import pyperclip
from tkinter import messagebox
import json
import os

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager and Generator")
        self.root.geometry("600x400")

        self.password_length = tk.IntVar(value=10)

        self.label_title = tk.Label(self.root, text="Password Manager and Generator", font=("Helvetica", 20))
        self.label_title.pack(pady=10)

        # Password Generator Interface
        self.label_generator_title = tk.Label(self.root, text="Password Generator", font=("Helvetica", 16))
        self.label_generator_title.pack(pady=5)

        self.label_length = tk.Label(self.root, text="Password Length:")
        self.label_length.pack(pady=5)

        self.entry_length = tk.Entry(self.root, textvariable=self.password_length, font=("Arial", 12), width=10)
        self.entry_length.pack(pady=5)

        self.uppercase_var = tk.IntVar(value=1)
        self.lowercase_var = tk.IntVar(value=1)
        self.digits_var = tk.IntVar(value=1)
        self.special_chars_var = tk.IntVar(value=1)

        self.checkbox_uppercase = tk.Checkbutton(self.root, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.checkbox_uppercase.pack(pady=5)

        self.checkbox_lowercase = tk.Checkbutton(self.root, text="Include Lowercase Letters", variable=self.lowercase_var)
        self.checkbox_lowercase.pack(pady=5)

        self.checkbox_digits = tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var)
        self.checkbox_digits.pack(pady=5)

        self.checkbox_special_chars = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.special_chars_var)
        self.checkbox_special_chars.pack(pady=5)

        self.button_generate = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.button_generate.pack(pady=10)

        self.button_copy = tk.Button(self.root, text="Copy Password to Clipboard", command=self.copy_to_clipboard)
        self.button_copy.pack(pady=5)

        self.button_save = tk.Button(self.root, text="Save Password to File", command=self.save_to_file)
        self.button_save.pack(pady=5)

        self.generated_password_var = tk.StringVar()
        self.label_generated_password = tk.Label(self.root, textvariable=self.generated_password_var, font=("Arial", 12))
        self.label_generated_password.pack(pady=5)

        # Password Manager Interface
        self.label_manager_title = tk.Label(self.root, text="Password Manager", font=("Helvetica", 16))
        self.label_manager_title.pack(pady=10)

        self.label_account = tk.Label(self.root, text="Account:")
        self.label_account.pack()

        self.entry_account = tk.Entry(self.root)
        self.entry_account.pack()

        self.label_password = tk.Label(self.root, text="Password:")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.button_add = tk.Button(self.root, text="Add Password", command=self.add_password)
        self.button_add.pack(pady=5)

        self.button_view = tk.Button(self.root, text="View Passwords", command=self.view_passwords)
        self.button_view.pack(pady=5)

        self.button_delete = tk.Button(self.root, text="Delete Password", command=self.delete_password)
        self.button_delete.pack(pady=5)

        self.passwords = {}
        self.load_passwords()

    def generate_password(self):
        password_length = self.password_length.get()
        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_digits = self.digits_var.get()
        include_special_chars = self.special_chars_var.get()

        chars = ""
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_lowercase:
            chars += string.ascii_lowercase
        if include_digits:
            chars += string.digits
        if include_special_chars:
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        generated_password = ''.join(random.choice(chars) for _ in range(password_length))
        self.generated_password_var.set(generated_password)

    def copy_to_clipboard(self):
        password = self.generated_password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copy Successful", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "No password generated yet.")

    def save_to_file(self):
        password = self.generated_password_var.get()
        if password:
            file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(password)
                messagebox.showinfo("Save Successful", "Password saved to file.")
        else:
            messagebox.showerror("Error", "No password generated yet.")

    def load_passwords(self):
        if os.path.exists("passwords.json"):
            with open("passwords.json", "r") as f:
                self.passwords = json.load(f)

    
    def save_passwords(self):
        with open("passwords.json", "w") as f:
            json.dump(self.passwords, f)

    def add_password(self):
        account = self.entry_account.get().strip()
        password = self.entry_password.get().strip()

        if account and password:
            self.passwords[account] = password
            self.save_passwords()
            self.clear_entry_fields()
            messagebox.showinfo("Success", "Password added successfully.")
        else:
            messagebox.showerror("Error", "Account and password fields cannot be empty.")

    def view_passwords(self):
        passwords_text = "\n".join(f"{account}: {password}" for account, password in self.passwords.items())
        messagebox.showinfo("Passwords", passwords_text)

    def delete_password(self):
        account = self.entry_account.get().strip()
        if account in self.passwords:
            del self.passwords[account]
            self.save_passwords()
            self.clear_entry_fields()
            messagebox.showinfo("Success", "Password deleted successfully.")
        else:
            messagebox.showerror("Error", "Account not found.")

    def clear_entry_fields(self):
        self.entry_account.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()