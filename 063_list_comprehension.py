a = [3, 6, 7, 8, 9, 2, 4, 23, 45, 67, 68, 44]
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)
# print(b)   #all even numbers printed 

#other method: Shortcut
b = [i for i in a if i%2 == 0]
print(b)

c = [item for item in a if item>8]
print(c)

#dictionary
t = [1, 4, 2, 4, 2, 1, 1, 3]
s = {i for i in t}
print(s)