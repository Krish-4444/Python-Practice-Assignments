"""
Program 6: Create a Book class to store title, author, and price, and display details.
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Price  : ${self.price:.2f}")
        print("-" * 30)


def main():
    print("--- Program 6: Book Details ---")
    book1 = Book(title="Atomic Habits", author="James Clear", price=19.99)
    book2 = Book(title="Clean Code", author="Robert C. Martin", price=34.50)
    book3 = Book(title="The Pragmatic Programmer", author="Andy Hunt & Dave Thomas", price=42.00)

    book1.display_details()
    book2.display_details()
    book3.display_details()


if __name__ == "__main__":
    main()
