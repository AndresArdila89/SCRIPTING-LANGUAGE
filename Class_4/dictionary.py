"""
    Dictionary in Python
    Author: Andres
    Date: 23-Sep-2020

"""
# dictionary = {key:value,key:value......} the keys must be unmutable objects such as int float tuple
D1 = {1: "ONE", "Two": 2, (1, 1): 1000, 12.9: "Hello"}

print(D1)
print(type(D1))
print(id(D1))

# print(D1[0]) dictionary navigation is not done by index

print(D1[1])
# print(D1[0:3]) TypeError: unhashable type: 'slice'

D1[1] = 'ONE on ONE'
print(D1)
print(type(D1))
print(id(D1))
# dictionary is a mutable object

grades = (90, 87, 79)
java, cpp, python = grades

D2 = {'java': 90, 'cpp': 87, 'python': 79}
print(D2['java'])
D2['java'] = 90*1.02
print(D2['java'])

D3 = {(1, 1): 1000, (2, 2): 2000}
print(D3)

D4 = {1: 100, 2: 200, 3: 300}
# dictionary takes the last value of a duplicated key
D5 = {1: "10", 2: 20, 3: 30, 1: 10}
# print(D4 + D5)  Error:  it is not index base

print(D5)


# print(D3 * 2) gives errror because is not gonna print the same value

print(len(D5))  # len function does not depends on the index

print(1000 in D3)
print((1, 1) in D3)
