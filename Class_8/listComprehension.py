"""
    List Comprehension
    Author: Andres 
    Date: 28-Oct-2020

"""

grades = [95.5,93,86,98.5,65,79]

modifiedGrades = []

for grade in grades:
    modifiedGrades.append(grade + 1.5)

print(grades)
print(modifiedGrades)


updateGrates = [grade + 1.5 for grade in grades]

print(updateGrates)

print("========= Example 2 =========")
nums = [1,2,3,4,5,6,7,8,9,10]

seqEvenNums = []

for num in nums:
    if(num ** 2)%2 == 0:
        seqEvenNums.append(num ** 2 )



print(nums)
print(seqEvenNums)

### studi this way of writing the for 
print([num ** 2 for num in nums if(num**2)%2 ==0])

