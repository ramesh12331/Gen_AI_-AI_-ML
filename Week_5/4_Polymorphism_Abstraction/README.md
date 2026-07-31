# 📘 Python OOP Master Handbook

# 🎯 Final Summary – Chapter 5: Polymorphism & Abstraction (Beginner to Interview Level)

> ⭐ This chapter covers **Polymorphism** and **Abstraction**, two of the **4 Pillars of OOP**. These topics are among the **most frequently asked Python interview questions**.

---

# 📖 PART 1 – POLYMORPHISM

---

# ✅ Definition

**Poly** = Many

**Morph** = Forms

**Polymorphism** means **one object, operator, or method behaves in many different ways depending on the situation**.

### Simple Definition (Interview)

> **Polymorphism is the ability of the same operator or method to perform different actions depending on the object or data type.**

---

# 🌍 Real-Life Examples

### Example 1 – Human

```text
Person

↓

Teacher at School

↓

Father at Home

↓

Customer in Shop
```

One person → Many Roles

---

### Example 2 – '+' Operator

```python
10 + 20
```

Output

```text
30
```

```python
"10" + "20"
```

Output

```text
1020
```

Same operator

Different behavior

This is Polymorphism.

---

# ✅ Types of Polymorphism

```text
                Polymorphism
                      │
      ┌───────────────┼───────────────┐
      │               │               │
Method          Method          Operator
Overloading     Overriding      Overloading
```

---

# 📖 1. Operator Overloading

## ✅ Definition

**Operator Overloading** means **giving a new meaning to operators (`+`, `-`, `*`, `>`, `<`, etc.) for user-defined objects** using **Magic (Dunder) Methods**.

---

## Syntax

```python
class ClassName:

    def __add__(self, other):
        return value
```

---

## Example

```python
class Account:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance


a = Account(3000)
b = Account(5000)

print(a + b)
```

### Output

```text
8000
```

---

## Internal Working

When Python sees

```python
a + b
```

Internally it executes

```python
a.__add__(b)
```

Where

```text
self = a

other = b
```

---

# 📖 2. Comparison Operator Overloading

## Greater Than (`__gt__`)

### Syntax

```python
def __gt__(self, other):
    return self.value > other.value
```

### Example

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student(80)
s2 = Student(70)

print(s1 > s2)
```

Output

```text
True
```

---

## Less Than (`__lt__`)

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks
```

---

# 📖 3. Magic Methods (Dunder Methods)

## Definition

Magic Methods are **special methods that start and end with double underscores (`__`)**.

They allow Python to customize the behavior of operators and built-in functions.

---

## Common Magic Methods

| Operator     | Magic Method    | Example        |
| ------------ | --------------- | -------------- |
| `+`          | `__add__()`     | `a + b`        |
| `-`          | `__sub__()`     | `a - b`        |
| `*`          | `__mul__()`     | `a * b`        |
| `/`          | `__truediv__()` | `a / b`        |
| `==`         | `__eq__()`      | `a == b`       |
| `>`          | `__gt__()`      | `a > b`        |
| `<`          | `__lt__()`      | `a < b`        |
| `>=`         | `__ge__()`      | `a >= b`       |
| `<=`         | `__le__()`      | `a <= b`       |
| `print(obj)` | `__str__()`     | Display object |

---

# 📖 4. `__str__()` Method

## Definition

`__str__()` controls what is displayed when we print an object.

### Example

```python
class Student:

    def __str__(self):
        return "Hello Student"


s = Student()

print(s)
```

### Output

```text
Hello Student
```

---

# 📖 5. Method Overriding

## Definition

A child class provides its own implementation of a parent class method.

### Syntax

```python
class Parent:

    def show(self):
        pass


class Child(Parent):

    def show(self):
        pass
```

---

## Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bow Bow")


Dog().sound()
```

Output

```text
Bow Bow
```

---

# 📖 6. Method Overloading

## Definition

Method Overloading means multiple methods with the same name but different parameters.

### Important Note

❌ **Python does NOT support Method Overloading directly.**

The last method definition replaces the previous ones.

---

## Alternative Methods

### Using Default Arguments

```python
class A:

    def add(self, a, b=0, c=0):
        return a + b + c
```

---

### Using `None`

```python
def add(self, a, b=None, c=None):
```

---

### Using `*args`

```python
def add(self, *values):
    return sum(values)
```

---

### Using `**kwargs`

```python
def details(self, **values):
    print(values)
```

---

# 🌍 Advantages of Polymorphism

* ✔ Flexible Code
* ✔ Code Reusability
* ✔ Easy Extension
* ✔ Cleaner Programs
* ✔ Better Maintenance

---

# ⚠ Common Beginner Mistakes

### Wrong

```python
a + b
```

Without defining

```python
__add__()
```

Result

```text
TypeError
```

---

### Wrong

```python
class A:

    def add(self,a):

    def add(self,a,b):
```

Python keeps only the last method.

---

# 🎓 Interview Questions

1. What is Polymorphism?
2. What are the types of Polymorphism?
3. What is Operator Overloading?
4. What are Magic Methods?
5. What is `__add__()`?
6. What is `__str__()`?
7. Does Python support Method Overloading?
8. What is Method Overriding?
9. Difference between Overloading and Overriding?
10. What are `*args` and `**kwargs`?

---

# ⭐ MCQs

### Q1. Which method overloads `+`?

A. `__sum__()`

B. `__plus__()`

C. `__add__()`

D. `__addition__()`

✅ **Answer:** **C**

---

### Q2. Which method changes object printing?

A. `__display__()`

B. `__show__()`

C. `__str__()`

D. `__print__()`

✅ **Answer:** **C**

---

# 📌 Final Summary (Polymorphism)

```text
POLYMORPHISM
      │
One Thing
Many Forms
      │
Operator Overloading
Method Overriding
Method Overloading*
      │
Magic Methods
      │
__add__()
__str__()
__gt__()
__lt__()
```

> *Python simulates method overloading using default arguments, `*args`, or `**kwargs`.

---

# 📖 PART 2 – ABSTRACTION

---

# ✅ Definition

**Abstraction** means **hiding implementation details and showing only the essential features to the user**.

The user knows **what to do**, not **how it works internally**.

---

# 🌍 Real-Life Examples

### ATM Machine

```text
ATM

↓

Withdraw Money

↓

User doesn't know

how ATM works internally.
```

---

### Car

```text
Drive Car

↓

Press Start Button

↓

Engine process is hidden.
```

---

# ✅ Why Use Abstraction?

* Hide complex logic
* Improve security
* Reduce complexity
* Make programs easier to use

---

# 📖 Abstract Class

## Definition

An **Abstract Class** is a class that contains **one or more Abstract Methods**.

It **cannot be instantiated directly**.

---

## Syntax

```python
from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def security(self):
        pass
```

---

# 📖 Abstract Method

## Definition

An **Abstract Method** is a method declared without implementation.

Every child class **must implement it**.

---

## Example

```python
from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def security(self):
        pass


class Mobile(Bank):

    def security(self):
        print("Mobile Security")


m = Mobile()

m.security()
```

Output

```text
Mobile Security
```

---

# 📖 Important Rules

✅ Import

```python
from abc import ABC, abstractmethod
```

✅ Inherit from

```python
ABC
```

✅ Use

```python
@abstractmethod
```

---

# 📖 Error Example

```python
class Desktop(Bank):
    pass

d = Desktop()
```

Output

```text
TypeError

Can't instantiate abstract class
```

Reason

The child class did not implement the abstract method.

---

# 📖 Correct Example

```python
class Desktop(Bank):

    def security(self):
        print("Desktop Security")
```

Now object creation works correctly.

---

# 🌍 Real-Time Example

```text
           Bank (Abstract)

             security()

                │

      ┌─────────┴─────────┐

   Mobile             Desktop

security()          security()
```

Each child provides its own implementation.

---

# 📊 Abstract Class vs Normal Class

| Normal Class                    | Abstract Class                        |
| ------------------------------- | ------------------------------------- |
| Object can be created           | Object cannot be created              |
| Methods may have implementation | Contains one or more abstract methods |
| Used directly                   | Used as a blueprint                   |

---

# 🌍 Advantages of Abstraction

* ✔ Hides internal implementation
* ✔ Improves Security
* ✔ Reduces Complexity
* ✔ Forces Child Classes to implement required methods
* ✔ Better Software Design

---

# ⚠ Common Beginner Mistakes

### Wrong

```python
class Mobile(Bank):
    pass
```

Result

```text
TypeError
```

---

### Correct

```python
class Mobile(Bank):

    def security(self):
        print("Security")
```

---

# 🎓 Interview Questions

1. What is Abstraction?
2. Why do we use Abstraction?
3. What is an Abstract Class?
4. What is an Abstract Method?
5. Can we create an object of an Abstract Class?
6. Why do we inherit from `ABC`?
7. What is `@abstractmethod`?
8. What happens if a child class does not implement an abstract method?
9. Difference between Abstraction and Encapsulation?
10. Real-life examples of Abstraction?

---

# ⭐ MCQs

### Q1. Which module provides Abstract Classes?

A. `math`

B. `abc`

C. `os`

D. `sys`

✅ **Answer:** **B**

---

### Q2. Which decorator creates an abstract method?

A. `@override`

B. `@staticmethod`

C. `@abstractmethod`

D. `@property`

✅ **Answer:** **C**

---

# 📌 Final Summary (Abstraction)

```text
ABSTRACTION
      │
Hide Implementation
      │
Abstract Class (ABC)
      │
Abstract Method
      │
@abstractmethod
      │
Child Must Implement
      │
Better Security
Less Complexity
```

---

# 📊 Encapsulation vs Abstraction

| Encapsulation                   | Abstraction                 |
| ------------------------------- | --------------------------- |
| Hides data                      | Hides implementation        |
| Uses Public, Protected, Private | Uses Abstract Classes       |
| Getter & Setter                 | `ABC` and `@abstractmethod` |
| Focus: Data Security            | Focus: Simplicity           |

---

# 🚀 30-Second Interview Revision

```text
✔ Polymorphism means one object or operator behaves in many forms.
✔ Types: Operator Overloading, Method Overriding, Method Overloading (simulated).
✔ Magic Methods (__add__, __str__, __gt__, __lt__) customize operator behavior.
✔ Python does not support true method overloading directly.

✔ Abstraction hides implementation details and shows only essential features.
✔ Abstract Classes inherit from ABC.
✔ Abstract Methods use @abstractmethod.
✔ Abstract Classes cannot be instantiated directly.
✔ Child classes must implement all abstract methods.
```

# 🏆 OOP Complete Revision

You have now completed all **4 Pillars of Object-Oriented Programming (OOP)**:

* ✅ **Inheritance** – Reuse code from parent classes.
* ✅ **Encapsulation** – Protect data using controlled access.
* ✅ **Polymorphism** – One interface, many behaviors.
* ✅ **Abstraction** – Hide implementation and expose only essential functionality.

With these concepts, you have a strong foundation for Python OOP and common technical interviews.
