import sqlite3;

class Advisor:
    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password
    


    def updateOwnPassword(_password):
        '''Update own password'''
        password = _password

    def addNewMember(firstname, lastname):
        '''add a new member to the system'''


        databaseConnection = sqlite3.connect('member.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            INSERT INTO Members
            VALUES(
                '{firstname}',
                '{lastname}'
            )
            """)

        databaseConnection.commit()
        databaseConnection.close()

        return
    
    def modifyMember():
        '''modify or update the information of a member in the system'''


        return
    
    def queryMember(column, variable):
        '''search and retrieve the information of a member. provide a column to specify on what information to look (firstname, lastname, phone number, home address, email address, user ID), then provide the variable'''
        databaseConnection = sqlite3.connect('member.db')
        DBcursor = databaseConnection.cursor()

        DBcursor.execute(f"""
            
            SELECT *
            FROM Members
            WHERE {column} = '{variable}'
            
            """)

        queryresult = DBcursor.fetchone()

        databaseConnection.commit()
        databaseConnection.close()

        return queryresult



print(Advisor.queryMember("firstname", "Jan"))