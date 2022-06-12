import sqlite3
from Functions.CheckFunctions import passwordCheck
from Userclasses.AdvisorClass import Advisor
from Userclasses.SysAdminClass import SysAdmin
from Userclasses.SuperAdminClass import SuperAdmin


def updateOwnPasswordMenu(user):
    '''
    brings up a menu where a user can attempt to update its password. 

    to do: also adjust new password in database
    '''

    print("updateOwnPassword()")

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
                    print(f"Updating {user.sayType} password succeeded (presumably)")  
                    break
                    # except: 
                    #     print("something went wrong")
                elif type(user) == SuperAdmin:
                    print("ERROR: cannot change SuperAdmin's password. The teachers would become angry... ")
                    print("Press enter to continue ... ")


                print("Password succesfully updated, I think? ")
            else:
                print(pwcheck)
                answer = input("Press enter to try again, or press 'Q' to quit this menu.")
                if answer.lower() == "q":
                    break
        
