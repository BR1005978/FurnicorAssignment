import os
from turtle import clear
from Menus.HomeScreens.HomeScreenNoUser import homeScreenNoUser
from Menus.HomeScreens.HomeScreenWithUser import homeScreenWithUser
from Menus.Login import loginScreen
from Menus.Info.InfoScreen import displayInfo

from Userclasses.AdvisorClass import Advisor
from Userclasses.SysAdminClass import SysAdmin

from Menus.ClassFunctionsMenus.ClassFunctions import classFunctionsMenu
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

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

    while True:
        currentUser = None 
        while currentUser == None:
            clearConsole()
            print(
        """    ______                     _                   
   / ____/__  __ _____ ____   (_)_____ ____   _____
  / /_   / / / // ___// __ \ / // ___// __ \ / ___/
 / __/  / /_/ // /   / / / // // /__ / /_/ // /    
/_/     \__,_//_/   /_/ /_//_/ \___/ \____//_/     
""")
            print("Welcome to Furnicor Family System v0.3")
            currentUser = homeScreenNoUser()
        print("Succesfully logged in as : ", currentUser)

        while currentUser != None:
            currentUser = homeScreenWithUser(currentUser)