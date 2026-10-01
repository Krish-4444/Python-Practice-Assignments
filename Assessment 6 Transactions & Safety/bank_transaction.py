import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "bank.db")

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

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create accounts table with balance CHECK constraint
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_holder VARCHAR(50) NOT NULL,
            balance REAL NOT NULL CHECK(balance >= 0)
        )
    """)
    conn.commit()

    # Clear existing data for a fresh execution
    cursor.execute("DELETE FROM accounts")
    conn.commit()

    # 1. Start a transaction & Insert records into accounts (Commit valid transactions)
    print(">>> 1. STARTING TRANSACTION & INSERTING INITIAL ACCOUNTS", flush=True)
    cursor.execute("BEGIN TRANSACTION;")
    initial_accounts = [
        (101, 'Alice', 10000.00),
        (102, 'Bob', 5000.00),
        (103, 'Charlie', 2000.00)
    ]
    cursor.executemany("INSERT INTO accounts (account_id, account_holder, balance) VALUES (?, ?, ?)", initial_accounts)
    conn.commit()
    print("Valid transaction committed successfully!\n", flush=True)

    cursor.execute("SELECT account_id, account_holder, balance FROM accounts")
    print_results("ACCOUNTS AFTER INITIAL COMMIT", cursor.fetchall(), ["account_id", "account_holder", "balance"])

    # 2. Rollback Changes Demonstration
    print(">>> 2. DEMONSTRATING TRANSACTION ROLLBACK", flush=True)
    try:
        cursor.execute("BEGIN TRANSACTION;")
        cursor.execute("INSERT INTO accounts (account_id, account_holder, balance) VALUES (999, 'Temp Account', 500.00)")
        print("Inserted 'Temp Account' inside transaction (not committed yet).", flush=True)

        print("Rolling back transaction...", flush=True)
        conn.rollback()
        print("Transaction rolled back successfully!\n", flush=True)
    except Exception as e:
        conn.rollback()
        print(f"Error occurred, rolled back: {e}\n", flush=True)

    cursor.execute("SELECT account_id, account_holder, balance FROM accounts")
    print_results("ACCOUNTS AFTER ROLLBACK (Temp Account not saved)", cursor.fetchall(), ["account_id", "account_holder", "balance"])

    # 3. Demonstrate Transfer of Money Using Transaction (Successful Case)
    print(">>> 3. DEMONSTRATING SUCCESSFUL MONEY TRANSFER (Alice -> Bob 3,000)", flush=True)
    transfer_amount = 3000.00
    from_acc = 101  # Alice
    to_acc = 102    # Bob

    try:
        cursor.execute("BEGIN TRANSACTION;")

        # Debit from Alice
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (transfer_amount, from_acc))
        # Credit to Bob
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (transfer_amount, to_acc))

        conn.commit()
        print(f"Successfully transferred {transfer_amount:.2f} from Account {from_acc} (Alice) to Account {to_acc} (Bob)!", flush=True)
    except Exception as e:
        conn.rollback()
        print(f"Transfer failed! Transaction rolled back: {e}\n", flush=True)

    cursor.execute("SELECT account_id, account_holder, balance FROM accounts")
    print_results("ACCOUNTS AFTER SUCCESSFUL MONEY TRANSFER", cursor.fetchall(), ["account_id", "account_holder", "balance"])

    # 4. Demonstrate Transfer of Money with Rollback (Failed Case - Insufficient Balance)
    print(">>> 4. DEMONSTRATING FAILED MONEY TRANSFER WITH ROLLBACK (Charlie tries to transfer 5,000 but only has 2,000)", flush=True)
    excess_amount = 5000.00
    from_acc_fail = 103  # Charlie (balance: 2000)
    to_acc_fail = 101    # Alice

    try:
        cursor.execute("BEGIN TRANSACTION;")

        # Debit from Charlie (will violate CHECK balance >= 0)
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (excess_amount, from_acc_fail))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (excess_amount, to_acc_fail))

        conn.commit()
        print("Transfer completed!", flush=True)
    except sqlite3.IntegrityError as e:
        conn.rollback()
        print(f"TRANSACTION FAILED & ROLLED BACK! Reason: CHECK constraint failed ({e})", flush=True)

    cursor.execute("SELECT account_id, account_holder, balance FROM accounts")
    print_results("ACCOUNTS AFTER FAILED MONEY TRANSFER (Balances unchanged)", cursor.fetchall(), ["account_id", "account_holder", "balance"])

    conn.close()

if __name__ == "__main__":
    main()
