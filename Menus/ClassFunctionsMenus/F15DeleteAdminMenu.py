from Functions.DatabaseFunctions import deleteEntry


def deleteAdminMenu(user):
    ''' 
    the interactive menu for SuperAdmin.deleteAdmin()
    '''

    print("[DEV] deleteAdminMenu()")
    
    username = input("Type the username of the Admin you wish to delete : ")
    user.deleteAdmin('SysAdmins', 'username', username)
    input("Press 'enter' to continue ... ")
    