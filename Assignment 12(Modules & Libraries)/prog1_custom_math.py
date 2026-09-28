"""
Program 1: Create a custom math module and import it in another file.
"""

import my_math

def main():
    print("--- Program 1: Custom Math Module Demo ---")
    x, y = 15, 5
    
    print(f"Numbers: x = {x}, y = {y}")
    print(f"Addition ({x} + {y})       : {my_math.add(x, y)}")
    print(f"Subtraction ({x} - {y})    : {my_math.subtract(x, y)}")
    print(f"Multiplication ({x} * {y}) : {my_math.multiply(x, y)}")
    print(f"Division ({x} / {y})       : {my_math.divide(x, y)}")
    print(f"Power ({x} ** 2)          : {my_math.power(x, 2)}")

if __name__ == "__main__":
    main()
