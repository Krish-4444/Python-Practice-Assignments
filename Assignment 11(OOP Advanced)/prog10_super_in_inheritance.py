"""
Program 10: Demonstrate the use of super() in inheritance.
"""

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Child Class
class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        # Using super() to call parent class's __init__ constructor
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display(self):
        # Using super() to call parent class's display method first
        super().display()
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")


def main():
    print("--- Program 10: Using super() in Inheritance ---")
    
    emp = Employee(name="Rahul Verma", age=29, employee_id="EMP-1042", department="Engineering")
    
    emp.display()


if __name__ == "__main__":
    main()
