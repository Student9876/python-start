class Sample:
    a = "ZEON"

obj = Sample()
obj.a = "Subha"

#Class attribute don't change by changing instance attribute
#To change class attribute
Sample.a = "Subha"

print(Sample.a) 
print(obj.a)

