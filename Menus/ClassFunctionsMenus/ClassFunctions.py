from Menus.ClassFunctionsMenus.AddNewMember2 import addNewMemberMenu
from Userclasses.SysAdminClass import SysAdmin
from Userclasses.SuperAdminClass import SuperAdmin


def classFunctionsMenu(user):

    answer = ""


    while answer != "0":
        ####################
        # display advisor functions
        print(f"""
    {user.sayType()} functions

    1. Update own password
    
    2. Add new member

    3. Modify existing member

    4. Search member in database""")
        ####################


        ####################
        # display sysadmin functions
        if isinstance(user, SysAdmin):
            print("""
    5. Search users (advisors or sysadmins) in database

    6. Create new advisor

    7. Modify existing advisor

    8. Delete an advisor

    9. Reset an advisor's password

    10. Make a backup of the system

    11. Show the logs

    12. Delete a member""")


        ####################
        # display superadmin functions
        if isinstance(user, SuperAdmin):
            print("""
    13. Add admin

    14. Modify admin

    15. Delete admin

    16. Reset admin password""")
        ####################



        print ("""
    0. Return to previous menu
    """ )
        answer = input("Type the number of an option and press enter : ")

        if answer == "1":
            print("updating own password not yet implemented")
            input()
    
        elif answer == "2":
            addNewMemberMenu(user)
            input("option 2, did it work?")
            
        elif answer == "3":
            print("modify member not yet implemented")
            input()

        elif answer == "4":
            print("search member in database not yet implemented")
            input()
        
        elif isinstance(user, SysAdmin):
            if answer == "5":
                print("Search users function not yet implemented")
                input()
            
            elif answer == "6":
                print("Create new advisor function not yet implemented")
                input()
            
            elif answer == "7": 
                print("Modify advisor function not yet implemented ")
                input()
            
            elif answer == "8": 
                print("Delete an advisor function not yet implemented ")
                input()
            
            elif answer == "9": 
                print("Reset advisor's password function not yet implemented ")
                input()
            
            elif answer == "10": 
                print("Create backup function not yet implemented ")
                input()
            
            elif answer == "11": 
                print("Show logs function not yet implemented ")
                input()
            
            elif answer == "12": 
                print("Delete member function not yet implemented ")
                input()
            elif answer != "0":
                print("(sysadmin) input not recognized")
                input()

        
        elif type(user) == SuperAdmin:
            if answer == "13":
                print("Add admin function not yet implemented")
                input()
                
            elif answer == "14":
                print("Modify admin function not yet implemented")
                input()

            elif answer == "15":
                print("Delete admin function not yet implemented")
                input()
                
            elif answer == "16":
                print("Reset admin password function not yet implemented")
                input()
            elif answer != "0":
                print("(superadmin) input not recognized")
                input()




        elif answer == "0":
            break
        

        #B1 waarom komt het programma niet op dit punt wanneer de gebruiker een super admin is? wtf
        else:
            print("input not recognized")
            input()
 