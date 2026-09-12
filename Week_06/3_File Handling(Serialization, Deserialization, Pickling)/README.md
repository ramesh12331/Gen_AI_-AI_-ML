# 📘 CHAPTER — JSON SERIALIZATION & DESERIALIZATION

We’ll start from your supplied code and go slowly. This first part covers **why serialization is needed, `json.dump()`, `json.load()`, lists, dictionaries, and `indent=4`**. After that, the same material moves into **custom class objects and Pickle**.

---

# 1️⃣ The Main Problem — Why Serialization? 🤔

Suppose we have a Python dictionary:

```python
d = {
    "name": "abc",
    "age": 40
}
```

Now suppose we try:

```python
with open("new.txt", "w") as f:
    f.write(d)
```

❌ This gives:

```text
TypeError: write() argument must be str, not dict
```

## 🧠 Why?

Because:

```python
d
```

contains a:

```text
Dictionary 📖
```

But normal text-file `write()` expects:

```text
String 🔤
```

So the problem is:

```text
Python Dictionary
       ↓
{"name": "abc", "age": 40}
       ↓
    f.write()
       ↓
       ❌
    TypeError
```

This is where **serialization** becomes useful.

---

# 2️⃣ What is Serialization? 📦

## ✅ Definition

From your notes:

> **Serialization is the process of converting Python data types into JSON format.**

### Simple English

We have some Python data:

```python
[1, 2, 3, 4]
```

or:

```python
{
    "name": "Ramesh",
    "age": 30
}
```

We want to convert that Python data into JSON so it can be stored.

```text
🐍 PYTHON DATA
      │
      │ Serialization 📦
      ▼
   JSON DATA
```

### 🧠 Shortcut

> 📦 **Serialization = Python → JSON**

---

# 3️⃣ What is Deserialization? 🔄

## ✅ Definition

From your supplied material:

> **Deserialization is the process of converting JSON format back into Python data types.**

So it is the opposite direction.

```text
JSON DATA
    │
    │ Deserialization 🔄
    ▼
PYTHON DATA 🐍
```

### 🧠 Shortcut

> 🔄 **Deserialization = JSON → Python**

---

# 4️⃣ Serialization vs Deserialization ⚖️

| 📦 Serialization                   | 🔄 Deserialization                 |
| ---------------------------------- | ---------------------------------- |
| Python → JSON                      | JSON → Python                      |
| Converts Python data               | Converts JSON data                 |
| Saving direction                   | Loading direction                  |
| `json.dump()` in your file example | `json.load()` in your file example |

### ⭐ Best Memory Trick

```text
SERIALIZATION 📦
Python ➡️ JSON


DESERIALIZATION 🔄
JSON ➡️ Python
```

Or simply:

> 📦 **Serialization = PACK**
> 📤 **Deserialization = UNPACK**

---

# 5️⃣ JSON Module 📦

Your code starts with:

```python
import json
```

## Why?

Python provides the `json` module for working with JSON data.

In your examples, the two most important functions are:

```python
json.dump()
json.load()
```

### 🧠 Shortcut

```text
dump() → Python → File 📦

load() → File → Python 📤
```

---

# 6️⃣ `json.dump()` 📦

## ✅ Definition

In your example, `json.dump()` takes Python data, converts it to JSON, and writes it to the opened file.

### Syntax

```python
json.dump(data, file_object)
```

Example:

```python
json.dump(l, f)
```

Here:

```text
l → Python data
f → File object
```

---

# 7️⃣ Simple List Serialization 📋

Your example starts with a list:

```python
import json

l = [1, 2, 3, 4, 5, "Anwar"]

with open("new.txt", "w") as f:
    json.dump(l, f)
```

## 🔍 Line-by-Line Explanation

### Line 1

```python
import json
```

Load the JSON module.

---

### Line 2

```python
l = [1, 2, 3, 4, 5, "Anwar"]
```

Create a Python list.

Memory concept:

```text
l
│
▼
┌──────────────────────────┐
│ [1,2,3,4,5,"Anwar"]      │
│                          │
│ Python List 📋           │
└──────────────────────────┘
```

---

### Line 3

```python
with open("new.txt", "w") as f:
```

Open:

```text
new.txt
```

in:

```text
w → Write mode ✍️
```

`f` represents the opened file.

---

### Line 4

```python
json.dump(l, f)
```

Now Python takes:

```text
l
↓
Python List
```

and serializes it to the file.

### Flow

```text
l
│
▼
[1,2,3,4,5,"Anwar"]
│
│ json.dump()
▼
JSON representation
│
▼
📄 new.txt
```

---

# 8️⃣ Dry Run of `json.dump()` 🔍

Code:

```python
l = [1, 2, 3, 4, 5, "Anwar"]

with open("new.txt", "w") as f:
    json.dump(l, f)
```

### Step 1

Python creates:

```text
l → [1,2,3,4,5,"Anwar"]
```

### Step 2

Python opens:

```text
new.txt
```

### Step 3

`f` refers to that opened file.

### Step 4

Python executes:

```python
json.dump(l, f)
```

Think:

```text
          json.dump(l, f)
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
        l                 f
   Python List        File Object
        │                 │
        └────────┬────────┘
                 ▼
             Serialize
                 ▼
            Write to File
```

---

# 9️⃣ `json.load()` 📤

Now we want the data back.

Your code:

```python
with open("new.txt", "r") as f:
    d = json.load(f)

print(d)
print(type(d))
```

## ✅ Definition

In this example, `json.load()` reads JSON data from the file and converts it back into Python data.

### Syntax

```python
variable = json.load(file_object)
```

Example:

```python
d = json.load(f)
```

---

# 🔟 Deserializing the List 🔄

```python
with open("new.txt", "r") as f:
    d = json.load(f)

print(d)
print(type(d))
```

Concept:

```text
📄 new.txt
     │
     ▼
 json.load(f)
     │
     ▼
Deserialization 🔄
     │
     ▼
Python List 📋
     │
     ▼
     d
```

The value is again available as Python data.

---

# 1️⃣1️⃣ Why `type(d)`? 🔍

Your code contains:

```python
print(type(d))
```

This is useful because we want to check:

> "After deserialization, what Python data type did I get?"

For this list example, `d` becomes a Python list.

So conceptually:

```text
JSON data
    ↓
json.load()
    ↓
Python List
```

---

# 1️⃣2️⃣ Complete List Flow 🔄

This is one of the most important diagrams in the chapter:

```text
          SERIALIZATION 📦

Python List
    │
    ▼
[1,2,3,4,5,"Anwar"]
    │
    ▼
json.dump(l, f)
    │
    ▼
📄 new.txt


        DESERIALIZATION 🔄

📄 new.txt
    │
    ▼
json.load(f)
    │
    ▼
Python List
    │
    ▼
    d
```

### 🧠 Master Shortcut

```text
dump ↓
Python → File

load ↑
File → Python
```

---

# 1️⃣3️⃣ Dictionary Serialization 📖

Your next example uses:

```python
d = {
    "name": "abc",
    "age": 40
}
```

This is a Python dictionary.

```text
d
│
▼
{
 "name": "abc",
 "age": 40
}
│
▼
Dictionary 📖
```

Now serialize it:

```python
with open("new.json", "w") as f:
    json.dump(d, f)
```

---

# 1️⃣4️⃣ Dictionary Flow Diagram 📖➡️📄

```text
Python Dictionary
       │
       ▼
{
 "name": "abc",
 "age": 40
}
       │
       ▼
 json.dump(d, f)
       │
       ▼
 Serialization 📦
       │
       ▼
   📄 new.json
```

---

# 1️⃣5️⃣ Does JSON Require `.json` Extension? 🤔

Your supplied code demonstrates both:

```python
with open("new.json", "w") as f:
    json.dump(d, f)
```

and:

```python
with open("new.txt", "w") as f:
    json.dump(d, f)
```

So in your examples, the JSON representation is written to both a `.json` file and a `.txt` file.

### 🧠 Important Concept

```text
.json
↓
Common JSON filename extension


.txt
↓
Can still contain JSON-formatted text
```

So your comment says:

> **Same JSON format but file extension is `.txt`.**

---

# 1️⃣6️⃣ Nested Dictionary 🏗️

Your material next uses:

```python
d = {
    101: {
        "name": "abc",
        "age": 40
    },

    102: {
        "name": "rahul",
        "age": 50
    }
}
```

Think of the structure:

```text
d
│
├── 101
│    │
│    ├── name → abc
│    └── age  → 40
│
└── 102
     │
     ├── name → rahul
     └── age  → 50
```

This is a dictionary containing dictionaries.

---

# 1️⃣7️⃣ What is `indent=4`? 🎨

Your example:

```python
with open("new.json", "w") as f:
    json.dump(d, f, indent=4)
```

The important new part is:

```python
indent=4
```

## ✅ Purpose

It formats the JSON with indentation so that the stored JSON is easier for humans to read.

### Without formatting

The data can appear compact.

### With:

```python
indent=4
```

it is displayed in a more structured way.

Concept:

```text
JSON Data
   │
   ▼
indent=4
   │
   ▼
Better formatted /
easier to read 👀
```

### 🧠 Shortcut

> `indent=4` → **Pretty / readable JSON**

---

# 1️⃣8️⃣ Full Dictionary Example 💻

```python
import json

d = {
    101: {
        "name": "abc",
        "age": 40
    },
    102: {
        "name": "rahul",
        "age": 50
    }
}

with open("new.json", "w") as f:
    json.dump(d, f, indent=4)
```

### Execution Flow

```text
d
↓
Python Dictionary
↓
json.dump()
↓
Serialization
↓
indent=4
↓
Formatted JSON
↓
new.json
```

---

# 1️⃣9️⃣ `dump()` vs `load()` ⚖️

This table is very important for interviews.

| `json.dump()` 📦         | `json.load()` 📤          |
| ------------------------ | ------------------------- |
| Serialization direction  | Deserialization direction |
| Python → JSON file       | JSON file → Python        |
| Used while writing       | Used while reading        |
| Takes data + file object | Takes file object         |
| `json.dump(d, f)`        | `json.load(f)`            |

### 🧠 Easy Trick

```text
DUMP
↓
Put data into file 📥


LOAD
↑
Bring data from file 📤
```

---

# 2️⃣0️⃣ Serialization vs Normal `write()` ⚖️

Your first example explains why this topic matters.

### ❌ Normal `write()`

```python
d = {
    "name": "abc",
    "age": 40
}

with open("new.txt", "w") as f:
    f.write(d)
```

Problem:

```text
Dictionary
    ↓
write()
    ↓
❌ TypeError
```

### ✅ Your JSON approach

```python
with open("new.json", "w") as f:
    json.dump(d, f)
```

Flow:

```text
Dictionary
    ↓
json.dump()
    ↓
Serialization
    ↓
JSON representation
    ↓
File ✅
```

---

# 2️⃣1️⃣ Real-Life Example 🏦

Imagine a bank program:

```python
customer = {
    "name": "Ramesh",
    "age": 30,
    "balance": 50000
}
```

During the Python program:

```text
customer
   ↓
Python Dictionary
   ↓
RAM 🧠
```

If we want to preserve the data in JSON form, conceptually:

```text
Python Dictionary
       ↓
Serialization 📦
       ↓
JSON
       ↓
File 💾
```

Later:

```text
File 💾
   ↓
JSON
   ↓
Deserialization 🔄
   ↓
Python Dictionary
   ↓
Program 🐍
```

---

# 2️⃣2️⃣ Common Mistakes ❌

### ❌ Mistake 1 — Using `write()` directly with dictionary

```python
f.write(d)
```

Your supplied example shows this causes:

```text
TypeError
```

Use the JSON serialization approach shown in your material:

```python
json.dump(d, f)
```

---

### ❌ Mistake 2 — Forgetting `import json`

Wrong:

```python
json.dump(d, f)
```

without:

```python
import json
```

Your examples explicitly import the module first.

---

### ❌ Mistake 3 — Confusing `dump()` and `load()`

Remember:

```text
dump → SAVE direction 📦

load → GET BACK direction 📤
```

---

### ❌ Mistake 4 — Wrong file mode

Your examples use:

```python
"w"
```

with:

```python
json.dump()
```

and:

```python
"r"
```

with:

```python
json.load()
```

Shortcut:

```text
dump + w ✍️

load + r 📖
```

---

# 2️⃣3️⃣ Interview Questions & Answers 🎤

### Q1. What is serialization?

**Answer:** Serialization is the process of converting Python data types into JSON format, according to your notes.

---

### Q2. What is deserialization?

**Answer:** Deserialization converts JSON format back into Python data types.

---

### Q3. Which module are you using?

```python
import json
```

---

### Q4. What does `json.dump()` do?

**Answer:** In your file examples, it serializes Python data and writes the JSON representation to the opened file.

---

### Q5. What does `json.load()` do?

**Answer:** It reads JSON data from the opened file and deserializes it back into Python data.

---

### Q6. What does `indent=4` do?

**Answer:** It formats the JSON in a more readable structure.

---

### Q7. Can `f.write()` directly write the dictionary shown in your example?

**Answer:** No.

Your example gives:

```text
TypeError: write() argument must be str, not dict
```

---

### Q8. What is the easiest difference between `dump()` and `load()`?

```text
dump()
Python → JSON/File

load()
JSON/File → Python
```

---

# 2️⃣4️⃣ MCQs 📝

### 1. Serialization means:

A. JSON → Python
B. Python → JSON
C. Integer → Float
D. Delete data

✅ **Answer: B**

### 2. Deserialization means:

A. Python → JSON
B. JSON → Python
C. List → Tuple
D. File → Delete

✅ **Answer: B**

### 3. Which function serializes to the file in your example?

A. `json.read()`
B. `json.dump()`
C. `json.open()`
D. `json.get()`

✅ **Answer: B**

### 4. Which function deserializes from the file?

A. `json.load()`
B. `json.write()`
C. `json.dump()`
D. `json.read()`

✅ **Answer: A**

### 5. `indent=4` is used for:

A. Deleting JSON
B. Formatting JSON
C. Closing file
D. Renaming file

✅ **Answer: B**

---

# 🏆 PART 1 FINAL SUMMARY

```text
           JSON SERIALIZATION
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
   SERIALIZATION      DESERIALIZATION
        📦                  🔄
          │                 │
          ▼                 ▼
 Python → JSON         JSON → Python
          │                 │
          ▼                 ▼
 json.dump()           json.load()
          │                 │
          ▼                 ▼
       Write               Read
```

## ⚡ Quick Revision

```text
📦 Serialization
→ Python → JSON

🔄 Deserialization
→ JSON → Python

🗂️ import json
→ Use JSON module

📥 json.dump()
→ Python data → file

📤 json.load()
→ File → Python data

✍️ "w"
→ Used with dump() in your examples

📖 "r"
→ Used with load() in your examples

🎨 indent=4
→ Readable formatted JSON

❌ f.write(dictionary)
→ TypeError in your example
```

## 🧠 One-Line Memory Trick

> **`dump()` = Python goes OUT ➡️📄**
> **`load()` = Python data comes BACK 📄➡️🐍**

---

# 📘 NEXT — PART 2: CUSTOM CLASS OBJECT SERIALIZATION 🏦

Your supplied code next introduces the important problem:

```python
a = Bank("Ramesh", 30, 4000000)

json.dump(a, f)
```

which gives:

```text
TypeError:
Object of type Bank is not JSON serializable
```

Then your material solves it in **two ways**:

```text
🏦 Bank Object
     │
     ├── default=get_info
     │
     └── a.__dict__
```

After that comes:

```text
🥒 PICKLING
pickle.dump()

🔄 UNPICKLING
pickle.load()

💾 wb / rb
```

That is the next part.
====
# 📘 PART 2 — JSON SERIALIZATION OF CUSTOM CLASS OBJECTS 🏦

Now we continue with the next section from **your supplied code**.

You already learned:

```text
Python List / Dictionary
        ↓
    json.dump()
        ↓
       JSON
```

But now we have a new problem:

```text
Custom Class Object 🏦
        ↓
    json.dump()
        ↓
        ❌
```

Let's understand **why**.

---

# 1️⃣ What is a Custom Object? 🏦

You created your own class:

```python
class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
```

Then:

```python
a = Bank("Ramesh", 30, 4000000)
```

Here:

```text
Bank
 ↓
Class / Blueprint 🏗️

a
 ↓
Bank Object 🏦
```

The object contains:

```text
a
│
├── name    → "Ramesh"
├── age     → 30
└── balance → 4000000
```

---

# 2️⃣ The Problem ❌

Your code tries:

```python
with open("new.json", "w") as f:
    json.dump(a, f)
```

And your supplied notes give:

```text
TypeError:
Object of type Bank is not JSON serializable
```

## 🤔 Why?

Because `a` is:

```text
a
↓
Bank Object
↓
Custom Python Object
```

Your notes explicitly say:

> **JSON cannot directly serialize custom Python objects.**

Therefore:

```text
Bank Object
    ↓
json.dump()
    ↓
    ❌
TypeError
```

---

# 3️⃣ What is the Solution? 💡

Your notes say:

> We must first convert the object into a dictionary before using `json.dump()`.

So the basic idea is:

```text
🏦 Bank Object
      ↓
Convert to Dictionary
      ↓
📖 Dictionary
      ↓
json.dump()
      ↓
📄 JSON
```

This is the most important concept in this section.

---

# 4️⃣ Method 1 — Direct Object ❌

Suppose:

```python
import json

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


a = Bank("Ramesh", 30, 60000000)
```

Now:

```python
with open("new.json", "w") as f:
    json.dump(a, f)
```

❌ According to your notes:

```text
TypeError:
Object of type Bank is not JSON serializable
```

### Flow

```text
a
│
▼
Bank Object
│
▼
json.dump(a, f)
│
▼
JSON cannot directly serialize it
│
▼
❌ TypeError
```

---

# 5️⃣ Method 2 — `default=get_info` 🔧

Your notes provide another method.

First create a function:

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
    json.dump(a, f, default=get_info, indent=4)
```

---

# 6️⃣ What Does `get_info()` Do? 🤔

Look carefully:

```python
def get_info(obj):
    return {
        "name": obj.name,
        "age": obj.age,
        "balance": obj.balance
    }
```

It receives an object:

```text
obj
 ↓
Bank Object
```

Then it takes:

```python
obj.name
obj.age
obj.balance
```

and returns a dictionary:

```python
{
    "name": obj.name,
    "age": obj.age,
    "balance": obj.balance
}
```

So:

```text
Bank Object
    ↓
get_info()
    ↓
Dictionary
```

---

# 7️⃣ Dry Run of `get_info()` 🔍

Our object is:

```python
a = Bank("Ramesh", 30, 60000000)
```

So:

```text
a.name
↓
"Ramesh"

a.age
↓
30

a.balance
↓
60000000
```

When `get_info(a)` is used, conceptually it returns:

```python
{
    "name": "Ramesh",
    "age": 30,
    "balance": 60000000
}
```

Now JSON can work with the returned dictionary.

---

# 8️⃣ What Does `default=get_info` Mean? ⭐

Your code:

```python
json.dump(
    a,
    f,
    default=get_info,
    indent=4
)
```

Focus on:

```python
default=get_info
```

In your notes, this function is used when `json.dump()` encounters the custom class object.

Conceptually:

```text
json.dump()
    │
    ▼
Sees Bank Object
    │
    ▼
Cannot directly serialize ❌
    │
    ▼
default=get_info
    │
    ▼
get_info(a)
    │
    ▼
Dictionary
    │
    ▼
JSON serialization ✅
```

### 🧠 Beginner Shortcut

> `default=get_info` → **If JSON cannot handle the object, use `get_info()` to convert it.**

---

# 9️⃣ Complete Example — `default` Method 💻

Based on your supplied code:

```python
import json


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


def get_info(obj):

    return {
        "name": obj.name,
        "age": obj.age,
        "balance": obj.balance
    }


a = Bank("Ramesh", 30, 60000000)


with open("new.json", "w") as f:

    json.dump(
        a,
        f,
        default=get_info,
        indent=4
    )
```

---

# 🔟 Complete Flow Diagram 🔄

```text
          a
          │
          ▼
      Bank Object 🏦
          │
          ▼
     json.dump()
          │
          ▼
Can JSON directly serialize it?
          │
          ▼
         NO ❌
          │
          ▼
 default=get_info
          │
          ▼
     get_info(a)
          │
          ▼
      Dictionary 📖
          │
          ▼
       JSON Data
          │
          ▼
      new.json 📄
```

---

# 1️⃣1️⃣ Method 3 — `__dict__` ⚡

Your supplied material gives a shortcut:

```python
with open("new.json", "w") as f:
    json.dump(a.__dict__, f, indent=4)
```

The important new concept is:

```python
a.__dict__
```

---

# 1️⃣2️⃣ What is `__dict__`? 🧠

For your `Bank` object, `__dict__` gives its instance attributes in dictionary form.

Your object:

```python
a = Bank("Ramesh", 30, 60000000)
```

contains:

```text
name    → Ramesh
age     → 30
balance → 60000000
```

So conceptually:

```python
a.__dict__
```

gives a dictionary like:

```python
{
    "name": "Ramesh",
    "age": 30,
    "balance": 60000000
}
```

---

# 1️⃣3️⃣ Why Does `__dict__` Help? 🤔

Originally:

```python
json.dump(a, f)
```

has:

```text
a
↓
Bank Object ❌
```

But:

```python
json.dump(a.__dict__, f)
```

has:

```text
a.__dict__
↓
Dictionary 📖
↓
json.dump()
↓
JSON ✅
```

### 🧠 Shortcut

```text
a
→ Object 🏦

a.__dict__
→ Object data as Dictionary 📖
```

---

# 1️⃣4️⃣ `default=get_info` vs `__dict__` ⚖️

These are the two methods shown in your notes.

| `default=get_info`                    | `a.__dict__`                             |
| ------------------------------------- | ---------------------------------------- |
| Uses a function                       | Uses object's attribute dictionary       |
| Function manually returns fields      | Gets instance attributes as a dictionary |
| `json.dump(a, ..., default=get_info)` | `json.dump(a.__dict__, ...)`             |
| More explicit conversion              | Shortcut shown in your notes             |

### Memory Trick

```text
Method 1 🔧
Object
 ↓
get_info()
 ↓
Dictionary


Method 2 ⚡
Object
 ↓
__dict__
 ↓
Dictionary
```

Both approaches solve the same main problem in your examples:

```text
CUSTOM OBJECT
      ↓
  DICTIONARY
      ↓
     JSON
```

---

# 1️⃣5️⃣ Deserializing the JSON 📖

Your supplied code then uses:

```python
with open("new.json", "r") as f:
    data = json.load(f)

print(data)
```

## Flow

```text
📄 new.json
     │
     ▼
 json.load(f)
     │
     ▼
Deserialization 🔄
     │
     ▼
Python Data
     │
     ▼
    data
```

### ⚠️ Important Beginner Point

In the code you supplied, `json.load(f)` gives you the loaded Python data; the notes do **not** show reconstructing a new `Bank` object from it.

So don't confuse:

```text
Original:
Bank Object
```

with the demonstrated loaded result:

```text
json.load()
    ↓
Python data
```

---

# 1️⃣6️⃣ Complete JSON Custom Object Summary 🏦

```text
              🏦 Bank Object
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
 default=get_info          __dict__
          │                   │
          ▼                   ▼
      Dictionary           Dictionary
          │                   │
          └─────────┬─────────┘
                    ▼
               json.dump()
                    │
                    ▼
                 JSON 📄
```

---

# 📘 PART 3 — PICKLING 🥒

Now we reach the next major section of your supplied code.

Your notes use:

```python
import pickle
```

and then:

```python
pickle.dump(a, f)
```

This is important because your example directly stores the `Bank` object using Pickle.

---

# 1️⃣7️⃣ What is Pickling? 🥒

## ✅ Definition

Based on your supplied section:

> **Pickling is serialization of a Python object using the `pickle` module.**

Your example:

```text
Python Bank Object
        ↓
    Pickling 🥒
        ↓
     .pkl File
```

---

# 1️⃣8️⃣ What is Unpickling? 🔄

## ✅ Definition

> **Unpickling is deserialization of pickled data back into a Python object.**

```text
.pkl File
    ↓
Unpickling 🔄
    ↓
Python Object
```

### 🧠 Master Trick

> 🥒 **Pickling = Object → File**
> 🔄 **Unpickling = File → Object**

---

# 1️⃣9️⃣ Import Pickle 📦

Your code:

```python
import pickle
```

This makes the `pickle` module available.

The two functions shown in your code are:

```python
pickle.dump()
pickle.load()
```

### Shortcut

```text
pickle.dump()
→ Pickling / Serialization 📦

pickle.load()
→ Unpickling / Deserialization 🔄
```

---

# 2️⃣0️⃣ Pickling Syntax 📝

Your example uses:

```python
with open("new.pkl", "wb") as f:
    pickle.dump(a, f)
```

Look at:

```text
new.pkl
```

and:

```text
wb
```

From your earlier binary chapter:

```text
w → Write
b → Binary

wb → Write Binary 💾
```

So:

```text
Python Object
     ↓
pickle.dump()
     ↓
Binary data
     ↓
new.pkl
```

---

# 2️⃣1️⃣ Complete Pickling Example 🏦

Cleaned up from your supplied code:

```python
import pickle


class Bank:

    def __init__(self, name, age, balance):

        self.name = name
        self.age = age
        self.balance = balance


    def get_info(self):

        return f"{self.name}, {self.age}, {self.balance}"


a = Bank("Ramesh", 30, 10000000)


with open("new.pkl", "wb") as f:

    pickle.dump(a, f)

    print("Object Stored Successfully")
```

---

# 2️⃣2️⃣ Dry Run — Pickling 🔍

### Step 1

```python
a = Bank("Ramesh", 30, 10000000)
```

Create object:

```text
a
│
▼
Bank Object
│
├── name → Ramesh
├── age → 30
└── balance → 10000000
```

### Step 2

```python
open("new.pkl", "wb")
```

Open binary file for writing.

### Step 3

```python
pickle.dump(a, f)
```

According to your example, the object is serialized to the pickle file.

```text
a
↓
Bank Object
↓
pickle.dump()
↓
Pickling
↓
new.pkl 💾
```

---

# 2️⃣3️⃣ What is `pickle.dump()`? 📦

## Definition

In your example, `pickle.dump()` serializes the Python object into the opened pickle file.

### Syntax

```python
pickle.dump(object, file_object)
```

Your example:

```python
pickle.dump(a, f)
```

Here:

```text
a
→ Bank Object

f
→ File Object
```

---

# 2️⃣4️⃣ Unpickling Syntax 🔄

Your code uses:

```python
with open("new.pkl", "rb") as f:
    d = pickle.load(f)
```

Remember:

```text
r → Read
b → Binary

rb → Read Binary 📖💾
```

And:

```python
pickle.load(f)
```

loads/deserializes the pickled object.

---

# 2️⃣5️⃣ Unpickling Flow 🔄

```text
             new.pkl 💾
                 │
                 ▼
                rb
                 │
                 ▼
         pickle.load(f)
                 │
                 ▼
           Unpickling 🔄
                 │
                 ▼
          Python Object 🏦
                 │
                 ▼
                 d
```

---

# 2️⃣6️⃣ Accessing the Loaded Object 🎯

Your code:

```python
print(d.name)
print(d.age)
print(d.balance)
print(d.get_info())
```

This demonstrates that `d` is being used like the loaded `Bank` object.

Conceptually:

```text
d
│
├── d.name
├── d.age
├── d.balance
└── d.get_info()
```

So unlike the JSON example shown earlier, the Pickle example demonstrates loading and then accessing the object's attributes/method.

---

# 2️⃣7️⃣ Important Issue in Your Supplied Unpickling Code ⚠️

Your second `Bank` class contains:

```python
self.balance = age
```

instead of:

```python
self.balance = balance
```

I am **not silently changing your source material**: this difference is present in the code you supplied.

For learning the constructor logic, these mean different things:

```text
self.balance = age
→ balance attribute receives age
```

whereas:

```text
self.balance = balance
→ balance attribute receives balance
```

So pay close attention to this line when revising your class notes.

---

# 2️⃣8️⃣ JSON vs Pickle — Based on Your Examples ⚖️

| JSON Example 🗂️                                         | Pickle Example 🥒                                   |
| -------------------------------------------------------- | --------------------------------------------------- |
| `import json`                                            | `import pickle`                                     |
| `json.dump()`                                            | `pickle.dump()`                                     |
| `json.load()`                                            | `pickle.load()`                                     |
| Your custom object needs conversion before `json.dump()` | Your example directly passes `a` to `pickle.dump()` |
| Example uses `"w"` / `"r"`                               | Example uses `"wb"` / `"rb"`                        |
| `.json` / `.txt` shown                                   | `.pkl` shown                                        |

---

# 2️⃣9️⃣ Most Important Difference ⭐

Your notes demonstrate this very clearly.

### JSON

This fails:

```python
json.dump(a, f)
```

because:

```text
Bank Object
    ↓
JSON
    ↓
❌ Not directly serializable
```

Your notes solve it using:

```text
default=get_info
```

or:

```text
a.__dict__
```

### Pickle

Your example directly uses:

```python
pickle.dump(a, f)
```

So the chapter's demonstrated flow is:

```text
Bank Object
    ↓
pickle.dump()
    ↓
.pkl file
```

---

# 3️⃣0️⃣ Common Mistakes ❌

### ❌ 1. Direct custom object with JSON

```python
json.dump(a, f)
```

Your notes show:

```text
TypeError:
Object of type Bank is not JSON serializable
```

---

### ❌ 2. Forgetting binary mode for the Pickle examples

Your supplied examples use:

```python
"wb"
```

for:

```python
pickle.dump()
```

and:

```python
"rb"
```

for:

```python
pickle.load()
```

Remember:

```text
pickle.dump() + wb

pickle.load() + rb
```

---

### ❌ 3. Confusing JSON and Pickle functions

```text
JSON
→ json.dump()
→ json.load()

Pickle
→ pickle.dump()
→ pickle.load()
```

---

### ❌ 4. Confusing `dump` and `load`

```text
dump
→ SAVE direction ➡️

load
→ LOAD BACK direction ⬅️
```

---

# 3️⃣1️⃣ Interview Questions & Answers 🎤

### Q1. Why can't the `Bank` object in your example be directly serialized with JSON?

**Answer:** Your notes show that `json.dump(a, f)` raises `TypeError: Object of type Bank is not JSON serializable`.

### Q2. How does your code solve it?

Two methods are shown:

```text
1. default=get_info

2. a.__dict__
```

### Q3. What is `__dict__` used for here?

It gives the object's instance attributes in dictionary form, which your example then passes to `json.dump()`.

### Q4. What is pickling?

**Answer:** In your notes, pickling is serialization using the `pickle` module.

### Q5. What is unpickling?

**Answer:** Deserialization of the pickled data back into a Python object.

### Q6. Which function performs pickling?

```python
pickle.dump()
```

### Q7. Which function performs unpickling?

```python
pickle.load()
```

### Q8. Which mode is shown for pickling?

```text
wb
→ Write Binary
```

### Q9. Which mode is shown for unpickling?

```text
rb
→ Read Binary
```

---

# 🏆 FINAL SUMMARY — CUSTOM OBJECT + PICKLE

```text
                  🏦 CUSTOM OBJECT
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
           JSON                    PICKLE
             │                       │
             ▼                       ▼
   Direct object fails ❌      pickle.dump()
             │                       │
      ┌──────┴──────┐                ▼
      │             │             .pkl 💾
      ▼             ▼                │
default=get_info  __dict__           ▼
      │             │          pickle.load()
      ▼             ▼                │
    Dictionary    Dictionary         ▼
      │             │          Python Object 🏦
      └──────┬──────┘
             ▼
         json.dump()
             │
             ▼
           JSON 📄
```

## ⚡ MASTER SHORTCUTS

```text
🏦 Custom Object + JSON
→ Directly fails in your example ❌

🔧 default=get_info
→ Object → Dictionary → JSON

⚡ a.__dict__
→ Object attributes → Dictionary

📦 json.dump()
→ Serialization to JSON file

🔄 json.load()
→ JSON file → Python data


🥒 Pickling
→ Serialization using pickle

📤 Unpickling
→ Deserialization using pickle

🥒 pickle.dump()
→ Object → .pkl

🔄 pickle.load()
→ .pkl → Object

💾 wb
→ Write Binary

📖💾 rb
→ Read Binary
```

### 🧠 One-Minute Memory Trick

> **JSON custom object:** 🏦 → 📖 Dictionary → JSON
> **Pickle:** 🏦 → 🥒 `pickle.dump()` → `.pkl` → `pickle.load()` → 🏦

This completes the **custom-object JSON serialization + Pickling/Unpickling section** from the code you supplied.
====
# 📘 PART 3 — JSON vs PICKLE + COMPLETE EXECUTION FLOW

Now that you understand **serialization, deserialization, custom objects, pickling, and unpickling**, the next step is to connect all of them together.

---

# 1️⃣ Serialization — Big Picture 📦

From your code, serialization appears in two forms:

```text
SERIALIZATION
     │
     ├── 🗂️ JSON
     │
     └── 🥒 Pickle
```

The common idea is:

```text
Python Data / Object
        ↓
   Serialization 📦
        ↓
  Stored Representation
        ↓
       File 💾
```

---

# 2️⃣ Deserialization — Big Picture 🔄

Deserialization reverses the process:

```text
File 💾
   ↓
Stored Representation
   ↓
Deserialization 🔄
   ↓
Python Data / Object
```

### 🧠 Shortcut

```text
SAVE ➡️ Serialization 📦

LOAD ⬅️ Deserialization 🔄
```

---

# 3️⃣ Complete JSON Flow 🗂️

Your JSON examples use:

```python
import json
```

and:

```python
json.dump()
json.load()
```

## Serialization

```text
Python Data 🐍
      ↓
 json.dump()
      ↓
JSON Representation
      ↓
File 📄
```

## Deserialization

```text
File 📄
   ↓
json.load()
   ↓
Python Data 🐍
```

---

# 4️⃣ JSON Syntax 📝

## 📦 Serialization

```python
import json

data = {
    "name": "abc",
    "age": 40
}

with open("new.json", "w") as f:
    json.dump(data, f)
```

### Important line

```python
json.dump(data, f)
```

Think:

```text
data
 ↓
dump
 ↓
file
```

---

# 5️⃣ JSON Deserialization Syntax 🔄

```python
import json

with open("new.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))
```

Think:

```text
file
 ↓
load
 ↓
data
```

---

# 6️⃣ JSON Dry Run 🔍

Suppose:

```python
data = {
    "name": "abc",
    "age": 40
}
```

### Step 1

Python creates the dictionary.

```text
data
 │
 ▼
{
 name : abc,
 age  : 40
}
```

### Step 2

```python
open("new.json", "w")
```

opens the file.

### Step 3

```python
json.dump(data, f)
```

serializes the data into the file.

```text
Python Dictionary
       ↓
  json.dump()
       ↓
   new.json
```

### Step 4

Later:

```python
json.load(f)
```

loads the JSON data.

```text
new.json
    ↓
json.load()
    ↓
Python Data
```

---

# 7️⃣ JSON with List 📋

Your notes also use:

```python
l = [1, 2, 3, 4, 5, "Anwar"]

with open("new.txt", "w") as f:
    json.dump(l, f)
```

Then:

```python
with open("new.txt", "r") as f:
    d = json.load(f)

print(d)
print(type(d))
```

### Flow

```text
Python List 📋
      ↓
 json.dump()
      ↓
 new.txt
      ↓
 json.load()
      ↓
Python List 📋
```

---

# 8️⃣ JSON with Dictionary 📖

Your example:

```python
d = {
    "name": "abc",
    "age": 40
}
```

Serialize:

```python
with open("new.json", "w") as f:
    json.dump(d, f)
```

Deserialize:

```python
with open("new.json", "r") as f:
    data = json.load(f)
```

### Memory Shortcut

```text
Dictionary
    ↓
 dump
    ↓
 JSON

 JSON
    ↓
 load
    ↓
Python Data
```

---

# 9️⃣ JSON with Custom Object 🏦

Now comes the important OOP connection.

Your class:

```python
class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
```

Object:

```python
a = Bank("Ramesh", 30, 60000000)
```

Memory:

```text
              a
              │
              ▼
        ┌───────────────┐
        │  Bank Object  │
        ├───────────────┤
        │ name          │
        │ "Ramesh"      │
        ├───────────────┤
        │ age           │
        │ 30            │
        ├───────────────┤
        │ balance       │
        │ 60000000      │
        └───────────────┘
```

---

# 🔟 Why Does Direct JSON Fail? ❌

Your notes show:

```python
json.dump(a, f)
```

producing:

```text
TypeError:
Object of type Bank is not JSON serializable
```

So your material converts the object first.

---

# 1️⃣1️⃣ Solution 1 — Function 🔧

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
Bank Object
    ↓
get_info()
    ↓
Dictionary
    ↓
json.dump()
    ↓
JSON File
```

---

# 1️⃣2️⃣ Solution 2 — `__dict__` ⚡

Your shortcut:

```python
with open("new.json", "w") as f:
    json.dump(a.__dict__, f, indent=4)
```

### What happens?

```text
a
↓
Bank Object

a.__dict__
↓
{
    "name": "Ramesh",
    "age": 30,
    "balance": 60000000
}
```

Then:

```text
Dictionary
    ↓
json.dump()
    ↓
JSON
```

### 🧠 Shortcut

> **`__dict__` = object's instance attributes as a dictionary**

---

# 1️⃣3️⃣ Now Pickle 🥒

Your second serialization approach uses:

```python
import pickle
```

The important methods are:

```python
pickle.dump()
pickle.load()
```

---

# 1️⃣4️⃣ Pickling 📦

## Definition

In your notes, **Pickling** is serialization using the `pickle` module.

### Syntax

```python
with open("new.pkl", "wb") as f:
    pickle.dump(a, f)
```

### Flow

```text
Bank Object 🏦
      ↓
pickle.dump()
      ↓
Pickling 📦
      ↓
new.pkl 💾
```

---

# 1️⃣5️⃣ Unpickling 🔄

## Definition

Unpickling is the reverse process shown in your notes.

### Syntax

```python
with open("new.pkl", "rb") as f:
    d = pickle.load(f)
```

### Flow

```text
new.pkl 💾
    ↓
pickle.load()
    ↓
Unpickling 🔄
    ↓
Bank Object 🏦
    ↓
d
```

---

# 1️⃣6️⃣ Complete Pickle Example 🏦

```python
import pickle


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name}, {self.age}, {self.balance}"


a = Bank("Ramesh", 30, 10000000)


# Pickling
with open("new.pkl", "wb") as f:

    pickle.dump(a, f)

    print("Object Stored Successfully")


# Unpickling
with open("new.pkl", "rb") as f:

    d = pickle.load(f)


print(d.name)
print(d.age)
print(d.balance)
print(d.get_info())
```

---

# 1️⃣7️⃣ Dry Run — Pickling 🔍

## Step 1

```python
a = Bank("Ramesh", 30, 10000000)
```

Memory:

```text
a
│
▼
Bank Object
│
├── name    → Ramesh
├── age     → 30
└── balance → 10000000
```

## Step 2

```python
with open("new.pkl", "wb") as f:
```

File opened in:

```text
w → Write
b → Binary

wb → Write Binary 💾
```

## Step 3

```python
pickle.dump(a, f)
```

Object is serialized into the pickle file.

```text
a
↓
pickle.dump()
↓
new.pkl
```

## Step 4

Later:

```python
with open("new.pkl", "rb") as f:
```

```text
r → Read
b → Binary

rb → Read Binary
```

## Step 5

```python
d = pickle.load(f)
```

```text
new.pkl
   ↓
pickle.load()
   ↓
Bank Object
   ↓
d
```

## Step 6

Now your code accesses:

```python
d.name
d.age
d.balance
d.get_info()
```

---

# 1️⃣8️⃣ Why `wb` and `rb`? 💾

Your Pickle examples use binary file modes.

```text
wb
│
├── w = Write
└── b = Binary
```

and:

```text
rb
│
├── r = Read
└── b = Binary
```

### Easy Formula

```text
pickle.dump() + wb 📦

pickle.load() + rb 📖
```

---

# 1️⃣9️⃣ JSON vs Pickle ⚖️

Based strictly on the examples you supplied:

| Feature              | 🗂️ JSON                         | 🥒 Pickle                       |
| -------------------- | -------------------------------- | ------------------------------- |
| Module               | `json`                           | `pickle`                        |
| Serialization        | `json.dump()`                    | `pickle.dump()`                 |
| Deserialization      | `json.load()`                    | `pickle.load()`                 |
| File modes shown     | `w`, `r`                         | `wb`, `rb`                      |
| Custom `Bank` object | Needs conversion in your example | Passed directly in your example |
| Object helper shown  | `default=get_info`, `__dict__`   | Not required in your example    |
| Extension shown      | `.json`, `.txt`                  | `.pkl`                          |

---

# 2️⃣0️⃣ `json.dump()` vs `pickle.dump()` ⚖️

### JSON

```python
json.dump(a.__dict__, f)
```

Flow shown:

```text
Bank Object
    ↓
Dictionary
    ↓
json.dump()
```

### Pickle

```python
pickle.dump(a, f)
```

Flow shown:

```text
Bank Object
    ↓
pickle.dump()
```

### 🧠 Memory Trick

```text
JSON example:
OBJECT → DICTIONARY → FILE

PICKLE example:
OBJECT → FILE
```

---

# 2️⃣1️⃣ `dump()` vs `load()` ⭐

This shortcut works for both modules in your examples:

```text
            DUMP 📦
              ↓
       Python → File


            LOAD 📤
              ↓
       File → Python
```

### JSON

```python
json.dump()
json.load()
```

### Pickle

```python
pickle.dump()
pickle.load()
```

---

# 2️⃣2️⃣ Common Mistakes ❌

### ❌ Mistake 1

```python
f.write({
    "name": "abc"
})
```

Your supplied example shows that `write()` does not directly accept the dictionary.

---

### ❌ Mistake 2

```python
json.dump(a, f)
```

Your custom `Bank` object example raises a serialization `TypeError`.

Your notes solve this using:

```python
default=get_info
```

or:

```python
a.__dict__
```

---

### ❌ Mistake 3

Using text mode in the Pickle pattern instead of the binary modes shown in your notes.

Remember:

```text
pickle.dump() → wb

pickle.load() → rb
```

---

### ❌ Mistake 4 — Constructor Typo

Your supplied unpickling section contains:

```python
self.balance = age
```

That line assigns the `age` parameter to `balance`.

The intended constructor pattern elsewhere in your notes is:

```python
self.balance = balance
```

For learning, keep these two assignments clearly separate.

---

# 2️⃣3️⃣ Interview Questions 🎤

### Q1. What is serialization?

**Answer:** In your chapter, serialization converts Python data into a storable representation, with JSON and Pickle shown as approaches.

### Q2. What is deserialization?

**Answer:** It is the reverse process of getting Python data/object back from the stored representation.

### Q3. Which JSON methods are shown?

```python
json.dump()
json.load()
```

### Q4. Which Pickle methods are shown?

```python
pickle.dump()
pickle.load()
```

### Q5. What is pickling?

**Answer:** Serialization using the `pickle` module in your notes.

### Q6. What is unpickling?

**Answer:** Loading/deserializing the pickled object.

### Q7. Why does `json.dump(a, f)` fail for your `Bank` object?

**Answer:** The supplied example says:

```text
Object of type Bank is not JSON serializable
```

### Q8. How did your code solve that?

```text
default=get_info
```

or:

```text
a.__dict__
```

### Q9. Which mode is used with `pickle.dump()`?

```text
wb
```

### Q10. Which mode is used with `pickle.load()`?

```text
rb
```

---

# 2️⃣4️⃣ MCQs 📝

**1. Which function serializes using JSON?**

A. `json.read()`
B. `json.dump()` ✅
C. `json.open()`
D. `json.write()`

**2. Which function deserializes JSON from a file?**

A. `json.dump()`
B. `json.load()` ✅
C. `json.get()`
D. `json.convert()`

**3. Pickling uses which module?**

A. `sys`
B. `os`
C. `pickle` ✅
D. `time`

**4. Pickling in your example uses:**

A. `pickle.dump()` ✅
B. `pickle.read()`
C. `pickle.write()`
D. `pickle.get()`

**5. Unpickling uses:**

A. `pickle.dump()`
B. `pickle.load()` ✅
C. `pickle.open()`
D. `pickle.get()`

**6. `wb` means:**

A. Write Boolean
B. Write Binary ✅
C. Write Back
D. Write Buffer

**7. `rb` means:**

A. Read Binary ✅
B. Read Boolean
C. Return Binary
D. Read Buffer

---

# 🏆 COMPLETE CHAPTER SHORTCUT

```text
        📦 SERIALIZATION
               │
       Python → Storage
               │
       ┌───────┴───────┐
       ▼               ▼
    🗂️ JSON          🥒 PICKLE
       │               │
 json.dump()      pickle.dump()
       │               │
       ▼               ▼
 JSON File          .pkl File


       🔄 DESERIALIZATION
               │
       Storage → Python
               │
       ┌───────┴───────┐
       ▼               ▼
    🗂️ JSON          🥒 PICKLE
       │               │
 json.load()      pickle.load()
       │               │
       ▼               ▼
 Python Data      Python Object
```

## 🚀 10-Second Interview Revision

```text
📦 Serialization
Python → Storage

🔄 Deserialization
Storage → Python

🗂️ JSON
dump → Save
load → Load

🏦 JSON Custom Object
→ default=get_info
→ or __dict__

🥒 Pickling
pickle.dump() + wb

🔄 Unpickling
pickle.load() + rb

🎨 indent=4
Readable JSON
```

### ⭐ Golden Formula

> **JSON:** `dump()` ➡️ file, `load()` ⬅️ file
> **Pickle:** `dump()` ➡️ `.pkl`, `load()` ⬅️ `.pkl`
> **Custom JSON object in your example:** Object ➡️ Dictionary ➡️ JSON.
