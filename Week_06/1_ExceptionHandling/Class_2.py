# ==========================================================
# PYTHON EXCEPTION HANDLING - ELSE BLOCK
# ==========================================================

# ----------------------------------------------------------
# What is else block?
# ----------------------------------------------------------
# The else block executes only when NO exception occurs
# inside the try block.

# Syntax
# -------
try:
    # Risky code

except Exception as e:
    # Exception handling

else:
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

# Output
# -------
# Enter a name: Ramesh
# Ramesh


# ==========================================================
# Example 2
# ==========================================================

try:
    age = int(input("Enter age: "))

except Exception as e:
    print(e)

else:
    print(age)

# Output
# -------
# Enter age: 25
# 25


# ==========================================================
# Example 3
# ==========================================================

try:
    age = int(input("Enter age: "))

except Exception as e:
    print(e)

else:
    print("Hey, I'm else block executing:", age)

# Output
# -------
# Enter age: 23
# Hey, I'm else block executing: 23


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
# Flow
# ==========================================================

# try
# ----
# Open file

# except
# -------
# Executes only if file not found

# else
# ----
# Executes only if file opened successfully

# finally
# -------
# Always closes the file


# ==========================================================
# Wrong Example
# ==========================================================

try:

    f = open("sample.txt", "r")

except FileNotFoundError:

    print("File not found")

else:

    print(f.read())

finally:

    f.close()

f.write("Hello")

# Output
# -------
# ValueError:
# I/O operation on closed file.


# ==========================================================
# Why?
# ==========================================================

# Because finally block already executed.

# f.close()

# After closing the file,
# Python does not allow writing.


# ==========================================================
# Summary
# ==========================================================

# try
# ----
# Risky code.

# except
# -------
# Handles exceptions.

# else
# ----
# Executes only if NO exception occurs.

# finally
# -------
# Executes ALWAYS.
# Mostly used for resource cleanup.

# Best Practice
# -------------
# try
#     Open File
#
# except
#     Handle Exception
#
# else
#     Read / Write File
#
# finally
#     Close File


# ==========================================================
# Execution Flow
# ==========================================================

# Case 1: No Exception
#
# try
#   ↓
# else
#   ↓
# finally


# Case 2: Exception Occurs
#
# try
#   ↓
# except
#   ↓
# finally
