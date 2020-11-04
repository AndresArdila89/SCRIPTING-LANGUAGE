"""
    Reduce in Python


"""
from functools import reduce
def mySum(x,y):
    return x+y
def myMulti(x,y):
    return x*y


myList = [1,2,3,4,5,6,7]
print(reduce(mySum, myList))
print(reduce(myMulti, myList))
