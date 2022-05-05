from tkinter import *
from tkinter import ttk

class Card:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc

    def append_to(self, bucket):
        cardframe = ttk.Frame(root, padding="3 3 12 12")
        cardframe.grid(column=0, row=0, sticky="nsew")

        title = ttk.Label(cardframe, text=self.title)
        title.grid(column=0, row=0, sticky="nsew")

        desc = ttk.Label(cardframe, text=self.desc)
        desc.grid(column=0, row=1, sticky="nsew")
