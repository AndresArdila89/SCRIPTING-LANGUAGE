"""
    Decorators
    Author: Andres
    Data: 29-oct-2020
"""

def call_me(m):
    msg = m
    def inner_call_me():
        print(msg)
    return inner_call_me

result_1 = call_me("Call me right away")
result_2 = call_me("Call me right away!!")
result_3 = call_me("Call me right away!!!!!!!!!!!!!!!!!!!")

result_1()
result_2()
result_3()

def decorator_func(my_func):
    def wrapper_func(*args, **kwargs):
        print(f"Before running {my_func.__name__} funciton ...")
        return my_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def display():
    print("Hello Guys!")


@decorator_func
def display_Info(name = None):
    print(f"Hello {name} ")



# result = decorator_func(display)
# result_4 = decorator_func(display_Info)
# result_4(name="Andres")
print("Testing the decorator @decorator_func")
display_Info(name="andres")
