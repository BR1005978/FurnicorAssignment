from Menus.Login import loginScreen
from Menus.InfoScreen import displayInfo

def homeScreen():
    '''intro screen '''
    print(
        """    ______                     _                   
   / ____/__  __ _____ ____   (_)_____ ____   _____
  / /_   / / / // ___// __ \ / // ___// __ \ / ___/
 / __/  / /_/ // /   / / / // // /__ / /_/ // /    
/_/     \__,_//_/   /_/ /_//_/ \___/ \____//_/     
""")
    print("Welcome to Furnicor Family System v0.01")

    currentUser = "" 

    # does this make any sense?
    while currentUser == "":
        currentUser = homeScreenNoUser()
    

    print("someone logged in! : ", currentUser)

    homeScreenWithUser(currentUser)

### losse functies voor de situatie waarin je als gebruiker bent ingelogd ? is dat handig
### en nog een functie voor zonder gebruiker?
def homeScreenNoUser():
        print(
            """
1. Log in\n
2. Display program info\n
3. Exit
            """)

        answer = input("Select the number of an option and press enter : ")

        if answer =="1":
            # werkt dit? 
            return loginScreen()
        elif answer =="2":
            displayInfo()
        elif answer =="3":
            exit()
        else:
            print("Input nog recognized")

def homeScreenWithUser(user):
    print("Welcome user: ", user)
    while True:
        print(
                """
    1. Log out\n
    2. Display program info\n
    3. Exit
                """)
        answer = input("Select the number of an option and press enter : ")

        if answer =="1":
            print("Logout function: not yet implemented")
            break
        elif answer =="2":
            displayInfo()
        elif answer =="3":
            exit()
        else:
            print("Input nog recognized")
