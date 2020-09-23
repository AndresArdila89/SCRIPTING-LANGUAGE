x = 0
y = 0
print('input first number: ')
x = int(input())
print('input second number: ')
y = int(input())
r = x * y

if r < 1000:
    print('this is a multiplication: ', x*y)
else:
    print('this is a sum: ', x+y)
