import sqlite3
from venv import create
from Auxfunctions import generateUserID
from datetime import date


def wipeDatabase():
    '''
    this function wipes all entries in the database. use with caution
    '''
    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    tables = ['Advisors', 'SysAdmins', 'Members']
    for table in tables:
        DBcursor.execute(f"""DELETE FROM {table}""")

    databaseConnection.commit()
    databaseConnection.close()



def createDummyData():
    '''
    This function fills the database with dummy data. 
    insert random members, advisors and sysadmins etc into all 3 tables
    '''

    databaseConnection = sqlite3.connect('FurnicorDatabase.db')
    DBcursor = databaseConnection.cursor()

    ### insert advisors into database
    DBcursor.execute("""
    INSERT INTO Advisors
    VALUES(
        'dummyAdvisor',
        'advisorpassword'
    )
    """)
    
    
    DBcursor.execute("""
    INSERT INTO Advisors
    VALUES(
        'lameAdvisor',
        'advisorpassword2'
    )
    """)

    
    DBcursor.execute("""
    INSERT INTO Advisors
    VALUES(
        'Richard123',
        'crazychicken'
    )
    """)

    
    DBcursor.execute("""
    INSERT INTO Advisors
    VALUES(
        'Jacket5',
        'HotlineFlorida'
    )
    """)

    
    DBcursor.execute("""
    INSERT INTO Advisors
    VALUES(
        'beeboo',
        'bungbung'
    )
    """)

    DBcursor.execute("""
    INSERT INTO Advisors
    VALUES(
        'stonkerino.supremo',
        'snickers'
    )
    """)


    ### insert SysAdmins into table
    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'chillerino',
        'youllneverguessthis'
    )
    """)

    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'sysadmin123',
        'sysadminpassword'
    )
    """)

    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'getrekt555',
        'some_damn_secret_password'
    )
    """)

    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'chillywilly',
        'snorkadork9325'
    )
    """)

    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'woolybully',
        'lecoqsportif'
    )
    """)

    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'derperinosupremo',
        'passworderinosupremo'
    )
    """)

    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'BIMPF',
        'knollzors'
    )
    """)

    DBcursor.execute("""
    INSERT INTO SysAdmins
    VALUES(
        'turdslug.Maximo',
        'cheesesticks'
    )
    """)

    ### insert members into database
    DBcursor.execute(f"""
    INSERT INTO Members
    VALUES(
        '{generateUserID()}',
        'Knoert',
        'Klokiebril',
        'Stronkstraat 85, Otterdam',
        'k.klokerino@bonkmail.com',
        '31-6-58785232',
        '{date.today()}'
    )
    """)

    DBcursor.execute(f"""
    INSERT INTO Members
    VALUES(
        '{generateUserID()}',
        'Sjaak',
        'Sjouwer',
        'Pronkstraat 88, Drollendam',
        'boterhammetje85@live.nl',
        '31-6-55447895',
        '{date.today()}'
    )
    """)    

    DBcursor.execute(f"""
    INSERT INTO Members
    VALUES(
        '{generateUserID()}',
        'Jos',
        'Brulvink',
        'Pokémonstraat 103, Heerenvoorn',
        'brullerino@gmail.com',
        '31-6-12969545',
        '{date.today()}'
    )
    """)    

    DBcursor.execute(f"""
    INSERT INTO Members
    VALUES(
        '{generateUserID()}',
        'Terry',
        'Tarrelbraft',
        'Snaakstraat 5, Hoogkerk',
        'tarreltjeknarreltje@outlook.com',
        '31-6-17879325',
        '{date.today()}'
    )
    """)

    DBcursor.execute(f"""
    INSERT INTO Members
    VALUES(
        '{generateUserID()}',
        'Berend',
        'Baardhuis',
        'Plopstraat 953, Plopsaland',
        'plopperdeplopperdeplop@plopmail.plop',
        '31-6-11223344',
        '{date.today()}'
    )
    """)    

    DBcursor.execute(f"""
    INSERT INTO Members
    VALUES(
        '{generateUserID()}',
        'Snoek',
        'van der Snor',
        'Zwemstraat 23, Vislandserdorp',
        'snorrrrr@snormail.org',
        '31-6-77896534',
        '{date.today()}'
    )
    """)  

    DBcursor.execute(f"""
    INSERT INTO Members
    VALUES(
        '{generateUserID()}',
        'Piet',
        'Potvis',
        'Zwemstraat 29, Vislandserdorp',
        'slappehap@vismail.org',
        '31-6-23334953',
        '{date.today()}'
    )
    """)    

    databaseConnection.commit()

    databaseConnection.close()


## testenv
# wipeDatabase()
createDummyData()