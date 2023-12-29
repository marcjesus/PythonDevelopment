# A method is a function that “belongs to” an object. 
# List of objects have methods called append, insert, remove, sort, etc…

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        """Method to add two numbers"""
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        """Method to subtract y from x"""
        self.result = x - y
        return self.result

# Creating an instance of the Calculator class
calc = Calculator()

# Using the methods of the Calculator class
sum_result = calc.add(5, 3)
print("Sum:", sum_result)  # Output: Sum: 8

difference_result = calc.subtract(10, 4)
print("Difference:", difference_result)  # Output: Difference: 6
