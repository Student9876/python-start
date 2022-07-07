#Matching the content of two files whether their content is same or not
def match(name1, name2):
    with open(f"{name1}.txt") as f:
        content1 = f.read()
    with open(f"{name2}.txt") as f:
        content2 = f.read()
    
    if content1 == content2:
        print("This two files are identical")
    else:
        print("This two files are not identical")


a = input("Enter name of the first file(txt): ")
b = input("Enter name of the second file(txt): ")
match(a,b)
    