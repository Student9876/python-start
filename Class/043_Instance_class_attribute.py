class Employee:
    company = "Google"  
    salary = 100

zeon = Employee()  
zeus = Employee() 

#creating Instance attribute salary for both objects
# zeon.salary = 300
# zeus.salary = 300
zeon.salary = 45
print(zeon.salary)  
print(zeus.salary)

# Below line throws an error as address is not present in instance/class
# print(zeus.address)

