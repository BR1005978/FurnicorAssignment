from Functions.Auxfunctions import hashEncrypt
from Functions.DatabaseFunctions import insertIntoDatabase3arg,insertIntoDatabase5args

def createDummyData():
    '''
    This function fills the database with dummy data. 
    insert random members, advisors and sysadmins etc into all 3 tables
    '''
    
    ### insert advisors into database   insertIntoDatabase3arg('Advisors', 'dummyAdvisor', 'advisorpassword')
    insertIntoDatabase3arg('Advisors', 'advisorAccount1', 'secretpassword')
    insertIntoDatabase3arg('Advisors', 'lameAdvisor', 'advisorpassword2')
    insertIntoDatabase3arg('Advisors', 'Richard123', 'crazychicken')
    insertIntoDatabase3arg('Advisors', 'Jacket5', 'HotlineFlorida')
    insertIntoDatabase3arg('Advisors', 'beeboo', 'bungbung')
    insertIntoDatabase3arg('Advisors', 'stonkerino.supremo', 'snickers')

    ### insert SysAdmins into table
    insertIntoDatabase3arg('SysAdmins', 'chillerino', 'youllneverguessthis')
    insertIntoDatabase3arg('SysAdmins', 'sysadmin123','sysadminpassword')
    insertIntoDatabase3arg('SysAdmins', 'getrekt555','some_damn_secret_password')
    insertIntoDatabase3arg('SysAdmins', 'chillywilly','snorkadork9325')
    insertIntoDatabase3arg('SysAdmins', 'woolybully','lecoqsportif')
    insertIntoDatabase3arg('SysAdmins', 'derperinosupremo','passworderinosupremo')
    insertIntoDatabase3arg('SysAdmins', 'BIMPF','knollzors')
    insertIntoDatabase3arg('SysAdmins', 'sluggy.Maximo', 'cheesesticks')

    ### insert members into database
    # allowed city names: 
    insertIntoDatabase5args('Knoert', 'Klokiebril', 'Stronkstraat 85, 3012TX, Botervuik', 'k.klokerino@bonkmail.com', '58785232')
    insertIntoDatabase5args('Sjaak', 'Sjouwer', 'Pronkstraat 88,  1805BB, Drollendam', 'boterhammetje85@live.nl', '55447895')
    insertIntoDatabase5args('Jos', 'Brulvink', 'Pokémonstraat 103, 1566WE, Heerenvoorn', 'brullerino@gmail.com', '12969545')
    insertIntoDatabase5args('Terry', 'Tarrelbraft', 'Snaakstraat 5, 1755PA, Hoogkerk', 'tarreltjeknarreltje@outlook.com', '17879325')
    insertIntoDatabase5args('Berend', 'Baardhuis', 'Plopstraat 953, 1988TT, Muizendam', 'plopperdeplopperdeplop@plopmail.plop', '11223344')
    insertIntoDatabase5args('Snoek', 'van der Snor', 'Zwemstraat 23, 2812BP, Vislandserdorp', 'snorrrrr@snormail.org', '77896534')
    insertIntoDatabase5args('Piet', 'Potvis', 'Zwemstraat 29, 2813TT, Vislandserdorp', 'slappehap@vismail.org', '23334953')

