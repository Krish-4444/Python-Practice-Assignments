"""
Program 4: Write a program to demonstrate multiple exception blocks.
"""

def perform_operation(val1, val2, index):
    numbers = [10, 20, 30]
    
    try:
        num1 = float(val1)
        num2 = float(val2)
        division_result = num1 / num2
        element = numbers[index]
        print(f"Result: {num1} / {num2} = {division_result:.2f}, Element at index {index} = {element}")
    except ValueError:
        print("ValueError: Input values must be numbers!")
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero!")
    except IndexError:
        print(f"IndexError: Index {index} is out of bounds for list of size {len(numbers)}!")
    except Exception as e:
        print(f"General Error: An unexpected error occurred ({e})")


def main():
    print("--- Program 4: Multiple Exception Blocks ---")
    
    print("\nCase 1 (Success):")
    perform_operation("100", "5", 1)
    
    print("\nCase 2 (ValueError):")
    perform_operation("abc", "5", 1)
    
    print("\nCase 3 (ZeroDivisionError):")
    perform_operation("50", "0", 1)
    
    print("\nCase 4 (IndexError):")
    perform_operation("50", "2", 10)


if __name__ == "__main__":
    main()
