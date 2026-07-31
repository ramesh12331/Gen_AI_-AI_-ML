# ==========================================================
# POLYMORPHISM - OPERATOR OVERLOADING
# ==========================================================

# ==========================================================
# EXAMPLE 1: '+' Operator with Integers
# ==========================================================

a = 10
b = 30

print("Addition:", a + b)

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

#print(a * b) # TypeError
# Strings cannot be multiplied by strings.

# ==========================================================
# EXAMPLE 5: Constructor Ignoring Parameter
# ==========================================================
class A:
    def __init__(self, balance):
        self.balance = 4000

a = A(5000)
print("Balance:", a.balance)

# Output:
# 40000

# ==========================================================
# EXAMPLE 6: Constructor Using Parameter
# ==========================================================

class A:
    def __init__(self, balance):
        self.balance = balance
a = A(5000)
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
        self.balance = 4000
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
b = A(2000)

# print(a+b)

# TypeError
# Unsupported operand type(s)

# ==========================================================
# EXAMPLE 10: Operator Overloading using __add__()
# ==========================================================

class A:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self,other):
        return self.balance + other.balance
a = A(3000)
b = A(5000)

print("Total Balance:", a + b)

# ==========================================================
# EXAMPLE 11: Greater Than using __gt__()
# ==========================================================
class A:
    def __init__(self,balance):
        self.balance = balance
    def __gt__(self,other):
        return self.balance > other.balance
a = A(3000)
b = A(5000)
print(a>b)

# Output:
# False
# ==========================================================
# EXAMPLE 12: Less Than using __lt__()
# ==========================================================

class A:
    def __init__(self,balance):
        self.balance = balance
    def __lt__(self, other):
        return self.balance < other.balance
a = A(3000)
b = A(5000)
print(a<b)

# Output:
# True