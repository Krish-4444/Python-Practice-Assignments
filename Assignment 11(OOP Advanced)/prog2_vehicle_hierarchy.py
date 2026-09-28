"""
Program 2: Create a class hierarchy for Vehicle -> Car -> ElectricCar.
"""

# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} vehicle is starting.")


# Intermediate derived class (Single inheritance from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def drive(self):
        print(f"Driving the {self.brand} {self.model} running on {self.fuel_type}.")


# Multi-level derived class (Inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        # Fuel type for electric car is 'Electric'
        super().__init__(brand, model, fuel_type="Electric")
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.brand} {self.model} with {self.battery_capacity} kWh battery.")


def main():
    print("--- Program 2: Vehicle -> Car -> ElectricCar Hierarchy ---")
    
    tesla = ElectricCar(brand="Tesla", model="Model 3", battery_capacity=75)
    
    # Accessing methods from Vehicle, Car, and ElectricCar
    tesla.start()
    tesla.drive()
    tesla.charge()


if __name__ == "__main__":
    main()
