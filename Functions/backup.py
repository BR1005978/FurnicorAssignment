import os
import zipfile

list_files = ['FurnicorDatabase.db', 'logfile.txt']

def createBackup():
    with zipfile.ZipFile('backup.zip', 'w') as zipF:
        for file in list_files:
            zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)

def restoreBackup():
    with zipfile.ZipFile('backup.zip', 'r') as zipF:
        zipF.extractall()