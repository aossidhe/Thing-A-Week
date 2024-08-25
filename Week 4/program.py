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
traits_to_retrieve = 1
frm_buttons = tk.Frame(window, bd=2)

# Functions

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

def clear_traits():
    selected_traits = list_traitsbox.curselection()
    #print(selected_traits)
    for trait in selected_traits[::-1]:
        #print(trait)
        #print(list_traitsbox.get(trait))
        array_deleted_traits.append(list_traitsbox.get(trait))
        list_traitsbox.delete(trait)
    print(array_deleted_traits)

def increment():
    #TODO: add function
    1==1


# Buttons for number of traits to retrieve
val_frame = tk.Frame(frm_buttons, bd=1, background="green")
btn_retrieve = tk.Button(frm_buttons, text="Retrieve", command=clicked)
btn_dec = tk.Button(val_frame, text="-")
entry_num = Entry(val_frame)
btn_inc = tk.Button(val_frame, text="+")
lbl_status = tk.Label(val_frame, text="")

# Other buttons
btn_save = tk.Button(frm_buttons, text="Generate")
btn_clear = tk.Button(frm_buttons, text="Clear", command=clear_traits)
btn_four = tk.Button(frm_buttons, text="Options")

# Arrange
btn_retrieve.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# Arrange retrieval numbers
val_frame.grid(row=1, column=0, sticky="ew", padx=5)
btn_dec.grid(row=0, column=0, sticky="ew", padx=5)
entry_num.grid(row=0, column=1, sticky="ew", padx=5)
btn_inc.grid(row=0, column=2, sticky="ew", padx=5)
#lbl_status.grid(row=1, column=0, columnspan=3, sticky="ew")

# Arrange other buttons
btn_clear.grid(row=2, column=0, sticky="ew", padx=5)
btn_four.grid(row=3, column=0, sticky="ew", padx=5)
frm_buttons.grid(row=0, column=0, sticky="ns")

list_traitsbox.grid(row=0, column=3, sticky="nsew")








window.mainloop()