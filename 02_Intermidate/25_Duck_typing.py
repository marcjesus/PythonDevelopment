class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Duck:
    def sound(self):
        return "Quack!"

# Function that takes any object with a 'sound' method and prints its sound
def make_sound(animal):
    print(animal.sound())


# Instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# Calling the function with different objects
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!
make_sound(duck)  # Output: Quack!
