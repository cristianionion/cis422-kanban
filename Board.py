from tkinter import *
from tkinter import ttk

from typing import List
from Card import *

class Board:
    def __init__(self, root, title: str, buckets: List["bucket"]):
        self.root = root
        self.title = title
        self.buckets = buckets
        self.new_name = None

    def gen(self):
        boardframe = ttk.Frame(self.root, padding="3 3 12 12")

        s = ttk.Style()
        s.configure("BoardTitle.TLabel",
                     font="Verdana 16",
                     )

        title = ttk.Label(boardframe, text=self.title, style="BoardTitle.TLabel")
        title.grid(column=0, row=0, sticky="nsew")

        bucketholder = ttk.Frame(boardframe, padding="3 3 12 12")

        for i in range(len(self.buckets)):
            bucketframe = self.buckets[i].gen(bucketholder)
            bucketframe.grid(row=0, column=i, sticky="n")

        bucketholder.grid(column=0, row=2)

        name = StringVar()
        name_entry = ttk.Entry(boardframe, textvariable=name)
        name_entry.grid(column=0, row=0, sticky="e")
        self.new_name = name

        desc = StringVar()
        desc_entry = ttk.Entry(boardframe, textvariable=desc)
        desc_entry.grid(column=0, row=1, sticky="e")
        self.new_desc = desc

        add_card = ttk.Button(boardframe, text="Add Card", command=self.add_card)
        add_card.grid(column=1, row=0)

        return boardframe

    def add_card(self):
        name = self.new_name.get()
        desc = self.new_desc.get()

        if len(name) > 0 and len(desc) > 0:
            self.new_name.set("")
            self.new_desc.set("")

            card = Card(name, desc)
            self.buckets[0].add_card(card)

            for widget in self.root.grid_slaves():
                widget.grid_forget()

            boardholder = self.gen()
            boardholder.grid(column=0, row=0)
