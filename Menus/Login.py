'''functions for logging in'''

def loginScreen():

    '''
    asks the user for a username and password, and queries the database to see if there is an overlap
    '''

    
    print("loginScreen()")

    username = input("Username: ")
    password = input("Password: ")


    return f"inputted username: {username} \ninputted password: {password}"
    