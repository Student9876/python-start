this = "       Zeon is a good         "
print(this)
print(this.strip())  # it cutoffs the extra spaces(White Spaces) in the front and end


def remove_and_strip(string, word):
    newStr= string.replace(word, "")
    return newStr.strip()
    
print(remove_and_strip(this, "a"))
