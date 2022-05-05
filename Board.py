from tkinter import *
from tkinter import ttk

from typing import List

class Board:
    def __init__(self, title: str):
        self.title = title

    def gen(self, root):
        boardframe = ttk.Frame(root, padding="3 3 12 12")

        title = ttk.Label(boardframe, text=self.title)
        title.grid(column=0, row=0, sticky="nsew")

        return boardframe
