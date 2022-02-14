"""
Demonstrates Object-Oriented Programming in Python.
Covers: classes, __init__, instance vs class variables, inheritance,
        super(), @property, @classmethod, @staticmethod, dunder methods
"""

class BankAccount:
    """A sample BankAccount class."""
    bank_name = "Pythonic Bank" # Class variable

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance # Protected attribute
        print(f"Account created for {owner} with balance {balance}")

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds or invalid amount")

    def transfer(self, target, amount: float):
        if 0 < amount <= self._balance:
            self.withdraw(amount)
            target.deposit(amount)
            print(f"Transferred {amount} to {target.owner}")

    # Dunder methods
    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance})"

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self._balance})"

    def __len__(self):
        return int(self._balance)

    def __eq__(self, other):
        return self._balance == other._balance

    def __lt__(self, other):
        return self._balance < other._balance

class SavingsAccount(BankAccount):
    """Subclass with interest calculation."""
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest: {interest}")

def main():
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 500)
    
    acc1.deposit(200)
    acc1.withdraw(100)
    acc1.transfer(acc2, 300)
    
    print(acc1)
    print(acc2)
    print(f"Is Alice richer than Bob? {acc1 > acc2}")

    savings = SavingsAccount("Charlie", 1000)
    savings.apply_interest()

if __name__ == "__main__":
    main()
