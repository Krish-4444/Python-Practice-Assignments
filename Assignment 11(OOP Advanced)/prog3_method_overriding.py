"""
Program 3: Implement method overriding in a base and derived class.
"""

# Base Class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    # Base implementation of calculate_pay
    def calculate_pay(self):
        return self.base_salary

    def show_details(self):
        print(f"Employee: {self.name}, Total Pay: ${self.calculate_pay()}")


# Derived Class
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    # Overriding calculate_pay to include bonus
    def calculate_pay(self):
        return self.base_salary + self.bonus


def main():
    print("--- Program 3: Method Overriding Demonstration ---")
    
    emp = Employee(name="John Doe", base_salary=50000)
    mgr = Manager(name="Jane Smith", base_salary=80000, bonus=15000)
    
    print("[Base Class Object]")
    emp.show_details()
    
    print("\n[Derived Class Object (Overridden calculate_pay)]")
    mgr.show_details()


if __name__ == "__main__":
    main()
