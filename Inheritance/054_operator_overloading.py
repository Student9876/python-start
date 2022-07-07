'''
operators can be overloaded in python using dunder method
any function containing __  __ is called dunder


add overload   ----> p1__add__
sub overload   ----> p1__sub__
mul overload   ----> p1__mul__
div overload   ----> p1__div__


'''
class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):   #custom method. 
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):   #custom method. 
        print("Lets add")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum) 
print(mul)