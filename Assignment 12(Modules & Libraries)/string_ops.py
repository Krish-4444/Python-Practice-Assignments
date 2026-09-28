"""
string_ops.py - Module to perform various string operations.
"""

def reverse_string(s: str) -> str:
    """Returns the reversed version of string s."""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Counts the number of vowels in string s."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    """Checks if the given string is a palindrome."""
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def count_words(s: str) -> int:
    """Counts the number of words in string s."""
    return len(s.split())

def to_title_case(s: str) -> str:
    """Converts the string into Title Case."""
    return s.title()
