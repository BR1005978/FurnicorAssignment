import sqlite3
from Functions.DatabaseFunctions import deleteEntry, insertIntoDatabase3arg, updateEntry
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
    #addNewMember():
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

    def newAdvisor(self, username, newpassword):
        '''define and add new advisor to the system'''
        insertIntoDatabase3arg('Advisors', username, newpassword)
        return

    def modifyAdvisor(column, variable, username):
        '''modify or update an existing advisor's account and profile'''

        databaseConnection = sqlite3.connect('FurnicorDatabase.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            UPDATE Advisors
            SET {column} = '{variable}'
            WHERE 'username' = '{username}'
            """)

        databaseConnection.commit()
        databaseConnection.close()
    
    def deleteAdvisor(username):
        '''delete an existing advisor's account'''

        deleteEntry('Advisors', 'username', username)
        return
    
    def resetAdvisorPassword(advisorUsername):
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
    
    def backupSystem():
        '''
        make a backup of the system
        
        input: nothing
        returns: nothing
        '''
        #TODOPS2: schrijf een functie die het bestandje FurnicorDatabase.db en logfile.txt
        #verplaatsen naar een mapje genaamd 'backup'




        return

    def showLogs():
        '''show the logs file of the system'''
        return

    def deleteMember(self, memID):
        '''delete a member's record from the database'''

        deleteEntry('Members', 'membershipID', memID)
        return


