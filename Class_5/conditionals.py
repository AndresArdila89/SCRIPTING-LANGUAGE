"""

    if-else-elif
"""

age = 25
if age > 18 and age < 60:
    print("welcome")
    print("=======")
else:
    print("done")
print("party is over")

# nested conditional statement

num = 30
if num % 2 == 0:
    print(num, "is a factor of 2")
    if num % 3 == 0:
        print(num, "is a factor of 3")
        if num % 5 == 0:
            print(num, "is a factor of 5")
        else:
            print(num, "is not a factor of 5")
    else:
        print(num, "is not a factor of 3")
else:
    print(num, "is not a factor of 2")
print("I'm out side of the IF ")


if num % 2 == 0:
    print(num, "is a factor of 2")
elif num % 3 == 0:
    print(num, "is a factor of 3")
elif num % 5 == 0:
    print(num, "is a factor of 5")
else:
    print("Non of them")
