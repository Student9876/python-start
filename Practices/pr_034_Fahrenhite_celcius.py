#Convert celsius to fahrenheit

def convert(cel):
    return cel*9/5 + 32
a = int(input("Enter Celsius value: "))
print("Temp in fahrenheit is: ", convert(a))