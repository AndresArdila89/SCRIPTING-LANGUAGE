listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
newlist = []
x = 0
while x < len(listOne):
    if x % 2:
        newlist.append(listOne[x])
        x += 1
    else:
        newlist.append(listTwo[x])
        x += 1

print(newlist)
