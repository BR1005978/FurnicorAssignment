from Functions.backup import createBackup, restoreBackup


def backupSystemMenu(user):
    '''
    the interactive menu for SysAdmin.backupSystem
    '''
    while True:
        answer = input("""
    1. Create backup
    2. Restore backup
    0. Go back
        """)
        if answer == "1":
            user.backupSystem()
            input("Backup created. Press enter to continue ...")
            break
        if answer == "2":
            user.restoreSystem()
            input("Backup restored. Press enter to continue ...")
            break
        if answer == "0":
            break
        
        
