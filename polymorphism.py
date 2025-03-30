#  Polymorphism
# polymorphism means having many forms

# No polymorphism

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the vehicle...")

    def stop(self):
        print("Stopping the vehicle...")

class MotorCycle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_bike(self):
        print("Starting the motorcycle...")

    def stop_bike(self):
        print("Stopping the motorcycle...")


# vehicles = [
#     Car("Toyota", "Camry", 2022),
#     MotorCycle("Honda", "CBR", 2023)
# ]

# for vehicle in vehicles:
#     if isinstance(vehicle, Car): #type scoping
#         print(f'inspecting {vehicle.make} {vehicle.model} {vehicle.year}')
#         vehicle.start()
#         vehicle.stop()
#     elif isinstance(vehicle, MotorCycle):
#         print(f'inspecting {vehicle.make} {vehicle.model} {vehicle.year}')
#         vehicle.start_bike()
#         vehicle.stop_bike() 

# Polymorphic approach

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
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    # def start(self):
    #     print("Starting the vehicle...")

    # def stop(self):
    #     print("Stopping the vehicle...")

class MotorCycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    # def start(self):
    #     print("Starting the motorcycle...")

    # def stop(self):
    #     print("Stopping the motorcycle...")


vehicles = [
    Car("Toyota", "Camry", 2022),
    MotorCycle("Honda", "CBR", 2023)
]

for vehicle in vehicles:
    print(f'inspecting {vehicle.make} {vehicle.model} {vehicle.year}')
    vehicle.start()
    vehicle.stop()
