# Decorators
import time
#This will be run first
def timer_decorator(func):   
    def wrapper(*args, **kwargs):
#This will be run second
        start_time = time.time()  
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

#THIS IS A DECORATOR
@timer_decorator    
def my_function():
#This will be run last
    time.sleep(2)   
my_function()
