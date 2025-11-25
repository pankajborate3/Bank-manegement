class Bank:
    def __init__(self, Account_ID, Account_Name):
        self.Account_ID = Account_ID
        self.Account_Name = Account_Name


class Account(Bank):
    def __init__(self, Account_ID, Account_Name, Balance, mobile_no, Address):
        super().__init__(Account_ID, Account_Name)
        self.Balance = Balance
        self.mobile_no = mobile_no
        self.Address = Address

    def Account_details(self):
        print(f"Account_ID: {self.Account_ID},\n"
              f"Account_Name: {self.Account_Name}, \n"
              f"Balance: {self.Balance}, \n"
              f"mobile_no: {self.mobile_no},\n"
              f"Address: {self.Address}\n")


class BankManagementSystem:
    def __init__(self):
        self.Accounts = []

    def add_Account(self):
        try:
            Account_ID = int(input("Enter Account ID: "))


            for a in self.Accounts:
                if a.Account_ID == Account_ID:
                    print("Account ID already exists! Try again.\n")
                    return

            Account_Name = input("Enter Name: ")
            Balance = int(input("Enter Balance: "))
            mobile_no = input("Enter mobile number: ")
            Address = input("Enter Address: ")

            account_obj = Account(Account_ID, Account_Name, Balance, mobile_no, Address)
            self.Accounts.append(account_obj)
            print(f"Account '{Account_Name}' added successfully!\n")

        except ValueError:
            print("Invalid input! Please enter correct data.\n")

    def view_all(self):
        if not self.Accounts:
            print("No Accounts found!\n")
            return

        print("\n===== All Accounts =====")
        for a in self.Accounts:
            a.Account_details()

    def search_Account(self):
        try:
            target = int(input("Enter Account ID to search: "))
            for a in self.Accounts:
                if a.Account_ID == target:
                    print("\nAccount Found:")
                    a.Account_details()
                    return
            print("Account not found!\n")

        except ValueError:
            print("Invalid input!\n")

    def delete_Account(self):
        try:
            target = int(input("Enter Account ID to delete: "))
            for a in self.Accounts:
                if a.Account_ID == target:
                    self.Accounts.remove(a)
                    print("Account deleted successfully!\n")
                    return
            print("Account not found!\n")

        except ValueError:
            print("Invalid input!\n")


    def withdraw_Amount(self):
        try:
            acc_id = int(input("Enter Account ID: "))

            for acc in self.Accounts:
                if acc.Account_ID == acc_id:
                    amount = int(input("Enter amount to withdraw: "))

                    if amount <= 0:
                        print("Amount must be greater than zero.\n")
                        return

                    if acc.Balance < amount:
                        print("Insufficient Balance!\n")
                        return

                    acc.Balance -= amount
                    print(f"Withdrawal successful! New Balance: {acc.Balance}\n")
                    return

            print("Account not found!\n")

        except ValueError:
            print("Invalid input! Enter numeric values.\n")


def main():
    bnk = BankManagementSystem()

    while True:
        print("========  Bank Management System ========")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Withdraw Amount")
        print("4. Search Account")
        print("5. Delete Account")
        print("6. Exit")
        print("============================================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            bnk.add_Account()
        elif choice == '2':
            bnk.view_all()
        elif choice == '3':
            bnk.withdraw_Amount()
        elif choice == '4':
            bnk.search_Account()
        elif choice == '5':
            bnk.delete_Account()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
