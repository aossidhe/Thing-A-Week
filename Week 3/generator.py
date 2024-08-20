from tkinter import *
import sqlite3

window = Tk()

window.title("Character trait generator")
window.geometry('800x600')

menu = Menu(window)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='Dice Roller', menu=item)
menu.add_cascade(label='Generators', menu=item)
window.config(menu=menu)

lbl = Label(window, text = "Number of traits to generate: ")
lbl.grid()
txt = Entry(window, width=10)
txt.grid(column=1, row=0, padx=10, pady=10)
status = Label(window, text = "")
status.grid(column=0, row=2)

list = Listbox(window, selectmode = "multiple")

list.grid(padx = 10, pady = 10, columnspan=50, sticky=EW)

traits_list = []
traits_number = 1

connection = sqlite3.connect('data')
cursor = connection.cursor()



def clicked():
    res = txt.get()
    if res.isnumeric():
        traits_number = res
        status.configure(text = "Retrieved " + res + " records:")
        get_traits(traits_number)
        for i in range(len(traits_list)):
            list.insert(END, traits_list[i])
            list.itemconfig(i, bg = "lightgray")
    else:
        status.configure(text = "Error: couldn't parse input")



def get_traits(number):
    data = cursor.execute("SELECT trait FROM traits ORDER BY RANDOM() LIMIT(?)", [number])
    #TODO: preserve selected traits
    traits_list.clear()
    for row in data:
        traits_list.append(row[0])

btn = Button(window, text = "Click me", fg = "red", command=clicked)

btn.grid(column=2, row=0)

#yscrollbar.config(command = list.yview)
window.mainloop()
