'''
    OOP in python 
    Author: Andres Ardila 
    Date: 07-oct-2020

'''

class Employee:

    ## self is like this
    ## self stores the object, for example self = emp1
    ## overload does not exitst in python but there is a way to handle this problem by setting default values to the parameter of the object

    def __init__(self, firstName ='null', lastName = 'null', age = 18):
        
        ### Attributes -- instance variables 
        self.fName = firstName
        self.lName = lastName
        self.age = age


    pass

emp1 = Employee('Andres','Ardila',31)
print(emp1.lName)

##  this is a new change that we are going to commit