from Userclasses.SysAdminClass import SysAdmin


class SuperAdmin(SysAdmin):

    '''
    Super Administrator (Hardcoded) - A super admin has full control of the system.
    '''
    
    def __init__(self):
        self.username = "superadmin"
        self.password = "Admin321!"

    def __repr__(self):
        return f"{self.username} (SuperAdmin)"

    ###########################################
    ### list of functions from superclasses ###

    # from Advisor
    #updateOwnPassword():
    #addNewMember():
    #modifyMember():
    #queryMember():

    # from SysAdmin
    #queryUsers():
    #newAdvisor():
    #modifyAdvisor():
    #deleteAdvisor():
    #resetAdvisorPassword():
    #backupSystem():
    #showLogs():
    #deleteMember():
    
    ###########################################
    
    def sayType(self):
        return "SUPER ADMIN"


    def addAdmin():
        '''add a new admin to the system'''
        return

    def modifyAdmin():
        '''modify or update an existing admin's account and profile'''
        return
    
    def deleteAdmin():
        '''delete an existing admin's account'''
        return
    
    def resetAdminPassword():
        '''reset an existing admin's password, give him a temporary one'''
        return
