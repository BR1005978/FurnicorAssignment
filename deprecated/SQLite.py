'''
this file is deprecated. this no longer has any use in the program itself , but illustrates 
some useful functions to be used in the rest of the program.
also to be used for fiddling with the database

Important functions: 
dbConn = sqlite3.connect('<filename>.db')
    this is for linking to the database, and making a database writ if it does not stand as of yet

DBcursor = dbConn.cursor()
    this is for marking a 'cursor' which is used for fulfilling calls to the database

DBcursor.execute(""" some database call here """)
    for making calls to the database

DBcursor.fetchone() / .fetchall() / .fetchmany(<integer>)
    for fetching database cases. use fetchmany along with a number of queries you want to retrieve

dbConnection.commit()
    push changes to the database

dbConn.close()
    close the connection to the database. best practice to put this after every interaction with the database

'''

from datetime import date
import sqlite3

from Functions.DatabaseFunctions import queryDatabase3args, wipeDatabase
from Functions.InitializeFunction import initializer
from Functions.caesar import encrypt
from Functions.createDummyData import createDummyData

# from Functions.Auxfunctions import generateUserID
#from Member import MemberClass

def SQLite3fiddle():

    print(queryDatabase3args('Members', 'membershipID', '2270762309'))

    input("press enter to continue")