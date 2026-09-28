"""
Program 8: Function to find GCD of two numbers.
"""

def find_gcd(a, b):
    # Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    return abs(a)


def main():
    print("--- Program 8: Greatest Common Divisor (GCD) ---")
    pairs = [(48, 18), (56, 98), (101, 10), (12, 60), (17, 13)]
    for num1, num2 in pairs:
        gcd_val = find_gcd(num1, num2)
        print(f"GCD of ({num1}, {num2}) = {gcd_val}")


if __name__ == "__main__":
    main()
