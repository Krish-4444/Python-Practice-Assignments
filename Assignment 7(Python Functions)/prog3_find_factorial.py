"""
Program 3: Function to find factorial.
"""

def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact


def main():
    print("--- Program 3: Factorial Calculator ---")
    numbers = [0, 1, 5, 7, 10, -3]
    for num in numbers:
        res = factorial(num)
        if res is None:
            print(f"Factorial of {num} is undefined (Negative input).")
        else:
            print(f"Factorial of {num:<2} = {res}")


if __name__ == "__main__":
    main()
