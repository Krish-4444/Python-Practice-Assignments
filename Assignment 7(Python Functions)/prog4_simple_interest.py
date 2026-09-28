"""
Program 4: Function to calculate simple interest.
Formula: SI = (Principal * Rate * Time) / 100
"""

def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100.0
    total_amount = principal + si
    return si, total_amount


def main():
    print("--- Program 4: Simple Interest Calculator ---")
    p, r, t = 10000, 7.5, 3
    interest, total = calculate_simple_interest(p, r, t)
    
    print(f"Principal Amount : ${p:,.2f}")
    print(f"Rate of Interest : {r}% per annum")
    print(f"Time Period      : {t} years")
    print(f"Simple Interest  : ${interest:,.2f}")
    print(f"Total Amount     : ${total:,.2f}")


if __name__ == "__main__":
    main()
