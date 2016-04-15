from AccountHolder import AccountHolder
from BankAccount import BankAccount

acct_holder_0 = AccountHolder(
    "Alice Jones",
    "123 Oak",
    "503-507-8889",
    "12/12/64",
    "123-12-1232"
    )

acct_holder_1 = AccountHolder(
    "Bob Jones",
    "123 Oak",
    "503-507-8889",
    "01/12/64",
    "123-14-1221"
    )

print(acct_holder_0.get_name())

acct_0 = BankAccount(
    [acct_holder_0],
    999,
    "Checking"
    )

acct_1 = BankAccount(
    [
     acct_holder_0,
     acct_holder_1
    ],
    1230,
    "Checking"
)
