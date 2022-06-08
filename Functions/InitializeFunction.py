import sqlite3



def initializer():

    '''
    the functions that initialize the database. think of the functions that make the tables if there are none yet. 
    so the functions that get executed on the first time starting up this program
    '''

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    #create SysAdmins table

    print('initializer()')

    print("attempting SysAdmins table creation ...")

    try:
        DBcursor.execute("""
            CREATE TABLE SysAdmins (
                username TEXT PRIMARY KEY, 
                password TEXT
                )""")
    except sqlite3.OperationalError:
        print("Table SysAdmins already exists.")
    except:
        print("Unknown error in database table creation")
    else:
        print("SysAdmins table created")




    #create advisors table

    print("attempting Advisor table creation ...")
    try:
        DBcursor.execute("""
            CREATE TABLE Advisors (
                username TEXT PRIMARY KEY, 
                password TEXT
                )""")
    except sqlite3.OperationalError:
        print("Table Advisors already exists.")
    except:
        print("Unknown error in database table creation")
    else:
        print("Advisors table created")



    #create Members table

    print("attempting Members table creation ...")
    try:
        DBcursor.execute("""
            CREATE TABLE Members (
                membershipID integer PRIMARY KEY,
                firstname text, 
                lastname text,
                address text,
                email text,
                phonenumber text,
                registrationdate text
                )""")
    except sqlite3.OperationalError:
        print("Table Members already exists.")
    except:
        print("Unknown error in database table creation")
    else:
        print("Members table created")


    databaseConnection.commit()

    databaseConnection.close()



