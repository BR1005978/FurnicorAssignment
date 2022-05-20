'''
this file is deprecated. this no longer has any use in the program itself , but illustrates 
some useful functions to be used in the rest of the program

Important functions: 
dbConn = sqlite3.connect('<filename>.db')
    this is for linking to the database, and making a database writ if it does not stand as of yet

DBcursor = dbConn.cursor()
    this is for marking a 'cursor' which is used for fulfilling calls to the database

DBcursor.execute(""" some database call here """)
    for making calls to the database

DBcursor.fetchone() / .fetchall() / .fetchmany(<integer>)
    for fetching database cases. use fetchmany along with a number 

dbConnection.commit()
    push changes to the database

dbConn.close()
    close the connection to the database. best practice to put this after every interaction with the database

'''

import sqlite3
from Member import MemberClass


databaseConnection = sqlite3.connect('FurnicoreDatabase.db')

DBcursor = databaseConnection.cursor()

#create table

DBcursor.execute("""
    CREATE TABLE Members (
        firstname text, 
        lastname text
        )""")


#insert

# DBcursor.execute("""
#     INSERT INTO Members
#     VALUES(
#         'Truus',
#         'Jacobs',
#         3500
#     )
#     """)

#query table

# DBcursor.execute("""
#     SELECT *
#     FROM members
#     WHERE
#     lastname = 'Jacobs'

#     """)

# print(DBcursor.fetchall())


databaseConnection.commit()

databaseConnection.close()