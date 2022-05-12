""" 
    


database structure 
    
1 database, each new board/project has its own table
    
new funcs we will need:
    new column/"bucket" function

1 database
each new board/project has its own table
each card is a new row in table:
    will have columns for card's attributes
    will have columns for each bucket
    if a card isn't in that bucket, its column value is Null or False, otherwise is True

"""

import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

def createDatabase(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS kanban")

createDatabase(conn)


def createTable(conn, project):
    conn.database = "kanban"
    cursor = conn.cursor()
    print("CREATE TABLE IF NOT EXISTS "+ str(project)+" (card VARCHAR(2000),card_notes VARCHAR(2000),cards_assignment VARCHAR(2000) )")
    query = "CREATE TABLE IF NOT EXISTS "+ str(project)+" (card VARCHAR(2000),card_notes VARCHAR(2000),cards_assignment VARCHAR(2000))"
    cursor.execute(query)

project = "FakeProject"
createTable(conn, project)

def addCard(conn,project,card,card_notes, cards_assignment):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "INSERT INTO "+str(project)+ " (card,card_notes,cards_assignment) VALUES (%s,%s,%s)"
    vals = (card, card_notes,cards_assignment)
    cursor.execute(query,vals)
    conn.commit()

#addCard(conn,project,"first card","what needs to be done","who is doing it")


def updateCard(conn,project,card,card_notes,cards_assignment):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "UPDATE "+str(project)+" SET card =%s, card_notes =%s, cards_assignment =%s"
    vals = (card,card_notes,cards_assignment)
    cursor.execute(query,vals)
    conn.commit()

#updateCard(conn,project, "first card-updated", "what needs to be done-updated", "who needs to do it-updated")
