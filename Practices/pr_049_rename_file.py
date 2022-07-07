#Renaming a a file
import os

def rename(name1, name2):
    with open(f"{name1}.txt") as f:
        content = f.read()

    with open(f"{name2}.txt" , 'w') as f:
        f.write(content)

    os.remove(f"{name1}.txt")

a = input("Enter the file name you want to rename: ")
b = input("Enter new name: ")

rename(a,b)
