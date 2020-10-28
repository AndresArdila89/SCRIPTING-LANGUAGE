"""
    Filters
    Author: Andres
    Date: 28-Oct-2020

"""


grades = [ 'A','B','F','A-','F']

### l- for loop
filteredGrades = []
for g in grades:
    if g != 'F':
        filteredGrades.append(g)
print(grades)
print(filteredGrades)

### 2 - List Comprehension 

newGrades = [g for g in grades if g != 'F']
print(newGrades)

### 3- Filter Method
def removeF(g):
    return g != 'F'

result = filter(removeF,grades)

print(result)