'''
    Question 7: Write a python program to construct 
    the following pattern, using a nested for loop.
*
**
****
*****
******
*****
****
***
**
*
'''




#negative = False
# y=1
# while y > 0:
#     string = "*"*y
#     print(string)
#     if y == 10:
#         negative = True     
#     if negative:
#         y -= 1
#     else:
#         y += 1 

counter = 1
limit = 10
while (counter >0):
    
    string = ""
    y=0
    while (y < counter):
        string += "*"
        y +=1 
    if counter == limit:
        counter -=1
        limit -= 1
    else:
        counter +=1
    
    print(string)
