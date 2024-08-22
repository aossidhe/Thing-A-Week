import tkinter as tk
from tkinter import ttk



LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Roller, TraitGen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Startpage", font = LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        
        button1 = ttk.Button(self, text="Roller", command = lambda: controller.show_frame(Roller))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Traits Generator", command = lambda: controller.show_frame(TraitGen))
        button2.grid(row=2, column=1, padx=10, pady=10)


class Roller(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Roller", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        
        button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="TraitGen", command = lambda : controller.show_frame(TraitGen))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)



class TraitGen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="TraitGen", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        
        button1 = ttk.Button(self, text ="StartPage", command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Roller", command = lambda : controller.show_frame(Roller))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        
app = tkinterApp()
app.mainloop()