class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fibre"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upgradeLevel()

print(p.level)
print(p.company)  #it prints the attribute of the first class written in the derived class. It will have first priority