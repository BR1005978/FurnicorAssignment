from Functions.DatabaseFunctions import deleteEntry


def deleteMemberMenu(user):
    '''
    the interactive menu for SysAdmin.deleteMember()
    '''

    print("[DEV] deleteMemberMenu()")
    
    membershipID = input("Type the membershipID of the Member you wish to delete (use the search member function to find one) : ")
    user.deleteMember('Members', 'membershipID', membershipID)
    input("Press 'enter' to continue ... ")
    