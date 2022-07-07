#WAP to create a dictionary of Hindi words with values as their english translation
myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Object"
}
print("Options are\n", myDict.keys())
a=input("Enter the Hindi Word:\n")
print("The meaning of your word is:", myDict.get(a)) 
#We used myDict.get() instead of myDict[] because it will not throw error if the item is not present
