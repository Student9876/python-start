'''
Class method allow you to change class attributes
@classmethod --> Class method decorator'''

class Employee:
    company = "Camel"
    salary = 100
    loaction = "delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal     #This will change the class attribute +_+

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal     #This will also change the class attribute +_+
        #this will let you access class. cls, classmethod



e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)    #it's an instance attribute
print(Employee.salary) #class attribute will not change
