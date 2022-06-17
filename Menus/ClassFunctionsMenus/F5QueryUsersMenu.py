import sqlite3

from Functions.DatabaseFunctions import queryDatabase3args
from Functions.caesar import decrypt, encrypt  


def queryUsersMenu(user):
    print("[DEV] queryUsersMenu()")
    value = input("Enter username to look for, or leave blank to search all: ")

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()
    
    resultsFormatted = ''


    # queryDatabase3args('')
    if value == '':
        DBcursor.execute(f"""
            SELECT username 
            FROM Advisors
            """)
        # print("advisor results: ", DBcursor.fetchall())
        
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"{decrypt(item[0])}, Advisor\n"

        DBcursor.execute(f"""
            SELECT username
            FROM SysAdmins
            """)
        # print("SysAdmin results: ", DBcursor.fetchall())
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"{decrypt(item[0])}, SysAdmin\n"

        print(resultsFormatted)

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
            resultsFormatted += f"{decrypt(item[0])}, Advisor\n"

        # DBcursor.execute(f"""
        # SELECT username
        # FROM SysAdmins
        # WHERE username LIKE :inp
        # """, {'inp': '%{value}%'})
        # # print("SysAdmin results: ", DBcursor.fetchall())
        results = queryDatabase3args('SysAdmins', 'username', value)


        for item in results:
            resultsFormatted += f"{decrypt(item[0])}, SysAdmin\n"

        print('Found the following results: \n' + resultsFormatted)    


    databaseConnection.commit()
    databaseConnection.close()