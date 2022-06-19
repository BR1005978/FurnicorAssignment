from Functions.DatabaseFunctions import deleteEntry


def deleteAdminMenu(user):
    ''' 
    the interactive menu for SuperAdmin.deleteAdmin()
    '''

    
    username = input("Type the username of the Admin you wish to delete : ")
    user.deleteAdmin(username)
    input("Press 'enter' to continue ... ")
    