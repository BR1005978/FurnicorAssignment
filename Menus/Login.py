import sqlite3

'''functions for logging in'''

def verifyCredentials(username, password):
    '''
    this is the function which we query the 
    database for correct credentials

    todo: check to see if correct credentials are returned from the database
    '''

    databaseConnection = sqlite3.connect('FurnicoreDatabase.db')
    DBcursor = databaseConnection.cursor()
    
    # try to find the credentials in the Advisors table first ...
    DBcursor.execute(f"""
                    SELECT * 
                    FROM Advisors
                    WHERE username = '{username}'
                    AND password = '{password}'
                    
                    """)
    ### maak een object aan van dit type. alleen een username is niet genoeg
    results = DBcursor.fetchone()

    # if that didn't work, try to find the credentials in the 
    # SysAdmins table ...
    if results == None:
        DBcursor.execute(f"""
                SELECT * 
                FROM SysAdmins
                WHERE username = '{username}'
                AND password = '{password}'
                
                """)
        ### maak een object aan van deze gast
        results = DBcursor.fetchone()

    # and if that didn't find any credentials, well, then the credentials
    # most likely do not exist.  
    if results == None: 
        print("verifyCredentials(): verifying credentials resulted in a nonetype. the credentials were probably incorrect")
        return False

    # if the credentials WERE correct ...
    elif results[0] == username and results[1] == password:
        print('verifyCredentials(): found correct credentials in database')
        return True

    # error handling for extremely weird errors which are likely not happening
    elif results == tuple(): 
        print('verifyCredentials(): returned an empty tuple, how did this happen?')
        return False 
    else:
        print("verifyCredentials(): something really weird happened.")
        return False


def loginScreen():

    '''
    asks the user for a username and password, and queries the database to see if 
    there is an overlap with information in the inputted values and the database
    '''
    # returnt deze functie een username? voor het definiëren van de huidige gebruiker?
    while True:
        print("loginScreen()")

        username = input("Username: ")
        password = input("Password: ")



        if verifyCredentials(username, password):
            print("loginScreen() returning the username: ", username)

            ### zoals in de vorige functie vermeld, is alleen een username
            ### niet genoeg. je moet een object maken ervan, zodat de functies ook kloppen
            return username
        else:
            cont = input("credentials not found. press enter to try again, or type q to cancel ... ")
            if cont.lower() == "q":
                return ""


#loginScreen()

    