"""
Program 5: Create an Employee class that displays salary details.
"""

class Employee:
    def __init__(self, emp_id, name, department, basic_pay, hra, allowance):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.basic_pay = basic_pay
        self.hra = hra
        self.allowance = allowance

    def calculate_total_salary(self):
        return self.basic_pay + self.hra + self.allowance

    def display_salary_details(self):
        total = self.calculate_total_salary()
        print(f"--- Employee Salary Slip ---")
        print(f"ID         : {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Department : {self.department}")
        print(f"Basic Pay  : ${self.basic_pay:.2f}")
        print(f"HRA        : ${self.hra:.2f}")
        print(f"Allowance  : ${self.allowance:.2f}")
        print(f"Total Pay  : ${total:.2f}")
        print("-" * 28)


def main():
    print("--- Program 5: Employee Salary Details ---")
    emp1 = Employee("EMP101", "David Miller", "Engineering", basic_pay=50000, hra=15000, allowance=5000)
    emp1.display_salary_details()

    emp2 = Employee("EMP102", "Sarah Jenkins", "Marketing", basic_pay=45000, hra=12000, allowance=4000)
    emp2.display_salary_details()


if __name__ == "__main__":
    main()
