from hashlib import new
import sqlite3
from Userclasses.AdvisorClass import Advisor
from Userclasses.SysAdminClass import SysAdmin

'''functions for logging in'''

def verifyCredentials(username, password):
    '''
    this is the function which we query the 
    database for correct credentials

    if succesful, returns a tuple: (True, <userobject>)
    userobject can be an advisor or a sysadmin

    if unsuccesful, returns a tuple: (False, None) 
    '''

    databaseConnection = sqlite3.connect('FurnicoreDatabase.db')
    DBcursor = databaseConnection.cursor()

    usertype = ""
    
    # try to find the credentials in the Advisors table first ...
    DBcursor.execute(f"""
                    SELECT * 
                    FROM Advisors
                    WHERE username = '{username}'
                    AND password = '{password}'
                    
                    """)

    results = DBcursor.fetchone()

    ### let's make an object of this retrieved user. merely a username is not enough
    try:
        userobject = Advisor(username, password)
    except: 
        print("creating advisor failed")

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
        try:
            userobject = SysAdmin(username, password)
        except: 
            print("creating sysadmin failed")


    # and if that didn't find any credentials, well, then the credentials
    # most likely do not exist.  
    if results == None: 
        print("verifyCredentials(): verifying credentials resulted in a nonetype. the credentials were probably incorrect")
        return False, None

    # if the credentials WERE correct ...
    elif results[0] == username and results[1] == password:
        print('verifyCredentials(): found correct credentials in database')
        return True, userobject

    # error handling for extremely weird errors which are likely not happening
    elif results == tuple(): 
        print('verifyCredentials(): returned an empty tuple, how did this happen?')
        return False, None 
    else:
        print("verifyCredentials(): something really weird happened.")
        return False, None


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



        verificationResults = verifyCredentials(username, password)


        if verificationResults[0]:
            print("loginScreen() returning the username: ", username)
            #print("attempting to print the object: ", verificationResults[1])
            return verificationResults[1]
        else:
            cont = input("credentials not found. press enter to try again, or type q to cancel ... ")
            if cont.lower() == "q":
                return ""


#loginScreen()

    