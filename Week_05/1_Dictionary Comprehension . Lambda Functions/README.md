Excellent! Your **Dictionary code** is well organized and covers almost all beginner topics. 

Let's start learning it **chapter by chapter**, just like we did for Functions, Lists, Strings, Sets, Tuples, and Lambda.

---

# 📘 Python Dictionary Master Handbook

# 📖 Chapter 1 – Introduction to Dictionaries (Beginner to Interview Level)

> ⭐ **Dictionary** is one of the most important Python data structures. It stores data in **key-value pairs** and is widely used in APIs, JSON data, databases, web development, and real-world applications.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand what a Dictionary is.
* ✅ Know why Dictionaries are used.
* ✅ Create Dictionaries.
* ✅ Understand Dictionary characteristics.
* ✅ Compare Dictionary with other collections.
* ✅ Answer interview questions.

---

# 📖 What is a Dictionary?

## ✅ Definition

A **Dictionary** is a **mutable collection of key-value pairs**.

Each **key** is used to access its corresponding **value**.

---

## Syntax

```python
dictionary_name = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

---

## Example

```python
student = {
    "name": "Rahul",
    "age": 25,
    "city": "Hyderabad"
}

print(student)
```

### Output

```text
{'name': 'Rahul', 'age': 25, 'city': 'Hyderabad'}
```

---

# 📖 Why Do We Use Dictionaries?

Instead of storing related values separately:

```python
name = "Rahul"
age = 25
city = "Hyderabad"
```

We can group them together:

```python
student = {
    "name": "Rahul",
    "age": 25,
    "city": "Hyderabad"
}
```

This makes the data easier to manage.

---

# 🌍 Real-Life Examples

## 👨 Student Details

```python
student = {
    "name": "Rahul",
    "age": 24,
    "marks": 90
}
```

---

## 👨 Employee Details

```python
employee = {
    "id": 101,
    "name": "Ajay",
    "salary": 50000
}
```

---

## 🛒 Product Information

```python
product = {
    "id": 101,
    "name": "Laptop",
    "price": 60000
}
```

---

## 🌐 JSON Data (API Response)

```python
{
    "success": True,
    "message": "Login Successful"
}
```

Most JSON data is stored as Python dictionaries.

---

# 📖 Creating a Dictionary

## Example

```python
d = {
    "name": "Rahul",
    "age": 40,
    "salary": 600000
}

print(d)
```

Output

```text
{'name': 'Rahul', 'age': 40, 'salary': 600000}
```

---

# 📖 Characteristics of Dictionary

| Feature               | Dictionary    |
| --------------------- | ------------- |
| Ordered (Python 3.7+) | ✅ Yes         |
| Mutable               | ✅ Yes         |
| Key-Value Pairs       | ✅ Yes         |
| Duplicate Keys        | ❌ Not Allowed |
| Duplicate Values      | ✅ Allowed     |
| Indexing              | ❌ No          |
| Slicing               | ❌ No          |

---

# 📖 Keys Must Be Unique

```python
student = {
    "name": "Rahul",
    "name": "Ajay"
}

print(student)
```

Output

```text
{'name': 'Ajay'}
```

The last value overwrites the previous one.

---

# 📖 Values Can Be Duplicated

```python
student = {
    "name": "Rahul",
    "friend": "Rahul"
}
```

This is perfectly valid.

---

# 📖 Dictionary is Mutable

You can modify values after creation.

```python
student = {
    "name": "Rahul"
}

student["name"] = "Ajay"

print(student)
```

Output

```text
{'name': 'Ajay'}
```

---

# 📖 Dictionary Does Not Support Indexing

❌ Wrong

```python
student = {
    "name": "Rahul"
}

print(student[0])
```

Output

```text
TypeError / KeyError
```

A Dictionary uses **keys**, not numeric indexes.

Correct:

```python
print(student["name"])
```

---

# 📊 Dictionary vs List vs Tuple vs Set

| Feature          | List | Tuple | Set | Dictionary |
| ---------------- | ---- | ----- | --- | ---------- |
| Ordered          | ✅    | ✅     | ❌   | ✅          |
| Mutable          | ✅    | ❌     | ✅   | ✅          |
| Duplicate Values | ✅    | ✅     | ❌   | ✅          |
| Key-Value Pairs  | ❌    | ❌     | ❌   | ✅          |
| Indexing         | ✅    | ✅     | ❌   | ❌          |

---

# 🌍 Real-Life Applications

Dictionaries are used in:

* 👨 Student records
* 👨 Employee information
* 🛒 Product details
* 🌐 JSON data
* 📱 Mobile contacts
* 💳 Banking systems
* 📊 API responses
* 🗄 Database records

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Trying to use indexing.

```python
student[0]
```

Use a **key**, not an index.

---

## ❌ Mistake 2

Using duplicate keys.

```python
{
    "name":"A",
    "name":"B"
}
```

Only the last value remains.

---

## ❌ Mistake 3

Thinking Dictionaries are unordered.

Since **Python 3.7**, Dictionaries preserve insertion order.

---

# 💡 Programmer Tips

Remember:

```text
Dictionary

↓

Key : Value
```

```text
Keys

↓

Unique
```

```text
Values

↓

Can Repeat
```

```text
Dictionary

↓

Mutable
```

```text
Dictionary

↓

No Indexing
```

---

# 🎓 Interview Questions with Answers

### ❓1. What is a Dictionary?

✅ **Answer:**

A Dictionary is a mutable collection of key-value pairs.

---

### ❓2. Are Dictionary keys unique?

✅ **Answer:**

Yes. Duplicate keys are not allowed.

---

### ❓3. Can Dictionary values be duplicated?

✅ **Answer:**

Yes.

---

### ❓4. Is a Dictionary mutable?

✅ **Answer:**

Yes.

---

### ❓5. Does a Dictionary support indexing?

✅ **Answer:**

No. Values are accessed using keys.

---

# ⭐ MCQs

### Q1. Which symbol is used to create a Dictionary?

A. `[]`

B. `()`

C. `{}`

D. `<>`

✅ **Answer:** **C**

---

### Q2. Which statement is true?

A. Keys can be duplicated.

B. Keys are unique.

C. Dictionaries use indexing.

D. Dictionaries don't store values.

✅ **Answer:** **B**

---

### Q3. Which collection stores data as key-value pairs?

A. List

B. Tuple

C. Set

D. Dictionary

✅ **Answer:** **D**

---

### Q4. Are Dictionaries mutable?

A. Yes

B. No

✅ **Answer:** **A**

---

# 📝 Practice Programs

### 1. Student Dictionary

```python
student = {
    "name": "Ramesh",
    "age": 24,
    "city": "Hyderabad"
}

print(student)
```

---

### 2. Product Dictionary

```python
product = {
    "id": 101,
    "name": "Laptop",
    "price": 60000
}

print(product)
```

---

### 3. Employee Dictionary

```python
employee = {
    "id": 1,
    "name": "Ajay",
    "salary": 50000
}

print(employee)
```

---

# 📌 Chapter Summary

```text
              PYTHON DICTIONARY
                     │
        ┌────────────┼────────────┐
        │            │            │
    Key-Value     Mutable     Ordered
       Pairs                     (3.7+)
        │
        ├────────────┬────────────┐
        │            │            │
   Unique Keys   Duplicate     No Indexing
                  Values
```

---

# 🏆 Congratulations!

You have completed **Python Dictionary – Chapter 1: Introduction to Dictionaries**.

### ✅ You learned:

* What is a Dictionary
* Why Dictionaries are used
* Creating Dictionaries
* Characteristics
* Keys vs Values
* Dictionary vs List/Tuple/Set
* Interview Questions
* MCQs
* Practice Programs

---

# 📖 Next Chapter

## **Chapter 2 – Accessing, Adding, Updating & Removing Dictionary Items**

We'll cover your next code topics:

```python
d["name"]
d.get("gender")

d["city"] = "Hyderabad"

d["name"] = "Ajay"

d.pop("salary")
d.popitem()
del d["age"]
d.clear()
```

This chapter will explain **every Dictionary method with dry runs, memory diagrams, interview questions, MCQs, and practice programs**, just like the previous chapters.
===
# 📘 Python Dictionary Master Handbook

# 📖 Chapter 2 – Accessing, Adding, Updating & Removing Dictionary Items (Beginner to Interview Level)

> ⭐ In this chapter, you'll learn how to **access, add, update, and remove Dictionary items**. These are the most frequently used Dictionary operations in Python and are commonly asked in interviews.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Access Dictionary values.
* ✅ Use `get()` safely.
* ✅ Add new key-value pairs.
* ✅ Update existing values.
* ✅ Remove items using `pop()`, `popitem()`, `del`, and `clear()`.
* ✅ Solve interview questions.

---

# 📖 Accessing Dictionary Values

Dictionary values are accessed using **keys**, not indexes.

---

## Method 1: Using Square Brackets `[]`

### Syntax

```python
dictionary[key]
```

### Example

```python
d = {
    "name": "Rahul",
    "age": 40,
    "salary": 600000
}

print(d["name"])
print(d["salary"])
```

### Output

```text
Rahul
600000
```

---

## 🔍 Dry Run

```text
Dictionary

{
"name":"Rahul",
"age":40,
"salary":600000
}

↓

Key = "name"

↓

Rahul
```

---

# ⚠ What Happens if the Key Doesn't Exist?

```python
print(d["gender"])
```

### Output

```text
KeyError: 'gender'
```

The program stops with an error.

---

# 📖 get() Method

## ✅ Definition

The `get()` method safely returns the value of a key.

If the key doesn't exist, it returns **None** (or a default value if provided).

---

## Syntax

```python
dictionary.get(key)
```

---

## Example

```python
print(d.get("gender"))
```

### Output

```text
None
```

No error occurs.

---

## Default Value Example

```python
print(d.get("gender", "Not Available"))
```

### Output

```text
Not Available
```

---

# 📊 `[]` vs `get()`

| `[]`                         | `get()`                         |
| ---------------------------- | ------------------------------- |
| Raises `KeyError` if missing | Returns `None` or default value |
| Best when key must exist     | Best when key may not exist     |

---

# 📖 Adding New Items

A new key-value pair can be added using assignment.

### Syntax

```python
dictionary["new_key"] = value
```

---

## Example

```python
d = {
    "name": "Rahul",
    "age": 40
}

d["city"] = "Hyderabad"

print(d)
```

### Output

```text
{
'name':'Rahul',
'age':40,
'city':'Hyderabad'
}
```

---

## 🔍 Memory Diagram

```text
Before

{
name
age
}

↓

Add city

↓

{
name
age
city
}
```

---

# 📖 Updating Existing Values

If the key already exists, Python updates its value.

---

## Example

```python
d = {
    "name": "Rahul"
}

d["name"] = "Ajay"

print(d)
```

### Output

```text
{'name': 'Ajay'}
```

---

## Dry Run

```text
Before

"name"

↓

Rahul

↓

Update

↓

Ajay
```

---

# 📖 Removing Items using `pop()`

## ✅ Definition

`pop()` removes a key and returns its value.

---

## Syntax

```python
dictionary.pop(key)
```

---

## Example

```python
d = {
    "name":"Rahul",
    "salary":600000
}

salary = d.pop("salary")

print(salary)
print(d)
```

### Output

```text
600000

{'name':'Rahul'}
```

---

## ⚠ If Key Doesn't Exist

```python
d.pop("gender")
```

Output

```text
KeyError
```

---

# 📖 `popitem()`

## ✅ Definition

Removes the **last inserted key-value pair**.

---

## Example

```python
d = {
    "name":"Rahul",
    "age":40,
    "city":"Hyderabad"
}

print(d.popitem())

print(d)
```

### Output

```text
('city', 'Hyderabad')

{'name':'Rahul','age':40}
```

---

## 🔍 Memory Diagram

```text
Before

name

age

city

↓

popitem()

↓

city removed
```

---

# 📖 `del` Statement

## ✅ Definition

Deletes a specific key.

---

## Syntax

```python
del dictionary[key]
```

---

## Example

```python
d = {
    "name":"Rahul",
    "age":40
}

del d["age"]

print(d)
```

### Output

```text
{'name':'Rahul'}
```

---

# 📖 `clear()`

## ✅ Definition

Removes **all items** from the Dictionary.

---

## Example

```python
d = {
    "name":"Rahul",
    "age":40
}

d.clear()

print(d)
```

### Output

```text
{}
```

---

# 📊 Removal Methods Comparison

| Method      | Removes            | Returns Value | Error if Missing?          |
| ----------- | ------------------ | ------------- | -------------------------- |
| `pop(key)`  | Specific key       | ✅ Yes         | ✅ Yes                      |
| `popitem()` | Last inserted item | ✅ Yes         | ❌ (if dictionary is empty) |
| `del`       | Specific key       | ❌ No          | ✅ Yes                      |
| `clear()`   | All items          | ❌ No          | ❌ No                       |

---

# 🌍 Real-Life Examples

## Student Record

```python
student = {
    "name":"Rahul",
    "marks":90
}

print(student.get("marks"))
```

---

## Employee Update

```python
employee = {
    "salary":50000
}

employee["salary"] = 60000

print(employee)
```

---

## Shopping Cart

```python
cart = {
    "Mobile":500,
    "Shoes":200
}

cart.pop("Shoes")

print(cart)
```

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using indexing.

```python
d[0]
```

Dictionaries use **keys**, not indexes.

---

## ❌ Mistake 2

Using `pop()` on a missing key.

```python
d.pop("abc")
```

Raises `KeyError`.

Use:

```python
d.get("abc")
```

when you're only reading a value.

---

## ❌ Mistake 3

Thinking `clear()` deletes the Dictionary.

```python
d.clear()
```

It only removes all items.

The variable still exists.

---

# 💡 Programmer Tips

Remember

```text
[]

↓

Direct Access
```

```text
get()

↓

Safe Access
```

```text
key = value

↓

Add / Update
```

```text
pop()

↓

Remove One Key
```

```text
popitem()

↓

Remove Last Item
```

```text
del

↓

Delete Specific Key
```

```text
clear()

↓

Remove Everything
```

---

# 🎓 Interview Questions with Answers

### ❓1. How do you access a Dictionary value?

✅ **Answer:**

Using the key.

```python
student["name"]
```

---

### ❓2. Difference between `[]` and `get()`?

✅ **Answer:**

* `[]` raises `KeyError` if the key doesn't exist.
* `get()` returns `None` or a default value.

---

### ❓3. How do you add a new item?

✅ **Answer:**

```python
d["city"] = "Hyderabad"
```

---

### ❓4. How do you update an existing value?

✅ **Answer:**

Assign a new value to the existing key.

```python
d["name"] = "Ajay"
```

---

### ❓5. Difference between `pop()` and `popitem()`?

✅ **Answer:**

* `pop(key)` removes a specific key.
* `popitem()` removes the last inserted key-value pair.

---

### ❓6. What does `clear()` do?

✅ **Answer:**

It removes all key-value pairs but keeps the Dictionary object.

---

# ⭐ MCQs

### Q1. Which method safely returns a value without raising `KeyError`?

A. `[]`

B. `get()`

C. `pop()`

D. `del`

✅ **Answer:** **B**

---

### Q2. Which method removes the last inserted item?

A. `pop()`

B. `clear()`

C. `popitem()`

D. `remove()`

✅ **Answer:** **C**

---

### Q3. Which statement updates an existing key?

A.

```python
d.update()
```

B.

```python
d["name"] = "Ajay"
```

C.

```python
append()
```

D.

```python
insert()
```

✅ **Answer:** **B**

---

### Q4. Which method removes all items?

A. `delete()`

B. `pop()`

C. `clear()`

D. `remove()`

✅ **Answer:** **C**

---

# 📝 Practice Programs

## ⭐ Easy

### 1. Access Values

```python
student = {
    "name": "Ramesh",
    "age": 24
}

print(student["name"])
print(student.get("age"))
```

---

### 2. Add a New Key

```python
student["city"] = "Hyderabad"

print(student)
```

---

## ⭐⭐ Medium

### Update Salary

```python
employee = {
    "name": "Ajay",
    "salary": 50000
}

employee["salary"] = 60000

print(employee)
```

---

## ⭐⭐⭐ Challenge

```python
employee = {
    "id":101,
    "name":"Rahul",
    "salary":50000
}

# 1. Print name
# 2. Add city
# 3. Update salary
# 4. Remove id
# 5. Print final dictionary
```

### Answer

```python
employee = {
    "id":101,
    "name":"Rahul",
    "salary":50000
}

print(employee["name"])

employee["city"] = "Hyderabad"

employee["salary"] = 60000

employee.pop("id")

print(employee)
```

---

# 📌 Chapter Summary

```text
          DICTIONARY OPERATIONS
                 │
      ┌──────────┼──────────┐
      │          │          │
   Access      Modify     Remove
      │          │          │
 []         Add Key      pop()
 get()      Update       popitem()
                         del
                         clear()
```

---

# 🏆 Congratulations!

You have completed **Python Dictionary – Chapter 2: Accessing, Adding, Updating & Removing Items**.

### ✅ You learned:

* Dictionary access using `[]`
* `get()` method
* Adding new keys
* Updating values
* `pop()`
* `popitem()`
* `del`
* `clear()`
* Interview questions
* MCQs
* Practice programs

---

# 📖 Next Chapter

## **Chapter 3 – `keys()`, `values()`, `items()`, Looping & Dictionary Conditions**

We'll cover:

```python
d.keys()
d.values()

for key, value in d.items():
    print(key, value)

if "name" in student:
    print("Key Found")
```

This chapter explains **dictionary traversal, membership testing, and iteration**, which are essential for interviews and real-world Python programming.
---
# 📘 Python Dictionary Master Handbook

# 📖 Chapter 3 – `keys()`, `values()`, `items()`, Looping & Dictionary Conditions (Beginner to Interview Level)

> ⭐ In this chapter, you'll learn how to **read all keys, values, key-value pairs, loop through dictionaries, and check whether a key exists**. These are some of the **most frequently asked Dictionary interview topics**.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Get all keys.
* ✅ Get all values.
* ✅ Get key-value pairs.
* ✅ Loop through a Dictionary.
* ✅ Use `items()`.
* ✅ Check whether a key exists.
* ✅ Solve interview questions.

---

# 📖 Sample Dictionary

We'll use this dictionary throughout the chapter.

```python
student = {
    "name": "Rahul",
    "age": 40,
    "salary": 600000
}
```

---

# 📖 1. `keys()` Method

## ✅ Definition

`keys()` returns **all keys** in the dictionary.

---

## Syntax

```python
dictionary.keys()
```

---

## Example

```python
student = {
    "name": "Rahul",
    "age": 40,
    "salary": 600000
}

print(student.keys())
```

### Output

```text
dict_keys(['name', 'age', 'salary'])
```

---

## Dry Run

```text
Dictionary

{
name
age
salary
}

↓

keys()

↓

name
age
salary
```

---

# 🌍 Real-Life Example

```python
employee = {
    "id":101,
    "name":"Ajay",
    "salary":50000
}

print(employee.keys())
```

Output

```text
dict_keys(['id', 'name', 'salary'])
```

---

# 📖 2. `values()` Method

## ✅ Definition

Returns **all values** in the dictionary.

---

## Syntax

```python
dictionary.values()
```

---

## Example

```python
print(student.values())
```

### Output

```text
dict_values(['Rahul', 40, 600000])
```

---

## Dry Run

```text
Dictionary

Rahul

40

600000

↓

values()
```

---

# 📖 3. `items()` Method

## ✅ Definition

Returns **both keys and values** as tuples.

---

## Syntax

```python
dictionary.items()
```

---

## Example

```python
print(student.items())
```

### Output

```text
dict_items([
('name','Rahul'),
('age',40),
('salary',600000)
])
```

---

## Memory Diagram

```text
Dictionary

name → Rahul

age → 40

salary → 600000

↓

items()

↓

(name,Rahul)

(age,40)

(salary,600000)
```

---

# 📖 4. Loop Through Dictionary

## Method 1 – Loop Through Keys

```python
student = {
    "name":"Rahul",
    "age":40,
    "salary":600000
}

for key in student:
    print(key)
```

Output

```text
name
age
salary
```

---

# 📖 Method 2 – Loop Through Values

```python
for value in student.values():
    print(value)
```

Output

```text
Rahul
40
600000
```

---

# 📖 Method 3 – Loop Through Keys and Values

Most commonly used in interviews.

```python
for key, value in student.items():
    print(key, ":", value)
```

Output

```text
name : Rahul
age : 40
salary : 600000
```

---

## Dry Run

```text
items()

↓

(name,Rahul)

↓

key=name

value=Rahul

↓

Print
```

---

# 📖 Dictionary with `if` Condition

## Example

```python
student = {
    "name":"A",
    "marks":90
}

if student["marks"] >= 90:
    print("Excellent")
```

Output

```text
Excellent
```

---

## Example – Grade System

```python
student = {
    "name":"Rahul",
    "marks":82
}

if student["marks"] >= 90:
    print("Grade A")

elif student["marks"] >= 75:
    print("Grade B")

else:
    print("Grade C")
```

Output

```text
Grade B
```

---

# 📖 Check if a Key Exists

## Using `in`

```python
student = {
    "name":"Rahul",
    "marks":90
}

if "name" in student:
    print("Key Found")

else:
    print("Key Not Found")
```

Output

```text
Key Found
```

---

## Key Not Found

```python
if "salary" in student:
    print("Found")

else:
    print("Not Found")
```

Output

```text
Not Found
```

---

# 📖 Membership Operators

| Operator | Purpose                            |
| -------- | ---------------------------------- |
| `in`     | Check whether a key exists         |
| `not in` | Check whether a key does not exist |

---

Example

```python
print("name" in student)

print("city" not in student)
```

Output

```text
True

True
```

---

# 📊 `keys()` vs `values()` vs `items()`

| Method     | Returns         |
| ---------- | --------------- |
| `keys()`   | All keys        |
| `values()` | All values      |
| `items()`  | Key-value pairs |

---

# 🌍 Real-Life Example

Employee Record

```python
employee = {
    "id":101,
    "name":"Ajay",
    "salary":50000
}

for key, value in employee.items():
    print(key, value)
```

Output

```text
id 101

name Ajay

salary 50000
```

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using `values()` when keys are needed.

Wrong

```python
for key in student.values():
```

Correct

```python
for key in student.keys():
```

---

## ❌ Mistake 2

Using only one variable with `items()`.

Wrong

```python
for item in student.items():
    print(item)
```

This works, but prints tuples.

Better

```python
for key, value in student.items():
    print(key, value)
```

---

## ❌ Mistake 3

Checking values with `in`.

```python
"Rahul" in student
```

This checks **keys**, not values.

Correct

```python
"Rahul" in student.values()
```

---

# 💡 Programmer Tips

Remember

```text
keys()

↓

All Keys
```

```text
values()

↓

All Values
```

```text
items()

↓

Key + Value
```

```text
for key,value

↓

Most Common Loop
```

```text
in

↓

Check Key
```

---

# 🎓 Interview Questions with Answers

### ❓1. What does `keys()` return?

✅ **Answer:**

It returns all dictionary keys.

---

### ❓2. What does `values()` return?

✅ **Answer:**

It returns all dictionary values.

---

### ❓3. What does `items()` return?

✅ **Answer:**

It returns key-value pairs as tuples.

---

### ❓4. Which is the best way to iterate through both keys and values?

✅ **Answer:**

```python
for key, value in dictionary.items():
    print(key, value)
```

---

### ❓5. How do you check whether a key exists?

✅ **Answer:**

```python
if "name" in student:
    print("Found")
```

---

### ❓6. Does `"Rahul" in student` check keys or values?

✅ **Answer:**

It checks **keys**, not values.

To check values:

```python
"Rahul" in student.values()
```

---

# ⭐ MCQs

### Q1. Which method returns all keys?

A. `items()`

B. `keys()`

C. `values()`

D. `get()`

✅ **Answer:** **B**

---

### Q2. Which method returns key-value pairs?

A. `keys()`

B. `values()`

C. `items()`

D. `pairs()`

✅ **Answer:** **C**

---

### Q3. Which statement checks whether `"age"` is a key?

```python
"A. "age" in student
B. "age" in student.values()
C. student.keys("age")
D. student.items("age")
```

✅ **Answer:** **A**

---

### Q4. Which loop is most commonly used?

```python
A. for key in d

B. for value in d.values()

C. for key, value in d.items()

D. All of the above
```

✅ **Answer:** **D**

---

# 📝 Practice Programs

## ⭐ Easy

### Print All Keys

```python
student = {
    "name":"Ramesh",
    "age":24,
    "city":"Hyderabad"
}

print(student.keys())
```

---

### Print All Values

```python
print(student.values())
```

---

## ⭐⭐ Medium

### Print Keys and Values

```python
for key, value in student.items():
    print(key, ":", value)
```

---

## ⭐⭐⭐ Challenge

```python
employee = {
    "id":101,
    "name":"Ajay",
    "salary":50000,
    "city":"Hyderabad"
}

# 1. Print all keys
# 2. Print all values
# 3. Print key:value pairs
# 4. Check if "salary" exists
# 5. Check if "email" exists
```

### Answer

```python
employee = {
    "id":101,
    "name":"Ajay",
    "salary":50000,
    "city":"Hyderabad"
}

print(employee.keys())

print(employee.values())

for key, value in employee.items():
    print(key, ":", value)

print("salary" in employee)

print("email" in employee)
```

---

# 📌 Chapter Summary

```text
           DICTIONARY TRAVERSAL
                  │
      ┌───────────┼────────────┐
      │           │            │
    keys()     values()     items()
      │           │            │
   All Keys   All Values   Key-Value Pairs
                  │
           for key, value
                  │
            Membership (in)
```

---

# 🏆 Congratulations!

You have completed **Python Dictionary – Chapter 3: `keys()`, `values()`, `items()`, Looping & Dictionary Conditions**.

### ✅ You learned:

* `keys()`
* `values()`
* `items()`
* Looping through dictionaries
* Membership operators (`in`, `not in`)
* Using `if` with dictionaries
* Interview questions
* MCQs
* Practice programs

---

# 📖 Next Chapter

## **Chapter 4 – `setdefault()`, Nested Dictionaries, Dictionary of Lists & List of Dictionaries**

We'll cover:

```python
student.setdefault("grade", "A")

products = {
    101: {
        "name": "Rahul",
        "price": 900
    }
}

employee = {
    "names": ["A", "B", "C"]
}

employees = [
    {"id":101, "name":"Rahul"},
    {"id":102, "name":"Ajay"}
]
```

This chapter introduces **advanced dictionary structures** used in real-world Python projects, APIs, JSON, databases, and interview questions.
---
# 📘 Python Dictionary Master Handbook

# 📖 Chapter 4 – `setdefault()`, Nested Dictionaries, Dictionary of Lists & List of Dictionaries (Beginner to Interview Level)

> ⭐ This chapter covers **advanced Dictionary concepts** that are used in **real-world Python projects**, **JSON APIs**, **Django/Flask**, **Data Science**, and **interviews**.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Use `setdefault()`
* ✅ Understand Nested Dictionaries
* ✅ Understand Dictionary of Lists
* ✅ Understand List of Dictionaries
* ✅ Access nested data
* ✅ Solve interview questions

---

# 📖 1. `setdefault()` Method

## ✅ Definition

The `setdefault()` method:

* Checks whether a key exists.
* If the key exists → returns its value.
* If the key doesn't exist → adds the key with a default value.

---

## Syntax

```python
dictionary.setdefault(key, default_value)
```

---

## Example 1

```python
student = {
    "name": "Rahul",
    "marks": 90
}

student.setdefault("grade", "A")

print(student)
```

### Output

```text
{
'name':'Rahul',
'marks':90,
'grade':'A'
}
```

---

## Dry Run

```text
Dictionary

name

marks

↓

setdefault("grade","A")

↓

grade added

↓

name

marks

grade
```

---

## Example 2

Key Already Exists

```python
student = {
    "name": "Rahul"
}

student.setdefault("name", "Ajay")

print(student)
```

Output

```text
{'name':'Rahul'}
```

Nothing changes.

---

# 📊 Assignment vs setdefault()

| Assignment       | setdefault()                      |
| ---------------- | --------------------------------- |
| Always updates   | Only adds if missing              |
| Overwrites value | Does not overwrite existing value |

---

Example

```python
student["grade"] = "B"
```

Always updates.

```python
student.setdefault("grade","A")
```

Adds only if `"grade"` doesn't exist.

---

# 🌍 Real-Life Example

```python
employee = {
    "id":101,
    "name":"Ajay"
}

employee.setdefault("department","IT")

print(employee)
```

Output

```text
{
'id':101,
'name':'Ajay',
'department':'IT'
}
```

---

# 📖 2. Nested Dictionary

## ✅ Definition

A Dictionary inside another Dictionary.

---

## Syntax

```python
{
 key:{
      key:value
    }
}
```

---

## Example

```python
products = {

    101:{
        "name":"Rahul",
        "product":"ABC",
        "price":900
    },

    102:{
        "name":"Ajay",
        "product":"XYZ",
        "price":6000
    }

}
```

---

# Access Nested Values

```python
print(products[101]["price"])

print(products[102]["name"])
```

Output

```text
900

Ajay
```

---

## Memory Diagram

```text
products

│

├──101

│    │

│    ├──name

│    ├──product

│    └──price

│

└──102

     │

     ├──name

     ├──product

     └──price
```

---

# 🌍 Real-Life Example

Student Database

```python
students = {

    1:{
        "name":"Ramesh",
        "marks":95
    },

    2:{
        "name":"Ajay",
        "marks":80
    }

}

print(students[1]["marks"])
```

Output

```text
95
```

---

# 📖 3. Dictionary of Lists

## ✅ Definition

A Dictionary where values are Lists.

---

## Example

```python
employee = {

    "names":["A","B","C"],

    "salary":[1000,2000,3000]

}

print(employee)
```

---

Output

```text
{
'names':['A','B','C'],
'salary':[1000,2000,3000]
}
```

---

## Access List

```python
print(employee["names"])
```

Output

```text
['A','B','C']
```

---

## Access Individual Element

```python
print(employee["names"][1])
```

Output

```text
B
```

---

## Memory Diagram

```text
Dictionary

names

↓

List

A

B

C
```

---

# 🌍 Real-Life Example

```python
student = {

    "subjects":[
        "Python",
        "SQL",
        "Java"
    ]

}

print(student["subjects"][0])
```

Output

```text
Python
```

---

# 📖 4. List of Dictionaries

## ✅ Definition

A List containing multiple Dictionaries.

---

## Example

```python
employees = [

    {"id":101,"name":"Rahul"},

    {"id":102,"name":"Ajay"},

    {"id":103,"name":"Annu"}

]

print(employees)
```

---

Output

```text
[
 {'id':101,'name':'Rahul'},

 {'id':102,'name':'Ajay'},

 {'id':103,'name':'Annu'}
]
```

---

# Access Dictionary

```python
print(employees[0])
```

Output

```text
{'id':101,'name':'Rahul'}
```

---

# Access Value

```python
print(employees[0]["id"])

print(employees[2]["name"])
```

Output

```text
101

Annu
```

---

## Memory Diagram

```text
List

↓

Dictionary

↓

Key

↓

Value
```

---

# 🌍 Real-Life Example

Shopping Cart

```python
cart = [

    {"item":"Laptop","price":900},

    {"item":"Mouse","price":50}

]

print(cart[1]["item"])
```

Output

```text
Mouse
```

---

# 📊 Nested Dictionary vs Dictionary of Lists vs List of Dictionaries

| Type                 | Structure   | Example             |
| -------------------- | ----------- | ------------------- |
| Nested Dictionary    | Dict → Dict | Student database    |
| Dictionary of Lists  | Dict → List | Subjects, Salaries  |
| List of Dictionaries | List → Dict | Employees, Products |

---

# 🌍 Real-World Applications

These structures are used in:

* 🌐 REST APIs
* 📦 JSON responses
* 🗄️ Database records
* 🛒 E-commerce products
* 👨‍🎓 Student management systems
* 💼 Employee management systems
* 📱 Mobile applications

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using assignment instead of `setdefault()`.

```python
student["grade"]="A"
```

Always overwrites.

---

## ❌ Mistake 2

Wrong nested access.

Wrong

```python
products["price"]
```

Correct

```python
products[101]["price"]
```

---

## ❌ Mistake 3

Confusing Dictionary of Lists with List of Dictionaries.

Remember

```text
Dictionary

↓

List
```

is different from

```text
List

↓

Dictionary
```

---

# 💡 Programmer Tips

Remember

```text
setdefault()

↓

Add Only If Missing
```

```text
Nested Dictionary

↓

Dictionary Inside Dictionary
```

```text
Dictionary of Lists

↓

Key → List
```

```text
List of Dictionaries

↓

List → Dictionary
```

---

# 🎓 Interview Questions with Answers

### ❓1. What does `setdefault()` do?

✅ **Answer:**

It adds a key with a default value only if the key doesn't already exist.

---

### ❓2. Does `setdefault()` overwrite existing values?

✅ **Answer:**

No.

---

### ❓3. What is a Nested Dictionary?

✅ **Answer:**

A Dictionary inside another Dictionary.

---

### ❓4. What is a Dictionary of Lists?

✅ **Answer:**

A Dictionary whose values are Lists.

---

### ❓5. What is a List of Dictionaries?

✅ **Answer:**

A List containing multiple Dictionary objects.

---

### ❓6. Which structure is commonly used for JSON?

✅ **Answer:**

Nested Dictionaries and Lists of Dictionaries.

---

# ⭐ MCQs

### Q1

Which method adds a key only if missing?

A. `update()`

B. `setdefault()`

C. `append()`

D. `insert()`

✅ **Answer:** **B**

---

### Q2

Which is a Nested Dictionary?

A.

```python
{"A":[1,2]}
```

B.

```python
{"A":{"age":20}}
```

C.

```python
[{"A":1}]
```

D.

```python
(1,2)
```

✅ **Answer:** **B**

---

### Q3

Which is a List of Dictionaries?

A.

```python
{"names":["A","B"]}
```

B.

```python
[
 {"id":1},

 {"id":2}
]
```

C.

```python
{"A":{"B":2}}
```

D.

```python
{1,2,3}
```

✅ **Answer:** **B**

---

### Q4

How do you access `"price"`?

```python
products = {
    101:{
        "price":900
    }
}
```

A.

```python
products["price"]
```

B.

```python
products[101]["price"]
```

C.

```python
products.price
```

D.

```python
products["101"]
```

✅ **Answer:** **B**

---

# 📝 Practice Programs

## ⭐ Easy

### Add Grade

```python
student = {
    "name":"Ramesh"
}

student.setdefault("grade","A")

print(student)
```

---

## ⭐⭐ Medium

### Nested Dictionary

```python
students = {

    1:{
        "name":"Rahul",
        "marks":90
    }

}

print(students[1]["marks"])
```

---

## ⭐⭐⭐ Challenge

```python
employees = [

    {"id":101,"name":"Ajay","salary":50000},

    {"id":102,"name":"Rahul","salary":60000}

]

# Print all employee names

for employee in employees:
    print(employee["name"])
```

---

# 📌 Chapter Summary

```text
           ADVANCED DICTIONARIES
                  │
      ┌───────────┼────────────┐
      │           │            │
 setdefault()  Nested Dict   Dict of Lists
      │           │            │
 Add If      Dict → Dict   Key → List
 Missing
                  │
          List of Dictionaries
                  │
             List → Dict
```

---

# 🏆 Congratulations!

You have completed **Python Dictionary – Chapter 4: `setdefault()`, Nested Dictionaries, Dictionary of Lists & List of Dictionaries**.

### ✅ You learned:

* `setdefault()`
* Nested Dictionaries
* Dictionary of Lists
* List of Dictionaries
* Accessing nested data
* Interview questions
* MCQs
* Practice programs

---

# 📖 Next Chapter

## **Chapter 5 – Dictionary Comprehension & Final Revision**

We'll cover:

```python
result = {
    ch: ch.upper()
    for ch in "apple"
}

numbers = {
    i: "Even" if i % 2 == 0 else "Odd"
    for i in range(1, 6)
}
```

This final chapter will include:

* ✅ Dictionary comprehension
* ✅ Comprehension with `if`
* ✅ Comprehension with `if-else`
* ✅ Top 30 interview questions
* ✅ One-page cheat sheet
* ✅ Final revision for interviews
---
# 📘 Python Dictionary Master Handbook

# 📖 Chapter 5 – Dictionary Comprehension & Final Revision (Beginner to Interview Level)

> ⭐ Dictionary Comprehension is a short and powerful way to create dictionaries. It is frequently asked in **Python interviews**, **coding tests**, **Data Science**, and **automation**.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand Dictionary Comprehension
* ✅ Create dictionaries dynamically
* ✅ Use `if` condition
* ✅ Use `if-else`
* ✅ Solve interview questions
* ✅ Revise the complete Dictionary topic

---

# 📖 What is Dictionary Comprehension?

## ✅ Definition

Dictionary Comprehension is a **short and efficient way** to create dictionaries using loops and conditions.

It is similar to **List Comprehension**, but it creates a **Dictionary**.

---

## Syntax

```python
{
    key_expression: value_expression
    for variable in iterable
}
```

---

# 📖 Example 1 – Convert Characters to Uppercase

```python
result = {
    ch: ch.upper()
    for ch in "apple"
}

print(result)
```

### Output

```text
{'a': 'A', 'p': 'P', 'l': 'L', 'e': 'E'}
```

---

## Dry Run

```
"apple"

↓

a → A

p → P

p → P

l → L

e → E

↓

Dictionary

{
'a':'A',
'p':'P',
'l':'L',
'e':'E'
}
```

> **Note:** Duplicate keys are overwritten, so `"p"` appears only once.

---

# 📖 Example 2 – Squares

```python
numbers = {
    i: i*i
    for i in range(1,6)
}

print(numbers)
```

### Output

```text
{
1:1,
2:4,
3:9,
4:16,
5:25
}
```

---

# 📖 Dictionary Comprehension with `if`

## Syntax

```python
{
    key:value
    for variable in iterable
    if condition
}
```

---

## Example

```python
result = {
    ch: ch.upper()
    for ch in "apple"
    if ch.upper() == "P"
}

print(result)
```

### Output

```text
{'p':'P'}
```

---

## Example – Even Numbers

```python
even = {
    i:i
    for i in range(1,11)
    if i%2==0
}

print(even)
```

### Output

```text
{
2:2,
4:4,
6:6,
8:8,
10:10
}
```

---

# 📖 Dictionary Comprehension with `if-else`

## Syntax

```python
{
    key:
    value_if_true
    if condition
    else value_if_false

    for variable in iterable
}
```

---

## Example

```python
numbers = {
    i: "Even" if i%2==0 else "Odd"
    for i in range(1,6)
}

print(numbers)
```

### Output

```text
{
1:'Odd',
2:'Even',
3:'Odd',
4:'Even',
5:'Odd'
}
```

---

## Dry Run

```
1 → Odd

2 → Even

3 → Odd

4 → Even

5 → Odd

↓

Dictionary Created
```

---

# 📖 More Examples

## Example – Square & Cube

```python
result = {
    i:(i*i,i*i*i)
    for i in range(1,6)
}

print(result)
```

### Output

```text
{
1:(1,1),
2:(4,8),
3:(9,27),
4:(16,64),
5:(25,125)
}
```

---

## Example – Student Grades

```python
marks = [95,82,76,65]

grades = {
    mark:
    "Pass" if mark>=35 else "Fail"
    for mark in marks
}

print(grades)
```

---

# 📊 Normal Loop vs Dictionary Comprehension

### Normal Loop

```python
result = {}

for i in range(1,6):
    result[i]=i*i
```

---

### Dictionary Comprehension

```python
result={
    i:i*i
    for i in range(1,6)
}
```

Both produce the same result.

---

# 🌍 Real-Life Applications

Dictionary Comprehension is used in:

* 📊 Student grade systems
* 💰 Salary calculations
* 🌐 API data transformation
* 📦 Product catalogs
* 📈 Reports and analytics
* 🤖 Automation scripts

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using `[]` instead of `{}`.

Wrong

```python
[
    x:x*x
]
```

Correct

```python
{
    x:x*x
}
```

---

## ❌ Mistake 2

Using duplicate keys.

```python
{
    ch:ch.upper()
    for ch in "apple"
}
```

The second `"p"` overwrites the first `"p"`.

---

## ❌ Mistake 3

Forgetting the colon (`:`).

Wrong

```python
{
x*x
for x in range(5)
}
```

Correct

```python
{
x:x*x
for x in range(5)
}
```

---

# 💡 Programmer Tips

Remember

```
Dictionary

↓

{ key:value }
```

```
Comprehension

↓

Short Loop
```

```
if

↓

Filter
```

```
if-else

↓

Decision
```

---

# 🎓 Interview Questions with Answers

### ❓1. What is Dictionary Comprehension?

✅ **Answer:**

It is a concise way to create dictionaries using loops and conditions.

---

### ❓2. What symbols are used?

✅ **Answer:**

Curly braces `{}`.

---

### ❓3. Can Dictionary Comprehension use `if`?

✅ **Answer:**

Yes.

---

### ❓4. Can Dictionary Comprehension use `if-else`?

✅ **Answer:**

Yes.

---

### ❓5. What happens if duplicate keys are generated?

✅ **Answer:**

The last value overwrites the previous one.

---

# ⭐ MCQs

### Q1

Which brackets are used in Dictionary Comprehension?

A. `[]`

B. `()`

C. `{}`

D. `<>`

✅ **Answer:** **C**

---

### Q2

Which statement is correct?

A. Dictionary Comprehension creates a List.

B. Dictionary Comprehension creates a Dictionary.

C. It creates a Tuple.

D. It creates a Set.

✅ **Answer:** **B**

---

### Q3

Can Dictionary Comprehension use `if`?

A. No

B. Yes

✅ **Answer:** **B**

---

### Q4

Duplicate keys in a Dictionary:

A. Cause an error

B. Keep all values

C. Overwrite the previous value

D. Are ignored completely

✅ **Answer:** **C**

---

# 📝 Practice Programs

## ⭐ Easy

### Squares

```python
result = {
    i:i*i
    for i in range(1,6)
}

print(result)
```

---

## ⭐⭐ Medium

### Even/Odd

```python
numbers = {
    i:"Even" if i%2==0 else "Odd"
    for i in range(1,11)
}

print(numbers)
```

---

## ⭐⭐⭐ Challenge

Create a dictionary where:

* Keys = numbers from **1 to 10**
* Values = `"Pass"` if the number is **5 or greater**, otherwise `"Fail"`

### Answer

```python
result = {
    i: "Pass" if i >= 5 else "Fail"
    for i in range(1,11)
}

print(result)
```

---

# 📘 Final Dictionary Revision (Interview Cheat Sheet)

## 📌 Dictionary Properties

| Feature          | Dictionary          |
| ---------------- | ------------------- |
| Ordered          | ✅ Yes (Python 3.7+) |
| Mutable          | ✅ Yes               |
| Duplicate Keys   | ❌ No                |
| Duplicate Values | ✅ Yes               |
| Indexing         | ❌ No                |
| Key-Value Pairs  | ✅ Yes               |

---

## 📌 Important Methods

| Method         | Purpose            |
| -------------- | ------------------ |
| `get()`        | Safe access        |
| `keys()`       | All keys           |
| `values()`     | All values         |
| `items()`      | Key-value pairs    |
| `pop()`        | Remove by key      |
| `popitem()`    | Remove last item   |
| `setdefault()` | Add key if missing |
| `clear()`      | Remove all items   |

---

## 📌 Important Concepts

* ✅ Dictionary stores **key-value pairs**
* ✅ Keys must be **unique**
* ✅ Values can be duplicated
* ✅ Access values using **keys**
* ✅ Supports nested dictionaries
* ✅ Supports dictionary comprehension

---

## 📌 Dictionary Structures

```
Dictionary
      │
 ┌────┼────┐
 │    │    │
Simple Nested Dict of Lists
            │
            └── List of Dictionaries
```

---

# 🎯 Top 20 Interview Questions

1. What is a Dictionary?
2. Why are keys unique?
3. Can values be duplicated?
4. Difference between `get()` and `[]`?
5. Difference between `pop()` and `del`?
6. Difference between `pop()` and `popitem()`?
7. What does `clear()` do?
8. What is `setdefault()`?
9. Difference between `keys()`, `values()`, and `items()`?
10. How do you loop through a Dictionary?
11. How do you check whether a key exists?
12. What is a Nested Dictionary?
13. What is a Dictionary of Lists?
14. What is a List of Dictionaries?
15. What is Dictionary Comprehension?
16. Can Dictionary Comprehension use `if`?
17. Can Dictionary Comprehension use `if-else`?
18. Can Dictionary keys be mutable?
19. Why are Dictionaries used in JSON?
20. Difference between List, Tuple, Set, and Dictionary?

---

# 🧠 One-Page Memory Map

```text
                 PYTHON DICTIONARY
                        │
        ┌───────────────┼───────────────┐
        │               │               │
    Key-Value       Mutable        Ordered
       Pairs                          │
        │                             │
   Unique Keys                 No Indexing
        │
 ┌──────┼──────────────┐
 │      │              │
Access Modify        Remove
 │      │              │
[]    Add/Update     pop()
get()               popitem()
                    del
                    clear()
        │
 ┌──────┼──────────────┐
 │      │              │
keys() values()     items()
        │
Nested Dictionary
Dictionary of Lists
List of Dictionaries
        │
Dictionary Comprehension
```

---

# 🏆 Congratulations!

You have successfully completed the **Python Dictionary Master Handbook**.

## ✅ Topics Covered

* ✔ Introduction to Dictionary
* ✔ Creating Dictionaries
* ✔ Accessing values
* ✔ `get()`
* ✔ Adding & Updating
* ✔ `pop()`, `popitem()`, `del`, `clear()`
* ✔ `keys()`, `values()`, `items()`
* ✔ Looping through Dictionaries
* ✔ Membership testing
* ✔ `setdefault()`
* ✔ Nested Dictionary
* ✔ Dictionary of Lists
* ✔ List of Dictionaries
* ✔ Dictionary Comprehension
* ✔ Interview Questions
* ✔ MCQs
* ✔ Practice Programs
* ✔ Final Revision & Cheat Sheet

🎉 **You now have interview-ready notes for:**

* ✅ Functions
* ✅ While Loops
* ✅ Lists
* ✅ Strings
* ✅ Sets
* ✅ Tuples
* ✅ Lambda Functions
* ✅ Dictionaries

These topics form a strong foundation for Python interviews, coding tests, automation, web development, and data science.
