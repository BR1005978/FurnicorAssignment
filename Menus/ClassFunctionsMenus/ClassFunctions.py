from Functions.createDummyData import createDummyData
from Menus.ClassFunctionsMenus.F10BackupSystemMenu import backupSystemMenu
from Menus.ClassFunctionsMenus.F12DeleteMemberMenu import deleteMemberMenu
from Menus.ClassFunctionsMenus.F13AddAdminMenu import addAdminMenu
from Menus.ClassFunctionsMenus.F14ModifyAdminMenu import modifyAdminMenu
from Menus.ClassFunctionsMenus.F15DeleteAdminMenu import deleteAdminMenu
from Menus.ClassFunctionsMenus.F16ResetAdminPasswordMenu import resetAdminPasswordMenu
from Menus.ClassFunctionsMenus.F2AddMemberMenu import addMemberMenu
from Menus.ClassFunctionsMenus.F6AddAdvisorMenu import createNewAdvisorMenu
from Menus.ClassFunctionsMenus.F3ModifyMemberMenu import modifyMemberMenu
from Menus.ClassFunctionsMenus.F5QueryUsersMenu import queryUsersMenu
from Menus.ClassFunctionsMenus.F1UpdateOwnPasswordMenu import updateOwnPasswordMenu
from Menus.ClassFunctionsMenus.F4QueryMembersMenu import queryMembersMenu
from Menus.ClassFunctionsMenus.F7ModifyAdvisorMenu import modifyAdvisorMenu
from Menus.ClassFunctionsMenus.F8DeleteAdvisorMenu import deleteAdvisorMenu
from Menus.ClassFunctionsMenus.F9ResetAdvisorPasswordMenu import resetAdvisorPassword
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

    10. Create or restore backup

    11. Show the logs

    12. Delete a member""")
        ####################

        ####################
        # display superadmin functions
        if isinstance(user, SuperAdmin):
            print("""
    13. Add admin

    14. Modify admin

    15. Delete admin

    16. Reset admin password
    
    17. Create dummy data""")
        ####################



        print ("""
    0. Return to previous menu
    """ )
        answer = input("Type the number of an option and press enter : ")

        if answer == "1":
            updateOwnPasswordMenu(user)
            classFunctionsMenu(user)
    
        elif answer == "2":
            addMemberMenu(user)

        elif answer == "3":
            modifyMemberMenu(user)

        elif answer == "4":
            queryMembersMenu(user)
            
        
        elif isinstance(user, SysAdmin):
            if answer == "5":
                queryUsersMenu(user)
                input()
            
            elif answer == "6":
                createNewAdvisorMenu(user)
            
            elif answer == "7": 
                modifyAdvisorMenu(user)
                input()
            
            elif answer == "8": 
                deleteAdvisorMenu(user)
            
            elif answer == "9": 
                resetAdvisorPassword(user)
                input()
            
            elif answer == "10": 
                backupSystemMenu(user)
            
            elif answer == "11": 
                print("Show logs function not yet implemented ")
                input()
            
            elif answer == "12": 
                deleteMemberMenu(user)
            elif answer != "0" and type(user) != SuperAdmin:
                print("(sysadmin) input not recognized")
                input()

        
        elif type(user) == SuperAdmin:
            if answer == "13":
                addAdminMenu(user)
                input()
                
            elif answer == "14":
                modifyAdminMenu(user)
                input()

            elif answer == "15":
                deleteAdminMenu(user)
                
            elif answer == "16":
                resetAdminPasswordMenu(user)

            elif answer == "17":
                createDummyData()


            elif answer != "0":
                print("(superadmin) input not recognized")
                input()




        elif answer == "0":
            break
        

        else:
            print("input not recognized")
            input()
 