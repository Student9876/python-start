'''
The enumerate function adds counter to an iterable
and returns it
'''

list1 = [3, 53,2,False, 6.2, "ZEON"]
# index = 0
# for item in list1:
#     print(item, index)
#     index += 1

for index, item in enumerate(list1):
    print(index , item)