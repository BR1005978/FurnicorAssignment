import os
import sqlite3
from Functions.DatabaseFunctions import queryDatabase3args

from Functions.Logfunction import LogData, logSuspicious
from Functions.caesar import decrypt, encrypt



def modifyMemberMenu(user):
    print("[DEV]modifyMemberMenu()")

    searchResults= queryDatabase3args('Members', 'firstname', '')
    for item in searchResults:
            print(f"""
Membership ID: {decrypt(item[0])}
First name: {decrypt(item[1])} 
Last name: {decrypt(item[2])}
Address: {decrypt(item[3])}
E-mail: {decrypt(item[4])}
Phone number: {decrypt(item[5])}
Registration date: {decrypt(item[6])}
            """)

    membershipID = input("Enter the membership ID of the member which you want to modify (use the search function (4) to find the membership ID) or type 'q' to cancel: ")
    
    if membershipID.lower() == 'q':
        return

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    DBcursor.execute("SELECT * FROM Members WHERE membershipID=:memberId", {'memberId': encrypt(membershipID)})

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
            LogData(user.username, "Modified member", variable)
            input("Modification succeeded. Press 'enter' to continue ... ")
        except:
            print("ERROR CODE MM3: Something went wrong... Please try again.")
            logSuspicious(user.username, "Modify member had a weird error")
            input()
    else:

        input("MemberId not found")