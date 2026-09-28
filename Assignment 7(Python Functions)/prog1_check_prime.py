"""
Program 1: Function to check if a number is prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    print("--- Program 1: Prime Number Checker ---")
    test_numbers = [1, 2, 7, 12, 19, 23, 29, 33, 97]
    for num in test_numbers:
        result = "Prime" if is_prime(num) else "Not Prime"
        print(f"Number {num:<4} -> {result}")


if __name__ == "__main__":
    main()
