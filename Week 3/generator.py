from tkinter import *
import sqlite3
import csv
import os

window = Tk()
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
lbl = Label(window, text = "Number of traits to generate: ")
lbl.grid(row=0, column=0, padx=10, pady=10, sticky="n")
numberEntryBox = Entry(window, width=10)
numberEntryBox.grid(row=0, column=1, padx=10, pady=10, sticky="n")
status = Label(window, text = "")
status.grid(column=0, row=3)
scrollbar = Scrollbar(window, orient="vertical")





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

window.title("Character trait generator")
window.geometry('800x600')


menu = Menu(window)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='Dice Roller', menu=item)
menu.add_cascade(label='Generators', menu=item)
window.config(menu=menu)





generatedTraitsList = Listbox(window, selectmode = "multiple", yscrollcommand=scrollbar.set)
scrollbar.config(command=generatedTraitsList.yview)
generatedTraitsList.grid(padx = 10, pady = 10, row=2, column=0, columnspan=3, sticky="NSEW")
#scrollbar.grid(row=2, column=4, sticky="nsE")

traits_list = []
traits_number = 1





def clicked():
    res = numberEntryBox.get()
    if res.isnumeric():
        traits_number = res
        status.configure(text = "Retrieved " + res + " records:")
        get_traits(traits_number)
        for i in range(len(traits_list)):
            generatedTraitsList.insert(END, traits_list[i])
            generatedTraitsList.itemconfig(i, bg = "lightgray")
    else:
        status.configure(text = "Error: couldn't parse input")



def get_traits(number):
    data = cursor.execute("SELECT trait FROM traitTable ORDER BY RANDOM() LIMIT(?)", [number])
    #TODO: preserve selected traits
    traits_list.clear()
    for row in data:
        traits_list.append(row[0])

btn = Button(window, text = "Retrieve", fg = "red", command=clicked)

btn.grid(row=0, column=2, sticky="nW")



    
    

#import_button = Button(window, text = "Import table", fg = "red", command=import_table)

#import_button.grid(column=3, row=0)



#yscrollbar.config(command = list.yview)
window.mainloop()
