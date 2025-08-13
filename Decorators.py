from typing import Callable
import time
from functools import wraps


# Decorator for func with param
# def timer_deco(func: Callable):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f"time of working is {end - start}")
#         return res
#     return wrapper

# @timer_deco
# def my_func(sleep_sec: int):
#     time.sleep(sleep_sec)
#     return 124

# print(my_func(3))


# Decorator with param

def limit_calls(limit: int):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            """Shit docstring"""
            nonlocal limit
            if limit == 0:
                print("Func can't be called")
                return
            
            res = func(*args, **kwargs)
            limit -= 1
            return res
        return inner
    return wrapper
    
@limit_calls(2)
def my_func(sleep_sec: int):
    """Very important docstring!!!"""
    time.sleep(sleep_sec)
    return 123

for i in range(3):
    print(my_func(1))

print(my_func.__doc__)
print(my_func.__name__)