"""
Program 7: Write a program to replace a specific word in a file and save changes.
"""

import os

def replace_word_in_file(filename, old_word, new_word):
    try:
        with open(filename, "r") as file:
            content = file.read()

        # Count occurrences before replacement
        occurrences = content.count(old_word)
        
        if occurrences == 0:
            print(f"Word '{old_word}' not found in '{os.path.basename(filename)}'.")
            return

        updated_content = content.replace(old_word, new_word)

        with open(filename, "w") as file:
            file.write(updated_content)

        print(f"Replaced '{old_word}' with '{new_word}' ({occurrences} occurrence(s) updated).")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


def display_file(filename, title):
    print(f"\n--- {title} ---")
    with open(filename, "r") as f:
        print(f.read().strip())


def main():
    print("--- Program 7: Replace Word in File ---")
    
    sample_file = os.path.join(os.path.dirname(__file__), "article.txt")
    
    initial_text = (
        "Java is a great language. Java is widely used in enterprise apps.\n"
        "Many developers love Java for backend programming."
    )
    
    with open(sample_file, "w") as f:
        f.write(initial_text)

    display_file(sample_file, "Original File Content")
    
    # Replace 'Java' with 'Python'
    replace_word_in_file(sample_file, old_word="Java", new_word="Python")
    
    display_file(sample_file, "Updated File Content")


if __name__ == "__main__":
    main()
