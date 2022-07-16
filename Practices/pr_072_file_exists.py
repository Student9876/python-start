import os.path


filename = input("Enter the filename with extension you want to fnd: ")
if os.path.exists(filename):
    print("Exixts")
else:
    print("Do not exists")