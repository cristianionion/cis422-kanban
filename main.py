from tkinter import *
from tkinter import ttk
from database import *
from ProjectSelection import *


boards2Delete = getDeleteTables(conn)
for i in range(len(boards2Delete)):
    deletedeleteBoard(conn,boards2Delete[i][0])

# Creates the root Tkinter window
root = Tk()
root.title("Kanban")

# Generates the Project Selection screen and displays it
ProjectSelection(root).gen().grid(column=0, row=0)

# Starts the Tkinter App
root.mainloop()
