"""
Program 7: Function to merge two lists.
"""

def merge_lists(list1, list2):
    # Combines list1 and list2
    return list1 + list2


def main():
    print("--- Program 7: Merge Two Lists ---")
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4]
    
    merged = merge_lists(fruits, numbers)
    print(f"List 1 : {fruits}")
    print(f"List 2 : {numbers}")
    print(f"Merged : {merged}")


if __name__ == "__main__":
    main()
