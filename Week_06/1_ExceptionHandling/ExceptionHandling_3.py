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
    def __init__(self,email, password, device):
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
google = Google("ramesh@gmail.com", 1234, "mobile")

# ----------------------------------------------------------
# Wrong Device
# ----------------------------------------------------------
try:
    google.login("ramesh@gmail.com", 1234, "laptop")
except Exception as e:
    print(e)

# ----------------------------------------------------------
# Correct Device
# ----------------------------------------------------------

try:
    google.login("ramesh@gmail.com", 1234, "mobile")
except Exception as e:
    print(e)

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
    def __init__(self,email, password, device):
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if device != self.device:
            raise SecurityException("Please login using your registered device.")
        if email == self.email and password == self.password:
            print("Login Successful")

google = Google("ramesh@gmail.com", 1234, "mobile")

try:
    google.login("ramesh@gmail.com", 1234, "laptop")
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
    def __init__(self,email, password, device):
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if device != self.device:
            raise SecurityException("Please login using your registered device.")
        if email == self.email and password == self.password:
            print("Login Successful")

google = Google("ramesh@gmail.com", 1234, "mobile")

try:
    google.login("ramesh@gmail.com", 1234, "laptop")
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
    def __init__(self,email, password, device):
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if device != self.device:
            raise SecurityException("Please login using your registered device.")
        if email == self.email and password == self.password:
            print("Login Successful")

google = Google("ramesh@gmail.com", 1234, "mobile")

try:
    google.login("ramesh@gmail.com", 1234, "laptop")
except SecurityException as e:
    print(e)
    e.logout()
    e.otp()