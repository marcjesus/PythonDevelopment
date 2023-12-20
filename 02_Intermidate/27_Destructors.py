class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"Object {self.name} is being destroyed")

# Creating objects
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

# Deleting objects explicitly
del obj1
del obj2
