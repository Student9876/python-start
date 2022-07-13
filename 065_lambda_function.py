'''
lambda function can be used as a normal function
'''
# def func(a):
#     return a + 5

func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 566
print(func(x))
print(square(25))    #prints 625
print(sum(3, 5, 8)) #prints 16