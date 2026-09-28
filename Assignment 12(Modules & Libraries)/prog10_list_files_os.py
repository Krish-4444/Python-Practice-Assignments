"""
Program 10: Use os module to list files in a directory.
"""

import os

def list_files_in_directory(target_directory: str = "."):
    """Lists files and folders in the specified directory using the os module."""
    abs_path = os.path.abspath(target_directory)
    print(f"Directory: {abs_path}\n")
    
    try:
        entries = os.listdir(abs_path)
        
        files = []
        directories = []
        
        for entry in entries:
            full_path = os.path.join(abs_path, entry)
            if os.path.isdir(full_path):
                directories.append(entry)
            else:
                files.append(entry)
                
        print(f"Subdirectories ({len(directories)}):")
        for folder in directories:
            print(f"  [DIR]  {folder}")
            
        print(f"\nFiles ({len(files)}):")
        for file in files:
            size_bytes = os.path.getsize(os.path.join(abs_path, file))
            print(f"  [FILE] {file:<28} ({size_bytes} bytes)")
            
    except FileNotFoundError:
        print(f"Error: The directory '{target_directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{target_directory}'.")

def main():
    print("--- Program 10: List Files Using os Module ---")
    # List files in the current working directory
    list_files_in_directory(".")

if __name__ == "__main__":
    main()
