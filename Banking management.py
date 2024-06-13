class BankAccount:
    def __init__(self, acc_num, ifsc_code, name, branch, acc_type, balance=0):
        self.acc_num = acc_num
        self.ifsc_code = ifsc_code
        self.name = name
        self.branch = branch
        self.acc_type = acc_type
        self.balance = balance

    def create_account(self):
        try:
            int(self.acc_num)
        except ValueError:
            raise ValueError("Account number must be an integer")

        try:
            ifsc_code_length = len(self.ifsc_code)
            if ifsc_code_length != 11:
                raise ValueError("IFSC code must be 11 characters long")

            for char in self.ifsc_code:
                if not char.isalnum():
                    raise ValueError("IFSC code must contain only alphanumeric characters")
        except ValueError:
            raise ValueError("Invalid IFSC code")

        try:
            if not self.name.isalpha():
                raise ValueError("Name must contain only alphabetic characters")
        except ValueError:
            raise ValueError("Invalid name")

        try:
            if not self.branch.isalpha():
                raise ValueError("Branch must contain only alphabetic characters")
        except ValueError:
            raise ValueError("Invalid branch")

        try:
            if self.acc_type not in ["zero balance", "student acc", "business acc"]:
                raise ValueError("Invalid account type")
        except ValueError:
            raise ValueError("Invalid account type")

        print(f"Account created successfully!\nAccount number: {self.acc_num}\nIFSC code: {self.ifsc_code}\nName: {self.name}\nBranch: {self.branch}\nAccount type: {self.acc_type}\nBalance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        print(f"Amount deposited successfully! New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if self.balance < amount:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        print(f"Amount withdrawn successfully! New balance: {self.balance}")

    def display_balance(self):
        print(f"Your current balance is: {self.balance}")


def main():
    # Create a new bank account
    try:
        acc_num = input("Enter account number: ")
        ifsc_code = input("Enter IFSC code: ")
        name = input("Enter name: ")
        branch = input("Enter branch: ")

        print("Choose account type:")
        print("1. Zero Balance Account")
        print("2. Student Account")
        print("3. Business Account")

        acc_type_choice = int(input("Enter your choice (1, 2, or 3): "))

        if acc_type_choice == 1:
            acc_type = "zero balance"
        elif acc_type_choice == 2:
            acc_type = "student acc"
        elif acc_type_choice == 3:
            acc_type = "business acc"
        else:
            raise ValueError("Invalid account type choice")

        bank_account = BankAccount(acc_num, ifsc_code, name, branch, acc_type)
        bank_account.create_account()
    except Exception as e:
        print(e)
        return

    # Perform banking operations
    while True:
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        try:
            if choice == 1:
                amount = float(input("Enter amount to deposit: "))
                bank_account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                bank_account.withdraw(amount)
            elif choice == 3:
                bank_account.display_balance()
            elif choice == 4:
                break
            else:
                raise ValueError("Invalid choice")
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
