# 📘 CHAPTER 12 — PYTHON EXCEPTION HANDLING INTERVIEW PREPARATION

Now we’ll revise the complete **Exception Handling chapter from an interview point of view**, from **beginner → advanced**.

---

# 1️⃣ What is an Exception? 🚨

## ✅ Definition

An **exception is a runtime error or abnormal condition that interrupts the normal flow of a Python program.**

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError: division by zero
```

Flow:

```text
Program starts
     ↓
print(10 / 0)
     ↓
ZeroDivisionError 🚨
     ↓
Normal flow stops
```

---

# 2️⃣ What is Exception Handling? 🛡️

## ✅ Definition

**Exception Handling is the process of detecting and handling runtime errors so that the program can respond properly instead of terminating unexpectedly.**

### Syntax

```python
try:
    # risky code

except:
    # error handling code
```

### Example

```python
try:
    print(10 / 0)

except:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

---

# 3️⃣ Why Do We Need Exception Handling? 🤔

Without exception handling:

```python
print("Start")

print(10 / 0)

print("End")
```

Output:

```text
Start
ZeroDivisionError
```

`"End"` does not execute.

With exception handling:

```python
print("Start")

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

print("End")
```

Output:

```text
Start
Cannot divide by zero
End
```

### ⭐ Interview Answer

> Exception handling prevents runtime errors from unexpectedly terminating the program and allows us to handle error situations gracefully.

---

# 4️⃣ Syntax Error vs Exception ⭐

This is a common interview question.

| Syntax Error                              | Exception                                 |
| ----------------------------------------- | ----------------------------------------- |
| Problem with Python syntax                | Problem occurring during execution        |
| Code cannot be parsed correctly           | Program starts, then encounters a problem |
| Example: missing `:`                      | Example: `10 / 0`                         |
| Usually fixed before successful execution | Can often be handled using `try-except`   |

Example syntax problem:

```python
if 10 > 5
    print("Hello")
```

Missing:

```text
:
```

Runtime exception:

```python
print(10 / 0)
```

Produces:

```text
ZeroDivisionError
```

---

# 5️⃣ Important Built-in Exceptions 🚨

From your chapter, remember these:

| Exception             | Meaning                                  | Example          |
| --------------------- | ---------------------------------------- | ---------------- |
| `IndexError`          | Invalid sequence index                   | `l[45]`          |
| `KeyError`            | Dictionary key missing                   | `d["abc"]`       |
| `TypeError`           | Invalid operation between types          | `10 + "a"`       |
| `ValueError`          | Correct type of operation, invalid value | `int("abc")`     |
| `NameError`           | Variable/name not defined                | `print(A)`       |
| `AttributeError`      | Attribute/method doesn't exist           | `"abc".append()` |
| `ZeroDivisionError`   | Division by zero                         | `10 / 0`         |
| `ModuleNotFoundError` | Module cannot be found                   | invalid import   |
| `FileNotFoundError`   | Requested file doesn't exist             | `open(...)`      |

---

# 6️⃣ `IndexError`

```python
numbers = [10, 20, 30]

print(numbers[10])
```

Valid indexes:

```text
0 → 10
1 → 20
2 → 30
```

But:

```text
10 ❌
```

Therefore:

```text
IndexError
```

Handle:

```python
try:
    numbers = [10, 20, 30]
    print(numbers[10])

except IndexError:
    print("Invalid index")
```

---

# 7️⃣ `KeyError`

```python
student = {
    "name": "Ramesh"
}

print(student["age"])
```

`age` doesn't exist.

Therefore:

```text
KeyError
```

Handle:

```python
try:
    print(student["age"])

except KeyError:
    print("Key not found")
```

---

# 8️⃣ `TypeError`

```python
print(10 + "20")
```

Python cannot directly add:

```text
integer + string
```

Therefore:

```text
TypeError
```

Handle:

```python
try:
    print(10 + "20")

except TypeError:
    print("Invalid data types")
```

---

# 9️⃣ `ValueError`

```python
age = int("twenty")
```

`int()` expects a value that can be converted to an integer.

But:

```text
"twenty"
```

cannot be converted.

Therefore:

```text
ValueError
```

Example:

```python
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Enter numbers only")
```

---

# 🔟 `NameError`

```python
a = 10

print(A)
```

Python is case-sensitive:

```text
a ≠ A
```

Therefore:

```text
NameError
```

---

# 1️⃣1️⃣ `AttributeError`

Example:

```python
name = "Python"

name.append("A")
```

Strings don't have:

```python
append()
```

Therefore:

```text
AttributeError
```

---

# 1️⃣2️⃣ `ZeroDivisionError`

```python
print(20 / 0)
```

Output:

```text
ZeroDivisionError
```

Handle:

```python
try:
    print(20 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 1️⃣3️⃣ `try` Block 🧪

## Definition

The `try` block contains code that **may produce an exception**.

### Syntax

```python
try:
    risky_code
```

Example:

```python
try:
    number = int(input("Enter number: "))
```

Remember:

```text
try
 ↓
"Try executing this code"
```

---

# 1️⃣4️⃣ `except` Block 🛡️

## Definition

The `except` block handles an exception raised from the corresponding `try` block.

### Syntax

```python
try:
    risky_code

except ExceptionType:
    handling_code
```

Example:

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Division by zero is not allowed")
```

---

# 1️⃣5️⃣ Flow of `try-except` ⭐

```text
                 try
                  │
          ┌───────┴───────┐
          │               │
     No Exception      Exception 🚨
          │               │
          ▼               ▼
   continue try       stop remaining
      block            try statements
          │               │
          │               ▼
          │            except
          │               │
          └───────┬───────┘
                  ▼
              Continue
```

---

# 1️⃣6️⃣ Important Interview Trap ⚠️

What is the output?

```python
try:

    print("A")

    print(10 / 0)

    print("B")

except ZeroDivisionError:

    print("C")
```

### Answer

```text
A
C
```

Why isn't `B` printed?

Because once an exception occurs inside `try`, Python leaves the remaining statements in that `try` block and searches for a matching handler.

```text
print("A")      ✅
      ↓
10 / 0          🚨
      ↓
print("B")      ❌ skipped
      ↓
except
      ↓
print("C")      ✅
```

---

# 1️⃣7️⃣ Specific Exception Handling ⭐

Instead of:

```python
except:
```

we can write:

```python
except ZeroDivisionError:
```

Example:

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

This makes the expected error clearer.

---

# 1️⃣8️⃣ Multiple `except` Blocks

### Syntax

```python
try:
    risky_code

except NameError:
    ...

except IndexError:
    ...

except ZeroDivisionError:
    ...
```

Example:

```python
try:

    numbers = [10, 20, 30]

    print(numbers[10])

except NameError:
    print("Variable not found")

except IndexError:
    print("Invalid index")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Which exception occurs?

```text
IndexError
```

Therefore:

```python
except IndexError:
```

executes.

---

# 1️⃣9️⃣ Why Doesn't Python Execute Every `except`?

Because Python handles the exception using the matching handler.

Conceptually:

```text
Exception occurs
      ↓
What type?
      ↓
IndexError
      ↓
Check except NameError ❌
      ↓
Check except IndexError ✅
      ↓
Execute it
```

---

# 2️⃣0️⃣ `Exception as e` ⭐

Very common interview syntax:

```python
try:
    age = int("twenty")

except Exception as e:
    print(e)
```

Output resembles:

```text
invalid literal for int() with base 10: 'twenty'
```

---

# 2️⃣1️⃣ What is `e`? 🧠

`e` refers to the caught exception object.

Conceptually:

```text
Exception occurs
      ↓
ValueError object
      ↓
      e
```

So:

```python
print(e)
```

prints its message.

This connects exception handling with OOP:

> Exceptions are objects.

---

# 2️⃣2️⃣ `else` Block ✅

## Definition

The `else` block executes when the `try` block completes **without an exception**.

### Syntax

```python
try:
    risky_code

except Exception:
    error_code

else:
    success_code
```

Example:

```python
try:

    age = int("25")

except ValueError:

    print("Invalid age")

else:

    print("Age:", age)
```

Output:

```text
Age: 25
```

---

# 2️⃣3️⃣ When Does `else` NOT Execute?

```python
try:

    age = int("twenty")

except ValueError:

    print("Invalid age")

else:

    print(age)
```

Output:

```text
Invalid age
```

`else` is skipped.

Remember:

```text
try success
     ↓
    else ✅


try exception
     ↓
   except ✅
     ↓
    else ❌
```

---

# 2️⃣4️⃣ `finally` Block 🔄

## Definition

The `finally` block is intended for code that should execute regardless of whether an exception occurred.

Common uses:

```text
📁 File cleanup
🗄️ Database connection cleanup
🔌 Resource release
🧹 Cleanup operations
```

### Syntax

```python
try:
    ...

except:
    ...

finally:
    ...
```

---

# 2️⃣5️⃣ `finally` Example

```python
try:

    print(10 / 0)

except ZeroDivisionError:

    print("Error")

finally:

    print("Finished")
```

Output:

```text
Error
Finished
```

---

# 2️⃣6️⃣ `try-except-else-finally` ⭐

### Complete Syntax

```python
try:
    # risky code

except ExceptionType:
    # handle exception

else:
    # executes if try succeeds

finally:
    # cleanup / executes regardless
```

Easy memory:

```text
🧪 try
"Try this"

🛡️ except
"Handle problem"

✅ else
"Everything succeeded"

🔄 finally
"Do cleanup"
```

---

# 2️⃣7️⃣ Output Interview Question

What is the output?

```python
try:

    print("Python")

except:

    print("Error")

else:

    print("Success")

finally:

    print("End")
```

### Answer

```text
Python
Success
End
```

Why?

```text
try      ✅
except   ❌
else     ✅
finally  ✅
```

---

# 2️⃣8️⃣ Another Output Question

```python
try:

    print(10 / 0)

except ZeroDivisionError:

    print("Zero Error")

else:

    print("Success")

finally:

    print("End")
```

Output:

```text
Zero Error
End
```

Flow:

```text
try      🚨
except   ✅
else     ❌
finally  ✅
```

---

# 2️⃣9️⃣ `raise` Keyword 🚨

## Definition

`raise` is used to **explicitly signal an exception**.

### Syntax

```python
raise Exception("Error message")
```

Example:

```python
age = 15

if age < 18:

    raise Exception(
        "Age must be 18 or above"
    )
```

---

# 3️⃣0️⃣ Why `raise` Is Important in OOP

Python knows:

```python
10 / 0
```

is invalid.

But Python doesn't automatically know your business rules such as:

```text
Withdraw ₹10,000
when balance is ₹5,000
```

So your class can decide:

```python
if amount > self.balance:

    raise Exception(
        "Insufficient Balance"
    )
```

---

# 3️⃣1️⃣ `print()` vs `raise` ⭐

| `print()`                    | `raise`                             |
| ---------------------------- | ----------------------------------- |
| Displays information         | Signals an exception                |
| Normal output                | Changes exception flow              |
| Cannot be caught by `except` | Can be handled by matching `except` |

Example:

```python
print("Insufficient Balance")
```

only displays the message.

Whereas:

```python
raise Exception(
    "Insufficient Balance"
)
```

signals an exceptional condition.

---

# 3️⃣2️⃣ Custom Exception 🧬

## Definition

A **custom exception is a programmer-defined exception class used to represent application-specific errors.**

### Syntax

```python
class CustomException(Exception):
    pass
```

Example:

```python
class BankException(Exception):
    pass
```

OOP concept:

```text
Exception
    │
    │ inheritance
    ▼
BankException
```

---

# 3️⃣3️⃣ Raising Custom Exception

```python
raise BankException(
    "Insufficient Balance"
)
```

Handling:

```python
try:

    raise BankException(
        "Insufficient Balance"
    )

except BankException as e:

    print(e)
```

Output:

```text
Insufficient Balance
```

---

# 3️⃣4️⃣ Custom Exception with `__init__`

```python
class BankException(Exception):

    def __init__(self, message):

        super().__init__(message)
```

Here:

```text
BankException
     ↓
Child Class

Exception
     ↓
Parent Class
```

And:

```python
super().__init__(message)
```

passes the message to inherited exception initialization.

---

# 3️⃣5️⃣ Important OOP Connection ⭐

Exception handling connects to several OOP ideas:

```text
Exception
   │
   │ inheritance
   ▼
BankException
   │
   │ instantiate
   ▼
BankException("Error")
   │
   ▼
Exception Object
   │
   │ raise
   ▼
🚨 signaled
   │
   ▼
except BankException as e
   │
   ▼
e refers to caught object
```

---

# 3️⃣6️⃣ Interview Bank Example 🏦

```python
class BankException(Exception):
    pass


class Bank:

    def __init__(self, balance):

        self.balance = balance

    def withdraw(self, amount):

        if amount <= 0:

            raise BankException(
                "Invalid Amount"
            )

        if amount > self.balance:

            raise BankException(
                "Insufficient Balance"
            )

        self.balance -= amount
```

Object:

```python
account = Bank(5000)
```

Test:

```python
try:

    account.withdraw(10000)

except BankException as e:

    print(e)
```

Output:

```text
Insufficient Balance
```

---

# 3️⃣7️⃣ Dry Run ⭐

Initial:

```text
balance = 5000
```

Call:

```text
withdraw(10000)
```

First condition:

```text
10000 <= 0
↓
False
```

Second:

```text
10000 > 5000
↓
True
```

Then:

```text
BankException("Insufficient Balance")
             ↓
       exception object
             ↓
           raise
             ↓
except BankException as e
             ↓
          print(e)
             ↓
Insufficient Balance
```

---

# 3️⃣8️⃣ Why Specific Exceptions First? ⚠️

Suppose:

```python
class BankException(Exception):
    pass
```

Then `BankException` is a child of `Exception`.

Prefer:

```python
try:
    ...

except BankException:
    ...

except Exception:
    ...
```

Think:

```text
Specific
   ↓
General
```

---

# 3️⃣9️⃣ Common Interview Mistakes ❌

### ❌ Mistake 1

Using a bare `except` everywhere:

```python
except:
```

Better when possible:

```python
except ValueError:
```

---

### ❌ Mistake 2

Raising a string:

```python
raise "Error"
```

Wrong.

Use:

```python
raise Exception("Error")
```

---

### ❌ Mistake 3

Custom class not inheriting from an exception base:

```python
class BankException:
    pass
```

Correct:

```python
class BankException(Exception):
    pass
```

---

### ❌ Mistake 4

Thinking `else` always executes.

No.

```text
No exception → else ✅
Exception    → else ❌
```

---

### ❌ Mistake 5

Thinking execution continues with the next line inside `try` after an exception is handled.

Example:

```python
try:

    print("A")
    print(10 / 0)
    print("B")

except:
    print("C")
```

`B` is skipped.

---

# 4️⃣0️⃣ Top Interview Questions & Answers 🎤

### Q1. What is an exception?

An exception is an abnormal runtime condition that interrupts the normal execution flow of a program.

### Q2. What is exception handling?

It is the process of handling runtime exceptions using constructs such as `try` and `except`.

### Q3. What is `try`?

It contains code that may raise an exception.

### Q4. What is `except`?

It handles a matching exception.

### Q5. Can Python have multiple `except` blocks?

Yes.

### Q6. What is `else`?

It executes if the `try` block completes without an exception.

### Q7. What is `finally`?

It is used for code that should run regardless of whether an exception occurs, commonly cleanup.

### Q8. What is `raise`?

It explicitly signals an exception.

### Q9. What is a custom exception?

A programmer-defined exception class for application-specific errors.

### Q10. Which OOP concept is used by custom exceptions?

**Inheritance.**

### Q11. What is `Exception as e`?

`e` refers to the caught exception object.

### Q12. Can custom exceptions contain methods?

Yes.

### Q13. Why use specific exceptions?

They make error handling clearer and allow different problems to be handled differently.

### Q14. What happens after an exception occurs inside `try`?

The remaining statements in that `try` block are skipped and Python looks for a matching exception handler.

### Q15. Can `Exception` catch a custom exception?

Yes, if the custom exception inherits from `Exception`.

---

# 4️⃣1️⃣ Difference Table — Interview Revision ⭐

| Topic            | Meaning                           |
| ---------------- | --------------------------------- |
| `try`            | Contains risky code               |
| `except`         | Handles exceptions                |
| `else`           | Runs when `try` succeeds          |
| `finally`        | Runs for cleanup regardless       |
| `raise`          | Explicitly signals an exception   |
| `Exception as e` | Captures the exception object     |
| Custom Exception | Programmer-defined exception type |

---

# 4️⃣2️⃣ MCQs 📝

### Q1. Which keyword handles exceptions?

A. `raise`
B. `except` ✅
C. `return`
D. `yield`

### Q2. Which keyword explicitly signals an exception?

A. `try`
B. `except`
C. `raise` ✅
D. `else`

### Q3. When does `else` execute?

A. Always
B. When `try` succeeds ✅
C. Only when an exception occurs
D. Before `try`

### Q4. Which is commonly used for cleanup?

A. `else`
B. `finally` ✅
C. `raise`
D. `yield`

### Q5. What error occurs here?

```python
print(10 / 0)
```

A. `ValueError`
B. `TypeError`
C. `ZeroDivisionError` ✅
D. `IndexError`

### Q6. What error occurs here?

```python
int("python")
```

A. `ValueError` ✅
B. `IndexError`
C. `KeyError`
D. `NameError`

### Q7. What error occurs here?

```python
numbers = [10, 20]

print(numbers[20])
```

A. `IndexError` ✅
B. `ValueError`
C. `NameError`
D. `KeyError`

### Q8. Which is correct?

```python
class BankException(Exception):
    pass
```

A. Encapsulation
B. Exception inheritance ✅
C. Looping
D. Generator

---

# 4️⃣3️⃣ Output Challenge 🧠

Try to answer before reading the solution.

```python
try:

    print("1")

    print(20 / 0)

    print("2")

except ZeroDivisionError:

    print("3")

else:

    print("4")

finally:

    print("5")
```

### Think 🤔

Which lines execute?

### Answer

```text
1
3
5
```

Why?

```text
print("1")       ✅

20 / 0           🚨

print("2")       ❌

except            ✅
print("3")       ✅

else              ❌

finally           ✅
print("5")       ✅
```

---

# 4️⃣4️⃣ Coding Challenge 💻

Create:

```python
class AgeException(Exception):
    pass
```

Then create:

```python
class Student:
```

Requirements:

```text
name
age
marks
```

Validation:

```text
age < 0
    ↓
AgeException


marks < 0 or marks > 100
    ↓
MarksException
```

Then handle using:

```text
try
except AgeException
except MarksException
else
finally
```

### 🎯 Don't look for the answer yet.

Try building it yourself.

---

# 🏆 CHAPTER 12 — FINAL INTERVIEW CHEAT SHEET

Remember this diagram:

```text
                  EXCEPTION HANDLING
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
Built-in Errors       Handling       Custom Errors
       │                 │                 │
       ▼                 ▼                 ▼
ValueError             try             Exception
TypeError              except              │
IndexError             else                │
KeyError               finally             ▼
NameError              raise        BankException
ZeroDivisionError                         │
                                         ▼
                                      OOP
                                  Inheritance
```

## 🔑 Seven Things You Must Remember

```text
1️⃣ try
   → risky code

2️⃣ except
   → handles matching exception

3️⃣ else
   → executes when try succeeds

4️⃣ finally
   → cleanup / runs regardless

5️⃣ raise
   → explicitly signals an exception

6️⃣ Exception as e
   → e refers to the caught exception object

7️⃣ Custom Exception
   → application-specific exception class
```

### ⭐ Interview Formula

```text
try
 ↓
Run risky code
 ↓
Exception?
 │
 ├── YES → except 🛡️
 │
 └── NO  → else ✅
              │
              ▼
          finally 🔄
```

### 🧠 OOP Formula

```text
Exception
    │
    │ Inheritance
    ▼
BankException
    │
    ▼
BankException("Error")
    │
    ▼
Exception Object
    │
    ▼
raise 🚨
    │
    ▼
except BankException as e
    │
    ▼
Handle 🛡️
```

## 🎯 One-Minute Interview Revision

> **Exception handling manages runtime errors in Python. `try` contains risky code, `except` handles errors, `else` runs when no exception occurs, `finally` is commonly used for cleanup, and `raise` explicitly signals an exception. Python provides built-in exceptions such as `ValueError`, `TypeError`, `IndexError`, and `ZeroDivisionError`. We can also create custom exception classes by inheriting from `Exception`, which connects exception handling with OOP inheritance.**

### 📚 Your Exception Handling Chapter Path

```text
CHAPTER 1 → Errors & Exceptions
     ↓
CHAPTER 2 → try-except
     ↓
CHAPTER 3 → Specific Exceptions
     ↓
CHAPTER 4 → Multiple except
     ↓
CHAPTER 5 → Exception as e
     ↓
CHAPTER 6 → else
     ↓
CHAPTER 7 → finally
     ↓
CHAPTER 8 → File Handling + Exceptions
     ↓
CHAPTER 9 → raise
     ↓
CHAPTER 10 → Custom Exceptions + OOP
     ↓
CHAPTER 11 → Real-Time OOP Project
     ↓
CHAPTER 12 → Interview Preparation 🏆
```

**Next: 📘 Chapter 13 — Exception Handling Practice Lab** — programs from **very easy → easy → medium → real-time → interview-level**, with logic-building steps, dry runs, expected outputs, debugging exercises, and coding challenges.
===
# 📘 CHAPTER 13 — EXCEPTION HANDLING PRACTICE LAB

This chapter is for **logic building + coding practice**. We’ll start very easy and gradually move toward **OOP and interview-level programs**.

## 🧪 Level 1 — Very Easy

### Program 1: Handle `ZeroDivisionError`

### 🎯 Problem

Take two numbers and divide them. If the second number is `0`, handle the error.

### 💡 Logic

```text
START
  ↓
Take a
  ↓
Take b
  ↓
Try a / b
  ↓
Is b = 0?
 ┌──────┴──────┐
YES            NO
 ↓              ↓
Exception      Division
 ↓              ↓
except         Result
  └──────┬──────┘
         ↓
        END
```

### 💻 Program

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 🔍 Dry Run

Input:

```text
a = 20
b = 0
```

Python executes:

```python
result = 20 / 0
```

🚨 `ZeroDivisionError` occurs.

Python jumps to:

```python
except ZeroDivisionError:
```

Output:

```text
Cannot divide by zero
```

---

# 🧪 Program 2 — Handle `ValueError`

### 🎯 Problem

Ask the user to enter their age.

If they enter:

```text
25
```

accept it.

If they enter:

```text
twenty
```

handle the error.

### 💻 Program

```python
try:
    age = int(input("Enter your age: "))

    print("Your age is:", age)

except ValueError:
    print("Please enter numbers only")
```

### 🔍 Dry Run

Input:

```text
twenty
```

Python tries:

```python
int("twenty")
```

🚨 `ValueError`

Therefore:

```text
Please enter numbers only
```

### ⭐ Interview Point

`ValueError` occurs when the operation accepts the type of value supplied, but the actual value is inappropriate for that operation.

---

# 🧪 Program 3 — Handle `IndexError`

### 🎯 Problem

Access an element from a list.

```python
numbers = [10, 20, 30]
```

Valid indexes:

```text
0 → 10
1 → 20
2 → 30
```

### 💻 Program

```python
numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))

    print(numbers[index])

except IndexError:
    print("Index does not exist")
```

### Example

Input:

```text
10
```

Python executes:

```python
numbers[10]
```

🚨 `IndexError`

Output:

```text
Index does not exist
```

---

# 🧪 Program 4 — Handle `KeyError`

### 🎯 Problem

Access dictionary data safely.

```python
student = {
    "name": "Ramesh",
    "age": 30
}
```

### 💻 Program

```python
student = {
    "name": "Ramesh",
    "age": 30
}

try:
    key = input("Enter key: ")

    print(student[key])

except KeyError:
    print("Key does not exist")
```

### Dry Run

Input:

```text
salary
```

Python tries:

```python
student["salary"]
```

But `salary` doesn't exist.

🚨 `KeyError`

Output:

```text
Key does not exist
```

---

# 🧪 Program 5 — Multiple Exceptions

Now let's combine concepts.

### 🎯 Problem

Take two numbers and divide them.

Possible problems:

```text
"abc" → ValueError

0 as divisor → ZeroDivisionError
```

### 💻 Program

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 🧠 Flow

```text
             INPUT
               ↓
         Convert to int
               ↓
        ┌──────┴──────┐
        │             │
   invalid text      valid
        │             │
        ▼             ▼
   ValueError       a / b
                      ↓
                  Is b zero?
                  ┌───┴───┐
                 YES      NO
                  ↓        ↓
          ZeroDivision   Result
             Error
```

---

# 🧪 Program 6 — `else` Practice

### 🎯 Problem

Print `"Division Successful"` only when no exception occurs.

### 💻 Program

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
    print("Division Successful")
```

### Input

```text
20
4
```

Output:

```text
Result: 5.0
Division Successful
```

Remember:

```text
try successful
      ↓
    else ✅
```

---

# 🧪 Program 7 — `finally` Practice

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Finished")
```

### Case 1 — Success

Input:

```text
20
5
```

Output:

```text
4.0
Program Finished
```

### Case 2 — Error

Input:

```text
20
0
```

Output:

```text
Cannot divide by zero
Program Finished
```

So:

```text
Success → finally ✅

Error   → finally ✅
```

---

# 🧪 Level 2 — `raise` Practice

## Program 8 — Age Validation

### 🎯 Requirement

```text
age < 0
   ↓
Exception

age >= 0
   ↓
Valid Age
```

### 💻 Program

```python
age = int(input("Enter age: "))

if age < 0:
    raise Exception("Age cannot be negative")

print("Valid Age:", age)
```

Input:

```text
-20
```

Output:

```text
Exception: Age cannot be negative
```

---

# 🧪 Program 9 — Marks Validation

### 🎯 Rule

Marks must be:

```text
0 to 100
```

Invalid:

```text
-10 ❌
120 ❌
```

Valid:

```text
0   ✅
35  ✅
90  ✅
100 ✅
```

### 💻 Program

```python
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    raise Exception("Marks must be between 0 and 100")

print("Marks:", marks)
```

### 🧠 Important Condition

```python
marks < 0 or marks > 100
```

Think:

```text
       marks
         │
    ┌────┴────┐
    ▼         ▼
 below 0?   above 100?
    │         │
    └────┬────┘
         ↓
Either True?
         ↓
      Invalid
```

---

# 🧪 Level 3 — Custom Exception

## Program 10 — `AgeException`

Instead of:

```python
raise Exception(...)
```

create our own exception.

### Step 1 — Create Exception Class

```python
class AgeException(Exception):
    pass
```

### Step 2 — Raise It

```python
age = int(input("Enter age: "))

if age < 0:
    raise AgeException(
        "Age cannot be negative"
    )

print("Valid Age:", age)
```

### Step 3 — Handle It

```python
class AgeException(Exception):
    pass


try:
    age = int(input("Enter age: "))

    if age < 0:
        raise AgeException(
            "Age cannot be negative"
        )

except AgeException as e:
    print("Age Error:", e)

else:
    print("Valid Age:", age)

finally:
    print("Validation Completed")
```

---

# 🔍 Dry Run — `AgeException`

Input:

```text
-25
```

Step 1:

```python
age = -25
```

Step 2:

```python
age < 0
```

becomes:

```text
-25 < 0
   ↓
 True
```

Step 3:

```python
raise AgeException(
    "Age cannot be negative"
)
```

Step 4:

Python finds:

```python
except AgeException as e:
```

Step 5:

```python
print("Age Error:", e)
```

Output:

```text
Age Error: Age cannot be negative
Validation Completed
```

`else` doesn't execute because an exception occurred.

---

# 🧪 Level 4 — OOP + Custom Exception

## Program 11 — Student Validation 🎓

Now we combine:

```text
🏗️ Class
🔧 Constructor
👤 self
🧬 Custom Exception
🚨 raise
🧪 try
🛡️ except
✅ else
🔄 finally
```

### Requirements

Student has:

```text
name
age
marks
```

Rules:

```text
age < 0
   ↓
AgeException

marks < 0 OR marks > 100
   ↓
MarksException
```

---

## Step 1 — Custom Exceptions

```python
class AgeException(Exception):
    pass


class MarksException(Exception):
    pass
```

---

## Step 2 — Student Class

```python
class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks
```

Object:

```python
student = Student(
    "Ramesh",
    25,
    90
)
```

Memory concept:

```text
student
   │
   ▼
┌──────────────────────┐
│ Student Object       │
├──────────────────────┤
│ name  = "Ramesh"     │
│ age   = 25           │
│ marks = 90           │
└──────────────────────┘
```

---

# Add Validation Method

```python
class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

    def validate(self):

        if self.age < 0:
            raise AgeException(
                "Age cannot be negative"
            )

        if self.marks < 0 or self.marks > 100:
            raise MarksException(
                "Marks must be between 0 and 100"
            )
```

---

# Add Display Method

```python
def display(self):

    print("Name :", self.name)
    print("Age  :", self.age)
    print("Marks:", self.marks)
```

Complete class:

```python
class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

    def validate(self):

        if self.age < 0:
            raise AgeException(
                "Age cannot be negative"
            )

        if self.marks < 0 or self.marks > 100:
            raise MarksException(
                "Marks must be between 0 and 100"
            )

    def display(self):

        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)
```

---

# Complete Program ⭐

```python
# ==========================================
# CUSTOM EXCEPTIONS
# ==========================================

class AgeException(Exception):
    pass


class MarksException(Exception):
    pass


# ==========================================
# STUDENT CLASS
# ==========================================

class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

    def validate(self):

        if self.age < 0:
            raise AgeException(
                "Age cannot be negative"
            )

        if self.marks < 0 or self.marks > 100:
            raise MarksException(
                "Marks must be between 0 and 100"
            )

    def display(self):

        print("Name  :", self.name)
        print("Age   :", self.age)
        print("Marks :", self.marks)


# ==========================================
# OBJECT
# ==========================================

student = Student(
    "Ramesh",
    25,
    90
)


# ==========================================
# EXCEPTION HANDLING
# ==========================================

try:

    student.validate()

except AgeException as e:

    print("Age Error:", e)

except MarksException as e:

    print("Marks Error:", e)

else:

    print("Student Data is Valid")

    student.display()

finally:

    print("Validation Completed")
```

Output:

```text
Student Data is Valid
Name  : Ramesh
Age   : 25
Marks : 90
Validation Completed
```

---

# 🧠 Logic-Building Formula

When you're given an exception-handling program in an interview, **don't immediately start coding**.

Think in this order:

```text
1️⃣ What data do I need?

        ↓

2️⃣ What can go wrong?

        ↓

3️⃣ Which conditions detect those problems?

        ↓

4️⃣ Which exception should represent each problem?

        ↓

5️⃣ Where should I raise it?

        ↓

6️⃣ Where should I catch it?

        ↓

7️⃣ What happens when everything succeeds?
```

For the Student program:

```text
DATA
 ↓
name, age, marks

PROBLEMS
 ↓
negative age
invalid marks

CONDITIONS
 ↓
age < 0
marks < 0 or marks > 100

EXCEPTIONS
 ↓
AgeException
MarksException

SIGNAL
 ↓
raise

HANDLE
 ↓
except

SUCCESS
 ↓
else

FINISH
 ↓
finally
```

# 🎯 Practice Before the Next Level

Try these yourself:

1. 👤 **Age Validator** — reject age below `0`.
2. 🎓 **Marks Validator** — allow only `0–100`.
3. 💰 **Salary Validator** — reject salary `<= 0`.
4. 🏦 **ATM Withdrawal** — reject negative amount and insufficient balance.
5. 🔐 **Login System** — raise `LoginException` for incorrect password.
6. 📱 **Device Security** — raise `SecurityException` for an unregistered device.
7. 🛒 **Shopping System** — raise `StockException` when requested quantity exceeds stock.
8. 👨‍💼 **Employee System** — validate employee age and salary.

## 🏆 Chapter 13 — Part 1 Summary

```text
Built-in Exceptions
        ↓
try + except
        ↓
Multiple except
        ↓
else
        ↓
finally
        ↓
raise
        ↓
Custom Exception
        ↓
OOP Class
        ↓
Business Validation
        ↓
Real-Time Program
```

The key idea is:

> **Your class contains the business logic, `raise` signals invalid situations, and `try-except` handles those situations.**

**Next in Chapter 13:** 🔥 **Part 2 — ATM, Login, Employee, Shopping Cart and Google Security practice programs**, with step-by-step logic, flow diagrams, dry runs, mistakes, and interview coding questions.
===# 📘 CHAPTER 13 — PART 2

# 🔥 REAL-TIME OOP + EXCEPTION HANDLING PRACTICE

Now we move from basic examples to **real-time programs**.

We will practice:

```text
🏧 ATM System
🔐 Login System
👨‍💼 Employee System
🛒 Shopping / Stock System
📱 Device Security System
```

For each program, focus on this thinking pattern:

```text
Data
  ↓
Business Rule
  ↓
Condition
  ↓
Custom Exception
  ↓
raise
  ↓
try
  ↓
except
```

---

# 1️⃣ ATM WITHDRAWAL SYSTEM 🏧

## ✅ Definition

An ATM withdrawal system allows a user to withdraw money from an account.

Before withdrawing, we need to validate:

```text
💰 Is amount positive?
💰 Is sufficient balance available?
```

---

# 2️⃣ Why Do We Need Exceptions Here? 🤔

Suppose:

```text
Account Balance = ₹5,000
```

User tries:

```text
Withdraw ₹10,000
```

We should not allow:

```text
5000 - 10000 = -5000 ❌
```

Instead:

```text
Requested amount > Balance
            ↓
BalanceException 🚨
```

We also shouldn't allow:

```text
withdraw(-1000) ❌
withdraw(0)     ❌
```

So we need another exception:

```text
Invalid Amount
      ↓
AmountException 🚨
```

---

# 3️⃣ Custom Exceptions 🧬

### Syntax

```python
class AmountException(Exception):
    pass


class BalanceException(Exception):
    pass
```

### OOP Concept

Both classes inherit from Python's `Exception` class.

```text
               Exception
                   │
           ┌───────┴────────┐
           ▼                ▼
 AmountException      BalanceException
```

This is **inheritance**.

---

# 4️⃣ ATM Class 🏧

```python
class ATM:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance
```

Create object:

```python
account = ATM("Ramesh", 5000)
```

Conceptually:

```text
account
   │
   ▼
┌─────────────────────┐
│ ATM Object          │
├─────────────────────┤
│ name = "Ramesh"     │
│ balance = 5000      │
└─────────────────────┘
```

---

# 5️⃣ Add `withdraw()` Method

```python
def withdraw(self, amount):

    if amount <= 0:
        raise AmountException(
            "Enter a positive amount"
        )

    if amount > self.balance:
        raise BalanceException(
            "Insufficient Balance"
        )

    self.balance -= amount
```

---

# 6️⃣ Understand the Logic 🧠

Three possibilities exist.

```text
              withdraw(amount)
                     │
                     ▼
              amount <= 0 ?
              /          \
           YES            NO
            │              │
            ▼              ▼
 AmountException     amount > balance?
                      /           \
                    YES            NO
                     │              │
                     ▼              ▼
            BalanceException    Withdraw
```

---

# 7️⃣ Valid Withdrawal — Dry Run 🔍

Balance:

```text
5000
```

Call:

```python
account.withdraw(2000)
```

### Step 1

```text
amount = 2000
```

### Step 2

```python
amount <= 0
```

becomes:

```text
2000 <= 0
   ↓
False
```

Continue.

### Step 3

```python
amount > self.balance
```

becomes:

```text
2000 > 5000
   ↓
False
```

Continue.

### Step 4

```python
self.balance -= amount
```

means:

```text
5000 - 2000
     ↓
3000
```

Final balance:

```text
₹3000
```

---

# 8️⃣ Invalid Withdrawal — Dry Run 🚨

Balance:

```text
5000
```

Call:

```python
account.withdraw(10000)
```

Check:

```text
10000 <= 0
      ↓
False
```

Next:

```text
10000 > 5000
      ↓
True
```

Therefore:

```python
raise BalanceException(
    "Insufficient Balance"
)
```

Python signals the exception.

---

# 9️⃣ Complete ATM Program ⭐

```python
# ==========================================
# CUSTOM EXCEPTIONS
# ==========================================

class AmountException(Exception):
    pass


class BalanceException(Exception):
    pass


# ==========================================
# ATM CLASS
# ==========================================

class ATM:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def view_balance(self):

        print(
            "Current Balance:",
            self.balance
        )

    def withdraw(self, amount):

        if amount <= 0:
            raise AmountException(
                "Enter a positive amount"
            )

        if amount > self.balance:
            raise BalanceException(
                "Insufficient Balance"
            )

        self.balance -= amount

        print(
            "Withdrawal Successful:",
            amount
        )


# ==========================================
# OBJECT
# ==========================================

account = ATM("Ramesh", 5000)


# ==========================================
# EXCEPTION HANDLING
# ==========================================

try:

    account.withdraw(2000)

except AmountException as e:

    print("Amount Error:", e)

except BalanceException as e:

    print("Balance Error:", e)

else:

    account.view_balance()

finally:

    print("ATM Transaction Completed")
```

### Output

```text
Withdrawal Successful: 2000
Current Balance: 3000
ATM Transaction Completed
```

---

# 🔟 INTERVIEW QUESTION 🎤

### Q: Why create two custom exceptions?

Because there are two different business problems:

```text
AmountException
→ amount itself is invalid

BalanceException
→ amount is valid, but balance is insufficient
```

This makes the program easier to understand and handle.

---

# 1️⃣1️⃣ LOGIN SYSTEM 🔐

Now let's create an OOP login system.

## Requirements

Store:

```text
📧 email
🔑 password
```

Validate:

```text
Correct Email + Correct Password
            ↓
      Login Successful


Wrong Email/Password
            ↓
      LoginException
```

---

# 1️⃣2️⃣ Create `LoginException`

```python
class LoginException(Exception):
    pass
```

Inheritance:

```text
Exception
    │
    ▼
LoginException
```

---

# 1️⃣3️⃣ Create User Class

```python
class User:

    def __init__(self, email, password):

        self.email = email
        self.password = password
```

Object:

```python
user = User(
    "ramesh@gmail.com",
    1234
)
```

Memory concept:

```text
user
 │
 ▼
┌──────────────────────────┐
│ User Object              │
├──────────────────────────┤
│ email = ramesh@gmail.com │
│ password = 1234          │
└──────────────────────────┘
```

---

# 1️⃣4️⃣ Login Method

```python
def login(self, email, password):

    if email != self.email:
        raise LoginException(
            "Invalid Email"
        )

    if password != self.password:
        raise LoginException(
            "Invalid Password"
        )

    print("Login Successful")
```

---

# 1️⃣5️⃣ Flow Diagram

```text
             login()
                │
                ▼
        Email Correct?
          /          \
        NO            YES
        │              │
        ▼              ▼
 LoginException   Password Correct?
                    /        \
                  NO          YES
                  │            │
                  ▼            ▼
           LoginException   SUCCESS ✅
```

---

# 1️⃣6️⃣ Login Dry Run

Stored:

```text
email    = ramesh@gmail.com
password = 1234
```

Call:

```python
user.login(
    "ramesh@gmail.com",
    9999
)
```

Email check:

```text
ramesh@gmail.com != ramesh@gmail.com
               ↓
             False
```

Continue.

Password:

```text
9999 != 1234
     ↓
    True
```

Therefore:

```python
raise LoginException(
    "Invalid Password"
)
```

---

# 1️⃣7️⃣ Complete Login Program

```python
class LoginException(Exception):
    pass


class User:

    def __init__(self, email, password):

        self.email = email
        self.password = password

    def login(self, email, password):

        if email != self.email:
            raise LoginException(
                "Invalid Email"
            )

        if password != self.password:
            raise LoginException(
                "Invalid Password"
            )

        print("Login Successful")


user = User(
    "ramesh@gmail.com",
    1234
)


try:

    user.login(
        "ramesh@gmail.com",
        1234
    )

except LoginException as e:

    print("Login Error:", e)

else:

    print("Welcome User")

finally:

    print("Login Process Completed")
```

Output:

```text
Login Successful
Welcome User
Login Process Completed
```

---

# 1️⃣8️⃣ EMPLOYEE SALARY SYSTEM 👨‍💼

## Requirements

Employee:

```text
name
age
salary
```

Rules:

```text
age < 18
   ↓
AgeException


salary <= 0
   ↓
SalaryException
```

---

# 1️⃣9️⃣ Custom Exceptions

```python
class AgeException(Exception):
    pass


class SalaryException(Exception):
    pass
```

---

# 2️⃣0️⃣ Employee Class

```python
class Employee:

    def __init__(self, name, age, salary):

        self.name = name
        self.age = age
        self.salary = salary

    def validate(self):

        if self.age < 18:
            raise AgeException(
                "Employee age must be 18 or above"
            )

        if self.salary <= 0:
            raise SalaryException(
                "Salary must be positive"
            )

    def display(self):

        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Salary :", self.salary)
```

---

# 2️⃣1️⃣ Complete Employee Program

```python
class AgeException(Exception):
    pass


class SalaryException(Exception):
    pass


class Employee:

    def __init__(self, name, age, salary):

        self.name = name
        self.age = age
        self.salary = salary

    def validate(self):

        if self.age < 18:
            raise AgeException(
                "Employee age must be 18 or above"
            )

        if self.salary <= 0:
            raise SalaryException(
                "Salary must be positive"
            )

    def display(self):

        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Salary :", self.salary)


employee = Employee(
    "Rahul",
    25,
    50000
)


try:

    employee.validate()

except AgeException as e:

    print("Age Error:", e)

except SalaryException as e:

    print("Salary Error:", e)

else:

    print("Employee Data Valid")
    employee.display()

finally:

    print("Employee Validation Completed")
```

Output:

```text
Employee Data Valid
Name   : Rahul
Age    : 25
Salary : 50000
Employee Validation Completed
```

---

# 2️⃣2️⃣ SHOPPING STOCK SYSTEM 🛒

This is another useful real-time example.

Suppose:

```text
Product = Laptop
Stock   = 5
```

Customer wants:

```text
Quantity = 10
```

Problem:

```text
10 > 5
 ↓
Insufficient Stock
```

We can create:

```python
class StockException(Exception):
    pass
```

---

# 2️⃣3️⃣ Product Class

```python
class Product:

    def __init__(self, name, stock):

        self.name = name
        self.stock = stock
```

Object:

```python
product = Product(
    "Laptop",
    5
)
```

Memory:

```text
product
   │
   ▼
┌──────────────────┐
│ Product Object   │
├──────────────────┤
│ name = Laptop    │
│ stock = 5        │
└──────────────────┘
```

---

# 2️⃣4️⃣ Purchase Method

```python
def purchase(self, quantity):

    if quantity <= 0:
        raise StockException(
            "Quantity must be positive"
        )

    if quantity > self.stock:
        raise StockException(
            "Insufficient Stock"
        )

    self.stock -= quantity

    print("Purchase Successful")
```

---

# 2️⃣5️⃣ Dry Run

Stock:

```text
5
```

Purchase:

```text
2
```

Check:

```text
2 <= 0
 ↓
False
```

Next:

```text
2 > 5
 ↓
False
```

Update:

```text
5 - 2
 ↓
3
```

Remaining stock:

```text
3
```

---

# 2️⃣6️⃣ Complete Shopping Program

```python
class StockException(Exception):
    pass


class Product:

    def __init__(self, name, stock):

        self.name = name
        self.stock = stock

    def purchase(self, quantity):

        if quantity <= 0:
            raise StockException(
                "Quantity must be positive"
            )

        if quantity > self.stock:
            raise StockException(
                "Insufficient Stock"
            )

        self.stock -= quantity

        print(
            "Purchased Quantity:",
            quantity
        )

    def display_stock(self):

        print(
            "Remaining Stock:",
            self.stock
        )


product = Product(
    "Laptop",
    5
)


try:

    product.purchase(2)

except StockException as e:

    print("Stock Error:", e)

else:

    product.display_stock()

finally:

    print("Shopping Process Completed")
```

Output:

```text
Purchased Quantity: 2
Remaining Stock: 3
Shopping Process Completed
```

---

# 2️⃣7️⃣ DEVICE SECURITY SYSTEM 📱

This is based directly on the Google-style security example you studied.

We store:

```text
Email
Password
Registered Device
```

Example:

```text
Email    → ramesh@gmail.com
Password → 1234
Device   → mobile
```

If user tries:

```text
Device → laptop
```

we raise:

```text
SecurityException
```

---

# 2️⃣8️⃣ Security Exception

```python
class SecurityException(Exception):
    pass
```

---

# 2️⃣9️⃣ Google Class

```python
class Google:

    def __init__(
        self,
        email,
        password,
        device
    ):

        self.email = email
        self.password = password
        self.device = device
```

---

# 3️⃣0️⃣ Login Method

```python
def login(
    self,
    email,
    password,
    device
):

    if device != self.device:

        raise SecurityException(
            "Use registered device"
        )

    if (
        email == self.email
        and password == self.password
    ):

        print("Login Successful")
```

---

# 3️⃣1️⃣ Device Flow

```text
                  LOGIN
                    │
                    ▼
            Device Correct?
              /          \
            NO            YES
            │              │
            ▼              ▼
 SecurityException    Check Credentials
                           │
                      ┌────┴────┐
                      ▼         ▼
                    Valid     Invalid
                      │
                      ▼
                  Login ✅
```

---

# 3️⃣2️⃣ Custom Exception with Methods ⭐

Your earlier example also demonstrates that a custom exception is a **class**, so it can have methods.

```python
class SecurityException(Exception):

    def logout(self):
        print("Logout Successfully")

    def otp(self):
        print("Sending OTP...")
```

This is an important OOP connection.

---

# 3️⃣3️⃣ Complete Security Program

```python
import time


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

    def __init__(
        self,
        email,
        password,
        device
    ):

        self.email = email
        self.password = password
        self.device = device

    def login(
        self,
        email,
        password,
        device
    ):

        if device != self.device:

            raise SecurityException(
                "Please login using your registered device."
            )

        if (
            email == self.email
            and password == self.password
        ):

            print("Login Successful")


google = Google(
    "ramesh@gmail.com",
    1234,
    "mobile"
)


try:

    google.login(
        "ramesh@gmail.com",
        1234,
        "laptop"
    )

except SecurityException as e:

    print(e)

    e.logout()
    e.otp()
```

Output:

```text
Please login using your registered device.
Logout Successfully
Sending OTP...

[wait 3 seconds]

OTP Verified
```

---

# 3️⃣4️⃣ Why Can We Write `e.logout()`? 🧠

This is important.

We raised:

```python
raise SecurityException(
    "Please login using your registered device."
)
```

Python creates a:

```text
SecurityException Object
```

Then:

```python
except SecurityException as e:
```

makes `e` refer to that caught object.

Conceptually:

```text
SecurityException(...)
         │
         ▼
┌──────────────────────────┐
│ SecurityException Object │
├──────────────────────────┤
│ error message            │
├──────────────────────────┤
│ logout()                 │
│ otp()                    │
└──────────────────────────┘
         ▲
         │
         e
```

Therefore:

```python
e.logout()
```

calls the exception object's `logout()` method.

And:

```python
e.otp()
```

calls its `otp()` method.

This clearly shows:

> **Exceptions in Python are objects.**

---

# 3️⃣5️⃣ Important Difference Table ⭐

| Program        | Custom Exception    | Condition           |
| -------------- | ------------------- | ------------------- |
| 🏧 ATM         | `AmountException`   | `amount <= 0`       |
| 🏧 ATM         | `BalanceException`  | `amount > balance`  |
| 🔐 Login       | `LoginException`    | invalid credentials |
| 👨‍💼 Employee | `AgeException`      | `age < 18`          |
| 👨‍💼 Employee | `SalaryException`   | `salary <= 0`       |
| 🛒 Shopping    | `StockException`    | `quantity > stock`  |
| 📱 Security    | `SecurityException` | wrong device        |

---

# 3️⃣6️⃣ Common Pattern in Every Program ⭐⭐⭐

Look carefully.

### ATM

```python
if amount > self.balance:
    raise BalanceException(
        "Insufficient Balance"
    )
```

### Employee

```python
if self.salary <= 0:
    raise SalaryException(
        "Invalid Salary"
    )
```

### Shopping

```python
if quantity > self.stock:
    raise StockException(
        "Insufficient Stock"
    )
```

### Security

```python
if device != self.device:
    raise SecurityException(
        "Invalid Device"
    )
```

The pattern is always:

```python
if problem_condition:
    raise CustomException(
        "Error message"
    )
```

Remember this formula:

```text
IF
 ↓
Check business rule

RAISE
 ↓
Signal the problem

CUSTOM EXCEPTION
 ↓
Identify the problem

EXCEPT
 ↓
Handle the problem
```

---

# 3️⃣7️⃣ Beginner Logic-Building Trick 🧠

Whenever an interviewer gives you a problem, don't immediately think about Python syntax.

First write plain English.

Example:

> Create ATM withdrawal.

Think:

```text
1. I need balance.

2. User gives withdrawal amount.

3. Amount cannot be zero/negative.

4. Amount cannot exceed balance.

5. If invalid → exception.

6. If valid → subtract amount.

7. Show remaining balance.
```

Now convert each English sentence into Python.

English:

```text
Amount cannot be zero or negative.
```

Python:

```python
if amount <= 0:
```

English:

```text
Signal invalid amount.
```

Python:

```python
raise AmountException(
    "Invalid Amount"
)
```

English:

```text
Amount cannot exceed balance.
```

Python:

```python
if amount > self.balance:
```

English:

```text
Signal insufficient balance.
```

Python:

```python
raise BalanceException(
    "Insufficient Balance"
)
```

English:

```text
Subtract money.
```

Python:

```python
self.balance -= amount
```

That's how you build logic step-by-step.

---

# 3️⃣8️⃣ Interview Coding Question 🎤

### Question

Create an employee class containing:

```text
name
age
salary
```

Rules:

```text
age < 18
   ↓
AgeException

salary < 10000
   ↓
SalaryException
```

### Think Before Coding

```text
Employee
   │
   ├── name
   ├── age
   └── salary
         │
         ▼
      validate()
         │
    ┌────┴─────┐
    ▼          ▼
 age < 18?  salary < 10000?
    │          │
    ▼          ▼
AgeException SalaryException
```

Try writing this yourself before checking your earlier Employee example.

---

# 3️⃣9️⃣ Coding Challenge 🔥

Create a `Payment` class.

Properties:

```text
customer
amount
balance
```

Rules:

```text
amount <= 0
     ↓
InvalidAmountException


amount > balance
     ↓
PaymentException


Valid
     ↓
balance -= amount
```

Your program should use:

```text
✅ Class
✅ Object
✅ Constructor
✅ self
✅ Custom Exception
✅ Inheritance
✅ raise
✅ try
✅ multiple except
✅ else
✅ finally
```

---

# 🏆 CHAPTER 13 — PART 2 FINAL SUMMARY

```text
              REAL-TIME APPLICATION
                       │
                       ▼
                    CLASS
                       │
                       ▼
                    OBJECT
                       │
                       ▼
                 BUSINESS DATA
                       │
                       ▼
                 BUSINESS RULE
                       │
                       ▼
                  CONDITION
                       │
               ┌───────┴───────┐
               │               │
             Valid           Invalid
               │               │
               ▼               ▼
           Continue          raise 🚨
                               │
                               ▼
                       Custom Exception
                               │
                               ▼
                          except 🛡️
```

## ⭐ Final Formula

```python
class MyException(Exception):
    pass


class MyClass:

    def operation(self, value):

        if value_is_invalid:
            raise MyException(
                "Something went wrong"
            )

        # continue operation


obj = MyClass()


try:

    obj.operation(value)

except MyException as e:

    print(e)

else:

    print("Operation Successful")

finally:

    print("Process Completed")
```

Remember:

```text
🏗️ Class
    → represents the real-world entity

📦 Object
    → actual instance

🔧 __init__()
    → initializes object data

👤 self
    → current object

🧬 Exception inheritance
    → creates custom exception types

🔍 if
    → checks business rules

🚨 raise
    → signals the problem

🧪 try
    → executes risky operation

🛡️ except
    → handles the problem

✅ else
    → success path

🔄 finally
    → final/cleanup path
```

## 🎯 Most Important Interview Point

> **In OOP applications, the class contains the business data and behavior. Validation methods check business rules. When a rule is violated, `raise` signals a built-in or custom exception, and the caller handles it using `try-except`.**

### 📚 Progress

```text
Chapter 13
   │
   ├── ✅ Part 1
   │     Basic Exceptions
   │     raise
   │     Student Validation
   │
   └── ✅ Part 2
         ATM
         Login
         Employee
         Shopping
         Device Security
```

**Next: 📘 Chapter 13 — Part 3: Interview Coding Lab** — output prediction, find-the-error programs, fix-the-code exercises, `try/except/else/finally` puzzles, custom exception challenges, and OOP interview coding problems.
