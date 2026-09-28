"""
Program 4: Create a Rectangle class with methods to find area and perimeter.
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print(f"Rectangle Dimensions: Length = {self.length}, Width = {self.width}")
        print(f"Area      : {self.area()}")
        print(f"Perimeter : {self.perimeter()}")


def main():
    print("--- Program 4: Rectangle Class (Area & Perimeter) ---")
    rect1 = Rectangle(length=10, width=5)
    rect1.display()

    print()
    rect2 = Rectangle(length=7.5, width=3.2)
    rect2.display()


if __name__ == "__main__":
    main()
