import email
import os
from sqlite3 import IntegrityError
from Functions.CheckFunctions import *
from Functions.Logfunction import LogData

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def addMemberMenu(user):
    '''
    the menu for creating a new member. asking all the required
    fields and then attempting to add it to the database


    '''
    
    firstname = input("Input first name: ")
    
    lastname = input("Input last name: ")
    
    streetname = input("Input street name: ")

    def housenumberfunc():
        housenumber = input("Enter house number: ")
        if checkHouseNumber(housenumber):
            return housenumber
        else:
            print("Wrong housenumber format. Please only use numbers")
            return housenumberfunc()
    
    housenumber = housenumberfunc()

    def zipcodefunc():
        zipcode = input("Enter zipcode: ")
        if checkZipCode(zipcode):
            return zipcode
        else:
            print("Wrong zipcode format. Please use this format: ")
            return zipcodefunc()
    
    zipcode = zipcodefunc()

    def cityfunc():
        answer = input("""Select one of the following cities: 
1.    Kapellerdijk
2.    Botervuik
3.    Hendrik-Ambacht
4.    Rotterdijk
5.    Hoogkerk
6.    Vislandserdorp
7.    Heerenvoorn
8.    Drollendam
9.    Koningsveen
10.   Muizendam
city: """)
        if answer == '1':
            return "Kapellerdijk"
        elif answer == '2':
            return 'Botervuik'
        elif answer == '3':
            return 'Hendrik-Ambacht'
        elif answer == '4':
            return 'Rotterdijk'
        elif answer == '5':
            return 'Hoogkerk'
        elif answer == '6':
            return 'Vislandserdorp'
        elif answer == '7':
            return 'Heerenvoorn'
        elif answer == '8':
            return 'Drollendam'
        elif answer == '9':
            return 'Koningsveen'
        elif answer == '10':
            return 'Muizendam'

        else:
            input("Input not recognized, please try again... ")
            return cityfunc()
    city = cityfunc()


    def emailfunc():
        email = input("Enter the e-mail address: ")
        if checkEmail(email):
            return email
        else:
            print("Wrong email format. Please use this format: text@text.text")
            return emailfunc()
    
    emailAddress = emailfunc()

    def phonenumberfunc():
        phonenumber = input("Enter phone number: +31-6")
        if checkPhonenumber(phonenumber):
            return phonenumber
        else:
            print("Wrong phonenumber format. Please use only use 8 numbers")
            return phonenumberfunc()
    
    phonenumber = phonenumberfunc()



    address = f"{streetname} {housenumber}, {zipcode} {city}"

    print(f"""
    Are these correct?

    First name: {firstname}
    Last name: {lastname}
    Home address: {address}
    E-mail address: {emailAddress}
    Phone number: 31-6-{phonenumber}
    """)

    answer = input("Y/N : ")

    if answer.lower() == 'y':
        try:
            user.addNewMember(firstname,lastname,address,emailAddress,phonenumber)
            clearConsole()
            print("Member added.")
        except ValueError:
            print("Errorcode ANMM1: some value error popped up while trying to add a member to the database.")
        except IntegrityError:
            print("Database injection failed. Max character length exceeded. ")
            input("Press enter to continue...")
        except:
            print("Errorcode ANMM2: something unknown happened")
            input()
    elif answer.lower() == 'n':
        print("OK. Aborting function.")