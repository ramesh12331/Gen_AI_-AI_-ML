class Bank:
    def __init__(self,name,accno,balance,pin):
        self.name = name
        self.accno = accno
        self.balance = balance
        self.pin = pin

    # ------------------------------------------------------
        # View Balance
    # ------------------------------------------------------
    
    def view_balance(self):
        print("Current Balance : ", self.balance)

    # ------------------------------------------------------
    # Deposit Money
    # ------------------------------------------------------

    def deposit(self, amount):
        if amount>0:
            self.balance += amount

            print("Amount Deposited Successfully")
            print("Current Balance :", self.balance)
        else:
            print("Enter Positive Amount")

    # ------------------------------------------------------
    # Withdraw Money
    # ------------------------------------------------------
    def withdraw(self, amount):
        if amount>0:
            if self.balance >= amount:
                self.balance -= amount

                print("Withdrawal Successful")
                print("Current Balance :", self.balance)

            else:
                print("Insufficient Balance")

        else:
            print("Enter Positive Amount")

# ==========================================================
# OBJECT CREATION
# ==========================================================
b = Bank("Ramesh", 123456789, 5000, 1234)

# ==========================================================
# METHOD CALLS
# ==========================================================

print("\n------ Bank Operations ------\n")

b.view_balance()

b.deposit(2000)

b.withdraw(1000)