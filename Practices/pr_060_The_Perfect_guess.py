import random

randNo = random.randint(1, 100)
n = int(input("Enter a number between 1-100: "))
with open('Practices\log_highscore1.txt', 'a') as f:
    f.write(f"{n}\n")
    
if n>randNo:
    print(f"Your guess is bigger than the random number {randNo}")    
    
elif n<randNo:
    print(f"Your guess is smaller than the random number {randNo}")    

elif n==randNo:
    print(f"Your guess is same as than the random number {randNo}")    
