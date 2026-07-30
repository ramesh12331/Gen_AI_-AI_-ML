Below is your code in **clean VS Code format** with proper spacing, comments, headings, and indentation.

```python
# ==========================================================
# PYTHON INHERITANCE
# Parent Constructor + Child Constructor
# ==========================================================

class Car:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        print("Brand :", self.brand)
        print("Price :", self.price)


# ----------------------------------------------------------
# Parent Object
# ----------------------------------------------------------

c = Car("BMW", 450000)
c.get_info()


# ==========================================================
# Child Class
# ==========================================================

class NewCar(Car):

    def __init__(self, brand, price, color, model):

        # Call Parent Constructor
        super().__init__(brand, price)

        # Child Variables
        self.color = color
        self.model = model


# ----------------------------------------------------------
# Child Object
# ----------------------------------------------------------

n = NewCar("BMW", 450000, "Red", "Basic Model")

print("\nBrand :", n.brand)
print("Price :", n.price)
print("Color :", n.color)
print("Model :", n.model)

# ==========================================================
# OUTPUT
# ==========================================================
# Brand : BMW
# Price : 450000
# Color : Red
# Model : Basic Model
```

---

# Inheriting Parent Method

```python
# ==========================================================
# INHERITING PARENT METHOD
# ==========================================================

class Car:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        print("Brand :", self.brand)
        print("Price :", self.price)


class NewCar(Car):

    def __init__(self, brand, price, color, model):

        super().__init__(brand, price)

        self.color = color
        self.model = model


n = NewCar("BMW", 450000, "Red", "Basic Model")

# Calling Parent Method
n.get_info()

# ==========================================================
# OUTPUT
# ==========================================================
# Brand : BMW
# Price : 450000
```

---

# Method Overriding

```python
# ==========================================================
# METHOD OVERRIDING
# ==========================================================

class Car:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        print(self.brand, self.price)


class NewCar(Car):

    def __init__(self, brand, price, color, model):

        super().__init__(brand, price)

        self.color = color
        self.model = model

    # Overriding Parent Method
    def get_info(self):
        print("Brand :", self.brand)
        print("Price :", self.price)
        print("Color :", self.color)
        print("Model :", self.model)


n = NewCar("BMW", 450000, "Red", "Basic Model")

n.get_info()

# ==========================================================
# OUTPUT
# ==========================================================
# Brand : BMW
# Price : 450000
# Color : Red
# Model : Basic Model
```

---

# Class Variable Example

```python
# ==========================================================
# CLASS VARIABLE
# ==========================================================

class Car:

    wheels = 4      # Class Variable

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


class NewCar(Car):

    def __init__(self, brand, price, color, model):

        super().__init__(brand, price)

        self.color = color
        self.model = model


n = NewCar("BMW", 450000, "Red", "Basic Model")

print("Wheels :", n.wheels)

# ==========================================================
# OUTPUT
# ==========================================================
# Wheels : 4
```

---

# Child Method Example

```python
# ==========================================================
# CHILD METHOD
# ==========================================================

class Car:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


class NewCar(Car):

    def __init__(self, brand, price, color, model):

        super().__init__(brand, price)

        self.color = color
        self.model = model

    def set_price(self, amount):

        self.price += amount

        print("Updated Price :", self.price)


n = NewCar("BMW", 450000, "Red", "Basic Model")

n.set_price(300)

# ==========================================================
# OUTPUT
# ==========================================================
# Updated Price : 450300
```

---

# Bank Application Using Inheritance

```python
# ==========================================================
# BANK APPLICATION USING INHERITANCE
# ==========================================================

# ----------------------------------------------------------
# Parent Class
# ----------------------------------------------------------

class Bank:

    def __init__(self, pin, balance):

        self.pin = pin
        self.balance = balance

    # Deposit
    def deposit(self, amount):

        self.balance += amount

        print("Amount Deposited Successfully")

    # Withdraw
    def withdraw(self, amount):

        if amount > 0:

            if amount <= self.balance:

                self.balance -= amount

                print("Withdrawal Successful")

            else:

                print("Insufficient Balance")

        else:

            print("Invalid Amount")

    # View Balance
    def view_balance(self):

        print("Current Balance :", self.balance)


# ----------------------------------------------------------
# Child Class
# ----------------------------------------------------------

class SavingsAccount(Bank):

    def __init__(self, pin, balance, interest_rate):

        super().__init__(pin, balance)

        self.interest_rate = interest_rate

    # Add Interest
    def add_interest(self):

        interest = self.balance * self.interest_rate / 100

        self.balance += interest

        print("Interest Added :", interest)


# ----------------------------------------------------------
# Object
# ----------------------------------------------------------

account = SavingsAccount("1234", 5000, 10)

account.view_balance()

account.add_interest()

account.view_balance()

# ==========================================================
# OUTPUT
# ==========================================================
# Current Balance : 5000
# Interest Added : 500.0
# Current Balance : 5500.0
```

---

# Common Errors in Inheritance

```python
# ==========================================================
# ERROR 1
# ==========================================================

# Wrong
n = NewCar("Red", "Basic Model")

# TypeError:
# Missing required arguments
```

```python
# Correct

n = NewCar(
    "BMW",
    450000,
    "Red",
    "Basic Model"
)
```

---

```python
# ==========================================================
# ERROR 2
# ==========================================================

AttributeError:
'NewCar' object has no attribute 'color'
```

### Reason

You forgot to initialize the variables.

```python
self.color = color
self.model = model
```

---

```python
# ==========================================================
# ERROR 3
# ==========================================================

self.ir = ir

def ir(self):
    pass
```

### Problem

Variable name and method name are the same.

```python
self.ir = 10
```

Later,

```python
n.ir()
```

Python thinks `ir` is an integer, not a function.

So it gives:

```text
TypeError: 'int' object is not callable
```

---

### Correct Solution

```python
class SavingsAccount(Bank):

    def __init__(self, pin, balance, interest_rate):

        super().__init__(pin, balance)

        self.interest_rate = interest_rate

    def add_interest(self):

        interest = self.balance * self.interest_rate / 100

        self.balance += interest

        print("Interest Added :", interest)
```

---

## Topics Covered

* ✅ Inheritance
* ✅ Parent Class
* ✅ Child Class
* ✅ `super()` Function
* ✅ Constructor Inheritance
* ✅ Method Inheritance
* ✅ Method Overriding
* ✅ Class Variable
* ✅ Child Method
* ✅ Bank Application using Inheritance
* ✅ Common Inheritance Errors and Solutions

This version is clean, properly indented, and ready to paste directly into **VS Code**.
---
Yes, I reviewed your screenshots. The remaining topic in your class after **Inheritance** is **Encapsulation**.

Below is the same content rewritten in **clean VS Code format**.

---

```python
# ==========================================================
# PYTHON ENCAPSULATION
# ==========================================================

# Access Modifiers in Python
#
# 1. Public
# 2. Protected
# 3. Private
```

---

# 1. Public Members

```python
# ==========================================================
# PUBLIC MEMBERS
# ==========================================================

class Shop:

    def __init__(self, product, price, pin):

        self.product = product
        self.price = price
        self.pin = pin

    def view(self):

        print("Product :", self.product)
        print("Price   :", self.price)
        print("PIN     :", self.pin)


s = Shop("Santoor", 5000, 1234)

print(s.product)
print(s.price)
print(s.pin)

s.view()

# ----------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------
# Santoor
# 5000
# 1234
# Product : Santoor
# Price   : 5000
# PIN     : 1234
```

---

# 2. Protected Members

```python
# ==========================================================
# PROTECTED MEMBERS
# Single Underscore (_)
# ==========================================================

class Shop:

    def __init__(self, product, price, pin):

        self.product = product
        self._price = price
        self._pin = pin

    def view(self):

        print(self.product)
        print(self._price)
        print(self._pin)


s = Shop("Santoor", 5000, 1234)

s.view()

print(s._price)
print(s._pin)

# ----------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------
# Santoor
# 5000
# 1234
# 5000
# 1234
```

> **Note:** `_variable` means **Protected**. It is only a convention. Python still allows access.

---

# 3. Inheritance with Protected Members

```python
# ==========================================================
# PROTECTED VARIABLE IN CHILD CLASS
# ==========================================================

class Shop:

    def __init__(self, product, price, pin):

        self.product = product
        self._price = price
        self._pin = pin


class Shop1(Shop):

    def info(self):

        print(self.product)
        print(self._price)
        print(self._pin)


s1 = Shop1("Santoor", 5000, 1234)

s1.info()

# ----------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------
# Santoor
# 5000
# 1234
```

---

# 4. Private Members

```python
# ==========================================================
# PRIVATE MEMBERS
# Double Underscore (__)
# ==========================================================

class Shop:

    def __init__(self, product, price, pin):

        self.product = product
        self.__price = price
        self.__pin = pin

    def view(self):

        print(self.product)
        print(self.__price)
        print(self.__pin)


s = Shop("Santoor", 5000, 1234)

s.view()

# ----------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------
# Santoor
# 5000
# 1234
```

---

# Private Variable Error

```python
# ==========================================================
# ERROR
# ==========================================================

class Shop:

    def __init__(self, product, price):

        self.product = product
        self.__price = price


s = Shop("Santoor", 5000)

print(s.__price)
```

### Output

```
AttributeError:
'Shop' object has no attribute '__price'
```

---

# Name Mangling

Python internally changes:

```python
self.__price
```

to

```python
self._Shop__price
```

So it can be accessed like this (not recommended):

```python
class Shop:

    def __init__(self, product, price):

        self.product = product
        self.__price = price


s = Shop("Santoor", 5000)

print(s._Shop__price)

# ----------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------
# 5000
```

---

# Public vs Protected vs Private

| Access Type | Syntax   | Accessible Outside Class | Accessible in Child |
| ----------- | -------- | ------------------------ | ------------------- |
| Public      | `name`   | ✅ Yes                    | ✅ Yes               |
| Protected   | `_name`  | ✅ Yes (Convention)       | ✅ Yes               |
| Private     | `__name` | ❌ No                     | ❌ No (Directly)     |

---

# Important Interview Questions

### Q1. What is Encapsulation?

**Answer:**

Encapsulation is the process of **wrapping data (variables) and methods (functions) into a single class** and controlling direct access to data.

---

### Q2. What are the access modifiers in Python?

* Public
* Protected
* Private

---

### Q3. Difference between `_name` and `__name`?

* `_name` → Protected (only a convention)
* `__name` → Private (uses Name Mangling)

---

### Q4. What is Name Mangling?

Python changes

```python
__price
```

into

```python
_ClassName__price
```

Example:

```python
__price
```

becomes

```python
_Shop__price
```

---

## Topics Covered

* ✅ Encapsulation
* ✅ Public Members
* ✅ Protected Members
* ✅ Private Members
* ✅ Name Mangling
* ✅ Protected Variables with Inheritance
* ✅ Access Modifiers
* ✅ Common Errors
* ✅ Interview Questions

This version matches the clean **VS Code format** used in your previous Python notes and is ready to paste directly into a `.py` file.
