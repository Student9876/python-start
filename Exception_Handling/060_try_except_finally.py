try:
    i  = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()   #in case of finally the code will not exit here
finally:
    print("We are done")  #it will always execute regardless of error

print("Thanks for using the program")  #it will not execute if we throw an error because we wrote exit()