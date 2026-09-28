"""
Program 6: Write a program to read a file and print only lines containing a specific word.
"""

import os

def filter_lines_by_keyword(filename, keyword):
    print(f"--- Lines containing the word '{keyword}' in '{os.path.basename(filename)}' ---")
    match_count = 0
    try:
        with open(filename, "r") as file:
            for line_no, line in enumerate(file, start=1):
                if keyword.lower() in line.lower():
                    print(f"Line {line_no}: {line.strip()}")
                    match_count += 1
        if match_count == 0:
            print(f"No lines found containing '{keyword}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


def main():
    print("--- Program 6: Filter Lines by Specific Word ---")
    
    sample_file = os.path.join(os.path.dirname(__file__), "tech_info.txt")
    
    content = [
        "Python is an interpreted, high-level programming language.\n",
        "Java is class-based and object-oriented.\n",
        "Python supports multiple programming paradigms.\n",
        "C++ provides low-level memory manipulation.\n",
        "Learning Python is fun and rewarding!\n"
    ]
    
    with open(sample_file, "w") as f:
        f.writelines(content)
    
    filter_lines_by_keyword(sample_file, "Python")


if __name__ == "__main__":
    main()
