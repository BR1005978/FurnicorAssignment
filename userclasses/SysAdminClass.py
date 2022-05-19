from userclasses.AdvisorClass import Advisor


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

    def queryUsers():
        '''check the list of users and their roles'''
        return

    def newAdvisor():
        '''define and add new advisor to the system'''
        return

    def modifyAdvisor():
        '''modify or update an existing advisor's account and profile'''
        return
    
    def deleteAdvisor():
        '''delete anexisting advisor's account'''
        return
    
    def resetAdvisorPassword():
        '''reset an advisor's password'''
        return
    
    def backupSystem():
        '''make a backup of the system'''
        return

    def showLogs():
        '''show the logs file of the system'''
        return

    def deleteMember():
        '''delete a member's record from the database'''
        return


