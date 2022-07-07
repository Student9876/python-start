#Taking 6 marks of student and sorting them
m1 = int(input("Enter Marks of student 1: "))
m2 = int(input("Enter Marks of student 2: "))
m3 = int(input("Enter Marks of student 3: "))
m4 = int(input("Enter Marks of student 4: "))
m5 = int(input("Enter Marks of student 5: "))
m6 = int(input("Enter Marks of student 6: "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

#insert items in list
list = []
n = int(input("Enter number of items:"))
for i in range(n):
    list.insert(i,input("Enter the word you want to censor: "))
print(list)

