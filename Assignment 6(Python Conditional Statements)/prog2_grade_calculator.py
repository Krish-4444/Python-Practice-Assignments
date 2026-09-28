"""
Program 2: Grade calculator based on marks: 90+ = A, 80+ = B, else C.
"""

def calculate_grade(marks):
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    else:
        grade = "C"
    
    print(f"Marks: {marks:<5} -> Grade: {grade}")
    return grade


def main():
    print("--- Program 2: Grade Calculator ---")
    
    test_marks = [95, 88, 72, 90, 80, 55]
    for m in test_marks:
        calculate_grade(m)


if __name__ == "__main__":
    main()
