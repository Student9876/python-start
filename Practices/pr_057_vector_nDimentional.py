class Vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0

        for i in range(len(self.vec)):
            