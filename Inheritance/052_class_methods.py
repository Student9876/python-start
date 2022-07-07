class Employee:
    company = "Camel"
    salary = 100
    loaction = "delhi"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal     #This will change the class attribute +_+

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal     #This will change the class attribute +_+



e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)    #it's an instance attribute
print(Employee.salary) #class attribute will not change
