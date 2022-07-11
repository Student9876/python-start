#We are going to use this function in another file
def greet(name):
    print(f"Good morning , {name}")

    # print(__name__)
    
if __name__ == "__main__":  #This will prevent the below syntax to perform in another file
    n = input("Enter your name\n")
    greet(n)