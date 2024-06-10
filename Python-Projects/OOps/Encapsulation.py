# Problem: Create a class Account with private attributes balance and account_number. 
# Add methods to deposit, withdraw, and check the balance.

class Account:
    def __init__(self, account_number, balance = 0):
        self.__account_number = account_number
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
            
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient fund')
        else:
            self.__balance -= amount
                
    def check_balance(self):
        return self.__balance
        
    
account1 = Account(124578895623)
account1.deposit(500)
account1.withdraw(200)
print(f'Balance: {account1.check_balance()}')

print('\n')

account2 = Account(152485487241)
account2.deposit(1000)
account2.withdraw(1100)
print(f'Balance: {account2.check_balance()}')