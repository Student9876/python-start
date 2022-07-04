#Default parameter Value
#A value in the function

def greet(name = "Stranger"): #Here we put a default name in the function.
    print("Good day, "+ name) #So in case of no arguments, It will print the default value and not throw error

greet("ZEON")
greet()  #Shows error. To solve the error we put a default value in the function 