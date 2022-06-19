from Functions.DatabaseFunctions import deleteEntry, queryDatabase3args
from Functions.Logfunction import LogData
from Functions.caesar import decrypt


def deleteMemberMenu(user):
    '''
    the interactive menu for SysAdmin.deleteMember()
    '''

    searchResults= queryDatabase3args('Members', 'firstname', '')
    for item in searchResults:
            print(f"""
Membership ID: {decrypt(item[0])}
First name: {decrypt(item[1])} 
Last name: {decrypt(item[2])}
Address: {decrypt(item[3])}
E-mail: {decrypt(item[4])}
Phone number: {decrypt(item[5])}
Registration date: {decrypt(item[6])}
            """)
    membershipID = input("Enter the membership ID of the member which you want to delete (use the search function (4) to find the membership ID) or type 'q' to cancel: ")
    
    if membershipID.lower() == 'q':
        return

    user.deleteMember(membershipID)
    LogData(user.username, "attempted removal of member", membershipID)
    input("Press 'enter' to continue ... ")
    