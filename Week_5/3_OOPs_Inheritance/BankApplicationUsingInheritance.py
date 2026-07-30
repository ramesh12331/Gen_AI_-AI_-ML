# ==========================================================
# BANK APPLICATION USING INHERITANCE
# ==========================================================

# ----------------------------------------------------------
# Parent Class
# ----------------------------------------------------------
class Bank:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    # Deposit
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    # Withdraw
    def withdraw(self, amount):
        if amount>0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Amount")

    # View Balance
    def view_balance(self):
        print("Current Balance :", self.balance)

# ----------------------------------------------------------
# Child Class
# ----------------------------------------------------------
class SavingAccount(Bank):
    def __init__(self, pin, balance, interest_rate):
        super().__init__(pin, balance)
        self.interest_rate = interest_rate

    # Add Interest
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest Added :", interest)

# ----------------------------------------------------------
# Object
# ----------------------------------------------------------

account = SavingAccount("1234", 5000, 10)

account.view_balance()
account.add_interest()
account.view_balance()