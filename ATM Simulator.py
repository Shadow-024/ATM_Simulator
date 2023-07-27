class ATM:
    def _init_(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_user_input(self, length):
        while True:
            user_input = input(f"Please enter your {length} digits pin: ")
            if user_input.isdigit() and len(user_input) == length:
                return user_input
            print(f"Invalid input! Please enter {length} digits only.")


class ATMPrint(ATM):
    def get_user_input(self, length):
        user_input = super().get_user_input(length)
        return user_input


if __name__ == "_main_":
    atm = ATMPrint()

    password_length = 4
    user_input = atm.get_user_input(password_length)

    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            print("Your balance: ", atm.check_balance())
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            if atm.deposit(amount):
                print("Deposit successful.")
                print("Your balance: ", atm.check_balance())
            else:
                print("Invalid amount.")
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: "))
            if atm.withdraw(amount):
                print("Withdrawal successful.")
                print("Your balance: ", atm.check_balance())
            else:
                print("Insufficient balance or invalid amount.")
        elif choice == 4:
            print("Exiting the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")