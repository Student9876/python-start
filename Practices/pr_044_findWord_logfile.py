# Finding a word in a log file
with open("log_sample.txt") as f:
    content = f.read().lower() #scanned the content and lowered the characters
if 'python' in content:
    print("Yes, python is present")
else:
    print("No, python is not present")