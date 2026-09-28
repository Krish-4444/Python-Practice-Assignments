"""
Program 6: Check if a number lies within a given range.
"""

def is_in_range(num, start_range, end_range):
    if start_range <= num <= end_range:
        print(f"Number {num} lies WITHIN the range [{start_range}, {end_range}].")
        return True
    else:
        print(f"Number {num} lies OUTSIDE the range [{start_range}, {end_range}].")
        return False


def main():
    print("--- Program 6: Check Number in Range ---")
    
    start, end = 10, 50
    
    test_nums = [25, 5, 50, 10, 60]
    for n in test_nums:
        is_in_range(n, start, end)


if __name__ == "__main__":
    main()
