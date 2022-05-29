from tkinter import *
from tkinter import ttk
import mysql.connector

from typing import List
from Card import *
from database import *

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")


class Bucket:
    '''
    Represents a column in Kanban. Holds all data associated with itself
    and is also responsible for creating the Tkinter object that is
    displayed to the user.
    '''

    def __init__(self, title: str, cards: List["Card"]):
        self.title = title
        self.cards = cards # A list of the cards that this Bucket stores
        self.parent = None # A reference to the parent object (a Board object)

    def change_parent_to(self, board: "Board"):
        '''
        Assigns a Board as the parent of this Bucket.
        '''
        self.parent = board

    def shift_left(self, c: "Card"):
        '''
        Takes a Card and moves it one bucket to the left.
        '''
        i = self.parent.buckets.index(self) # The position of this Bucket on the Board
        j = self.cards.index(c) # The position of the given Card in the Cards list

        # Check to see if there's room to move left
        if i >= 1:

            # Delete all Tkinter objects so we can redraw them
            for widget in self.parent.root.grid_slaves():
                widget.grid_forget()

            card = self.cards.pop(j) # Get the Card out of the list of Cards
            self.parent.buckets[i-1].add_card(card) # Add the Card in its new position

            self.parent.gen().grid(column=0, row=0) # Redraw the Board


            bins = self.parent.buckets
            binsList = []
            for bin in range(len(bins)):
                binsList.append(bins[bin].title)
            oldLoc = self.title
            newLoc = binsList[i-1]
            cardMoved(conn,self.parent.title,card.title,oldLoc,newLoc)

    def shift_right(self, c: "Card"):
        '''
        Takes a Card and moves it one bucket to the right.
        '''
        i = self.parent.buckets.index(self) # The position of this Bucket on the Board
        j = self.cards.index(c) # The position of the given Card in the Cards list

        # Check to see if there's room to move right
        if i < len(self.parent.buckets) - 1:

            # Delete all Tkinter objects so we can redraw them
            for widget in self.parent.root.grid_slaves():
                widget.grid_forget()

            card = self.cards.pop(j) # Get the Card out of the list of Cards
            self.parent.buckets[i+1].add_card(card) # Add the Card in its new position

            self.parent.gen().grid(column=0, row=0) # Redraw the Board


            
            bins = self.parent.buckets
            binsList = []
            for bin in range(len(bins)):
                binsList.append(bins[bin].title)
            oldLoc = self.title
            newLoc = binsList[i+1]
            cardMoved(conn,self.parent.title,card.title,oldLoc,newLoc)

    def add_card(self, c: "Card"):
        '''
        Adds a Card to the list of Cards
        '''
        c.change_parent_to(self) # Changes the parent of the Card to this Bucket
        self.cards.append(c)

    def gen(self, board):
        '''
        Creates the Tkinter object for the Bucket. After it is returned,
        it must be gridded onto the Board.
        '''

        s = ttk.Style()

        # Adds a red background to the Not Started Bucket
        if self.title == "Not Started":
            s.configure('RedBucket.TFrame',
                         relief="ridge",
                         borderwidth=3,
                         background='#f5b8be'
                         )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='RedBucket.TFrame')

        # Adds a yellow background to the Not Started Bucket
        elif self.title == "In Progress":
            s.configure('YellowBucket.TFrame',
                        relief="ridge",
                        borderwidth=3,
                        background='#f4f5b8'
                        )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='YellowBucket.TFrame')

        # Adds a green background to the Not Started Bucket
        elif self.title == "Completed":
            s.configure('GreenBucket.TFrame',
                        relief="ridge",
                        borderwidth=3,
                        background='#d1f5b8'
                        )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='GreenBucket.TFrame')

        # Adds a white background for all other Buckets
        else:
            s.configure('WhiteBucket.TFrame',
                        relief="ridge",
                        borderwidth=3,
                        background='white'
                        )
            bucketframe = ttk.Frame(board, padding="10 10 10 10", style='WhiteBucket.TFrame')

        # Configures the style for the Bucket Title
        s.configure('BucketTitle.TLabel',
                     font="Verdana 14",
                     padding="4 4 4 4",
                     foreground='black',
                     )

        # The Bucket title
        title = ttk.Label(bucketframe, text=self.title, style='BucketTitle.TLabel')
        title.grid(column=0, row=0, sticky="nsew")

        # A Frame to hold the Cards
        cardholder = ttk.Frame(bucketframe, padding="3 3 12 12")

        # Adds each Card to the cardholder Frame
        for i in range(len(self.cards)):
            cardframe = self.cards[i].gen(cardholder)
            cardframe.grid(column=0, row=i)

        # Adds the cardholder onto the Bucket
        cardholder.grid(column=0, row=1)

        # Returns the entire Bucket
        return bucketframe
