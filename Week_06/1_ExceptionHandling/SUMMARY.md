# 📘 CHAPTER 8 — COMPLETE PYTHON EXCEPTION HANDLING REVISION

Now we will connect the complete Exception Handling topic you studied:

**Errors → Exceptions → `try` → `except` → Multiple `except` → `Exception as e` → `else` → `finally` → `raise` → Custom Exceptions → OOP + Exceptions**

---

# 1️⃣ What is an Error?

## ✅ Definition

An **error** is a problem in a program that prevents the program from executing correctly.

Simple meaning:

> Something went wrong in our program.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError: division by zero
```

Python cannot divide a number by zero.

---

# 2️⃣ Main Error Categories

For your current chapter, think about errors mainly as:

```text
Errors
  │
  ├── Syntax-related problems
  │
  └── Runtime Exceptions
```

Runtime exceptions from your notes include:

```text
IndexError
KeyError
TypeError
ValueError
NameError
AttributeError
ZeroDivisionError
ModuleNotFoundError
FileNotFoundError
```

---

# 3️⃣ SyntaxError 📝

## ✅ Definition

`SyntaxError` happens when Python code does not follow Python grammar.

Example:

```python
if 10 > 5
    print("Hello")
```

❌ Missing `:` after the condition.

Correct:

```python
if 10 > 5:
    print("Hello")
```

---

# ⚠️ Important Correction in Your Notes

You had:

```python
a = 10
print(A)
```

This is **not `SyntaxError`**.

It produces:

```text
NameError
```

because Python syntax is valid, but variable `A` doesn't exist.

Remember:

```text
Wrong Python grammar
        ↓
   SyntaxError

Unknown variable name
        ↓
    NameError
```

---

# 4️⃣ What is an Exception? 🚨

## ✅ Definition

An **exception is an error that occurs while the program is running and interrupts the normal flow of the program.**

Example:

```python
a = 10
b = 0

print(a / b)
```

Python starts executing normally.

Then:

```text
10 / 0
```

causes:

```text
ZeroDivisionError
```

---

# 5️⃣ Common Exceptions ⭐

| Exception             | When it happens                                |
| --------------------- | ---------------------------------------------- |
| `IndexError`          | Invalid list/tuple index                       |
| `KeyError`            | Dictionary key doesn't exist                   |
| `TypeError`           | Invalid operation between types                |
| `ValueError`          | Correct type expected, invalid value supplied  |
| `NameError`           | Variable/name doesn't exist                    |
| `AttributeError`      | Object doesn't have requested attribute/method |
| `ZeroDivisionError`   | Division by zero                               |
| `FileNotFoundError`   | Requested file doesn't exist                   |
| `ModuleNotFoundError` | Imported module cannot be found                |

---

# 6️⃣ `IndexError`

## Definition

Occurs when we access an index that doesn't exist.

### Example

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Indexes available:

```text
Value →  10    20    30
Index →   0     1     2
```

We requested:

```text
5 ❌
```

Therefore:

```text
IndexError: list index out of range
```

---

# 7️⃣ `KeyError`

Occurs when a dictionary key doesn't exist.

```python
student = {
    "name": "Ramesh",
    "age": 30
}

print(student["salary"])
```

Available keys:

```text
name
age
```

Requested:

```text
salary ❌
```

Therefore:

```text
KeyError
```

---

# 8️⃣ `TypeError`

Occurs when an operation is not supported between the given types.

```python
print(10 + "20")
```

Here:

```text
10
↓
int

"20"
↓
str
```

Python cannot directly perform:

```text
int + str
```

Therefore:

```text
TypeError
```

---

# 9️⃣ `ValueError`

Example:

```python
age = int("twenty")
```

`int()` can convert:

```python
int("20")
```

but not:

```python
int("twenty")
```

Therefore:

```text
ValueError
```

---

# 🔟 `NameError`

```python
a = 10

print(A)
```

Python is case-sensitive.

```text
a ≠ A
```

So:

```text
NameError
```

---

# 1️⃣1️⃣ `AttributeError`

Example:

```python
numbers = [10, 20, 30]

numbers.get()
```

A list doesn't have a:

```python
get()
```

method.

Therefore:

```text
AttributeError
```

Another example:

```python
name = "Python"

name.append("A")
```

Strings don't have `append()`.

Again:

```text
AttributeError
```

---

# 1️⃣2️⃣ `ZeroDivisionError`

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

Because division by zero isn't allowed.

---

# 1️⃣3️⃣ Why Exception Handling? 🤔

Suppose:

```python
print("Program Started")

print(10 / 0)

print("Program Completed")
```

Execution:

```text
Program Started
       ↓
    10 / 0
       ↓
💥 ZeroDivisionError
       ↓
Program stops
```

The final statement doesn't execute.

Exception handling helps us deal with expected runtime problems in a controlled way.

---

# 1️⃣4️⃣ `try-except` 🛡️

## Definition

`try-except` is used to handle exceptions.

### Syntax

```python
try:
    # risky code

except:
    # handling code
```

---

# 1️⃣5️⃣ Simple Example

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

# 1️⃣6️⃣ Flow Diagram 🔄

```text
             try
              │
              ▼
        Execute code
              │
        ┌─────┴─────┐
        │           │
   No Exception   Exception
        │           │
        ▼           ▼
 continue       except block
```

---

# 1️⃣7️⃣ Dry Run

```python
try:
    a = 20
    print(a / 0)

except:
    print("Pass value greater than zero")
```

### Step 1

```python
a = 20
```

Memory:

```text
a → 20
```

### Step 2

```python
print(a / 0)
```

Becomes:

```text
20 / 0
```

Exception:

```text
ZeroDivisionError
```

### Step 3

Python stops executing the remaining statements in that `try` block and searches for a matching `except`.

### Step 4

```python
except:
```

handles it.

Output:

```text
Pass value greater than zero
```

---

# 1️⃣8️⃣ Specific Exception Handling ⭐

Instead of:

```python
except:
```

prefer a specific exception when you know what problem you're expecting.

Example:

```python
try:
    print(20 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

This clearly tells another programmer:

> We are expecting a `ZeroDivisionError` here.

---

# 1️⃣9️⃣ Multiple `except` Blocks

A `try` block may potentially produce different errors.

Example:

```python
try:

    numbers = [10, 20, 30]

    index = int(input("Enter index: "))

    print(numbers[index])

except ValueError:

    print("Enter numbers only")

except IndexError:

    print("Invalid index")
```

Possible situations:

```text
Input = abc
    ↓
ValueError


Input = 100
    ↓
IndexError


Input = 1
    ↓
20
```

---

# 2️⃣0️⃣ Important Execution Rule 🚨

Consider your original example:

```python
try:
    a = 20

    print(A)

    numbers = [2, 3, 4]

    print(numbers[8])

    print(20 / 0)

except NameError:
    print("Give some valid variable name")

except IndexError:
    print("Give proper index value")

except ZeroDivisionError:
    print("Enter value greater than zero")
```

You may think Python will find all three errors.

It doesn't.

The first error is:

```python
print(A)
```

So:

```text
NameError
```

occurs.

Python immediately leaves the `try` block.

Therefore:

```python
print(numbers[8])
```

and:

```python
print(20 / 0)
```

are not executed during that try-block run.

### ⭐ Remember

> Once an exception occurs inside a `try`, Python stops the remaining code in that `try` and searches for a matching handler.

---

# 2️⃣1️⃣ `Exception as e`

Instead of writing handlers for every possible exception:

```python
except ValueError:
```

you can sometimes use:

```python
except Exception as e:
```

Example:

```python
try:
    age = int(input("Enter age: "))

except Exception as e:
    print(e)
```

If input is:

```text
twenty
```

`e` contains/references the exception object.

Printing:

```python
print(e)
```

shows the error message.

---

# 2️⃣2️⃣ OOP Connection 🧠

This becomes easier when you think in OOP.

```python
except Exception as e:
```

Conceptually:

```text
Exception occurs
       ↓
Exception object
       ↓
      e
```

So:

```python
print(e)
```

prints the exception object's message.

---

# 2️⃣3️⃣ `else` Block ✅

## Definition

The `else` block executes **only when the `try` block completes without an exception**.

### Syntax

```python
try:
    # risky code

except Exception as e:
    # handle exception

else:
    # executes when no exception occurs
```

---

# 2️⃣4️⃣ Example

```python
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Only numbers allowed")

else:
    print("Your age is:", age)
```

Input:

```text
25
```

Flow:

```text
"25"
 ↓
int("25")
 ↓
25
 ↓
No Exception
 ↓
else
 ↓
Your age is: 25
```

---

# 2️⃣5️⃣ If Exception Occurs

Input:

```text
twenty
```

Flow:

```text
int("twenty")
      ↓
 ValueError
      ↓
   except
      ↓
Only numbers allowed
```

`else` does not execute.

---

# 2️⃣6️⃣ `finally` Block 🔥

## Definition

The `finally` block executes whether an exception occurs or not.

### Syntax

```python
try:
    # risky code

except:
    # handling

else:
    # no exception

finally:
    # always executes
```

---

# 2️⃣7️⃣ Why Do We Need `finally`?

It is useful for cleanup work such as:

```text
📁 Closing files
🗄️ Closing database connections
🌐 Closing network connections
🧹 Releasing resources
```

---

# 2️⃣8️⃣ Example

```python
try:
    print("Try Block")

except:
    print("Except Block")

finally:
    print("Finally Block")
```

Output:

```text
Try Block
Finally Block
```

Even though there was no exception:

```text
finally
```

still executed.

---

# 2️⃣9️⃣ Complete Flow ⭐

```text
                  TRY
                   │
          ┌────────┴────────┐
          │                 │
    No Exception         Exception
          │                 │
          ▼                 ▼
        ELSE             EXCEPT
          │                 │
          └────────┬────────┘
                   ▼
                FINALLY
```

This diagram is very important for interviews.

---

# 3️⃣0️⃣ File Handling Example 📁

From your notes:

```python
try:
    f = open("sample.txt", "r")

except FileNotFoundError:
    print("File not found")

else:
    print(f.read())

finally:
    f.close()
```

Concept:

```text
Open File
   ↓
Success?
 ┌─┴─┐
Yes  No
 │    │
else except
 │    │
 └─┬──┘
   ↓
finally
   ↓
close file
```

---

# ⚠️ Important Problem With This Version

If:

```python
open("sample.txt", "r")
```

fails, `f` may never have been assigned.

Then:

```python
f.close()
```

can itself cause a problem.

A safer beginner version is:

```python
f = None

try:
    f = open("sample.txt", "r")

except FileNotFoundError:
    print("File not found")

else:
    print(f.read())

finally:
    if f is not None:
        f.close()
```

Later, when you study context managers, you'll learn an even cleaner approach using `with`.

---

# 3️⃣1️⃣ `raise` Keyword 🚨

## Definition

`raise` is used to **manually generate an exception** when your program detects an invalid situation.

### Syntax

```python
raise Exception("Message")
```

Example:

```python
age = 15

if age < 18:
    raise Exception("Not eligible")
```

---

# 3️⃣2️⃣ Why Do We Need `raise`?

Python automatically raises errors such as:

```text
10 / 0
→ ZeroDivisionError
```

But Python doesn't automatically understand your business rules.

For example:

```text
Bank balance = ₹5,000

Withdrawal = ₹10,000
```

Technically Python can calculate numbers.

But your banking rule says:

> Withdrawal should not exceed the available balance.

So **you** detect that condition and `raise` an exception.

---

# 3️⃣3️⃣ Bank OOP Example 🏦

```python
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
```

Object:

```python
account = Bank("Ramesh", 5000)
```

---

# 3️⃣4️⃣ Memory Diagram

```text
account
   │
   ▼
┌────────────────────┐
│ Bank Object        │
├────────────────────┤
│ name = Ramesh      │
│ balance = 5000     │
└────────────────────┘
```

Call:

```python
account.withdraw(900)
```

Check:

```text
900 < 0 ?
   ↓
False

900 > 5000 ?
   ↓
False

5000 - 900
   ↓
4100
```

New balance:

```text
4100
```

---

# 3️⃣5️⃣ Invalid Withdrawal

```python
account.withdraw(10000)
```

Flow:

```text
amount = 10000
     ↓
10000 > balance?
     ↓
10000 > 5000
     ↓
True
     ↓
raise Exception
     ↓
"Insufficient Balance"
```

---

# 3️⃣6️⃣ Custom Exception 🛡️

## Definition

A **custom exception** is an exception class created by the programmer for a specific application problem.

### Syntax

```python
class MyException(Exception):
    pass
```

Example:

```python
class BankException(Exception):
    pass
```

---

# 3️⃣7️⃣ Custom Exception With Constructor

Your notes use:

```python
class BankException(Exception):

    def __init__(self, message):
        super().__init__(message)
```

OOP structure:

```text
Exception
 Parent
    │
    ▼
BankException
   Child
```

Concept:

```text
Inheritance 🧬
```

---

# 3️⃣8️⃣ Using It

```python
class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):

        if amount < 0:
            raise BankException(
                "Enter a valid amount"
            )

        if amount > self.balance:
            raise BankException(
                "Insufficient Balance"
            )

        self.balance -= amount
```

---

# 3️⃣9️⃣ Handling Custom Exception

```python
try:
    account.withdraw(10000)

except BankException as e:
    print(e)
```

Flow:

```text
withdraw()
    ↓
Business Rule Fails
    ↓
BankException object
    ↓
raise
    ↓
except BankException as e
    ↓
print(e)
```

---

# 4️⃣0️⃣ Built-in vs Custom Exception

| Built-in Exception                | Custom Exception              |
| --------------------------------- | ----------------------------- |
| Provided by Python                | Created by programmer         |
| `ValueError`                      | `BankException`               |
| `IndexError`                      | `SecurityException`           |
| `TypeError`                       | `LoginException`              |
| General language/runtime problems | Application-specific problems |

---

# 4️⃣1️⃣ Google Security Example 🔐

Your advanced example:

```python
class SecurityException(Exception):

    def __init__(self, message):
        super().__init__(message)
```

Google class:

```python
class Google:

    def __init__(self, email, password, device):

        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):

        if device != self.device:

            raise SecurityException(
                "Please login using your registered device."
            )

        if email == self.email and password == self.password:

            print("Login Successful")
```

---

# 4️⃣2️⃣ Complete OOP Relationship

```text
              Exception
                  │
                  │ inheritance
                  ▼
          SecurityException


              Google
                │
                ▼
          google object
                │
        ┌───────┼───────┐
        ▼       ▼       ▼
      email  password  device
                │
                ▼
             login()
                │
                ▼
        Security checking
                │
        ┌───────┴────────┐
        │                │
      Valid            Invalid
        │                │
        ▼                ▼
      Login            raise
    Successful    SecurityException
```

---

# 4️⃣3️⃣ `raise` vs `except` ⭐

This interview question is important.

| `raise`                         | `except`                    |
| ------------------------------- | --------------------------- |
| Generates/signals an exception  | Handles an exception        |
| Used when a problem is detected | Used after exception occurs |
| `raise BankException()`         | `except BankException:`     |

Remember:

```text
raise
  ↓
🚨 "There is a problem!"


except
  ↓
🛡️ "I'll handle the problem."
```

---

# 4️⃣4️⃣ `try` vs `except` vs `else` vs `finally`

| Keyword   | Purpose                                  |
| --------- | ---------------------------------------- |
| `try`     | Put risky code here                      |
| `except`  | Handle exceptions                        |
| `else`    | Runs if `try` succeeds without exception |
| `finally` | Runs whether exception occurs or not     |
| `raise`   | Manually signal an exception             |

---

# 4️⃣5️⃣ Complete Syntax ⭐

```python
try:

    # risky code

except ValueError:

    # handle ValueError

except TypeError:

    # handle TypeError

except Exception as e:

    # handle other Exception subclasses

else:

    # runs if try completes successfully

finally:

    # cleanup code
```

And manually raising:

```python
raise Exception("Error message")
```

Custom exception:

```python
class MyException(Exception):
    pass
```

---

# 4️⃣6️⃣ Common Mistakes ❌

### ❌ Mistake 1 — Using only bare `except` everywhere

```python
try:
    ...
except:
    ...
```

For learning, understand it. But when you know the expected problem, prefer:

```python
except ValueError:
```

---

### ❌ Mistake 2 — Expecting all errors in one `try` to execute

```python
try:
    print(A)
    print(numbers[100])
    print(10 / 0)
```

The first exception stops that `try` block.

---

### ❌ Mistake 3 — Confusing `raise` with `except`

```text
raise → generate/signal

except → handle
```

---

### ❌ Mistake 4 — Forgetting inheritance

Wrong custom exception:

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

### ❌ Mistake 5 — Calling a closed file

```python
f.close()

f.write("Hello")
```

The file is already closed.

---

# 4️⃣7️⃣ Interview Questions 🎤

### Q1. What is an exception?

An exception is a runtime problem that interrupts the normal execution flow of a program.

### Q2. What is exception handling?

Exception handling is the process of detecting and handling runtime exceptions so the program can respond appropriately.

### Q3. What is `try`?

`try` contains code that may raise an exception.

### Q4. What is `except`?

`except` handles a matching exception.

### Q5. Can we have multiple `except` blocks?

Yes.

```python
except ValueError:
    ...

except TypeError:
    ...
```

### Q6. What is `else`?

`else` executes when the `try` block finishes without an exception.

### Q7. What is `finally`?

`finally` executes whether an exception occurs or not.

### Q8. What is `raise`?

`raise` manually signals an exception.

### Q9. What is a custom exception?

A programmer-defined exception class used for application-specific error situations.

### Q10. Why inherit from `Exception`?

So our custom class behaves as an exception and can participate in Python's exception-handling system.

---

# 4️⃣8️⃣ MCQs 📝

### 1. Which keyword handles an exception?

A. `try`
B. `except` ✅
C. `raise`
D. `error`

### 2. Which block always executes in the normal `try`/`except` flow?

A. `try`
B. `except`
C. `else`
D. `finally` ✅

### 3. What happens here?

```python
print(10 / 0)
```

A. `ValueError`
B. `TypeError`
C. `ZeroDivisionError` ✅
D. `IndexError`

### 4. What happens here?

```python
int("hello")
```

A. `ValueError` ✅
B. `NameError`
C. `IndexError`
D. `KeyError`

### 5. Which keyword manually generates an exception?

A. `except`
B. `finally`
C. `raise` ✅
D. `else`

---

# 4️⃣9️⃣ Practice Programs 💻

Practice these in order:

1. Handle `ZeroDivisionError`.
2. Handle invalid age input using `ValueError`.
3. Handle invalid list index using `IndexError`.
4. Handle missing dictionary key using `KeyError`.
5. Write one program with multiple `except` blocks.
6. Write a `try-except-else` program.
7. Write a `try-except-finally` program.
8. Use `raise` for age validation.
9. Create `BankException`.
10. Create a bank withdrawal system using `BankException`.
11. Create `LoginException`.
12. Create a login system using OOP + custom exceptions.
13. Create `SecurityException` for an unregistered device.

---

# 🏆 FINAL CHAPTER SUMMARY

The complete topic can be remembered with this single flow:

```text
                    PYTHON ERRORS
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
       Syntax problems        Runtime Exceptions
                                     │
                   ┌─────────────────┼────────────────┐
                   ▼                 ▼                ▼
              ValueError        IndexError      TypeError
              NameError         KeyError        etc.
                   │
                   ▼
             Exception Handling
                   │
                   ▼
                 try
                   │
          ┌────────┴────────┐
          ▼                 ▼
     No Exception        Exception
          │                 │
          ▼                 ▼
        else             except
          │                 │
          └────────┬────────┘
                   ▼
                finally

                   +

                 raise
                   │
                   ▼
          Manually signal error

                   +

        class MyError(Exception)
                   │
                   ▼
            Custom Exception
                   │
                   ▼
             OOP Inheritance
```

## 🧠 Five Lines You Must Remember

```python
try:
    # risky code

except Exception as e:
    # handle error

else:
    # executes when no exception occurs

finally:
    # cleanup / always executes
```

To manually generate an exception:

```python
raise Exception("Something went wrong")
```

To create your own exception:

```python
class MyException(Exception):
    pass
```

### ⭐ One-line interview answer

> **Exception handling is a mechanism for handling runtime errors using `try`, `except`, `else`, and `finally`; Python also provides `raise` for explicitly signaling exceptions and allows custom exception classes to represent application-specific errors.**

At this point, your Exception Handling chapter connects directly with your earlier **OOP concepts: class, object, constructor, `self`, methods, inheritance, `super()`, and custom exception objects**.
====
# 📘 CHAPTER 9 — `raise` KEYWORD IN PYTHON

Now we’ll study `raise` separately because it is one of the most important parts of **Exception Handling + OOP**.

---

# 1️⃣ What is `raise`? 🚨

## ✅ Definition

The **`raise` keyword is used to manually generate an exception when a specific condition occurs.**

Normally, Python automatically generates exceptions.

Example:

```python
print(10 / 0)
```

Python automatically raises:

```text
ZeroDivisionError
```

But sometimes **our own application rule** is violated.

Example:

```text
Bank Balance = 5000
Withdrawal   = 10000
```

Python doesn't know that withdrawing ₹10,000 from ₹5,000 should be considered invalid in our application.

So we can write:

```python
raise Exception("Insufficient Balance")
```

---

# 2️⃣ Why Do We Need `raise`? 🤔

Consider:

```python
age = 15

if age < 18:
    print("Not Eligible")
```

This only prints a message.

But suppose being under 18 should be treated as an exceptional condition in our application.

We can write:

```python
age = 15

if age < 18:
    raise Exception("Age must be 18 or above")
```

Output:

```text
Exception: Age must be 18 or above
```

So remember:

```text
print()
   ↓
Displays information


raise
   ↓
Signals an exception 🚨
```

---

# 3️⃣ Basic Syntax 📝

```python
raise Exception("Error message")
```

General structure:

```python
if condition:
    raise Exception("Message")
```

Example:

```python
amount = -500

if amount < 0:
    raise Exception("Enter positive amount")
```

---

# 4️⃣ Simple Example

```python
age = 16

if age < 18:
    raise Exception("Not eligible to vote")

print("Eligible to vote")
```

### Dry Run 🔍

First:

```python
age = 16
```

Memory:

```text
age
 ↓
16
```

Check:

```python
age < 18
```

Becomes:

```text
16 < 18
```

Result:

```text
True
```

Therefore:

```python
raise Exception("Not eligible to vote")
```

executes.

Normal execution stops there.

---

# 5️⃣ `raise` With `try-except` 🛡️

Usually we handle the raised exception using `try-except`.

```python
try:

    age = 16

    if age < 18:
        raise Exception("Not eligible to vote")

except Exception as e:

    print(e)
```

Output:

```text
Not eligible to vote
```

---

# 6️⃣ Complete Flow Diagram 🔄

```text
START
  │
  ▼
age = 16
  │
  ▼
age < 18 ?
  │
 ┌┴───────────────┐
 │                │
Yes               No
 │                │
 ▼                ▼
raise           Continue
Exception       Program
 │
 ▼
except Exception as e
 │
 ▼
print(e)
 │
 ▼
END
```

---

# 7️⃣ What Happens Internally? 🧠

Consider:

```python
raise Exception("Invalid Age")
```

Conceptually Python creates an exception object:

```text
Exception
    │
    ▼
┌────────────────────┐
│ Exception Object   │
├────────────────────┤
│ "Invalid Age"      │
└────────────────────┘
```

Then:

```python
raise
```

signals that exception.

If we have:

```python
except Exception as e:
```

then conceptually:

```text
Exception Object
       │
       ▼
       e
```

Therefore:

```python
print(e)
```

prints:

```text
Invalid Age
```

This is where your **OOP knowledge** becomes useful.

---

# 8️⃣ `raise` in OOP 🏗️

Let's use your Bank example.

```python
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
```

Create object:

```python
account = Bank("Ramesh", 5000)
```

Memory:

```text
account
   │
   ▼
┌──────────────────────┐
│ Bank Object          │
├──────────────────────┤
│ name    = Ramesh     │
│ balance = 5000       │
└──────────────────────┘
```

---

# 9️⃣ Valid Withdrawal 💰

```python
account.withdraw(900)
```

Inside:

```text
amount = 900
balance = 5000
```

First condition:

```python
if amount < 0:
```

Becomes:

```text
900 < 0
↓
False
```

Next:

```python
if amount > self.balance:
```

Becomes:

```text
900 > 5000
↓
False
```

Then:

```python
self.balance -= amount
```

means:

```text
5000 - 900
     ↓
4100
```

New object state:

```text
account
   │
   ▼
┌──────────────────────┐
│ name    = Ramesh     │
│ balance = 4100       │
└──────────────────────┘
```

---

# 🔟 Invalid Withdrawal 🚨

Suppose:

```python
account.withdraw(10000)
```

Check:

```text
10000 < 0
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
raise Exception("Insufficient Balance")
```

executes.

Flow:

```text
withdraw(10000)
      ↓
amount > balance
      ↓
10000 > 5000
      ↓
    True
      ↓
raise Exception
      ↓
🚨 Insufficient Balance
```

---

# 1️⃣1️⃣ Handling Bank Exception

```python
try:

    account.withdraw(10000)

except Exception as e:

    print(e)
```

Output:

```text
Insufficient Balance
```

---

# 1️⃣2️⃣ `raise` vs `print()` ⭐

This difference is very important.

## Using `print()`

```python
if amount > balance:
    print("Insufficient Balance")
```

This only displays:

```text
Insufficient Balance
```

The program isn't signaling an exception.

## Using `raise`

```python
if amount > balance:
    raise Exception("Insufficient Balance")
```

Now an exception is generated.

It can be handled by:

```python
except Exception as e:
```

---

# 1️⃣3️⃣ Difference Table

| `print()`                      | `raise`                               |
| ------------------------------ | ------------------------------------- |
| Displays message               | Signals exception                     |
| Normal statement               | Exception mechanism                   |
| Does not create exception flow | Changes normal execution flow         |
| Cannot be caught by `except`   | Can be caught by matching `except`    |
| Used for output                | Used for error/business-rule handling |

---

# 1️⃣4️⃣ Real-Time Example — Login 🔐

Suppose:

```python
username = "admin"
password = 1234
```

User enters:

```text
username = admin
password = 9999
```

We can raise an exception.

```python
class Login:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def login(self, username, password):

        if username != self.username:
            raise Exception("Invalid Username")

        if password != self.password:
            raise Exception("Invalid Password")

        print("Login Successful")
```

Object:

```python
user = Login("admin", 1234)
```

---

# 1️⃣5️⃣ Testing Login

```python
try:

    user.login("admin", 9999)

except Exception as e:

    print(e)
```

Flow:

```text
username
admin == admin
      ↓
    True ✅

password
9999 == 1234
      ↓
    False ❌

      ↓

raise Exception
"Invalid Password"

      ↓

except Exception as e

      ↓

print(e)
```

Output:

```text
Invalid Password
```

---

# 1️⃣6️⃣ Why General `Exception` Is Not Always Enough

Currently:

```python
raise Exception("Invalid Password")
```

works.

But imagine a large application containing:

```text
Bank errors
Login errors
Payment errors
Security errors
Database errors
```

Using:

```python
Exception
```

for everything is too general.

Instead we can create meaningful custom exceptions:

```text
BankException
LoginException
SecurityException
PaymentException
```

This brings us directly to **OOP + Inheritance**.

---

# 1️⃣7️⃣ Custom Exception 🛡️

## Definition

A **custom exception is a programmer-defined exception class used to represent a specific application error.**

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

---

# 1️⃣8️⃣ OOP Concept — Inheritance 🧬

Look carefully:

```python
class BankException(Exception):
```

This means:

```text
       Exception
       Parent Class
            │
            │
        inheritance
            │
            ▼
      BankException
       Child Class
```

So custom exceptions are directly connected to the OOP concept:

> **Inheritance**

---

# 1️⃣9️⃣ Custom Exception With Constructor

Your notes use:

```python
class BankException(Exception):

    def __init__(self, message):

        super().__init__(message)
```

Here:

```python
message
```

receives the error message.

And:

```python
super().__init__(message)
```

passes it to the parent `Exception` class.

---

# 2️⃣0️⃣ Understanding `super()`

```python
super()
```

means we want to access functionality from the parent class according to Python's method resolution rules.

Here:

```text
BankException
      │
      ▼
  Exception
```

So:

```python
super().__init__(message)
```

initializes the inherited exception with the supplied message.

---

# 2️⃣1️⃣ Complete Custom Bank Exception

```python
class BankException(Exception):

    def __init__(self, message):
        super().__init__(message)


class Bank:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def withdraw(self, amount):

        if amount < 0:

            raise BankException(
                "Enter a valid amount"
            )

        if amount > self.balance:

            raise BankException(
                "Insufficient Balance"
            )

        self.balance -= amount
```

Object:

```python
account = Bank("Ramesh", 5000)
```

---

# 2️⃣2️⃣ Handling `BankException`

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

# 2️⃣3️⃣ Complete Execution Flow ⭐

```text
account.withdraw(10000)
          │
          ▼
   withdraw() method
          │
          ▼
 amount > balance ?
          │
          ▼
 10000 > 5000
          │
          ▼
        True
          │
          ▼
Create BankException Object
          │
          ▼
       raise
          │
          ▼
except BankException as e
          │
          ▼
      print(e)
          │
          ▼
 Insufficient Balance
```

---

# 2️⃣4️⃣ Exception Object Memory Diagram 🧠

When Python evaluates:

```python
BankException("Insufficient Balance")
```

conceptually:

```text
┌──────────────────────────┐
│ BankException Object     │
├──────────────────────────┤
│ Message                  │
│ "Insufficient Balance"   │
└──────────────────────────┘
             ▲
             │
             e
```

Therefore:

```python
print(e)
```

shows:

```text
Insufficient Balance
```

---

# 2️⃣5️⃣ Built-in vs Custom Exception

| Built-in                          | Custom                          |
| --------------------------------- | ------------------------------- |
| Created/provided by Python        | Created by programmer           |
| `ValueError`                      | `BankException`                 |
| `TypeError`                       | `LoginException`                |
| `IndexError`                      | `SecurityException`             |
| General Python/runtime situations | Application-specific situations |

---

# 2️⃣6️⃣ Custom Login Exception 🔐

Let's improve the previous login program.

```python
class LoginException(Exception):

    def __init__(self, message):
        super().__init__(message)
```

Now:

```python
class Login:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def login(self, username, password):

        if username != self.username:

            raise LoginException(
                "Invalid Username"
            )

        if password != self.password:

            raise LoginException(
                "Invalid Password"
            )

        print("Login Successful")
```

---

# 2️⃣7️⃣ Object Creation

```python
user = Login("admin", 1234)
```

Memory:

```text
user
 │
 ▼
┌────────────────────────┐
│ Login Object           │
├────────────────────────┤
│ username = admin       │
│ password = 1234        │
└────────────────────────┘
```

---

# 2️⃣8️⃣ Wrong Password

```python
try:

    user.login("admin", 9999)

except LoginException as e:

    print(e)
```

Output:

```text
Invalid Password
```

---

# 2️⃣9️⃣ Multiple Custom Exceptions ⭐

In a larger program, we can even create different exception types.

```python
class UsernameException(Exception):
    pass


class PasswordException(Exception):
    pass
```

Then:

```python
class Login:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def login(self, username, password):

        if username != self.username:
            raise UsernameException(
                "Invalid Username"
            )

        if password != self.password:
            raise PasswordException(
                "Invalid Password"
            )

        print("Login Successful")
```

---

# 3️⃣0️⃣ Multiple Custom `except` Blocks

```python
user = Login("admin", 1234)

try:

    user.login("admin", 9999)

except UsernameException as e:

    print("Username Error:", e)

except PasswordException as e:

    print("Password Error:", e)
```

Output:

```text
Password Error: Invalid Password
```

This is more specific than catching every problem using:

```python
except Exception:
```

---

# 3️⃣1️⃣ Exception Hierarchy 🧬

For your beginner understanding:

```text
              Exception
                  │
        ┌─────────┼──────────┐
        │         │          │
        ▼         ▼          ▼
BankException LoginException SecurityException
```

All three are custom exceptions.

All inherit from:

```python
Exception
```

---

# 3️⃣2️⃣ Common Mistakes ❌

### ❌ Mistake 1

```python
raise "Invalid Password"
```

Don't raise a normal string.

Use an exception:

```python
raise Exception("Invalid Password")
```

or:

```python
raise LoginException("Invalid Password")
```

---

### ❌ Mistake 2

Creating custom exception without inheritance:

```python
class LoginException:
    pass
```

Then trying:

```python
raise LoginException()
```

This is not a valid exception class because it doesn't derive from `BaseException`.

Use:

```python
class LoginException(Exception):
    pass
```

---

### ❌ Mistake 3

Using `print()` when you actually need exception handling.

```python
if amount > balance:
    print("Insufficient Balance")
```

This may be fine when you only want a message.

But if the calling code must handle the failure:

```python
raise BankException(
    "Insufficient Balance"
)
```

is more appropriate.

---

# 3️⃣3️⃣ Advantages of `raise` ✅

`raise` helps us:

```text
✅ Enforce application rules
✅ Validate data
✅ Stop invalid operations
✅ Separate normal flow from error handling
✅ Create meaningful custom errors
✅ Build cleaner OOP applications
```

---

# 3️⃣4️⃣ Disadvantages / Cautions ⚠️

Incorrect exception use can make programs harder to understand.

For example:

```text
❌ Raising exceptions for normal everyday control flow
❌ Catching every exception without understanding it
❌ Using only generic Exception everywhere
❌ Giving unclear error messages
❌ Ignoring exceptions completely
```

Use exceptions for genuinely exceptional or invalid situations.

---

# 3️⃣5️⃣ Interview Questions & Answers 🎤

### Q1. What is `raise`?

`raise` is used to manually signal an exception.

### Q2. Syntax?

```python
raise Exception("Error message")
```

### Q3. Can we raise custom exceptions?

Yes.

```python
raise BankException(
    "Insufficient Balance"
)
```

### Q4. What is a custom exception?

A custom exception is a programmer-defined exception class for application-specific errors.

### Q5. Which class is normally inherited?

```python
Exception
```

Example:

```python
class BankException(Exception):
    pass
```

### Q6. Which OOP concept is used?

**Inheritance.**

### Q7. What is `super()`?

`super()` allows access to parent-class functionality according to the method resolution order.

### Q8. Difference between `raise` and `except`?

```text
raise  → signal an exception 🚨

except → handle an exception 🛡️
```

---

# 3️⃣6️⃣ MCQs 📝

### 1. Which keyword manually signals an exception?

A. `try`
B. `except`
C. `raise` ✅
D. `finally`

### 2. Which is correct?

A.

```python
raise "Error"
```

B.

```python
raise Exception("Error")
```

✅ **Answer: B**

### 3. Custom exception normally inherits from?

A. `list`
B. `dict`
C. `Exception` ✅
D. `str`

### 4. What OOP concept is this?

```python
class BankException(Exception):
```

A. Encapsulation
B. Inheritance ✅
C. Abstraction
D. Looping

### 5. What handles a raised exception?

A. `raise`
B. `except` ✅
C. `if`
D. `return`

---

# 3️⃣7️⃣ Practice Programs 💻

Try these yourself in order:

1. Raise an exception if age is below 18.
2. Raise an exception if salary is negative.
3. Raise an exception if marks are above 100 or below 0.
4. Create `BankException`.
5. Raise `BankException` for insufficient balance.
6. Create `LoginException`.
7. Raise `LoginException` for an incorrect password.
8. Create `SecurityException`.
9. Raise `SecurityException` for a wrong device.
10. Create separate `UsernameException` and `PasswordException`.

---

# 🏆 CHAPTER 9 — FINAL SUMMARY

The easiest way to remember the complete topic is:

```text
Business/Application Rule
          │
          ▼
     Check Condition
          │
      ┌───┴───┐
      │       │
    Valid   Invalid
      │       │
      ▼       ▼
 Continue   raise
              │
              ▼
       Exception Object
              │
              ▼
            except
              │
              ▼
          Handle Error
```

### Built-in exception

```python
raise Exception("Something went wrong")
```

### Custom exception

```python
class BankException(Exception):
    pass
```

### Raise custom exception

```python
raise BankException(
    "Insufficient Balance"
)
```

### Handle custom exception

```python
try:
    account.withdraw(10000)

except BankException as e:
    print(e)
```

### 🧠 OOP Connection

```text
Exception
   │
   │ Inheritance
   ▼
BankException
   │
   │ Object created
   ▼
BankException("Insufficient Balance")
   │
   │ raise
   ▼
🚨 Exception
   │
   │ caught by
   ▼
except BankException as e
```

## ⭐ Interview Definition

> **The `raise` keyword is used to explicitly signal an exception. It is commonly combined with custom exception classes to represent application-specific error conditions.**

## 🔑 Remember These 6 Keywords

```text
try      → 🧪 risky code
except   → 🛡️ handle exception
else     → ✅ no exception
finally  → 🔄 cleanup / runs regardless
raise    → 🚨 manually signal exception
Exception → 🧬 common base for many exception types
```

**Next: Chapter 10 — Custom Exceptions in OOP**, focusing deeply on `Exception` inheritance, `super()`, custom exception objects, multiple custom exception classes, and complete real-time Bank/Login/Security programs.
====
# 📘 CHAPTER 10 — CUSTOM EXCEPTIONS IN OOP

Now we’ll study **Custom Exceptions** deeply as an **OOP concept**.

This chapter connects everything you already learned:

```text
Class → Object → Constructor → self
                  ↓
             Inheritance
                  ↓
               super()
                  ↓
              Exception
                  ↓
          Custom Exception
                  ↓
                raise
                  ↓
            try → except
```

---

# 1️⃣ What is a Custom Exception? 🛡️

## ✅ Definition

A **Custom Exception** is an exception class created by the programmer to represent a specific error in an application.

Python already provides exceptions such as:

```python
ValueError
TypeError
IndexError
KeyError
ZeroDivisionError
FileNotFoundError
```

But Python doesn't know all the rules of our application.

For example:

```text
🏦 Bank Application
Withdrawal > Balance
        ↓
Insufficient Balance

🔐 Login Application
Wrong Device
        ↓
Security Problem

🛒 Shopping Application
Product Out of Stock
        ↓
Stock Problem
```

We can create our own exceptions:

```python
BankException
SecurityException
StockException
```

---

# 2️⃣ Why Do We Need Custom Exceptions? 🤔

Consider:

```python
raise Exception("Insufficient Balance")
```

This works.

But `Exception` is very general.

Imagine a large application containing:

```text
Banking Error
Login Error
Payment Error
Security Error
Database Error
```

If everything uses:

```python
Exception
```

we don't immediately know what type of application problem occurred.

Instead:

```python
raise BankException("Insufficient Balance")
```

is more meaningful.

---

# 3️⃣ Basic Syntax 📝

The simplest custom exception is:

```python
class CustomException(Exception):
    pass
```

Example:

```python
class BankException(Exception):
    pass
```

Here:

```text
Exception
    ↑
    │
BankException
```

`BankException` inherits from `Exception`.

---

# 4️⃣ OOP Concept — Inheritance 🧬

Look carefully:

```python
class BankException(Exception):
```

This is exactly the same inheritance syntax you learned earlier:

```python
class Dog(Animal):
    pass
```

Comparison:

| Normal Inheritance | Exception Inheritance |
| ------------------ | --------------------- |
| `Animal`           | `Exception`           |
| `Dog`              | `BankException`       |
| Parent class       | Parent class          |
| Child class        | Child class           |

So:

```python
class BankException(Exception):
```

means:

```text
       Exception
      Parent Class
           │
           │ inherits
           ▼
     BankException
      Child Class
```

---

# 5️⃣ Simplest Custom Exception Example

```python
class BankException(Exception):
    pass


balance = 5000
withdraw = 10000

if withdraw > balance:
    raise BankException("Insufficient Balance")
```

Output:

```text
BankException: Insufficient Balance
```

---

# 6️⃣ Flow Diagram 🔄

```text
balance = 5000
withdraw = 10000
       │
       ▼
withdraw > balance?
       │
       ▼
10000 > 5000
       │
       ▼
      True
       │
       ▼
BankException(...)
       │
       ▼
Exception Object
       │
       ▼
     raise
       │
       ▼
🚨 BankException
```

---

# 7️⃣ Handling the Custom Exception 🛡️

Instead of allowing the exception to remain unhandled:

```python
try:

    balance = 5000
    withdraw = 10000

    if withdraw > balance:
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

# 8️⃣ Understanding `as e` 🧠

This is very important for OOP.

```python
except BankException as e:
```

When this happens:

```python
BankException("Insufficient Balance")
```

an exception object is created.

Conceptually:

```text
e
│
▼
┌───────────────────────────┐
│ BankException Object      │
├───────────────────────────┤
│ "Insufficient Balance"    │
└───────────────────────────┘
```

Therefore:

```python
print(e)
```

prints the exception message.

---

# 9️⃣ Custom Exception With Constructor 🔧

Your notes use this pattern:

```python
class BankException(Exception):

    def __init__(self, message):
        super().__init__(message)
```

Let's understand every line.

---

# 🔟 Line 1

```python
class BankException(Exception):
```

Meaning:

```text
Create BankException class
        +
inherit Exception class
```

OOP concept:

> 🧬 Inheritance

---

# 1️⃣1️⃣ Line 2 — Constructor

```python
def __init__(self, message):
```

The constructor receives the error message.

Example:

```python
BankException("Insufficient Balance")
```

So:

```text
message
   ↓
"Insufficient Balance"
```

---

# 1️⃣2️⃣ What is `self` Here? 👤

Just like normal OOP:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

`self` represents the current object.

Similarly:

```python
class BankException(Exception):

    def __init__(self, message):
        ...
```

`self` represents the current `BankException` object.

---

# 1️⃣3️⃣ What is `super()`? ⬆️

Your code:

```python
super().__init__(message)
```

`super()` allows us to access parent-class functionality according to Python's method resolution order.

Here:

```text
BankException
     │
     ▼
 Exception
```

So:

```python
super().__init__(message)
```

calls the inherited parent initialization with the error message.

---

# 1️⃣4️⃣ Execution Flow of Constructor

When we write:

```python
BankException("Insufficient Balance")
```

conceptually:

```text
BankException("Insufficient Balance")
              │
              ▼
BankException.__init__()
              │
              ▼
message = "Insufficient Balance"
              │
              ▼
super().__init__(message)
              │
              ▼
Exception.__init__(message)
```

---

# 1️⃣5️⃣ Complete Bank OOP Example 🏦

```python
class BankException(Exception):

    def __init__(self, message):
        super().__init__(message)


class Bank:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def withdraw(self, amount):

        if amount < 0:

            raise BankException(
                "Enter a valid amount"
            )

        if amount > self.balance:

            raise BankException(
                "Insufficient Balance"
            )

        self.balance -= amount


account = Bank("Ramesh", 5000)
```

---

# 1️⃣6️⃣ OOP Structure 🏗️

There are two classes:

```text
                 Exception
                     │
                     ▼
              BankException


                   Bank
                     │
                     ▼
                  account
```

Notice:

`BankException` and `Bank` have different jobs.

### `Bank`

Contains banking data and operations.

### `BankException`

Represents banking-related exceptional situations.

---

# 1️⃣7️⃣ Bank Object Memory 🧠

After:

```python
account = Bank("Ramesh", 5000)
```

conceptually:

```text
account
   │
   ▼
┌─────────────────────────┐
│ Bank Object             │
├─────────────────────────┤
│ name    = "Ramesh"      │
│ balance = 5000          │
├─────────────────────────┤
│ withdraw()              │
└─────────────────────────┘
```

---

# 1️⃣8️⃣ Valid Withdrawal ✅

```python
account.withdraw(900)
```

Inside:

```text
amount = 900
```

Check 1:

```python
if amount < 0:
```

Becomes:

```text
900 < 0
↓
False
```

Check 2:

```python
if amount > self.balance:
```

Becomes:

```text
900 > 5000
↓
False
```

Then:

```python
self.balance -= amount
```

means:

```text
5000 - 900
     ↓
4100
```

New balance:

```text
4100
```

---

# 1️⃣9️⃣ Invalid Withdrawal ❌

Suppose a fresh account has:

```text
Balance = 5000
```

and we call:

```python
account.withdraw(10000)
```

Check:

```text
10000 < 0
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
raise BankException(
    "Insufficient Balance"
)
```

executes.

---

# 2️⃣0️⃣ Complete Dry Run 🔍

```text
account.withdraw(10000)
          │
          ▼
amount = 10000
          │
          ▼
amount < 0 ?
          │
          ▼
        False
          │
          ▼
amount > self.balance ?
          │
          ▼
10000 > 5000
          │
          ▼
        True
          │
          ▼
BankException(
 "Insufficient Balance"
)
          │
          ▼
Create Exception Object
          │
          ▼
        raise
          │
          ▼
🚨 Exception generated
```

---

# 2️⃣1️⃣ Handling It

```python
try:

    account.withdraw(10000)

except BankException as e:

    print(e)
```

Flow:

```text
try
 │
 ▼
withdraw()
 │
 ▼
raise BankException
 │
 ▼
Search matching except
 │
 ▼
except BankException as e
 │
 ▼
e → Exception Object
 │
 ▼
print(e)
```

Output:

```text
Insufficient Balance
```

---

# 2️⃣2️⃣ Custom Security Exception 🔐

Now consider your Google example.

```python
class SecurityException(Exception):

    def __init__(self, message):
        super().__init__(message)
```

This represents security-related problems.

---

# 2️⃣3️⃣ Google Class

```python
class Google:

    def __init__(self, email, password, device):

        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):

        if device != self.device:

            raise SecurityException(
                "Please login using your registered device."
            )

        if email == self.email and password == self.password:

            print("Login Successful")
```

Object:

```python
google = Google(
    "ramesh@gmail.com",
    1234,
    "mobile"
)
```

---

# 2️⃣4️⃣ Memory Diagram

```text
google
  │
  ▼
┌───────────────────────────────┐
│ Google Object                 │
├───────────────────────────────┤
│ email                         │
│ "ramesh@gmail.com"            │
│                               │
│ password = 1234               │
│                               │
│ device = "mobile"             │
├───────────────────────────────┤
│ login()                       │
└───────────────────────────────┘
```

---

# 2️⃣5️⃣ Wrong Device

Call:

```python
google.login(
    "ramesh@gmail.com",
    1234,
    "laptop"
)
```

Comparison:

```python
if device != self.device:
```

Becomes:

```text
"laptop" != "mobile"
```

Result:

```text
True
```

Therefore:

```python
raise SecurityException(
    "Please login using your registered device."
)
```

---

# 2️⃣6️⃣ Catch Security Exception

```python
try:

    google.login(
        "ramesh@gmail.com",
        1234,
        "laptop"
    )

except SecurityException as e:

    print(e)
```

Output:

```text
Please login using your registered device.
```

---

# 2️⃣7️⃣ Adding Methods to Custom Exception ⚙️

Your notes also contain:

```python
class SecurityException(Exception):

    def __init__(self, message):
        super().__init__(message)

    def logout(self):
        print("Logout Successfully")

    def otp(self):
        print("Sending OTP...")
```

This demonstrates an important OOP point:

> A custom exception is still a class, so it can define methods.

---

# 2️⃣8️⃣ Why Does `e.logout()` Work?

Consider:

```python
except SecurityException as e:

    print(e)
    e.logout()
```

`e` refers to a `SecurityException` object.

And:

```python
SecurityException
```

contains:

```python
logout()
```

Therefore:

```python
e.logout()
```

works.

Conceptually:

```text
e
│
▼
SecurityException Object
│
├── exception message
├── logout()
└── otp()
```

---

# 2️⃣9️⃣ OTP Example 🔢

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
```

Handler:

```python
except SecurityException as e:

    print(e)

    e.logout()

    e.otp()
```

Possible output:

```text
Please login using your registered device.
Logout Successfully
Sending OTP...

[wait approximately 3 seconds]

OTP Verified
```

---

# 3️⃣0️⃣ Multiple Custom Exceptions ⭐

We don't need to create only one custom exception.

Suppose our login system has two problems:

```text
Wrong Username
Wrong Password
```

Create:

```python
class UsernameException(Exception):
    pass


class PasswordException(Exception):
    pass
```

---

# 3️⃣1️⃣ Login Program

```python
class Login:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def login(self, username, password):

        if username != self.username:

            raise UsernameException(
                "Invalid Username"
            )

        if password != self.password:

            raise PasswordException(
                "Invalid Password"
            )

        print("Login Successful")
```

Object:

```python
user = Login("admin", 1234)
```

---

# 3️⃣2️⃣ Multiple `except`

```python
try:

    user.login("admin", 9999)

except UsernameException as e:

    print("Username Error:", e)

except PasswordException as e:

    print("Password Error:", e)
```

Output:

```text
Password Error: Invalid Password
```

---

# 3️⃣3️⃣ Execution Flow

```text
login("admin", 9999)
        │
        ▼
username correct?
        │
       YES
        │
        ▼
password correct?
        │
        NO
        │
        ▼
PasswordException(...)
        │
        ▼
      raise
        │
        ▼
Find matching except
        │
        ├── UsernameException ❌
        │
        └── PasswordException ✅
                    │
                    ▼
             print error
```

---

# 3️⃣4️⃣ Parent Exception Can Catch Child Exception 🧬

Consider:

```python
class BankException(Exception):
    pass
```

Because:

```text
BankException
      IS-A
Exception
```

this works:

```python
try:

    raise BankException(
        "Insufficient Balance"
    )

except Exception as e:

    print(e)
```

Why?

Because `BankException` inherits from `Exception`.

---

# 3️⃣5️⃣ Specific vs General Handler

You can write:

```python
except BankException as e:
```

or:

```python
except Exception as e:
```

But when you know the specific expected error, this is clearer:

```python
except BankException as e:
```

---

# 3️⃣6️⃣ Handler Order Is Important ⚠️

Suppose:

```python
try:

    raise BankException(
        "Insufficient Balance"
    )

except Exception as e:

    print("General Error")

except BankException as e:

    print("Bank Error")
```

The general `Exception` handler already matches `BankException`, so the later specific handler cannot be reached for that exception.

Prefer:

```python
try:

    raise BankException(
        "Insufficient Balance"
    )

except BankException as e:

    print("Bank Error:", e)

except Exception as e:

    print("General Error:", e)
```

Remember:

```text
Specific Exceptions
       ↓
General Exceptions
```

---

# 3️⃣7️⃣ Exception Hierarchy 🧬

For your current level, visualize:

```text
                  Exception
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
 BankException  LoginException SecurityException
```

And we could further design:

```text
                 LoginException
                  /          \
                 /            \
                ▼              ▼
UsernameException       PasswordException
```

---

# 3️⃣8️⃣ Real-Time Shopping Example 🛒

Suppose:

```text
Available Stock = 5

Customer asks = 10
```

Create:

```python
class StockException(Exception):
    pass
```

Product:

```python
class Product:

    def __init__(self, name, stock):

        self.name = name
        self.stock = stock

    def order(self, quantity):

        if quantity <= 0:
            raise StockException(
                "Quantity must be positive"
            )

        if quantity > self.stock:
            raise StockException(
                "Insufficient Stock"
            )

        self.stock -= quantity

        print("Order Successful")
```

---

# 3️⃣9️⃣ Test It

```python
product = Product("Laptop", 5)

try:

    product.order(10)

except StockException as e:

    print(e)
```

Output:

```text
Insufficient Stock
```

---

# 4️⃣0️⃣ Real-Time Age Validation 👤

```python
class AgeException(Exception):
    pass


class User:

    def __init__(self, name, age):

        if age < 0:
            raise AgeException(
                "Age cannot be negative"
            )

        self.name = name
        self.age = age
```

Test:

```python
try:

    user = User("Ravi", -5)

except AgeException as e:

    print(e)
```

Output:

```text
Age cannot be negative
```

---

# 4️⃣1️⃣ Built-in vs Custom Exceptions

| Built-in Exceptions         | Custom Exceptions               |
| --------------------------- | ------------------------------- |
| Provided by Python          | Created by programmer           |
| `ValueError`                | `AgeException`                  |
| `TypeError`                 | `BankException`                 |
| `IndexError`                | `StockException`                |
| `KeyError`                  | `SecurityException`             |
| Runtime/language conditions | Application-specific conditions |

---

# 4️⃣2️⃣ Normal Class vs Custom Exception Class

| Normal Class                  | Custom Exception Class            |
| ----------------------------- | --------------------------------- |
| Represents application object | Represents application error      |
| `class Bank:`                 | `class BankException(Exception):` |
| Object: `Bank(...)`           | Object: `BankException(...)`      |
| Contains application data     | Contains error information        |
| Has normal methods            | Can also define methods           |
| Usually not raised            | Can be raised                     |

---

# 4️⃣3️⃣ `raise` vs Custom Exception

Don't confuse these.

### Custom exception

```python
class BankException(Exception):
    pass
```

This **defines the type of exception**.

### `raise`

```python
raise BankException(
    "Insufficient Balance"
)
```

This **signals an instance of that exception**.

Easy memory:

```text
class BankException
       ↓
Create error type


BankException(...)
       ↓
Create error object


raise
       ↓
Signal that error
```

---

# 4️⃣4️⃣ `raise` vs `except`

| `raise`                      | `except`                       |
| ---------------------------- | ------------------------------ |
| Signals exception            | Handles exception              |
| Used where error is detected | Used around calling/risky code |
| `raise BankException()`      | `except BankException:`        |
| 🚨 Problem generated         | 🛡️ Problem handled            |

---

# 4️⃣5️⃣ `Exception` vs `BankException`

| `Exception`       | `BankException`                 |
| ----------------- | ------------------------------- |
| Built-in class    | Programmer-created class        |
| Parent            | Child                           |
| General           | Specific                        |
| Built into Python | Created for bank-related errors |

---

# 4️⃣6️⃣ `self` vs `super()` ⭐

Another important interview difference:

| `self`                                | `super()`                                              |
| ------------------------------------- | ------------------------------------------------------ |
| Represents current object             | Provides access to parent behavior via MRO             |
| `self.balance`                        | `super().__init__()`                                   |
| Access current object's state/methods | Commonly used to call inherited initialization/methods |

Example:

```python
class BankException(Exception):

    def __init__(self, message):

        super().__init__(message)
```

Here:

```text
self
 ↓
Current BankException object


super()
 ↓
Parent behavior
 ↓
Exception
```

---

# 4️⃣7️⃣ Common Mistakes ❌

### ❌ Mistake 1

```python
class BankException:
    pass
```

Then trying to raise it.

Correct:

```python
class BankException(Exception):
    pass
```

---

### ❌ Mistake 2

```python
raise "Insufficient Balance"
```

Correct:

```python
raise BankException(
    "Insufficient Balance"
)
```

---

### ❌ Mistake 3

Catching everything generally:

```python
except Exception:
```

when you specifically expect:

```python
except BankException:
```

Specific handling often makes the program easier to understand.

---

### ❌ Mistake 4

General handler before specific handler:

```python
except Exception:
    ...

except BankException:
    ...
```

Prefer:

```python
except BankException:
    ...

except Exception:
    ...
```

---

### ❌ Mistake 5

Confusing creation with raising:

```python
error = BankException(
    "Insufficient Balance"
)
```

This creates an exception object, but does not by itself signal it.

To signal it:

```python
raise error
```

---

# 4️⃣8️⃣ Advantages ✅

Custom exceptions provide:

```text
✅ Meaningful error names
✅ Better program organization
✅ Easier debugging
✅ Specific exception handling
✅ Cleaner business-rule validation
✅ Better OOP design
✅ Reusable exception classes
```

---

# 4️⃣9️⃣ Disadvantages / Cautions ⚠️

Custom exceptions can become unnecessary if you create a separate exception for every tiny situation.

Possible problems:

```text
❌ Too many exception classes
❌ More code to maintain
❌ Confusing hierarchy
❌ Unnecessary complexity for simple programs
```

Create them when the error type has useful application meaning.

---

# 5️⃣0️⃣ Interview Questions & Answers 🎤

### Q1. What is a custom exception?

A custom exception is a programmer-defined exception class used for application-specific errors.

---

### Q2. How do you create one?

```python
class BankException(Exception):
    pass
```

---

### Q3. Which OOP concept is used?

**Inheritance.**

---

### Q4. Which class is normally inherited?

```python
Exception
```

---

### Q5. How do you raise a custom exception?

```python
raise BankException(
    "Insufficient Balance"
)
```

---

### Q6. How do you handle it?

```python
try:
    ...

except BankException as e:
    print(e)
```

---

### Q7. What does `e` represent?

`e` refers to the caught exception object.

---

### Q8. Why use `super()`?

To access parent-class functionality according to the inheritance/MRO chain.

Example:

```python
super().__init__(message)
```

---

### Q9. Can custom exceptions contain methods?

Yes.

Example:

```python
class SecurityException(Exception):

    def logout(self):
        print("Logout")
```

---

### Q10. Can `Exception` catch a custom exception?

Yes, when the custom exception inherits from `Exception`.

---

### Q11. Why should specific exceptions come before general ones?

Because a general handler such as:

```python
except Exception:
```

can also match many child exception types.

---

### Q12. Difference between `raise` and custom exception?

A custom exception defines an error type; `raise` signals an exception instance.

---

# 5️⃣1️⃣ MCQs 📝

### 1. Which is correct?

A.

```python
class BankException:
    pass
```

B.

```python
class BankException(Exception):
    pass
```

✅ **Answer: B**

### 2. Which OOP concept is used?

```python
class SecurityException(Exception):
```

A. Polymorphism
B. Inheritance ✅
C. Loop
D. Generator

### 3. What does `raise` do?

A. Creates a loop
B. Signals an exception ✅
C. Creates a list
D. Handles an exception

### 4. What handles `BankException` specifically?

```python
except BankException as e:
```

✅ Correct.

### 5. What does `super()` help access?

A. Child class only
B. Parent behavior through MRO ✅
C. Loop
D. Dictionary

---

# 5️⃣2️⃣ Practice Programs 💻

Practice in this order:

1. Create `AgeException`.
2. Raise it when age is negative.
3. Create `MarksException`.
4. Raise it when marks are outside `0–100`.
5. Create `BankException`.
6. Build deposit and withdrawal validation.
7. Create `LoginException`.
8. Validate username/password.
9. Create separate `UsernameException` and `PasswordException`.
10. Create `SecurityException`.
11. Validate registered device.
12. Add `logout()` to `SecurityException`.
13. Add `otp()` to `SecurityException`.
14. Create `StockException`.
15. Build a small product-ordering system.

---

# 🏆 CHAPTER 10 — FINAL SUMMARY

Remember the whole chapter with this diagram:

```text
                 OOP
                  │
                  ▼
             Inheritance
                  │
                  ▼
              Exception
                  │
                  ▼
          Custom Exception
                  │
                  ▼
       BankException(...)
                  │
                  ▼
        Exception Object
                  │
                  ▼
               raise 🚨
                  │
                  ▼
                try
                  │
                  ▼
     except BankException as e
                  │
                  ▼
             Handle Error 🛡️
```

### Step 1 — Define

```python
class BankException(Exception):
    pass
```

### Step 2 — Detect

```python
if amount > self.balance:
```

### Step 3 — Raise

```python
raise BankException(
    "Insufficient Balance"
)
```

### Step 4 — Handle

```python
try:
    account.withdraw(10000)

except BankException as e:
    print(e)
```

## ⭐ Most Important Interview Definition

> **A custom exception is a programmer-defined exception class, usually derived from Python's `Exception` class, used to represent application-specific error conditions.**

And remember this one line:

```python
class BankException(Exception):
```

It combines **Exception Handling + OOP Inheritance**.

**Next chapter: 📘 Chapter 11 — Complete Real-Time OOP Exception Project**, combining **Bank Account + Login + Security + multiple custom exceptions + `raise` + multiple `except` + `else` + `finally` + complete dry run and interview questions**.
===
# 📘 CHAPTER 11 — REAL-TIME OOP EXCEPTION HANDLING PROJECT

Now we combine the concepts from your exception-handling notes into **one complete OOP program**.

We will use:

```text
🏗️ Class & Object
🔧 Constructor
👤 self
🧬 Inheritance
⬆️ super()
🚨 raise
🛡️ Custom Exceptions
🧪 try
❌ except
✅ else
🔄 finally
```

---

# 1️⃣ What Are We Building? 🏦

We will create a small **Bank Account System**.

The system should:

```text
1. Create a bank account
2. Login with PIN
3. View balance
4. Deposit money
5. Withdraw money
6. Reject wrong PIN
7. Reject negative amounts
8. Reject withdrawal above balance
9. Use custom exceptions
10. Handle errors using try-except
```

---

# 2️⃣ Why Is This an OOP Example? 🤔

Because we represent a bank account using a class.

```python
class Bank:
    pass
```

Then create an object:

```python
account = Bank(...)
```

Conceptually:

```text
                 Bank Class
                     │
                     │ creates
                     ▼
               account Object
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        name       balance      pin
```

The object contains both:

```text
DATA
────
name
balance
pin

BEHAVIOR
────────
login()
deposit()
withdraw()
view_balance()
```

That is the basic idea of OOP:

> **Combine related data and behavior inside objects.**

---

# 3️⃣ Custom Exceptions 🚨

Our bank has three important error situations.

```text
Wrong PIN
   ↓
LoginException

Invalid Amount
   ↓
AmountException

Insufficient Balance
   ↓
BalanceException
```

Let's create them.

```python
class LoginException(Exception):
    pass


class AmountException(Exception):
    pass


class BalanceException(Exception):
    pass
```

---

# 4️⃣ OOP Concept Used Here — Inheritance 🧬

Look at:

```python
class LoginException(Exception):
```

This means:

```text
Exception
 Parent
   │
   ├───────────────┐
   ▼               ▼
LoginException   AmountException
                     │
                     ▼
              BalanceException
```

More accurately, all three independently inherit from `Exception`:

```text
                Exception
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
 LoginException AmountException BalanceException
```

This is **Hierarchical Inheritance**:

> One parent class has multiple child classes.

---

# 5️⃣ Why Separate Exceptions? 🎯

We could simply use:

```python
raise Exception("Wrong PIN")
```

and:

```python
raise Exception("Insufficient Balance")
```

But then every problem has the same general type.

Custom exceptions make the error type meaningful:

```python
raise LoginException("Invalid PIN")
```

```python
raise BalanceException("Insufficient Balance")
```

Now the calling code can handle each problem separately.

---

# 6️⃣ Create Bank Class 🏦

```python
class Bank:

    def __init__(self, name, balance, pin):

        self.name = name
        self.balance = balance
        self.pin = pin
```

---

# 7️⃣ Understanding Constructor 🔧

When we write:

```python
account = Bank(
    "Ramesh",
    5000,
    1234
)
```

Python calls:

```python
__init__()
```

Values:

```text
name    = "Ramesh"
balance = 5000
pin     = 1234
```

Then:

```python
self.name = name
```

stores:

```text
self.name
    ↓
"Ramesh"
```

Similarly:

```text
self.balance
     ↓
    5000

self.pin
   ↓
  1234
```

---

# 8️⃣ Memory Diagram 🧠

Conceptually:

```text
account
   │
   ▼
┌──────────────────────────┐
│ Bank Object              │
├──────────────────────────┤
│ name    = "Ramesh"       │
│ balance = 5000           │
│ pin     = 1234           │
├──────────────────────────┤
│ login()                  │
│ deposit()                │
│ withdraw()               │
│ view_balance()           │
└──────────────────────────┘
```

---

# 9️⃣ Login Method 🔐

Add:

```python
def login(self, pin):

    if pin != self.pin:

        raise LoginException(
            "Invalid PIN"
        )

    print("Login Successful")
```

---

# 🔟 How Login Works

Suppose stored PIN:

```text
1234
```

User enters:

```text
9999
```

Condition:

```python
if pin != self.pin:
```

becomes:

```text
9999 != 1234
      ↓
     True
```

Therefore:

```python
raise LoginException(
    "Invalid PIN"
)
```

executes.

---

# 1️⃣1️⃣ Login Flow Diagram 🔄

```text
login(9999)
    │
    ▼
pin != self.pin
    │
    ▼
9999 != 1234
    │
    ▼
   True
    │
    ▼
LoginException(...)
    │
    ▼
  raise 🚨
```

---

# 1️⃣2️⃣ Correct PIN ✅

Suppose:

```python
account.login(1234)
```

Condition:

```text
1234 != 1234
      ↓
     False
```

So `raise` does not execute.

Next:

```python
print("Login Successful")
```

Output:

```text
Login Successful
```

---

# 1️⃣3️⃣ Deposit Method 💰

Now add:

```python
def deposit(self, amount):

    if amount <= 0:

        raise AmountException(
            "Deposit amount must be positive"
        )

    self.balance += amount

    print("Amount Deposited:", amount)
```

---

# 1️⃣4️⃣ Why Check `amount <= 0`?

These should not be accepted:

```text
deposit(-500) ❌
deposit(0)    ❌
```

But:

```text
deposit(500)  ✅
```

So:

```python
if amount <= 0:
```

handles both zero and negative values.

---

# 1️⃣5️⃣ Deposit Dry Run 🔍

Current balance:

```text
5000
```

Call:

```python
account.deposit(2000)
```

Step 1:

```text
amount = 2000
```

Step 2:

```python
amount <= 0
```

becomes:

```text
2000 <= 0
    ↓
False
```

Step 3:

```python
self.balance += amount
```

means:

```text
5000 + 2000
     ↓
7000
```

Object changes:

```text
BEFORE

balance
  ↓
5000


AFTER

balance
  ↓
7000
```

---

# 1️⃣6️⃣ Invalid Deposit ❌

Call:

```python
account.deposit(-500)
```

Condition:

```text
-500 <= 0
    ↓
True
```

Therefore:

```python
raise AmountException(
    "Deposit amount must be positive"
)
```

---

# 1️⃣7️⃣ Withdrawal Method 💸

Now:

```python
def withdraw(self, amount):

    if amount <= 0:

        raise AmountException(
            "Withdrawal amount must be positive"
        )

    if amount > self.balance:

        raise BalanceException(
            "Insufficient Balance"
        )

    self.balance -= amount

    print("Amount Withdrawn:", amount)
```

---

# 1️⃣8️⃣ Why Two Conditions?

Because withdrawal can fail for two different reasons.

### Problem 1

```python
account.withdraw(-500)
```

This is an invalid amount.

Therefore:

```text
AmountException
```

### Problem 2

```python
account.withdraw(10000)
```

when balance is:

```text
5000
```

This is insufficient balance.

Therefore:

```text
BalanceException
```

---

# 1️⃣9️⃣ Withdrawal Dry Run — Valid Case 🔍

Current balance:

```text
5000
```

Call:

```python
account.withdraw(1000)
```

### Step 1

```text
amount = 1000
```

### Step 2

```python
if amount <= 0:
```

```text
1000 <= 0
    ↓
False
```

### Step 3

```python
if amount > self.balance:
```

```text
1000 > 5000
    ↓
False
```

### Step 4

```python
self.balance -= amount
```

```text
5000 - 1000
     ↓
4000
```

New balance:

```text
4000
```

---

# 2️⃣0️⃣ Withdrawal Dry Run — Insufficient Balance 🚨

Current balance:

```text
5000
```

Call:

```python
account.withdraw(10000)
```

First:

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

Therefore:

```python
raise BalanceException(
    "Insufficient Balance"
)
```

Program immediately leaves the normal method flow and looks for a matching handler.

---

# 2️⃣1️⃣ View Balance Method 👀

Simple:

```python
def view_balance(self):

    print(
        "Current Balance:",
        self.balance
    )
```

Call:

```python
account.view_balance()
```

Output:

```text
Current Balance: 5000
```

---

# 2️⃣2️⃣ Complete Bank Class 🏦

```python
class Bank:

    def __init__(self, name, balance, pin):

        self.name = name
        self.balance = balance
        self.pin = pin

    def login(self, pin):

        if pin != self.pin:
            raise LoginException(
                "Invalid PIN"
            )

        print("Login Successful")

    def deposit(self, amount):

        if amount <= 0:
            raise AmountException(
                "Deposit amount must be positive"
            )

        self.balance += amount

        print(
            "Amount Deposited:",
            amount
        )

    def withdraw(self, amount):

        if amount <= 0:
            raise AmountException(
                "Withdrawal amount must be positive"
            )

        if amount > self.balance:
            raise BalanceException(
                "Insufficient Balance"
            )

        self.balance -= amount

        print(
            "Amount Withdrawn:",
            amount
        )

    def view_balance(self):

        print(
            "Current Balance:",
            self.balance
        )
```

---

# 2️⃣3️⃣ Object Creation

```python
account = Bank(
    "Ramesh",
    5000,
    1234
)
```

Now:

```text
account
   ↓
Bank Object
   ↓
name    = Ramesh
balance = 5000
pin     = 1234
```

---

# 2️⃣4️⃣ Using `try-except` 🛡️

Let's test login.

```python
try:

    account.login(9999)

except LoginException as e:

    print("Login Error:", e)
```

Output:

```text
Login Error: Invalid PIN
```

---

# 2️⃣5️⃣ What Exactly Happens? ⭐

This is an important interview concept.

```python
account.login(9999)
```

calls:

```python
login()
```

Inside:

```python
raise LoginException(
    "Invalid PIN"
)
```

Python creates a `LoginException` object.

Conceptually:

```text
┌─────────────────────────┐
│ LoginException Object   │
├─────────────────────────┤
│ "Invalid PIN"           │
└─────────────────────────┘
```

Then `raise` signals it.

Python searches for:

```python
except LoginException as e:
```

It matches.

Now:

```text
e
│
▼
LoginException Object
```

So:

```python
print(e)
```

prints:

```text
Invalid PIN
```

---

# 2️⃣6️⃣ Handling Deposit Exception

```python
try:

    account.deposit(-500)

except AmountException as e:

    print("Amount Error:", e)
```

Output:

```text
Amount Error: Deposit amount must be positive
```

---

# 2️⃣7️⃣ Handling Withdrawal Exception

```python
try:

    account.withdraw(10000)

except BalanceException as e:

    print("Balance Error:", e)
```

Output:

```text
Balance Error: Insufficient Balance
```

---

# 2️⃣8️⃣ Multiple `except` Blocks ⭐

Now combine them:

```python
try:

    account.withdraw(10000)

except LoginException as e:

    print("Login Error:", e)

except AmountException as e:

    print("Amount Error:", e)

except BalanceException as e:

    print("Balance Error:", e)

except Exception as e:

    print("Unknown Error:", e)
```

Python selects the matching handler.

Here:

```text
BalanceException
```

is raised.

Therefore:

```python
except BalanceException as e:
```

runs.

---

# 2️⃣9️⃣ Why Put `Exception` Last? ⚠️

Because:

```python
Exception
```

is the parent class.

Our custom exceptions are children:

```text
                  Exception
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
LoginException AmountException BalanceException
```

Therefore, put specific handlers first:

```python
except LoginException:
```

```python
except AmountException:
```

```python
except BalanceException:
```

and general:

```python
except Exception:
```

last.

---

# 3️⃣0️⃣ Using `else` ✅

Remember:

> `else` executes when the `try` block finishes without an exception.

Example:

```python
try:

    account.withdraw(1000)

except BalanceException as e:

    print(e)

else:

    print("Transaction Completed")
```

If withdrawal succeeds:

```text
Amount Withdrawn: 1000
Transaction Completed
```

---

# 3️⃣1️⃣ Flow of `else`

```text
             try
              │
       ┌──────┴──────┐
       │             │
 Exception       No Exception
       │             │
       ▼             ▼
    except          else
```

Remember:

```text
Exception ❌
   ↓
except


No Exception ✅
   ↓
else
```

---

# 3️⃣2️⃣ Using `finally` 🔄

Definition:

> **`finally` executes whether an exception occurs or not.**

Example:

```python
try:

    account.withdraw(1000)

except BalanceException as e:

    print(e)

else:

    print("Transaction Successful")

finally:

    print("Transaction Finished")
```

---

# 3️⃣3️⃣ Successful Case

Suppose balance:

```text
5000
```

withdraw:

```text
1000
```

Output:

```text
Amount Withdrawn: 1000
Transaction Successful
Transaction Finished
```

Because:

```text
try       ✅
except    ❌
else      ✅
finally   ✅
```

---

# 3️⃣4️⃣ Error Case

Suppose:

```text
Balance    = 5000
Withdrawal = 10000
```

Output:

```text
Balance Error: Insufficient Balance
Transaction Finished
```

Flow:

```text
try       🚨 exception
except    ✅
else      ❌
finally   ✅
```

---

# 3️⃣5️⃣ `try-except-else-finally` Flow ⭐

```text
                     START
                       │
                       ▼
                      try
                       │
             ┌─────────┴─────────┐
             │                   │
        Exception            No Exception
             │                   │
             ▼                   ▼
           except               else
             │                   │
             └─────────┬─────────┘
                       │
                       ▼
                    finally
                       │
                       ▼
                      END
```

This diagram is very important.

---

# 3️⃣6️⃣ Complete Program ⭐

```python
# ==========================================
# CUSTOM EXCEPTIONS
# ==========================================

class LoginException(Exception):
    pass


class AmountException(Exception):
    pass


class BalanceException(Exception):
    pass


# ==========================================
# BANK CLASS
# ==========================================

class Bank:

    def __init__(self, name, balance, pin):

        self.name = name
        self.balance = balance
        self.pin = pin

    def login(self, pin):

        if pin != self.pin:
            raise LoginException(
                "Invalid PIN"
            )

        print("Login Successful")

    def deposit(self, amount):

        if amount <= 0:
            raise AmountException(
                "Deposit amount must be positive"
            )

        self.balance += amount

        print(
            "Amount Deposited:",
            amount
        )

    def withdraw(self, amount):

        if amount <= 0:
            raise AmountException(
                "Withdrawal amount must be positive"
            )

        if amount > self.balance:
            raise BalanceException(
                "Insufficient Balance"
            )

        self.balance -= amount

        print(
            "Amount Withdrawn:",
            amount
        )

    def view_balance(self):

        print(
            "Current Balance:",
            self.balance
        )


# ==========================================
# OBJECT CREATION
# ==========================================

account = Bank(
    "Ramesh",
    5000,
    1234
)


# ==========================================
# EXCEPTION HANDLING
# ==========================================

try:

    account.login(1234)

    account.view_balance()

    account.deposit(2000)

    account.withdraw(1000)

except LoginException as e:

    print("Login Error:", e)

except AmountException as e:

    print("Amount Error:", e)

except BalanceException as e:

    print("Balance Error:", e)

except Exception as e:

    print("Unknown Error:", e)

else:

    print("All Operations Successful")

finally:

    print("Bank Application Closed")
```

---

# 3️⃣7️⃣ Dry Run of Complete Program 🔍

Initial object:

```text
name    = Ramesh
balance = 5000
pin     = 1234
```

### Step 1

```python
account.login(1234)
```

Check:

```text
1234 != 1234
      ↓
False
```

Output:

```text
Login Successful
```

---

### Step 2

```python
account.view_balance()
```

Output:

```text
Current Balance: 5000
```

---

### Step 3

```python
account.deposit(2000)
```

Calculation:

```text
5000 + 2000
     ↓
7000
```

Output:

```text
Amount Deposited: 2000
```

---

### Step 4

```python
account.withdraw(1000)
```

Calculation:

```text
7000 - 1000
     ↓
6000
```

Output:

```text
Amount Withdrawn: 1000
```

---

### Step 5

No exception occurred.

Therefore:

```python
else:
```

executes.

Output:

```text
All Operations Successful
```

---

### Step 6

Finally:

```python
finally:
```

executes.

Output:

```text
Bank Application Closed
```

---

# 3️⃣8️⃣ Final Output

```text
Login Successful
Current Balance: 5000
Amount Deposited: 2000
Amount Withdrawn: 1000
All Operations Successful
Bank Application Closed
```

Final balance:

```text
6000
```

---

# 3️⃣9️⃣ What Happens If Login Fails? 🔐

Change:

```python
account.login(1234)
```

to:

```python
account.login(9999)
```

Then:

```text
9999 != 1234
      ↓
True
```

So:

```python
raise LoginException(
    "Invalid PIN"
)
```

executes.

Python immediately leaves the remaining `try` block.

Therefore these will **not execute**:

```python
account.view_balance()
account.deposit(2000)
account.withdraw(1000)
```

It goes directly to:

```python
except LoginException as e:
```

Output:

```text
Login Error: Invalid PIN
Bank Application Closed
```

Notice:

```python
else:
```

doesn't execute.

But:

```python
finally:
```

still executes.

---

# 4️⃣0️⃣ Very Important Concept ⭐

Suppose:

```python
try:

    print("A")

    print(10 / 0)

    print("B")

except ZeroDivisionError:

    print("Error")
```

Output:

```text
A
Error
```

Not:

```text
A
Error
B
```

Why?

As soon as an exception occurs:

```text
try
 │
 ├── statement 1 ✅
 │
 ├── statement 2 🚨
 │
 └── statement 3 ❌ skipped
          │
          ▼
       except
```

---

# 4️⃣1️⃣ `raise` vs `except` vs `else` vs `finally`

| Keyword      | Purpose                 |
| ------------ | ----------------------- |
| 🚨 `raise`   | Signal an exception     |
| 🛡️ `except` | Handle exception        |
| ✅ `else`     | Run when `try` succeeds |
| 🔄 `finally` | Run regardless          |

---

# 4️⃣2️⃣ Built-in vs Custom Exception

| Built-in                        | Custom                        |
| ------------------------------- | ----------------------------- |
| Python provides it              | Programmer creates it         |
| `ValueError`                    | `AmountException`             |
| `TypeError`                     | `LoginException`              |
| `IndexError`                    | `BalanceException`            |
| General Python/runtime problems | Application-specific problems |

---

# 4️⃣3️⃣ `print()` vs `raise`

### `print()`

```python
print("Insufficient Balance")
```

Means:

> Show this message.

### `raise`

```python
raise BalanceException(
    "Insufficient Balance"
)
```

Means:

> An exceptional condition occurred; signal it to the caller.

---

# 4️⃣4️⃣ Common Mistakes ❌

### ❌ Mistake 1 — Wrong exception class

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

### ❌ Mistake 2 — Raising string

```python
raise "Error"
```

Correct:

```python
raise Exception("Error")
```

---

### ❌ Mistake 3 — Negative deposit accepted

Bad:

```python
self.balance += amount
```

without validation.

Better:

```python
if amount <= 0:
    raise AmountException(
        "Amount must be positive"
    )
```

---

### ❌ Mistake 4 — No balance validation

Bad:

```python
self.balance -= amount
```

Better:

```python
if amount > self.balance:
    raise BalanceException(
        "Insufficient Balance"
    )
```

---

### ❌ Mistake 5 — General exception first

Avoid:

```python
except Exception:
    ...

except BalanceException:
    ...
```

Prefer:

```python
except BalanceException:
    ...

except Exception:
    ...
```

Specific first, general last.

---

# 4️⃣5️⃣ Advantages ✅

This approach gives us:

```text
✅ Better code organization
✅ OOP-based design
✅ Meaningful error types
✅ Easier debugging
✅ Business-rule validation
✅ Specific error handling
✅ Reusable exception classes
✅ Cleaner separation of responsibilities
```

---

# 4️⃣6️⃣ Disadvantages / Cautions ⚠️

For very small programs, too many custom exception classes can make the code unnecessarily complex.

Also:

```text
❌ Too many exception classes
❌ Poorly designed exception hierarchy
❌ Catching everything with Exception
❌ Ignoring errors
❌ Using exceptions for ordinary control flow
```

can reduce readability.

---

# 4️⃣7️⃣ Interview Questions & Answers 🎤

### Q1. What is exception handling?

Exception handling is a mechanism used to handle runtime errors so the program can respond appropriately instead of terminating unexpectedly.

### Q2. What is a custom exception?

A custom exception is a programmer-defined exception class used for application-specific errors.

### Q3. Which OOP concept is used in custom exceptions?

**Inheritance.**

```python
class BankException(Exception):
    pass
```

### Q4. What does `raise` do?

It explicitly signals an exception.

### Q5. What does `except` do?

It handles a matching exception.

### Q6. When does `else` execute?

When the `try` block completes without an exception.

### Q7. When does `finally` execute?

It normally executes regardless of whether an exception occurred.

### Q8. Why use custom exceptions?

To represent application-specific problems with meaningful exception types.

### Q9. Can we have multiple `except` blocks?

Yes.

### Q10. Why put `Exception` last?

Because it is a general parent class and can catch many child exception types.

### Q11. What is `as e`?

`e` refers to the caught exception object.

### Q12. Can custom exception classes have methods?

Yes, because they are classes.

---

# 4️⃣8️⃣ MCQs 📝

**1. Which keyword signals an exception?**

A. `try`
B. `raise` ✅
C. `else`
D. `finally`

**2. Which handles an exception?**

A. `except` ✅
B. `raise`
C. `return`
D. `yield`

**3. Which executes when `try` succeeds?**

A. `except`
B. `raise`
C. `else` ✅
D. `yield`

**4. Which block is commonly used for cleanup?**

A. `finally` ✅
B. `if`
C. `for`
D. `raise`

**5. What concept is this?**

```python
class LoginException(Exception):
    pass
```

A. Encapsulation
B. Inheritance ✅
C. Looping
D. Generator

---

# 4️⃣9️⃣ Practice Programs 💻

Try these one by one:

1. 🧑 Create `AgeException` for invalid age.
2. 🎓 Create `MarksException` for marks outside `0–100`.
3. 💰 Create `SalaryException` for negative salary.
4. 🏦 Create `BankException` for insufficient balance.
5. 🔐 Create `LoginException` for wrong PIN.
6. 📱 Create `SecurityException` for an unregistered device.
7. 🛒 Create `StockException` for insufficient stock.
8. 💳 Create `PaymentException` for invalid payment amount.
9. 🏧 Build ATM withdrawal with three custom exceptions.
10. 🏦 Build the complete Bank system above without looking at the solution.

---

# 🏆 CHAPTER 11 — FINAL SUMMARY

The complete concept is:

```text
                  OOP
                   │
                   ▼
            Create Classes
                   │
       ┌───────────┴───────────┐
       ▼                       ▼
    Bank Class            Exception Classes
       │                       │
       ▼                       ▼
 Bank Object              Inheritance
       │                       │
       │                       ▼
       │                   Exception
       │
       ▼
Check Business Rules
       │
       ▼
Problem Found?
       │
    ┌──┴──┐
    │     │
   NO    YES
    │     │
    ▼     ▼
Continue raise 🚨
          │
          ▼
    Exception Object
          │
          ▼
       except 🛡️
          │
          ▼
      Handle Error
```

Remember these six concepts:

```text
🧪 try
   → Put risky code here

🛡️ except
   → Handle the error

✅ else
   → Runs when try succeeds

🔄 finally
   → Cleanup / normally runs regardless

🚨 raise
   → Explicitly signal an exception

🧬 Custom Exception
   → Application-specific exception class
```

And the most important OOP connection:

```python
class BalanceException(Exception):
    pass
```

means:

```text
Exception
    │
    │ 🧬 Inheritance
    ▼
BalanceException
```

Then:

```python
raise BalanceException(
    "Insufficient Balance"
)
```

signals the problem, and:

```python
except BalanceException as e:
```

handles it.

## ⭐ One-Line Interview Answer

> **In an OOP application, custom exceptions are programmer-defined exception classes derived from `Exception`, while `raise`, `try`, `except`, `else`, and `finally` are used to signal and manage exceptional conditions.**

### 📚 Exception Handling Learning Path Completed So Far

```text
✅ Errors & Exceptions
        ↓
✅ try-except
        ↓
✅ Specific Exceptions
        ↓
✅ Multiple except
        ↓
✅ Exception as e
        ↓
✅ else
        ↓
✅ finally
        ↓
✅ raise
        ↓
✅ Custom Exceptions
        ↓
✅ OOP + Exception Handling
        ↓
🏆 Real-Time Bank Application
```

**Next chapter: 📘 Chapter 12 — Exception Handling Interview Preparation**, covering **beginner → advanced interview questions, output questions, tricky programs, debugging questions, MCQs, coding questions, and a final interview cheat sheet**.
