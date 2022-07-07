class Person:
    country = "India"

    def __init__(self):
        print('Initializing Person....')

    def takeBreath(self):
        print("I'm breathing....")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print('Initializing Employee....')

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
         print("I'm an employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print('Initializing Programmer....')
    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()    #***
        print("I'm an Programmer so I am luckily breathing+_+.")

# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()  
# pr.takeBreath()   #for super() function it will first print it's superclass then its own




