#What is written in the function is called function definition
'''
There are some built in functions
Like- len(), sum(), print(), range()
'''

def percent(marks):  #A functiom with argument. Give a value to funtion to work with
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p
    #return that value where the function is called

def mySum(num1, num2):
    return num1 + num2

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)



marks2 = [75, 98, 86, 77]
percentage2 = percent(marks2)
print(percentage1 , percentage2)

s = mySum(20,39)
print(s)