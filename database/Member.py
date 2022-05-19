class MemberClass:
    '''
    this member class has no functionality in this program and does not instantiate objects (as of 19-5-2022)
    but only servers to provide a blueprint for information to add to the database


    ● First Name and Last Name

    ● Address (Street name, House number, Zip Code (DDDDXX), City (system should generate a list of 10 city names of your choice predefined in the system)

    ● Email Address

    ● Mobile Phone (+31-6-DDDDDDDD)  only DDDDDDDD to be entered by the user.

    The system then needs to automatically add the registration date and assign a unique membership ID to every new member. The membership ID is a string of 10 random digits, not allowed to start with a Zero. The last digit on the right is a checksum digit, which must be equal to the remainder of the sum of the first 9 digits by 10.
    '''

    def __init__(self, _firstname, _lastname, _email):
        self.firstname = _firstname
        self.lastname = _lastname
        self.doekoe = _email