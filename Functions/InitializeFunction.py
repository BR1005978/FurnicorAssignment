import sqlite3
import os
import csv

from Functions.caesar import encrypt

def initializeLogfile():
    ''' 
    function that creates the logfile if it does not exist yet on startup
    '''

    if os.path.exists('logfile.txt'):
        print("[DEV] logfile exists")
    else:
        print("logfile does not exist")
        file = open('logfile.txt', 'w', encoding="utf-8")
        file.write(encrypt("Nr,Username,Date,Time,Description of Activity,Additional information,Suspicious\n"))

def initializeSusfile():
    if os.path.exists('susfile.txt'):
        print("[DEV] susfile exists")
    else:
        print("[DEV] susfile does not yet exist. making susfile")
        file = open('susfile.txt', 'w', encoding="utf-8")
        file.write(encrypt("""Nr,Username,Date,Time,Description of Activity,Additional information,Suspicious\n
"""))


def initializer():

    '''
    the functions that initialize the database. think of the functions that make the tables if there are none yet. 
    so the functions that get executed on the first time starting up this program
    '''
    initializeLogfile()
    initializeSusfile()

    if os.path.exists('FurnicorDatabase.db'):
        print('[DEV] database exists')
    else:
        print('[DEV] database does not yet exist, creating now ...')
        databaseConnection = sqlite3.connect('FurnicorDatabase.db')
        DBcursor = databaseConnection.cursor()

        #create SysAdmins table

        print('[DEV] initializer()')

        print("attempting SysAdmins table creation ...")

        try:
            DBcursor.execute("""
                CREATE TABLE SysAdmins (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    firstname TEXT,
                    lastname TEXT,
                    regdate TEXT,

                    CHECK 
                    (length(username) < 50
                    AND
                    length(password) < 50
                    AND
                    length(firstname) < 50
                    AND
                    length(lastname) < 50
                    AND
                    length(regdate) < 50
                    ) 
                    )""")
        except sqlite3.OperationalError:
            print("Table SysAdmins already exists.")
        except:
            print("Unknown error in database table creation")
        else:
            print("SysAdmins table created")




        #create advisors table

        print("attempting Advisor table creation ...")
        try:
            DBcursor.execute("""
                CREATE TABLE Advisors (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    firstname TEXT,
                    lastname TEXT,
                    regdate TEXT,

                    CHECK 
                    (length(username) < 50
                    AND
                    length(password) < 50
                    AND
                    length(firstname) < 50
                    AND
                    length(lastname) < 50
                    AND
                    length(regdate) < 50
                    ) 
                    )""")
        except sqlite3.OperationalError:
            print("Table Advisors already exists.")
        except:
            print("Unknown error in database table creation")
        else:
            print("Advisors table created")



        #create Members table

        print("attempting Members table creation ...")
        try:
            DBcursor.execute("""
                CREATE TABLE Members (
                    membershipID text PRIMARY KEY,
                    firstname text, 
                    lastname text,
                    address text,
                    email text,
                    phonenumber text,
                    registrationdate text,

                    CHECK 
                    (length(firstname) < 50
                    AND
                    length(lastname) < 50
                    AND
                    length(address) < 50
                    AND
                    length(email) < 50
                    AND
                    length(phonenumber) < 50
                    AND
                    length(registrationdate) < 50
                    ) 
                    )""")
        except sqlite3.OperationalError:
            print("Table Members already exists.")
        except:
            print("Unknown error in database table creation")
        else:
            print("Members table created")


        databaseConnection.commit()

        databaseConnection.close()


