from Functions.DatabaseFunctions import deleteEntry


def deleteMemberMenu(user):
    '''
    the interactive menu for SysAdmin.deleteMember()
    '''

    print("[DEV] deleteMemberMenu()")
    membershipID = input("Enter the membership ID of the member which you want to delete (use the search function (4) to find the membership ID) or type 'q' to cancel: ")
    
    if membershipID.lower() == 'q':
        return

    user.deleteMember(membershipID)
    input("Press 'enter' to continue ... ")
    