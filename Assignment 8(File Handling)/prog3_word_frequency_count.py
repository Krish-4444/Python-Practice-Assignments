"""
Program 3: Write a program to count how many times each word appears in a file.
"""

import os
import re
from collections import Counter

def count_word_frequency(filename):
    try:
        with open(filename, "r") as file:
            content = file.read().lower()
            # Extract words ignoring punctuation
            words = re.findall(r"\b\w+\b", content)
            frequency = Counter(words)
            
            print(f"--- Word Frequency Count for '{os.path.basename(filename)}' ---")
            print(f"{'Word':<15} {'Frequency':<10}")
            print("-" * 25)
            for word, count in sorted(frequency.items(), key=lambda x: (-x[1], x[0])):
                print(f"{word:<15} {count:<10}")
            return frequency
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}


def main():
    print("--- Program 3: Word Frequency Counter ---")
    
    sample_file = os.path.join(os.path.dirname(__file__), "sample_words.txt")
    
    text = "Python is great. Python is fast and Python is easy to learn!"
    with open(sample_file, "w") as f:
        f.write(text)
    
    print(f"Sample Text: \"{text}\"\n")
    count_word_frequency(sample_file)


if __name__ == "__main__":
    main()
