from Menus.Login import loginScreen
from Menus.InfoScreen import displayInfo
import Userclasses
from Userclasses.AdvisorClass import Advisor

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
    1. Log out

    2. Display program info

    9. [DEV] print own type

    0. Exit
                """)
        answer = input("Select the number of an option and press enter : ")
        # answer 1 is for logging out. use y or n to decide whether to log out 
        print("printin' ", user)
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
        elif answer == "9":
            print(type(user))
            print("am i an advisor?")
            if type(user) == Advisor:
                print("yep, this is an advisor")
            else:
                print("this is probably not an advisor. or maybe it is, but python didn't understand it")
            input()
        elif answer =="0":
            exit()
        else:
            input("Input nog recognized")
