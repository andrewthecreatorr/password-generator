import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    chars = ""
    
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_nums.get():
        chars += string.digits
    if var_syms.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showerror("Error", "Select at least one character type!")
        return
    
    password = "".join(random.choice(chars) for _ in range(length))
    output_entry.delete(0, tk.END)
    output_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(output_entry.get())
    messagebox.showinfo("Copied!", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")

# Length
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_nums = tk.BooleanVar(value=True)
var_syms = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_upper).pack()
tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lower).pack()
tk.Checkbutton(root, text="Numbers (0-9)", variable=var_nums).pack()
tk.Checkbutton(root, text="Symbols (!@#$)", variable=var_syms).pack()

# Output
tk.Label(root, text="Generated Password:").pack()
output_entry = tk.Entry(root)
output_entry.pack()

# Buttons
tk.Button(root, text="Generate", command=generate_password).pack(pady=5)
tk.Button(root, text="Copy", command=copy_password).pack()

root.mainloop()
