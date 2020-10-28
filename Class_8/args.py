"""
    Type of arguments in Python ---> Positional Arguments -- Keyword Arguments
   


"""

def student_info_1(c1,c2, name=None, age=0):
    print(c1)
    print(c2)
    print(name)
    print(age)


student_info_1("Math","Comp sci", name="James", age= 22)
## the key word argument has no problem withthe order in wich is place
student_info_1("Math","Comp sci",  age= 22, name="James")
## but Positional Arguments needs to be passed in the position where is define
## this line gisve an error ---> student_info("Math",  age= 22, "Comp sci", name="James")


def student_info_2(*args, **kwargs):
    print(args)
    print(kwargs)
    print("====== Separate values from keys =======")
    print(kwargs.keys)
    print(kwargs.values)

student_info_2("Math", name="andres")

courses = ["Math","CS","History"]
info = {'age':21,'name':"Andres",'phone':"514-621-2222"}
print("======================")
student_info_2(*courses,**info)
