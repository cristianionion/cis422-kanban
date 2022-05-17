from tkinter import *
from tkinter import ttk

from ProjectSelection import *

root = Tk()
root.title("Kanban")

ProjectSelection(root).gen().grid(column=0, row=0)

root.mainloop()
