from Functions.CheckFunctions import checkString
from Functions.Logfunction import Log


def addNewMemberMenu(user):
    '''
    the menu for creating a new member. asking all the required
    fields and then attempting to add it to the database

    this is not very secure or robust yet as of 2-6-2022
    '''

    firstname = input("Enter the first name of the member: ")
    #checkString(firstname)
    lastname = input("Enter the last name of the member: ")
    #checkString(lastname)
    streetname = input("Enter street name: ")

    housenumber = input("Enter house number: ")

    zipcode = input("Enter zipcode: ")

    city = input("Enter city: ")

    email = input("Enter the e-mail address: ")

    phonenumber = input("Enter the phonenumber: ")



    address = f"{streetname} {housenumber}, {zipcode}, {city}"

    print(f"""
    Are these correct?

    First name: {firstname}
    Last name: {lastname}
    Home address: {address}
    E-mail address: {email}
    Phone number: 31-6-{phonenumber}
    """)

    answer = input("Y/N : ")

    if answer.lower() == 'y':
        try:
            user.addNewMember(firstname,lastname,address,email,phonenumber)
            input("Member added. Press 'enter' to continue... ")
        except ValueError:
            print("Errorcode ANMM1: some value error popped up while trying to add a member to the database.")
        except:
            print("Errorcode ANMM2: something unknown happened")
    elif answer.lower() == 'n':
        print("OK. Aborting function.")