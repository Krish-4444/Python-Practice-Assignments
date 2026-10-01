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

    # Insert sample data if tables are empty
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
            (1, 'Alice', 101, 60000),
            (2, 'Bob', 101, 55000),
            (3, 'Charlie', 101, 45000),
            (4, 'David', 102, 48000),
            (5, 'Eve', 102, 52000),
            (6, 'Frank', 103, 70000),
            (7, 'Grace', None, 53000)
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

    # Task 1: Display employee name with department name
    cursor.execute("""
        SELECT e.emp_name, d.dept_name
        FROM employees e
        JOIN departments d ON e.dept_id = d.dept_id
    """)
    records = cursor.fetchall()
    print_results("1. EMPLOYEE NAME WITH DEPARTMENT NAME", records, ["emp_name", "dept_name"])

    # Task 2: Display employees earning more than 50,000
    cursor.execute("""
        SELECT emp_id, emp_name, salary
        FROM employees
        WHERE salary > 50000
    """)
    records = cursor.fetchall()
    print_results("2. EMPLOYEES EARNING MORE THAN 50,000", records, ["emp_id", "emp_name", "salary"])

    # Task 3: Display department-wise total salary
    cursor.execute("""
        SELECT d.dept_name, SUM(e.salary) AS total_salary
        FROM employees e
        JOIN departments d ON e.dept_id = d.dept_id
        GROUP BY d.dept_name
    """)
    records = cursor.fetchall()
    print_results("3. DEPARTMENT-WISE TOTAL SALARY", records, ["dept_name", "total_salary"])

    # Task 4: Display departments with more than 2 employees
    cursor.execute("""
        SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
        FROM departments d
        JOIN employees e ON d.dept_id = e.dept_id
        GROUP BY d.dept_name
        HAVING COUNT(e.emp_id) > 2
    """)
    records = cursor.fetchall()
    print_results("4. DEPARTMENTS WITH MORE THAN 2 EMPLOYEES", records, ["dept_name", "total_employees"])

    # Task 5: Display employees without a department
    cursor.execute("""
        SELECT emp_id, emp_name, salary
        FROM employees
        WHERE dept_id IS NULL
    """)
    records = cursor.fetchall()
    print_results("5. EMPLOYEES WITHOUT A DEPARTMENT", records, ["emp_id", "emp_name", "salary"])

    conn.close()

if __name__ == "__main__":
    main()
