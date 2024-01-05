from tkinter import *
from tkinter.ttk import *
from time import strftime

class Clock:

    def __init__(self):

        self.top = Tk()
        self.top.title("Digital Clock")
        self.lbl = Label(self.top, font=('monaco', 50, 'bold'), background='black', foreground='red')
        self.lbl.pack(anchor='center')
        self.update_time()

        mainloop()

    def update_time(self):
        text = strftime(' %H:%M:%S %p ')
        self.lbl.config(text=text)
        self.lbl.after(1000, self.update_time)

c = Clock()
