class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")
            
    def display_balance(self):
        print(f"Account Balance for {self.name}: {self.balance:.2f}")

def main():
    print("Welcome to the Bank Management System")
    name = input("Enter your name to open an account: ")
    account = BankAccount(name)
    
    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
