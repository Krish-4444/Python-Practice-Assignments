"""
Program 10: Write a program to back up a file by copying its contents into another file.
"""

import os
import shutil

def backup_file(source_file, backup_file_name=None):
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        return

    if backup_file_name is None:
        base, ext = os.path.splitext(source_file)
        backup_file_name = f"{base}_backup{ext}"

    try:
        shutil.copyfile(source_file, backup_file_name)
        print(f"Backup Successful!")
        print(f"  Source : '{os.path.basename(source_file)}'")
        print(f"  Backup : '{os.path.basename(backup_file_name)}'")
    except Exception as e:
        print(f"Error creating backup: {e}")


def main():
    print("--- Program 10: File Backup Utility ---")
    
    dir_path = os.path.dirname(__file__)
    source = os.path.join(dir_path, "important_data.txt")

    # Create dummy source file
    with open(source, "w") as f:
        f.write("Critical Configuration & Security Keys\nKey_ID=987654321\nStatus=Active\n")

    backup_file(source)

    backup_target = os.path.join(dir_path, "important_data_backup.txt")
    if os.path.exists(backup_target):
        print(f"\n--- Verifying Backup File Contents ---")
        with open(backup_target, "r") as f:
            print(f.read().strip())


if __name__ == "__main__":
    main()
