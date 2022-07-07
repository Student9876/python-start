#Sum of natural numbers using recursion

def sum1(n):
    if n<=1:
        return n
    else:
        return n + sum1(n-1)
    
n = int(input("Enter number of natural numbers you want to add: "))
print("Sum is: ", sum1(n))