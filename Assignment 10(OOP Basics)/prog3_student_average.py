"""
Program 3: Create a Student class with a method to calculate average marks.
"""

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # list of marks

    def calculate_average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def display_report(self):
        avg = self.calculate_average()
        print(f"Student: {self.name} (Roll No: {self.roll_number})")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {avg:.2f}")


def main():
    print("--- Program 3: Student Class with Average Marks ---")
    s1 = Student("John Doe", 101, [85, 90, 78, 92, 88])
    s1.display_report()

    print()
    s2 = Student("Emma Watson", 102, [95, 98, 92, 94, 96])
    s2.display_report()


if __name__ == "__main__":
    main()
