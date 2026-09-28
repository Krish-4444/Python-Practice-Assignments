"""
Program 5: Write a program to use finally for resource cleanup.
"""

import os

def process_file(filename):
    file = None
    try:
        print(f"Opening file '{filename}'...")
        file = open(filename, "r")
        content = file.read()
        print("File read successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error while reading file: {e}")
    finally:
        print("Executing 'finally' block for resource cleanup...")
        if file and not file.closed:
            file.close()
            print("Resource cleanup: File closed successfully.")
        else:
            print("Resource cleanup: No active file handle to close.")


def main():
    print("--- Program 5: Using finally for Resource Cleanup ---")
    
    # Create a dummy temporary file for demo
    dummy_file = "sample_test.txt"
    with open(dummy_file, "w") as f:
        f.write("Hello, World! Sample content for testing cleanup.")
    
    print("Test 1 (File exists):")
    process_file(dummy_file)
    
    print("\nTest 2 (File does NOT exist):")
    process_file("missing_file.txt")
    
    # Clean up dummy file
    if os.path.exists(dummy_file):
        os.remove(dummy_file)


if __name__ == "__main__":
    main()
