from Functions.Logfunction import showSus
from Functions.createDummyData import createDummyData
from Menus.ClassFunctionsMenus.F10BackupSystemMenu import backupSystemMenu
from Menus.ClassFunctionsMenus.F11ShowLogsMenu import showLogsMenu
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

    16. Reset admin password""")
        ####################



        print ("""
    0. Return to previous menu
    """ )
        answer = input("Type the number of an option and press enter : ")

        if answer == "1":
            updateOwnPasswordMenu(user)
            break

        elif answer == "2":
            addMemberMenu(user)
            break

        elif answer == "3":
            modifyMemberMenu(user)
            break
        elif answer == "4":
            queryMembersMenu(user)
            break
        
        if isinstance(user, SysAdmin):
            if answer == "5":
                queryUsersMenu(user)
                break
            elif answer == "6":
                createNewAdvisorMenu(user)
                break
            elif answer == "7": 
                modifyAdvisorMenu(user)
                break
            
            elif answer == "8": 
                deleteAdvisorMenu(user)
                break
            elif answer == "9": 
                resetAdvisorPassword(user)
                break
            
            elif answer == "10": 
                backupSystemMenu(user)
                break
            elif answer == "11": 
                showLogsMenu(user)
                break
            
            elif answer == "12": 
                deleteMemberMenu(user)
                break
            elif answer != "0" and type(user) != SuperAdmin:
                print("...")
                input()

        
        if type(user) == SuperAdmin:
            if answer == "13":
                addAdminMenu(user)
                break
                
            elif answer == "14":
                modifyAdminMenu(user)
                break

            elif answer == "15":
                deleteAdminMenu(user)
                break

            elif answer == "16":
                resetAdminPasswordMenu(user)
                break
            
            # elif answer == "17":
            #     createDummyData()

            elif answer != "0":
                print("...")
                input()




        elif answer == "0":
            break
        

        else:
            print("...")
            input()
 