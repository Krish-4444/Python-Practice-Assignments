"""
Runner script to execute all Assignment 9 programs in sequence.
"""

import subprocess
import sys
from pathlib import Path

def main():
    current_dir = Path(__file__).parent
    programs = sorted([f for f in current_dir.glob("prog*.py")])
    
    print("=" * 60)
    print("          ASSIGNMENT 9 - FILE HANDLING IN PYTHON")
    print("=" * 60)
    
    for prog in programs:
        print(f"\n>>> Running: {prog.name}")
        print("-" * 60)
        res = subprocess.run([sys.executable, str(prog)], capture_output=True, text=True)
        if res.stdout:
            print(res.stdout.strip())
        if res.stderr:
            print("[STDERR]", res.stderr.strip())
        print("-" * 60)
        
    print("\nAll Assignment 9 programs executed successfully!")

if __name__ == "__main__":
    main()
