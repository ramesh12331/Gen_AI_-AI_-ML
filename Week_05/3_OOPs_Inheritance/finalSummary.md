# 📘 Python OOP Master Handbook

# 🎯 Final Summary – Chapter 3 (Inheritance) & Chapter 4 (Encapsulation)

> This is a **one-shot interview revision** covering **Definitions, Syntax, Examples, Differences, Interview Questions, MCQs, and Final Mind Maps** for **Inheritance** and **Encapsulation**. It summarizes the concepts covered in your notes. 

---

# 📖 CHAPTER 3 – INHERITANCE

---

# ✅ Definition

**Inheritance** is an OOP feature in which one class (**Child Class**) acquires the **variables (properties)** and **methods (behaviors)** of another class (**Parent Class**).

It allows **code reusability** and avoids writing the same code multiple times.

---

# 🌍 Real-Life Examples

```text
Animal
 ├── Dog
 ├── Cat
 └── Cow
```

```text
Vehicle
 ├── Car
 ├── Bike
 └── Bus
```

```text
Person
 ├── Student
 └── Employee
```

---

# ✅ Syntax

## Single Inheritance

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## Multiple Inheritance

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

---

## Multilevel Inheritance

```python
class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass
```

---

# ✅ Simple Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Bow Bow")


dog = Dog()

dog.sound()

dog.bark()
```

### Output

```text
Animal Sound
Bow Bow
```

---

# ✅ Types of Inheritance

| Type         | Diagram                          |
| ------------ | -------------------------------- |
| Single       | Parent → Child                   |
| Multilevel   | Parent → Child → Grandchild      |
| Multiple     | Parent1 + Parent2 → Child        |
| Hierarchical | Parent → Many Children           |
| Hybrid       | Combination of inheritance types |

---

# ✅ super() Function

### Definition

`super()` is used to call the **parent class constructor or methods**.

### Syntax

```python
super().__init__(arguments)
```

### Example

```python
class Car:

    def __init__(self, brand):
        self.brand = brand


class NewCar(Car):

    def __init__(self, brand, color):

        super().__init__(brand)

        self.color = color
```

---

# ✅ Method Overriding

### Definition

When a **child class provides its own implementation** of a parent class method.

### Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bow Bow")


Dog().sound()
```

### Output

```text
Bow Bow
```

---

# ✅ MRO (Method Resolution Order)

### Definition

MRO defines the order in which Python searches for methods in inherited classes.

### Example

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.mro())
```

Output

```text
[C, A, B, object]
```

Python searches **Left → Right**.

---

# ✅ Advantages of Inheritance

* ✔ Code Reusability
* ✔ Less Code
* ✔ Easy Maintenance
* ✔ Better Organization
* ✔ Faster Development
* ✔ Supports Method Overriding

---

# ❌ Disadvantages

* Deep inheritance becomes difficult to understand.
* Tight coupling if not designed properly.
* Debugging becomes harder.

---

# 🎓 Interview Questions

1. What is Inheritance?
2. Why do we use Inheritance?
3. What is a Parent Class?
4. What is a Child Class?
5. What is `super()`?
6. What is Method Overriding?
7. What is MRO?
8. What are the five types of Inheritance?
9. Difference between Single and Multiple Inheritance?
10. What are the advantages of Inheritance?

---

# ⭐ MCQs

### Q1. Which keyword calls the parent constructor?

A. parent

B. self

C. super

D. object

✅ **Answer:** C

---

### Q2. Which inheritance has one parent and one child?

A. Multiple

B. Hybrid

C. Single

D. Hierarchical

✅ **Answer:** C

---

# 📌 Final Summary (Inheritance)

```text
INHERITANCE
     │
Reuse Parent Code
     │
Parent → Child
     │
Single
Multiple
Multilevel
Hierarchical
Hybrid
     │
super()
     │
MRO
     │
Method Overriding
```

---

# 📖 CHAPTER 4 – ENCAPSULATION

---

# ✅ Definition

**Encapsulation** is the process of **wrapping variables (data) and methods (functions) into a single class** and controlling access to the data.

It is used for **data hiding** and **security**.

---

# 🌍 Real-Life Example

```text
ATM Machine

↓

PIN Hidden

↓

Deposit / Withdraw using methods
```

---

# ✅ Access Modifiers

| Type      | Syntax   | Access                     |
| --------- | -------- | -------------------------- |
| Public    | `name`   | Anywhere                   |
| Protected | `_name`  | Class & Child (Convention) |
| Private   | `__name` | Inside Class               |

---

# ✅ Public Members

### Definition

Public members can be accessed from anywhere.

### Example

```python
class Student:

    def __init__(self):
        self.name = "Ramesh"


s = Student()

print(s.name)
```

---

# ✅ Protected Members

### Definition

Protected members start with a **single underscore (`_`)**.

They are meant for internal use and child classes, but Python still allows access from outside.

### Example

```python
class Student:

    def __init__(self):
        self._marks = 95


s = Student()

print(s._marks)
```

---

# ✅ Private Members

### Definition

Private members start with **double underscores (`__`)**.

They cannot be accessed directly from outside the class.

### Example

```python
class Student:

    def __init__(self):
        self.__roll = 101

    def get_roll(self):
        return self.__roll


s = Student()

print(s.get_roll())
```

---

# ✅ Name Mangling

### Definition

Python internally changes:

```python
__price
```

into

```python
_ClassName__price
```

Example

```python
class Shop:

    def __init__(self):
        self.__price = 5000


s = Shop()

print(s._Shop__price)
```

---

# ✅ Getter Method

### Definition

A Getter Method is used to **read private data**.

### Syntax

```python
def get_value(self):
    return self.__value
```

---

# ✅ Setter Method

### Definition

A Setter Method is used to **update private data safely**.

### Syntax

```python
def set_value(self, value):
    self.__value = value
```

---

# 📊 Public vs Protected vs Private

| Feature       | Public | Protected          | Private       |
| ------------- | ------ | ------------------ | ------------- |
| Syntax        | `name` | `_name`            | `__name`      |
| Outside Class | ✅ Yes  | ✅ Yes (Convention) | ❌ No          |
| Child Class   | ✅ Yes  | ✅ Yes              | ❌ Directly No |
| Security      | Low    | Medium             | High          |

---

# ✅ Advantages of Encapsulation

* ✔ Data Hiding
* ✔ Better Security
* ✔ Easy Maintenance
* ✔ Better Control
* ✔ Reusable Code

---

# ❌ Disadvantages

* Slightly more code because of Getter and Setter methods.
* Improper design may reduce flexibility.

---

# 🎓 Interview Questions

1. What is Encapsulation?
2. Why do we use Encapsulation?
3. What are Access Modifiers?
4. What is a Public Member?
5. What is a Protected Member?
6. What is a Private Member?
7. What is Name Mangling?
8. Difference between `_name` and `__name`?
9. What is a Getter Method?
10. What is a Setter Method?

---

# ⭐ MCQs

### Q1. Which symbol represents a Private member?

A. `_`

B. `__`

C. `***`

D. `#`

✅ **Answer:** **B**

---

### Q2. Which access modifier is only a naming convention?

A. Public

B. Protected

C. Private

D. Global

✅ **Answer:** **B**

---

# 📌 Final Summary (Encapsulation)

```text
ENCAPSULATION
      │
Data Hiding
      │
Public
Protected
Private
      │
Getter
Setter
      │
Name Mangling
      │
Secure Data Access
```

---

# 📝 Chapter 3 vs Chapter 4

| Feature          | Inheritance                           | Encapsulation                             |
| ---------------- | ------------------------------------- | ----------------------------------------- |
| Purpose          | Reuse code                            | Protect data                              |
| Main Idea        | Child inherits Parent                 | Hide internal data                        |
| Keyword          | `class Child(Parent)`                 | `__variable`, Getter, Setter              |
| Benefits         | Code Reusability                      | Data Security                             |
| Common Functions | `super()`, `mro()`                    | Getter, Setter                            |
| Interview Focus  | Types of Inheritance, MRO, Overriding | Public, Protected, Private, Name Mangling |

---

# 🚀 30-Second Interview Revision

```text
✔ Inheritance allows one class to reuse another class's variables and methods.
✔ Five types: Single, Multiple, Multilevel, Hierarchical, Hybrid.
✔ super() calls the parent constructor or methods.
✔ MRO decides the order of method lookup.
✔ Method Overriding lets a child redefine a parent method.

✔ Encapsulation wraps data and methods into one class.
✔ It provides data hiding and security.
✔ Public → name
✔ Protected → _name
✔ Private → __name
✔ Getter reads data.
✔ Setter updates data safely.
✔ Python uses Name Mangling for private members.
```

# 🏆 Congratulations!

You have now completed the **core OOP concepts** in Python:

* ✅ Chapter 1 – Class & Object
* ✅ Chapter 2 – Constructor, `self`, Variables, Getter & Setter
* ✅ Chapter 3 – Inheritance
* ✅ Chapter 4 – Encapsulation

These topics form the foundation for advanced Python development and are among the most frequently asked concepts in Python interviews.
