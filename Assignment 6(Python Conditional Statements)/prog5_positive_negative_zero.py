"""
Program 5: Check if a number is positive, negative, or zero.
"""

def check_number_status(num):
    if num > 0:
        status = "Positive"
    elif num < 0:
        status = "Negative"
    else:
        status = "Zero"
        
    print(f"Number: {num:<8} -> Status: {status}")
    return status


def main():
    print("--- Program 5: Positive, Negative, or Zero Check ---")
    
    test_numbers = [15, -7, 0, 3.14, -0.01]
    for n in test_numbers:
        check_number_status(n)


if __name__ == "__main__":
    main()
