class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.value = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

# Creating instances of MyClass
obj1 = MyClass(42)
obj2 = MyClass(99)

# Calling the class method to increment class_variable
obj1.increment_class_variable()
print(MyClass.class_variable)  # Output: 1

obj2.increment_class_variable()
print(MyClass.class_variable)  # Output: 2