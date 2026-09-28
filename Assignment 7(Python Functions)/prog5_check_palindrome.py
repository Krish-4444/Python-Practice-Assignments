"""
Program 5: Function to check if a word is palindrome.
"""

def is_palindrome(word):
    clean_word = str(word).lower().replace(" ", "")
    return clean_word == clean_word[::-1]


def main():
    print("--- Program 5: Palindrome Checker ---")
    words = ["madam", "racecar", "python", "radar", "nurses run", "hello"]
    for w in words:
        result = "Palindrome" if is_palindrome(w) else "Not a Palindrome"
        print(f"Word: '{w}' -> {result}")


if __name__ == "__main__":
    main()
