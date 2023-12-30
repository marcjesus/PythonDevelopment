# Static Methods are defined using the ‘@staticmethod’ decorator. They don’t operate on instances or class variables. 
# They are bound to the class and can be called on the class itself. 
# Static methods are often used for utility functions that don’t depend on instance or class state.

class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)

# Creating an instance of MyClass
obj = MyClass(42)

# Calling the instance method
obj.display()  # Output: 42