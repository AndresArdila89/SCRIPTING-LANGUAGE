# Variables in python class 3


x = 3
y = x+3
print(y)


CLIENT_1 = "Marry"
print(CLIENT_1)


print("========integers=========")
age = 23
print(age)
print(type(age))
print(id(age))


print("========floats=========")
price = 19.99
print(price)
print(type(price))
print(id(price))

price = price + 10
print(price)
print(type(price))
print(id(price))

print("========complex=========")

z = 30 + 2j
print(z)
print(type(z))
print(id(z))

z = 300 + 2j
print(z)
print(type(z))
print(id(z))

print("========complex=========")
"""
grade = int(input("Enter your Marks:"))
print(type(grade))
print("current grade: ", grade)
# casting from string to integer

print("new grade: ", grade + 10)
"""

# integers and floats are inmutable objects in python we can not keep the memory value
# every time that the value of the integer or float changes, the memory address changes as well


print("===== arithmetic operators ======")

a = 10
b = 5

print("10 + 5 --> ", a + b)
print("10 - 5 --> ", a - b)
print("10 * 5 --> ", a * b)
print("10 / 5 --> ", a/b)
print("10 // 5 --> ", a // b)
print("10 % 5 --> ", a % b)
print("10 ** 2 --> ", a ** 2)

print("==== comparison operator ======")
print("10 == 5 -->", a == b)
print("10 != 5 --> ", a != b)
print("10 >= 5 --> ", a >= b)
print("10 > 5 --> ", a > b)
print("10 <= 5 --> ", a <= b)
print("10 < 5 --> ", a < b)
print("=======Assigment Operators ======")
print(id(a))
a = a + 10
print("10 + 10 --> ", a)
print(id(a))

a += 10
print("20 + 10 --> ", a)

a -= 10
print("30 - 10 --> ", a)

a += 10
print("20 + 10 --> ", a)


print("======= bitwise opperator =======")

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = b & b  # 12 = 0000 1100
print("60 & 13 --> ", c)

c = a | b  # 61 = 0011 1101
print("60 | 13 --> ", c)

c = a ^ b  # 61 = 0011 1101
print("60 | 13 --> ", c)

c = ~a  # 61 = 0011 1101
print("60 | 13 --> ", c)

c = a << 2  # 240 = 1111 0000
print("60 << 2 --> ", c)

c = a >> 2  # 15 = 0000 1111
print("60 >> 2 --> ", c)


print("==== membership opperator ====")
lst_1 = [1, 2, 13, 5, 90]

print(1 in lst_1)
print(60 in lst_1)

print("===== identity opperator ======")
x1 = [1, 2, 3]
x2 = x1
x3 = list(x1)
print(x1)
print(type(x1))
print(x2)
print(type(x2))
print(x3)
print(type(x2))

print("x1 == x2 --> ", x1 == x2)
print("x1 is x2 --> ", x1 is x2)
print("x1 is x3 --> ", x1 is x3)
