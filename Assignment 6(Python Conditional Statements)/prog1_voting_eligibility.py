"""
Program 1: Check if a person is eligible to vote (age >= 18).
"""

def check_voting_eligibility(name, age):
    if age >= 18:
        print(f"Eligible: {name} (Age: {age}) is eligible to vote.")
        return True
    else:
        print(f"Not Eligible: {name} (Age: {age}) must be at least 18 to vote.")
        return False


def main():
    print("--- Program 1: Voting Eligibility Checker ---")
    
    check_voting_eligibility("Rahul", 20)
    check_voting_eligibility("Priya", 16)
    check_voting_eligibility("Amit", 18)


if __name__ == "__main__":
    main()
