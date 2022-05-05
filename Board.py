from tkinter import *
from tkinter import ttk

from typing import List

class Board:
    def __init__(self, title: str, children: List["Bucket"]):
        self.title = title
        self.children = children

    def append_to(self, root):
        boardframe = ttk.Frame(board, padding="3 3 12 12")
        boardframe.grid(column=0, row=0, sticky="nsew")

        title = ttk.Label(bucketframe, text=self.title)
        title.grid(column=0, row=0, sticky="nsew")

        for i in range(len(children)):
            children[i].grid(column=0, row=i, sticky="nsew")
