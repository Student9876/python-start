#Finding sum of n natural numbers using while loop

n = int(input("Enter the number of terms you want to add:"))

i = 1
sum = 0
while i<=n:
    sum = sum + i
    i = i + 1
print(sum)