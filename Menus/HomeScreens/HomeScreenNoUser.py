from Menus.Login import loginScreen
from Menus.Info.InfoScreen import displayInfo
from Userclasses.AdvisorClass import Advisor
from Userclasses.SuperAdminClass import SuperAdmin
from Userclasses.SysAdminClass import SysAdmin

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

    7. [DEV] Quick login as Advisor (beeboo, bungbung)

    8. [DEV] Quick login as Super Admin(superadmin, Admin321!)

    9. [DEV] Quick login as SysAdmin (sysadmin123, sysadminpassword)

    0. Shut down program
            """)

        answer = input("Type the number of an option and press enter : ")

        if answer =="1":
            return loginScreen()
        elif answer =="2":
            displayInfo()
        elif answer == "7":
            return Advisor("beeboo","bungbung")
        elif answer =="8":
            return SuperAdmin()
        elif answer =="9":
            return SysAdmin('sysadmin123', 'sysadminpassword')
        elif answer =="0":
            exit()
        else:
            input("Input nog recognized")