# "Has-a" Composition Example
class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

# Creating instances and using them
car = Car()
car.start_engine()
car.stop_engine()