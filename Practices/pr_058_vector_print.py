class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    
    def __add__(self, vec2):
        return f"{self.vec[0] + vec2.vec[0]}i + {self.vec[1] + vec2.vec[1]}j + {self.vec[2] + vec2.vec[2]}k"

    
    def __mul__(self, vec2):
        return self.vec[0]*vec2.vec[0] + self.vec[1]*vec2.vec[1] + self.vec[2]*vec2.vec[2]

    
    def vecMul(self, vec2):
        return Vector([(self.vec[1]*vec2.vec[2] - self.vec[2]*vec2.vec[1]), (self.vec[2]*vec2.vec[0] - self.vec[0]*vec2.vec[2]), (self.vec[0]*vec2.vec[1] - self.vec[1]*vec2.vec[0])])



while True:
    i = int(input("1. Vector Addition 2. Vector Dot product 3. Vector Cross Product 4. Exit \n choose your option: "))
    
    if i == 1:
        a = int(input("Enter i of First Vector : "))
        b = int(input("Enter j of First Vector : "))
        c = int(input("Enter k of First Vector : "))

        e = int(input("Enter i of Second Vector : "))
        f = int(input("Enter j of Second Vector : "))
        g = int(input("Enter k of Second Vector : "))

        v1 = Vector([a, b, c])
        v2 = Vector([e, f, g])
        print( v1 + v2)
    elif i == 2:
        a = int(input("Enter i of First Vector : "))
        b = int(input("Enter j of First Vector : "))
        c = int(input("Enter k of First Vector : "))

        e = int(input("Enter i of Second Vector : "))
        f = int(input("Enter j of Second Vector : "))
        g = int(input("Enter k of Second Vector : "))

        v1 = Vector([a, b, c])
        v2 = Vector([e, f, g])

        print(v1 * v2)

    elif i == 3:
        a = int(input("Enter i of First Vector : "))
        b = int(input("Enter j of First Vector : "))
        c = int(input("Enter k of First Vector : "))

        e = int(input("Enter i of Second Vector : "))
        f = int(input("Enter j of Second Vector : "))
        g = int(input("Enter k of Second Vector : "))

        v1 = Vector([a, b, c])
        v2 = Vector([e, f, g])
        print(v1.vecMul(v2))
    elif i == 4:
        exit()






