"""
Program 2: Create a BankAccount class with deposit and withdraw methods.
"""

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print(f"Insufficient funds! Current Balance: ${self.balance:.2f}, Requested: ${amount:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder} | Balance: ${self.balance:.2f}")


def main():
    print("--- Program 2: BankAccount Class Demo ---")
    account = BankAccount("Alice Smith", balance=500.0)
    account.display_balance()

    account.deposit(250.0)
    account.withdraw(100.0)
    account.withdraw(800.0)  # Exceeds balance


if __name__ == "__main__":
    main()
