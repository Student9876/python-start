# Inheritance is a way to create a class using an existing class

'''
Syntax:
class Employee:             #Base class
    #code

class Programmer(Employee):
    #code                   #Derived or child class



'''

class Employee:                    #base class
    company = "Google"
    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):            # derived class
    language = "Pyhton"
    company = "Youtube"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("this is a programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(e.company) 
print(p.company)
p.getLanguage()
