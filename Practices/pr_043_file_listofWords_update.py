#A word to be censored 

def update(name, words):
    with open(f"{name}.txt") as f:
        content = f.read()
    for word in words:
        content = content.replace(word, "$$%##$%%")
        with open(f"{name}.txt", 'w') as f:
            f.write(content)



list = []
a = input("Enter file(txt) name you want to edit: ")
n = int(input("Enter number of words you want to replace:"))
for i in range(n):
    list.insert(i,input("Enter the word you want to censor: "))

update(a,list)
