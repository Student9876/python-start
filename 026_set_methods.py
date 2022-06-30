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

b.add({4:5})
print(b)

b.add([4,5,7]) #we cannot add list in set
print(b)