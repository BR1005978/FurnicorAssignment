from Menus.Login import loginScreen
from Menus.InfoScreen import displayInfo
import Userclasses

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
        currentUser = None 

        
        while currentUser == None:
            currentUser = homeScreenNoUser()
        

        print("Someone logged in! : ", currentUser)

        while currentUser != "":
            currentUser = homeScreenWithUser(currentUser)

def homeScreenNoUser():
        '''
        the screen that gets shown when no user is logged in
        '''
        print(
            """
Hello, anonymous user.\n
1. Log in

2. Display program info

0. Exit
            """)

        answer = input("Select the number of an option and press enter : ")

        if answer =="1":
            # werkt dit? 
            return loginScreen()
        elif answer =="2":
            displayInfo()
        elif answer =="0":
            exit()
        else:
            input("Input nog recognized")



def homeScreenWithUser(user):
    '''
    the screen that is shown when a user is succesfully logged in

    #to do : implement class-specific functions
    '''

    print("Welcome user: ", user)
    while True:
        print(
                """
    1. Log out\n
    2. Display program info\n
    0. Exit
                """)
        answer = input("Select the number of an option and press enter : ")
        # answer 1 is for logging out. use y or n to decide whether to log out 
        
        if answer =="1":
            logoutanswer = "" 
            while logoutanswer.lower() not in ["y", "n"]:
                logoutanswer = input(f"Log out user {user.username}? y/n : ")
                if logoutanswer.lower() == "y":
                    print("Logging out ...")
                    return ""
                elif logoutanswer.lower() == "n":
                    input("Ok, not logging out.")
                else: 
                    input("input not recognized. type 'y' or 'n' ")
            # break
        elif answer =="2":
            displayInfo()
        elif answer =="0":
            exit()
        else:
            input("Input nog recognized")
