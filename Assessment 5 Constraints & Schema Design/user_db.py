import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "store.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Enable Foreign Key Support in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Create users table with Primary Key, Unique Email, and Not Null Password
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """)

    # 2. Create orders table with Foreign Key referencing users(user_id)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_name VARCHAR(100) NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )
    """)

    # 3. Create index on email column
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
    """)

    # 4. Create view to display user order summary
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_order_summary AS
        SELECT 
            u.user_id,
            u.name AS user_name,
            u.email,
            COUNT(o.order_id) AS total_orders,
            COALESCE(SUM(o.amount), 0) AS total_spent
        FROM users u
        LEFT JOIN orders o ON u.user_id = o.user_id
        GROUP BY u.user_id, u.name, u.email;
    """)

    conn.commit()

    # Insert sample data if tables are empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        sample_users = [
            ('Krish Patel', 'krish@example.com', 'pass123'),
            ('Alice Smith', 'alice@example.com', 'secure456'),
            ('Bob Jones', 'bob@example.com', 'mypass789'),
            ('Charlie Brown', 'charlie@example.com', 'pwd321')
        ]
        cursor.executemany("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", sample_users)

        sample_orders = [
            (1, 'Laptop', 75000.00),
            (1, 'Mouse', 1500.00),
            (2, 'Smartphone', 45000.00),
            (2, 'Headphones', 3000.00),
            (2, 'Charger', 1200.00),
            (3, 'Tablet', 25000.00)
            # Charlie (user_id 4) has 0 orders to test LEFT JOIN in view
        ]
        cursor.executemany("INSERT INTO orders (user_id, product_name, amount) VALUES (?, ?, ?)", sample_orders)
        conn.commit()
        print("Sample users and orders inserted successfully!\n", flush=True)

    def print_results(title, records, headers):
        print("=" * 70, flush=True)
        print(title, flush=True)
        print("=" * 70, flush=True)

        header_str = " | ".join(f"{h:<20}" for h in headers)
        print(header_str, flush=True)
        print("-" * len(header_str), flush=True)

        for row in records:
            formatted_row = [f"{round(val, 2)}" if isinstance(val, float) else ("NULL" if val is None else str(val)) for val in row]
            print(" | ".join(f"{val:<20}" for val in formatted_row), flush=True)
        print("\n", flush=True)

    # Display Users Table Records
    cursor.execute("SELECT user_id, name, email, password FROM users")
    records = cursor.fetchall()
    print_results("1. USERS TABLE (PRIMARY KEY, UNIQUE EMAIL, NOT NULL PASSWORD)", records, ["user_id", "name", "email", "password"])

    # Display Orders Table Records (Foreign Key to Users)
    cursor.execute("SELECT order_id, user_id, product_name, amount FROM orders")
    records = cursor.fetchall()
    print_results("2. ORDERS TABLE (FOREIGN KEY -> USERS.USER_ID)", records, ["order_id", "user_id", "product_name", "amount"])

    # Display Index Details on email column
    cursor.execute("PRAGMA index_list('users')")
    indexes = cursor.fetchall()
    print_results("3. INDEXES CREATED ON USERS TABLE", indexes, ["seq", "name", "unique", "origin", "partial"])

    # Display User Order Summary View
    cursor.execute("SELECT user_id, user_name, email, total_orders, total_spent FROM user_order_summary")
    records = cursor.fetchall()
    print_results("4. USER ORDER SUMMARY VIEW", records, ["user_id", "user_name", "email", "total_orders", "total_spent"])

    conn.close()

if __name__ == "__main__":
    main()
