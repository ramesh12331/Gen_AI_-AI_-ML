"""
==========================================================
PYTHON EXCEPTION HANDLING
Date : 03-08-2026
Topics:
1. try / except / else / finally
2. raise keyword
3. Raising built-in exceptions
4. Custom Exceptions
==========================================================
"""

# ==========================================================
# 1. try / except / else / finally
# ==========================================================

try:

    f = open("sample1.txt", "r")

except FileNotFoundError:

    print("File not found")

else:

    print(f.read())

finally:

    print("Hey, I'm finally block. I always execute.")

    try:
        f.close()
    except NameError:
        pass


# ==========================================================
# 2. raise Keyword
# ==========================================================
# We can manually generate an exception using raise.

a = 10

raise NameError("Hey! Name is not there.")


# ==========================================================
# 3. Bank Account Example using Exception
# ==========================================================

class Bank:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def withdraw(self, amount):

        if amount < 0:
            raise Exception("Enter a valid amount")

        if amount > self.balance:
            raise Exception("Insufficient Balance")

        self.balance -= amount


account = Bank("Raghu", 5000)


# ----------------------------------------------------------
# Example 1
# ----------------------------------------------------------

try:

    account.withdraw(9000000)

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

    print(a + b)

except Exception as e:

    print(e)


# ==========================================================
# 5. Creating Custom Exception
# ==========================================================

class BankException(Exception):

    def __init__(self, message):

        super().__init__(message)


# ==========================================================
# Bank Class using Custom Exception
# ==========================================================

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


account = Bank("Raghu", 5000)


# ----------------------------------------------------------
# Valid Withdrawal
# ----------------------------------------------------------

try:

    account.withdraw(900)

except BankException as e:

    print(e)

else:

    print("Remaining Balance :", account.balance)


# ----------------------------------------------------------
# Invalid Withdrawal
# ----------------------------------------------------------

try:

    account.withdraw(12900)

except BankException as e:

    print(e)

else:

    print("Remaining Balance :", account.balance)

# ==========================================================
"""
==========================================================
PYTHON EXCEPTION HANDLING
Date : 03-08-2026
Topic : Custom Exceptions (Google Login Example)
==========================================================
"""

import time

# ==========================================================
# 1. Using Built-in Exception
# ==========================================================

class Google:

    def __init__(self, email, password, device):

        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):

        if device != self.device:
            raise Exception("Please login using your registered device.")

        if email == self.email and password == self.password:
            print("Login Successful")


# ----------------------------------------------------------
# Object Creation
# ----------------------------------------------------------

google = Google(
    "anwar@gmail.com",
    12345,
    "mobile"
)

# ----------------------------------------------------------
# Wrong Device
# ----------------------------------------------------------

try:

    google.login(
        "anwar@gmail.com",
        12345,
        "laptop"
    )

except Exception as e:

    print(e)


# ----------------------------------------------------------
# Correct Device
# ----------------------------------------------------------

google.login(
    "anwar@gmail.com",
    12345,
    "mobile"
)

# Output
# ------
# Login Successful


# ==========================================================
# 2. Creating Custom Exception
# ==========================================================

class SecurityException(Exception):

    def __init__(self, message):

        super().__init__(message)


class Google:

    def __init__(self, email, password, device):

        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):

        if device != self.device:
            raise SecurityException(
                "Unknown Device Detected."
            )

        if email == self.email and password == self.password:
            print("Login Successful")


google = Google(
    "anwar@gmail.com",
    12345,
    "mobile"
)

try:

    google.login(
        "anwar@gmail.com",
        12345,
        "laptop"
    )

except SecurityException as e:

    print(e)


# ==========================================================
# 3. Adding logout() Method
# ==========================================================

class SecurityException(Exception):

    def __init__(self, message):

        super().__init__(message)

    def logout(self):

        print("Logout Successfully")


class Google:

    def __init__(self, email, password, device):

        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):

        if device != self.device:
            raise SecurityException(
                "Unknown Device Detected."
            )

        if email == self.email and password == self.password:
            print("Login Successful")


google = Google(
    "anwar@gmail.com",
    12345,
    "mobile"
)

try:

    google.login(
        "anwar@gmail.com",
        12345,
        "laptop"
    )

except SecurityException as e:

    print(e)
    e.logout()


# ==========================================================
# 4. Adding OTP Authentication
# ==========================================================

class SecurityException(Exception):

    def __init__(self, message):

        super().__init__(message)

    def logout(self):

        print("Logout Successfully")

    def otp(self):

        print("Sending OTP...")
        time.sleep(3)
        print("OTP Verified")


class Google:

    def __init__(self, email, password, device):

        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):

        # --------------------------------------------------
        # If the user logs in from a different device,
        # ask for additional authentication.
        # --------------------------------------------------

        if device != self.device:

            raise SecurityException(
                "Unknown Device Detected."
            )

        if email == self.email and password == self.password:

            print("Login Successful")


google = Google(
    "anwar@gmail.com",
    12345,
    "mobile"
)

try:

    google.login(
        "anwar@gmail.com",
        12345,
        "laptop"
    )

except SecurityException as e:

    print(e)

    e.logout()

    e.otp()