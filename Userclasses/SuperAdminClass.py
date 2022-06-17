from Functions.DatabaseFunctions import deleteEntry, insertIntoDatabaseUSER, updateEntry
from Userclasses.SysAdminClass import SysAdmin


class SuperAdmin(SysAdmin):

    '''
    Super Administrator (Hardcoded) - A super admin has full control of the system.
    '''
    
    def __init__(self):
        self.username = "superadmin"

    def __repr__(self):
        return f"{self.username} (SuperAdmin)"

    ###########################################
    ### list of functions from superclasses ###

    # from Advisor
    #updateOwnPassword():
    #addMember():
    #modifyMember():
    #queryMember():

    # from SysAdmin
    #queryUsers():
    #addAdvisor():
    #modifyAdvisor():
    #deleteAdvisor():
    #resetAdvisorPassword():
    #backupSystem():
    #showLogs():
    #deleteMember():
    
    ###########################################
    
    def sayType(self):
        return "SUPER ADMIN"

    def updateOwnPassword(self, newpass):
        print("This function is not available for SUPER ADMIN.")
        input()

    def addAdmin(self, firstname, lastname, username, password):
        '''add a new admin to the system'''
        insertIntoDatabaseUSER('SysAdmins',username, password,firstname,lastname)

    def modifyAdmin(self, column, newValue):
        '''modify or update an existing admin's account and profile'''
        updateEntry('SysAdmins', column, newValue)
    
    def deleteAdmin(self, username):
        '''delete an existing admin's account'''
        deleteEntry('SysAdmins', 'username', username)
    
    def resetAdminPassword(self, sysadminUsername):
        '''reset an existing admin's password, give him a temporary one'''
        
        def generaterandomstring():
            print("placeholder function, will be Auxfunctions.generateRandomPassword() instead")
            return "randomstring"


        newPassword = generaterandomstring()

        updateEntry('SysAdmins', 'password', newPassword, 'username', sysadminUsername)

        return newPassword

        
