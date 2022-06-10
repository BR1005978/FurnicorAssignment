import sqlite3
from Functions.Auxfunctions import generateUserID, hashEncrypt
from datetime import date


def wipeDatabase():
    '''
    this function wipes all entries in the database. use with caution
    '''
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    tables = ['Advisors', 'SysAdmins', 'Members']
    for table in tables:
        DBcursor.execute(f"""DELETE FROM {table}""")

    databaseConnection.commit()
    databaseConnection.close()

def insertIntoDatabase3arg(table, username, password):
    ''' 
    function that inserts data into either the Advisors or the SysAdmins table
    '''
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute(f"""
    INSERT INTO {table}
    VALUES(
        '{username}',
        '{hashEncrypt(password)}'
    )
    """)

    databaseConnection.commit()
    databaseConnection.close()


def insertIntoDatabase5args(firstname, lastname, address, email, phonenumber):
    '''
    add a new member to the system
    '''


    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute(f"""
        INSERT INTO Members
        VALUES(
            '{generateUserID()}',
            '{firstname}',
            '{lastname}',
            '{address}',
            '{email}',
            '31-6-{phonenumber}',
            '{date.today()}'
        )
        """)

    databaseConnection.commit()
    databaseConnection.close()


def queryDatabase2args(column = '*', table = ''):
    '''
    '''
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute(f"""
        SELECT {column} 
        FROM {table}
        """)

    databaseConnection.commit()
    databaseConnection.close()

def deleteEntry(table, key, variable):
    '''
    deletes an entry from the database. 
    TODO: verify if the inputted variable actually exists in the database
    
    '''
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute(f"""
        DELETE FROM {table}
        WHERE {key} = '{variable}'
    """)

    databaseConnection.commit()
    databaseConnection.close()


def updateEntry(table, column, newValue, conditionColumn, conditionValue):
    '''
    versatile function that allows modifications on one entry in the database
    '''
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute(f"""
        UPDATE {table}
        SET {column} = '{newValue}'
        WHERE {conditionColumn} = '{conditionValue}'
    """)

    databaseConnection.commit()
    databaseConnection.close()

def resetPassword(table, column, newValue, conditionColumn, conditionValue):
    '''
    reset the password of a user
    '''
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute(f"""
        UPDATE {table}
        SET {column} = '{hashEncrypt(newValue)}'
        WHERE {conditionColumn} = '{conditionValue}'
    """)

    databaseConnection.commit()
    databaseConnection.close()


## testenv
# wipeDatabase()
