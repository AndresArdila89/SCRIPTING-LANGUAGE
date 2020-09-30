"""
    Set in Python
"""

SS1 = "Hello Python"
L1 = [1, 20.5, "Hello", [1, 2, 3, 4]]
T1 = (1, 20.5, "H1", (1, 2, 3))
D1 = {(1, 1): "Hi", (2, 2): "Hola"}

S1 = {1, 20.5, "Hello"}
print(S1)
print(type(S1))
print(id(S1))

S1.add("Python")
print(S1)

L2 = []  # L2 = list()
print(type(L2))
T2 = ()  # T2 = tuple()
print(type(T2))
D1 = {}  # D1 = dict()
print(type(D1))
S1 = set()
print(type(S1))

print("--------------- break-------------------")

Langs = ["Java", "Python", "C++"]
print(Langs)
print(id(Langs))
cp_Langs = Langs.copy()
print(cp_Langs)
print(id(cp_Langs))

# clear the object
# cp_Langs.clear()
print(cp_Langs)
print(id(cp_Langs))

# Remove any alement from the set
# cp_Langs.remove("Java")
print(cp_Langs)
print(id(cp_Langs))

# Discard does not throw an error when item is not foound

# cp_Langs.discard("Java")
print(cp_Langs)

print(cp_Langs.pop())


print(type(Langs))

Langs.append("Java")

print(Langs)


Langs2 = {"JQuery", "GO", "Java", "Python"}
Langs3 = {"JavaScript", "Kotlin", "Lisp", "R"}
Langs4 = {"Python", "Java"}

print(Langs2)
print(Langs3)
print(Langs4)

# -------------isdisjoint
print("-------- disjoint")
print(Langs2.isdisjoint(Langs3))
print(Langs2.isdisjoint(Langs4))

# -------------- issubset
print("-------- subset")
print(Langs2.issubset(Langs3))
print(Langs2.issubset(Langs4))

# -------------- issuperset
print("-------- superset")
print(Langs2.issuperset(Langs3))
print(Langs2.issuperset(Langs4))


# -------------- union
print("-------- union")
print(Langs2.union(Langs3))
print(Langs2.union(Langs4).union(Langs3))

# -------------- difference
print("-------- difference")
print(Langs2.difference(Langs3))
print(Langs2.difference(Langs4))

# -------------- symetric_difference
print("-------- symetric difference")
print(Langs2.symmetric_difference(Langs3))
print(Langs2.symmetric_difference(Langs4))

#------------- applie
print("-------- exer")
print(Langs2)
print(Langs3)
print(Langs4)

print(Langs2.difference(Langs4))
