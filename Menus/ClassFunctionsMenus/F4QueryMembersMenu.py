import sqlite3
from Functions.Logfunction import LogData

from Functions.caesar import decrypt


def queryMembersMenu(user):
    print("[DEV]queryMemberMenu()")
    while True:
        columnName = ''
        print("""Search by...
1. First name
2. Last name
3. Home addres
4. E-mail
5. Phone number
6. Membership ID
7. Registration date""")
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
        elif choice == "6":
            columnName = "membershipID"
            break
        elif choice == "7":
            columnName = "registrationdate"
            break
        else:
            input("Input not recognized, please try again ...")

    searchData = input("Enter data to look for: ")


    #TODO: hier gaat het mis. serachData.lower() werkt niet
    #want door de encryption klopt de searchdata niet meer
    searchResults = user.queryMembers(columnName, searchData)
    print("Fetching results ...")
    print("[DEV] found this: ", searchResults)
    if not (searchResults):
        print("Nothing found")
        LogData(user.username, "Attempted to find members, found nothing", sus="no" )
    else:
        print("Found these matching results: ")
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
        print("")
        LogData(user.username, "Retrieved information from the database about members", sus="no")
    input("Press 'enter' to continue ...")

