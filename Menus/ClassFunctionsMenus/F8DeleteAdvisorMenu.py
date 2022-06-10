from Functions.DatabaseFunctions import deleteEntry


def deleteAdvisorMenu(user):
    '''
    the interactive menu for SysAdmin.deleteAdvisor

    
    '''
    print("[DEV] deleteAdvisorMenu()")
    
    username = input("Type the username of the advisor you wish to delete : ")
    user.deleteAdvisor('Advisors', 'username', username)
    input("Press 'enter' to continue ... ")
    