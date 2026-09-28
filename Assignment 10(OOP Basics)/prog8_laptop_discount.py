"""
Program 8: Create a Laptop class with a method to apply discounts on price.
"""

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_percent):
        if 0 < discount_percent < 100:
            discount_amount = (self.price * discount_percent) / 100
            discounted_price = self.price - discount_amount
            print(f"Original Price : ${self.price:.2f}")
            print(f"Discount ({discount_percent}%) : -${discount_amount:.2f}")
            print(f"Final Price    : ${discounted_price:.2f}")
            return discounted_price
        else:
            print("Invalid discount percentage. Must be between 0 and 100.")
            return self.price

    def display_info(self):
        print(f"Laptop: {self.brand} {self.model} | Retail Price: ${self.price:.2f}")


def main():
    print("--- Program 8: Laptop Class with Discount Method ---")
    laptop1 = Laptop(brand="Dell", model="XPS 15", price=1500.00)
    laptop1.display_info()
    laptop1.apply_discount(15)

    print()
    laptop2 = Laptop(brand="Apple", model="MacBook Pro M3", price=2000.00)
    laptop2.display_info()
    laptop2.apply_discount(10)


if __name__ == "__main__":
    main()
