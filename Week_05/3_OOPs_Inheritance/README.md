Excellent! This completes the **Inheritance** topic in Python OOP. Your notes cover:

* ✅ Single Inheritance
* ✅ Multilevel Inheritance
* ✅ Multiple Inheritance
* ✅ Hierarchical Inheritance
* ✅ Hybrid Inheritance (Theory)
* ✅ Method Resolution Order (MRO)
* ✅ `super()` Function
* ✅ Constructor Inheritance
* ✅ Method Inheritance
* ✅ Method Overriding
* ✅ Polymorphism (Introduction)
* ✅ Real-Time Bank Application
* ✅ Common Errors
* ✅ Interview Questions 

Now let's make it into a **complete interview handbook**.

---

# 📘 Python OOP Master Handbook

# 📖 Chapter 3 – Inheritance (Beginner to Interview Level)

> ⭐ **Inheritance** is one of the **four pillars of OOP** and one of the **most frequently asked interview topics**. It allows one class to reuse the properties and methods of another class, reducing code duplication and improving maintainability.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand Inheritance
* ✅ Create Parent and Child classes
* ✅ Use `super()`
* ✅ Understand MRO
* ✅ Perform Method Overriding
* ✅ Learn all five types of Inheritance
* ✅ Build real-world applications using Inheritance
* ✅ Answer interview questions confidently

---

# 📖 What is Inheritance?

## ✅ Definition

**Inheritance** is a mechanism in which a **Child Class acquires the variables and methods of a Parent Class**.

Instead of rewriting code, we reuse existing code.

---

## Real-Life Example

```text
Animal
 ├── Dog
 ├── Cat
 └── Cow
```

* Animal → Parent Class
* Dog, Cat, Cow → Child Classes

---

# 📖 Parent Class vs Child Class

| Parent Class     | Child Class         |
| ---------------- | ------------------- |
| Base Class       | Derived Class       |
| Super Class      | Sub Class           |
| Gives properties | Inherits properties |

---

# 📖 Why Do We Use Inheritance?

Without Inheritance:

```text
Dog
eat()

Cat
eat()

Cow
eat()
```

The same code is written multiple times.

With Inheritance:

```text
Animal
   │
 eat()
   │
 ├── Dog
 ├── Cat
 └── Cow
```

The `eat()` method is written once and reused.

---

# 📖 Syntax

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

# 📖 Single Inheritance

## Definition

One Parent → One Child

```text
Animal
   │
 Dog
```

### Example

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

Output

```text
Animal Sound
Bow Bow
```

---

# 📖 Multilevel Inheritance

## Definition

One child becomes the parent of another child.

```text
Animal
   │
 Dog
   │
 Cat
```

### Example

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def bark(self):
        print("Bow Bow")

class Cat(Dog):
    def meow(self):
        print("Meow Meow")

c = Cat()

c.sound()
c.bark()
c.meow()
```

---

# 📖 Multiple Inheritance

## Definition

One child inherits from more than one parent.

```text
Animal      Bird
     \      /
      \    /
       Duck
```

### Example

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Bird:
    def fly(self):
        print("Flying")

class Duck(Animal, Bird):
    pass

d = Duck()

d.sound()
d.fly()
```

---

# 📖 Hierarchical Inheritance

## Definition

One Parent → Multiple Children

```text
      Animal
     /   |   \
   Dog  Cat  Cow
```

All child classes inherit the parent methods.

---

# 📖 Hybrid Inheritance

## Definition

A combination of two or more inheritance types.

Example:

* Single + Multiple
* Multilevel + Hierarchical

Python supports Hybrid Inheritance using combinations of inheritance patterns.

---

# 📖 Method Resolution Order (MRO)

When a method exists in multiple parent classes, Python searches classes in a specific order.

Example

```python
class A:
    def display(self):
        print("A")

class B:
    def display(self):
        print("B")

class C(A, B):
    pass

obj = C()

obj.display()

print(C.mro())
```

Output

```text
A
[C, A, B, object]
```

Python searches **from left to right**.

---

# 📖 `super()` Function

## Definition

`super()` is used to call the parent class constructor or methods.

### Example

```python
class Car:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class NewCar(Car):

    def __init__(self, brand, price, color):

        super().__init__(brand, price)

        self.color = color
```

---

## Why Use `super()`?

Without `super()`:

```python
self.brand = brand
self.price = price
```

This repeats the parent's code.

With `super()`:

```python
super().__init__(brand, price)
```

The parent constructor handles initialization.

---

# 📖 Constructor Inheritance

A child constructor can call the parent constructor using `super()`.

Example

```python
class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course
```

---

# 📖 Method Inheritance

Child classes automatically inherit methods from the parent.

Example

```python
class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

dog = Dog()

dog.eat()
```

---

# 📖 Method Overriding

## Definition

When a child class defines a method with the same name as the parent class, the child version replaces the parent version.

Example

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

# 📖 Calling Parent Method with `super()`

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog Sound")

Dog().sound()
```

Output

```text
Animal Sound
Dog Sound
```

---

# 🌍 Real-World Example – Bank Application

```text
Bank
 ├── view_balance()
 ├── deposit()
 └── withdraw()

        │

SavingsAccount
 └── add_interest()
```

The child class reuses all banking features and adds interest calculation.

---

# 📊 Types of Inheritance

| Type         | Structure                        |
| ------------ | -------------------------------- |
| Single       | Parent → Child                   |
| Multilevel   | Parent → Child → Grandchild      |
| Multiple     | Two Parents → One Child          |
| Hierarchical | One Parent → Multiple Children   |
| Hybrid       | Combination of inheritance types |

---

# 📊 Method Overloading vs Method Overriding

| Method Overloading                         | Method Overriding                    |
| ------------------------------------------ | ------------------------------------ |
| Same method name with different parameters | Same method name in parent and child |
| Limited in Python                          | Fully supported                      |
| Compile-time concept (other languages)     | Runtime polymorphism                 |

---

# 🌍 Advantages of Inheritance

* ✅ Code Reusability
* ✅ Less Code
* ✅ Easy Maintenance
* ✅ Better Organization
* ✅ Faster Development
* ✅ Easy Extension
* ✅ Supports Polymorphism

---

# ⚠ Disadvantages

* ❌ Poor design can create tight coupling.
* ❌ Deep inheritance trees become difficult to understand.
* ❌ Debugging can become more complex.

---

# 💡 Programmer Tips

```text
Inheritance
     │
Reuse Existing Code
```

```text
super()
   │
Call Parent Constructor
```

```text
MRO
 │
Left → Right Search
```

```text
Overriding
     │
Child Replaces Parent Method
```

---

# 🎓 Top 20 Interview Questions

### Basic

1. What is Inheritance?
2. Why do we use Inheritance?
3. What is a Parent Class?
4. What is a Child Class?
5. What are the advantages of Inheritance?

### Types

6. What is Single Inheritance?
7. What is Multilevel Inheritance?
8. What is Multiple Inheritance?
9. What is Hierarchical Inheritance?
10. What is Hybrid Inheritance?

### `super()`

11. What is `super()`?
12. Why do we use `super()`?
13. Can `super()` call parent methods?
14. Can `super()` call constructors?

### Advanced

15. What is MRO?
16. How does Python search for methods?
17. What is Method Overriding?
18. Difference between Overloading and Overriding?
19. Can Python support Multiple Inheritance?
20. How do you check MRO?

---

# ⭐ MCQs

### Q1. Which keyword is used to call the parent constructor?

A. `parent`

B. `base`

C. `super`

D. `self`

✅ **Answer:** **C**

---

### Q2. Which inheritance has one parent and one child?

A. Multiple

B. Hybrid

C. Single

D. Hierarchical

✅ **Answer:** **C**

---

### Q3. Which function shows the Method Resolution Order?

A. `dir()`

B. `help()`

C. `mro()`

D. `type()`

✅ **Answer:** **C**

---

### Q4. Method Overriding occurs when:

A. Parent and child have methods with the same name.

B. Two classes have different method names.

C. Variables are inherited.

D. Objects are copied.

✅ **Answer:** **A**

---

# 📝 Practice Programs

## ⭐ Easy

Create:

* `Vehicle`
* `Bike`

Inherit the `start()` method.

---

## ⭐⭐ Medium

Create:

* `Person`
* `Employee`

Use `super()` to initialize the parent constructor.

---

## ⭐⭐⭐ Challenge

Create:

* `Bank`
* `SavingsAccount`

Add:

* `deposit()`
* `withdraw()`
* `view_balance()`
* `add_interest()`

Use inheritance and `super()`.

---

# 📌 Chapter Summary

```text
                     INHERITANCE
                          │
         ┌────────────────┼────────────────┐
         │                │                │
      Single        Multilevel       Multiple
         │                │                │
  Parent → Child   Parent→Child→GC   Two Parents
         │
    Hierarchical
         │
 One Parent → Many Children
         │
       Hybrid
         │
 Combination of Types
         │
      super()
         │
 Parent Constructor
         │
         MRO
         │
 Left → Right Search
         │
  Method Overriding
```

---

# 🏆 Congratulations!

You have completed **Python OOP – Chapter 3: Inheritance**.

### ✅ You learned:

* Inheritance
* Single, Multilevel, Multiple, Hierarchical & Hybrid Inheritance
* Parent & Child Classes
* `super()` Function
* Constructor & Method Inheritance
* Method Resolution Order (MRO)
* Method Overriding
* Real-world Bank Application
* Interview Questions
* MCQs
* Practice Programs

## 📖 Next Chapter

**Chapter 4 – Encapsulation**

We'll learn:

* 🔒 Public Members
* 🔒 Protected Members
* 🔒 Private Members
* 🔒 Name Mangling
* 🔒 Getter & Setter with Encapsulation
* 🔒 Real-world examples
* 🔒 Interview Questions
* 🔒 MCQs
* 🔒 Practice Programs
----
# 📘 Python OOP Master Handbook

# 📖 Chapter 4 – Encapsulation (Beginner to Interview Level)

> ⭐ **Encapsulation** is one of the **4 Pillars of OOP** and is a **very common interview topic**. It helps protect data by controlling how it is accessed and modified.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand Encapsulation
* ✅ Learn Public, Protected, and Private Members
* ✅ Understand Name Mangling
* ✅ Control access to object data
* ✅ Write secure OOP programs
* ✅ Answer interview questions confidently

---

# 📖 1. What is Encapsulation?

## ✅ Definition

**Encapsulation** is the process of **wrapping data (variables) and methods (functions) together into a single class** while controlling access to the data.

It helps in:

* Data Hiding
* Security
* Better Code Organization

---

## 🌍 Real-Life Example

### 🏦 ATM Machine

```text
ATM Machine
     │
 ┌── PIN (Hidden)
 ├── Balance (Protected)
 └── Deposit/Withdraw (Methods)
```

You cannot directly change the balance or PIN. You must use the ATM's methods.

---

# 📖 Why Do We Need Encapsulation?

Without Encapsulation:

```python
account.balance = -50000
```

Anyone can modify data.

With Encapsulation:

```python
account.withdraw(500)
```

The class checks whether the operation is valid.

---

# 📖 Access Modifiers in Python

Python supports three types of members:

| Modifier  | Syntax   | Access                     |
| --------- | -------- | -------------------------- |
| Public    | `name`   | Anywhere                   |
| Protected | `_name`  | Class & Child (convention) |
| Private   | `__name` | Inside class only          |

---

# 📖 2. Public Members

## ✅ Definition

Public members can be accessed **from anywhere**.

### Example

```python
class Shop:

    def __init__(self, product, price):
        self.product = product
        self.price = price

shop = Shop("Laptop", 50000)

print(shop.product)
print(shop.price)
```

### Output

```text
Laptop
50000
```

---

## Memory Diagram

```text
Shop Object

↓

product

↓

Accessible Everywhere
```

---

# 📖 3. Protected Members

## ✅ Definition

Protected members begin with a **single underscore (`_`)**.

```python
self._price
```

It is a **convention**, meaning:

> "Please don't access this directly outside the class."

Python **still allows access**.

---

### Example

```python
class Shop:

    def __init__(self, product, price):
        self.product = product
        self._price = price

shop = Shop("Laptop", 50000)

print(shop._price)
```

### Output

```text
50000
```

---

# 📖 Protected Members in Inheritance

```python
class Shop:

    def __init__(self):
        self._price = 5000

class OnlineShop(Shop):

    def show_price(self):
        print(self._price)

s = OnlineShop()

s.show_price()
```

### Output

```text
5000
```

Protected members are intended for use by child classes.

---

# 📖 4. Private Members

## ✅ Definition

Private members begin with **double underscores (`__`)**.

```python
self.__price
```

Private members cannot be accessed directly outside the class.

---

### Example

```python
class Shop:

    def __init__(self):
        self.__price = 5000

shop = Shop()

# print(shop.__price)
```

### Output

```text
AttributeError
```

---

# 📖 Why Does This Error Occur?

Python performs **Name Mangling**.

Internally,

```python
self.__price
```

becomes

```text
_Shop__price
```

This prevents accidental access.

---

# 📖 Name Mangling

Example

```python
class Shop:

    def __init__(self):
        self.__price = 5000

shop = Shop()

print(shop._Shop__price)
```

### Output

```text
5000
```

⚠️ Although possible, this is **not recommended**. Access private data through methods instead.

---

# 📖 Using Getter and Setter with Private Members

### Getter

```python
class Shop:

    def __init__(self):
        self.__price = 5000

    def get_price(self):
        return self.__price

shop = Shop()

print(shop.get_price())
```

---

### Setter

```python
class Shop:

    def __init__(self):
        self.__price = 5000

    def set_price(self, value):
        if value > 0:
            self.__price = value

shop = Shop()

shop.set_price(6000)

print(shop.get_price())
```

---

# 📊 Public vs Protected vs Private

| Feature               | Public         | Protected               | Private       |
| --------------------- | -------------- | ----------------------- | ------------- |
| Syntax                | `name`         | `_name`                 | `__name`      |
| Access Outside Class  | ✅ Yes          | ✅ Yes (not recommended) | ❌ No          |
| Access in Child Class | ✅ Yes          | ✅ Yes                   | ❌ Directly No |
| Purpose               | General access | Internal use            | Data hiding   |

---

# 🌍 Real-World Example – Bank Account

```python
class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = Bank(10000)

account.deposit(2000)

account.withdraw(3000)

print(account.get_balance())
```

### Output

```text
9000
```

Notice that `__balance` is protected from direct modification.

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Trying to access a private variable directly.

Wrong

```python
print(shop.__price)
```

Correct

```python
print(shop.get_price())
```

---

## ❌ Mistake 2

Using Name Mangling in normal programs.

Wrong

```python
print(shop._Shop__price)
```

Use a getter instead.

---

## ❌ Mistake 3

Thinking `_price` is private.

```python
_price
```

is only **Protected**, not Private.

---

# 💡 Programmer Tips

```text
Public
   │
Open for Everyone
```

```text
Protected
     │
For Class & Child
```

```text
Private
    │
Hidden Data
```

```text
Getter
   │
Read Data
```

```text
Setter
   │
Update Data Safely
```

---

# 🎓 Top Interview Questions

### Basic

1. What is Encapsulation?
2. Why do we use Encapsulation?
3. What are Access Modifiers?

### Public / Protected / Private

4. What is a Public Member?
5. What is a Protected Member?
6. What is a Private Member?
7. Difference between `_name` and `__name`?

### Advanced

8. What is Name Mangling?
9. Why does Python use Name Mangling?
10. Can we access private variables?
11. What is a Getter Method?
12. What is a Setter Method?
13. Why are Getter and Setter methods useful?
14. Is `_name` truly private?
15. How does Encapsulation improve security?

---

# ⭐ MCQs

### Q1. Which symbol represents a private member?

A. `name`

B. `_name`

C. `__name`

D. `***name`

✅ **Answer:** **C**

---

### Q2. Which access modifier is only a naming convention?

A. Public

B. Protected

C. Private

D. Global

✅ **Answer:** **B**

---

### Q3. Name Mangling changes:

```python
__price
```

to:

A. `_price`

B. `price`

C. `_ClassName__price`

D. `price__`

✅ **Answer:** **C**

---

### Q4. Which method is mainly used to read private data?

A. Constructor

B. Getter

C. Destructor

D. Lambda

✅ **Answer:** **B**

---

# 📝 Practice Programs

## ⭐ Easy

Create a `Student` class with:

* Public → `name`
* Protected → `_marks`
* Private → `__roll_no`

Print the public value and access the private value using a getter.

---

## ⭐⭐ Medium

Create an `Employee` class with:

* Private salary
* Getter
* Setter (allow only positive salary)

---

## ⭐⭐⭐ Challenge

Create a `BankAccount` class with:

* Private `__balance`
* Deposit
* Withdraw
* Getter for balance
* Prevent negative deposits and overdrafts

---

# 📌 Chapter Summary

```text
                  ENCAPSULATION
                        │
          ┌─────────────┼─────────────┐
          │             │             │
      Public       Protected      Private
          │             │             │
        name         _name        __name
          │             │             │
   Anywhere     Class & Child     Inside Class
                        │
                 Name Mangling
                        │
               _ClassName__variable
                        │
                 Getter / Setter
                        │
              Secure Data Access
```

---

# 🏆 Congratulations!

You have now completed **4 major OOP topics**:

* ✅ OOP Basics (Class & Object)
* ✅ Constructors, `self`, Getter & Setter
* ✅ Inheritance
* ✅ Encapsulation

These topics form the foundation of object-oriented programming and are commonly asked in Python interviews.

---

# 📖 Next Chapter

## **Chapter 5 – Polymorphism & Abstraction**

We'll cover:

* 🔄 Polymorphism
* 🔁 Method Overriding (deep dive)
* 🎭 Abstraction
* 📦 Abstract Base Classes (`ABC`)
* 🧩 `@abstractmethod`
* 🌍 Real-world examples
* 🎓 Interview Questions
* ⭐ MCQs
* 📝 Practice Programs
---