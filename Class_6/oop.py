'''
    OOP in python 
    Author: Andres Ardila 
    Date: 07-oct-2020

'''

class Employee:

    ## self is like this
    ## self stores the object, for example self = emp1
    ## overload does not exitst in python but there is a way to handle this problem by setting default values to the parameter of the object



    #this is a class variable it can be access by any object
    counter = 0
    serialNumber = 1000

    def __init__(self, firstName ='null', lastName = 'null', age = 18):
        
        ### Attributes -- instance variables 
        self.fName = firstName
        self.lName = lastName
        self.age = age
        self.email = self.createAnEmail()
        Employee.counter = Employee.counter + 1
        Employee.serialNumber += 1
        self.employeeId = Employee.serialNumber
    ### ========== Getters and Setters

    def createAnEmail(self):
        return f'{self.fName}.{self.lName}@mycompany.ca'

    def setAge(self, age):
        if age > 0:
            self.age = age
        else:
            self.age = 18

    

emp1 = Employee('Andres','Ardila',31)

emp2 = Employee('Andres','Ardila',31)

print(emp1.employeeId)
print(emp2.employeeId)

