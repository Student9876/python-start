story = '''once upon a time there was a student 
named ZEON who loved to code'''

#string Functions
print(len(story))
print(story.endswith("code"))
print(story.count("a"))
print(story.count("time"))
print(story.capitalize())
print(story.find("student")) # it shows only first occurrence with its first index.
                            #If there is no such words then -1
print(story.replace("ZEON","zeon"))  #replaces all occurrences. (old,new)   


#f-string(Learn More about it in Multiplication table)
# print(f"{num}X{i}={multi}") #This is called f string. And this is how we can use it
