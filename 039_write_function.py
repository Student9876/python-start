# Comment out one function to check another
# Write functions overwrites new data on the previous data
f = open('another.txt', 'w') #if the text file is not present, It will create a new text file and write in it
f.write("I'm writing")   #This print will be perforemed how many times you write it
f.write("I'm writing")    #f.write accepts a string
f.close()


# f = open('another.txt', 'a')
# f.write("I am appending\n")
# f.close()

