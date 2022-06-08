from datetime import date
import sqlite3

from Functions.Auxfunctions import generateUserID
from Functions.DatabaseFunctions import insertIntoDatabase5args


class Advisor:

    '''
    Advisors (to be defined by a system administrator or a super administrator) – An advisor can manage members in the system (register new members, modify, search or retrieve their information.)
    this class serves as the base class for SysAdmin and SuperAdmin due to shared functionality.
    '''
    def __init__(self, _username):
        self.username = _username

    def __repr__(self):
        return f"{self.username} (Advisor)"

    def sayType(self):
        return "ADVISOR"


    def updateOwnPassword(self,newpass):
        '''
        Update own password
        note: this function is called by Menus.ClassFunctionsMenus.UpdateOwnPassword1
        '''
        databaseConnection = sqlite3.connect('FurnicorDatabase.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            UPDATE {self.sayType()}
            SET password = '{newpass}'
            WHERE username = '{self.username}'
            """)

        databaseConnection.commit()
        databaseConnection.close()

    def addNewMember(self, firstname, lastname, address, email, phonenumber):
        insertIntoDatabase5args(firstname, lastname, address, email, phonenumber)
        #TODOA1: make sure this function also logs this operation into the log file

    
    def modifyMember(self, column, variable, memID ):
        '''modify or update the information of a member in the system

        returns: void
        '''
        databaseConnection = sqlite3.connect('FurnicorDatabase.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            UPDATE Members
            SET {column} = '{variable}'
            WHERE membershipID = '{memID}'
            """)

        databaseConnection.commit()
        databaseConnection.close()

        return
    
    def queryMembers(self,column, variable):
        '''search and retrieve the information of a member. provide a column to specify on what information to look (firstname, lastname, phone number, home address, email address, user ID), then provide the variable'''
        databaseConnection = sqlite3.connect('FurnicorDatabase.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            
            SELECT *
            FROM Members
            WHERE {column} LIKE '%{variable}%' COLLATE NOCASE
            
            """)

        queryresult = DBcursor.fetchall()

        databaseConnection.commit()
        databaseConnection.close()

        return queryresult
    
