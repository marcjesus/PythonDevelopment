# "Is-a" Inheritance Example
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):  # Dog "is-a" type of Animal
    def make_sound(self):
        print("Woof!")

class Cat(Animal):  # Cat "is-a" type of Animal
    def make_sound(self):
        print("Meow!")

# Creating instances and using them

cat = Cat()
cat.make_sound()