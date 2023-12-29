# Method overriding is the practice of re-implementing a method in a child class. 

class Shape:
   def no_of_sides(self):
       pass


   def three_dimensiomns(self):
       print("I am 3D from shape class")


class Rectangle(Shape):
   def no_of_sides(self):
       print("I have 4 sides. I'm from Rectangle class and I'm overriding")


re = Rectangle()
re.no_of_sides()