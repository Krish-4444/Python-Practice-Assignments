import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "mess_management.db")

def print_results(title, records, headers):
    print("=" * 75, flush=True)
    print(title, flush=True)
    print("=" * 75, flush=True)

    if not records:
        print("No records found.\n", flush=True)
        return

    header_str = " | ".join(f"{h:<20}" for h in headers)
    print(header_str, flush=True)
    print("-" * len(header_str), flush=True)

    for row in records:
        formatted_row = [f"{round(val, 2)}" if isinstance(val, float) else str(val) for val in row]
        print(" | ".join(f"{val:<20}" for val in formatted_row), flush=True)
    print("\n", flush=True)

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    # Drop existing tables for fresh execution
    cursor.execute("DROP TABLE IF EXISTS meal_logs;")
    cursor.execute("DROP TABLE IF EXISTS payments;")
    cursor.execute("DROP TABLE IF EXISTS mess_expenses;")
    cursor.execute("DROP TABLE IF EXISTS menu;")
    cursor.execute("DROP TABLE IF EXISTS members;")
    cursor.execute("DROP VIEW IF EXISTS monthly_mess_financial_summary;")

    # 1. Create Schema & Relationships
    cursor.execute("""
        CREATE TABLE members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            hostel_block VARCHAR(10) NOT NULL,
            room_no INT NOT NULL,
            mess_plan VARCHAR(20) NOT NULL,
            joining_date DATE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE menu (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name VARCHAR(50) NOT NULL,
            category VARCHAR(20) NOT NULL,
            cost_per_serving REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE meal_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            meal_type VARCHAR(20) NOT NULL,
            log_date DATE NOT NULL,
            status VARCHAR(15) NOT NULL,
            FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            month VARCHAR(10) NOT NULL,
            amount_paid REAL NOT NULL,
            payment_date DATE NOT NULL,
            payment_status VARCHAR(15) NOT NULL,
            FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE mess_expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category VARCHAR(50) NOT NULL,
            amount REAL NOT NULL,
            expense_date DATE NOT NULL
        )
    """)

    # Populate Sample Data
    members_data = [
        (1, 'Krish Patel', 'Block A', 101, 'Full Month', '2026-01-01'),
        (2, 'Amit Sharma', 'Block A', 102, 'Full Month', '2026-01-01'),
        (3, 'Priya Singh', 'Block B', 201, 'Per Meal', '2026-01-05'),
        (4, 'Rohan Verma', 'Block B', 202, 'Full Month', '2026-01-10'),
        (5, 'Siddharth Rao', 'Block C', 301, 'Per Meal', '2026-02-01')
    ]
    cursor.executemany("INSERT INTO members VALUES (?, ?, ?, ?, ?, ?)", members_data)

    menu_data = [
        (1, 'Poha & Tea', 'Breakfast', 30.0),
        (2, 'Aloo Paratha', 'Breakfast', 40.0),
        (3, 'Thali (Roti, Dal, Rice, Sabzi)', 'Lunch', 80.0),
        (4, 'Special Paneer Thali', 'Dinner', 100.0),
        (5, 'Samosa & Coffee', 'Snacks', 25.0)
    ]
    cursor.executemany("INSERT INTO menu VALUES (?, ?, ?, ?)", menu_data)

    meal_logs_data = [
        # Date: 2026-09-01
        (1, 1, 'Breakfast', '2026-09-01', 'Eaten'),
        (2, 1, 'Lunch', '2026-09-01', 'Eaten'),
        (3, 1, 'Dinner', '2026-09-01', 'Eaten'),
        (4, 2, 'Breakfast', '2026-09-01', 'Eaten'),
        (5, 2, 'Lunch', '2026-09-01', 'Skipped'),
        (6, 2, 'Dinner', '2026-09-01', 'Eaten'),
        (7, 3, 'Breakfast', '2026-09-01', 'Skipped'),
        (8, 3, 'Lunch', '2026-09-01', 'Guest Meal'),
        (9, 3, 'Dinner', '2026-09-01', 'Eaten'),
        # Date: 2026-09-02
        (10, 1, 'Breakfast', '2026-09-02', 'Eaten'),
        (11, 1, 'Lunch', '2026-09-02', 'Eaten'),
        (12, 1, 'Dinner', '2026-09-02', 'Skipped'),
        (13, 4, 'Breakfast', '2026-09-02', 'Eaten'),
        (14, 4, 'Lunch', '2026-09-02', 'Eaten'),
        (15, 4, 'Dinner', '2026-09-02', 'Eaten'),
        (16, 5, 'Lunch', '2026-09-02', 'Skipped'),
        (17, 5, 'Dinner', '2026-09-02', 'Skipped')
    ]
    cursor.executemany("INSERT INTO meal_logs VALUES (?, ?, ?, ?, ?)", meal_logs_data)

    payments_data = [
        (1, 1, '2026-08', 3500.0, '2026-09-01', 'Paid'),
        (2, 2, '2026-08', 3500.0, '2026-09-02', 'Paid'),
        (3, 3, '2026-08', 1200.0, '2026-09-03', 'Paid'),
        (4, 4, '2026-08', 3500.0, '2026-09-05', 'Pending'),
        (5, 5, '2026-08', 1500.0, '2026-09-10', 'Overdue')
    ]
    cursor.executemany("INSERT INTO payments VALUES (?, ?, ?, ?, ?, ?)", payments_data)

    expenses_data = [
        (1, 'Groceries & Vegetables', 4500.0, '2026-09-01'),
        (2, 'LPG Cylinder Refill', 1800.0, '2026-09-03'),
        (3, 'Cook & Staff Salary', 8000.0, '2026-09-05'),
        (4, 'Dairy Products (Milk/Curd)', 2200.0, '2026-09-07')
    ]
    cursor.executemany("INSERT INTO mess_expenses VALUES (?, ?, ?, ?)", expenses_data)
    conn.commit()

    print(">>> MESS MANAGEMENT SYSTEM DATABASE CREATED WITH SAMPLE DATA <<<\n", flush=True)

    # ==========================================
    # 15 BUSINESS QUERIES FOR MESS SYSTEM
    # ==========================================

    # Query 1: All registered mess members
    cursor.execute("SELECT member_id, name, hostel_block, room_no, mess_plan FROM members")
    print_results("QUERY 1: ALL REGISTERED MESS MEMBERS", cursor.fetchall(), ["member_id", "name", "hostel_block", "room_no", "mess_plan"])

    # Query 2: Attendance count per member
    cursor.execute("""
        SELECT m.member_id, m.name, COUNT(l.log_id) AS total_eaten_meals
        FROM members m
        JOIN meal_logs l ON m.member_id = l.member_id
        WHERE l.status = 'Eaten'
        GROUP BY m.member_id, m.name
    """)
    print_results("QUERY 2: TOTAL EATEN MEALS PER MEMBER", cursor.fetchall(), ["member_id", "name", "total_eaten_meals"])

    # Query 3: Revenue by Payment Status
    cursor.execute("""
        SELECT payment_status, COUNT(payment_id) AS count, SUM(amount_paid) AS total_amount
        FROM payments
        GROUP BY payment_status
    """)
    print_results("QUERY 3: REVENUE BREAKDOWN BY PAYMENT STATUS", cursor.fetchall(), ["payment_status", "count", "total_amount"])

    # Query 4: Most skipped meal types
    cursor.execute("""
        SELECT meal_type, COUNT(*) AS skipped_count
        FROM meal_logs
        WHERE status = 'Skipped'
        GROUP BY meal_type
        ORDER BY skipped_count DESC
    """)
    print_results("QUERY 4: MOST SKIPPED MEAL TYPES", cursor.fetchall(), ["meal_type", "skipped_count"])

    # Query 5: Monthly Financial Summary (Collections vs Expenses)
    cursor.execute("""
        SELECT 
            (SELECT SUM(amount_paid) FROM payments WHERE payment_status = 'Paid') AS total_collections,
            (SELECT SUM(amount) FROM mess_expenses) AS total_expenses,
            ((SELECT SUM(amount_paid) FROM payments WHERE payment_status = 'Paid') - (SELECT SUM(amount) FROM mess_expenses)) AS net_balance
    """)
    print_results("QUERY 5: MONTHLY FINANCIAL SUMMARY", cursor.fetchall(), ["total_collections", "total_expenses", "net_balance"])

    # Query 6: Members with Pending / Overdue Payments
    cursor.execute("""
        SELECT m.name, m.hostel_block, p.month, p.amount_paid, p.payment_status
        FROM members m
        JOIN payments p ON m.member_id = p.member_id
        WHERE p.payment_status IN ('Pending', 'Overdue')
    """)
    print_results("QUERY 6: MEMBERS WITH PENDING / OVERDUE PAYMENTS", cursor.fetchall(), ["name", "hostel_block", "month", "amount_paid", "payment_status"])

    # Query 7: Average daily meals served by meal type
    cursor.execute("""
        SELECT meal_type, COUNT(log_id) AS total_served
        FROM meal_logs
        WHERE status = 'Eaten'
        GROUP BY meal_type
    """)
    print_results("QUERY 7: TOTAL MEALS SERVED BY MEAL TYPE", cursor.fetchall(), ["meal_type", "total_served"])

    # Query 8: Most Expensive Operational Expense Category
    cursor.execute("""
        SELECT category, SUM(amount) AS total_spent
        FROM mess_expenses
        GROUP BY category
        ORDER BY total_spent DESC
        LIMIT 1
    """)
    print_results("QUERY 8: MOST EXPENSIVE OPERATIONAL EXPENSE", cursor.fetchall(), ["category", "total_spent"])

    # Query 9: Members who ate all 3 meals on 2026-09-01
    cursor.execute("""
        SELECT m.name, m.hostel_block
        FROM members m
        JOIN meal_logs l ON m.member_id = l.member_id
        WHERE l.log_date = '2026-09-01' AND l.status = 'Eaten'
        GROUP BY m.member_id, m.name
        HAVING COUNT(DISTINCT l.meal_type) = 3
    """)
    print_results("QUERY 9: MEMBERS WHO ATE ALL 3 MEALS ON 2026-09-01", cursor.fetchall(), ["name", "hostel_block"])

    # Query 10: Total cost of guest meals per member
    cursor.execute("""
        SELECT m.name, COUNT(l.log_id) AS guest_meals_count, COUNT(l.log_id) * 100.0 AS guest_charge
        FROM members m
        JOIN meal_logs l ON m.member_id = l.member_id
        WHERE l.status = 'Guest Meal'
        GROUP BY m.member_id, m.name
    """)
    print_results("QUERY 10: GUEST MEAL CHARGES PER MEMBER", cursor.fetchall(), ["name", "guest_meals_count", "guest_charge"])

    # Query 11: Member count per hostel block
    cursor.execute("""
        SELECT hostel_block, COUNT(member_id) AS total_students
        FROM members
        GROUP BY hostel_block
    """)
    print_results("QUERY 11: MEMBER COUNT PER HOSTEL BLOCK", cursor.fetchall(), ["hostel_block", "total_students"])

    # Query 12: Members who skipped 2 or more meals
    cursor.execute("""
        SELECT m.name, COUNT(l.log_id) AS skipped_meals
        FROM members m
        JOIN meal_logs l ON m.member_id = l.member_id
        WHERE l.status = 'Skipped'
        GROUP BY m.member_id, m.name
        HAVING skipped_meals >= 2
    """)
    print_results("QUERY 12: MEMBERS WITH 2 OR MORE SKIPPED MEALS", cursor.fetchall(), ["name", "skipped_meals"])

    # Query 13: Operational expenses breakdown
    cursor.execute("SELECT expense_id, category, amount, expense_date FROM mess_expenses ORDER BY amount DESC")
    print_results("QUERY 13: OPERATIONAL EXPENSES BREAKDOWN", cursor.fetchall(), ["expense_id", "category", "amount", "expense_date"])

    # Query 14: Menu items and pricing by category
    cursor.execute("SELECT item_name, category, cost_per_serving FROM menu ORDER BY category")
    print_results("QUERY 14: MENU ITEMS AND PRICING BY CATEGORY", cursor.fetchall(), ["item_name", "category", "cost_per_serving"])

    # Query 15: Per-member average attendance rate
    cursor.execute("""
        SELECT m.name, 
               COUNT(l.log_id) AS total_logged,
               SUM(CASE WHEN l.status = 'Eaten' THEN 1 ELSE 0 END) AS eaten_count,
               ROUND(CAST(SUM(CASE WHEN l.status = 'Eaten' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(l.log_id) * 100, 2) AS attendance_pct
        FROM members m
        JOIN meal_logs l ON m.member_id = l.member_id
        GROUP BY m.member_id, m.name
    """)
    print_results("QUERY 15: MEMBER ATTENDANCE PERCENTAGE", cursor.fetchall(), ["name", "total_logged", "eaten_count", "attendance_pct"])

    # ==========================================
    # OPTIMIZE AT LEAST 3 QUERIES WITH INDEXES
    # ==========================================
    print("=" * 75, flush=True)
    print(">>> OPTIMIZING AT LEAST 3 QUERIES USING INDEXES & EXPLAIN QUERY PLAN <<<", flush=True)
    print("=" * 75 + "\n", flush=True)

    # Optimization 1: meal_logs by member_id & log_date
    print("--- OPTIMIZATION 1: QUERYING MEAL LOGS BY MEMBER & DATE ---", flush=True)
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM meal_logs WHERE member_id = 1 AND log_date = '2026-09-01'")
    print(f"BEFORE INDEX: {cursor.fetchall()[0][-1]}")

    cursor.execute("CREATE INDEX idx_meal_logs_member_date ON meal_logs(member_id, log_date);")
    conn.commit()

    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM meal_logs WHERE member_id = 1 AND log_date = '2026-09-01'")
    print(f"AFTER INDEX:  {cursor.fetchall()[0][-1]}\n")

    # Optimization 2: payments by payment_status
    print("--- OPTIMIZATION 2: FILTERING PAYMENTS BY STATUS ---", flush=True)
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM payments WHERE payment_status = 'Pending'")
    print(f"BEFORE INDEX: {cursor.fetchall()[0][-1]}")

    cursor.execute("CREATE INDEX idx_payments_status ON payments(payment_status);")
    conn.commit()

    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM payments WHERE payment_status = 'Pending'")
    print(f"AFTER INDEX:  {cursor.fetchall()[0][-1]}\n")

    # Optimization 3: meal_logs by status
    print("--- OPTIMIZATION 3: FILTERING MEAL LOGS BY STATUS ('Skipped') ---", flush=True)
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM meal_logs WHERE status = 'Skipped'")
    print(f"BEFORE INDEX: {cursor.fetchall()[0][-1]}")

    cursor.execute("CREATE INDEX idx_meal_logs_status ON meal_logs(status);")
    conn.commit()

    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM meal_logs WHERE status = 'Skipped'")
    print(f"AFTER INDEX:  {cursor.fetchall()[0][-1]}\n")

    conn.close()

if __name__ == "__main__":
    main()
