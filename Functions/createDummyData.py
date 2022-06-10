from Functions.Auxfunctions import hashEncrypt
from Functions.DatabaseFunctions import insertIntoDatabase3arg,insertIntoDatabase5args

def createDummyData():
    '''
    This function fills the database with dummy data. 
    insert random members, advisors and sysadmins etc into all 3 tables
    '''
    
    ### insert advisors into database   insertIntoDatabase3arg('Advisors', 'dummyAdvisor', hashEncrypt('advisorpassword'))
    insertIntoDatabase3arg('Advisors', 'advisorAccount1', hashEncrypt('secretpassword'))
    insertIntoDatabase3arg('Advisors', 'lameAdvisor', hashEncrypt('advisorpassword2'))
    insertIntoDatabase3arg('Advisors', 'Richard123', hashEncrypt('crazychicken'))
    insertIntoDatabase3arg('Advisors', 'Jacket5', hashEncrypt('HotlineFlorida'))
    insertIntoDatabase3arg('Advisors', 'beeboo', hashEncrypt('bungbung'))
    insertIntoDatabase3arg('Advisors', 'stonkerino.supremo', hashEncrypt('snickers'))

    ### insert SysAdmins into table
    insertIntoDatabase3arg('SysAdmins', 'chillerino', hashEncrypt('youllneverguessthis'))
    insertIntoDatabase3arg('SysAdmins', 'sysadmin123',hashEncrypt('sysadminpassword'))
    insertIntoDatabase3arg('SysAdmins', 'getrekt555',hashEncrypt('some_damn_secret_password'))
    insertIntoDatabase3arg('SysAdmins', 'chillywilly',hashEncrypt('snorkadork9325'))
    insertIntoDatabase3arg('SysAdmins', 'woolybully',hashEncrypt('lecoqsportif'))
    insertIntoDatabase3arg('SysAdmins', 'derperinosupremo',hashEncrypt('passworderinosupremo'))
    insertIntoDatabase3arg('SysAdmins', 'BIMPF',hashEncrypt('knollzors'))
    insertIntoDatabase3arg('SysAdmins', 'sluggy.Maximo', hashEncrypt('cheesesticks'))

    ### insert members into database
    insertIntoDatabase5args('Knoert', 'Klokiebril', 'Stronkstraat 85, Otterdam', 'k.klokerino@bonkmail.com', '31-6-58785232')
    insertIntoDatabase5args('Sjaak', 'Sjouwer', 'Pronkstraat 88, Drollendam', 'boterhammetje85@live.nl', '31-6-55447895')
    insertIntoDatabase5args('Jos', 'Brulvink', 'Pokémonstraat 103, Heerenvoorn', 'brullerino@gmail.com', '31-6-12969545')
    insertIntoDatabase5args('Terry', 'Tarrelbraft', 'Snaakstraat 5, Hoogkerk', 'tarreltjeknarreltje@outlook.com', '31-6-17879325')
    insertIntoDatabase5args('Berend', 'Baardhuis', 'Plopstraat 953, Plopsaland', 'plopperdeplopperdeplop@plopmail.plop', '31-6-11223344')
    insertIntoDatabase5args('Snoek', 'van der Snor', 'Zwemstraat 23, Vislandserdorp', 'snorrrrr@snormail.org', '31-6-77896534')
    insertIntoDatabase5args('Piet', 'Potvis', 'Zwemstraat 29, Vislandserdorp', 'slappehap@vismail.org', '31-6-23334953')

