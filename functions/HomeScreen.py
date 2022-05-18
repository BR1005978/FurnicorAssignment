import functions.Login as Login

def homeScreen():
    '''intro screen '''

    print("Welcome to Furnicor Family System v0.01")

    while True:
        print(
            """
            1. Login\n
            2. Exit
            """)

        answer = input("input: ")

        if answer =="1":
            Login.loginScreen()
        elif answer =="2":
            break
        else:
            print("Input nog recognized")