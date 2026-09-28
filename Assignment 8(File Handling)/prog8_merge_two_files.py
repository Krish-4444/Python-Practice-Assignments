"""
Program 8: Write a program to merge the contents of two text files into a third file.
"""

import os

def merge_files(file1_path, file2_path, merged_file_path):
    try:
        with open(file1_path, "r") as f1, open(file2_path, "r") as f2, open(merged_file_path, "w") as f_out:
            f_out.write(f"=== Content from {os.path.basename(file1_path)} ===\n")
            f_out.write(f1.read().strip() + "\n\n")
            
            f_out.write(f"=== Content from {os.path.basename(file2_path)} ===\n")
            f_out.write(f2.read().strip() + "\n")

        print(f"Successfully merged '{os.path.basename(file1_path)}' and '{os.path.basename(file2_path)}' into '{os.path.basename(merged_file_path)}'.")

    except FileNotFoundError as e:
        print(f"Error: One of the input files was not found! ({e})")


def display_file(filename):
    print(f"\n--- Content of '{os.path.basename(filename)}' ---")
    with open(filename, "r") as f:
        print(f.read())


def main():
    print("--- Program 8: Merge Two Text Files ---")
    
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, "part1.txt")
    file2 = os.path.join(dir_path, "part2.txt")
    merged_file = os.path.join(dir_path, "combined.txt")

    # Create dummy source files
    with open(file1, "w") as f:
        f.write("Header: Project Documentation Part 1\nSection 1: Introduction to Python.")
        
    with open(file2, "w") as f:
        f.write("Header: Project Documentation Part 2\nSection 2: Advanced OOP Features.")

    merge_files(file1, file2, merged_file)
    display_file(merged_file)


if __name__ == "__main__":
    main()
