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
        if self.title == "Not Started":
            s.configure('RedBucket.TFrame',
                         relief="ridge",
                         borderwidth=3,
                         background='#f5b8be'
                         )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='RedBucket.TFrame')
        elif self.title == "In Progress":
            s.configure('YellowBucket.TFrame',
                        relief="ridge",
                        borderwidth=3,
                        background='#f4f5b8'
                        )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='YellowBucket.TFrame')
        elif self.title == "Completed":
            s.configure('GreenBucket.TFrame',
                        relief="ridge",
                        borderwidth=3,
                        background='#d1f5b8'
                        )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='GreenBucket.TFrame')
        else:
            s.configure('WhiteBucket.TFrame',
                        relief="ridge",
                        borderwidth=3,
                        background='white'
                        )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='WhiteBucket.TFrame')



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
