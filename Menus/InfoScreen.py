
def displayInfo():
    extractedInfo = open("Menus/Infofiles/inf.txt")

    # with open ("inf.txt", "r") as readableFile:
    #     extractedInfo = readableFile.read().splitlines()

    print(extractedInfo.read())

    cont = input("\nPress 'enter' to continue ... \n")