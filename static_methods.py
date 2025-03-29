# static methods

# a static method in Python is a method that belongs to the class itself 
# rather than to an instance of the class.

# to define a static method in Python, you use the @staticmethod decorator.

# when to use static methods:
# when you want to create a method that is not associated with any specific instance of a class.
# when you want to create a method that is not dependent on the instance state of the class.
# ie - process data that does not need to be associated with any specific instance of a class.

class BackAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):  
            self.balance += amount
            self.__log_transaction("deposited", amount)
        else:
            print("Deposit amount must be greater than 0.")
    
    def _is_valid_amount(self, amount):
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        print(f"{self.owner} {transaction_type} ${amount}. New balance: ${self.balance}")

    @staticmethod
    def is_valid_intrest_rate(rate):
        return 0 <= rate <= 5
    

acct = BackAccount("Jeremy")
acct.deposit(100)
print(BackAccount.is_valid_intrest_rate(6))