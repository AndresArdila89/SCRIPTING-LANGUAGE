# set
originalCharacters = {'f', 'b', 'U', 'i', 'o', 'E', 'a'}


def lowerAndUper(c):
    y = (c.lower(), c.upper())
    return y


result = map(lowerAndUper, originalCharacters)

print(result)
