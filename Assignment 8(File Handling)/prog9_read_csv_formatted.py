"""
Program 9: Write a program to read a CSV file and display its content in a formatted way.
"""

import csv
import os

def read_and_format_csv(csv_filename):
    try:
        with open(csv_filename, mode="r", newline="") as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            
            print(f"--- Formatted View of '{os.path.basename(csv_filename)}' ---")
            header_str = f"{headers[0]:<10} {headers[1]:<20} {headers[2]:<15} {headers[3]:<10}"
            print(header_str)
            print("-" * len(header_str))

            for row in reader:
                if len(row) == 4:
                    print(f"{row[0]:<10} {row[1]:<20} {row[2]:<15} ${float(row[3]):<9.2f}")
            print("-" * len(header_str))
            
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_filename}' not found.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")


def main():
    print("--- Program 9: Formatted CSV File Reader ---")
    
    csv_file = os.path.join(os.path.dirname(__file__), "students.csv")

    # Create a sample CSV file
    sample_data = [
        ["ID", "Name", "Department", "Fee Paid"],
        ["101", "Krish", "Computer Sci", "25000"],
        ["102", "Jignesh", "Electrical Eng", "14500"],
        ["103", "Deep", "Mechanical Eng", "16000"],
        ["104", "Devansh", "Information Tech", "15500"]
    ]

    with open(csv_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)

    read_and_format_csv(csv_file)


if __name__ == "__main__":
    main()
