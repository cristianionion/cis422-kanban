from tkinter import *
from tkinter import ttk

from typing import List

class Bucket:
    def __init__(self, title: str, cards: List["Card"]):
        self.title = title
        self.cards = cards

    def gen(self, board):
        s = ttk.Style()
        s.configure('Bucket.TFrame',
                     relief="ridge",
                     borderwidth=3,
                     )
        bucketframe = ttk.Frame(board, padding="10 10 10 10", style='Bucket.TFrame')

        s.configure('BucketTitle.TLabel',
                     font="Verdana 14",
                     padding="4 4 4 4",
                     foreground='black',
                     )

        title = ttk.Label(bucketframe, text=self.title, style='BucketTitle.TLabel')
        title.grid(column=0, row=0, sticky="nsew")

        cardholder = ttk.Frame(bucketframe, padding="3 3 12 12")

        for i in range(len(self.cards)):
            cardframe = self.cards[i].gen(cardholder)
            cardframe.grid(column=0, row=i)

        cardholder.grid(column=0, row=1)

        return bucketframe
