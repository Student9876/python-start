# Uses of If-elif-else 
'''
1. There can be any number of elif statements
2. Last else is executed only if all the conditions
inside elif fails
'''

a = 8

# 1. If-elif-else ladder 
# if(a<3):
#     print("The value of a is greater than 3")
# elif(a>7):
#     print("The value of a is greater than 7")
# elif(a>13):
#     print("The value of a is greater than 13")
# elif(a>17):
#     print("The value of a is greater than 17")
# else:
#     print("The value of a is not greater then 3")


# 2. Multiple if statements. Those two where if and else is  together, that forms a if else ladder. Others are independent statements. Obviously they will execute if they are true
if(a<3):
    print("The value of a is greater than 3")
if(a>7):
    print("The value of a is greater than 7")
if(a>13):
    print("The value of a is greater than 13")
if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value of a is not greater then 3 or 7")
