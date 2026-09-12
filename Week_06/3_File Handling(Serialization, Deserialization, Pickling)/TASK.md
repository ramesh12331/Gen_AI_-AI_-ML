# 📘 CONTINUATION — SERIALIZING MULTIPLE OBJECTS USING `for` LOOP

Now your topic becomes more practical. Earlier, you stored **one `Bank` object**. Here, your code stores **10 customer objects** using both **JSON** and **Pickle**.

---

# 1️⃣ Main Idea 🧠

Previously:

```text
1 Customer
    ↓
Bank Object
    ↓
Store in File
```

Now:

```text
Customer 1 → Bank Object
Customer 2 → Bank Object
Customer 3 → Bank Object
...
Customer 10 → Bank Object
        ↓
      List
        ↓
   Store in File
```

So the new concepts are:

```text
🔁 for loop
🏦 Multiple Bank objects
📋 List of customers
📦 Serialization
🗂️ JSON
🥒 Pickle
📖 Reading objects back
```

---

# 2️⃣ Why Do We Need a Loop? 🔁

Without a loop, we would need to write:

```python
name1 = input("Enter Name: ")
name2 = input("Enter Name: ")
name3 = input("Enter Name: ")
```

and repeat the same code 10 times.

That's unnecessary.

Instead:

```python
for i in range(10):
```

runs the same block:

```text
10 times
```

### 🧠 Shortcut

> 🔁 **Loop = Repeat**

---

# 3️⃣ JSON — Store 10 Customers 🗂️

Here is your code with the pasted formatting cleaned up:

```python
import json


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name}, {self.age}, {self.balance}"


customers = []


for i in range(10):

    print(f"\nEnter Customer {i+1} Details")

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    balance = float(input("Enter Balance : "))

    obj = Bank(name, age, balance)

    customers.append(obj.__dict__)


with open("customers.json", "w") as f:
    json.dump(customers, f, indent=4)


print("\n10 Customer Records Stored Successfully.")
```

---

# 4️⃣ Step 1 — Create Empty List 📋

```python
customers = []
```

Initially:

```text
customers
    ↓
   [ ]
```

Why?

Because we need somewhere to collect the 10 customer records.

After customers are added:

```text
customers
    ↓
[
 Customer 1,
 Customer 2,
 Customer 3,
 ...
 Customer 10
]
```

---

# 5️⃣ Step 2 — Loop 10 Times 🔁

```python
for i in range(10):
```

`range(10)` produces values:

```text
0
1
2
3
4
5
6
7
8
9
```

Total:

```text
10 iterations
```

---

# 6️⃣ Why `i + 1`? 🤔

Your code:

```python
print(f"\nEnter Customer {i+1} Details")
```

On the first iteration:

```text
i = 0
i + 1 = 1

Customer 1
```

Second:

```text
i = 1
i + 1 = 2

Customer 2
```

Last:

```text
i = 9
i + 1 = 10

Customer 10
```

So the user sees:

```text
Customer 1
Customer 2
...
Customer 10
```

instead of:

```text
Customer 0
Customer 1
...
Customer 9
```

---

# 7️⃣ Step 3 — Take Customer Input ⌨️

```python
name = input("Enter Name : ")
age = int(input("Enter Age : "))
balance = float(input("Enter Balance : "))
```

Suppose the user enters:

```text
Name    : Ramesh
Age     : 30
Balance : 50000
```

Then:

```text
name
 ↓
"Ramesh"

age
 ↓
30

balance
 ↓
50000.0
```

---

# 8️⃣ Step 4 — Create Object 🏦

Your code:

```python
obj = Bank(name, age, balance)
```

Suppose:

```text
name    = Ramesh
age     = 30
balance = 50000
```

Python effectively calls:

```python
Bank("Ramesh", 30, 50000)
```

Constructor:

```python
def __init__(self, name, age, balance):
    self.name = name
    self.age = age
    self.balance = balance
```

Memory concept:

```text
              obj
               │
               ▼
       ┌─────────────────┐
       │   Bank Object   │
       ├─────────────────┤
       │ name            │
       │ "Ramesh"        │
       ├─────────────────┤
       │ age             │
       │ 30              │
       ├─────────────────┤
       │ balance         │
       │ 50000.0         │
       └─────────────────┘
```

---

# 9️⃣ Step 5 — `obj.__dict__` ⭐

This is the most important JSON line:

```python
customers.append(obj.__dict__)
```

Remember:

```python
obj
```

is a:

```text
Bank Object 🏦
```

But:

```python
obj.__dict__
```

represents its instance attributes as a dictionary:

```python
{
    "name": "Ramesh",
    "age": 30,
    "balance": 50000.0
}
```

Therefore:

```text
Bank Object
     ↓
obj.__dict__
     ↓
Dictionary
```

Then:

```python
customers.append(...)
```

adds that dictionary to the list.

---

# 🔟 After First Customer 📋

Initially:

```python
customers = []
```

After customer 1:

```python
customers = [
    {
        "name": "Ramesh",
        "age": 30,
        "balance": 50000.0
    }
]
```

---

# 1️⃣1️⃣ After Second Customer 📋

Suppose the second customer is:

```text
Rahul
25
40000
```

Now conceptually:

```python
customers = [
    {
        "name": "Ramesh",
        "age": 30,
        "balance": 50000.0
    },
    {
        "name": "Rahul",
        "age": 25,
        "balance": 40000.0
    }
]
```

The same process continues until 10 records are collected.

---

# 1️⃣2️⃣ Memory Diagram 🧠

```text
customers
    │
    ▼
┌────────────────────────────┐
│ List                       │
├────────────────────────────┤
│ 0 → Customer 1 Dictionary  │
│ 1 → Customer 2 Dictionary  │
│ 2 → Customer 3 Dictionary  │
│ 3 → Customer 4 Dictionary  │
│ ...                        │
│ 9 → Customer 10 Dictionary │
└────────────────────────────┘
```

---

# 1️⃣3️⃣ Step 6 — Store List in JSON 📦

After the loop:

```python
with open("customers.json", "w") as f:
    json.dump(customers, f, indent=4)
```

Flow:

```text
customers
    ↓
List of 10 Dictionaries
    ↓
json.dump()
    ↓
Serialization 📦
    ↓
customers.json
```

`indent=4` makes the JSON formatted and easier to read.

---

# 1️⃣4️⃣ Complete JSON Flow Diagram 🗂️

```text
           for loop 🔁
               │
               ▼
         Take User Input
               │
               ▼
      Create Bank Object 🏦
               │
               ▼
          obj.__dict__
               │
               ▼
          Dictionary 📖
               │
               ▼
      customers.append()
               │
               ▼
        customers List 📋
               │
       Repeat 10 Times
               │
               ▼
         json.dump()
               │
               ▼
       customers.json 📄
```

---

# 1️⃣5️⃣ Now Pickle — Store Actual Objects 🥒

Your second program changes one important line.

JSON version:

```python
customers.append(obj.__dict__)
```

Pickle version:

```python
customers.append(
    Bank(name, age, balance)
)
```

According to your supplied code, the list now contains the `Bank` objects themselves.

---

# 1️⃣6️⃣ Pickle Program 🥒

Clean version of your supplied code:

```python
import pickle


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name}, {self.age}, {self.balance}"


customers = []


for i in range(10):

    print(f"\nEnter Customer {i+1} Details")

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    balance = float(input("Enter Balance : "))

    customers.append(
        Bank(name, age, balance)
    )


with open("customers.pkl", "wb") as f:
    pickle.dump(customers, f)


print("\n10 Objects Stored Successfully.")
```

---

# 1️⃣7️⃣ Important Line ⭐

```python
customers.append(
    Bank(name, age, balance)
)
```

Let's split it.

First:

```python
Bank(name, age, balance)
```

creates:

```text
Bank Object 🏦
```

Then:

```python
customers.append(...)
```

puts that object into the list.

So:

```text
Bank(...)
   ↓
Object
   ↓
append()
   ↓
customers
```

---

# 1️⃣8️⃣ JSON List vs Pickle List ⚖️

This difference is very important in **your two programs**.

### JSON program

```text
customers
    ↓
[
 Dictionary,
 Dictionary,
 Dictionary,
 ...
]
```

because your code uses:

```python
customers.append(obj.__dict__)
```

### Pickle program

```text
customers
    ↓
[
 Bank Object,
 Bank Object,
 Bank Object,
 ...
]
```

because your code uses:

```python
customers.append(
    Bank(name, age, balance)
)
```

---

# 1️⃣9️⃣ Pickling the Complete List 📦

After 10 objects:

```python
with open("customers.pkl", "wb") as f:
    pickle.dump(customers, f)
```

Concept:

```text
customers
     │
     ▼
List of Bank Objects
     │
     ▼
pickle.dump()
     │
     ▼
Pickling 📦
     │
     ▼
customers.pkl 💾
```

Remember:

```text
wb
│
├── w → Write
└── b → Binary
```

---

# 2️⃣0️⃣ Reading the Objects Back 📖

Your third program:

```python
with open("customers.pkl", "rb") as f:
    data = pickle.load(f)
```

This performs unpickling.

```text
customers.pkl
      ↓
pickle.load()
      ↓
Unpickling 🔄
      ↓
List of Bank Objects
      ↓
data
```

---

# 2️⃣1️⃣ What is Inside `data`? 📋

Based on your program:

```text
data
 │
 ▼
List
 │
 ├── Bank Object 1
 ├── Bank Object 2
 ├── Bank Object 3
 ├── ...
 └── Bank Object 10
```

That's why your next code can loop through them.

---

# 2️⃣2️⃣ Loop Through Loaded Objects 🔁

Your code:

```python
for customer in data:
    print(customer.get_info())
```

Let's understand carefully.

Suppose:

```text
data
 ↓
[obj1, obj2, obj3, ...]
```

The loop runs:

```text
Iteration 1
customer → obj1

Iteration 2
customer → obj2

Iteration 3
customer → obj3

...

Iteration 10
customer → obj10
```

---

# 2️⃣3️⃣ Calling `get_info()` 🎯

Each `customer` is used as a `Bank` object in your code.

Therefore:

```python
customer.get_info()
```

calls:

```python
def get_info(self):
    return f"{self.name}, {self.age}, {self.balance}"
```

For example:

```text
self.name
↓
Ramesh

self.age
↓
30

self.balance
↓
50000
```

Returns something like:

```text
Ramesh, 30, 50000
```

---

# 2️⃣4️⃣ Complete Pickle Flow Diagram 🏆

```text
                INPUT
                  │
                  ▼
        name, age, balance
                  │
                  ▼
            Bank(...)
                  │
                  ▼
           Bank Object 🏦
                  │
                  ▼
       customers.append()
                  │
                  ▼
        List of Objects 📋
                  │
          Repeat 10 times
                  │
                  ▼
          pickle.dump()
                  │
                  ▼
         customers.pkl 💾
                  │
                  ▼
           pickle.load()
                  │
                  ▼
        List of Objects 📋
                  │
                  ▼
      for customer in data
                  │
                  ▼
      customer.get_info()
                  │
                  ▼
             OUTPUT 🖥️
```

---

# 2️⃣5️⃣ Dry Run with 3 Customers 🔍

Instead of 10, imagine:

```python
for i in range(3):
```

### 🔁 Iteration 1

Input:

```text
Ramesh
30
50000
```

Create:

```text
Bank("Ramesh", 30, 50000)
```

List:

```text
customers
↓
[obj1]
```

### 🔁 Iteration 2

Input:

```text
Rahul
25
40000
```

List:

```text
customers
↓
[obj1, obj2]
```

### 🔁 Iteration 3

Input:

```text
Anwar
35
70000
```

List:

```text
customers
↓
[obj1, obj2, obj3]
```

Then:

```python
pickle.dump(customers, f)
```

stores the list.

Later:

```python
data = pickle.load(f)
```

gets it back.

Then:

```python
for customer in data:
    print(customer.get_info())
```

conceptually displays each customer's information.

---

# 2️⃣6️⃣ OOP Connection 🏦

This program combines several concepts you have already studied:

```text
                  PROGRAM
                     │
      ┌──────────────┼───────────────┐
      ▼              ▼               ▼
     OOP          File Handling    Loop
      │              │               │
      ▼              ▼               ▼
   Class           open()           for
   Object          wb/rb          range()
   Method
   __init__
```

And serialization connects them:

```text
OOP Object
    ↓
Serialization
    ↓
File
```

This is why this example is useful: it combines **classes + objects + lists + loops + files + serialization**.

---

# 2️⃣7️⃣ JSON vs Pickle in Your 10-Customer Programs ⚖️

| JSON Program 🗂️                                 | Pickle Program 🥒                              |
| ------------------------------------------------ | ---------------------------------------------- |
| Creates `Bank` object                            | Creates `Bank` object                          |
| Uses `obj.__dict__`                              | Keeps the `Bank` object                        |
| List contains dictionaries                       | List contains objects                          |
| `json.dump()`                                    | `pickle.dump()`                                |
| `"w"`                                            | `"wb"`                                         |
| `customers.json`                                 | `customers.pkl`                                |
| `indent=4` shown                                 | No `indent` shown                              |
| Loaded JSON data would be Python data structures | Your code loads objects and calls `get_info()` |

---

# 2️⃣8️⃣ Common Mistakes ❌

### ❌ Mistake 1 — List inside loop

Wrong:

```python
for i in range(10):
    customers = []
```

That recreates the list every iteration.

Your program correctly creates it **before** the loop:

```python
customers = []

for i in range(10):
```

🧠 Remember:

> **Create collection outside → add data inside.**

---

### ❌ Mistake 2 — Forgetting conversion in your JSON pattern

Your JSON program uses:

```python
customers.append(obj.__dict__)
```

not simply the raw object.

---

### ❌ Mistake 3 — Forgetting binary modes with Pickle

Remember your pattern:

```text
pickle.dump()
      +
     "wb"

pickle.load()
      +
     "rb"
```

---

### ❌ Mistake 4 — Wrong indentation

Correct:

```python
for customer in data:
    print(customer.get_info())
```

The `print()` belongs inside the loop.

---

# 2️⃣9️⃣ Interview Questions & Answers 🎤

### Q1. Why is `customers = []` created before the loop?

**Answer:** To create one list that collects all 10 customer records/objects.

### Q2. What does `range(10)` do here?

**Answer:** It makes the loop execute 10 times.

### Q3. Why use `i + 1`?

**Answer:** Because `range(10)` starts at `0`, but we want to display Customer 1 through Customer 10.

### Q4. What does this do?

```python
obj = Bank(name, age, balance)
```

**Answer:** It creates a `Bank` object using the entered customer information.

### Q5. What does this do in your JSON program?

```python
customers.append(obj.__dict__)
```

**Answer:** It adds the object's instance-attribute dictionary to `customers`.

### Q6. What does this do in your Pickle program?

```python
customers.append(Bank(name, age, balance))
```

**Answer:** It creates a `Bank` object and appends that object to the list.

### Q7. What does `pickle.dump(customers, f)` do?

**Answer:** In your program, it serializes the list of customer objects to `customers.pkl`.

### Q8. What does `pickle.load(f)` do?

**Answer:** It reads/deserializes the stored pickle data back into `data`.

### Q9. Why can your code call:

```python
customer.get_info()
```

after loading the Pickle data?

**Answer:** Because the supplied program treats each loaded `customer` as a `Bank` object with the `get_info()` method.

---

# 🏆 FINAL SHORTCUT SUMMARY

```text
👤 INPUT
name + age + balance
        ↓
🏦 Bank(...)
        ↓
Bank Object
        ↓
🔁 Repeat 10 times
```

### 🗂️ JSON

```text
Bank Object
    ↓
__dict__
    ↓
Dictionary
    ↓
append()
    ↓
List of Dictionaries
    ↓
json.dump()
    ↓
customers.json
```

### 🥒 PICKLE

```text
Bank Object
    ↓
append()
    ↓
List of Objects
    ↓
pickle.dump()
    ↓
customers.pkl
```

### 🔄 UNPICKLE

```text
customers.pkl
      ↓
pickle.load()
      ↓
data
      ↓
List of Objects
      ↓
for loop
      ↓
customer.get_info()
```

## 🧠 Golden Formula

> 🗂️ **Your JSON program:** `Object → __dict__ → List → json.dump()`
> 🥒 **Your Pickle program:** `Object → List → pickle.dump()`
> 🔄 **Read Pickle:** `pickle.load() → List of Objects → get_info()`

This is the key idea behind your **10-object serialization program**.
