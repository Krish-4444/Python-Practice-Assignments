"""
Program 9: Write a program to log errors to a file instead of printing them.
"""

import logging
import os

# Configure logging to write errors to error_log.log file
log_filename = os.path.join(os.path.dirname(__file__), "app_errors.log")

logging.basicConfig(
    filename=log_filename,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result of {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        # Log error to file with traceback details
        logging.error("Division by zero error occurred", exc_info=True)
        print("An error occurred. Check 'app_errors.log' for details.")
    except TypeError as e:
        logging.error(f"Type error: {e}", exc_info=True)
        print("An error occurred. Check 'app_errors.log' for details.")


def main():
    print("--- Program 9: Logging Errors to a File ---")
    
    print("Executing operations (errors will be logged to file)...")
    divide_numbers(10, 2)   # Success
    divide_numbers(10, 0)   # Logs ZeroDivisionError
    divide_numbers("10", 2) # Logs TypeError

    if os.path.exists(log_filename):
        print(f"\n[Log File Created]: {log_filename}")
        print("--- Log File Contents ---")
        with open(log_filename, "r") as f:
            print(f.read().strip())


if __name__ == "__main__":
    main()
