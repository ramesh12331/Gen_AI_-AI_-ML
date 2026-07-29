Excellent! Since you've completed Functions, Collections, Lambda, the next major topic is **Object-Oriented Programming (OOP)**.

We'll learn it **chapter by chapter** in the same interview style.

---

# 📘 Python OOP Master Handbook

# 📖 Chapter 1 – Introduction to OOP, Class, Object & Constructor (`__init__`) (Beginner to Interview Level)

> ⭐ OOP (Object-Oriented Programming) is one of the **most important Python interview topics**. It is widely used in **Django, Flask, Automation, Desktop Applications, APIs, and Enterprise Software**.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand OOP
* ✅ Understand Class
* ✅ Understand Object
* ✅ Understand Constructor (`__init__`)
* ✅ Understand Instance Variables
* ✅ Create your own objects
* ✅ Answer interview questions confidently

---

# 📖 What is OOP?

## ✅ Definition

**Object-Oriented Programming (OOP)** is a programming style where we organize programs using **Classes** and **Objects**.

Instead of writing everything in one place, we group related **data (variables)** and **functions (methods)** together.

---

## 🌍 Real-Life Examples

| Real World | Class    | Object         |
| ---------- | -------- | -------------- |
| Bank       | Bank     | SBI            |
| Student    | Student  | Ramesh         |
| Car        | Car      | Swift          |
| Mobile     | Mobile   | Samsung Galaxy |
| Employee   | Employee | Rahul          |

---

# 📖 What is a Class?

## ✅ Definition

A **Class** is a **blueprint (template)** used to create objects.

It defines:

* Variables (Data)
* Methods (Functions)

---

## Syntax

```python
class ClassName:

    # Variables

    # Methods
```

---

## Example

```python
class Student:
    pass
```

Here,

`Student` is a Class.

Nothing has been created yet.

---

## Memory Diagram

```text
Student Class

↓

Blueprint

↓

No Memory for Student Yet
```

---

# 📖 What is an Object?

## ✅ Definition

An **Object** is a **real instance of a Class**.

Objects occupy memory.

---

## Syntax

```python
object_name = ClassName()
```

---

## Example

```python
class Student:
    pass

s1 = Student()

print(s1)
```

Output

```text
<__main__.Student object at 0x...>
```

Python creates a Student object in memory.

---

## Memory Diagram

```text
Student Class

↓

Create Object

↓

s1

↓

Memory Allocated
```

---

# 📖 Why Do We Need a Constructor?

Suppose we create a Bank account.

Every customer has:

* Name
* Age
* Branch

Instead of assigning values one by one, Python provides a **Constructor**.

---

# 📖 Constructor (`__init__`)

## ✅ Definition

A **Constructor** is a special method that is **called automatically whenever an object is created**.

---

## Syntax

```python
class Student:

    def __init__(self):
        print("Constructor Called")
```

---

## Example

```python
class Student:

    def __init__(self):
        print("Constructor Executed")

s1 = Student()
```

Output

```text
Constructor Executed
```

Notice:

We never called `__init__()` directly.

Python called it automatically.

---

# 📖 Constructor with Parameters

Example

```python
class Bank:

    def __init__(self, user_name, user_age, user_branch):

        self.name = user_name
        self.age = user_age
        self.branch = user_branch
```

---

# 📖 Understanding `self`

`self` refers to the **current object**.

Whenever an object is created,

```python
b = Bank(...)
```

Python internally does something like:

```python
Bank.__init__(b, ...)
```

So,

```python
self
```

means

```text
Current Object
```

---

# 📖 Instance Variables

Variables created using

```python
self.variable_name
```

are called **Instance Variables**.

Example

```python
self.name = user_name
self.age = user_age
self.branch = user_branch
```

Each object gets its own copy.

---

# 📖 Creating an Object

```python
b = Bank(
    "Annu",
    25,
    "Hyderabad"
)
```

Python performs these steps:

### Step 1

Creates memory for object.

↓

### Step 2

Calls Constructor.

↓

### Step 3

Stores values.

↓

### Step 4

Returns object reference.

---

## Dry Run

```text
Bank()

↓

Memory Created

↓

__init__()

↓

self.name = "Annu"

↓

self.age = 25

↓

self.branch = Hyderabad

↓

Object Ready
```

---

# 📖 Accessing Instance Variables

### Using Object

```python
print(b.name)

print(b.age)

print(b.branch)
```

Output

```text
Annu

25

Hyderabad
```

---

# 📖 Complete Example

```python
class Bank:

    def __init__(self, name, age, branch):

        self.name = name
        self.age = age
        self.branch = branch


customer = Bank(
    "Ramesh",
    24,
    "Hyderabad"
)

print(customer.name)
print(customer.age)
print(customer.branch)
```

Output

```text
Ramesh

24

Hyderabad
```

---

# 📊 Class vs Object

| Class               | Object           |
| ------------------- | ---------------- |
| Blueprint           | Real instance    |
| No memory allocated | Memory allocated |
| Defines properties  | Uses properties  |
| Template            | Actual data      |

---

# 📊 Constructor vs Normal Method

| Constructor                   | Normal Method        |
| ----------------------------- | -------------------- |
| `__init__()`                  | Any method name      |
| Called automatically          | Called manually      |
| Initializes object            | Performs operations  |
| Runs once per object creation | Runs whenever called |

---

# 🌍 Real-Life Example

### Student Class

```python
class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks


s1 = Student("Ajay", 90)

print(s1.name)
print(s1.marks)
```

---

### Employee Class

```python
class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


emp = Employee("Rahul", 50000)

print(emp.name)
```

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Forgetting `self`

Wrong

```python
def __init__(name):
```

Correct

```python
def __init__(self, name):
```

---

## ❌ Mistake 2

Not using `self`

Wrong

```python
name = name
```

Correct

```python
self.name = name
```

---

## ❌ Mistake 3

Calling constructor directly

Wrong

```python
Bank.__init__()
```

Correct

```python
b = Bank(...)
```

Python calls it automatically.

---

# 💡 Programmer Tips

Remember

```text
Class

↓

Blueprint
```

```text
Object

↓

Real Instance
```

```text
Constructor

↓

Runs Automatically
```

```text
self

↓

Current Object
```

```text
self.variable

↓

Instance Variable
```

---

# 🎓 Interview Questions

### 1. What is OOP?

**Answer:** OOP (Object-Oriented Programming) is a programming paradigm that organizes code using classes and objects, combining data and methods together.

---

### 2. What is a Class?

**Answer:** A class is a blueprint or template used to create objects.

---

### 3. What is an Object?

**Answer:** An object is an instance of a class that occupies memory and contains data.

---

### 4. What is a Constructor?

**Answer:** A constructor (`__init__`) is a special method that is called automatically when an object is created to initialize its data.

---

### 5. What is `self`?

**Answer:** `self` refers to the current object and is used to access instance variables and methods.

---

### 6. What are Instance Variables?

**Answer:** Variables created using `self.variable_name` are called instance variables. Each object has its own copy.

---

# ⭐ MCQs

### Q1. What is a Class?

A. Variable

B. Blueprint

C. Function

D. Module

✅ **Answer:** **B**

---

### Q2. Which method is the constructor?

A. `main()`

B. `start()`

C. `__init__()`

D. `create()`

✅ **Answer:** **C**

---

### Q3. What does `self` represent?

A. Class

B. Current Object

C. Module

D. Function

✅ **Answer:** **B**

---

### Q4. Which statement creates an object?

```python
Bank("Ramesh", 24, "Hyderabad")
```

This creates:

A. Function

B. Variable

C. Object

D. Module

✅ **Answer:** **C**

---

# 📝 Practice Programs

## ⭐ Easy

```python
class Student:

    def __init__(self, name):
        self.name = name

s = Student("Ramesh")

print(s.name)
```

---

## ⭐⭐ Medium

```python
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Fortuner")

print(car.brand)
print(car.model)
```

---

## ⭐⭐⭐ Challenge

Create an **Employee** class with:

* `name`
* `id`
* `salary`

Create two employee objects and print their details.

---

# 📌 Chapter Summary

```text
                PYTHON OOP BASICS
                       │
         ┌─────────────┼─────────────┐
         │             │             │
      Class         Object      Constructor
         │             │             │
   Blueprint     Real Instance   __init__()
         │                           │
      self                    Instance Variables
```

---

# 🏆 Congratulations!

You have completed **Python OOP – Chapter 1: Class, Object, Constructor & Instance Variables**.

### ✅ You learned:

* OOP basics
* Class
* Object
* Constructor (`__init__`)
* `self`
* Instance variables
* Object creation
* Interview questions
* MCQs
* Practice programs

---

# 📖 Next Chapter

## **Chapter 2 – Class Variables, Instance Variables, Getter & Setter Methods**

We'll cover:

* ✅ Class Variables
* ✅ Instance Variables
* ✅ Difference between Class & Instance Variables
* ✅ Getter Methods
* ✅ Setter Methods
* ✅ `Bank.bank_name` vs `self.name`
* ✅ Interview Questions
* ✅ MCQs
* ✅ Practice Programs
---
# 📘 Python OOP Master Handbook

# 📖 Chapter 2 – Class Variables, Instance Variables, Getter & Setter Methods (Beginner to Interview Level)

> ⭐ This chapter explains one of the **most frequently asked OOP interview topics**: **Class Variables, Instance Variables, Getter Methods, and Setter Methods**. These concepts are used in almost every real-world Python project.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand Class Variables
* ✅ Understand Instance Variables
* ✅ Differentiate between Class and Instance Variables
* ✅ Use Getter Methods
* ✅ Use Setter Methods
* ✅ Access variables correctly
* ✅ Answer interview questions confidently

---

# 📖 1. Class Variable

## ✅ Definition

A **Class Variable** belongs to the **class**, not to individual objects.

* Shared by all objects.
* Only one copy exists in memory.
* Declared inside the class but outside methods.

---

## Syntax

```python
class ClassName:

    class_variable = value
```

---

## Example

```python
class Bank:

    bank_name = "SBI"
```

Here,

```text
bank_name

↓

Class Variable
```

---

# 📖 Why Class Variables?

Suppose 10,000 customers belong to **SBI**.

Instead of storing `"SBI"` inside every object,

Python stores it **once** as a Class Variable.

This saves memory.

---

# 📖 Example

```python
class Bank:

    bank_name = "SBI"

    def __init__(self, name):

        self.name = name


b1 = Bank("Rahul")
b2 = Bank("Ajay")

print(b1.bank_name)
print(b2.bank_name)
```

### Output

```text
SBI
SBI
```

---

## Memory Diagram

```text
               Bank Class

        bank_name = SBI

             ▲
             │
      ┌──────┴──────┐
      │             │
     b1            b2

   Rahul         Ajay
```

Only **one copy** of `bank_name`.

---

# 📖 2. Instance Variables

## ✅ Definition

Instance Variables belong to **individual objects**.

Each object has its own copy.

Created using

```python
self.variable_name
```

---

## Example

```python
class Bank:

    def __init__(self, name):

        self.name = name
```

Each object stores a different name.

---

## Example

```python
class Student:

    def __init__(self, name):

        self.name = name


s1 = Student("Ramesh")

s2 = Student("Ajay")

print(s1.name)

print(s2.name)
```

Output

```text
Ramesh

Ajay
```

---

## Memory Diagram

```text
Student

↓

s1

↓

name = Ramesh

----------------

s2

↓

name = Ajay
```

Each object has its own memory.

---

# 📖 Complete Example

```python
class Bank:

    bank_name = "SBI"

    def __init__(self, name, age, branch, amount):

        self.name = name
        self.age = age
        self.branch = branch
        self.amount = amount


b = Bank(
    "Annu",
    25,
    "Hyderabad",
    4000
)

print(b.bank_name)

print(b.name)
```

Output

```text
SBI

Annu
```

---

# 📖 3. Getter Method

## ✅ Definition

A Getter Method returns (reads) object data.

It is mainly used to access instance variables safely.

---

## Syntax

```python
def get_data(self):

    return self.variable
```

---

## Example

```python
class Bank:

    bank_name = "SBI"

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def get_info(self):

        return (
            self.name,
            self.age,
            self.bank_name
        )


b = Bank("Annu",25)

print(b.get_info())
```

Output

```text
('Annu', 25, 'SBI')
```

---

## Dry Run

```text
Object

↓

get_info()

↓

Return

name

age

bank_name
```

---

# 📖 Why Getter?

Advantages

* Read object data
* Hide internal implementation
* Easy maintenance
* Supports encapsulation

---

# 📖 4. Setter Method

## ✅ Definition

Setter Method updates object data.

Instead of directly changing variables,

we use methods.

---

## Syntax

```python
def set_value(self,new_value):

    self.variable = new_value
```

---

## Example

```python
class Bank:

    def __init__(self,name,branch):

        self.name=name

        self.branch=branch

    def set_branch(self,new_branch):

        self.branch=new_branch


b=Bank("Rahul","Hyderabad")

b.set_branch("Vijayawada")

print(b.branch)
```

Output

```text
Vijayawada
```

---

## Dry Run

```text
Before

Branch

↓

Hyderabad

↓

Setter

↓

Vijayawada
```

---

# 📖 Ways to Access Instance Variables

## Method 1

Direct Access

```python
print(b.name)
```

---

## Method 2

Getter Method

```python
print(b.get_info())
```

---

## Can We Do This?

```python
Bank.name
```

❌ No.

Because

`name`

is an Instance Variable.

It belongs to the object.

---

# 📖 Access Class Variable

Using Object

```python
print(b.bank_name)
```

Using Class

```python
print(Bank.bank_name)
```

Both are correct.

---

# 📊 Class Variable vs Instance Variable

| Class Variable               | Instance Variable              |
| ---------------------------- | ------------------------------ |
| Shared by all objects        | Separate copy for every object |
| Declared inside class        | Declared using `self`          |
| Memory efficient             | Uses more memory               |
| Access using Class or Object | Access using Object only       |

---

# 📊 Getter vs Setter

| Getter                     | Setter                     |
| -------------------------- | -------------------------- |
| Reads data                 | Updates data               |
| Returns value              | Changes value              |
| Usually starts with `get_` | Usually starts with `set_` |

---

# 🌍 Real-Life Example

## Employee

```python
class Employee:

    company="Google"

    def __init__(self,name,salary):

        self.name=name

        self.salary=salary

    def get_salary(self):

        return self.salary

    def set_salary(self,new_salary):

        self.salary=new_salary


emp=Employee("Ajay",50000)

print(emp.get_salary())

emp.set_salary(70000)

print(emp.get_salary())
```

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using Class Name for Instance Variable

Wrong

```python
Bank.name
```

Correct

```python
b.name
```

---

## ❌ Mistake 2

Changing Variable Directly

Instead of

```python
b.branch="Delhi"
```

Prefer

```python
b.set_branch("Delhi")
```

---

## ❌ Mistake 3

Using `self` outside the class

Wrong

```python
print(self.name)
```

Correct

```python
print(b.name)
```

---

# 💡 Programmer Tips

Remember

```text
Class Variable

↓

Shared
```

```text
Instance Variable

↓

Individual
```

```text
Getter

↓

Read Data
```

```text
Setter

↓

Update Data
```

```text
self.variable

↓

Instance Variable
```

```text
Class.variable

↓

Class Variable
```

---

# 🎓 Interview Questions

### 1. What is a Class Variable?

**Answer:**
A Class Variable belongs to the class and is shared by all objects.

---

### 2. What is an Instance Variable?

**Answer:**
An Instance Variable belongs to an object. Every object has its own copy.

---

### 3. Difference between Class Variable and Instance Variable?

**Answer:**

* Class Variable → Shared by all objects.
* Instance Variable → Separate copy for each object.

---

### 4. What is a Getter Method?

**Answer:**
A Getter Method returns or reads object data.

---

### 5. What is a Setter Method?

**Answer:**
A Setter Method updates object data.

---

### 6. Can Instance Variables be accessed using the Class Name?

**Answer:**
No. They must be accessed using an object.

---

# ⭐ MCQs

### Q1. Which variable is shared by all objects?

A. Instance Variable

B. Class Variable

C. Local Variable

D. Global Variable

✅ **Answer:** **B**

---

### Q2. Which keyword creates an Instance Variable?

A. `class`

B. `self`

C. `return`

D. `lambda`

✅ **Answer:** **B**

---

### Q3. Which method reads object data?

A. Setter

B. Getter

C. Constructor

D. Destructor

✅ **Answer:** **B**

---

### Q4. Which method updates object data?

A. Getter

B. Constructor

C. Setter

D. Class Method

✅ **Answer:** **C**

---

# 📝 Practice Programs

## ⭐ Easy

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

s = Student("Ramesh")

print(Student.school)
print(s.name)
```

---

## ⭐⭐ Medium

```python
class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary


emp = Employee("Ajay", 50000)

print(emp.get_salary())

emp.set_salary(70000)

print(emp.get_salary())
```

---

## ⭐⭐⭐ Challenge

Create a **Bank** class with:

* Class Variable → `bank_name`
* Instance Variables → `name`, `balance`
* Getter → `get_info()`
* Setter → `set_balance()`

Create two customers, update one balance, and display both details.

---

# 📌 Chapter Summary

```text
                 OOP VARIABLES
                      │
        ┌─────────────┼─────────────┐
        │                           │
 Class Variable             Instance Variable
        │                           │
 Shared by All             One Copy per Object
        │                           │
 Bank.bank_name             self.name
        │
        ├─────────────┐
        │             │
     Getter        Setter
        │             │
   Read Data     Update Data
```

---

# 🏆 Congratulations!

You have completed **Python OOP – Chapter 2: Class Variables, Instance Variables, Getter & Setter Methods**.

### ✅ You learned:

* Class Variables
* Instance Variables
* Difference between Class & Instance Variables
* Getter Methods
* Setter Methods
* Proper variable access
* Interview Questions
* MCQs
* Practice Programs

---

# 📖 Next Chapter

## **Chapter 3 – Pillars of OOP: Encapsulation, Inheritance, Polymorphism & Abstraction**

We'll cover:

* ✅ Encapsulation
* ✅ Inheritance (Single, Multiple, Multilevel, Hierarchical, Hybrid)
* ✅ Polymorphism (Method Overriding)
* ✅ Abstraction
* ✅ `super()` keyword
* ✅ `isinstance()` and `issubclass()`
* ✅ Interview Questions
* ✅ MCQs
* ✅ Real-world examples
---