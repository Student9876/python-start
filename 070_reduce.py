'''
Reduce applies a rolling computation
to sequential pair of elements
'''

from functools import reduce

sum = lambda a,b: a+b
l = [1, 2, 3, 4, 5]
value = reduce(sum, l)
print(value)
