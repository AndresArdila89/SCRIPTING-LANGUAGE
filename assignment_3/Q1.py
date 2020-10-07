# Question 1: arrange String characters such that lowercase letters should come first

#Given input String of combination of the lower and upper case arrange characters in such a way that all lowercase letters should come first


def orderByLetterCase(word):
    lowerStr =""
    upperStr =""
    strLen = len(word)

    for i in range(0,strLen):
        if word[i].isupper():
            lowerStr = lowerStr + word[i]
            print("yes sir is a lowercase", lowerStr)
        else:
            upperStr = upperStr + word[i]
            print("is Upppercasseeee",upperStr)

    return lowerStr + upperStr



x = "$%^^^&"
print(orderByLetterCase(x))


