import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "ecommerce.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Create customers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            city VARCHAR(50) NOT NULL
        )
    """)

    # 2. Create orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date DATE NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)

    # 3. Create products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(50) NOT NULL,
            price REAL NOT NULL
        )
    """)

    # 4. Create order_items table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            PRIMARY KEY (order_id, product_id),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)

    conn.commit()

    # Populate sample data if empty
    cursor.execute("SELECT COUNT(*) FROM customers")
    if cursor.fetchone()[0] == 0:
        sample_customers = [
            (1, 'Krish Patel', 'Mumbai'),
            (2, 'Anita Sharma', 'Delhi'),
            (3, 'Rahul Verma', 'Bangalore'),
            (4, 'Siddharth Rao', 'Mumbai'),
            (5, 'Pooja Mehta', 'Ahmedabad') # Customer with 0 orders
        ]
        cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", sample_customers)

        sample_products = [
            (101, 'Laptop', 60000.00),
            (102, 'Smartphone', 25000.00),
            (103, 'Headphones', 2000.00),
            (104, 'Monitor', 15000.00)
        ]
        cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", sample_products)

        sample_orders = [
            (1, 1, '2026-01-15', 62000.00),
            (2, 1, '2026-02-10', 25000.00),
            (3, 2, '2026-01-20', 52000.00),
            (4, 3, '2026-02-15', 15000.00),
            (5, 4, '2026-03-05', 60000.00)
        ]
        cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", sample_orders)

        sample_items = [
            (1, 101, 1),
            (1, 103, 1),
            (2, 102, 1),
            (3, 102, 2),
            (3, 103, 1),
            (4, 104, 1),
            (5, 101, 1)
        ]
        cursor.executemany("INSERT INTO order_items VALUES (?, ?, ?)", sample_items)
        conn.commit()
        print("Sample data inserted successfully!\n", flush=True)

    def print_results(title, records, headers):
        print("=" * 70, flush=True)
        print(title, flush=True)
        print("=" * 70, flush=True)

        header_str = " | ".join(f"{h:<20}" for h in headers)
        print(header_str, flush=True)
        print("-" * len(header_str), flush=True)

        for row in records:
            formatted_row = [f"{round(val, 2)}" if isinstance(val, float) else str(val) for val in row]
            print(" | ".join(f"{val:<20}" for val in formatted_row), flush=True)
        print("\n", flush=True)

    # Task 1: Total orders per customer
    cursor.execute("""
        SELECT c.customer_id, c.name, COUNT(o.order_id) AS total_orders
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.name
    """)
    print_results("1. TOTAL ORDERS PER CUSTOMER", cursor.fetchall(), ["customer_id", "name", "total_orders"])

    # Task 2: Customers who never placed an order
    cursor.execute("""
        SELECT c.customer_id, c.name, c.city
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        WHERE o.order_id IS NULL
    """)
    print_results("2. CUSTOMERS WHO NEVER PLACED AN ORDER", cursor.fetchall(), ["customer_id", "name", "city"])

    # Task 3: Highest selling product
    cursor.execute("""
        SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity_sold
        FROM products p
        JOIN order_items oi ON p.product_id = oi.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_quantity_sold DESC
        LIMIT 1
    """)
    print_results("3. HIGHEST SELLING PRODUCT", cursor.fetchall(), ["product_id", "product_name", "total_quantity_sold"])

    # Task 4: Monthly sales report
    cursor.execute("""
        SELECT strftime('%Y-%m', order_date) AS month, COUNT(order_id) AS total_orders, SUM(amount) AS total_sales
        FROM orders
        GROUP BY month
        ORDER BY month
    """)
    print_results("4. MONTHLY SALES REPORT", cursor.fetchall(), ["month", "total_orders", "total_sales"])

    # Task 5: Customers with total purchase > 50,000
    cursor.execute("""
        SELECT c.customer_id, c.name, SUM(o.amount) AS total_purchase
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.name
        HAVING total_purchase > 50000
    """)
    print_results("5. CUSTOMERS WITH TOTAL PURCHASE > 50,000", cursor.fetchall(), ["customer_id", "name", "total_purchase"])

    # Task 6: Top 3 cities by revenue
    cursor.execute("""
        SELECT c.city, SUM(o.amount) AS total_revenue
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.city
        ORDER BY total_revenue DESC
        LIMIT 3
    """)
    print_results("6. TOP 3 CITIES BY REVENUE", cursor.fetchall(), ["city", "total_revenue"])

    conn.close()

if __name__ == "__main__":
    main()
