"""
Program 5: Write a program to append a list of strings to an existing file.
"""

import os

def append_strings_to_file(filename, lines_to_append):
    try:
        with open(filename, "a") as file:
            for line in lines_to_append:
                file.write(line + "\n")
        print(f"Appended {len(lines_to_append)} lines to '{os.path.basename(filename)}'.")
    except Exception as e:
        print(f"Error appending to file: {e}")


def display_file(filename):
    print(f"\n--- Current Contents of '{os.path.basename(filename)}' ---")
    with open(filename, "r") as f:
        print(f.read())


def main():
    print("--- Program 5: Append List of Strings to File ---")
    
    target_file = os.path.join(os.path.dirname(__file__), "log_history.txt")
    
    # Initialize file with initial content
    with open(target_file, "w") as f:
        f.write("Initial Log Entry 1: System initialized.\n")
        f.write("Initial Log Entry 2: User logged in.\n")
    
    print("Before Appending:")
    display_file(target_file)
    
    new_logs = [
        "Appended Log Entry 3: Data backup completed.",
        "Appended Log Entry 4: Security scan passed.",
        "Appended Log Entry 5: System shutdown cleanly."
    ]
    
    append_strings_to_file(target_file, new_logs)
    
    print("\nAfter Appending:")
    display_file(target_file)


if __name__ == "__main__":
    main()
