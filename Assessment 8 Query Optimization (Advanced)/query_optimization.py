import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "optimization.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    # Setup Tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date DATE NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)
    conn.commit()

    # Populate Sample Data
    cursor.execute("SELECT COUNT(*) FROM customers")
    if cursor.fetchone()[0] == 0:
        sample_customers = [
            (101, 'Alice Smith', 'alice@example.com'),
            (102, 'Bob Jones', 'bob@example.com'),
            (103, 'Charlie Brown', 'charlie@example.com')
        ]
        cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", sample_customers)

        sample_orders = []
        for i in range(1, 1001):
            cust_id = 101 if i % 3 == 0 else (102 if i % 3 == 1 else 103)
            sample_orders.append((i, cust_id, '2026-01-01', round(100.0 + i * 2.5, 2)))

        cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", sample_orders)
        conn.commit()
        print("Sample database created with 1,000 orders!\n", flush=True)

    def print_section(title):
        print("=" * 75, flush=True)
        print(title, flush=True)
        print("=" * 75, flush=True)

    # Task 1 & 2: EXPLAIN QUERY PLAN Before Indexing orders.customer_id
    print_section("1. EXPLAIN QUERY PLAN - BEFORE ADDING INDEX")
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 101")
    plan_before = cursor.fetchall()
    for row in plan_before:
        print(f"Plan Detail: {row[-1]}", flush=True)
    print("\nNotice: SQLite performs a SCAN (Full Table Scan) on 'orders' table.\n", flush=True)

    # Add Index to orders.customer_id
    print_section("2. ADDING INDEX ON orders.customer_id")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON orders(customer_id);")
    conn.commit()
    print("Index 'idx_orders_customer_id' created successfully!\n", flush=True)

    # EXPLAIN QUERY PLAN After Indexing
    print_section("3. EXPLAIN QUERY PLAN - AFTER ADDING INDEX")
    cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 101")
    plan_after = cursor.fetchall()
    for row in plan_after:
        print(f"Plan Detail: {row[-1]}", flush=True)
    print("\nNotice: SQLite now uses SEARCH 'orders USING INDEX idx_orders_customer_id'.\n", flush=True)

    # Task 3: Optimize a Slow JOIN Query
    print_section("4. OPTIMIZING SLOW JOIN QUERY")
    print("Executing JOIN query: SELECT c.name, o.order_id, o.amount FROM customers c JOIN orders o ON c.customer_id = o.customer_id WHERE o.customer_id = 101;")
    cursor.execute("""
        EXPLAIN QUERY PLAN
        SELECT c.name, o.order_id, o.amount
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        WHERE o.customer_id = 101
    """)
    join_plan = cursor.fetchall()
    print("\nQuery Execution Plan for JOIN:")
    for row in join_plan:
        print(f" - {row[-1]}", flush=True)
    
    cursor.execute("""
        SELECT c.name, COUNT(o.order_id) AS order_count, SUM(o.amount) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        WHERE o.customer_id = 101
        GROUP BY c.name
    """)
    results = cursor.fetchall()
    print(f"\nJOIN Result: Customer: {results[0][0]} | Total Orders: {results[0][1]} | Total Spent: Rs.{results[0][2]:,.2f}\n")

    # Task 4: Explain When Index Should NOT Be Used
    print_section("5. WHEN INDEXES SHOULD NOT BE USED (BEST PRACTICES)")
    reasons = [
        "1. Small Tables: On tables with very few rows, full table scan is faster than index lookup.",
        "2. Heavy Write Operations (Frequent INSERT/UPDATE/DELETE): Every index slows down write operations because indexes must be updated.",
        "3. Low Selectivity / Low Cardinality Columns: Columns with few unique values (e.g., Gender, Status, True/False) where query returns large % of rows.",
        "4. Columns with Mostly NULL Values or rarely used in WHERE, JOIN, or ORDER BY clauses.",
        "5. Columns Used in Function Expressions: Standard index won't be used if query wraps column in function like UPPER(email)."
    ]
    for r in reasons:
        print(r, flush=True)
    print("\n", flush=True)

    conn.close()

if __name__ == "__main__":
    main()
