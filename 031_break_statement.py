# Break ends a loop at a point 
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for") 
    # It will not execute. Because loop wasn't ended normally. It was ended due to break
