"""
Program 7: Import multiple functions from one module and use them.
"""

# Importing multiple specific functions from the built-in 'math' module
from math import sqrt, pow, floor, ceil, gcd

def main():
    print("--- Program 7: Import Multiple Functions From One Module ---")
    
    num = 27.85
    base, exp = 4, 3
    a, b = 48, 18
    
    print(f"Square root of 64          (sqrt)  : {sqrt(64)}")
    print(f"{base} raised to power {exp}      (pow)   : {pow(base, exp)}")
    print(f"Floor of {num}             (floor) : {floor(num)}")
    print(f"Ceiling of {num}           (ceil)  : {ceil(num)}")
    print(f"GCD of {a} and {b}            (gcd)   : {gcd(a, b)}")

if __name__ == "__main__":
    main()
