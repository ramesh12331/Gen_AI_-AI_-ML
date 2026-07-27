# 📘 Python Dictionary – Final Revision & Interview Summary

## 🎯 Beginner to Interview Level (One-Shot Revision)

> **Goal:** Revise the complete Dictionary topic in **15–20 minutes** before an interview.

---

# 📚 1. What is a Dictionary?

## ✅ Definition

A **Dictionary** is a **mutable collection of key-value pairs**.

* Each key is unique.
* Values can be duplicated.
* Access data using keys.
* Written using curly braces `{}`.

### Syntax

```python
student = {
    "name": "Ramesh",
    "age": 24,
    "city": "Hyderabad"
}
```

---

# 📚 2. Dictionary Characteristics

| Feature               | Dictionary |
| --------------------- | ---------- |
| Ordered (Python 3.7+) | ✅ Yes      |
| Mutable               | ✅ Yes      |
| Duplicate Keys        | ❌ No       |
| Duplicate Values      | ✅ Yes      |
| Indexing              | ❌ No       |
| Slicing               | ❌ No       |
| Key-Value Pairs       | ✅ Yes      |

---

# 📚 3. Creating a Dictionary

```python
student = {
    "name": "Ramesh",
    "age": 24,
    "city": "Hyderabad"
}
```

---

# 📚 4. Accessing Values

### Using `[]`

```python
print(student["name"])
```

✔ Raises **KeyError** if key is missing.

---

### Using `get()`

```python
print(student.get("name"))
print(student.get("salary"))
```

Output

```text
Ramesh
None
```

✔ Safe method (no error if key is missing).

---

# 📚 5. Adding New Items

```python
student["city"] = "Hyderabad"
```

Output

```python
{
'name':'Ramesh',
'age':24,
'city':'Hyderabad'
}
```

---

# 📚 6. Updating Existing Items

```python
student["name"] = "Ajay"
```

Output

```python
{
'name':'Ajay',
'age':24
}
```

---

# 📚 7. Removing Items

### `pop()`

```python
student.pop("age")
```

Removes a specific key.

---

### `popitem()`

```python
student.popitem()
```

Removes the **last inserted** key-value pair.

---

### `del`

```python
del student["city"]
```

Deletes a specific key.

---

### `clear()`

```python
student.clear()
```

Removes all items.

---

# 📚 8. Dictionary Methods

## `keys()`

```python
student.keys()
```

Returns all keys.

---

## `values()`

```python
student.values()
```

Returns all values.

---

## `items()`

```python
student.items()
```

Returns key-value pairs.

---

# 📚 9. Looping Through Dictionary

### Loop through Keys

```python
for key in student:
    print(key)
```

---

### Loop through Values

```python
for value in student.values():
    print(value)
```

---

### Loop through Keys & Values

```python
for key, value in student.items():
    print(key, value)
```

⭐ Most commonly used in interviews.

---

# 📚 10. Membership Operators

### Check if Key Exists

```python
"name" in student
```

Returns

```text
True
```

---

### Check if Key Doesn't Exist

```python
"salary" not in student
```

---

# 📚 11. `setdefault()`

Adds a key only if it doesn't exist.

```python
student.setdefault("grade", "A")
```

If `"grade"` already exists, nothing changes.

---

# 📚 12. Nested Dictionary

```python
students = {

    101: {
        "name": "Ramesh",
        "marks": 90
    },

    102: {
        "name": "Ajay",
        "marks": 80
    }

}
```

Access

```python
print(students[101]["marks"])
```

---

# 📚 13. Dictionary of Lists

```python
employee = {
    "names": ["A", "B", "C"],
    "salary": [1000, 2000, 3000]
}
```

Access

```python
print(employee["names"][0])
```

---

# 📚 14. List of Dictionaries

```python
employees = [

    {"id":101, "name":"Ramesh"},

    {"id":102, "name":"Ajay"}

]
```

Access

```python
print(employees[0]["name"])
```

---

# 📚 15. Dictionary Comprehension

### Syntax

```python
{
    key:value
    for variable in iterable
}
```

---

### Example

```python
result = {
    i: i*i
    for i in range(1,6)
}

print(result)
```

Output

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

### With `if`

```python
result = {
    i:i
    for i in range(1,11)
    if i%2==0
}
```

---

### With `if-else`

```python
numbers = {
    i: "Even" if i%2==0 else "Odd"
    for i in range(1,6)
}
```

---

# 📚 16. Dictionary vs Other Collections

| Feature    | List | Tuple | Set        | Dictionary  |
| ---------- | ---- | ----- | ---------- | ----------- |
| Ordered    | ✅    | ✅     | ❌          | ✅           |
| Mutable    | ✅    | ❌     | ✅          | ✅           |
| Duplicates | ✅    | ✅     | ❌ (values) | Values Only |
| Indexing   | ✅    | ✅     | ❌          | ❌           |
| Key-Value  | ❌    | ❌     | ❌          | ✅           |

---

# 📚 17. Important Dictionary Methods

| Method         | Purpose                 |
| -------------- | ----------------------- |
| `get()`        | Safe access             |
| `keys()`       | Returns keys            |
| `values()`     | Returns values          |
| `items()`      | Returns key-value pairs |
| `pop()`        | Remove by key           |
| `popitem()`    | Remove last item        |
| `setdefault()` | Add key if missing      |
| `clear()`      | Remove all items        |

---

# 📚 18. Common Beginner Mistakes

### ❌ Using Indexing

```python
student[0]
```

✔ Dictionaries use **keys**, not indexes.

---

### ❌ Duplicate Keys

```python
{
"name":"A",
"name":"B"
}
```

Only `"B"` is stored.

---

### ❌ Using `[]` for Missing Key

```python
student["salary"]
```

Raises `KeyError`.

Use

```python
student.get("salary")
```

---

### ❌ Forgetting `key:` in Dictionary Comprehension

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

# 📚 19. Real-Life Applications

* 👨 Student Management System
* 👨 Employee Database
* 🛒 E-Commerce Products
* 🌐 JSON Data from APIs
* 🏦 Banking Systems
* 📱 Mobile Contacts
* 📊 Reports & Analytics
* 🤖 Automation Scripts

---

# 🎓 Top 30 Interview Questions

### Basic

1. What is a Dictionary?
2. Why do we use Dictionaries?
3. Is Dictionary mutable?
4. Are Dictionaries ordered?
5. Can keys be duplicated?
6. Can values be duplicated?
7. Does Dictionary support indexing?

### Access

8. Difference between `[]` and `get()`.
9. What happens if a key doesn't exist?
10. Which method is safer?

### Methods

11. Explain `pop()`.
12. Explain `popitem()`.
13. Explain `clear()`.
14. Explain `setdefault()`.
15. Difference between `pop()` and `del`.
16. Difference between `pop()` and `popitem()`.

### Looping

17. Difference between `keys()`, `values()`, and `items()`.
18. How do you loop through a Dictionary?
19. How do you check if a key exists?

### Advanced

20. What is a Nested Dictionary?
21. What is a Dictionary of Lists?
22. What is a List of Dictionaries?
23. What is Dictionary Comprehension?
24. Can Dictionary Comprehension use `if`?
25. Can it use `if-else`?

### Comparison

26. Difference between Dictionary and List.
27. Difference between Dictionary and Tuple.
28. Difference between Dictionary and Set.
29. When should you use a Dictionary?
30. Why is Dictionary widely used in JSON?

---

# 🧠 Memory Tricks

```text
Dictionary
     │
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

Duplicates Allowed
```

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
pop()

↓

Remove by Key
```

```text
popitem()

↓

Remove Last Item
```

```text
setdefault()

↓

Add If Missing
```

```text
Nested Dictionary

↓

Dictionary → Dictionary
```

```text
Dictionary of Lists

↓

Dictionary → List
```

```text
List of Dictionaries

↓

List → Dictionary
```

```text
Dictionary Comprehension

↓

Short Way to Create Dictionaries
```

---

# 🧠 One-Page Mind Map

```text
                    PYTHON DICTIONARY
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    Key-Value         Mutable          Ordered
      Pairs                              (3.7+)
        │
 ┌──────┼───────────────┐
 │      │               │
Access  Modify       Remove
 │      │               │
[]     Add/Update     pop()
get()                popitem()
                     del
                     clear()
        │
 ┌──────┼──────────────┐
 │      │              │
keys() values()     items()
        │
 ┌──────┼──────────────┐
 │      │              │
setdefault()   Nested Dictionary
               Dictionary of Lists
               List of Dictionaries
        │
Dictionary Comprehension
```

---

# 🎯 30-Second Interview Revision

```text
✓ Dictionary stores data as Key : Value pairs.
✓ Keys are unique; values can repeat.
✓ Dictionary is mutable.
✓ Uses {}.
✓ Access using keys, not indexes.
✓ get() is safer than [].
✓ keys(), values(), items() are used for traversal.
✓ pop() removes a specific key.
✓ popitem() removes the last inserted item.
✓ del deletes a key.
✓ clear() removes all items.
✓ setdefault() adds a key only if missing.
✓ Supports Nested Dictionaries.
✓ Supports Dictionary of Lists.
✓ Supports List of Dictionaries.
✓ Supports Dictionary Comprehension.
✓ Widely used for JSON, APIs, databases, and real-world applications.
```

---

# 🏆 Final Interview Tip

If an interviewer asks **"Explain Python Dictionary in 2 minutes"**, you can answer:

> **"A Dictionary is a mutable collection of key-value pairs. It stores data using unique keys and corresponding values. Dictionaries are ordered (from Python 3.7+), allow duplicate values but not duplicate keys, and values are accessed using keys instead of indexes. Common methods include `get()`, `keys()`, `values()`, `items()`, `pop()`, `popitem()`, `setdefault()`, and `clear()`. Dictionaries support nested structures and dictionary comprehension, making them ideal for representing JSON data, API responses, configuration settings, and database records."**

---

## 🎉 Congratulations!

You have now completed **interview-ready master notes** for:

* ✅ While Loops
* ✅ Functions
* ✅ Lists
* ✅ Strings
* ✅ Sets
* ✅ Tuples
* ✅ Lambda Functions
* ✅ Dictionaries

These topics provide a strong Python foundation for **interviews, coding tests, automation, web development (Django/Flask), and data science**.
