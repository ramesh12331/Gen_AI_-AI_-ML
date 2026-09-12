# ==========================================================
# PYTHON OOPS - CLASSES & OBJECTS
# ==========================================================

# ----------------------------------------------------------
# What is OOP?
# ----------------------------------------------------------

# OOP = Object Oriented Programming

# Real-Time Examples:
# 1. Bank
# 2. Student
# 3. Employee
# 4. Car
# 5. Mobile


# ==========================================================
# WHAT IS A CLASS?
# ==========================================================

# A Class is a blueprint (template) used to create objects.

class Bank:

    # Class Variables
    name = None
    age = None
    branch = None


# ==========================================================
# CREATING AN OBJECT
# ==========================================================

b = Bank()

print(b)

# Output:
# <__main__.Bank object at 0x.....>


# ==========================================================
# ACCESSING CLASS VARIABLES
# ==========================================================

print(b.name)

# Output:
# None


# ==========================================================
# UPDATING CLASS VARIABLES
# ==========================================================

class Bank:

    name = "Rahul"
    age = 40
    branch = "Hyderabad"


b = Bank()

print(b.name)
print(b.age)
print(b.branch)

# Output
# Rahul
# 40
# Hyderabad


# ==========================================================
# MULTIPLE OBJECTS
# ==========================================================

class Bank:

    name = "Rahul"
    age = 40
    branch = "Hyderabad"


b = Bank()
b1 = Bank()

print(b.name, b.age, b.branch)
print(b1.name, b1.age, b1.branch)

# Output
# Rahul 40 Hyderabad
# Rahul 40 Hyderabad


# ==========================================================
# CONSTRUCTOR (__init__)
# ==========================================================

# Wrong Example

class Bank:

    def __init__(name, age, branch):
        print(name, age, branch)


# b = Bank()

# Error:
# TypeError
# Missing required positional arguments


# ----------------------------------------------------------
# Another Wrong Example
# ----------------------------------------------------------

class Bank:

    def __init__(name, age, branch):
        print(name, age, branch)


# b = Bank("Annu", 25, "Hyd")

# Error:
# TypeError:
# Takes 3 positional arguments but 4 were given

# Why?
# Python automatically passes the current object (self).


# ==========================================================
# CORRECT CONSTRUCTOR
# ==========================================================

class Bank:

    def __init__(self, name, age, branch):

        print(name)
        print(age)
        print(branch)


b = Bank("Annu", 25, "Hyd")

# Output
# Annu
# 25
# Hyd


# ==========================================================
# WHY SELF?
# ==========================================================

# self represents the current object.

# Python internally executes:

# Bank.__init__(b, "Annu", 25, "Hyd")

# self = b
# name = "Annu"
# age = 25
# branch = "Hyd"


# ==========================================================
# INSTANCE VARIABLES
# ==========================================================

class Bank:

    def __init__(self, user_name, u_age, u_branch):

        self.name = user_name
        self.age = u_age
        self.branch = u_branch


b = Bank("Annu", 25, "Hyd")

print(b.name)
print(b.age)
print(b.branch)

# Output
# Annu
# 25
# Hyd


# ==========================================================
# PARAMETER NAMES CAN BE ANYTHING
# ==========================================================

class Bank:

    def __init__(self, x, y, z):

        self.name = x
        self.age = y
        self.branch = z


b = Bank("Annu", 25, "Hyd")

print(b.name)
print(b.age)
print(b.branch)

# Output
# Annu
# 25
# Hyd


# ==========================================================
# GETTER METHOD
# ==========================================================

class Bank:

    def __init__(self, user_name, u_age, u_branch):

        self.name = user_name
        self.age = u_age
        self.branch = u_branch

    # Getter Method
    def get_info(self):

        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Branch :", self.branch)


b = Bank("Annu", 25, "Hyd")

b.get_info()


# ==========================================================
# MULTIPLE OBJECTS
# ==========================================================

class Bank:

    def __init__(self, user_name, u_age, u_branch):

        self.name = user_name
        self.age = u_age
        self.branch = u_branch

    def get_info(self):

        print(self.name, self.age, self.branch)


b = Bank("Annu", 25, "Hyd")
b1 = Bank("Shannu", 35, "Vij")

b.get_info()
b1.get_info()

# Output
# Annu 25 Hyd
# Shannu 35 Vij


# ==========================================================
# HOW TO ACCESS INSTANCE VARIABLES
# ==========================================================

# Method 1: Using Object Name

print(b.name)

# Method 2: Using Getter Method

b.get_info()


# ==========================================================
# BANK MANAGEMENT SYSTEM
# ==========================================================

class Bank:

    # Constructor
    def __init__(self, name, accno, balance, pin):

        self.name = name
        self.accno = accno
        self.balance = balance
        self.pin = pin


    # ------------------------------------------------------
    # View Balance
    # ------------------------------------------------------

    def view_balance(self):

        print("Current Balance :", self.balance)


    # ------------------------------------------------------
    # Deposit Money
    # ------------------------------------------------------

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            print("Amount Deposited Successfully")
            print("Current Balance :", self.balance)

        else:

            print("Enter Positive Amount")


    # ------------------------------------------------------
    # Withdraw Money
    # ------------------------------------------------------

    def withdraw(self, amount):

        if amount > 0:

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

print()

b.deposit(2000)

print()

b.withdraw(1000)

print()

b.withdraw(10000)

print()

b.withdraw(-500)


# ==========================================================
# OUTPUT
# ==========================================================

# ------ Bank Operations ------
#
# Current Balance : 5000
#
# Amount Deposited Successfully
# Current Balance : 7000
#
# Withdrawal Successful
# Current Balance : 6000
#
# Insufficient Balance
#
# Enter Positive Amount


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

# 1. What is OOP?
# 2. What is a Class?
# 3. What is an Object?
# 4. What is a Constructor?
# 5. What is self?
# 6. What are Instance Variables?
# 7. What is a Getter Method?
# 8. How many ways can we access instance variables?
# 9. Why do we use __init__()?
# 10. Difference between Class Variable and Instance Variable?