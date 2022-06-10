import sqlite3


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

    searchResults = user.queryMembers(columnName, searchData.lower())
    print("Fetching results ...")
    if searchData == []:
        print("Nothing found")
    else:
        print("Found these matching results: ")
        for item in searchResults:
            print(f"""
Membership ID: {item[0]}
First name: {item[1]} 
Last name: {item[2]}
Address: {item[3]}
E-mail: {item[4]}
Phone number: {item[5]}
Registration date: {item[6]}
            """)
        print("")
    input("Press 'enter' to continue ...")

