"""
    Lambda in Python
"""

def squareNum(n):
    return n*n 

nums = [10,20,30,40]

resull_1 = map(squareNum, nums)
print(list(resull_1))

#lambda labda_args_list:expression
result_2 = map(lambda n:n*n, nums)
print(list(result_2))