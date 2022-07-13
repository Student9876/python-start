def div(num):
    if num%5 == 0:
        return True
    else:
        return False

l = [1, 2, 3, 5, 50, 35, 4, 7, 34, 25, 65, 108]
print(list(filter(div, l)))


