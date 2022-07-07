class Calculator:
    @staticmethod
    def Greet():
        print("*************Hello there. Welcome to pythin made calculator*****************")

    def square(self, num):
        self.number = num
        print(f"Square of the given number {self.number} is: {self.number **2}")

    def cube(self, num):
        self.number = num
        print(f"Cube of the given number {self.number} is: {self.number **3}")

    def squareRoot(self, num):
        self.number = num
        import math
        sq = math.sqrt(self.number)
        print(f"SquareRoot of the given number {self.number} is: {sq}")


n = Calculator()
n.Greet()

b = int(input("Select the option:\n 1. Square 2. Cube 3. SquareRoot \n Your Choice: "))
a = int(input("Enter the number: "))


if b ==1:
    n.square(a)
elif b ==2:
    n.cube(a)
elif b ==3:
    n.squareRoot(a)