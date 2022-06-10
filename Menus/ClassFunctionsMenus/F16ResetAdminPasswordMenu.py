from Functions.Auxfunctions import generateRandomPassword
from Functions.DatabaseFunctions import resetPassword, updateEntry


def resetAdminPasswordMenu(user):
    '''
    the interactive menu for SuperAdmin.resetAdminPassword()
    TODO: make sure the username actually exists in the databases
    '''
    newpass = generateRandomPassword()

    username = input("Enter the username of the SysAdmin from which you want to reset the password: ")

    resetPassword('SysAdmins', 'password', newpass, 'username', username)

    print(f"The new password is: {newpass}\nRemember it well.")