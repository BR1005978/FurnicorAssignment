from Menus.Login import loginScreen
from Menus.Info.InfoScreen import displayInfo

from Userclasses.AdvisorClass import Advisor
from Userclasses.SysAdminClass import SysAdmin
'''

the main menus of this program.

three functions: 

1. homeScreen() which initiates the main menu
2. homeScreenNoUser() for when there is no user logged in
3. homeScreenWithUser() for when there is a user logged in 


'''


def homeScreen():
    '''
    the main function that shows the homescreen and allows passage to the 
    homescreenNoUser and homeScreenWithUser functions. 

    '''
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
        

        print("Succesfully logged in as : ", currentUser)
        input("Press any key to continue ... ")

        while currentUser != None:
            currentUser = homeScreenWithUser(currentUser)



def homeScreenNoUser():
        '''
        the screen that gets shown when NO user is logged in

        returns: a user
        '''

        print(
            """
    Hello, anonymous user.\n
    1. Log in

    2. Display program info

    9. [DEV] Quick login as SysAdmin (sysadmin123, sysadminpassword)

    0. Exit
            """)

        answer = input("Select the number of an option and press enter : ")

        if answer =="1":
            return loginScreen()
        elif answer =="2":
            displayInfo()
        elif answer =="9":
            return SysAdmin('sysadmin123', 'sysadminpassword')
        elif answer =="0":
            exit()
        else:
            input("Input nog recognized")



def homeScreenWithUser(user):
    '''
    the screen that is shown when a user is succesfully logged in

    returns: None

    it only returns None when you want to log out 
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


        if answer =="1":
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
            
        
        elif answer =="2":
            displayInfo()

        elif answer == "9":
            print(type(user))
            input()

        elif answer =="0":
            exit()

        else:
            input("Input nog recognized")
