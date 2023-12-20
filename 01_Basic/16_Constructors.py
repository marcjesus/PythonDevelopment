class Dog:
    scientific = "Canis lupus familiaris"

    def __init__(self,name):
        self.name = name
        self.woofs = 0 

    def speak(self):
        print("Woof!")

    def hear(self, words):
        if self.name in words: 
            self.speak()
 
    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak() 

my_dog = Dog("Nemo") #Instance of the Dog class 
my_dog.hear("Nemo, say hello")
my_dog.count() #It will increase woof prints
my_dog.count()
