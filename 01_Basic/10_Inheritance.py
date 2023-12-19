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
