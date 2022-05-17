from tkinter import *
from tkinter import ttk

class ProjectSelection:
    def __init__(self, root):
        self.root = root
        self.boards = []

    def gen(self):
        mainframe = ttk.Frame(self.root)

        login_btn = ttk.Button(mainframe, text="Login")
        login_btn.grid(column=0, row=0)

        add_board_btn = ttk.Button(mainframe, text="Add Board", command=self.add_board)
        add_board_btn.grid(column=1, row=0)

        for i in range(len(self.boards)):
            b = ttk.Button(mainframe, text=self.boards[i])
            b.grid(column=0, row=i+1) 

        return mainframe

    def add_board(self):
        self.boards.append("Name")

        for widget in self.root.grid_slaves():
            widget.grid_forget()

        self.gen().grid(column=0, row=0)
