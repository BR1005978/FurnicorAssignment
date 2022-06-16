import email
import os
from Functions.CheckFunctions import *
from Functions.Logfunction import LogData

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def addNewMemberMenu(user):
    '''
    the menu for creating a new member. asking all the required
    fields and then attempting to add it to the database

    this is not very secure or robust yet as of 2-6-2022
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
        city = input("""Enter one of the following cities: 
Kapellerdijk
Botervuik
Hendrik-Ambacht
Rotterdijk
Hoogkerk
Vislandserdorp
Heerenvoorn
Drollendam
Koningsveen
Muizendam
city: """)
        if checkCity(city):
            return city
        else:
            print("Wrong city format. Please use one of the provided cities.")
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
        except:
            print("Errorcode ANMM2: something unknown happened")
    elif answer.lower() == 'n':
        print("OK. Aborting function.")