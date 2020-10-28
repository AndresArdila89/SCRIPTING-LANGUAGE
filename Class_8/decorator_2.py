"""
 decorator Example 

 """

 ### Logger

def my_loogger(my_func):
    
    import logging
    logging.basicConfig(filename=f"{my_func.__name__}.log",level=logging.INFO)
    
    def wrapper_func(*args, **kwargs):
        logging.info(f"{my_func.__name__} is running with positional args: {args} and keyword args: {kwargs}")
        return my_func(*args, **kwargs)
    return wrapper_func

@my_loogger
def student_info(name, age):
    print(f"this is {name}  -- {age}")


student_info(name="Anna",age = 22)
student_info(name="Andres",age = 31)
