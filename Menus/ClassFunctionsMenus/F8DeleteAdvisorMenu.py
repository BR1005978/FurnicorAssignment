from Functions.DatabaseFunctions import deleteEntry
from Functions.Logfunction import LogData


def deleteAdvisorMenu(user):
    '''
    the interactive menu for SysAdmin.deleteAdvisor

    
    '''

    
    username = input("Type the username of the advisor you wish to delete : ")
    user.deleteAdvisor(username)
    LogData(user.username, "Deleted an advisor", username)
    input("Press 'enter' to continue ... ")
    