letter = '''Dear <|Name|> 
Greetings from XYZ Corporation. Congratulations!!
Your are selected!!

Date: <|Date|>
'''
name = input("Enter your name:\n")
date = input("Enter Date:\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)