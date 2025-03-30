#Inheritance

# a class that inherits from another class is called a subclass
# a class that is inherited from is called a superclass

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the vehicle...")

    def stop(self):
        print("Stopping the vehicle...")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, num_wheels):
        super().__init__(make, model, year) # call the constructor of the superclass or parent class
        self.num_doors = num_doors
        self.num_wheels = num_wheels

class Bike(Vehicle):    
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year) # call the constructor of the superclass or parent class
        self.num_wheels = num_wheels



car = Car("Toyota", "Camry", 2022, 4, 4)
car.start()
car.stop()
print(car.__dict__)

bike = Bike("BMX", "Mountain", 1902, 2)
bike.start()
bike.stop()
print(bike.__dict__)


