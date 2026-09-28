"""
Program 6: Create a Bank system with SavingsAccount and CurrentAccount classes.
"""

# Base Bank Account Class
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[{self.account_holder}] Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"[{self.account_holder}] Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print(f"[{self.account_holder}] Insufficient balance for withdrawal of ${amount:.2f} (Current: ${self.balance:.2f})")


# Subclass for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"[{self.account_holder}] Interest of ${interest:.2f} added (Rate: {self.interest_rate*100}%). New Balance: ${self.balance:.2f}")


# Subclass for Current Account (Allows Overdraft)
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"[{self.account_holder}] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f} (Overdraft Limit: ${self.overdraft_limit:.2f})")
        else:
            print(f"[{self.account_holder}] Exceeded overdraft limit of ${self.overdraft_limit:.2f}. Withdrawal failed.")


def main():
    print("--- Program 6: Bank System (Savings and Current Account) ---")
    
    # Savings Account Demo
    print("\n--- Savings Account ---")
    savings = SavingsAccount(account_holder="Alice", balance=1000.0, interest_rate=0.04)
    savings.deposit(500.0)
    savings.apply_interest()
    savings.withdraw(300.0)
    
    # Current Account Demo
    print("\n--- Current Account ---")
    current = CurrentAccount(account_holder="Bob", balance=300.0, overdraft_limit=400.0)
    current.withdraw(500.0)  # Allowed using overdraft
    current.withdraw(300.0)  # Exceeds overdraft limit


if __name__ == "__main__":
    main()
