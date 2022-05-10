from tkinter import *
from tkinter import ttk

from typing import List

class Board:
    def __init__(self, title: str, buckets: List["bucket"]):
        self.title = title
        self.buckets = buckets

    def gen(self, root):
        boardframe = ttk.Frame(root, padding="3 3 12 12")

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

        bucketholder.grid(column=0, row=1)

        return boardframe
