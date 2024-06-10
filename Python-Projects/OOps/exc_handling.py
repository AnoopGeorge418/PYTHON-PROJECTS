class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds to withdraw the amount")
        self.balance -= amount

account = BankAccount(100)
account.deposit(50)
print(f"Balance after deposit: {account.balance}")

try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(e)

print(f"Balance after withdrawal attempt: {account.balance}")
