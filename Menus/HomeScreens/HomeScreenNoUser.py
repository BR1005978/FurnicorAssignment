from Functions.InitializeFunction import initializer
from Functions.createDummyData import createDummyData
from Menus.Login import loginScreen
from Menus.Info.InfoScreen import displayInfo
from Userclasses.AdvisorClass import Advisor
from Userclasses.SuperAdminClass import SuperAdmin
from Userclasses.SysAdminClass import SysAdmin
from deprecated.SQLite import SQLite3fiddle

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

    0. Shut down program
            """)

        answer = input("Type the number of an option and press enter : ")

        if answer =="1":
            return loginScreen()
        elif answer =="2":
            displayInfo()
        elif answer == "7":
            return Advisor("advisorAccount1")
        elif answer =="8":
            return SysAdmin('sysadmin123')
        elif answer =="9":
            return SuperAdmin()
        elif answer.lower() == "a":
            SQLite3fiddle()
        elif answer.lower() == "b":
            initializer()
            createDummyData()
        elif answer =="0":
            exit()
        else:
            input("Input nog recognized")