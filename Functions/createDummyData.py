from DatabaseFunctions import *

def createDummyData():
    '''
    This function fills the database with dummy data. 
    insert random members, advisors and sysadmins etc into all 3 tables
    '''

    ### insert advisors into database   insertIntoDatabase3arg('Advisors', 'dummyAdvisor', hash('advisorpassword'))
    insertIntoDatabase3arg('Advisors', 'advisorAccount1', hash('secretpassword'))
    insertIntoDatabase3arg('Advisors', 'lameAdvisor', hash('advisorpassword2'))
    insertIntoDatabase3arg('Advisors', 'Richard123', hash('crazychicken'))
    insertIntoDatabase3arg('Advisors', 'Jacket5', hash('HotlineFlorida'))
    insertIntoDatabase3arg('Advisors', 'beeboo', hash('bungbung'))
    insertIntoDatabase3arg('Advisors', 'stonkerino.supremo', hash('snickers'))

    ### insert SysAdmins into table
    insertIntoDatabase3arg('SysAdmins', 'chillerino', hash('youllneverguessthis'))
    insertIntoDatabase3arg('SysAdmins', 'sysadmin123',hash('sysadminpassword'))
    insertIntoDatabase3arg('SysAdmins', 'getrekt555',hash('some_damn_secret_password'))
    insertIntoDatabase3arg('SysAdmins', 'chillywilly',hash('snorkadork9325'))
    insertIntoDatabase3arg('SysAdmins', 'woolybully',hash('lecoqsportif'))
    insertIntoDatabase3arg('SysAdmins', 'derperinosupremo',hash('passworderinosupremo'))
    insertIntoDatabase3arg('SysAdmins', 'BIMPF',hash('knollzors'))
    insertIntoDatabase3arg('SysAdmins', 'sluggy.Maximo', hash('cheesesticks'))

    ### insert members into database
    insertIntoDatabase5args('Knoert', 'Klokiebril', 'Stronkstraat 85, Otterdam', 'k.klokerino@bonkmail.com', '31-6-58785232')
    insertIntoDatabase5args('Sjaak', 'Sjouwer', 'Pronkstraat 88, Drollendam', 'boterhammetje85@live.nl', '31-6-55447895')
    insertIntoDatabase5args('Jos', 'Brulvink', 'Pokémonstraat 103, Heerenvoorn', 'brullerino@gmail.com', '31-6-12969545')
    insertIntoDatabase5args('Terry', 'Tarrelbraft', 'Snaakstraat 5, Hoogkerk', 'tarreltjeknarreltje@outlook.com', '31-6-17879325')
    insertIntoDatabase5args('Berend', 'Baardhuis', 'Plopstraat 953, Plopsaland', 'plopperdeplopperdeplop@plopmail.plop', '31-6-11223344')
    insertIntoDatabase5args('Snoek', 'van der Snor', 'Zwemstraat 23, Vislandserdorp', 'snorrrrr@snormail.org', '31-6-77896534')
    insertIntoDatabase5args('Piet', 'Potvis', 'Zwemstraat 29, Vislandserdorp', 'slappehap@vismail.org', '31-6-23334953')
