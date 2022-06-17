import datetime
import os
import csv

from Functions.InitializeFunction import initializeLogfile
from Functions.caesar import decrypt, encrypt


def LogData(username = 'no username entered', description = 'no description given', addinfo = '.', sus ='no'):
    '''
    the function that logs a happening in the log file
    
    TODO: implement log functionality

    import os



    columns: No.,Username,Date,Time,Description of Activity, Additional information, Suspicious
    '''
    initializeLogfile()
    amountOfLines = len(open('logfile.txt', 'r', encoding="utf-8").readlines())



    # append to logfile
    with open('logfile.txt', 'a', encoding="utf-8") as appendfile:
        # file.write('nr', {username}, {date}, {time}, {description}, {addinfo}, {sus})


        currentime = datetime.datetime.now()
        time = currentime.strftime('%H:%M:%S')
        appendfile.write(encrypt(f"""{username}, {datetime.date.today()}, {time}, {description}, {addinfo}, {sus}
        """))

def logSuspicious(username = 'no username entered', description = 'no description given', addinfo = '.', sus ='No'):
    LogData(username, description,addinfo, "Yes")
    amountOfLines = len(open('susfile.txt', encoding="utf-8").readlines())



    # append to susfile
    with open('susfile.txt', 'a+', encoding="utf-8") as appendfile:


        currentime = datetime.datetime.now()
        time = currentime.strftime('%H:%M:%S')
        appendfile.write(encrypt(f"""{amountOfLines}, {username}, {datetime.date.today()}, {time}, {description}, {addinfo}, {sus}
        """+"""
        """  ))

def showSus():
    amountOfLines = len(open('susfile.txt', 'r', encoding="utf-8").readlines())

    if amountOfLines > 1:
        print("Admin, there is suspicious activity that requires your attention: ")
        answer = input("Would you like to see suspicious activity? Y/N ")
        if answer.lower() == "y":
            with open('susfile.txt', 'r', encoding="utf-8") as readfile: 
                lines = readfile.readlines()
                for line in lines:
                    print(decrypt(line))
                print("These are the alerts.")
                ans = input("Clear logs? Y / N")
                if ans.lower() == "y":
                    file = open('susfile.txt', 'w', encoding="utf-8")
                    file.write(encrypt("Nr,Username,Date,Time,Description of Activity,Additional information,Suspicious"))
                elif ans.lower() == "n":
                    input("Ok. Not removing logs.")
                else:
                    input("Input not recognized. Aborting. You can view suspicious activity in the admin menu.")
        else:
            input("Input not recognized. Aborting. You can view suspicious activity in the admin menu.")

def showLogs():
    with open("logfile.txt" , 'r', encoding="utf-8") as file: 
        lines = file.readlines()
        for line in lines:
            print(decrypt(line))