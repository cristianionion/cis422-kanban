from tkinter import *
from tkinter import ttk

from typing import List
from Card import *
from database import *
import ProjectSelection
import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")


class Board:
    '''
    A Board that represents a Kanban board. It stores all information associated
    with a Board including Buckets and Cards. It also is responsible for creating
    the Tkinter objects that display its information to the user.
    '''

    def __init__(self, root, title: str, buckets: List["bucket"]):
        self.root = root # The root Tkinter object
        self.title = title
        self.buckets = buckets # A list of the Buckets in this Board
        self.new_name = None # Is later used to store the name of a new Card
        self.new_desc = None # Is later used to store the description of a new Card

    def add_card(self):
        '''
        A method that gets called when the add card button is pressed.
        It is used to add a Card to the first Bucket.
        '''

        # Gets the name and description for the new Card
        name = self.new_name.get()
        desc = self.new_desc.get()

        query = "INSERT INTO " +str(self.title).replace(" ","あ")+" (title, description, "

        bins = self.buckets
        binsList = []
        # this creates a string for db query 
        for i in range(len(bins)):
            binsList.append(bins[i].title)
        for i in range(len(binsList)):
            if i == (len(binsList)-1):
                query += binsList[i].replace(" ","あ")+") VALUES ("
            else:
                query += binsList[i].replace(" ","あ")+', '
        for i in range(len(binsList)+2):
            if i == (len(binsList)+1):
                query += "%s)"
            else:
                query += "%s,"
        info = (len(binsList), name, desc)
        print("AHNBSBSBSBSBBSSBAOL<MHKJHO", query, info)
        addCard(conn, query, info)

        # Checks if name and desc are not empty
        if len(name) > 0 and len(desc) > 0:

            # Removes text inside the name and description text boxes
            self.new_name.set("")
            self.new_desc.set("")

            # Creates a new Card and adds it to the Cards list in the first Bucket
            card = Card(name, desc)
            self.buckets[0].add_card(card)

            # Deletes the whole Board's visuals
            for widget in self.root.grid_slaves():
                widget.grid_forget()

            # Redraws the visuals for the whole Board 
            boardholder = self.gen().grid(column=0, row=0)
    
    def delete(self):

        #deleteBoard(conn, self.title)
        createDeleteTable(conn, self.title)
        # Deletes the current frame from root
        for widget in self.root.grid_slaves():
            widget.grid_forget()

        ProjectSelection.ProjectSelection(self.root).gen().grid(column=0, row=0)


    def gen(self):
        '''
        Responsible for creating the Tkinter object that will be used
        to display the Board to the user. This method is recursive. It
        calls the gen method for each Bucket and Card on the Board.
        '''



        # The Frame that stores everything that goes on the Board
        boardframe = ttk.Frame(self.root, padding="3 3 12 12")

        # The style object that is used for the title of the Board
        s = ttk.Style()
        s.configure("BoardTitle.TLabel",
                     font="Verdana 16",
                     )

        # The title of the Board
        title = ttk.Label(boardframe, text=self.title, style="BoardTitle.TLabel")
        title.grid(column=0, row=0, sticky="nsew")

        # The Frame that holds all the Buckets on the Board
        bucketholder = ttk.Frame(boardframe, padding="3 3 12 12")

        # Generates the Tkinter for each of the Boards and adds it to the bucketholder frame
        for i in range(len(self.buckets)):
            bucketframe = self.buckets[i].gen(bucketholder)
            bucketframe.grid(row=0, column=i, sticky="n")

        # Adds the bucketholder frame onto the Board
        bucketholder.grid(column=0, row=2)

        # A variable to hold the current name in name_entry
        name = StringVar()
        self.new_name = name

        # The name text entry box
        name_entry = ttk.Entry(boardframe, textvariable=name)
        name_entry.grid(column=0, row=0, sticky="e")

        # A variable to hold the current description in desc_entry
        desc = StringVar()
        self.new_desc = desc

        # The description text entry box
        desc_entry = ttk.Entry(boardframe, textvariable=desc)
        desc_entry.grid(column=0, row=1, sticky="e")

        # A Button that adds a new Card to the Board
        add_card = ttk.Button(boardframe, text="Add Card", command=self.add_card)
        add_card.grid(column=1, row=0)

        # button to delete the entire board
        delete_board = ttk.Button(boardframe, text="Delete Board",command= lambda : self.delete())
        delete_board.grid(column=1, row=2)

        # Returns the whole Board's visuals
        return boardframe

