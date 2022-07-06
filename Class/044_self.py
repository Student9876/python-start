class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 100K")

zeon = Employee()   
zeon.getSalary() #also works as below line
# Employee.getSalary(zeon)


class Employee1:
    company = "Google"
    name = ""
    def getSalary(self): #self receives object as an argument
        print(f"Salary for this employee working in {self.company} is {self.salary}")
        print(f"Name of Employee is {self.name}")

zeus = Employee1() 
zeus.salary = 100000
zeus.name = "Subhajit"
zeus.getSalary()

