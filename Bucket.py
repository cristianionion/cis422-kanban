from tkinter import *
from tkinter import ttk

class Bucket:
    def __init__(self, title: str):
        self.title = title

    def append_to(self, root):
        bucketframe = ttk.Frame(root, padding="3 3 12 12")
        bucketframe.grid(column=0, row=0, sticky="nsew")

        title = ttk.Label(bucketframe, text=self.title)
        title.grid(column=0, row=0, sticky="nsew")
