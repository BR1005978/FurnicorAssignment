import sqlite3

'''functions for logging in'''

def searchDB(username, password):
    '''
    this is the function which we query the 
    database for correct credentials
    '''

    databaseConnection = sqlite3.connect('FurnicoreDatabase.db')
    DBcursor = databaseConnection.cursor()

    tables = ['Advisors', 'SysAdmins']
    
    # for table in tables:
    DBcursor.execute(f"""
                    SELECT * 
                    FROM Advisors
                    WHERE username = '{username}'
                    AND password = '{password}'
                    
                    """)

    results = DBcursor.fetchone()

    return results 

def loginScreen():

    '''
    asks the user for a username and password, and queries the database to see if 
    there is an overlap with information in the inputted values and the database
    '''

    
    print("loginScreen()")

    username = input("Username: ")
    password = input("Password: ")

    print(searchDB(username, password))



    