class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):  #It initializes an object
        print("Employee is created!") #this function runs automatically. Don't need to call
        self.name = name
        self.salary = salary
        self.subunit = subunit 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
        print(type(self.salary))  # we can send integer as arguments
        


    def getSalary(self, signature):
        print(f"Salary for this employee workinf in {self.company} is {self.salary}\n{signature}")

    @staticmethod   #decorator to mask greet as a static method
    def greet():   #After this @ noo need to put self, Where arguments aren't needed
        print("Good Morning, Sir")
    @staticmethod
    def time():
        from datetime import datetime      #for showing date and time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

harry = Employee("ZEON", 100, "Youtube")  #once class has been set, we need to send all the arguments. or it will throw

harry.getDetails()