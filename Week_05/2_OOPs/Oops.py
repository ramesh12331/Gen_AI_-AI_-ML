# ==========================================================
# WHAT IS A CLASS?
# ==========================================================

# A Class is a blueprint (template) used to create objects.

class Bank:

    # Class Variables
    name = None
    age = None
    branch = None

# CREATING AN OBJECT

b = Bank()
print(b) 
# Output:
# <__main__.Bank object at 0x000002D0CBAE9CD0>

# ACCESSING CLASS VARIABLES
print(b.name)

# Output:
# None

# ==========================================================
# UPDATING CLASS VARIABLES
# ==========================================================
class Bank:
    name = "Ramesh"
    age = 25
    branch = "Hyderabad"

b = Bank()
print(b.name)
print(b.age)
print(b.branch)

# Output:
# Ramesh
# 25
# Hyderabad

# ==========================================================
# MULTIPLE OBJECTS
# ==========================================================
class Bank:
    name = "Ramesh"
    age = 25
    branch = "Hyderabad"

# Object
b = Bank()
b1 = Bank()

print(b.name, b.age, b.branch)
print(b1.name, b1.age, b1.branch)

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
    def __init__(name,age,branch):
        print(name, age, branch)

# b = Bank("Mamidi Ramesh", 25, "Hyderabad")

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

b = Bank("Rakesh", 25, "Hyderabad")

# Output
# Rakesh
# 25
# Hyderabad

# ==========================================================
# INSTANCE VARIABLES
# ==========================================================
class Bank:
    def __init__(self, user_name, u_age, u_branch):
        self.name = user_name
        self.age = u_age
        self.branch = u_branch

b = Bank("Ravi",25,"Hyderabad")
print(b.name)
print(b.age)
print(b.branch)

# ==========================================================
# PARAMETER NAMES CAN BE ANYTHING
# ==========================================================

class Bank:

    def __init__(self, x, y, z):

        self.name = x
        self.age = y
        self.branch = z


b = Bank("Rohith", 25, "Hyd")

print(b.name)
print(b.age)
print(b.branch)

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
        print(self.name)
        print(self.age)
        print(self.branch)

b = Bank("Roshan",25,"Hyderabad")
b.get_info()

# ==========================================================
# MULTIPLE OBJECTS
# ==========================================================
class Bank:
    def __init__(self,user_name, u_age, u_branch):
        self.name = user_name
        self.age = u_age
        self.branch = u_branch

    def get_info(self):
        print(self.name, self.age, self.branch)

b = Bank("Lakshman", 30, "Hyderabad")
b1 = Bank("Murali", 30, "Hyderabad")

# b.get_info()
# b1.get_info()

# ==========================================================
# HOW TO ACCESS INSTANCE VARIABLES
# ==========================================================

# Method 1: Using Object Name

print(b.name)

# Method 2: Using Getter Method

b.get_info()