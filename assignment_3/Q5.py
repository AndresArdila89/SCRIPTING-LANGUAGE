'''
    Question 5: Given a list iterate it and count the occurrence 
    of each element and create a dictionary to show the count of 
    each element.

'''

demoList = [10,20,30,10,20,40,50]
dic = {}

for item in demoList:
    if item in dic:
        dic[item] +=1
    else:
        dic[item] = 1

print(dic)