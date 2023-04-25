# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 19:06:04 2023

@author: Thomas
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

class Item:
    def __init__(self, name, length, width, multiplier, status_effect, can_cleanse, mpu, buffed_by, cleansable_effects, use_limit, diminishing_rate, conveyor_height, item_type):
        self.name = name
        self.length = length
        self.width = width
        self.multiplier = multiplier
        self.status_effect = status_effect
        self.can_cleanse = can_cleanse
        self.mpu = mpu
        self.buffed_by = buffed_by
        self.use_limit = use_limit
        self.diminishing_rate = diminishing_rate
        self.item_type = item_type


def save_item(item):
    with open("items.txt", "a") as file:
        file.write(json.dumps(item.__dict__) + "\n")

def load_items():
    items = []
    try:
        with open("items.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                item_data = json.loads(line.strip())
                item = Item(**item_data)
                items.append(item)
    except FileNotFoundError:
        pass
    return items

def add_item():
    name = name_entry.get()
    length = float(length_entry.get())
    width = float(width_entry.get())
    multiplier = float(multiplier_entry.get())
    status_effect = status_effect_entry.get()
    can_cleanse = can_cleanse_var.get()
    buffed_by = buffed_by_entry.get()
    mpu = multiplier ** (1 / length)
    cleansable_effects = cleansable_effects_entry.get() if can_cleanse_var.get() else ""
    use_limit = int(use_limit_entry.get()) if not unlimited_uses_var.get() else -1
    diminishing_rate = float(diminishing_rate_entry.get()) if unlimited_uses_var.get() else 0
    conveyor_height = conveyor_height_combobox.get()
    item_type = item_type_combobox.get()

    existing_items = load_items()
    for item in existing_items:
        if item.name == name:
            messagebox.showerror("Error", "An item with the same name already exists.")
            return

    item = Item(name, length, width, multiplier, status_effect, can_cleanse, mpu, buffed_by, cleansable_effects, use_limit, diminishing_rate, conveyor_height, item_type)
    save_item(item)
    messagebox.showinfo("Success", "Item added successfully.")



def sort_items():
    items = load_items()
    sort_key = sort_var.get()
    
    if sort_key == "MPU":
        items.sort(key=lambda x: x.mpu, reverse=True)
    elif sort_key == "Multiplier":
        items.sort(key=lambda x: x.multiplier, reverse=True)
        
    sorted_items.delete(1.0, tk.END)
    for item in items:
        sorted_items.insert(tk.END, f"{item.name} (MPU: {item.mpu:.2f}, Multiplier: {item.multiplier:.2f})\n")

def reset_items():
    confirm_reset = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the item list?")

    if confirm_reset:
        with open("items.txt", "w") as file:
            file.write("")
        messagebox.showinfo("Success", "The item list has been reset.")

def toggle_cleansable_effects():
    if can_cleanse_var.get():
        cleansable_effects_label.grid(row=8, column=0, sticky=tk.W)
        cleansable_effects_entry.grid(row=8, column=1, sticky=tk.W)
    else:
        cleansable_effects_label.grid_remove()
        cleansable_effects_entry.grid_remove()

def toggle_diminishing_rate():
    if unlimited_uses_var.get():
        diminishing_rate_label.grid(row=11, column=0, sticky=tk.W)
        diminishing_rate_entry.grid(row=11, column=1, sticky=tk.W)
    else:
        diminishing_rate_label.grid_remove()
        diminishing_rate_entry.grid_remove()

def update_item_name():
    if max_value_var.get():
        item_name = name_entry.get() + " (max)"
        name_entry.delete(0, tk.END)
        name_entry.insert(0, item_name)
    else:
        item_name = name_entry.get().replace(" (max)", "")
        name_entry.delete(0, tk.END)
        name_entry.insert(0, item_name)

root = tk.Tk()
root.title("Mechanical Ascension X Item Manager")

# Input form
form_frame = ttk.Frame(root, padding="10")
form_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

name_label = ttk.Label(form_frame, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(form_frame)
name_entry.grid(row=0, column=1, sticky=tk.W)

max_value_label = ttk.Label(form_frame, text="Max Value:")
max_value_label.grid(row=0, column=2, sticky=tk.W)
max_value_var = tk.BooleanVar()
max_value_check = ttk.Checkbutton(form_frame, variable=max_value_var, command=update_item_name)
max_value_check.grid(row=0, column=3, sticky=tk.W)

length_label = ttk.Label(form_frame, text="Length:")
length_label.grid(row=1, column=0, sticky=tk.W)
length_entry = ttk.Entry(form_frame)
length_entry.grid(row=1, column=1, sticky=tk.W)

width_label = ttk.Label(form_frame, text="Width:")
width_label.grid(row=2, column=0, sticky=tk.W)
width_entry = ttk.Entry(form_frame)
width_entry.grid(row=2, column=1, sticky=tk.W)

multiplier_label = ttk.Label(form_frame, text="Multiplier:")
multiplier_label.grid(row=3, column=0, sticky=tk.W)
multiplier_entry = ttk.Entry(form_frame)
multiplier_entry.grid(row=3, column=1, sticky=tk.W)

status_effect_label = ttk.Label(form_frame, text="Status Effect:")
status_effect_label.grid(row=4, column=0, sticky=tk.W)
status_effect_entry = ttk.Entry(form_frame)
status_effect_entry.grid(row=4, column=1, sticky=tk.W)

buffed_by_label = ttk.Label(form_frame, text="Buffed by:")
buffed_by_label.grid(row=6, column=0, sticky=tk.W)
buffed_by_entry = ttk.Entry(form_frame)
buffed_by_entry.grid(row=6, column=1, sticky=tk.W)

can_cleanse_label = ttk.Label(form_frame, text="Can Cleanse:")
can_cleanse_label.grid(row=7, column=0, sticky=tk.W)
can_cleanse_var = tk.BooleanVar()
can_cleanse_check = ttk.Checkbutton(form_frame, variable=can_cleanse_var, command=toggle_cleansable_effects)
can_cleanse_check.grid(row=7, column=1, sticky=tk.W)

cleansable_effects_label = ttk.Label(form_frame, text="Cleansable Effects:")
cleansable_effects_entry = ttk.Entry(form_frame)

use_limit_label = ttk.Label(form_frame, text="Use Limit:")
use_limit_label.grid(row=9, column=0, sticky=tk.W)
use_limit_entry = ttk.Entry(form_frame)
use_limit_entry.grid(row=9, column=1, sticky=tk.W)

unlimited_uses_label = ttk.Label(form_frame, text="Unlimited Uses:")
unlimited_uses_label.grid(row=10, column=0, sticky=tk.W)
unlimited_uses_var = tk.BooleanVar()
unlimited_uses_check = ttk.Checkbutton(form_frame, variable=unlimited_uses_var, command=toggle_diminishing_rate)
unlimited_uses_check.grid(row=10, column=1, sticky=tk.W)

diminishing_rate_label = ttk.Label(form_frame, text="Diminishing Rate:")
diminishing_rate_entry = ttk.Entry(form_frame)

conveyor_height_label = ttk.Label(form_frame, text="Conveyor Height:")
conveyor_height_label.grid(row=12, column=0, sticky=tk.W)
conveyor_height_combobox = ttk.Combobox(form_frame, values=["Low", "Mid", "High"], state="readonly")
conveyor_height_combobox.grid(row=12, column=1, sticky=tk.W)
conveyor_height_combobox.current(0)

item_type_label = ttk.Label(form_frame, text="Item Type:")
item_type_label.grid(row=13, column=0, sticky=tk.W)
item_type_combobox = ttk.Combobox(form_frame, values=["Mine", "Processor", "Upgrader", "Portable", "Static"], state="readonly")
item_type_combobox.grid(row=13, column=1, sticky=tk.W)
item_type_combobox.current(0)

add_button = ttk.Button(form_frame, text="Add Item", command=add_item)
add_button.grid(row=14, columnspan=2, sticky=(tk.W, tk.E))

# Sorting options
sort_frame = ttk.Frame(root, padding="10")
sort_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))


sort_label = ttk.Label(sort_frame, text="Sort by:")
sort_label.grid(row=0, column=0, sticky=tk.W)
sort_var = tk.StringVar(value="MPU")
sort_mpu = ttk.Radiobutton(sort_frame, text="MPU", variable=sort_var, value="MPU")
sort_mpu.grid(row=0, column=1, sticky=tk.W)
sort_multiplier = ttk.Radiobutton(sort_frame, text="Multiplier", variable=sort_var, value="Multiplier")
sort_multiplier.grid(row=0, column=2, sticky=tk.W)

sort_button = ttk.Button(sort_frame, text="Sort Items", command=sort_items)
sort_button.grid(row=0, column=3, sticky=(tk.W, tk.E))

# Sorted items display
sorted_items_label = ttk.Label(root, text="Sorted Items:")
sorted_items_label.grid(row=2, column=0, sticky=(tk.W, tk.E))

sorted_items = tk.Text(root, wrap=tk.WORD, width=50, height=10)
sorted_items.grid(row=3, column=0, sticky=(tk.W, tk.E))

# Reset Button
reset_button = ttk.Button(sort_frame, text="Reset List", command=reset_items)
reset_button.grid(row=0, column=4, sticky=(tk.W, tk.E))

root.mainloop()
