# ==========================================================
# SyntaxError
# Something in the program is not written according to
# Python grammar.
# ==========================================================
a = 10
# A

# Output : NameError: name 'A' is not defined. Did you mean: 'a'?

# ==========================================================
# Runtime Errors (Exceptions)
# ==========================================================

# ----------------------------------------------------------
# IndexError
# ----------------------------------------------------------
l = [1, 2, 3]
# print(l[45])

# IndexError: list index out of range

# ----------------------------------------------------------
# KeyError
# ----------------------------------------------------------

d = {"name": "abc"}
# print(d["abc"])

# ----------------------------------------------------------
# TypeError
# ----------------------------------------------------------

# print(10 + "a")

# ----------------------------------------------------------
# ValueError
# ----------------------------------------------------------
# print(int("str"))

# ----------------------------------------------------------
# NameError
# ----------------------------------------------------------
a = 10
# print(A)

# ----------------------------------------------------------
# AttributeError
# ----------------------------------------------------------

l = [2, 3, 4, 5, 6]
# l.get()

# Another AttributeError example

a = "string"
# a.append("r")

# ----------------------------------------------------------
# ZeroDivisionError
# ----------------------------------------------------------

# print(10 / 0)

# ----------------------------------------------------------
# ModuleNotFoundError
# ----------------------------------------------------------

# import numpyeee as np

# ==========================================================
# Example Without Exception Handling
# ==========================================================

# f = open("sample.txt", "r")
# print(f.read())

# ==========================================================
# Handling Exception using try-except
# ==========================================================

try:
    f = open("sample.txt", "r")
    print(f.read())
except:
    print("File not found")

# ==========================================================
# Another Example
# ==========================================================
try:
    a = 20
    print(a/0)
except:
    print("Pass value greater than zero")

# ==========================================================
# Flow of try-except
# ==========================================================

# try
# ----
# Risky code goes here.

# If there is NO exception
# -> Remaining try block executes.

# If there IS an exception
# -> Python immediately jumps to except block.


# ==========================================================
# Catching Specific Exception
# ==========================================================
try:
    a = 20
    print(A)

    l = [2,3,4]
    print(l[8])

    print(20/0)
except NameError:
    print("Give some valid variable name")

# ==========================================================
# Multiple Except Blocks
# ==========================================================
try:
    a = 20
    print(A)

    l = [2,3,4]
    print(l[8])

    print(20/0)

except NameError:
     print("Give some valid variable name")
except IndexError:
    print("Give proper index value")
except ZeroDivisionError:
    print("Enter value greater than zero")

# ==========================================================
# Example 1
# ==========================================================

try:
    a = 20
    print(A)
except NameError:
    print("Give some valid variable name")

# Output
# -------
# Give some valid variable name

# ==========================================================
# Example 2
# ==========================================================

try:
    l = [2,3,4]
    print(l[8])
except IndexError:
    print("Give proper index value")

# Output
# -------
# Give proper index value

# ==========================================================
# Example 3
# ==========================================================

try:
    print(20/0)
except ZeroDivisionError:
    print("Enter value greater than zero")

# Output
# -------
# Enter value greater than zero

# ==========================================================
# ValueError Example
# ==========================================================
age = int(input("Enter age: "))
print(age)

# Input
# -----
# twenty

# Output
# ------
# ValueError

# ==========================================================
# Handling ValueError
# ==========================================================

try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Only numerical values are allowed")

# Input
# -----
# twenty

# Output
# ------
# Only numerical values are allowed

# ==========================================================
# Exception as e
# ==========================================================

try:
    age = int(input("Enter age: "))
    print(age)
except Exception as e:
    print(e)

# Input
# -----
# twenty

# Output
# ------
# invalid literal for int() with base 10: 'twenty'

# ==========================================================
# PYTHON EXCEPTION HANDLING - ELSE BLOCK
# ==========================================================
# Syntax
# -------
# try:
#     # Risky code

# except Exception as e:
#     # Exception handling

# else:
    # Executes only if no exception occurs

# ==========================================================
# Example 1
# ==========================================================
try:
    name = input("Enter a name: ")
except Exception as e:
    print(e)
else:
    print(name)

# ==========================================================
# Example 2
# ==========================================================

try:
    age = int(input("Enter age: "))
except Exception as e:
    print(e)
else:
    print(age)

# ==========================================================
# Example 3
# ==========================================================
try:
    age = int(input("Enter age: "))
except Exception as e:
    print(e)
else:
    print("Hey, I'm else block executing:", age)

# ==========================================================
# What happens if exception occurs?
# ==========================================================
try:
    age = int(input("Enter age: "))
except Exception as e:
    print(e)
else:
    print(age)

# Input
# -----
# twenty

# Output
# ------
# invalid literal for int() with base 10: 'twenty'

# Note:
# Since exception occurred,
# else block will NOT execute.

# ==========================================================
# FINALLY BLOCK
# ==========================================================
# ----------------------------------------------------------
# What is finally block?
# ----------------------------------------------------------
# finally block always executes
# whether exception occurs or not.

# Mostly used for:
# - Closing files
# - Closing database connections
# - Releasing resources
# ==========================================================
# Example 1 - Writing File
# ==========================================================

f = open("sample.txt", "w")
f.write("Heyyyy Raghav!!!!!!")
f.close()

# ==========================================================
# Example 2 - Reading File
# ==========================================================

f = open("sample.txt", "r")
print(f.read())
f.close()

# Output
# -------
# Heyyyy Raghav!!!!!!

# ==========================================================
# Combination of try, except, else, finally
# ==========================================================
try:
    f = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
finally:
    f.close()

# Output
# -------
# Heyyyy Raghav!!!!!!

# ==========================================================
# Wrong Example
# ==========================================================

try:
    f= open("sample.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
finally:
    f.close()
# f.write("Hello")

# Output
# -------
# ValueError:
# I/O operation on closed file.

# ------------------------------------------------------------------
# try / except / else / finally with file handling
# ------------------------------------------------------------------
try:
    f = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
finally:
    print("Hey im executed")
    f.close()