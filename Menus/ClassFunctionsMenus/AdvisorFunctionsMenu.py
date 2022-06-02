def advisorFunctionsMenu(user):

    answer = ""


    while answer != "0":
        print(f"""
    {user.sayType()} functions

    1. update own password
    
    2. add new member

    3. modify existing member

    4. search member in database
    
    0. return to previous menu 
        """)
        answer = input("Type the number of an option and press enter : ")

        if answer == "1":
            print("updating own password not yet implemented")
            input()
    
        elif answer == "2":
            print("add new member not yet implemented")
            input()
            
        elif answer == "3":
            print("modify member not yet implemented")
            input()

        elif answer == "4":
            print("search member in database not yet implemented")
            input()

        elif answer == "0":
            break

        else:
            print("input not recognized")
            input()
