class Person:
    country = "India"

    def takeBreath(self):
        print("I'm breathing....")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
         print("I'm an employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
         print("I'm an Programmer so I am luckily breathing+_+.")

p = Person()
e = Employee()
pr = Programmer()
e.takeBreath()
p.takeBreath()
pr.takeBreath()  #it will use the function from the  latest one, if it not has it's own function
# print(p.company)  #Throws an error
print(e.company)  
print(pr.company)  
print(pr.country)  



