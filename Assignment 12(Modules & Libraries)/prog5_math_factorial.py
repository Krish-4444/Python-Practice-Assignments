"""
Program 5: Use math module to find factorial of a number.
"""

import math

def calculate_factorial(num: int):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(num)

def main():
    print("--- Program 5: Factorial Using math Module ---")
    
    # Demonstration with sample numbers
    test_numbers = [0, 1, 5, 7, 10]
    for n in test_numbers:
        print(f"Factorial of {n:2d} ({n}!) = {calculate_factorial(n)}")

if __name__ == "__main__":
    main()
