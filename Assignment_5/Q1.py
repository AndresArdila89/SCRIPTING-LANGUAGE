# Question 1: Write a program to calculate factorial of a number
# (note: you could create a recursive function to calculate factorial).
# In addition, you need to write a decorator named time_calculator to calculate duration taken by factorial / any other function.
# Hint: import time module and use (end – begin ) and display total time taken by factorial function.

import time


def time_calculator(original_function):
    def wrapper_function(n):
        sec = time.time()
        original_function(n)
        print('end time', time.time()-sec)
    return wrapper_function


def calcFactorial(n):
    counter = n - 1
    while counter > 0:
        n = counter * n
        counter -= 1
    print(n)


decorato_function = time_calculator(calcFactorial)
decorato_function(6)
