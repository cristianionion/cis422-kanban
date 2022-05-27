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

from winreg import QueryReflectionKey
import mysql.connector

#from Board import *
#from Bucket import *
#from Card import *
#from ProjectSelection import *

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

def createDatabase(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS kanban")

createDatabase(conn)


def createTable(conn, query):
    conn.database = "kanban"
    cursor = conn.cursor()
    #query = "CREATE TABLE IF NOT EXISTS "+ str(board)+" (card VARCHAR(2000),card_notes VARCHAR(2000),cards_assignment VARCHAR(2000))"
    cursor.execute(query)

#board = "FakeBoard"
#createTable(conn, board)

def addCard(conn,query, info):
    binNum = info[0]
    name = info[1]
    desc = info[2]
    vals = [name, desc,True] 
    for i in range(binNum-1):
        vals.append(False)
    conn.database = "kanban"
    cursor = conn.cursor()
    #query = "INSERT INTO "+str(board)+ " (card,card_notes,cards_assignment) VALUES (%s,%s,%s)"
    #vals = (card, card_notes,cards_assignment)
    #print(query, vals)
    cursor.execute(query,vals)
    conn.commit()


#def updateCard(conn,board,card,card_notes,cards_assignment):
#    conn.database = "kanban"
#    cursor = conn.cursor()
#    query = "UPDATE "+str(board)+" SET card =%s, card_notes =%s, cards_assignment =%s"
#    vals = (card,card_notes,cards_assignment)
#    cursor.execute(query,vals)
#    conn.commit()


def cardMoved(conn, board, cardTitle,oldLocation, newLocation):
    conn.database = "kanban"
    cursor = conn.cursor()
    # title and desc don't change, remaining are buckets on board
    # search for card title, make newLocation column True, rest false
    # need sum like UPDATE board SET oldLoc = False, newLoc = True WHERE title = cardTitle
    query = "UPDATE "+str(board).replace(" ","あ")+ " SET "+ str(oldLocation)+" =%s, "+str(newLocation)+" =%s WHERE title =%s "
    vals = (False,True, str(cardTitle))
    cursor.execute(query,vals)
    conn.commit()



# returns all data for a specific board
def selectAll(conn,board):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "SELECT * FROM "+str(board)
    #print(query)
    cursor.execute(query)
    return cursor.fetchall()





# returns all data for a specific card
def selectOne(conn,board,card):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "SELECT * FROM "+str(board)+" WHERE card = %s"
    adr = (card,)
    cursor.execute(query,adr)
    return cursor.fetchone()



# deletes specific card from DB
def deleteCard(conn,board,card):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "DELETE FROM "+str(board)+" WHERE card =%s"
    adr = (card,)
    cursor.execute(query,adr)
    conn.commit()



# deletes a whole board from DB
def deleteBoard(conn,board):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "DROP TABLE IF EXISTS "+str(board)
    cursor.execute(query)
    conn.commit()


#https://www.geeksforgeeks.org/how-to-add-a-column-to-a-mysql-table-in-python/
# inserts new bin into DB for specific kanban board
def addBin(conn,board, bin):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "ALTER TABLE "+str(board)+" ADD IF NOT EXISTS "+str(bin)+" VARCHAR(100)"
    cursor.execute(query)
    conn.commit()


# deletes a bin from a board in DB
def deleteBin(conn,board,bin):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "ALTER TABLE "+str(board)+" DROP COLUMN IF EXISTS "+str(bin)
    cursor.execute(query)
    conn.commit()

def getTables(conn):
    conn.database = "kanban"
    mycursor = conn.cursor()
    mycursor.execute("SHOW TABLES FROM kanban")
    return mycursor.fetchall()

def getColumns(conn,board):
    conn.database = "kanban"
    mycursor = conn.cursor()
    query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'kanban' AND TABLE_NAME = '"+str(board)+ "'"
    mycursor.execute(query)
    return mycursor.fetchall()
    




#print(getTables(conn)) # a list of tuples, [(board1,),(board2,)]
#print(getTables(conn)[0][0])  # type=str output "board1"
#print(len(getTables(conn)), getTables(conn))
allBoards = getTables(conn)

#for i in range(len(allBoards)):
#    print(type(allBoards[i]),allBoards[i]) # tuple [(board1,)]
#    print(type(allBoards[i][0]),allBoards[i][0]) # string "board1"

allBoardsAndTables = []
for i in range(len(allBoards)):
    tempBoardTitle = allBoards[i][0]
    allBoardsAndTables.append(selectAll(conn,tempBoardTitle))
    #print("\n")

#print(allBoardsAndTables)  
# returns list of lists of tuples NOT SAME BOARDS, each list has a tuple for each card in that board
# [[('cardTitle','cardDesc',bool isInThisBin,....)], [('cardTitle2',...)]]

#print(getColumns(conn,allBoards[2][0]))
#for i in range(len(allBoards)):
#    print("\n What i want")
#    print(getColumns(conn,allBoards[i][0])) # this is board's columns
#    print(allBoards[i][0],type(allBoards[i][0])) # this is board Title
#    print(getColumns(conn, allBoards[i][0])[1][0])



# how should i organize this?
# list of list of tuples, 
# [ [ (BoardTitle, Col1,Col2,Col3,...), (cardTitle1,cardDesc1,bin,bin,...)]]
