from Functions.Logfunction import showLogs, showSus


def showLogsMenu(user):
    ''' 
    the interactive menu for SysAdmin.showLogs
    '''
    while True:
        answer = input("""Show normal logs or show alerts (suspicious) logs?: 
    1. Normal logs
    2. Suspicious logs
    0. Go back
    """)


        if answer == "1":
            showLogs()
        elif answer == "2":
            showSus()
        elif answer == "0":
            return
        else:
            input("Input not recognized... ")