#A word to be censored 

def update(name, word):
    with open(f"{name}.txt") as f:
        content = f.read()
        content = content.replace(f"{word}", "####$$$$")

    with open(f"{name}.txt", 'w') as f:
        content = f.write(content)

a = input("Enter file(txt) name you want to edit: ")
b = input("Enter the word you want to censor: ")
update(a,b)