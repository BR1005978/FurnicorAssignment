from Menus.ClassFunctionsMenus.SysAdminFunctionsMenu import sysAdminFunctionsMenu
from Menus.Login import loginScreen
from Menus.Info.InfoScreen import displayInfo
from Menus.ClassFunctionsMenus.AdvisorFunctionsMenu import advisorFunctionsMenu
from Menus.ClassFunctionsMenus.SuperAdminFunctionsMenu import superAdminFunctionsMenu
from Userclasses.AdvisorClass import Advisor
from Userclasses.SuperAdminClass import SuperAdmin

from Userclasses.SysAdminClass import SysAdmin



def homeScreenWithUser(user):
    '''
    the screen that is shown when a user is succesfully logged in

    returns: None

    it only returns None when you want to log out 
    '''

    print("Welcome user: ", user)
    while True:
        print(
                f"""
    1. Access {user.sayType()} functions

    2. Display program info

    8. [DEV] print own type

    9. Log out

    0. Shut down program
                """)
                
        answer = input("Type the number of an option and press enter : ")
        # answer 1 is for logging out. use y or n to decide whether to log out 


        if answer == "1":
            print("accessing class-specific functions...") 
            if type(user) == Advisor: 
                advisorFunctionsMenu(user)
            elif type(user) == SysAdmin:
                sysAdminFunctionsMenu(user)
            elif type(user) == SuperAdmin:
                superAdminFunctionsMenu(user)
            else:
                print("something really weird just happened. the user is of an unknown class?")
            
               
        
        elif answer =="2":
            displayInfo()

        elif answer == "8":
            print(type(user))
            input()

        elif answer =="9":
            logoutanswer = "" 
            while logoutanswer.lower() not in ["y", "n"]:
                logoutanswer = input(f"Log out user {user.username}? y/n : ")
                if logoutanswer.lower() == "y":
                    print("Logging out ...")
                    input()
                    return None
                elif logoutanswer.lower() == "n":
                    input("Ok, not logging out.")
                else: 
                    input("input not recognized. type 'y' or 'n' ")

        elif answer =="0":
            exit()

        else:
            input("Input nog recognized")