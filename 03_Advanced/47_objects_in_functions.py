# Define the Dog class
class Dog:
   def __init__(self, name, breed):
       self.name = name
       self.breed = breed


   def bark(self):
       return "Woof!"


# Function that uses an object from the Dog class
def greet_dog(dog):
   return f"Hello, {dog.name}! You are a {dog.breed} dog. {dog.bark()}"

# Creating a Dog object
my_dog = Dog("Buddy", "Golden Retriever")


# Calling the function with the Dog object
greeting_message = greet_dog(my_dog)


# Printing the greeting message
print(greeting_message)


# OUTPUT: Hello, Buddy! You are a Golden Retriever dog. Woof!
