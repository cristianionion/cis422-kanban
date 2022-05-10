from tkinter import *
from tkinter import ttk

class Card:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc

    def gen(self, bucket):
        cardframe = ttk.Frame(bucket, padding="4 10 4 10")

        s = ttk.Style()
        s.configure('CardTitle.TLabel',
                     font="Verdana 12",
                     padding="4 4 4 4",
                     foreground='black',
                     background='darkgray',
                     justify='center',
                     relief="groove",
                     )

        title = ttk.Label(cardframe, text=self.title, style='CardTitle.TLabel')
        title.grid(column=0, row=0, sticky="nsew")

        s.configure('CardDesc.TLabel',
                     font="Verdana 8",
                     padding="4 4 4 4",
                     foreground='black',
                     background='darkgray',
                     justify="center",
                     relief="groove",
                     )
        desc = ttk.Label(cardframe, text=self.desc, style='CardDesc.TLabel')
        desc.grid(column=0, row=1, sticky="nsew")

        return cardframe
