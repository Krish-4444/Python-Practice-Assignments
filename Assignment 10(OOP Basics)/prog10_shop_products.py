"""
Program 10: Create a Shop class with a method to add and list products.
"""

class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = {}  # Dictionary to store product: price

    def add_product(self, product_name, price):
        if price > 0:
            self.products[product_name] = price
            print(f"Added '{product_name}' priced at ${price:.2f} to {self.shop_name}.")
        else:
            print("Product price must be greater than 0.")

    def list_products(self):
        print(f"\n--- {self.shop_name} Product Catalog ---")
        if not self.products:
            print("No products available in the shop.")
            return

        print(f"{'No.':<4} {'Product Name':<20} {'Price':<10}")
        print("-" * 36)
        for idx, (product, price) in enumerate(self.products.items(), start=1):
            print(f"{idx:<4} {product:<20} ${price:<9.2f}")
        print("-" * 36)


def main():
    print("--- Program 10: Shop Class Demo ---")
    my_shop = Shop("Tech Zone")

    my_shop.add_product("Wireless Mouse", 25.50)
    my_shop.add_product("Mechanical Keyboard", 79.99)
    my_shop.add_product("USB-C Hub", 35.00)
    my_shop.add_product("Gaming Headset", 59.99)

    my_shop.list_products()


if __name__ == "__main__":
    main()
