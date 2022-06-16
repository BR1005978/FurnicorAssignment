from multiprocessing.sharedctypes import Value
from Functions.CheckFunctions import passwordCheck, usernameCheck


def createNewAdvisorMenu(user):
    '''
    takes the current user as an argument for logging purposes, nothing else

    TODO: add input validation and security
    '''

    print("[DEV] createNewAdvisorMenu()")
    firstname = input("Enter the first name of the new advisor: ")
    lastname = input("Enter the last name of the new advisor: ")
    username = input("Enter the username of the new advisor: ")
    if usernameCheck(username) == ValueError:
        print(usernameCheck(username))
        return


    else:
        while True:
            pw1 = input("Enter new password  : ")
            pw2 = input("Repeat password     : ")

            if pw1 != pw2:
                
                answer = input("The two passwords must be identical, please try again. Or type 'Q' to cancel ")
                if answer.lower() == "q":
                    break
            else:
                pwcheck = passwordCheck(pw1)
                if pwcheck == True:
                    #add new advisor to database
                    user.addAdvisor(username, pw1, firstname, lastname)
                    break
                else:
                    print(pwcheck)
                    answer = input("Press enter to try again, or press 'Q' to quit this menu.")
                    if answer.lower() == "q":
                        break

