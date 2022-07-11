list = [1, 2, 3, 4, 6, 3, 54, 23, 23, 34 ,6 ,8 ]

b =[]
for index, item in enumerate(list) :
    if index==2 or index== 4 or index== 6:
        print(f"The {index +1}th item is: {item}")