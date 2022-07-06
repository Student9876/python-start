class Employee:
    company = "Google"

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


zeon = Employee()   
zeon.greet()
zeon.time()
zeon.salary = 100000
zeon.getSalary("Thanks!")


