from tkinter import *
from tkinter import ttk

class Card:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc
        self.parent = None

    def change_parent_to(self, bucket: "Bucket"):
        self.parent = bucket

    def left(self):
        self.parent.shift_left(self)

    def right(self):
        self.parent.shift_right(self)

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

        header_frame = ttk.Frame(cardframe)
        header_frame.grid(column=0, row=0)

        title = ttk.Label(header_frame, text=self.title, style='CardTitle.TLabel')
        title.grid(column=1, row=0, sticky="nsew")

        left_btn = ttk.Button(header_frame, text="<", style='CardTitle.TLabel', command=self.left)
        left_btn.grid(column=0, row=0, sticky="nsew")

        right_btn = ttk.Button(header_frame, text=">", style='CardTitle.TLabel', command=self.right)
        right_btn.grid(column=2, row=0, sticky="nsew")

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
