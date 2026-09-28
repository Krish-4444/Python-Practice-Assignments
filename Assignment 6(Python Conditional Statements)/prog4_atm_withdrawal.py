"""
Program 4: ATM withdrawal check: sufficient balance or not.
"""

def check_atm_withdrawal(current_balance, withdrawal_amount):
    print(f"Current Balance: ${current_balance:.2f} | Requested Withdrawal: ${withdrawal_amount:.2f}")
    
    if withdrawal_amount <= 0:
        print("Status: Invalid withdrawal amount. Must be greater than $0.")
        return False
    elif withdrawal_amount <= current_balance:
        remaining = current_balance - withdrawal_amount
        print(f"Status: Transaction Successful! Remaining Balance: ${remaining:.2f}")
        return True
    else:
        print("Status: Transaction Failed! Insufficient balance.")
        return False


def main():
    print("--- Program 4: ATM Withdrawal Checker ---")
    
    print("Scenario 1:")
    check_atm_withdrawal(current_balance=1000.00, withdrawal_amount=400.00)
    
    print("\nScenario 2:")
    check_atm_withdrawal(current_balance=500.00, withdrawal_amount=800.00)


if __name__ == "__main__":
    main()
