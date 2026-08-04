# ==========================================================
# 2. raise Keyword
# ==========================================================
# We can manually generate an exception using raise.
a = 10

# raise NameError("Hey! Name is not there.")

# ==========================================================
# 3. Bank Account Example using Exception
# ==========================================================
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdraw(self, amount):
        if amount<0:
            raise Exception("Enter a valid amount")
        if amount>self.balance:
            raise Exception("Insufficient Balance")
        self.balance -= amount
account = Bank("Ramesh", 100000)

# ----------------------------------------------------------
# Example 1
# ----------------------------------------------------------
try:
    account.withdraw(200000)
except Exception as e:
    print(e)

# ----------------------------------------------------------
# Example 2
# ----------------------------------------------------------
try:
    account.withdraw(900)
except Exception as e:
    print(e)
else:
    print("Remaining Balance :", account.balance)

# ==========================================================
# 4. Built-in Exception Example
# ==========================================================
try:
    a = 20
    b = "s"
    print(a+b)
except Exception as e:
    print(e)
# ==========================================================
# 5. Creating Custom Exception
# ==========================================================
class BankException(Exception):
    def __init__(self, message):
        super().__init__(message)
# =================================
# Bank Class using Custom Exception
# =================================
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        if amount < 0:
             raise BankException("Enter a valid amount")
        if amount > self.balance:
            raise BankException("Insufficient Balance")
        self.balance -= amount
account = Bank("Ramesh", 5000)

# ----------------
# Valid Withdrawal
# ----------------
try:
    account.withdraw(900)
except Exception as e:
    print(e)
else:
    print("Remaining Balance :", account.balance)

# -------------------
# Invalid Withdrawal
# -------------------
try:
    account.withdraw(12900)
except BankException as e:
    print(e)
else:
    print("Remaining Balance :", account.balance)