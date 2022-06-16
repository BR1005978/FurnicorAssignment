import sqlite3
from Functions.Auxfunctions import generateUserID, hashEncrypt
from datetime import date

from Functions.caesar import *


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
    try: 
        DBcursor.execute(f"INSERT INTO {table} VALUES(?, ?)", (encrypt(username,s), hashEncrypt(password)))
    except sqlite3.IntegrityError:
        print("Database injection failed. Max character length exceeded. ")
        input("Press enter to continue...")

   

    databaseConnection.commit()
    databaseConnection.close()


def insertIntoDatabase5args(firstname, lastname, address, email, phonenumber):
    '''
    add a new member to the system
    '''


    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    try:
         DBcursor.execute("INSERT INTO Members VALUES(?, ?, ?, ?, ?, ?, ?)", (encrypt(generateUserID()), encrypt(firstname, s), encrypt(lastname, s), encrypt(address, s), encrypt(email, s), encrypt("31-6-"+ phonenumber, s), date.today()))
    except sqlite3.IntegrityError:
        print("Database injection failed. Max character length exceeded. ")
        input("Press enter to continue...")
   

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
        WHERE {key} = :var
    """, {'var': variable})

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
        SET {column} = :val
        WHERE {conditionColumn} = :val2
    """, {'val':newValue, 'val2': conditionValue})

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
        SET {column} = :col
        WHERE {conditionColumn} = :col2
    """, {'col': hashEncrypt(newValue), 'col2': conditionValue})

    databaseConnection.commit()
    databaseConnection.close()


## testenv
# wipeDatabase()
