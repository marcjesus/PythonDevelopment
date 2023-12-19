class Dog:
    scientific = "Canis lupus familiaris" 

    def speak(self):
        print("Woof!")
    def learn_name(self,name):
        self.name = name
    def hear(self, words):
        if self.name in words: 
            self.speak()

my_dog = Dog() #Instance of the Dog class
my_dog.name = "Nemo" 
your_dog = Dog()
my_dog.speak() #Method call on the instance
your_dog.speak()

my_dog.hear("Nemo, say hello")