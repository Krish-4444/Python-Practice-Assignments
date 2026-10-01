import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "students.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT PRIMARY KEY,
            name VARCHAR(50),
            department VARCHAR(30),
            year INT,
            marks INT
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        sample_students = [
            (101, 'Krish', 'CS', 3, 88),
            (102, 'Jignesh', 'CS', 2, 72),
            (103, 'Deep', 'IT', 4, 95),
            (104, 'Devansh', 'CS', 1, 64),
            (105, 'Harshil', 'IT', 2, 81),
            (106, 'Yash', 'IT', 3, 79)
        ]
        cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", sample_students)
        conn.commit()
        print("Sample data inserted successfully!\n")

    def print_results(title, records, headers):
        print("=" * 60, flush=True)
        print(title, flush=True)
        print("=" * 60, flush=True)

        header_str = " | ".join(f"{h:<20}" for h in headers)
        print(header_str, flush=True)
        print("-" * len(header_str), flush=True)

        for row in records:
            formatted_row = [f"{round(val, 2)}" if isinstance(val, float) else str(val) for val in row]
            print(" | ".join(f"{val:<20}" for val in formatted_row), flush=True)
        print("\n", flush=True)

    cursor.execute("SELECT COUNT(*) FROM students")
    records = cursor.fetchall()
    print_results("1. TOTAL NUMBER OF STUDENTS", records, ["total_students"])

    cursor.execute("SELECT AVG(marks) FROM students")
    records = cursor.fetchall()
    print_results("2. AVERAGE MARKS OF STUDENTS", records, ["average_marks"])

    cursor.execute("SELECT MAX(marks), MIN(marks) FROM students")
    records = cursor.fetchall()
    print_results("3. HIGHEST AND LOWEST MARKS", records, ["highest_marks", "lowest_marks"])

    cursor.execute("SELECT department, AVG(marks) FROM students GROUP BY department")
    records = cursor.fetchall()
    print_results("4. DEPARTMENT-WISE AVERAGE MARKS", records, ["department", "avg_marks"])

    cursor.execute("SELECT department, AVG(marks) FROM students GROUP BY department HAVING AVG(marks) > 70")
    records = cursor.fetchall()
    print_results("5. DEPARTMENTS WHERE AVERAGE MARKS > 70", records, ["department", "avg_marks"])

    conn.close()

if __name__ == "__main__":
    main()
