from tkinter import *
from tkinter import ttk

from typing import List
from Card import *

class Bucket:
    def __init__(self, title: str, cards: List["Card"]):
        self.title = title
        self.cards = cards
        self.parent = None

    def change_parent_to(self, board: "Board"):
        self.parent = board

    def shift_left(self, c: "Card"):
        i = self.parent.buckets.index(self)
        j = self.cards.index(c)
        if i >= 1:
            for widget in self.parent.root.grid_slaves():
                widget.grid_forget()

            card = self.cards.pop(j)
            self.parent.buckets[i-1].add_card(card)
            self.parent.gen().grid(column=0, row=0)

    def shift_right(self, c: "Card"):
        i = self.parent.buckets.index(self)
        j = self.cards.index(c)
        if i < len(self.parent.buckets) - 1:
            for widget in self.parent.root.grid_slaves():
                widget.grid_forget()

            card = self.cards.pop(j)
            self.parent.buckets[i+1].add_card(card)
            self.parent.gen().grid(column=0, row=0)

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

    def add_card(self, c: "Card"):
        c.change_parent_to(self)
        self.cards.append(c)
