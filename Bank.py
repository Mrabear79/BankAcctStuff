import random


class BankAccount:

    def __init__(self, acct_holder, acct_balance, acct_type):
        self.acct_holder = acct_holder
        self.acct_balance = acct_balance
        self.acct_type = acct_type
        self.acct_no = random.randint(0, 2**64)

    def deposit(self, amount):
        self.acct_balance += amount

    def withdrawl(self, amount):
        self.acct_balance -= amount

    def get_balance(self):
        return self.acct_balance

    def get_no(self):
        return self.acct_no

acct_0 = BankAccount("Alice", 999, "Checking")

print(acct_0.get_balance())

acct_1 = BankAccount("Bob", 1, "Checking")

print(acct_1.get_balance())

accts_list = []
for i in range(10):
    accts_list.append(BankAccount(i, 99, "Checking"))

print(accts_list)
