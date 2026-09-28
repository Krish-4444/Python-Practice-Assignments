"""
Program 3: Write a program to open a file and handle the "file not found" error.
"""

def read_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(f"File '{file_path}' opened successfully. Content:")
            print(content)
    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found! ({e})")


def main():
    print("--- Program 3: File Not Found Exception Handling ---")
    
    print("Attempting to open non-existent file:")
    read_file_contents("non_existent_file.txt")
    
    print("\nAttempting to open existing file:")
    read_file_contents(__file__)  # Opens this Python script file itself


if __name__ == "__main__":
    main()
