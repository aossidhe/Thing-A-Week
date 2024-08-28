import csv
import os
import sqlite3
import tkinter as tk
from tkinter import *

LARGEFONT =("Verdana", 35)

# Create table if necessary and connect to it
generator_directory = os.path.dirname(os.path.abspath(__file__))
connection = sqlite3.connect(os.path.join(generator_directory, 'data'))
cursor = connection.cursor()
table_def = '''CREATE TABLE IF NOT EXISTS traitTable(trait TEXT NOT NULL, tags TEXT, conflicts TEXT, modifier TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT);'''
cursor.execute(table_def)
tsv_filename = os.path.join(generator_directory, 'traits.tsv')
tsv_file = open(tsv_filename)
tsv_contents = csv.reader(tsv_file, delimiter="\t")
insert_query = "INSERT INTO traitTable (trait, tags, conflicts, modifier) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_query, tsv_contents)

window = Tk()
window.title("D&D Helper")
window.geometry('800x600')

menu = Menu(window)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='Dice Roller', menu=item)
menu.add_cascade(label='Generators', menu=item)
window.config(menu=menu)

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(3, minsize=800, weight=1)

list_traitsbox = tk.Listbox(window, selectmode="multiple")
array_traits = []
array_deleted_traits = []
array_recovered_traits = []
traits_to_retrieve = 1
frame_buttons = tk.Frame(window)

# Functions

def recover(deleted_listbox):
    array_recovery = deleted_listbox.curselection()
    print("recovering:")
    print(deleted_listbox)
    for row in array_recovery:
        array_traits.append(array_deleted_traits[row])
        list_traitsbox.insert(END, array_deleted_traits[row])
        print(array_deleted_traits[row])
    print('Traits array:')
    print(array_traits)
    for trait in array_recovery[::-1]:
        #print(trait)
        #print(list_traitsbox.get(trait))
        deleted_listbox.delete(trait)


def show_deleted_window():
    array_recovered_traits.clear()
    deleted_window = Toplevel(window)
    deleted_window.title("Select traits to re-add")
    deleted_window.geometry("600x600")
    deleted_window.rowconfigure(0, weight=1)
    deleted_window.columnconfigure(0, weight=1)
    deleted_listbox = tk.Listbox(deleted_window, selectmode="multiple")
    for i in range(len(array_deleted_traits)):
        deleted_listbox.insert(END, array_deleted_traits[i])
    deleted_listbox.grid(row=0, column=0, sticky="nsew")

    btn_deleted_recover = tk.Button(deleted_window, text="Recover selected", command= lambda: recover(deleted_listbox))
    btn_deleted_recover.grid(column=0, row=1)

def clicked():
    res = entry_num.get()
    if res.isnumeric():
        traits_to_retrieve = res
        #status.configure(text = "Retrieved " + res + " records:")
        get_traits(traits_to_retrieve)
        for i in range(len(array_traits)):
            list_traitsbox.insert(END, array_traits[i])
            #list_traitsbox.itemconfig(i, bg = "lightgray")
    else:
        #status.configure(text = "Error: couldn't parse input")
        1==1

def get_traits(number):
    data = cursor.execute("SELECT trait FROM traits ORDER BY RANDOM() LIMIT(?)", [number])
    array_traits.clear()
    for row in data:
        array_traits.append(row[0])

def remove_selected_traits():
    selected_traits = list_traitsbox.curselection()
    #print(selected_traits)
    for trait in selected_traits[::-1]:
        #print(trait)
        #print(list_traitsbox.get(trait))
        array_deleted_traits.append(list_traitsbox.get(trait))
        list_traitsbox.delete(trait)
    #print(array_deleted_traits)

def clear_traits():
    list = list_traitsbox.get(0, END)
    for trait in list:
        array_deleted_traits.append(trait)
    # array_deleted_traits.append(list)
    #print(array_deleted_traits)
    list_traitsbox.delete(0, END)

def increment():
    num = int(entry_num.get())
    entry_num.delete(0,END)
    if(num >= 0):
        entry_num.insert(0, num+1)
    else:
        entry_num.insert(0, "0")

def decrement():
    num = int(entry_num.get())
    entry_num.delete(0,END)
    if(num > 0):
        entry_num.insert(0, num-1)
    else:
        entry_num.insert(0, "0")

# Buttons for number of traits to retrieve
frame_values = tk.Frame(frame_buttons, background="green")
btn_retrieve = tk.Button(frame_buttons, text="Retrieve", command=clicked)
btn_dec = tk.Button(frame_values, text="-", command=decrement)
entry_num = Entry(frame_values)
entry_num.insert(0, "10")
btn_inc = tk.Button(frame_values, text="+", command=increment)
lbl_status = tk.Label(frame_values, text="")


# Deleted window buttons
lbl_choose_deleted = tk.Label()
btn_show_deleted = tk.Button(frame_buttons, text="Recover deleted traits", command=show_deleted_window)

# Other buttons
btn_save = tk.Button(frame_buttons, text="Generate")
btn_remove = tk.Button(frame_buttons, text="Remove selected traits", command=remove_selected_traits)
btn_clear = tk.Button(frame_buttons, text="Clear all traits", command=clear_traits)

# Arrange
btn_retrieve.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# Arrange retrieval numbers
frame_values.grid(row=1, column=0, sticky="ew", padx=5)
btn_dec.grid(row=0, column=0, sticky="ew", padx=5)
entry_num.grid(row=0, column=1, sticky="ew", padx=5)
btn_inc.grid(row=0, column=2, sticky="ew", padx=5)
#lbl_status.grid(row=1, column=0, columnspan=3, sticky="ew")

# Arrange other buttons
btn_remove.grid(row=2, column=0, sticky="ew", padx=5)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5)
frame_buttons.grid(row=0, column=0, sticky="ns")
btn_show_deleted.grid(row=4, column=0, sticky="ew", padx=5)

list_traitsbox.grid(row=0, column=3, sticky="nsew")








window.mainloop()