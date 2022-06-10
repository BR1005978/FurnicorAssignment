from Functions.Auxfunctions import generateRandomPassword
from Functions.DatabaseFunctions import resetPassword, updateEntry


def resetAdvisorPassword(user):
    '''
    the interactive menu for SysAdmin.resetAdvisorPassword
    TODO: make sure the username actually exists in the databases
    '''
    newpass = generateRandomPassword()

    username = input("Enter the username of the advisor from which you want to reset the password: ")

    resetPassword('Advisors', 'password', newpass, 'username', username)

    print(f"The new password is: {newpass}\nRemember it well.")