from tkinter import *
from tkinter import ttk

from typing import List

class Bucket:
    def __init__(self, title: str):
        self.title = title

    def gen(self, board):
        bucketframe = ttk.Frame(board, padding="3 3 12 12")

        title = ttk.Label(bucketframe, text=self.title)
        title.grid(column=0, row=0, sticky="nsew")

        return bucketframe
