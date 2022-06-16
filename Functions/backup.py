import os

def createBackup():
    os.system('copy FurnicorDatabase.db backup.db')
    os.system('copy logfile.txt backup.txt')

def restoreBackup():
    os.system('copy backup.db FurnicorDatabase.db')
    os.system('copy backup.txt logfile.txt')

