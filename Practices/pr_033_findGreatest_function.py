#Find greatest among 3 numbers

def greatest(num1, num2, num3):
    if num1 > num2:
        f1 = num1
    else:
        f1 = num2
    if f1>num3:
        print("Greatest among 3 is: ", f1)
    else:
        print("Greatest among 3 is: ", num3)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
greatest(a,b,c)