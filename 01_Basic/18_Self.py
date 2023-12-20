#Example with ‘self’
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

# Creating an instance of MyClass
obj = MyClass(42)

# Calling a method that uses 'self'
obj.print_value()  # Output: 42

#Example without ‘self’
class MyClass2:
    def __init__(self, value):
        # 'value' is a local variable, not an instance variable
        value = value

    def print_value(self):
        # This will raise an error because 'value' is not defined in this scope
        print(value)

# Creating an instance of MyClass
obj = MyClass2(42)

# Calling a method that tries to access 'value' without 'self'
obj.print_value()  
# Raises NameError: name 'value' is not defined

