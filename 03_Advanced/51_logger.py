import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Decorator to log time taken and result of a function
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds. Result: {result}")
        return result
    return wrapper

# Example function to be timed
@log_execution_time
def calculate_sum(n):
    # Simulate some computation
    result = sum(range(1, n+1))
    return result

# Test the function
result = calculate_sum(10000)
