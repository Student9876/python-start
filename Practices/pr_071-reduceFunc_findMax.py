from functools import reduce


l = [1, 3, 5, 56, 78, 34, 45]

max1 = reduce(max, l)
print(max1)
