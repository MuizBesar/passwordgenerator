import random
import string
import pyperclip
import tkinter as tk

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_length_input(*args):
    value = length_var.get()
    if value.isdigit() or value == "":
        generate_button.config(state=tk.NORMAL)
    else:
        generate_button.config(state=tk.DISABLED)

def generate_button_clicked():
    length = int(length_var.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_special_chars = special_chars_var.get()

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
    if password:
        generated_password_label.config(text=password)
        copy_button.config(state=tk.NORMAL, text="Copy to Clipboard", command=lambda: copy_to_clipboard(password))

def copy_to_clipboard(password):
    pyperclip.copy(password)
    copy_button.config(text="Copied!")

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Create the widgets
length_label = tk.Label(window, text="Password Length:")
length_var = tk.StringVar()
length_entry = tk.Entry(window, textvariable=length_var)
length_entry.config(validate="key")
length_entry.config(validatecommand=(window.register(validate_length_input), "%P"))
length_label.pack()
length_entry.pack()

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var)
lowercase_check = tk.Checkbutton(window, text="Include Lowercase Letters", variable=lowercase_var)
numbers_check = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
special_chars_check = tk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)

uppercase_check.pack()
lowercase_check.pack()
numbers_check.pack()
special_chars_check.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_button_clicked, state=tk.DISABLED)
generate_button.pack()

generated_password_label = tk.Label(window, text="")
generated_password_label.pack()

copy_button = tk.Button(window, text="Copy to Clipboard", state=tk.DISABLED)
copy_button.pack()

# Start the main event loop
window.mainloop()

