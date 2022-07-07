
def copy(name):
    with open(f'{name}.txt') as f:
        content = f.read()
    with open(f'{name}_copy.txt', 'w') as f:
        f.write(content)


a = input("Enter the name of the file(txt) you want to copy: ")
copy(a)