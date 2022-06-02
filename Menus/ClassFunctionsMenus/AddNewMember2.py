def addNewMemberMenu(user):
    '''
    the menu for creating a new member. asking all the required
    fields and then attempting to add it to the database

    this is not very secure or robust yet as of 2-6-2022
    '''
    firstname = input("Enter the first name of the member: ")
    lastname = input("Enter the last name of the member: ")
    address = input("Enter the address of the member: ")
    email = input("Enter the e-mail address of the member: ")
    phonenumber = input("Enter the phonenumber of the member: ")

    print(f"""
    Are these correct?

    First name: {firstname}
    Last name: {lastname}
    Home address: {address}
    E-mail address: {email}
    Phone number: {phonenumber}
    """)

    answer = input("Y/N : ")

    if answer.lower() == 'y':
        try:
            user.addNewMember(firstname,lastname,address,email,phonenumber)
        except ValueError:
            print("Errorcode ANMM1: some value error popped up while trying to add a member to the database.")
        except:
            print("Errorcode ANMM2: something unknown happened")
    elif answer.lower() == 'n':
        print("OK. Aborting function.")