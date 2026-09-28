"""
Program 9: Simple calculator (add, subtract, multiply, divide).
"""

def simple_calculator(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print(f"{num1} {operator} {num2} -> Error: Division by zero!")
            return None
        result = num1 / num2
    else:
        print(f"Invalid operator '{operator}'. Supported: +, -, *, /")
        return None

    print(f"{num1} {operator} {num2} = {result:.2f}" if isinstance(result, float) else f"{num1} {operator} {num2} = {result}")
    return result


def main():
    print("--- Program 9: Simple Calculator ---")
    
    simple_calculator(10, "+", 5)
    simple_calculator(20, "-", 8)
    simple_calculator(6, "*", 7)
    simple_calculator(15, "/", 4)
    simple_calculator(10, "/", 0)


if __name__ == "__main__":
    main()
