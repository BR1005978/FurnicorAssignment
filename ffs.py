import importlib
import sqlite3
from Functions.InitializeFunction import initializer
from Functions.Logfunction import LogData
import Menus.HomeScreens.HomeScreen as hs
import Userclasses
from Userclasses.SysAdminClass import SysAdmin


initializer()
LogData("no username", "starting up program")
def Main():




    hs.homeScreen()




## run the program
Main()


#testenv

