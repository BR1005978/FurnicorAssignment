from Functions.CheckFunctions import passwordCheck, usernameCheck
from Functions.Logfunction import logSuspicious


def addAdminMenu(user):
    '''
    the interactive menu for SuperAdmin.addAdmin()
    '''


    firstname = input("Enter the first name of the new admin: ")
    lastname = input("Enter the last name of the new admin: ")
    username = input("Enter the username of the new admin: ")
    if usernameCheck(username) == ValueError:
        print(usernameCheck(username))
        logSuspicious(user.username, "attempted creation of admin failed with username", username)
        return
    else:
        i = 0
        while i < 3:
            pw1 = input("Enter new password  : ")
            pw2 = input("Repeat password     : ")

            if pw1 != pw2:
                
                answer = input("The two passwords must be identical, please try again. Or type 'Q' to cancel ")
                if answer.lower() == "q":
                    break
            else:
                pwcheck = passwordCheck(pw1)
                if pwcheck == True:
                    #add new Admin to database
                    user.addAdmin(firstname, lastname, username, pw1)
                    break
                else:
                    print(pwcheck)
                    answer = input("Press enter to try again, or press 'Q' to quit this menu.")
                    if answer.lower() == "q":
                        break
            print("Maximum attempts exceeded. Logging data. ")
            logSuspicious(user.username, "Failed to create admin after several attempts")