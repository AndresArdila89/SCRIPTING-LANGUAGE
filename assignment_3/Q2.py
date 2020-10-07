###Question 2: Given an input string Count all lower case, upper case, digits, and special symbols


def countCharType(word):
    lowerCounter = 0
    upperCounter = 0
    digitCounter = 0
    symbolCounter = 0

    strLen = len(word)

    for i in range(0,strLen):

        if word[i].islower():
            lowerCounter += 1

        elif word[i].isupper():
            upperCounter += 1
            
        elif word[i].isdigit():
            digitCounter += 1
        else:
            symbolCounter +=1

    return f"lowerCase: {lowerCounter} , upperCase: {upperCounter} , digit: {digitCounter} , symbol: {symbolCounter}"


print(countCharType("Andre#$@kdjf8989"))
