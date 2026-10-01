import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "company.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            dept_id INT PRIMARY KEY,
            dept_name VARCHAR(50)
        )
    """)

    # Create employees table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT PRIMARY KEY,
            emp_name VARCHAR(50),
            dept_id INT,
            salary INT,
            FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        )
    """)

    # Insert sample data if empty
    cursor.execute("SELECT COUNT(*) FROM departments")
    if cursor.fetchone()[0] == 0:
        sample_departments = [
            (101, 'IT'),
            (102, 'HR'),
            (103, 'Finance'),
            (104, 'Marketing')
        ]
        cursor.executemany("INSERT INTO departments VALUES (?, ?)", sample_departments)

        sample_employees = [
            (1, 'Amit', 101, 60000),
            (2, 'Bob', 101, 55000),
            (3, 'Charlie', 101, 45000),
            (4, 'David', 102, 48000),
            (5, 'Eve', 102, 52000),
            (6, 'Frank', 103, 75000),
            (7, 'Grace', 103, 70000)
        ]
        cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", sample_employees)
        conn.commit()
        print("Sample data inserted successfully!\n", flush=True)

    def print_results(title, records, headers):
        print("=" * 60, flush=True)
        print(title, flush=True)
        print("=" * 60, flush=True)

        header_str = " | ".join(f"{h:<20}" for h in headers)
        print(header_str, flush=True)
        print("-" * len(header_str), flush=True)

        for row in records:
            formatted_row = [f"{round(val, 2)}" if isinstance(val, float) else ("NULL" if val is None else str(val)) for val in row]
            print(" | ".join(f"{val:<20}" for val in formatted_row), flush=True)
        print("\n", flush=True)

    # Task 1: Find employees earning more than average salary
    cursor.execute("""
        SELECT emp_id, emp_name, salary
        FROM employees
        WHERE salary > (SELECT AVG(salary) FROM employees)
    """)
    records = cursor.fetchall()
    print_results("1. EMPLOYEES EARNING MORE THAN AVERAGE SALARY", records, ["emp_id", "emp_name", "salary"])

    # Task 2: Find department with highest total salary
    cursor.execute("""
        SELECT d.dept_name, SUM(e.salary) AS total_salary
        FROM employees e
        JOIN departments d ON e.dept_id = d.dept_id
        GROUP BY d.dept_name
        ORDER BY total_salary DESC
        LIMIT 1
    """)
    records = cursor.fetchall()
    print_results("2. DEPARTMENT WITH HIGHEST TOTAL SALARY", records, ["dept_name", "total_salary"])

    # Task 3: Display employee with second highest salary
    cursor.execute("""
        SELECT emp_id, emp_name, salary
        FROM employees
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    """)
    records = cursor.fetchall()
    print_results("3. EMPLOYEE WITH SECOND HIGHEST SALARY", records, ["emp_id", "emp_name", "salary"])

    # Task 4: Display employees working in same department as "Amit"
    cursor.execute("""
        SELECT emp_id, emp_name, dept_id, salary
        FROM employees
        WHERE dept_id = (SELECT dept_id FROM employees WHERE emp_name = 'Amit')
          AND emp_name != 'Amit'
    """)
    records = cursor.fetchall()
    print_results("4. EMPLOYEES WORKING IN SAME DEPARTMENT AS 'AMIT'", records, ["emp_id", "emp_name", "dept_id", "salary"])

    conn.close()

if __name__ == "__main__":
    main()
