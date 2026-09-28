"""
Program 1: Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
"""

class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"Accelerated by {increment} km/h. Current speed: {self.speed} km/h")

    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"Braked by {decrement} km/h. Current speed: {self.speed} km/h")

    def display_status(self):
        print(f"Car: {self.brand} {self.model} | Current Speed: {self.speed} km/h")


def main():
    print("--- Program 1: Car Class Demo ---")
    my_car = Car(brand="Toyota", model="Supra", speed=40)
    my_car.display_status()

    my_car.accelerate(30)
    my_car.accelerate(20)
    my_car.brake(50)
    my_car.brake(60)


if __name__ == "__main__":
    main()
