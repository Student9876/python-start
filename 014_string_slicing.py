greeting = "Good Morning "
name = "Student"
# print(type(name))
#  Concatenating two strings 
# c = greeting + name 
# print(c)

print(name[1]) # will give output 'Z' of my name
# name[2] = "d" ---> Does not work changing char 

# String Slicing 
print(name[0:3])  # this will print from 0th char 
                  #to 2th char


print(name[:4]) # is same as name[0:4]
print(name[0:]) #same as name[0:6]

''' If length of a string is unknown but we want to access it's last characters,
 then -ve indices plays the role. Last time we used +ve indices to point out character 
out of a string. Index of the last character of a string will be '-1', before that '-2'.
'''
c = name[-5:-1] # same as name[2:7]
print(c)

#skipping values
name = "RepublicofGamers"
d = name[0::2] #this will print the characters skipping every 2nd value
print(d)
e= name[0::3] #will skip 2 values after printing 1 value
print(e)