from datetime import date
import sqlite3

from Functions.Auxfunctions import generateUserID;

class Advisor:

    '''
    Advisors (to be defined by a system administrator or a super administrator) – An advisor can manage members in the system (register new members, modify, search or retrieve their information.)
    this class serves as the base class for SysAdmin and SuperAdmin due to shared functionality.
    '''
    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password

    def __repr__(self):
        return f"{self.username} (Advisor)"
    


    def updateOwnPassword(_password):
        '''Update own password'''
        password = _password

    def addNewMember(firstname, lastname, address, email, phonenumber):
        '''add a new member to the system'''


        databaseConnection = sqlite3.connect('FurnicorDatabase.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            INSERT INTO Members
            VALUES(
                '{generateUserID()}',
                '{firstname}',
                '{lastname}',
                '{address},
                '{email}',
                '31-6-{phonenumber},
                '{date.today()}'
            )
            """)

        databaseConnection.commit()
        databaseConnection.close()

        return
    
    def modifyMember():
        '''modify or update the information of a member in the system'''


        return
    
    def queryMember(column, variable):
        '''search and retrieve the information of a member. provide a column to specify on what information to look (firstname, lastname, phone number, home address, email address, user ID), then provide the variable'''
        databaseConnection = sqlite3.connect('member.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            
            SELECT *
            FROM Members
            WHERE {column} = '{variable}'
            
            """)

        queryresult = DBcursor.fetchone()

        databaseConnection.commit()
        databaseConnection.close()

        return queryresult


