"""
Program 8: Write a program that takes two numbers and handles all possible errors.
"""

def compute_numbers(input_a, input_b):
    print(f"Inputs: a = '{input_a}', b = '{input_b}'")
    try:
        a = float(input_a)
        b = float(input_b)
        
        sum_val = a + b
        diff_val = a - b
        prod_val = a * b
        div_val = a / b
        
        print(f"  Addition       : {sum_val}")
        print(f"  Subtraction    : {diff_val}")
        print(f"  Multiplication : {prod_val}")
        print(f"  Division       : {div_val:.2f}")

    except ValueError:
        print("  Error [ValueError]: One or both inputs are not valid numbers!")
    except ZeroDivisionError:
        print("  Error [ZeroDivisionError]: Cannot divide by zero!")
    except TypeError:
        print("  Error [TypeError]: Unsupported operand types provided!")
    except Exception as e:
        print(f"  Error [{type(e).__name__}]: An unexpected error occurred ({e})")


def main():
    print("--- Program 8: Handle All Errors for Two Numbers ---")
    
    print("\nCase 1 (Valid Input):")
    compute_numbers(20, 4)

    print("\nCase 2 (Invalid Number Format):")
    compute_numbers("ten", 5)

    print("\nCase 3 (Division by Zero):")
    compute_numbers(15, 0)

    print("\nCase 4 (None / Invalid Types):")
    compute_numbers(None, 5)


if __name__ == "__main__":
    main()
