"""
Demonstrates Modules and Packages in Python.
Covers: import, from...import, __name__, __all__, relative imports
"""
import sys
from banking import BankAccount, SavingsAccount

def main():
    print(f"Import path: {sys.path[:3]}")
    acc = BankAccount("Dev", 1000)
    acc.deposit(500)
    print(f"Account for {acc.owner} has balance {acc.balance}")
    
    # Demonstrate SavingsAccount
    savings = SavingsAccount("Alice", 5000, rate=0.03)
    print(f"\nSavings Account for {savings.owner} has balance {savings.balance}")
    savings.apply_interest()
    print(f"After interest: {savings.balance}")

if __name__ == "__main__":
    main()
