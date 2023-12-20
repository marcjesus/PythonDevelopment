# Generator function that yields squares of numbers from 1 to n
def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

# Function to calculate the sum of squares using return
def calculate_sum_of_squares(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return sum(squares)

# Calculate sum of squares using the generator function
n = 10

# Using the generator function
squares_generator = generate_squares(n)
sum_using_generator = sum(squares_generator)

# Using the regular function
sum_using_return = calculate_sum_of_squares(n)

print("Sum of squares using generator function:", sum_using_generator)
print("Sum of squares using regular function:", sum_using_return)
