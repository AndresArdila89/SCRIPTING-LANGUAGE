string = "Welcome to USA. usa awesome, isn't it?"
newString = string.lower()
counter = 0
result = 0

while result > -1:
    result = newString.find('usa', result)
    newString = newString[result+2:]
    counter += 1

print(counter)
