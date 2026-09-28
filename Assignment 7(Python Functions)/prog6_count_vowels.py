"""
Program 6: Function to count vowels in a string.
"""

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count


def main():
    print("--- Program 6: Vowel Counter ---")
    sentences = [
        "Hello World",
        "Python Programming is Easy",
        "AEIOU",
        "Rhythm",
        "Artificial Intelligence"
    ]
    
    for s in sentences:
        v_count = count_vowels(s)
        print(f"Text: '{s}' -> Vowels Count: {v_count}")


if __name__ == "__main__":
    main()
