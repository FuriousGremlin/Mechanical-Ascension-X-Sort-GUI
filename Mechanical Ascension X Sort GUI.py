# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import messagebox

# set directory path and filename
directory = "[Filepath]"
all_items_filename = "all_items.txt"
current_items_filename = "current_items.txt"

# create full file paths
all_items_filepath = os.path.join(directory, all_items_filename)
current_items_filepath = os.path.join(directory, current_items_filename)

# read in all items from file if it exists, otherwise create empty list
def load_items(filepath):
    if os.path.isfile(filepath):
        with open(filepath, "r") as f:
            content = f.readlines()
            items = [tuple(line.strip().split(",")) for line in content]
            items = [(name, float(mpu) if mpu else 0.0) for name, mpu in items]
    else:
        items = []
    return items

all_items = load_items(all_items_filepath)


def update_listbox(items=None):
    if items is None:
        items = current_items
    sorted_items = sorted(list(items), key=lambda x: x[1], reverse=True)
    listbox.delete(0, tk.END)
    for item in sorted_items:
        listbox.insert(tk.END, f"{item[0]} - {item[1]}")

# function to save the current items list
def save_current_items():
    sorted_items = sorted(current_items, key=lambda x: x[1], reverse=True)
    with open(current_items_filepath, "w") as f:
        for name, mpu in sorted_items:
            f.write(name + "," + str(mpu) + "\n")


# function to save the all items list
def save_all_items():
    sorted_all_items = sorted(all_items, key=lambda x: x[1], reverse=True)
    with open(all_items_filepath, "w") as f:
        for name, mpu in sorted_all_items:
            f.write(name + "," + str(mpu) + "\n")


# function to switch list shown
def switch_list():
    global current_items
    if current_items is all_items:
        current_items = load_items(current_items_filepath)
        switch_button.config(text="Show All Items")
    else:
        current_items = all_items
        switch_button.config(text="Show Current Items")
    update_listbox(sorted(current_items, key=lambda x: x[1], reverse=True))

# function to reset current items list
def reset_current_items():
    global current_items
    current_items = []
    update_listbox()
    save_current_items()
    with open(current_items_filepath, "w") as f:
        f.write("")




# function to add item to list
def add_item():
    name = name_entry.get()
    mpu = mpu_entry.get()

    # Check if the item already exists in current_items
    if any(name == item[0] for item in current_items):
        messagebox.showerror("Duplicate Item", "Item already exists in the list.")
        return

    # Check if the item exists in all_items and add the mpu value if it exists
    all_item_mpu = None
    for item in all_items:
        if item[0] == name:
            all_item_mpu = item[1]
            break

    if all_item_mpu is not None and not mpu:
        mpu = all_item_mpu

    if name and mpu:
        current_items.append((name, float(mpu)))
        name_entry.delete(0, tk.END)
        mpu_entry.delete(0, tk.END)
        update_listbox(current_items)
        save_current_items()

        # Update all_items list
        all_items.append((name, float(mpu)))
        save_all_items()



all_items = load_items(all_items_filepath)
current_items = load_items(current_items_filepath)

# create GUI
root = tk.Tk()
root.title("MPU Sorter")

# create entry fields
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
mpu_label = tk.Label(root, text="MPU:")
mpu_entry = tk.Entry(root)

# create listbox
current_items = load_items(current_items_filepath)
listbox = tk.Listbox(root)
update_listbox()

# create buttons
add_button = tk.Button(root, text="Add Item", command=add_item)
save_button = tk.Button(root, text="Save Current Items", command=save_current_items)
reset_button = tk.Button(root, text="Reset Current Items", command=reset_current_items)
switch_button = tk.Button(root, text="Switch List", command=switch_list)
quit_button = tk.Button(root, text="Quit", command=root.quit)

# grid entry fields, listbox, and buttons
name_label.grid(row=0, column=0, sticky="W")
name_entry.grid(row=0, column=1)
mpu_label.grid(row=1, column=0, sticky="W")
mpu_entry.grid(row=1, column=1)
listbox.grid(row=2, column=0, columnspan=2, sticky="WE")
add_button.grid(row=3, column=0)
save_button.grid(row=3, column=1)
reset_button.grid(row=4, column=0)
switch_button.grid(row=4, column=1)
quit_button.grid(row=5, column=0, columnspan=2, sticky="WE")

def show_error_message(message):
    messagebox.showerror("Error", message)

root.mainloop()