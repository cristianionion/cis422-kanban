import mysql.connector

# don't need this - defined in projectSelection
# conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="") 

########################## USERS DB ##########################

def createUserDB(conn):
    '''
    Creates a separate database to store user info
    '''
    cursor = conn.cursor()
    query = 'CREATE DATABASE IF NOT EXISTS `user` DEFAULT CHARACTER SET utf8'
    cursor.execute(query)
    cursor.close()
    conn.commit()

def createUsersTable(conn):
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

def checkForm(userData):
    # userData must be a tuple of the form (username, password, type) with datatypes (str, str, int) respectively
    return (isinstance(userData[0], str) and isinstance(userData[1], str) and isinstance(userData[2], int))

def insertUser(conn, userData):
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
        VALUES (%s, %s, %s)
    '''
    # run query
    cursor.execute(insertUserQuery, userData)
    # cleanup and commit
    cursor.close()
    conn.commit()
    return True

def removeUser(conn, userData):
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
            type = %s
    '''
    # run query
    cursor.execute(removeUserQuery, userData)
    # close and commit
    cursor.close()
    conn.commit()
    return True
    
def checkForUser(conn, userData):
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
            type = %s
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