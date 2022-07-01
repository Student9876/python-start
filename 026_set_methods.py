# Creating empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(4)
b.add(4)
b.add(5)
b.add(6)
b.add(6)
print(b)

b.add((4,5,8)) #We can add tuple in set
print(b)

# b.add({4:5})  #We cannot add dictionary in set
print(b)

# b.add([4,5,7]) #we cannot add list in set
print(b)

# Length of Set
print(len(b))

# Removal of an item

b.remove(5) # Removes 5 from set b
# b.remove(15) # throws an erroe while trying to remove 15 (which is not present in the set)
print(b)

# pop function
# Removes an arbitrary element from a set and return it
print(b.pop())
print(b)

#Clear function. It empties a set
b.clear()
print(b)