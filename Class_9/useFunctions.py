"""
    Using map - filter - lambda - reduce

"""

c = map(lambda x: x+x, filter(lambda x:(x >= 4),[1,2,3,4,5,6,7]) )
print(list(c))

d = filter(lambda x:(x >= 8),map(lambda x:x+x,[1,2,3,4,5,6,7]))
print(list(d))