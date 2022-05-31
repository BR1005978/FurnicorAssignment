
def displayInfo():
    '''
    display information about this program.
    in this case, it reads the text in Menus/Infofiles/inf.txt
    '''
    extractedInfo = open("Menus/Infofiles/inf.txt")

    print(extractedInfo.read())

    cont = input("\nPress 'enter' to continue ... \n")