def wipe(name):
    with open(f"{name}.txt", 'w') as f:
        f.write("")

a = input("Enter the file name you want to wipe its content:")
wipe(a)