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

# from Functions.Auxfunctions import generateUserID
#from Member import MemberClass

def SQLite3fiddle():

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    column = 'firstname'
    variable = 'sjaak'

    DBcursor.execute(f"""
        
        SELECT *
        FROM Members
        WHERE {column} = '{variable}' COLLATE NOCASE
        
        """)

    queryresult = DBcursor.fetchall()

    print(queryresult)
    print(type(queryresult))

    if queryresult == []: 
        print("queryresult is an empty list")
    else:
        print("apparantly queryresult is not an empty list")

    # DBcursor.execute(f"""
    #     INSERT INTO Members
    #     VALUES(
    #         555111462,
    #         '{firstname}',
    #         '{lastname}',
    #         '{address}',
    #         '{email}',
    #         '31-6-{phonenumber}',
    #         '{date.today()}'
    #     )
    #     """)


    # firstname = 'Stronkerino'
    # lastname = 'Snollerino'
    # address = 'Boterkoekstraat'
    # email = 'Drolleredosio@kontmail.org'
    # phonenumber = 33445566

    # DBcursor.execute(f"""
    #     INSERT INTO Members
    #     VALUES(
    #         555111462,
    #         '{firstname}',
    #         '{lastname}',
    #         '{address}',
    #         '{email}',
    #         '31-6-{phonenumber}',
    #         '{date.today()}'
    #     )
    #     """)







    ### updating a table
    # DBcursor.execute(f"""
    # UPDATE Advisors
    # SET password = 'bungbung'
    # WHERE username = 'beeboo';

    # UPDATE SysAdmins
    # SET password = 'POOPOO'
    # WHERE username = 'beeboo'

    # """ )

    ### querying from 2 tables with same column name
    # DBcursor.execute("""
    #     SELECT username
    #     FROM Advisors
    #     UNION
    #     SELECT username
    #     FROM SysAdmins
    # """)

    # queryresults= DBcursor.fetchall()

    # print(queryresults)

    # DBcursor.execute("""
    # SELECT username 
    # FROM Advisors


    # """)
    # queryresult = DBcursor.fetchall()


    # print('query result =', queryresult)

    # print(type(queryresult[0]))

    # if ('lameAdvisor',) in queryresult:
    #     print('found lameAdvisor username')



    #create table

    # DBcursor.execute("""
    #     CREATE TABLE SysAdmins (
    #         username text, 
    #         password text
    #         )""")

    # DBcursor.execute("DROP TABLE SysAdmin")

    # DBcursor.execute("""
    #     INSERT INTO Advisors
    #     VALUES(
    #         'dummyAdvisor',
    #         'advisorpassword'
    #     )
    #     """)


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

    input("press enter to continue")