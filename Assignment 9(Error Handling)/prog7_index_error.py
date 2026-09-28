"""
Program 7: Write a program to handle IndexError when accessing a list.
"""

def get_element_at(items, index):
    try:
        val = items[index]
        print(f"Element at index {index}: {val}")
        return val
    except IndexError as e:
        print(f"IndexError: Index {index} is out of range for list of size {len(items)}! ({e})")
        return None


def main():
    print("--- Program 7: Handling IndexError in Lists ---")
    fruits = ["Apple", "Banana", "Cherry", "Mango"]
    print(f"List: {fruits} (Length: {len(fruits)})")

    print("\nValid Index:")
    get_element_at(fruits, 2)

    print("\nInvalid Positive Index:")
    get_element_at(fruits, 5)

    print("\nInvalid Negative Index:")
    get_element_at(fruits, -10)


if __name__ == "__main__":
    main()
