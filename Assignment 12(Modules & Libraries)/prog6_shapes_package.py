"""
Program 6: Create a package shapes with modules for circle and rectangle.
"""

from shapes import circle, rectangle

def main():
    print("--- Program 6: Shapes Package Demo ---")
    
    # Circle calculations
    r = 7.0
    print(f"Circle (radius = {r}):")
    print(f"  Area          : {circle.area(r):.2f}")
    print(f"  Circumference : {circle.circumference(r):.2f}")
    
    # Rectangle calculations
    l, w = 10.0, 5.0
    print(f"\nRectangle (length = {l}, width = {w}):")
    print(f"  Area          : {rectangle.area(l, w):.2f}")
    print(f"  Perimeter     : {rectangle.perimeter(l, w):.2f}")

if __name__ == "__main__":
    main()
