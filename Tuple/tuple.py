"""

    Tuple in Python
    Author: Andres
    Date: 23-Sept-2020

"""

T1 = (12, 22.9, "Hello", [1, 2, 3], (9, 8))
print(T1)
print(type(T1))
print(id(T1))
print(T1[0])
print(T1[-2])

"""tuple is an unmutable object, values cannot be assign separetly"""

# T1[0] = 1220 TypeError: tuple objectdoes not support item assigment

# this way the values inside the tuple can be change
T1 = (1200, 22.9, "Hello", [1, 2, 3], (9, 8))
print(T1)
print(type(T1))
print(id(T1))
# T2 = (20) this is not a tuple
T2 = (20,)  # by adding the comma python undestands it as a tuple
print(T2)
print(type(T2))
print(id(T2))


# this is another way of deffining a tuple
T3 = "hello", "its me", "again", 23, "times"
print(T3)
print(type(T3))

print(T3[0:4])
print(T1[-2:])
print(T1[-1][-1])  # print an element from an array inside a tuple

# tuple can only be concatenated with another tuple.
new_T1 = T1[:2] + ("bonjou",) + T1[3:]

T4 = T2 + T3
print(T4)

msg = "Pia"
print(type(msg))
new_msg = "T" + msg[1:]
print(new_msg)

print(T3 * 2)


TT = T2, T3
print(TT)
print(len(T4))
print(len(TT))


print(T4[-1][-1])
print(TT[-1])
print(TT[-1][-1])

print(20 in T4)  # verified if an element is inside the tuple returns a boolean
print(20 in TT)

T5 = ("Math", "Art", "Comp Sci", "Math")
print("The number of Math is ", T5.count("Math"))
print("The index of Math is ", T5.index("Math"))
print("The index of Math is ", T5.index("Math", 1))
#print("The index of Math is ", T5.index("Math", 4))

seansons = ("Spring", "Summer", "Fall", "Winter")
print(seansons[0])
print(seansons[1])
print(seansons[2])
print(seansons[3])
print("==================")

s1, s2, s3, s4 = seansons

print(s1, s2, s3, s4)
