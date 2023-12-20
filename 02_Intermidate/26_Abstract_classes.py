from abc import ABC, abstractmethod

# Define an abstract class named Shape
class Shape(ABC):
    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def area(self):
        pass

# Derived class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementation of the abstract method area() for Circle
    def area(self):
        return 3.14 * self.radius * self.radius


# Derived class Square inheriting from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    # Implementation of the abstract method area() for Square
    def area(self):
        return self.side * self.side

# Create objects of Circle and Square classes
circle = Circle(5)
square = Square(4)

# Call the area() method for Circle and Square objects
print("Area of the circle:", circle.area())  
# Output: Area of the circle: 78.5
print("Area of the square:", square.area())  
# Output: Area of the square: 16
