"""
Program 10: Check type of triangle (equilateral, isosceles, scalene).
"""

def check_triangle_type(a, b, c):
    print(f"Sides: a={a}, b={b}, c={c}")
    
    # Triangle Inequality Theorem Check
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("  Result: Not a valid triangle (Sides fail triangle inequality theorem).")
        return "Invalid"

    if a == b == c:
        triangle_type = "Equilateral Triangle (All sides equal)"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles Triangle (Two sides equal)"
    else:
        triangle_type = "Scalene Triangle (All sides different)"

    print(f"  Result: {triangle_type}")
    return triangle_type


def main():
    print("--- Program 10: Triangle Type Checker ---")
    
    print("\nTest Case 1:")
    check_triangle_type(5, 5, 5)

    print("\nTest Case 2:")
    check_triangle_type(5, 5, 8)

    print("\nTest Case 3:")
    check_triangle_type(3, 4, 5)

    print("\nTest Case 4:")
    check_triangle_type(1, 2, 10)


if __name__ == "__main__":
    main()
