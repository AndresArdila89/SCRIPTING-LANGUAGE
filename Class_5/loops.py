"""
    Loop in Python

"""

# for - while


num = 1
while num < 10:
    print(num)
    num = num + 1
    if num == 8:
        break

# range(start,end ,step)
T1 = ["Swift", "kotlin", "JavaScript", "Php", "C#"]
for i in range(len(T1)-1, -1, -1):
    print(i, ": ", T1[i])


for obj in D1.keys():
    print(obj)
