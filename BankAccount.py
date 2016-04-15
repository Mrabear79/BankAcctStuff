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
