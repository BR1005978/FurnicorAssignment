import os
import sqlite3

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def modifyMemberMenu(user):
    print("[DEV]modifyMemberMenu()")
    membershipID = input("Enter the membership ID of the member which you want to modify (use the search function (3) to find the membership ID): ")
    
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute("SELECT * FROM Members WHERE membershipID=:memberId", {'memberId': membershipID})

    idFound = DBcursor.fetchall()
    if idFound:
        while True:
            columnName = ''
            print("""Select column to modify...
    1. First name
    2. Last name
    3. Home addres
    4. E-mail
    5. Phone number""")
            choice = input("Type the number of an option and press enter : ")
            if choice == "1":
                columnName = "firstname"
                break
            elif choice == "2":
                columnName = "lastname"
                break
            if choice == "3":
                columnName = "address"
                break
            elif choice == "4": 
                columnName = "email"
                break
            elif choice == "5":
                columnName = "phonenumber"
                break

            else:
                input("Input not recognized, please try again ...")

        variable = input("Input new data: ")

        try:
            print("Attempting to modify...")
            user.modifyMember(columnName,variable, membershipID)
            input("Modification probably succeeded. Press 'enter' to continue ... ")
        except:
            print("ERROR CODE MM3: Something went wrong... Please try again.")
            input()
    else:
        clearConsole()
        print("MemberId not found")