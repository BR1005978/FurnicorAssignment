from Menus.Login import loginScreen
from Menus.InfoScreen import displayInfo

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
2. Display program info\n
3. Exit
            """)

        answer = input("Select the number of an option and press enter : ")

        if answer =="1":
            loginScreen()
        if answer =="2":
            displayInfo()
        elif answer =="3":
            exit()
        else:
            print("Input nog recognized")

homeScreen()