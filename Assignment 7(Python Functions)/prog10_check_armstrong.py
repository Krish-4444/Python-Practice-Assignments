"""
Program 10: Function to check Armstrong number.
An Armstrong number (n-digit) is a number that is the sum of its own digits each raised to the power of n.
Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
"""

def is_armstrong(num):
    if num < 0:
        return False
    str_num = str(num)
    num_digits = len(str_num)
    sum_powers = sum(int(digit) ** num_digits for digit in str_num)
    return sum_powers == num


def main():
    print("--- Program 10: Armstrong Number Checker ---")
    test_numbers = [153, 370, 371, 407, 9474, 123, 5, 50]
    for n in test_numbers:
        result = "Armstrong Number" if is_armstrong(n) else "Not an Armstrong Number"
        print(f"Number: {n:<5} -> {result}")


if __name__ == "__main__":
    main()
