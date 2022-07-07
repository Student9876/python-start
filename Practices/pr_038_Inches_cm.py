#Convert Inches to CM

def convert(n):
    cm = n*2.54
    return cm
n = int(input("Enter Inch value to convert it to Centimeter:"))
print("Centimeter value is: ", convert(n))
