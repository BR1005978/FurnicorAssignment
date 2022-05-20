from menus.Login import loginScreen

def homeScreen():
    '''intro screen '''
    print(
        """    ______                     _                   
   / ____/__  __ _____ ____   (_)_____ ____   _____
  / /_   / / / // ___// __ \ / // ___// __ \ / ___/
 / __/  / /_/ // /   / / / // // /__ / /_/ // /    
/_/     \__,_//_/   /_/ /_//_/ \___/ \____//_/     
""")
    print("Welcome to Furnicor Family System v0.01")

    while True:
        print(
            """
1. Login\n
2. Exit
            """)

        answer = input("input: ")

        if answer =="1":
            loginScreen()
        elif answer =="2":
            break
        else:
            print("Input nog recognized")

homeScreen()