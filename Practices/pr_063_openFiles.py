def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")
        
readFile("Practices/log_files1.txt")
readFile("Practices/log_files2.txt")
readFile("Practices/log_files3.txt")
    