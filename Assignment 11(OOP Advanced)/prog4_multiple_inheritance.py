"""
Program 4: Demonstrate multiple inheritance with two parent classes.
"""

# First Parent Class
class Camera:
    def take_photo(self):
        print("Camera: Capturing high-resolution photo...")


# Second Parent Class
class Phone:
    def make_call(self, number):
        print(f"Phone: Calling {number}...")


# Child Class inheriting from both Camera and Phone
class SmartPhone(Camera, Phone):
    def __init__(self, model):
        self.model = model

    def browse_internet(self):
        print(f"{self.model}: Browsing the web...")


def main():
    print("--- Program 4: Multiple Inheritance Demo ---")
    
    my_phone = SmartPhone("iPhone 15")
    
    # Method from first parent (Camera)
    my_phone.take_photo()
    
    # Method from second parent (Phone)
    my_phone.make_call("+1-800-555-0199")
    
    # Method from child class (SmartPhone)
    my_phone.browse_internet()


if __name__ == "__main__":
    main()
