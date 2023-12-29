# The task of constructors is to initialise (assign values) to the data members of the class when an object of class is created. 
# In python __init()__ method is called the constructor and is always called when an objcect is created. It’s possible 
# to store information in instances if the variable is initialised under __init__.  

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
