num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
num4 = int(input("Enter number 4:"))

if(num1>num4):  #Kinda playing semi-finals among num1 and num4 and selecting a winner
    f1 = num1   #semi-finalist
else:
    f1 = num4

if(num2>num3): 
    f2 = num2
else:
    f2 = num3 #semi-finalist

if (f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")


