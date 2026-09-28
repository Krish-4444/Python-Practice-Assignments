"""
Program 2: Function to reverse a string.
"""

def reverse_string(s):
    return s[::-1]


def main():
    print("--- Program 2: Reverse a String ---")
    words = ["Python", "Hello World", "OpenAI", "12345", "racecar"]
    for w in words:
        rev = reverse_string(w)
        print(f"Original: '{w}' -> Reversed: '{rev}'")


if __name__ == "__main__":
    main()
