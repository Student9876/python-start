a = 54  #Global variable
def func1():
    global a   #telling the function to use global variable
    print(a)  #printing the value of global variable
    a = 8     #Changing the value of global variable. Using global func
    print(a)

func1()
print(a)      #Printing the value of global variable which has been changed in the function 