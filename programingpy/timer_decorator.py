import time
from icecream import ic

def timer(function):
    def wrapper(*args, **kwargs):
        fname = function.__name__
        first_time = time.time()
        value = function(*args, **kwargs)
        after_time = time.time()
        ic(f'The function {fname} took {after_time - first_time} secconds to finish')
        return value
    return wrapper

@timer
def add(num):
    result = 1
    for i in range(1,num):
        result *= 1
    return result

add(1030000)