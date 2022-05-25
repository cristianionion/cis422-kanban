from tkinter import *
from tkinter import ttk

class Card:
    '''
    Represents a task in Kanban. Stores all information related
    to itself and also handles its own rendering.
    '''

    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc
        self.parent = None # A reference to its parent (a bucket)

    def change_parent_to(self, bucket: "Bucket"):
        '''
        Assigns the parent of the Card so that the Card can
        reference it.
        '''
        self.parent = bucket

    def left(self):
        '''
        Moves the Card one bucket to the left.
        '''
        self.parent.shift_left(self)

    def right(self):
        '''
        Moves the Card one bucket to the right.
        '''
        self.parent.shift_right(self)

    def gen(self, bucket):
        '''
        Creates the Tkinter object that can be displayed.
        After being created using this method, it must be gridded
        to the bucket.
        '''
        # The frame that holds the entire Card
        cardframe = ttk.Frame(bucket, padding="4 10 4 10")

        # The style for the title of the Card
        s = ttk.Style()
        s.configure('CardTitle.TLabel',
                     font="Verdana 12",
                     padding="4 4 4 4",
                     foreground='black',
                     background='lightgray',
                     justify='center',
                     relief="groove",
                     )

        # Another frame to store stuff along the top
        header_frame = ttk.Frame(cardframe)
        header_frame.grid(column=0, row=0)

        # The name of the Card
        title = ttk.Label(header_frame, text=self.title, style='CardTitle.TLabel')
        title.grid(column=1, row=0, sticky="nsew")

        # The button to move the Card left
        left_btn = ttk.Button(header_frame, text="<", style='CardTitle.TLabel', command=self.left)
        left_btn.grid(column=0, row=0, sticky="nsew")

        # The button to move the Card right
        right_btn = ttk.Button(header_frame, text=">", style='CardTitle.TLabel', command=self.right)
        right_btn.grid(column=2, row=0, sticky="nsew")

        # The style for the description of the Card
        s.configure('CardDesc.TLabel',
                     font="Verdana 8",
                     padding="4 4 4 4",
                     foreground='black',
                     background='lightgray',
                     justify="center",
                     relief="groove",
                     )

        # The description of the Card
        desc = ttk.Label(cardframe, text=self.desc, style='CardDesc.TLabel')
        desc.grid(column=0, row=1, sticky="nsew")

        # Returns the entire Card
        return cardframe
