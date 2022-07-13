#This is f string
name = "ZEON"
a = f"This is {name}"
print(a)
channel = "Goner"
type = "coding"
#but before f string they used 'format'

a = "This is {} and his channel is {}".format(name, channel)
print(a)

#another type(Using index)

a = "This is {0} and his {1} channel is {2}".format(name, type, channel)
print(a)