f = open('sample.txt') 
#reads first line
data = f.readline() #It also prints a \n
print(data)
#reads second line
data = f.readline() #Repeated two times to print 2 lines
print(data)
#Reads third line
data = f.readline() 
print(data)
f.close