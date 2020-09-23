s1 = 'Introduction to Python'
print(s1)
print(s1[0])

print(s1[5])
print(s1[-1])
print(s1[-2])
print(s1[-7])

print(s1[0:5])
print(s1[:13])
print(s1[16:-1])
print(s1[-2:-5])###retun and empty char

s1 = s1 + " for students"
print(s1)
##print(s1 + 2)  error
##print(s1 * 2)

print(s1[0:5] + 'D' + s1[6:13])




###========== methods

s2 = 'Welcome to Python'
print(s2)
print(len(s2))

print(s2.upper())
print(s2.lower())
print(s2.count('O'))
print(s2.count('o'))
print(s2.count('come'))
print(s2.find('o'))### retuns the index where o is store
print(s2.find('o',16))### the find function begins to search for the character o from the index 16 forward

##print('W' + s2[1:])

print('come' in s2)
print('come' in s2)


## separated strings by comma
s3 = 'java, c++, python'
print(s3.split(', '))

###======= input method
## price = input("Enter your item price: ")
## price = price + 0.2 gives error
## price = price * 0.2 gives error bercause is afloat, multiplication only works if the number is an int


price = float(input("Enter your item: "))
price = price * 0.2 ## it works because we cast price into a float
print(price)

###========= format method ---- format string

num1 = 3.12345678
num2 = 10.12345678

print('Num1 is ', num1, 'Num2', num2)

### total of 3/4  digits after and before the decinal point
print('Num1 i9s { 0:.3f} Num2 is {1:.4}',format(num1,num2))

###total of 3/4 digits after and before the decimal point
print(f'Num2 is {num2:.3f} Num1 is {num1:.4f}')
