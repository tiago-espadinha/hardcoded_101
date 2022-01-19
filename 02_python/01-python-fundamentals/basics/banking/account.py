# banking/account.py
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount): self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate
    def apply_interest(self): self.balance *= (1 + self.rate)
