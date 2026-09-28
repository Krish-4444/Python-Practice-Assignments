"""
Program 3: Use random module to generate 5 random integers.
"""

import random

def main():
    print("--- Program 3: Generate 5 Random Integers ---")
    
    # Range: 1 to 100 (inclusive)
    random_integers = [random.randint(1, 100) for _ in range(5)]
    
    print("5 Random Integers (between 1 and 100):")
    for idx, num in enumerate(random_integers, start=1):
        print(f"Number {idx}: {num}")
    
    print(f"\nAll generated numbers as list: {random_integers}")

if __name__ == "__main__":
    main()
