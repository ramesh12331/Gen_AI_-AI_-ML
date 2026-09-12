# ==========================================================
# BANK APPLICATION USING OOPS
# ==========================================================

class Bank:

    # ------------------------------------------------------
    # Constructor
    # ------------------------------------------------------

    def __init__(self, pin, balance, password):

        self.pin = pin
        self.balance = balance

        # Password Validation
        while True:

            upper = False
            lower = False
            number = False
            special = False

            if len(password) >= 8:

                for ch in password:

                    if ch.isupper():
                        upper = True

                    elif ch.islower():
                        lower = True

                    elif ch.isdigit():
                        number = True

                    else:
                        special = True

                if upper and lower and number and special:

                    self.password = password
                    print("\nPassword Created Successfully")
                    break

                else:

                    print("\nPassword must contain:")
                    print("✔ One Uppercase Letter")
                    print("✔ One Lowercase Letter")
                    print("✔ One Number")
                    print("✔ One Special Character")

            else:

                print("\nPassword must be at least 8 characters.")

            password = input("Create Password Again : ")

    # ------------------------------------------------------
    # Deposit
    # ------------------------------------------------------

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount
            print("Amount Deposited Successfully")

        else:

            print("Invalid Amount")

    # ------------------------------------------------------
    # Withdraw
    # ------------------------------------------------------

    def withdraw(self, amount):

        if amount > 0:

            if amount <= self.balance:

                self.balance -= amount
                print("Withdrawal Successful")

            else:

                print("Insufficient Balance")

        else:

            print("Invalid Amount")

    # ------------------------------------------------------
    # View Balance (Password Required)
    # ------------------------------------------------------

    def view_balance(self):

        pwd = input("Enter Password : ")

        if pwd == self.password:

            print("Current Balance :", self.balance)

        else:

            print("Incorrect Password")

    # ------------------------------------------------------
    # Reset PIN
    # ------------------------------------------------------

    def reset_pin(self):

        old_pin = input("Enter Current PIN : ")

        if old_pin == self.pin:

            new_pin = input("Enter New PIN : ")
            confirm_pin = input("Confirm New PIN : ")

            if new_pin == confirm_pin:

                self.pin = new_pin
                print("PIN Changed Successfully")

            else:

                print("PIN Does Not Match")

        else:

            print("Incorrect PIN")


# ==========================================================
# Create Account
# ==========================================================

print("========== CREATE ACCOUNT ==========")

pin = input("Create PIN : ")

balance = int(input("Enter Opening Balance : "))

password = input("Create Password : ")

account = Bank(pin, balance, password)

# ==========================================================
# MENU
# ==========================================================

while True:

    print("\n===================================")
    print("        BANK APPLICATION")
    print("===================================")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Reset PIN")
    print("5. Exit")
    print("===================================")

    choice = input("Enter Your Choice : ")

    # Deposit
    if choice == "1":

        amount = int(input("Enter Deposit Amount : "))

        account.deposit(amount)

    # Withdraw
    elif choice == "2":

        amount = int(input("Enter Withdrawal Amount : "))

        account.withdraw(amount)

    # View Balance
    elif choice == "3":

        account.view_balance()

    # Reset PIN
    elif choice == "4":

        account.reset_pin()

    # Exit
    elif choice == "5":

        print("\nThank You")
        print("Bye")
        break

    else:

        print("Invalid Choice")

# =====================================================
# ========== CREATE ACCOUNT ==========

# Create PIN : 1234
# Enter Opening Balance : 10000
# Create Password : admin

# Password must contain:
# ✔ One Uppercase Letter
# ✔ One Lowercase Letter
# ✔ One Number
# ✔ One Special Character

# Create Password Again : Admin@123

# Password Created Successfully

# ===================================
#         BANK APPLICATION
# ===================================
# 1. Deposit
# 2. Withdraw
# 3. View Balance
# 4. Reset PIN
# 5. Exit
# ===================================

# Enter Your Choice : 1
# Enter Deposit Amount : 5000
# Amount Deposited Successfully

# Enter Your Choice : 3
# Enter Password : Admin@123
# Current Balance : 15000

# Enter Your Choice : 2
# Enter Withdrawal Amount : 3000
# Withdrawal Successful

# Enter Your Choice : 3
# Enter Password : Admin@123
# Current Balance : 12000

# Enter Your Choice : 4
# Enter Current PIN : 1234
# Enter New PIN : 5678
# Confirm New PIN : 5678
# PIN Changed Successfully

# Enter Your Choice : 5

# Thank You
# Bye