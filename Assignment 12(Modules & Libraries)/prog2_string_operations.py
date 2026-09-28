"""
Program 2: Create a module to perform string operations and use it.
"""

import string_ops

def main():
    print("--- Program 2: String Operations Module Demo ---")
    sample_text = "madam Arora teaches Malayalam"
    word = "Radar"
    
    print(f"Sample Text: '{sample_text}'")
    print(f"Reversed: '{string_ops.reverse_string(sample_text)}'")
    print(f"Total Vowels: {string_ops.count_vowels(sample_text)}")
    print(f"Word Count: {string_ops.count_words(sample_text)}")
    print(f"Is '{word}' a Palindrome? {string_ops.is_palindrome(word)}")
    print(f"Title Case: '{string_ops.to_title_case('python programming language')}'")

if __name__ == "__main__":
    main()
