import os
import sqlite3
from Functions.Logfunction import LogData, logSuspicious

from Functions.caesar import *



def modifyAdvisorMenu(user):
    '''
    the interactive menu for SysAdmin.modifyAdvisor()
    '''
    username = input("Whose credentials do you want to modify? (enter the username): ")

    ###TODO: check if this username exists. 


    print("[DEV]modifyAdvisorMenu()")

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute("SELECT * FROM Advisors WHERE username=:usr", {'usr': encrypt(username, s)})

    idFound = DBcursor.fetchall()
    if idFound:
        while True:
            columnName = ''
            print("""Select credential to modify...
    1. Username
    2. First name
    3. Last name""")
            choice = input("Type the number of an option and press enter : ")
            if choice == "1":
                columnName = "username"
                break
            # elif choice == "2":
            #     columnName = "password"
            #     break
            elif choice == "2":
                columnName = "firstname"
                break
            elif choice == "3":
                columnName = "lastname"
                break
            else:
                input("Input not recognized, please try again ...")

        variable = input("Change to: ")

        try:
            print("Attempting to modify...")
            user.modifyAdvisor(columnName,variable, username)
            LogData(user.username, "User modified advisor", username)
            input("Modification probably succeeded. Press 'enter' to continue ... ")
        except:
            print("ERROR CODE MA3: Something went wrong... Please try again.")
            logSuspicious(user.username, "Error code MA3, modification of advisor went wrong for some reason")
            input()
    else:

        print("MemberId not found")
