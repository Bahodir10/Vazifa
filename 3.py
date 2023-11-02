class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance, transaction_fee):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        if self.balance >= amount + self.transaction_fee:
            self.balance -= amount + self.transaction_fee
        else:
            print("Insufficient funds")

savings_account = SavingsAccount("SA001", 1000, 0.05)
checking_account = CheckingAccount("CA001", 2000, 1.5)

savings_account.deposit(500)
checking_account.withdraw(100)
savings_interest = savings_account.calculate_interest()

print("Savings Account Balance:", savings_account.balance)
print("Checking Account Balance:", checking_account.balance)
print("Interest Earned on Savings Account:", savings_interest)
