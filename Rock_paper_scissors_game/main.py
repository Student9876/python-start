#Rock Paper Scissors Game with Computer
import random

def game(comp, you):
    #checking all possibilities
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False        

def HS(a):
    if a == True:
        with open('Rock_paper_scissors_game\log_highscore.txt' , 'a') as f:
            f.write("Win\n")
    elif a == False:
        with open('Rock_paper_scissors_game\log_highscore.txt' , 'a') as f:
            f.write("Lose\n")
    elif a == None:
        with open('Rock_paper_scissors_game\log_highscore.txt' , 'a') as f:
            f.write("Draw\n")

print("comp Turn: Rock(r) Paper(p) Scissors(s)?")
randNo = random.randint(1, 3)  #Here select a random number between 1-3
# print(randNo)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) Scissors(s)?")

result=game(comp, you)
if result == True:
    HS(True)
    print(f"Computer chose {comp} and you chose {you} You win!!")
elif result == False:
    HS(False)
    print(f"Computer chose {comp} and you chose {you} You lose ;);)")
else:
    HS(None)
    print(f"Computer chose {comp} and you chose {you} Draw")
    