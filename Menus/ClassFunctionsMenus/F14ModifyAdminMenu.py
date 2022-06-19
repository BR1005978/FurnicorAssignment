import sqlite3

from Functions.caesar import *
from Functions.Logfunction import LogData, logSuspicious


def modifyAdminMenu(user):


    username = input("Whose credentials do you want to modify? (enter the username): ")

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute("SELECT * FROM SysAdmins WHERE username=:usr", {'usr': encrypt(username, s)})

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
            user.modifyAdmin(columnName,variable, username)
            LogData(user.username, "User modified Admin", username)
            input("Modification probably succeeded. Press 'enter' to continue ... ")
        except:
            print("ERROR CODE MA3: Something went wrong... Please try again.")
            logSuspicious(user.username, "Error code MA3, modification of Admin went wrong for some reason")
            input()
    else:

        input("MemberId not found")