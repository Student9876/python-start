l1 = [1, 8, 7, 2, 21, 56, 11]
print(l1)

l1.reverse()
print(l1) #reverses the list

# l1_sorted = l1.sort()
'''2 ways a function may work. Either it can return something
or it can change the actual data'''

l1.sort() #Sorts in increasing order
print(l1)

l1.append(69) #adds something end of the list
print(l1)

l1.insert(0,34) # inserts something in a index. 
print(l1)       #inserts 34 at index 0

l1.pop(3)   #removes element from index 2
print(l1)

l1.remove(21)  #removes element 21 from the list
print(l1)

l1[7] = 9
print(l1)

