from tkinter import *
from tkinter import ttk

from Card import *
from Bucket import *
from Board import *

root = Tk()
root.title("Kanban")

board = Board("Sprint 1")
tk_board = board.gen(root)
tk_board.grid(column=0, row=0)

b1 = Bucket("Not Started")
tk_b1 = b1.gen(tk_board)
tk_b1.grid(column=0, row=0, sticky="n")

c1 = Card("Card 1", "Description 1")
tk_c1 = c1.gen(tk_b1)
tk_c1.grid(column=0, row=1)

c2 = Card("Card 2", "Description 2")
tk_c2 = c2.gen(tk_b1)
tk_c2.grid(column=0, row=2)

b2 = Bucket("In Progress")
tk_b2 = b2.gen(tk_board)
tk_b2.grid(column=1, row=0, sticky="n")

c3 = Card("Card 3", "Description 3")
tk_c3 = c3.gen(tk_b2)
tk_c3.grid(column=0, row=1)

b3 = Bucket("Completed")
tk_b3 = b3.gen(tk_board)
tk_b3.grid(column=2, row=0, sticky="n")

root.mainloop()
