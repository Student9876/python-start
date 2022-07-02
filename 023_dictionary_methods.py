mydict = {
    "zeon": "Currently a programming Learner",
    "fast": "In a quick manner",
    "marks": [1,2,5],
    "anotherdict": {"zeon":"gamer"},
     1:7
}
# Dictionary Methods
print(mydict.keys()) #Prints the keys of the dictionary
print(mydict.values()) #Prints the values of the corresponding keys
print(mydict.items()) #Prints the (key, value) of the keys within ()

#Update dictionary. It adds keys with values
print(mydict)
updateDict = {
    "Google" : "Assistant",
    "Mouse" : "Cat",
    56 : 90,
    "marks": [34,56,73]   # It also updates the key already present
 }
mydict.update(updateDict)
print(mydict)

# Use of .get
print(mydict.get('zeon')) #same result as print(mydict['zeon']) but 

# Difference between .get and[] syntax in Dictionary
print(mydict.get('zeon2'))   #it Returns none
#print(mydict['zeon2'])       #Throws error

