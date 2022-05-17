from tkinter import *
from tkinter import ttk

from Board import *
from Bucket import *

class ProjectSelection:
    def __init__(self, root):
        self.root = root
        self.boards = []
        self.name_field = StringVar()

    def gen(self):
        mainframe = ttk.Frame(self.root)

        login_btn = ttk.Button(mainframe, text="Login")
        login_btn.grid(column=0, row=0)

        name_entry = ttk.Entry(mainframe, text="Name", textvariable=self.name_field)
        name_entry.grid(column=0, row=1)

        add_board_btn = ttk.Button(mainframe, text="Add Board", command=self.add_board)
        add_board_btn.grid(column=1, row=1)

        for i in range(len(self.boards)):
            b = ttk.Button(mainframe, text=self.boards[i], command=lambda: self.enter_board(b))
            b.grid(column=0, row=i+2) 

        return mainframe

    def add_board(self):
        name = self.name_field.get()

        if len(name) > 0:
            self.name_field.set("")
            self.boards.append(name)

            for widget in self.root.grid_slaves():
                widget.grid_forget()

            self.gen().grid(column=0, row=0)

    def enter_board(self, event):
        for widget in self.root.grid_slaves():
            widget.grid_forget()

        buckets = [Bucket("Not Started", []),
                   Bucket("In Progress", []),
                   Bucket("Completed", [])
                   ]

        b = Board(self.root, event["text"], buckets)

        for bucket in buckets:
            bucket.change_parent_to(b)

        b.gen().grid(row=0, column=0)
