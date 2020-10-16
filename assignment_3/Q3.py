'''
    Question 3: String characters balance Test
    We’ll say that a String s1 and s2 is balanced if all the chars in the string1 are there in s2.
    characters position doesn’t matter.
'''

s1 = "nyf"
s2 = "Pynative"
x = True


for letter in s1:
    if not letter in s2:
        x = False
        break
    else:
        pass


print(x)
