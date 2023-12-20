class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_car_info(self):
        car_info = f"{self.year} {self.make} {self.model}"
        return car_info

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Creating two instances of the Car class
car1 = Car('Ford', 'Fusion', 2019)
car2 = Car('Tesla', 'Model S', 2022)

# Accessing attributes and methods of each instance
print(f"Car 1: {car1.get_car_info()}")
car1.read_odometer()
car1.update_odometer(15000)
car1.read_odometer()

print("\n")

print(f"Car 2: {car2.get_car_info()}")
car2.read_odometer()
car2.update_odometer(5000)
car2.read_odometer()
