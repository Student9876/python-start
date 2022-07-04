'''
1. Recursion is a function which calls itself.
2. Recursion is used in some problems with formula repeating 
same type again and again.
3. A programmer should be careful while using recursion so that it doesn't 
calling itselt infinitely. (Base condition)
'''

#n!=1*2*3*4....*n
#n!=1*2*3*4....*(n-1)*n
#n!=n*(n-1)!

# n = 4
# product = 1
# for i in range(n):
#     product= product*(i+1)
# print(product)

def factorial_iter(n):  #we used loop here. It's not a recursion
    product = 1
    for i in range(n):  
        product= product*(i+1)
    return product

def factorial_recursive(n):
    if n==1 or n==0:  #Base condition
        return 1
    return n* factorial_recursive(n-1)

print(factorial_recursive(78))


