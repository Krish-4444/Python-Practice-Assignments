"""
Program 7: Create a Circle class to find area and circumference.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Radius        : {self.radius}")
        print(f"Area          : {self.area():.2f}")
        print(f"Circumference : {self.circumference():.2f}")
        print("-" * 30)


def main():
    print("--- Program 7: Circle Class (Area & Circumference) ---")
    c1 = Circle(radius=7)
    c1.display()

    c2 = Circle(radius=3.5)
    c2.display()


if __name__ == "__main__":
    main()
