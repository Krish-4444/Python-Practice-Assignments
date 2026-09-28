"""
Program 2: Write a program to count the number of lines in a file.
"""

import os

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            line_count = sum(1 for _ in file)
            print(f"Total lines in '{os.path.basename(filename)}': {line_count}")
            return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0


def main():
    print("--- Program 2: Count Lines in a File ---")
    
    sample_file = os.path.join(os.path.dirname(__file__), "sample_lines.txt")
    
    lines_content = [
        "Line 1: Python is awesome.\n",
        "Line 2: Object-Oriented Programming is powerful.\n",
        "Line 3: Exception Handling keeps code safe.\n",
        "Line 4: File Handling stores data persistently.\n",
        "Line 5: Practice makes perfect.\n"
    ]
    
    with open(sample_file, "w") as f:
        f.writelines(lines_content)
    
    count_lines(sample_file)


if __name__ == "__main__":
    main()
