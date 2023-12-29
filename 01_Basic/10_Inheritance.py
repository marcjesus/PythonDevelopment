# Inheritance allows us to define a class that inherits all the methods and properties from another class. 
# Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, 
# also called derived class. pass can be used in class or method definitions to indicate that it's intentional for the definition to do nothing.

class Dog: 
    scientific_name = "Canis lupus familiaris" 
    def __init__(self, name): 
        self.name = name 
        self.woofs = 0 
    def speak(self): 
        print("Woof!")

class Hasky(Dog):
    origin = "Russia"
    def speak(self):
        print("Wuufff")

class chihuahua(Dog):
    pass

my_dog = Hasky("Alex")
my_dog.speak()
