"""
Program 7: Create a class with private attributes and getter/setter methods.
"""

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name                 # Public attribute
        self.__roll_number = roll_number # Private attribute
        self.__marks = marks             # Private attribute

    # Getter for roll_number
    def get_roll_number(self):
        return self.__roll_number

    # Setter for roll_number
    def set_roll_number(self, roll_number):
        if roll_number > 0:
            self.__roll_number = roll_number
        else:
            print("Error: Roll number must be a positive integer.")

    # Getter for marks
    def get_marks(self):
        return self.__marks

    # Setter for marks with validation
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Error: Marks must be between 0 and 100.")

    def display_details(self):
        print(f"Name: {self.name} | Roll No: {self.get_roll_number()} | Marks: {self.get_marks()}")


def main():
    print("--- Program 7: Private Attributes with Getter/Setter Methods ---")
    
    student = Student("John Doe", 101, 85)
    student.display_details()

    print("\nUpdating marks and roll number using setters:")
    student.set_marks(92)
    student.set_roll_number(105)
    student.display_details()

    print("\nAttempting invalid values:")
    student.set_marks(120)       # Invalid marks
    student.set_roll_number(-5)   # Invalid roll number
    student.display_details()


if __name__ == "__main__":
    main()
