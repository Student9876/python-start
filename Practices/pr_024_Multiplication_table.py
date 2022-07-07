# Using for loop
num = int(input('Enter the number you want to see Multiplication table: '))

for i in range(1, 11):
    multi = num*i 
    # print(str(num) + " X " + str(i) + "=" + str(multi))
    print(f"{num}X{i}={multi}") #This is called f string. And this is how we can use it


# Using while loop
num1 = int(input("Enter the number: "))
i = 1
while i<=10:
    print(f"{num1}X{i}={num1*i}")
    i = i + 1

# Reverse multiplication table using for loop
num2 = int(input("Enter the number you want to see Multiplication Table: "))
for i in reversed(range(1, 11)):
    print(f"{num2} X {i} = {num2*i}")