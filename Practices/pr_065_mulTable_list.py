#Using list comprehension
def Table(num):
    list = [num*i for i in range(1, 11)]
    print(list)


n = int(input("Enter the number of which you want to see Multiplication table: "))
Table(n)



