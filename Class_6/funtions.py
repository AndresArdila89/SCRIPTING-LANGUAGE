"""
    Functions in python
    Author: Andres Ardila
    Date: 07 oct 2020
"""
"""
print('Hello Python')

saySth = input('Say Something')

print('Hello ', saySth)

x = 2 
y = 4 
print('4 power of 2 ---', pow(4,2))

abs_val  = abs(-9)
print(abs_val)

import math

print(math.sin(90))
print(math.floor(4.3))
print(math.log10(8))
print(math.sqrt(9))


from math import sin,floor,sqrt,log10

"""



###======== User Define Function 
def isEven(n):
    if n %2 ==0:
        return True
    return False

# def isPrime(n):
#     for x in range(2,n):
#         if n%x ==0:
#             return f' the number is NOT prime'
#         else:
#             return f' the number is prime'
def isPrime(n):
    flag = True
    for x in range(2,n):
        if n%x == 0:
            flag == False
            break
    if flag == True:
        return f' {n} the number is a prime'
    else: 
        return f' {n} the number is NOT prime'
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


num = int(input('Enter any number'))
print(factorial(num))




