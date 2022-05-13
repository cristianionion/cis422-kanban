from tkinter import *
from tkinter import ttk

from Card import *
from Bucket import *
from Board import *

root = Tk()
root.title("Kanban")

b1 = Bucket("Not Started", [])
b2 = Bucket("In Progress", [])
b3 = Bucket("Completed", [])

board = Board(root, "Sprint 1", [b1, b2, b3])
boardholder = board.gen()
boardholder.grid(column=0, row=0)

for b in b1,b2,b3:
    b.change_parent_to(board)

root.mainloop()
