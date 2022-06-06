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

                ###TD1 update password in database

                databaseConnection = sqlite3.connect('FurnicorDatabase.db')
                DBcursor = databaseConnection.cursor()
                
                if type(user) == Advisor:
                    try: 
                        DBcursor.execute(f"""
                        UPDATE Advisors
                        SET password = '{pw1}'
                        WHERE username = '{user.username}'
                        """)  
                        print("Updating Advisor password succeeded (presumably)")  
                    except: 
                        print("something went wrong")
                elif type(user) == SysAdmin:    
                    try:
                        DBcursor.execute(f"""
                        UPDATE SysAdmins
                        SET password = '{pw1}'
                        WHERE username = '{user.username}'
                        """ )
                        print("Updating SysAdmin password succeeded (presumably)")
                    except:
                        print("updating SysAdmin password failed for some reason")
                elif type(user) == SuperAdmin:
                    print("Error: cannot change SuperAdmin's password. The teachers would become angry... ")
                    print("Press enter to continue ... ")


                print("Password succesfully updated, I think? ")
            else:
                print(pwcheck)
                answer = input("Press enter to try again, or press 'Q' to quit this menu.")
                if answer.lower() == "q":
                    break
        
