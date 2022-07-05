#Use open function to read the content of a file
# f = open('sample.txt', 'r')
f = open('sample.txt') #by default mode is Read mode
# data = f.read()
data = f.read(5) #reads first 5 characters from the file
print(data)
f.close


'''
Modes of Opening a file
r --> open for reading
w --> open for writing
a --> open for appending(addind data at last)
+ --> open for updating


'rb'--> will open for read in binary mode
'rt'--> will open for read in text mode
by default it opens in 'rt' if only r is written
'''