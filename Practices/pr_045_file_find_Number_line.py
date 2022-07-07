#Find the number of the line where 'python' is present
content = True #for entering while loop first time
i = 1
with open("log_sample.txt") as f:
    while content:
        content = f.readline() #it reads lines

        if 'python' in content:
            print(content)
            print(f"Yes, python is present on line number {i}")
        i+=1