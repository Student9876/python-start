def Table(num):
    list = [num*i for i in range(1, 11)]
    print(list)
    with open('Tables.txt', 'a') as f:
        f.write(str(list))
        f.write("\n")


n = int(input("Enter the number of which you want to see Multiplication table: "))
Table(n)