from tkinter import *
from tkinter import ttk

from Card import *
from Bucket import *
from Board import *

root = Tk()
root.title("Kanban")

c1 = Card("Card 1", "Description 1")
c2 = Card("Card 2", "Description 2")
c3 = Card("Card 3", "Description 3")

b1 = Bucket("Not Started", [c1, c2])
b2 = Bucket("In Progress", [c3])
b3 = Bucket("Completed", [])

board = Board(root, "Sprint 1", [b1, b2, b3])
boardholder = board.gen()
boardholder.grid(column=0, row=0)

root.mainloop()
