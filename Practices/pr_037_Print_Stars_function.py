''' 
print   ***
        **
        *       this pattern
'''

def pattern(n):
    for i in range(n):
        print("*" * (n-i))

n = int(input("Enter number of lines you want to print:"))
pattern(n)