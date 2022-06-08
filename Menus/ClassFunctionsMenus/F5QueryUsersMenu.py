import sqlite3  


def queryUsersMenu(user):
    print("[DEV] queryUsersMenu()")
    value = input("Enter username to look for, or leave blank to search all: ")

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()
    
    resultsFormatted = ''

    if value == '':
        DBcursor.execute(f"""
            SELECT username 
            FROM Advisors
            """)
        # print("advisor results: ", DBcursor.fetchall())
        
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"{item[0]}, Advisor\n"

        DBcursor.execute(f"""
            SELECT username
            FROM SysAdmins
            """)
        # print("SysAdmin results: ", DBcursor.fetchall())
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"{item[0]}, SysAdmin\n"

        print(resultsFormatted)

    else:
        DBcursor.execute(f"""
        SELECT username 
        FROM Advisors
        WHERE username LIKE '%{value}%'
        """)
        # print("advisor results: ", DBcursor.fetchall())
        
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"{item[0]}, Advisor\n"

        DBcursor.execute(f"""
        SELECT username
        FROM SysAdmins
        WHERE username LIKE '%{value}%'
        """)
        # print("SysAdmin results: ", DBcursor.fetchall())
        results = DBcursor.fetchall()

        for item in results:
            resultsFormatted += f"{item[0]}, SysAdmin\n"

        print('Found the following results: \n' + resultsFormatted)    


    databaseConnection.commit()
    databaseConnection.close()