import tkinter as tk
from datetime import date
from tkinter import font

# File path for storing the task list
file_path = "task_list.txt"

def add_item(event=None):
    item = entry.get("1.0", tk.END).strip()
    if item:
        listbox.insert(tk.END, item)
        entry.delete("1.0", tk.END)
        save_tasks()

def remove_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks()

def clear_list():
    listbox.delete(0, tk.END)
    save_tasks()

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(file_path, "w") as file:
        file.write("\n".join(tasks))

def load_tasks():
    try:
        with open(file_path, "r") as file:
            tasks = file.read().splitlines()
        for task in tasks:
            listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("Daily Todo List - " + date.today().strftime("%d/%m/%Y"))

# Set the window size
root.geometry("500x300")

# Create a frame
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a listbox with larger font size
listbox_font = font.Font(size=12)  
listbox = tk.Listbox(frame, width=50, font=listbox_font)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create an entry widget with larger font size
entry_font = font.Font(size=16)
entry = tk.Text(root, width=50, font=entry_font, height=1)
entry.pack(pady=(0, 10), padx=10)

# Bind the Enter key to the add_item() function
entry.bind("<Return>", add_item)

# buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=(0, 5))

# Increase the size of the buttons
# Calculate button width based on button_frame width
button_width = int(button_frame.winfo_width() / 3)
# Calculate button height based on button_frame height
button_height = int(button_frame.winfo_height() * 1.5)

# Button properties
button_width = 20
button_height = 2

# Color the backgrounds of the buttons and adjust size
add_button = tk.Button(button_frame, text="Add Item", command=add_item,
                       bg="green", width=button_width, height=button_height)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(button_frame, text="Remove Item", command=remove_item,
                          bg="red", width=button_width, height=button_height)
remove_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear List", command=clear_list,
                         bg="orange", width=button_width, height=button_height)
clear_button.pack(side=tk.LEFT, padx=5)

# Load the tasks from the file
load_tasks()

root.mainloop()