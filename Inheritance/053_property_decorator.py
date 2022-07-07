
class Employee:
    company = "Bharat Gas"
    salary = 5000
    salarybonus = 400
    # totalSalary = 5500

    @property          #getter method                 #in short, using this decorator I can call this not as a function, But as a property
    def totalSalary(self):
        return self.salary + self.salarybonus


    @totalSalary.setter     #setter method
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5400                #in decorator @totalSalary, it gonna set the salary bonus so that the salary matches the newly changed salary
print(e.salary)
print(e.salarybonus)