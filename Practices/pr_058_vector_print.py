class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    
    def __add__(self, vec2):
        return f"{self.vec[0] + vec2.vec[0]}i + {self.vec[1] + vec2.vec[1]}j + {self.vec[2] + vec2.vec[2]}k"
    
    def __mul__(self, vec2):
        return f"{self.vec[0]*vec2.vec[0] + self.vec[1]*vec2.vec[1] + self.vec[2]*vec2.vec[2]}"

v1 = vector([1, 2, 3])
v2 = vector([4, 5, 7])

print(v1)
print(v2)
print(v1 + v2)
print(v1*v2)
