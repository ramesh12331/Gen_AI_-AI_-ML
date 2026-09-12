# 🐍 Python Tuple, Set, JSON & Operators – Complete Notes

---

# 📦 Tuple

## 📖 Definition

A **Tuple** is an **ordered** and **immutable** collection of values.

✅ Ordered → Items are stored in a fixed order.

✅ Immutable → Values cannot be changed after creation.

✅ Allows duplicate values.

---

## ✍️ Syntax

```python
variable_name = (value1, value2, value3, ..., valueN)
```

### 📌 Example

```python
employees = ("Ramesh", "Suresh", "Priya")

print(employees)
```

### 📤 Output

```text
('Ramesh', 'Suresh', 'Priya')
```

---

## 📌 Indexing

| Value  | Index |
| ------ | ----: |
| Ramesh |     0 |
| Suresh |     1 |
| Priya  |     2 |

Access a value:

```python
print(employees[0])
```

Output

```text
Ramesh
```

---

## ❌ Can we modify a Tuple?

No.

```python
employees[0] = "Kiran"
```

Output

```text
TypeError
```

---

## ⭐ Features of Tuple

✔ Ordered

✔ Immutable

✔ Allows duplicate values

✔ Faster than List

---

# 🎯 Set

## 📖 Definition

A **Set** is an **unordered**, **mutable** collection of **unique** values.

---

## ✍️ Syntax

```python
variable_name = {value1, value2, value3}
```

---

## 💻 Example

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

---

## ⭐ Features

✔ Unordered

✔ Mutable

✔ Does not allow duplicate values

---

## 📌 Duplicate Example

```python
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)
```

Output

```text
{10, 20, 30, 40}
```

Duplicates are removed automatically.

---

## ➕ Add a Value

```python
numbers.add(50)
```

---

## ❌ Remove a Value

```python
numbers.remove(20)
```

---

# 🌐 JSON (JavaScript Object Notation)

## 📖 Definition

**JSON** stands for **JavaScript Object Notation**.

It is a lightweight data format used to store and exchange data between different applications and technologies.

---

## ⭐ Why JSON?

✔ Easy to read

✔ Easy to write

✔ Human readable

✔ Lightweight

✔ Supported by almost every programming language

---

## 📌 JSON Structure

JSON stores data as:

* Dictionary (Object)
* List of Dictionaries (Array of Objects)

---

## 💻 Example 1 – Dictionary

```json
{
    "name": "Ramesh",
    "department": "IT",
    "salary": 45000
}
```

---

## 💻 Example 2 – List of Dictionaries

```json
[
    {
        "id":101,
        "name":"Ramesh"
    },
    {
        "id":102,
        "name":"Suresh"
    }
]
```

---

# 🛒 Product JSON Example

```json
[
    {
        "name":"Laptop",
        "price":65000,
        "discount":"10%",
        "average_rating":4.5,
        "rating_count":250
    },
    {
        "name":"Mobile",
        "price":25000,
        "discount":"15%",
        "average_rating":4.4,
        "rating_count":540
    },
    {
        "name":"Headphones",
        "price":2000,
        "discount":"20%",
        "average_rating":4.3,
        "rating_count":150
    }
]
```

---

# ⚙️ Operators

## 📖 Definition

Operators are special symbols used to perform operations on variables and values.

---

# 1️⃣ Arithmetic Operators

| Operator | Meaning        | Example     |
| -------- | -------------- | ----------- |
| +        | Addition       | 10 + 5 = 15 |
| -        | Subtraction    | 10 - 5 = 5  |
| *        | Multiplication | 10 * 5 = 50 |
| /        | Division       | 10 / 5 = 2  |
| %        | Modulus        | 10 % 3 = 1  |
| //       | Floor Division | 10 // 3 = 3 |
| **       | Exponent       | 2 ** 3 = 8  |

---

## Example

```python
a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

# 2️⃣ Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal to              |
| !=       | Not Equal             |
| >        | Greater Than          |
| <        | Less Than             |
| >=       | Greater Than or Equal |
| <=       | Less Than or Equal    |

Example

```python
print(20 > 10)
print(20 == 10)
```

---

# 3️⃣ Logical Operators

| Operator | Meaning                        |
| -------- | ------------------------------ |
| and      | Both conditions must be True   |
| or       | At least one condition is True |
| not      | Reverses the result            |

Example

```python
age = 25

print(age > 18 and age < 60)
```

---

# 4️⃣ Assignment Operators

| Operator | Example |
| -------- | ------- |
| =        | x = 10  |
| +=       | x += 5  |
| -=       | x -= 2  |
| *=       | x *= 3  |
| /=       | x /= 2  |

---

# 5️⃣ Membership Operators

| Operator | Meaning              |
| -------- | -------------------- |
| in       | Value exists         |
| not in   | Value does not exist |

Example

```python
employees = ["Ramesh", "Suresh"]

print("Ramesh" in employees)
```

---

# 6️⃣ Identity Operators

| Operator | Meaning           |
| -------- | ----------------- |
| is       | Same object       |
| is not   | Different objects |

Example

```python
a = [1,2]
b = a

print(a is b)
```

---

# 📚 Final Summary

## 📦 Tuple

✔ Ordered

✔ Immutable

✔ Allows duplicates

Uses **()**

---

## 🎯 Set

✔ Unordered

✔ Mutable

✔ Unique values only

Uses **{}**

---

## 🌐 JSON

✔ JavaScript Object Notation

✔ Used for storing and exchanging data

✔ Stores Dictionary and List of Dictionaries

---

## ⚙️ Operators

➕ Arithmetic

⚖️ Comparison

🧠 Logical

📝 Assignment

🔍 Membership

🆔 Identity

---

# 🎯 Interview Questions & Answers

## ❓1. What is a Tuple?

**Answer:**

A tuple is an ordered and immutable collection of values.

---

## ❓2. Can we modify a Tuple?

**Answer:**

No. A tuple is immutable, so its values cannot be changed after creation.

---

## ❓3. What is a Set?

**Answer:**

A set is an unordered and mutable collection of unique values.

---

## ❓4. Does a Set allow duplicate values?

**Answer:**

No. A set automatically removes duplicate values.

---

## ❓5. What is JSON?

**Answer:**

JSON stands for **JavaScript Object Notation**. It is a lightweight format used to store and exchange data.

---

## ❓6. Why is JSON used?

**Answer:**

JSON is easy to read, lightweight, human-readable, and supported by almost every programming language.

---

## ❓7. What are operators?

**Answer:**

Operators are symbols used to perform operations on variables and values.

---

## ❓8. Name the types of operators in Python.

**Answer:**

* ➕ Arithmetic Operators
* ⚖️ Comparison Operators
* 🧠 Logical Operators
* 📝 Assignment Operators
* 🔍 Membership Operators
* 🆔 Identity Operators

---

## ❓9. Difference between List and Tuple?

| List      | Tuple     |
| --------- | --------- |
| Mutable   | Immutable |
| Uses `[]` | Uses `()` |
| Slower    | Faster    |

---

## ❓10. Difference between List and Set?

| List              | Set                |
| ----------------- | ------------------ |
| Ordered           | Unordered          |
| Allows duplicates | Removes duplicates |
| Uses indexes      | No indexing        |

---

# 🌟 Quick Revision

📦 **Tuple** → Ordered + Immutable

🎯 **Set** → Unordered + Unique Values

🌐 **JSON** → Data Exchange Format

⚙️ **Operators** → Perform operations on data
