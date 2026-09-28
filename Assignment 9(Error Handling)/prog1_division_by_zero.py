"""
Program 1: Write a program to handle division by zero error.
"""

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"{numerator} / {denominator} = {result}")
        return result
    except ZeroDivisionError as e:
        print(f"Error: Division by zero is not allowed! ({e})")
        return None


def main():
    print("--- Program 1: Division by Zero Handling ---")
    
    print("Test Case 1 (Valid Division):")
    safe_divide(10, 2)
    
    print("\nTest Case 2 (Division by Zero):")
    safe_divide(10, 0)


if __name__ == "__main__":
    main()
