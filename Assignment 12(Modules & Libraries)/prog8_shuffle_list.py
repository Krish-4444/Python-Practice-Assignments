"""
Program 8: Write a program to shuffle a list using random module.
"""

import random

def main():
    print("--- Program 8: Shuffle a List Using random Module ---")
    
    # Original list
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
    
    print("Original list:")
    print(fruits)
    
    # Make a copy so we can shuffle in-place
    shuffled_fruits = fruits.copy()
    random.shuffle(shuffled_fruits)
    
    print("\nShuffled list:")
    print(shuffled_fruits)
    
    # Another example with numbers
    numbers = list(range(1, 11))
    print(f"\nOriginal numbers: {numbers}")
    random.shuffle(numbers)
    print(f"Shuffled numbers: {numbers}")

if __name__ == "__main__":
    main()
