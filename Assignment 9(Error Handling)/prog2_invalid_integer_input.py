"""
Program 2: Write a program to handle invalid integer input.
"""

def parse_integer(user_input):
    try:
        value = int(user_input)
        print(f"Successfully converted '{user_input}' to integer: {value}")
        return value
    except ValueError as e:
        print(f"Error: '{user_input}' is not a valid integer! ({e})")
        return None


def main():
    print("--- Program 2: Invalid Integer Input Handling ---")
    
    test_inputs = ["42", "hello", "3.14", "-100", "abc123"]
    for inp in test_inputs:
        parse_integer(inp)


if __name__ == "__main__":
    main()
