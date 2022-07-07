#Length of the following set
s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))
print(s) #In set 20 and 20.0 is counted as one element


#What is the type of s={}
s = {} #It's a dictionary 
print(type(s)) 