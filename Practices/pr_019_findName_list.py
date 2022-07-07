#Whether a name is present in a list 

names = ["subhajit", "shubham", "abhijeet", "diganta", "saikat"]

name = input("Enter name to check:\n")

if name in names:
    print("Your name is present in the list")
else:
        print("Your name is not present in the list")