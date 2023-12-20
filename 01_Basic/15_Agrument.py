# Function without using kwargs
def greet_without_kwargs(name, age):
    print(f"Hello {name}! You are {age} years old.")

# Function using kwargs
def greet_with_kwargs(**kwargs):
    if 'name' in kwargs and 'age' in kwargs:
        print(f"Hello {kwargs['name']}! You are {kwargs['age']} years old.")
    else:
        print("Please provide both 'name' and 'age'.")

# Calling functions with and without kwargs
greet_without_kwargs('Alice', 30)  # Without kwargs
greet_with_kwargs(name='Bob', age=25)  # With kwargs