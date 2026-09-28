"""
Program 9: Write a program to calculate the difference between two dates.
"""

from datetime import date, datetime

def calculate_days_difference(date_str1: str, date_str2: str, date_format: str = "%Y-%m-%d"):
    """Calculate the difference in days between two date strings."""
    d1 = datetime.strptime(date_str1, date_format).date()
    d2 = datetime.strptime(date_str2, date_format).date()
    diff = abs((d2 - d1).days)
    return diff

def main():
    print("--- Program 9: Calculate Difference Between Two Dates ---")
    
    # Example 1: Direct date objects
    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)
    delta = end_date - start_date
    
    print(f"Start Date : {start_date}")
    print(f"End Date   : {end_date}")
    print(f"Difference : {delta.days} days ({delta.days // 7} weeks and {delta.days % 7} days)")
    
    # Example 2: Using user-friendly string format (YYYY-MM-DD)
    date_a = "2023-08-15"
    date_b = "2026-09-28"
    diff_days = calculate_days_difference(date_a, date_b)
    print(f"\nDifference between {date_a} and {date_b} : {diff_days} days")

if __name__ == "__main__":
    main()
