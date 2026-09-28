"""
run_all.py - Convenient runner to run any or all 10 programs
"""

import subprocess
import sys

PROGRAMS = {
    "1": ("Custom Math Module", "prog1_custom_math.py"),
    "2": ("String Operations Module", "prog2_string_operations.py"),
    "3": ("Generate 5 Random Integers", "prog3_random_integers.py"),
    "4": ("Current Date and Time", "prog4_current_datetime.py"),
    "5": ("Factorial Using Math Module", "prog5_math_factorial.py"),
    "6": ("Shapes Package (Circle & Rectangle)", "prog6_shapes_package.py"),
    "7": ("Import Multiple Functions", "prog7_import_multiple.py"),
    "8": ("Shuffle List Using Random", "prog8_shuffle_list.py"),
    "9": ("Difference Between Two Dates", "prog9_date_difference.py"),
    "10": ("List Files Using os Module", "prog10_list_files_os.py"),
}

def run_program(script_name):
    print(f"\n{'='*55}\nRunning: {script_name}\n{'='*55}")
    subprocess.run([sys.executable, script_name])

def main():
    while True:
        print("\n" + "="*45)
        print("          ASSIGNMENT 5 - PYTHON PROGRAMS")
        print("="*45)
        for num, (desc, file) in PROGRAMS.items():
            print(f" {num:>2}. {desc:<35} ({file})")
        print("  A. Run ALL programs")
        print("  Q. Quit")
        print("="*45)
        
        choice = input("Enter your choice (1-10 / A / Q): ").strip().lower()
        if choice == 'q':
            print("Exiting. Happy coding!")
            break
        elif choice == 'a':
            for num in sorted(PROGRAMS.keys(), key=int):
                run_program(PROGRAMS[num][1])
        elif choice in PROGRAMS:
            run_program(PROGRAMS[choice][1])
        else:
            print("Invalid selection! Please enter a number between 1 and 10, 'A', or 'Q'.")

if __name__ == "__main__":
    main()
