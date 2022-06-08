def modifyAdvisorMenu(user):
    '''
    the interactive menu for SysAdmin.modifyAdvisor()
    '''
    username = input("Whose credentials do you want to modify? (enter the username): ")

    ###TODO: check if this username exists. 


    print("[DEV]modifyAdvisorMenu()")
    while True:
        columnName = ''
        print("""Select credential to modify...
1. Username
2. Password""")
        choice = input("Type the number of an option and press enter : ")
        if choice == "1":
            columnName = "username"
            break
        elif choice == "2":
            columnName = "password"
        else:
            input("Input not recognized, please try again ...")

    variable = input("Change to: ")

    try:
        print("Attempting to modify...")
        user.modifyAdvisor(columnName,variable, username)
        input("Modification probably succeeded. Press 'enter' to continue ... ")
    except:
        print("ERROR CODE MA3: Something went wrong... Please try again.")
        input()