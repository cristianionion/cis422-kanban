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

#from Board import *
#from Bucket import *
#from Card import *
#from ProjectSelection import *

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

def createDatabase(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS kanban DEFAULT CHARACTER SET utf8")
    cursor.close()
    conn.commit()

createDatabase(conn)

def createTable(conn, query):
    conn.database = "kanban"
    cursor = conn.cursor()
    #query = "CREATE TABLE IF NOT EXISTS "+ str(board)+" (card VARCHAR(2000),card_notes VARCHAR(2000),cards_assignment VARCHAR(2000))"
    #print("QUERY",query)
    cursor.execute(query)
    cursor.close()
    conn.commit()

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
    cursor.close()
    conn.commit()

def cardMoved(conn, board, cardTitle, oldLocation, newLocation):
    conn.database = "kanban"
    cursor = conn.cursor()
    # title and desc don't change, remaining are buckets on board
    # search for card title, make newLocation column True, rest false
    # need sum like UPDATE board SET oldLoc = False, newLoc = True WHERE title = cardTitle
    query = "UPDATE "+str(board).replace(" ","あ")+ " SET "+ str(oldLocation).replace(" ","あ")+" =%s, "+str(newLocation).replace(" ","あ")+" =%s WHERE title =%s "
    #print(query)
    vals = (False,True, str(cardTitle))
    cursor.execute(query,vals)
    cursor.close()
    conn.commit()

# returns all data for a specific board
def selectAll(conn,board):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "SELECT * FROM "+str(board)
    #print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# returns all data for a specific card
def selectOne(conn,board,card):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "SELECT * FROM "+str(board)+" WHERE card = %s"
    adr = (card,)
    cursor.execute(query,adr)
    result = cursor.fetchone()
    cursor.close()
    return result

# deletes specific card from DB
def deleteCard(conn,board,card):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "DELETE FROM "+str(board)+" WHERE card =%s"
    adr = (card,)
    cursor.execute(query,adr)
    cursor.close()
    conn.commit()

# deletes a whole board from DB
def deleteBoard(conn,board):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "DROP TABLE IF EXISTS "+str(board)
    cursor.execute(query)
    cursor.close()
    conn.commit()

#https://www.geeksforgeeks.org/how-to-add-a-column-to-a-mysql-table-in-python/
# inserts new bin into DB for specific kanban board
def addBin(conn,board, bin):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "ALTER TABLE "+str(board)+" ADD IF NOT EXISTS "+str(bin)+" VARCHAR(100)"
    cursor.execute(query)
    cursor.close()
    conn.commit()

# deletes a bin from a board in DB
def deleteBin(conn,board,bin):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "ALTER TABLE "+str(board)+" DROP COLUMN IF EXISTS "+str(bin)
    cursor.execute(query)
    cursor.close()
    conn.commit()

def getTables(conn):
    conn.database = "kanban"
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES FROM kanban")
    result = cursor.fetchall()
    cursor.close()
    return result

def getColumns(conn,board):
    conn.database = "kanban"
    cursor = conn.cursor()
    query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'kanban' AND TABLE_NAME = '"+str(board)+ "'"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result    
    
allBoards = getTables(conn)
print(allBoards)

#for i in range(len(allBoards)):
    #deleteBoard(conn,allBoards[i][0])
    #print(allBoards[i][0], type(allBoards[i][0]))

allBoardsAndTables = []
for i in range(len(allBoards)):
    tempBoardTitle = allBoards[i][0]
    allBoardsAndTables.append(selectAll(conn,tempBoardTitle))
    #print("\n")

# Brad - wrapped this section in a function so we can (hopefully) 
# use it in project selection to populate existing boards
# not sure why the bucket name tuple always starts with 'title', 'description'
def getAllData():
    allData = []
    for i in range(len(allBoards)):
        allData.append([])
        allData[i].append((allBoards[i][0],),)
        cols = getColumns(conn,allBoards[i][0])
        for j in range(len(cols)):
            allData[i][0] = allData[i][0] + ((cols[j][0]),) 
            # at this point, each table has a list of one tuple containing boardTitle and colTitles
        for k in range(len(allBoardsAndTables[i])):
            allData[i].append(allBoardsAndTables[i][k])
    return allData

allData = getAllData()

#print(allData[1])
#print(allData[1][2][4])
for i in range(len(allData)):
    print(allData[i], "\n")
#print(allData[0][0],len(allData[0][0]), type(allData[0][0]))
#print(len(allData[1][1]), allData[1][0][0], allData[1][0][0].replace("あ"," "))

# how should i organize this?
# list of lists of tuples, each list for a board,
#                        tuple1 = boardtitle+cols, tuple2(+) = card data
# [ [ (BoardTitle, Col1,Col2,Col3,...), (cardTitle1,cardDesc1,bin,bin,...)]]

boardNamesList = []
for i in range(len(allData)): 
    bucketNames = []
    for j in range(len(allData[i][0])):
        if j == 0:
            boardName = allData[i][0][0]  # this is the Board's name
            boardName = boardName.replace("あ"," ")
            boardNamesList.append(boardName)
            #print("\n",boardName)
        else:
            bucketNames.append(allData[i][0][j].replace("あ"," ")) # the names of buckets for the respective board
    #print(bucketNames)
    for k in range(len(allData[i])):
        cardInfo = []
        if k>0:
            for card in range(len(allData[i][k])):
                cardInfo.append(allData[i][k][card]) # all the info for each card.
            #print(cardInfo)
#print("ALL BOARD NAMES: ", boardNamesList)
#print("HOW IT LOOKS ALL TOGETHER ", allData)
#print(allData[1][0])
#print("ronaldo" in allData[1][0]) # true
#a = boardNamesList.index('hopeffully it works')
#print(len(allData[a][0]), allData[a][0])
#print(boardNamesList.index('hopeffully it works'))
#print(allData[a][1], len(allData[a][1]), len(allData[a]))
#print('1' in allData[a][1], allData[a][1].index('1'))

########################## USERS DB ##########################

def createUserDB():
    '''
    Creates a separate database to store user info
    '''
    cursor = conn.cursor()
    query = 'CREATE DATABASE IF NOT EXISTS `user` DEFAULT CHARACTER SET utf8'
    cursor.execute(query)
    cursor.close()
    conn.commit()

def createUsersTable():
    '''
    Brad Bailey 6/2/22 8:42am
    Creates the 'users' table in the users DB
    this table stores all user info and is used to track both instructors and student groups
    its fields and their types can be observed in the query below
    in practice, instructors are group '0' and students are grouped by integers larger than zero
    '''
    # setup DB
    conn.database = 'user'
    # init cursor
    cursor = conn.cursor()
    # define query
    createUsersTableQuery = '''
        USE `user` ;
        CREATE TABLE IF NOT EXISTS `user`.`users` (
            `userID` INT NOT NULL AUTO_INCREMENT,
            `username` VARCHAR(255) NULL,
            `password` VARCHAR(255) NULL,
            `type` INT NULL,
            PRIMARY KEY (`userID`))
        ENGINE = InnoDB;
    '''
    # run query
    cursor.execute(createUsersTableQuery)
    # close and commit
    cursor.close()
    conn.commit()

def checkForm(userData):
    # userData must be a tuple of the form (username, password, type) with datatypes (str, str, int) respectively
    return (isinstance(userData[0], str) and isinstance(userData[1], str) and isinstance(userData[2], int))

def insertUser(userData):
    '''
    Brad Bailey 6/2/22 8:58am
    This function inserts a user's login info into the users table of the kanban DB
    userData must be a tuple of the form (username, password, type) with datatypes (str, str, int) respectively
    return value could be changed from boolean to int if we need to represent more error types/codes
    '''
    if not checkForm(userData):
        print('userData incorrectly formatted')
        return False
    
    # setup DB
    conn.database = 'user'
    # init cursor
    cursor = conn.cursor()
    # define query
    insertUserQuery = '''
        INSERT INTO users
        (username, password, type) 
        VALUES (%s, %s, %i)
    '''
    # run query
    cursor.execute(insertUserQuery, userData)
    # cleanup and commit
    cursor.close()
    conn.commit()
    return True

def removeUser(userData):
    '''
    Brad Bailey 6/4/22 10:00 AM 
    Removes a row from the users table in the user DB
    Values and types must match exactly
    SQL error handling yet to be implemented
    '''
    # check for correct format
    if not checkForm(userData):
        print('userData incorrectly formatted')
        return False

    # setup DB
    conn.database = 'user'
    # init cursor
    cursor = conn.cursor()
    # define query
    removeUserQuery = '''
        DELETE FROM users
        WHERE 
            username = %s AND 
            password = %s AND
            type = %i
    '''
    # run query
    cursor.execute(removeUserQuery, userData)
    # close and commit
    cursor.close()
    conn.commit()
    return True
    
def checkForUser(userData):
    '''
    Brad Bailey 6/4/22 10:00 AM 
    Checks for the existence of a user in the users table of the user DB
    Values and types must match exactly
    SQL error handling yet to be implemented
    '''
    # check for correct format
    if not checkForm(userData):
        print('userData incorrectly formatted')
        return False

    # setup DB
    conn.database = 'user'
    # init cursor
    cursor = conn.cursor()
    # define query
    checkUserQuery = '''
        SELECT * FROM users
        WHERE 
            username = %s AND 
            password = %s AND
            type = %i
    '''
    # run query
    cursor.execute(checkUserQuery, userData)
    # store result
    result = cursor.fetchall()
    # close cursor
    cursor.close()
    # if no rows match, return True, otherwise return False
    if len(result) == 0:
        return True
    else: return False

    ## TODO: fix error handling flow (try - except - else - finally) and change return vals accordingly
    # try:
    #     cursor.execute(removeUserQuery, userData)
    #     cursor.close()
    #     conn.commit()
    #     return True
    # # handle SQL errors
    # except mysql.connector.Error as error:
    #     errStr = str(error)
    #     print('Error: ', errStr) # errno, sqlstate, msg values
    #     cursor.close()
    #     return False