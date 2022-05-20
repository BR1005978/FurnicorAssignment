import sqlite3
import Menus.HomeScreen as hs


def Main():
    databaseConnection = sqlite3.connect('FurnicoreDatabase.db')
    hs.homeScreen()




### run the program
Main()
    

