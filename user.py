import random


class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = f"{random.randint(10000, 99999)}"
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited : {amount}")
        print(f"Successfully deposited with : {amount}. New balance :{self.balance}")

    def withdraw(self, amount, is_bankrupt):
        if is_bankrupt:
            print("Withdraw is not possible due to bankrupt")
            return

        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew : {amount}")
            print(f"Successfully withdrawn {amount}. New balance : {self.balance}")

    def check_balance(self, is_bankrupt):
        if is_bankrupt:
            print("The bank is bankrupt!!! No operations are possible.")
        else:
            print(f"Available balance : {self.balance}")

    def view_transactions(self):
        if self.transaction_history:
            print("----Transaction History----")
            for transaction in self.transaction_history:
                print(transaction)

        else:
            print("No transactions available!!")

    def take_loan(self, amount, is_bankrupt):
        if is_bankrupt:
            print("The bank is bankrupt!!Loan is not possible.")
            return
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transaction_history.append(f"Loan Taken : {amount}")
            print(
                f"Loan {amount} taken successfully. New balance is : {self.balance}. "
            )
        else:
            print("Loan limit exceeded!! You can only take loan twice.")

    def transfer(self, amount, recipient_account, is_bankrupt):
        if is_bankrupt:
            print("The bank is bankrupt!!Transfer is not possible.")
            return

        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(
                f"Transferred {amount} to Account Number: {recipient_account.account_number}, Name : {recipient_account.name}  "
            )
            recipient_account.transaction_history.append(
                f"Received {amount} from {self.account_number}"
            )
            print(
                f"Successfully transferred {amount} to {recipient_account.account_number}. New balance: {self.balance}"
            )
        else:
            print("Insufficient funds for transfer!!")
