"""
Program 5: Create a polymorphic function that works with different shapes.
"""

import math

# Base Shape Class
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Polymorphic Function: accepts any shape object and computes details
def print_shape_info(shape):
    shape_name = shape.__class__.__name__
    print(f"Shape: {shape_name:<10} | Area: {shape.area():.2f} | Perimeter: {shape.perimeter():.2f}")


def main():
    print("--- Program 5: Polymorphic Function with Shapes ---")
    
    shapes = [
        Circle(radius=5),
        Rectangle(width=4, height=6),
        Triangle(a=3, b=4, c=5)
    ]
    
    for s in shapes:
        print_shape_info(s)


if __name__ == "__main__":
    main()
