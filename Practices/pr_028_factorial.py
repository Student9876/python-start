n = int(input("Enter the number you want to calcualte factorial: "))

fact = 1
for i in range(1,n+1):
    fact=fact*i

print(f"The factorial of the number {n} is {fact}")
