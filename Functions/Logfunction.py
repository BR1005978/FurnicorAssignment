import datetime
import os
import csv

from Functions.InitializeFunction import initializeLogfile


def LogData(username = 'no username entered', description = 'no description given', addinfo = '.', sus ='sus?'):
    '''
    the function that logs a happening in the log file
    
    TODO: implement log functionality

    import os

    if not os.path.exists(path):
        with open(path, 'w'): 

    columns: No.,Username,Date,Time,Description of Activity, Additional information, Suspicious
    '''
    initializeLogfile()
    amountOfLines = len(open('logfile.txt').readlines())



    # append to logfile
    with open('logfile.txt', 'a+') as appendfile:
        # file.write('nr', {username}, {date}, {time}, {description}, {addinfo}, {sus})


        currentime = datetime.datetime.now()
        time = currentime.strftime('%H:%M:%S')
        appendfile.write(f"{amountOfLines}, {username}, {datetime.date.today()}, {time}, {description}, {addinfo}, {sus}\n" )





LogData()