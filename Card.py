from tkinter import *
from tkinter import ttk

class Card:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc

    def gen(self, bucket):
        cardframe = ttk.Frame(bucket, padding="3 3 12 12")

        title = ttk.Label(cardframe, text=self.title)
        title.grid(column=0, row=0, sticky="nsew")

        desc = ttk.Label(cardframe, text=self.desc)
        desc.grid(column=0, row=1, sticky="nsew")

        return cardframe
