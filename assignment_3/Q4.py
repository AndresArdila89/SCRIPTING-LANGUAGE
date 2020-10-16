'''
    Question 4: Given an input string, count occurrences 
    of all characters within a string.
'''

string = "andres"

letterInString = {}

for i in string:
    if i in letterInString:
        letterInString[i] += 1
    else:
        letterInString[i] = 1

    

print(letterInString)