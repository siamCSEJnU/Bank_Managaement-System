from user import Account


class Admin:
    def __init__(self):
        self.accounts = []
        self.is_loan_active = True
        self.is_bankrupt = False

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts.append(account)
        print(
            f"Account created successfully. Account Number : {account.account_number}"
        )

    def delete_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)
            print(f"Account {account_number} deleted successfully!!")
        else:
            print("Account does not exist!")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def view_all_accounts(self):
        if self.accounts:
            print("----All User Accounts----")
            for account in self.accounts:
                print(
                    f"Account Number : {account.account_number}, Name : {account.name}, Balance : {account.balance}"
                )
        else:
            print("No accounts available")

    def total_bank_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        print(f"Total available balance in the bank: {total_balance}")

    def total_loan_amount(self):
        total_loan = sum(account.loan_count for account in self.accounts)
        print(
            f"Total loan amount in the bank: {total_loan*1000}"
        )  # Assuming the amount per loan is 1000tk

    def toggle_loan_status(self):
        self.is_loan_active = not self.is_loan_active
        if self.is_loan_active:
            status = "enabled"
        else:
            status = "disabled"
        print(f"Loan features is now {status}")

    def toggle_bankrupt_status(self):
        self.is_bankrupt = not self.is_bankrupt
        if self.is_bankrupt:
            status = "bankrupt"
        else:
            status = "operational"
        print(f"The bank is now {status}")


def main():
    admin = Admin()
    while True:
        print("\n--- Banking Management System ---")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")
        option = input("Enter option: ")
        if option == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == "admin" and password == "123":
                print("Admin login successful.")
                while True:
                    print("\n--- Admin Menu ---")
                    print("1. Create Account")
                    print("2. Delete Account")
                    print("3. List All Accounts")
                    print("4. Total Bank Balance")
                    print("5. Total Loan Amount")
                    print("6. Toggle Loan Status")
                    print("7. Toggle Bankrupt Status")
                    print("8. Go Back to Main Menu")

                    choice = input("Enter your choice: ")
                    if choice == "1":
                        name = input("Enter name: ")
                        email = input("Enter email: ")
                        address = input("Enter address: ")
                        account_type = input("Enter account type (Savings/Current): ")
                        admin.create_account(name, email, address, account_type)

                    elif choice == "2":
                        account_number = input("Enter account number to delete: ")
                        admin.delete_account(account_number)

                    elif choice == "3":
                        admin.view_all_accounts()

                    elif choice == "4":
                        admin.total_bank_balance()

                    elif choice == "5":
                        admin.total_loan_amount()

                    elif choice == "6":
                        admin.toggle_loan_status()

                    elif choice == "7":
                        admin.toggle_bankrupt_status()

                    elif choice == "8":
                        break
                    else:
                        print("Invalid choice!! Please try again.")
            else:
                print("Invalid username or password.")

        elif option == "2":
            while True:
                print("\n--- User Menu ---")
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Check Balance")
                print("4. View Transactions")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Go Back to Main Menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    account_number = input("Enter your account number: ")
                    account = admin.find_account(account_number)
                    if account:
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    else:
                        print("Account does not exist.")

                elif choice == "2":
                    account_number = input("Enter your account number: ")
                    account = admin.find_account(account_number)
                    if account:
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount, admin.is_bankrupt)
                    else:
                        print("Account does not exist.")

                elif choice == "3":
                    account_number = input("Enter your account number: ")
                    account = admin.find_account(account_number)
                    if account:
                        account.check_balance(admin.is_bankrupt)
                    else:
                        print("Account does not exist.")

                elif choice == "4":
                    account_number = input("Enter your account number: ")
                    account = admin.find_account(account_number)
                    if account:
                        account.view_transactions()
                    else:
                        print("Account does not exist.")

                elif choice == "5":
                    account_number = input("Enter your account number: ")
                    account = admin.find_account(account_number)
                    if account:
                        amount = float(input("Enter loan amount(1000): "))
                        account.take_loan(amount, admin.is_bankrupt)
                    else:
                        print("Account does not exist.")

                elif choice == "6":
                    account_number = input("Enter your account number: ")
                    account = admin.find_account(account_number)
                    if account:
                        recipient_number = input("Enter recipient account number: ")
                        recipient_account = admin.find_account(recipient_number)
                        if recipient_account:
                            amount = float(input("Enter amount to transfer: "))
                            account.transfer(
                                amount, recipient_account, admin.is_bankrupt
                            )
                        else:
                            print("Recipient account does not exist.")
                    else:
                        print("Account does not exist.")

                elif choice == "7":
                    break

                else:
                    print("Invalid choice!! Please try again.")

        elif option == "3":
            print("Exiting the system... Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")


main()


# 85975
# 29249
# 18574
