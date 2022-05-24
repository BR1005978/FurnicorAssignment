'''
Auxiliary functions such as generateUserID to be used in other places of the program
'''

import random 

def generateUserID():
    '''
    generate a user ID

    The membership ID is a string of 10 random digits, not allowed to start with a Zero. 
    The last digit on the right is a checksum digit, which must be equal to the remainder of the sum of the first 9 digits by 10.

    Few examples are given below:

    § Invalid ID number: 0223287420 [a Zero at index 0 is not allowed]

    § Invalid ID number: 5223287424 [The checksum is not correct]
    > (5+2+2+3+2+8+7+4+2) = 35 35 mod 10 = 5 ¹ 4

    § Valid ID number: 5223287425
    '''

    ID = random.randint(100000000,999999999)

    IDstring = str(ID)

    IDsum = 0

    for digit in IDstring:
        IDsum += int(digit)
    
    IDsumstring = IDstring + str(IDsum % 10)

    finalID = int(IDsumstring)


    
    # this generates a valid user ID
    return finalID


print(generateUserID())