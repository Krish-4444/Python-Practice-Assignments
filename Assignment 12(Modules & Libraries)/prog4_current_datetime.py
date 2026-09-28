"""
Program 4: Use datetime module to display current date and time.
"""

from datetime import datetime

def main():
    print("--- Program 4: Current Date and Time ---")
    
    # Get current date and time
    now = datetime.now()
    
    print(f"Default Format        : {now}")
    print(f"Date Only (YYYY-MM-DD): {now.strftime('%Y-%m-%d')}")
    print(f"Time Only (HH:MM:SS)  : {now.strftime('%H:%M:%S')}")
    print(f"Formatted String      : {now.strftime('%A, %d %B %Y, %I:%M:%S %p')}")

if __name__ == "__main__":
    main()
