from hashlib import new
import sqlite3
from telnetlib import ENCRYPT
from Functions.Auxfunctions import hashEncrypt
from Functions.Logfunction import LogData, logSuspicious
from Functions.caesar import *
from Userclasses.AdvisorClass import Advisor
from Userclasses.SuperAdminClass import SuperAdmin
from Userclasses.SysAdminClass import SysAdmin

import os

'''functions for logging in'''

def verifyCredentials(username, password):
    '''
    this is the function which we query the 
    database for correct credentials

    if succesful, returns a tuple: (True, <userobject>)
    userobject can be an advisor or a sysadmin

    if unsuccesful, returns a tuple: (False, None) 
    '''

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    results = None
    encryptedPassword = hashEncrypt(password)

    
    # try to find the credentials in the Advisors table first ...
    DBcursor.execute(f"""
                    SELECT * 
                    FROM Advisors
                    WHERE username=:username
                    AND password=:password
                    """, {'username': encrypt(username, s), 'password': encryptedPassword})

    results = DBcursor.fetchone()

    # if something was returned from the database, that must imply that
    # the credentials were correct. therefore, make an advisor with this username

    if results != None:
        try:
            userobject = Advisor(username)
        except: 
            pass
    # if that didn't work, try to find the credentials in the 
    # SysAdmins table ...
    if results == None:
        DBcursor.execute(f"""
                SELECT * 
                FROM SysAdmins
                WHERE username=:username
                AND password=:password
                """, {'username': encrypt(username, s), 'password': encryptedPassword})
        
        results = DBcursor.fetchone()
        try:
            userobject = SysAdmin(username)
        except: 
            pass

    # if THAT also didn't work, we should check if the user attempted to login as superadmin,
    # which has some hardcoded credentials
    if results == None and username == 'superadmin' and password == 'Admin321!':
        print("super admin login succeeded")
        return True, SuperAdmin()

        

    # and if that didn't find any credentials, well, then the credentials
    # most likely do not exist.  
    if results == None: 
        print("Verifying credentials resulted in a nonetype. the credentials were probably incorrect")
        return False, None

    # if the credentials WERE correct ...
    elif results[0] == encrypt(username) and results[1] == encryptedPassword:
        print('Found correct credentials in database')
        return True, userobject

    # error handling for extremely weird errors which are likely not happening
    elif results == tuple(): 
        print('Verifying credentials returned an empty tuple, how did this happen?')
        return False, None 
    else:
        print("verifyCredentials(): something really weird happened.")
        return False, None


def loginScreen():

    '''
    returns: a user object (Advisor, SysAdmin, SuperAdmin)
    
    asks the user for a username and password, and queries the database to see if 
    there is an overlap with information in the inputted values and the database


    '''
    i = 0
    while i < 3:


        username = input("Username: ")
        password = input("Password: ")

        verificationResults = verifyCredentials(username, password)


        if verificationResults[0]:

            #print("attempting to print the object: ", verificationResults[1])
            return verificationResults[1]
        else:
            cont = input("Credentials not found. Press enter to try again, or type q to cancel ... ")
            i += 1
            if cont.lower() == "q":
                return None
    input("Maximum amount of login attempts exceeded. Logging data...")
    logSuspicious("anonymous user", "Max amount of login attempts exceeded")