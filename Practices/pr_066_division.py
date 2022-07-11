def cal(num1, num2):
    try:
        c = num1/num2
        print(c)
    except ZeroDivisionError as e:
        print("Infinite")

a = int(input("Enter Numereator: "))
b = int(input("Enter Denominator: "))
cal(a, b)
