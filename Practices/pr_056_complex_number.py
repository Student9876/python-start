class Complex:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
    def __add__(self, c):
        print("Lets Add")
        return Complex(self.Re  + c.Re, self.Im + c.Im )  #in return we send the calculated data into its own function

    def __str__(self):
        return f"{self.Re} + {self.Im}i"

    # def __mul__(self, c):             #We can also use this instead of using str
    #     return f"({self.Re*c.Re - self.Im*c.Im}) + ({self.Re*c.Im - c.Re*self.Im})i"
    
    def __mul__(self, c):
        return Complex(self.Re*c.Re - self.Im*c.Im , self.Re*c.Im - c.Re*self.Im)

    def __str__(self):
        return f"{self.Re} + {self.Im}i"
    

while True:
    n = int(input("1. Complex addition  2.Complex Multiplication 3. Exit \n Choose Option:"))
    if n == 1:
        r1 = int(input("Enter Real part of the First complex number:"))
        i1 = int(input("Enter Imaginary part of the Firstcomplex number:"))
        r2 = int(input("Enter Real part of the Second complex number:"))
        i2 = int(input("Enter Imaginary part of the Second complex number:"))
        c1 = Complex(r1, i1)
        c2 = Complex(r2, i2)
        print(c1 + c2)
    elif n == 2:
        r1 = int(input("Enter Real part of the First complex number:"))
        i1 = int(input("Enter Imaginary part of the Firstcomplex number:"))
        r2 = int(input("Enter Real part of the Second complex number:"))
        i2 = int(input("Enter Imaginary part of the Second complex number:"))
        c1 = Complex(r1, i1)
        c2 = Complex(r2, i2)
        print(c1*c2)
    elif n== 3:
        exit()
    else:
        print("Wrong choice")
    
