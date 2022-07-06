class Employee:
    company = "Google"  #anything directly related to class is called class attribute.
    salary = 100
zeon = Employee()  #Object initialization
zeus = Employee() 
print(zeon.company)
print(zeus.company)
zeon.salary = 300
zeus.salary = 300
#Changing Class attribute
Employee.company = "Youtube"
print(zeon.company)

print(zeon.salary)
print(zeus.salary)