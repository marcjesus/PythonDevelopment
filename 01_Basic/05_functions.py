# Function annotations and type hints allow you to provide additional information about function arguments and 
# return values. They enhance code readability and help catch potential type-related errors during development. 


# Function Annotations and Type Hints
def add_numbers(x: int, y: int) -> int:
    return x + y

result = add_numbers(5, 10)
print(result)