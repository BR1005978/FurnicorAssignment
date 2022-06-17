import sqlite3
from Functions.DatabaseFunctions import deleteEntry, insertIntoDatabaseUSER, updateEntry
from Functions.Logfunction import LogData, showLogs
from Functions.backup import createBackup, restoreBackup
from Userclasses.AdvisorClass import Advisor


class SysAdmin(Advisor):

    '''
    System Administrators (to be defined by the Super Administrator only) 
    An admin who can manage advisors (register new advisor, modify or delete
    an advisor, etc.)

    > this class inherits from the Advisor class due to shared functionality
    '''

    ###########################################
    ### functions inherited from advisor    ###
    #updateOwnPassword():
    #addMember():
    #modifyMember():
    #queryMember():
    ###########################################

    def __repr__(self):
        return f"{self.username} (SysAdmin)" 

    def sayType(self):
        return "SYSADMIN"


    def queryUsers():
        '''check the list of users and their roles'''
        return

    def addAdvisor(self, username, newpassword, firstname, lastname):
        '''define and add new advisor to the system'''
        insertIntoDatabaseUSER('Advisors', username, newpassword, firstname, lastname)
        return

    def modifyAdvisor(column, variable, username):
        '''modify or update an existing advisor's account and profile'''

        databaseConnection = sqlite3.connect('FurnicorDatabase.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            UPDATE Advisors
            SET {column} = :var
            WHERE 'username' = :user
            """, {'var': variable ,'user':username})

        databaseConnection.commit()
        databaseConnection.close()
    
    def deleteAdvisor(self, username):
        '''delete an existing advisor's account'''

        deleteEntry('Advisors', 'username', username)
        return
    
    def resetAdvisorPassword(self, advisorUsername):
        '''
        reset an advisor's password.
        generates a random password and updates the advisor based on the inputted username in 
        the database accordingly. 

        input: the username of the advisor
        returns: the new (randomized) password
        '''

        def generaterandomstring():
            print("placeholder function, will be Auxfunctions.generateRandomPassword() instead")
            return "randomstring"


        newPassword = generaterandomstring()

        updateEntry('SysAdmins', 'password', newPassword, 'username', advisorUsername)

        return newPassword
    
    def backupSystem(self):
        '''
        make a backup of the system
        
        input: nothing
        returns: nothing
        '''

        createBackup()
        #TODOPS2: schrijf een functie die het bestandje FurnicorDatabase.db en logfile.txt
        #verplaatsen naar een mapje genaamd 'backup'

    def restoreSystem(self):
        restoreBackup()

    def showLogsAdmin():
        
        return

    def deleteMember(self, memID):
        '''delete a member's record from the database'''

        deleteEntry('Members', 'membershipID', memID)
        
        return