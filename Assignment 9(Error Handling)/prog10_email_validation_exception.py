"""
Program 10: Write a program that validates an email format and raises an exception for invalid ones.
"""

import re

# Custom Exception for Invalid Email
class InvalidEmailError(Exception):
    def __init__(self, email, reason="Invalid email format"):
        self.email = email
        self.reason = reason
        super().__init__(f"Invalid Email '{email}': {reason}")


def validate_email(email):
    # Regex pattern for basic email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if not isinstance(email, str) or not email.strip():
        raise InvalidEmailError(email, "Email cannot be empty or non-string.")
    
    if not re.match(pattern, email):
        raise InvalidEmailError(email, "Does not match format 'user@domain.com'.")
    
    print(f"Valid Email: '{email}'")
    return True


def main():
    print("--- Program 10: Email Format Validation & Exception ---")
    
    test_emails = [
        "john.doe@example.com",
        "invalid-email.com",
        "user@domain",
        "hello@company.org",
        "@missinguser.com"
    ]
    
    for email in test_emails:
        try:
            validate_email(email)
        except InvalidEmailError as e:
            print(f"Validation Failed -> {e}")


if __name__ == "__main__":
    main()
