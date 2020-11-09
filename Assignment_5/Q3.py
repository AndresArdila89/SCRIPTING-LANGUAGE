list_one = [6, 5, 3, 9]
list_two = [0, 1, 7, 7]


def sumAndDiference(l1, l2):
    return (l1+l2, l1-l2)


result = map(sumAndDiference, list_one, list_two)

print(result)
