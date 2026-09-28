"""
Program 1: Write a program to read a file and display its contents.
"""

import os

def read_and_display(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"--- Contents of '{filename}' ---")
            print(content)
            print("-" * 35)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


def main():
    print("--- Program 1: Read File and Display Contents ---")
    
    sample_file = os.path.join(os.path.dirname(__file__), "sample_reading.txt")
    
    # Create sample file for demonstration
    with open(sample_file, "w") as f:
        f.write("Welcome to Python File Handling!\n")
        f.write("File handling allows you to read, write, and manipulate files.\n")
        f.write("Python provides easy-to-use built-in functions for file operations.\n")
    
    read_and_display(sample_file)


if __name__ == "__main__":
    main()
