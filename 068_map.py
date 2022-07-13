'''
map applies a function to all 
the items in an input list
 '''
def square(num):
    return num*num


l = [1,2,4]

# method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# method 2
# print(map(square , l)) #result shown as an object

print(list(map(square , l))) #Typecasted into list

