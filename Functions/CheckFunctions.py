'''
CheckFunctions.py contains typechecking functions such as passwordcheck, usernamecheck, etc
'''


print("CheckFunctions.py")

# some variables to be used in following functions 

letterlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers1 = list(range(0,10))
numbers = [str(i) for i in numbers1]

def passwordCheck(password):
    '''
    checks the password for a valid format:

    - Password must have a length of at least 8 characters
    - Cannot be longer than 30 characters
    - Can contain letters (a-z), (A-Z), numbers (0-9), special characters such as ~!@#$%&_-+=`|\(){}[]:;'<>,.?\n
    - Must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character
    '''
    print("passwordCheck()")

    lettercount = 0
    digitcount = 0

    speccharlist= ["~","!", "@", "#", "$", "%", "&", "_" ,"-","+","=","`","|","\\","(",")", "{","}","[","]",":",";"","<",">",",",",".","?"]
    speccharcount = 0


    if len(password) > 30:
        return ValueError("Error: This password is too long")
    if len(password) < 8:
        return ValueError("Error: This password is too short")
    if password == password.lower():
        return ValueError("Error: Password must contain at least one lowercase and one uppercase letter")

    for i in range(len(password)):
        if password[i].lower() in letterlist:
            lettercount+=1
        elif password[i] in numbers:
            digitcount+=1
        elif password[i] in speccharlist:
            speccharcount+=1 
        else:
            return ValueError("Error: false input detected")

    if lettercount < 1:
        return ValueError("Error: The password must have at least one letter")
    if digitcount < 1:
        return ValueError("Error: The password must have at least one digit")
    if speccharcount < 1:
        return ValueError("Error: The password must have at least one special symbol")

    return True



def usernameCheck(username):
    '''
    checking the username for validity

    ○ must be unique and have a length of at least 6 characters

    ○ must be no longer than 10 characters

    ○ must be started with a letter

    ○ can contain letters (a-z), numbers (0-9), underscores (_), apostrophes ('), and periods (.)

    ○ no distinguishing between lowercase and uppercase letters
    '''

    if not (isinstance(username, str)):
        return ValueError("Error: some weird shit just happened. How did you manage to not make the username a string?")


    usernameAllowedsymbols = ["_", "\'", "."]

    # checking for length and first character
    if len(username) < 6:
        return ValueError("Error: username must have at least 6 characters")
    if len(username) > 10: 
        return ValueError("Error: username cannot be longer than 10 characters")
    if (username[0].lower() not in letterlist):
        return ValueError("Error: first character of username must be a letter")
    
    # typechecking dat boi
    for i in range(len(username)):
        if username[i].lower() not in [*letterlist, *numbers, *usernameAllowedsymbols]:
            return ValueError(f"Error: '{username[i]}' is not allowed in usernames")
    
    return True













###testenv
# while True:
#     password = input("enter password: ")

#     outcome = passwordCheck(password)


#     if isinstance(outcome, ValueError):
#         print("this is a value error: ", outcome)
#     else:
#         print("password probably correct")



# while True:
#     usernayme = input("enter username: ")

#     outcomeUsername = usernameCheck(usernayme)

#     if isinstance(outcomeUsername, ValueError):
#         print("this is a value error: ", outcomeUsername)
#     else:
#         print("username probably correct", usernayme)