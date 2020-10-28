"""
    Pass By Value: All inmutable objects are passed by value
    Pass By Reference: All mutable objects are passed by reference


"""

def changeVal_1(x):
    x += 10

def changeVal_2(l):
    l.append(60)

def changeVal_3(l):
    l = []
    l.append(60)


print("======= Example 1 =======")
n = 10
print("Before calling ....", n)
changeVal_1(n)
print("After calling ...", n)

print("======= Example 2 =======")
lst_1 = [10,20,30,40]
print("Before calling ...", lst_1)
changeVal_2(lst_1)
print("After calling ...", lst_1)

print("======= Example 3 =======")
print("Before calling ...", lst_1)
changeVal_3(lst_1)
print("After calling ...", lst_1)


