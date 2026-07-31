# ==========================================================
# POLYMORPHISM - OPERATOR OVERLOADING
# ==========================================================

# ==========================================================
# EXAMPLE 1: '+' Operator with Integers
# ==========================================================

a = 10
b = 30

print("Addition:", a + b)      # Output: 40


# ==========================================================
# EXAMPLE 2: '+' Operator with Strings
# ==========================================================

a = "10"
b = "30"

print("Concatenation:", a + b)     # Output: 1030


# ==========================================================
# EXAMPLE 3: '*' Operator with String and Integer
# ==========================================================

a = "10"
b = 3

print("String Repetition:", a * b)     # Output: 101010


# ==========================================================
# EXAMPLE 4: '*' Operator with Two Strings
# ==========================================================

a = "10"
b = "30"

# print(a * b)       # TypeError
# Strings cannot be multiplied by strings.


# ==========================================================
# EXAMPLE 5: Constructor Ignoring Parameter
# ==========================================================

class A:

    def __init__(self, balance):
        self.balance = 40000


a = A(500000)

print("Balance:", a.balance)

# Output:
# 40000


# ==========================================================
# EXAMPLE 6: Constructor Using Parameter
# ==========================================================

class A:

    def __init__(self, balance):
        self.balance = balance


a = A(500000)

print("Balance:", a.balance)

# Output:
# 500000


# ==========================================================
# EXAMPLE 7: Constructor Without Argument (Error)
# ==========================================================

class A:

    def __init__(self, balance):
        self.balance = balance


# a = A()

# TypeError
# Missing required positional argument


# ==========================================================
# EXAMPLE 8: Constructor Without Parameters
# ==========================================================

class A:

    def __init__(self):
        self.balance = 40000


a = A()

print("Balance:", a.balance)

# Output:
# 40000


# ==========================================================
# EXAMPLE 9: Why a + b Gives Error
# ==========================================================

class A:

    def __init__(self, balance):
        self.balance = balance


a = A(3000)
b = A(5000)

# print(a + b)

# TypeError
# Unsupported operand type(s)


# ==========================================================
# EXAMPLE 10: Operator Overloading using __add__()
# ==========================================================

class A:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance


a = A(3000)
b = A(5000)

print("Total Balance:", a + b)

# Output:
# 8000


# ==========================================================
# EXAMPLE 11: Greater Than using __gt__()
# ==========================================================

class A:

    def __init__(self, balance):
        self.balance = balance

    def __gt__(self, other):
        return self.balance > other.balance


a = A(3000)
b = A(5000)

print(a > b)

# Output:
# False


# ==========================================================
# EXAMPLE 12: Less Than using __lt__()
# ==========================================================

class A:

    def __init__(self, balance):
        self.balance = balance

    def __lt__(self, other):
        return self.balance < other.balance


a = A(3000)
b = A(5000)

print(a < b)

# Output:
# True


# ==========================================================
# MAGIC METHODS TABLE
# ==========================================================

# +   --> __add__()
# -   --> __sub__()
# *   --> __mul__()
# /   --> __truediv__()
# ==  --> __eq__()
# >   --> __gt__()
# <   --> __lt__()
# >=  --> __ge__()
# <=  --> __le__()


# ==========================================================
# HOW PYTHON EXECUTES a + b
# ==========================================================

# Python Code:
#
#     a + b
#
# Internally Python Converts It Into:
#
#     a.__add__(b)
#
# Here:
#
# self  = a
# other = b
#
# return self.balance + other.balance
#
# 3000 + 5000
#
# Output:
#
# 8000


# ==========================================================
# INTERVIEW DEFINITIONS
# ==========================================================

# Polymorphism:
# One operator or method behaves differently for different objects.

# Operator Overloading:
# Giving a new meaning to operators like +, -, >, < for user-defined objects
# using magic methods.