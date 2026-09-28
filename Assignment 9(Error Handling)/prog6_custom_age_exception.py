"""
Program 6: Write a program to create a custom exception for invalid age (< 18).
"""

# Custom Exception Class
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be 18 or above to register."):
        self.age = age
        self.message = f"{message} (Provided age: {age})"
        super().__init__(self.message)


def register_voter(name, age):
    try:
        if age < 18:
            raise InvalidAgeError(age)
        print(f"Registration Successful! {name} (Age: {age}) is eligible to vote.")
    except InvalidAgeError as e:
        print(f"Registration Failed! Custom Exception Caught -> {e}")


def main():
    print("--- Program 6: Custom Exception for Invalid Age (< 18) ---")
    
    print("Test Case 1 (Valid Age):")
    register_voter("Alice", 21)
    
    print("\nTest Case 2 (Invalid Age):")
    register_voter("Bob", 15)


if __name__ == "__main__":
    main()
