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
            (101, 'Krish', 'CSE', 3, 88),
            (102, 'Jignesh', 'ECE', 2, 72),
            (103, 'Deep', 'CSE', 4, 95),
            (104, 'Devansh', 'MECH', 1, 64),
            (105, 'Harshil', 'CSE', 2, 81),
            (106, 'Yash', 'ECE', 3, 79),
            (107, 'Nain', 'CSE', 1, 90)
        ]
        cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", sample_students)
        conn.commit()
        print("Sample data inserted successfully!\n")

    def print_results(title, records, headers):
        print("=" * 60, flush=True)
        print(title, flush=True)
        print("=" * 60, flush=True)

        header_str = " | ".join(f"{h:<12}" for h in headers)
        print(header_str, flush=True)
        print("-" * len(header_str), flush=True)

        for row in records:
            print(" | ".join(f"{str(val):<12}" for val in row), flush=True)
        print("\n", flush=True)


    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print_results("1. ALL STUDENT RECORDS", records, ["student_id", "name", "department", "year", "marks"])


    cursor.execute("SELECT name, department FROM students")
    records = cursor.fetchall()
    print_results("2. NAME AND DEPARTMENT ONLY", records, ["name", "department"])


    cursor.execute("SELECT * FROM students WHERE marks > 75")
    records = cursor.fetchall()
    print_results("3. STUDENTS WITH MARKS > 75", records, ["student_id", "name", "department", "year", "marks"])

    cursor.execute("SELECT * FROM students WHERE department = 'CSE'")
    records = cursor.fetchall()
    print_results("4. STUDENTS FROM CSE DEPARTMENT", records, ["student_id", "name", "department", "year", "marks"])

    cursor.execute("SELECT * FROM students ORDER BY marks DESC")
    records = cursor.fetchall()
    print_results("5. STUDENTS SORTED BY MARKS (DESCENDING)", records, ["student_id", "name", "department", "year", "marks"])

    cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
    records = cursor.fetchall()
    print_results("6. TOP 3 SCORERS", records, ["student_id", "name", "department", "year", "marks"])

    conn.close()

if __name__ == "__main__":
    main()
