"""
Program 9: Function to find area of rectangle.
Formula: Area = length * width
"""

def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        return 0.0
    return length * width


def main():
    print("--- Program 9: Rectangle Area Calculator ---")
    dimensions = [(10, 5), (7.5, 3.2), (12, 12), (-4, 5)]
    for l, w in dimensions:
        area = rectangle_area(l, w)
        if area == 0.0 and (l <= 0 or w <= 0):
            print(f"Dimensions ({l}, {w}) -> Invalid dimensions!")
        else:
            print(f"Length: {l:<5} | Width: {w:<5} -> Area: {area:.2f}")


if __name__ == "__main__":
    main()
