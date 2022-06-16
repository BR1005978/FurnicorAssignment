from Functions.Auxfunctions import hashEncrypt
from Functions.DatabaseFunctions import insertIntoDatabaseUSER,insertIntoDatabaseMEMBER

def createDummyData():
    '''
    This function fills the database with dummy data. 
    insert random members, advisors and sysadmins etc into all 3 tables
    '''
    
    ### insert advisors into database   insertIntoDatabaseUSER('Advisors', 'dummyAdvisor', 'advisorpassword', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('Advisors', 'advisorAccount1', 'secretpassword', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('Advisors', 'lameAdvisor', 'advisorpassword2', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('Advisors', 'Richard123', 'crazychicken', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('Advisors', 'Jacket5', 'HotlineFlorida', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('Advisors', 'beeboo', 'bungbung', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('Advisors', 'stonkerino.supremo', 'snickers', 'samplename', 'samplelastname')

    ### insert SysAdmins into table
    insertIntoDatabaseUSER('SysAdmins', 'chillerino', 'youllneverguessthis', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('SysAdmins', 'sysadmin123','sysadminpassword', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('SysAdmins', 'getrekt555','some_damn_secret_password', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('SysAdmins', 'chillywilly','snorkadork9325', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('SysAdmins', 'woolybully','lecoqsportif', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('SysAdmins', 'derperinosupremo','passworderinosupremo', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('SysAdmins', 'BIMPF','knollzors', 'samplename', 'samplelastname')
    insertIntoDatabaseUSER('SysAdmins', 'sluggy.Maximo', 'cheesesticks', 'samplename', 'samplelastname')

    ### insert members into database
    # allowed city names: 
    insertIntoDatabaseMEMBER('Knoert', 'Klokiebril', 'Stronkstraat 85, 3012TX Botervuik', 'k.klokerino@bonkmail.com', '58785232')
    insertIntoDatabaseMEMBER('Sjaak', 'Sjouwer', 'Pronkstraat 88,  1805BB Drollendam', 'boterhammetje85@live.nl', '55447895')
    insertIntoDatabaseMEMBER('Jos', 'Brulvink', 'Pokémonstraat 103, 1566WE Heerenvoorn', 'brullerino@gmail.com', '12969545')
    insertIntoDatabaseMEMBER('Terry', 'Tarrelbraft', 'Snaakstraat 5, 1755PA Hoogkerk', 'tarreltjeknarreltje@outlook.com', '17879325')
    insertIntoDatabaseMEMBER('Berend', 'Baardhuis', 'Plopstraat 953, 1988TT Muizendam', 'plopperdeplopperdeplop@plopmail.plop', '11223344')
    insertIntoDatabaseMEMBER('Snoek', 'van der Snor', 'Zwemstraat 23, 2812BP Vislandserdorp', 'snorrrrr@snormail.org', '77896534')
    insertIntoDatabaseMEMBER('Piet', 'Potvis', 'Zwemstraat 29, 2813TT Vislandserdorp', 'slappehap@vismail.org', '23334953')

