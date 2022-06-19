import sqlite3

from Functions.DatabaseFunctions import queryDatabase3args
from Functions.Logfunction import LogData
from Functions.caesar import decrypt, encrypt  


def queryUsersMenu(user):

    value = input("Enter username to look for, or leave blank to search all: ")

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()
    
    resultsFormatted = ''


    # queryDatabase3args('')
    if value == '':
        DBcursor.execute(f"""
            SELECT * 
            FROM Advisors
            """)
        # print("advisor results: ", DBcursor.fetchall())
        
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"""
    Username  :{decrypt(item[0])}, 
    User type : Advisor
    First name: {decrypt(item[2])}
    Last name : {decrypt(item[3])}
    Registration date: {decrypt(item[4])}
    """
        DBcursor.execute(f"""
            SELECT *
            FROM SysAdmins
            """)
        # print("SysAdmin results: ", DBcursor.fetchall())
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"""
    Username  : {decrypt(item[0])} 
    User type : SysAdmin
    First name: {decrypt(item[2])}
    Last name : {decrypt(item[3])}
    Registration date: {decrypt(item[4])}
    """
        LogData(user.username, "Queried the database for all users" )
        print(resultsFormatted)
        input()

    else:
        # queryDatabase3args('')
        # DBcursor.execute(f"""
        # SELECT username 
        # FROM Advisors
        # WHERE username LIKE :inp
        # """, {'inp': '%{value}%'})
        # # print("advisor results: ", DBcursor.fetchall())
        
        results = queryDatabase3args('Advisors', 'username', value)

        for item in results:
            resultsFormatted += f"""
    Username  :{decrypt(item[0])}, 
    User type : Advisor
    First name: {decrypt(item[2])}
    Last name : {decrypt(item[3])}
    Registration date: {decrypt(item[4])}
    """
        # DBcursor.execute(f"""
        # SELECT username
        # FROM SysAdmins
        # WHERE username LIKE :inp
        # """, {'inp': '%{value}%'})
        # # print("SysAdmin results: ", DBcursor.fetchall())
        results = queryDatabase3args('SysAdmins', 'username', value)


        for item in results:
            resultsFormatted += f"""
    Username  : {decrypt(item[0])} 
    User type : SysAdmin
    First name: {decrypt(item[2])}
    Last name : {decrypt(item[3])}
    Registration date: {decrypt(item[4])}
    """
        LogData(user.username, "Queried the database for users")
        print('Found the following results: \n' + resultsFormatted)    
        input()

    databaseConnection.commit()
    databaseConnection.close()