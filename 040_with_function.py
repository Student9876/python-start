'''
The best way to opem and close the file automatically is the with statement
Dpn't need to write f.close()
'''
with open('another.txt', 'r') as f:
    a = f.read()
    print(a)
with open('another.txt', 'w') as f:
    a = f.write("me")
    print(a)
