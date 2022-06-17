import os
import sqlite3
from Functions.CheckFunctions import passwordCheck
from Functions.Logfunction import LogData, logSuspicious
from Userclasses.AdvisorClass import Advisor
from Userclasses.SysAdminClass import SysAdmin
from Userclasses.SuperAdminClass import SuperAdmin

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def updateOwnPasswordMenu(user):
    '''
    brings up a menu where a user can attempt to update its password. 

    to do: also adjust new password in database
    '''

    print("[DEV]updateOwnPassword()")

    while True:
        pw1 = input("Enter new password  : ")
        pw2 = input("Repeat password     : ")

        if pw1 != pw2:
            
            answer = input("The two passwords must be identical, please try again. Or type 'Q' to cancel ")
            if answer.lower() == "q":
                break
        else:
            pwcheck = passwordCheck(pw1)
            if pwcheck == True:

                
                if type(user) == Advisor or type(user) == SysAdmin:
                    # try: 
                    user.updateOwnPassword(pw1) 
                    clearConsole() 
                    print(f"Updating {user.sayType} password succeeded (presumably)")
                    LogData(user.username, "Changed password", sus = "no")  
                    break
                    # except: 
                    #     print("something went wrong")
                elif type(user) == SuperAdmin:
                    print("ERROR: cannot change SuperAdmin's password. The teachers would become angry... ")
                    print("Press enter to continue ... ")
                    
                    logSuspicious(user.username, "Attempted to change SuperAdmin password", "very sus", "Yes")

                print("Password succesfully updated, I think? ")
            else:
                print(pwcheck)
                LogData(user.username, "Password change failed",sus="no")
                answer = input("Press enter to try again, or press 'Q' to quit this menu.")
                if answer.lower() == "q":
                    break
        
