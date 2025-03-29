#encapsulation

class BadBackAccount:
    def __init__(self, balance):
        self.balance = balance


account = BadBackAccount(0)
print(account.balance)
account.balance = -200


class BackAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self._balance += amount

    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if self._balance < amount:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


acc = BackAccount()
print(acc.balance)
acc.deposit(100)
acc.withdraw(50)
print(acc.balance)