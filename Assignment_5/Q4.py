import random


ranNum = random.randint(0, 100)
gNumber = ranNum + 1

print("this  is the answer: ", ranNum)

while ranNum != gNumber:
    gNumber = input("Please input a number between 0 and 100: ")

    if gNumber > ranNum:
        print("This is higher than the actual number")
    elif gNumber < ranNum:
        print("This number is lower than the actual number")
    else:
        print("This is the correct number")

print("Thank you for playing number guess")
