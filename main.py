from tkinter import *
from tkinter import ttk

from ProjectSelection import *

# Creates the root Tkinter window
root = Tk()
root.title("Kanban")

# Generates the Project Selection screen and displays it
ProjectSelection(root).gen().grid(column=0, row=0)

# Starts the Tkinter App
root.mainloop()
