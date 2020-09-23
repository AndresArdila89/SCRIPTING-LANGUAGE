
L2 = [10, 20, 30, 40, 50]
print(L2)
L2[0] = 100
print(L2)

L2[1:3] = [200,300] ## update more than one element
print(L2)

L2[3:3] = [400,500]
print(L2)

L3 = [700,800, [800,900]]### nested list

print(L2 + L3)
print(L3*L2)

##L3 = []

del[L3] ##delete the list
## print(L3)

###======= Methods
L4 = ['Math', 'Algebra', 'Art']
L4.append('Comp Sci')
print(L4)
L4.append('Comp Sci')
L4.append('Math')
L4.append('Algebra')
print(L4)
print(L4.index('Math'))
print(L4.count('Math'))
L5 = ['English', 'French']
L4.extend(L5)
print(L4)
L4.removeL('Math')
print(L4)
L4.insert(3,'Design')
print(L4)

###L4.sort() this method affects the object
###print(L4)

print(sort(L4)) ##3this way the object does not get affected by the method sort()

L6 = [100, 9,20,1]
print(min(L6))
print(max(L6))
print(sum(L6))
