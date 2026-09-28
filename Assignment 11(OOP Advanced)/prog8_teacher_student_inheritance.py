"""
Program 8: Create a Teacher and Student class to show inheritance.
"""

# Base Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I am {self.age} years old.")


# Teacher Subclass inheriting from Person
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def teach(self):
        print(f"Teacher {self.name} is teaching {self.subject}.")


# Student Subclass inheriting from Person
class Student(Person):
    def __init__(self, name, age, grade, student_id):
        super().__init__(name, age)
        self.grade = grade
        self.student_id = student_id

    def study(self):
        print(f"Student {self.name} (ID: {self.student_id}) is studying in Grade {self.grade}.")


def main():
    print("--- Program 8: Teacher and Student Inheritance ---")
    
    teacher = Teacher(name="Mr. Sharma", age=42, subject="Computer Science", salary=65000)
    student = Student(name="Aman", age=16, grade="10th", student_id="STU2024")
    
    print("[Teacher Details]")
    teacher.introduce()
    teacher.teach()
    
    print("\n[Student Details]")
    student.introduce()
    student.study()


if __name__ == "__main__":
    main()
