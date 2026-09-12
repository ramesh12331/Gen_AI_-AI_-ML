# 🏆 FINAL SUMMARY — PYTHON SERIALIZATION & DESERIALIZATION

This summary covers the material you provided: **JSON, custom class objects, Pickling/Unpickling, and storing multiple `Bank` objects using loops**.

---

## 🧠 1. Main Concept

### 📦 Serialization

**Definition:** Converting Python data into a format that can be stored in a file.

In your chapter, you used:

```text
Serialization
     │
     ├── 🗂️ JSON
     │
     └── 🥒 Pickle
```

### 🔄 Deserialization

**Definition:** Reading stored data and converting it back into Python data/object form.

### ⚡ Shortcut

```text
Serialization
Python ➡️ File 📦

Deserialization
File ➡️ Python 🔄
```

---

# 🗂️ 2. JSON Serialization

Import:

```python
import json
```

### Save

```python
with open("new.json", "w") as f:
    json.dump(data, f)
```

### Load

```python
with open("new.json", "r") as f:
    data = json.load(f)
```

### 🧠 Shortcut

```text
json.dump() → SAVE 📦
json.load() → LOAD 📤
```

---

# 📋 3. JSON with List

```python
import json

numbers = [1, 2, 3, 4, 5]

with open("new.json", "w") as f:
    json.dump(numbers, f)
```

Read:

```python
with open("new.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))
```

### Flow

```text
Python List
    ↓
json.dump()
    ↓
JSON File
    ↓
json.load()
    ↓
Python List
```

---

# 📖 4. JSON with Dictionary

```python
data = {
    "name": "abc",
    "age": 40
}

with open("new.json", "w") as f:
    json.dump(data, f, indent=4)
```

### 🎨 `indent=4`

Used in your examples to make JSON easier to read.

```text
indent=4
   ↓
Formatted JSON 👀
```

---

# ❌ 5. Why Normal `write()` Fails

Your example:

```python
d = {
    "name": "abc",
    "age": 40
}

with open("new.txt", "w") as f:
    f.write(d)
```

gives:

```text
TypeError:
write() argument must be str, not dict
```

So your chapter uses:

```python
json.dump(d, f)
```

for this dictionary serialization pattern.

---

# 🏦 6. JSON with Custom Class Object

Example:

```python
class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


a = Bank("Ramesh", 30, 50000)
```

Your material shows that directly doing:

```python
json.dump(a, f)
```

gives:

```text
TypeError:
Object of type Bank is not JSON serializable
```

---

# 🔧 7. Solution — `default=get_info`

Convert the object into a dictionary:

```python
def get_info(obj):

    return {
        "name": obj.name,
        "age": obj.age,
        "balance": obj.balance
    }
```

Then:

```python
with open("new.json", "w") as f:
    json.dump(
        a,
        f,
        default=get_info,
        indent=4
    )
```

### Flow

```text
Bank Object 🏦
     ↓
get_info()
     ↓
Dictionary 📖
     ↓
json.dump()
     ↓
JSON 📄
```

---

# ⚡ 8. `__dict__` Shortcut

Your other approach is:

```python
a.__dict__
```

For the `Bank` object, this gives its instance attributes in dictionary form.

Conceptually:

```python
{
    "name": "Ramesh",
    "age": 30,
    "balance": 50000
}
```

Therefore:

```python
with open("new.json", "w") as f:
    json.dump(a.__dict__, f, indent=4)
```

### 🧠 Remember

```text
Object
  ↓
__dict__
  ↓
Dictionary
  ↓
JSON
```

---

# 🥒 9. Pickling

Your chapter next uses:

```python
import pickle
```

**Pickling** is the serialization process using `pickle` in your notes.

### Syntax

```python
with open("new.pkl", "wb") as f:
    pickle.dump(a, f)
```

### Flow

```text
Python Object 🏦
      ↓
pickle.dump()
      ↓
Pickling 📦
      ↓
new.pkl 💾
```

---

# 🔄 10. Unpickling

Your chapter reads the object back with:

```python
with open("new.pkl", "rb") as f:
    data = pickle.load(f)
```

### Flow

```text
new.pkl 💾
    ↓
pickle.load()
    ↓
Unpickling 🔄
    ↓
Python Object 🏦
```

### ⚡ Shortcut

```text
pickle.dump() → PICKLE / SAVE 📦

pickle.load() → UNPICKLE / LOAD 🔄
```

---

# 💾 11. `wb` and `rb`

Your Pickle examples use:

```text
wb
│
├── w = Write
└── b = Binary
```

```text
rb
│
├── r = Read
└── b = Binary
```

### 🧠 Golden Pair

```text
pickle.dump() + wb

pickle.load() + rb
```

---

# 🔟 12. Storing 10 Customer Objects

Your program creates:

```python
customers = []
```

Then:

```python
for i in range(10):
```

The loop executes 10 times.

```text
i = 0
i = 1
i = 2
...
i = 9
```

You display:

```python
print(f"Customer {i+1}")
```

so the user sees:

```text
Customer 1
Customer 2
...
Customer 10
```

---

# 👤 13. Taking Customer Information

Inside the loop:

```python
name = input("Enter Name : ")
age = int(input("Enter Age : "))
balance = float(input("Enter Balance : "))
```

Then:

```python
obj = Bank(name, age, balance)
```

creates the object.

```text
Input
 │
 ├── Name
 ├── Age
 └── Balance
       ↓
    Bank(...)
       ↓
  Bank Object 🏦
```

---

# 🗂️ 14. 10 Objects with JSON

Your JSON pattern:

```python
customers = []

for i in range(10):

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    balance = float(input("Enter Balance : "))

    obj = Bank(name, age, balance)

    customers.append(obj.__dict__)
```

Then:

```python
with open("customers.json", "w") as f:
    json.dump(customers, f, indent=4)
```

### Flow

```text
Customer Input
      ↓
Bank Object
      ↓
obj.__dict__
      ↓
Dictionary
      ↓
customers.append()
      ↓
List of Dictionaries
      ↓
json.dump()
      ↓
customers.json
```

---

# 🥒 15. 10 Objects with Pickle

Your Pickle pattern keeps the objects:

```python
customers = []

for i in range(10):

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    balance = float(input("Enter Balance : "))

    customers.append(
        Bank(name, age, balance)
    )
```

Then:

```python
with open("customers.pkl", "wb") as f:
    pickle.dump(customers, f)
```

### Flow

```text
Customer Input
      ↓
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

---

# 📖 16. Reading 10 Pickled Objects

Your program:

```python
with open("customers.pkl", "rb") as f:
    data = pickle.load(f)
```

Now loop:

```python
for customer in data:
    print(customer.get_info())
```

### Flow

```text
customers.pkl
      ↓
pickle.load()
      ↓
data
      ↓
List of Bank Objects
      ↓
for loop 🔁
      ↓
customer
      ↓
get_info()
      ↓
Customer Details 🖥️
```

---

# ⚖️ 17. JSON vs Pickle — Quick Table

| 🗂️ JSON                                    | 🥒 Pickle                              |
| ------------------------------------------- | -------------------------------------- |
| `import json`                               | `import pickle`                        |
| `json.dump()`                               | `pickle.dump()`                        |
| `json.load()`                               | `pickle.load()`                        |
| `w`                                         | `wb`                                   |
| `r`                                         | `rb`                                   |
| `.json` shown                               | `.pkl` shown                           |
| Your custom object is converted first       | Your example directly stores objects   |
| `obj.__dict__` shown                        | Actual `Bank` objects shown            |
| List of dictionaries in 10-customer example | List of objects in 10-customer example |

---

# 🎤 18. Top Interview Questions

**Q1. What is Serialization?**
Converting Python data into a storable representation.

**Q2. What is Deserialization?**
Converting stored data back into Python data/object form.

**Q3. JSON serialization method?**

```python
json.dump()
```

**Q4. JSON deserialization method?**

```python
json.load()
```

**Q5. Pickling method?**

```python
pickle.dump()
```

**Q6. Unpickling method?**

```python
pickle.load()
```

**Q7. Why use `__dict__` in your JSON example?**
To get the object's instance attributes as a dictionary before JSON serialization.

**Q8. What does `indent=4` do?**
Makes JSON more readable.

**Q9. Why `wb` with Pickle?**
Your Pickle writing example uses binary write mode.

**Q10. Why `rb`?**
Your Pickle reading example uses binary read mode.

---

# 🚀 MASTER SHORTCUT SHEET

```text
📦 SERIALIZATION
Python → Storage

🔄 DESERIALIZATION
Storage → Python


🗂️ JSON
────────────
json.dump()
Python → JSON File

json.load()
JSON File → Python

indent=4
Readable JSON

__dict__
Object → Dictionary


🥒 PICKLE
────────────
pickle.dump()
Object → .pkl

pickle.load()
.pkl → Object

wb
Write Binary

rb
Read Binary


🔟 MULTIPLE OBJECTS
────────────────────
customers = []
      ↓
for i in range(10)
      ↓
Take Input
      ↓
Create Bank Object
      ↓
Append
      ↓
Store
```

# 🏆 ONE-MINUTE FINAL REVISION

```text
                  📦 SERIALIZATION
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
           🗂️ JSON               🥒 PICKLE
              │                     │
         json.dump()           pickle.dump()
              │                     │
              ▼                     ▼
          JSON File              .pkl File
              │                     │
         json.load()           pickle.load()
              │                     │
              ▼                     ▼
        Python Data          Python Object(s)


🏦 CUSTOM OBJECT + JSON
Object → __dict__ → Dictionary → json.dump()


🏦 CUSTOM OBJECT + PICKLE
Object → pickle.dump()


🔟 MULTIPLE CUSTOMERS
Input → Bank Object → List → Serialization → File
```

## 🧠 5 Golden Shortcuts

> 📦 **Serialization = SAVE direction**
> 🔄 **Deserialization = LOAD direction**
> 🗂️ **JSON = `dump()` / `load()`**
> 🥒 **Pickle = `dump()` + `wb` / `load()` + `rb`**
> 🔟 **Multiple objects = Loop → Object → List → Serialize**

### ⭐ Most Important Program Flow

```text
INPUT
  ↓
CLASS
  ↓
OBJECT
  ↓
LIST
  ↓
SERIALIZATION
  ↓
FILE
  ↓
DESERIALIZATION
  ↓
PYTHON DATA / OBJECT
```

That is the complete shortcut for revising your **Serialization & Deserialization chapter**.
