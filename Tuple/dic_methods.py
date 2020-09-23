seasons = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}

cp_seasons = seasons.copy()

print(seasons)
print(cp_seasons)

print(cp_seasons == seasons)
# exactlly the same, memory id needs to be the same in order to be true
print(cp_seasons is seasons)
print(id(cp_seasons))
print(id(seasons))
del cp_seasons

keys = seasons.keys()  # keys variable is a collection

print(keys)

values = seasons.values()
print(values)
print(type(values))

items = seasons.items()
print(items)


M1 = [[0, 0, 0.37, 0], [1, 0.34, 0, 0], [0, 0.5, 0, 0]]

print(M1[0][0])
print(M1[1][0])
print(M1[2][0])

M2 = {(1, 3): 0.37, (2, 1): 1, (2, 2): 0.34, (3, 2): 0.5, }

print(M2[(1, 3)])
print(M2.get())
