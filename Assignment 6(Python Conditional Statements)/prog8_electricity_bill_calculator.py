"""
Program 8: Electricity bill calculator based on units consumed.
Slab Structure:
  - First 100 units  : $1.50 per unit
  - Next 100 units   : $2.50 per unit
  - Above 200 units  : $4.00 per unit
"""

def calculate_electricity_bill(units):
    if units < 0:
        print("Units consumed cannot be negative.")
        return 0.0

    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    print(f"Units Consumed: {units:<6} -> Total Electricity Bill: ${bill:.2f}")
    return bill


def main():
    print("--- Program 8: Electricity Bill Calculator ---")
    
    test_units = [75, 150, 250, 0]
    for u in test_units:
        calculate_electricity_bill(u)


if __name__ == "__main__":
    main()
