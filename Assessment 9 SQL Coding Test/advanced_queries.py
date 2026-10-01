import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "advanced_queries.db")

def print_results(title, records, headers):
    print("=" * 70, flush=True)
    print(title, flush=True)
    print("=" * 70, flush=True)

    if not headers:
        for row in records:
            print(row, flush=True)
        print("\n", flush=True)
        return

    header_str = " | ".join(f"{h:<22}" for h in headers)
    print(header_str, flush=True)
    print("-" * len(header_str), flush=True)

    for row in records:
        formatted_row = [f"{round(val, 2)}" if isinstance(val, float) else str(val) for val in row]
        print(" | ".join(f"{val:<22}" for val in formatted_row), flush=True)
    print("\n", flush=True)

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Clear existing tables for fresh execution
    cursor.execute("DROP TABLE IF EXISTS employees;")
    cursor.execute("DROP TABLE IF EXISTS project_a_employees;")
    cursor.execute("DROP TABLE IF EXISTS project_b_employees;")
    cursor.execute("DROP TABLE IF EXISTS logs;")
    cursor.execute("DROP TABLE IF EXISTS employee_duplicates;")

    # 1. Create employees table
    cursor.execute("""
        CREATE TABLE employees (
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name VARCHAR(50) NOT NULL,
            department VARCHAR(50) NOT NULL,
            salary INT NOT NULL,
            hire_date DATE NOT NULL
        )
    """)

    sample_employees = [
        (1, 'Alice', 'IT', 95000, '2025-02-10'),
        (2, 'Bob', 'IT', 85000, '2026-06-15'),      # Hired in last 6 months
        (3, 'Charlie', 'HR', 75000, '2025-11-20'),
        (4, 'David', 'Finance', 90000, '2026-07-01'), # Hired in last 6 months
        (5, 'Eve', 'HR', 65000, '2026-08-20'),       # Hired in last 6 months
        (6, 'Frank', 'Finance', 85000, '2025-01-05')
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", sample_employees)

    # 2. Create project_a and project_b tables for common records task
    cursor.execute("CREATE TABLE project_a_employees (emp_id INT, emp_name VARCHAR(50))")
    cursor.execute("CREATE TABLE project_b_employees (emp_id INT, emp_name VARCHAR(50))")

    cursor.executemany("INSERT INTO project_a_employees VALUES (?, ?)", [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')])
    cursor.executemany("INSERT INTO project_b_employees VALUES (?, ?)", [(2, 'Bob'), (3, 'Charlie'), (4, 'David')])

    # 3. Create logs table for continuous duplicate values task
    cursor.execute("CREATE TABLE logs (id INTEGER PRIMARY KEY AUTOINCREMENT, num INT)")
    sample_logs = [(1, 10), (2, 10), (3, 10), (4, 20), (5, 30), (6, 30), (7, 30), (8, 30), (9, 40)]
    cursor.executemany("INSERT INTO logs VALUES (?, ?)", sample_logs)

    # 4. Create employee_duplicates table for remove duplicates task
    cursor.execute("CREATE TABLE employee_duplicates (emp_id INT, emp_name VARCHAR(50), department VARCHAR(50))")
    sample_dups = [
        (1, 'Alice', 'IT'),
        (2, 'Alice', 'IT'), # Duplicate
        (3, 'Bob', 'HR'),
        (4, 'Bob', 'HR'),   # Duplicate
        (5, 'Charlie', 'Finance')
    ]
    cursor.executemany("INSERT INTO employee_duplicates VALUES (?, ?, ?)", sample_dups)

    conn.commit()

    # Task 1: Find Nth Highest Salary (e.g. N = 3)
    n = 3
    cursor.execute("""
        WITH RankedSalaries AS (
            SELECT emp_id, emp_name, salary,
                   DENSE_RANK() OVER (ORDER BY salary DESC) as rank
            FROM employees
        )
        SELECT emp_id, emp_name, salary, rank
        FROM RankedSalaries
        WHERE rank = ?
    """, (n,))
    print_results(f"1. FIND {n}RD HIGHEST SALARY (USING DENSE_RANK)", cursor.fetchall(), ["emp_id", "emp_name", "salary", "salary_rank"])

    # Task 2: Remove Duplicate Records
    cursor.execute("SELECT emp_id, emp_name, department FROM employee_duplicates")
    print_results("2A. BEFORE REMOVING DUPLICATE RECORDS", cursor.fetchall(), ["emp_id", "emp_name", "department"])

    cursor.execute("""
        DELETE FROM employee_duplicates
        WHERE emp_id NOT IN (
            SELECT MIN(emp_id)
            FROM employee_duplicates
            GROUP BY emp_name, department
        )
    """)
    conn.commit()

    cursor.execute("SELECT emp_id, emp_name, department FROM employee_duplicates")
    print_results("2B. AFTER REMOVING DUPLICATE RECORDS", cursor.fetchall(), ["emp_id", "emp_name", "department"])

    # Task 3: Find Records Common in Two Tables
    cursor.execute("""
        SELECT emp_id, emp_name FROM project_a_employees
        INTERSECT
        SELECT emp_id, emp_name FROM project_b_employees
    """)
    print_results("3. RECORDS COMMON IN TWO TABLES (PROJECT A & PROJECT B)", cursor.fetchall(), ["emp_id", "emp_name"])

    # Task 4: Find Employees Hired in Last 6 Months
    cursor.execute("""
        SELECT emp_id, emp_name, department, hire_date
        FROM employees
        WHERE hire_date >= date('2026-10-01', '-6 months')
        ORDER BY hire_date DESC
    """)
    print_results("4. EMPLOYEES HIRED IN LAST 6 MONTHS", cursor.fetchall(), ["emp_id", "emp_name", "department", "hire_date"])

    # Task 5: Find Continuous Duplicate Values (Appearing 3+ consecutive times)
    cursor.execute("""
        WITH ConsecutiveCheck AS (
            SELECT num,
                   LAG(num, 1) OVER (ORDER BY id) AS prev_num,
                   LEAD(num, 1) OVER (ORDER BY id) AS next_num
            FROM logs
        )
        SELECT DISTINCT num AS continuous_duplicate_value
        FROM ConsecutiveCheck
        WHERE num = prev_num AND num = next_num
    """)
    print_results("5. CONTINUOUS DUPLICATE VALUES (APPEARING 3+ CONSECUTIVE TIMES)", cursor.fetchall(), ["continuous_duplicate_value"])

    conn.close()

if __name__ == "__main__":
    main()
