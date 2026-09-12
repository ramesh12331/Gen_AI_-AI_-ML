# 🐍 Python Variables & Data Types – Complete Notes

---

# 📌 1. Variable

## 📖 Definition

A **Variable** is a container that stores data. It allows us to store, access, and modify values in a Python program.

✅ A variable helps us use the same value multiple times without writing it again.

---

## ✍️ Syntax

```python
variable_name = value
```

### 📌 Explanation

* 🏷️ **variable_name** → Name of the variable.
* 🟰 **=** → Assignment operator.
* 📦 **value** → Data stored inside the variable.

---

## 💻 Example

```python
name = "Ramesh"
age = 25
salary = 35000.50
is_employee = True

print(name)
print(age)
print(salary)
print(is_employee)
```

### 📤 Output

```
Ramesh
25
35000.5
True
```

---

# 📌 Variable Naming Rules

### ✅ Valid Rules

✔ Use letters, numbers and underscore (_)

✔ Cannot start with a number

✔ No spaces allowed

✔ Cannot use Python keywords

✔ Variable names are case-sensitive

---

### ✅ Valid Examples

```python
company_name = "ABC Pvt Ltd"
employee_name = "Ramesh"
employee_salary = 45000
is_account_suspended = False
```

---

### ❌ Invalid Examples

```python
2name = "Ramesh"
employee name = "Ramesh"
class = "Python"
```

---

# 🐍 Snake Case

Python follows **Snake Case** naming convention.

### Rules

🔹 All letters should be lowercase.

🔹 Separate words using an underscore (_).

### ✅ Examples

```python
company_name
employee_salary
employee_phone
is_account_suspended
total_marks
```

---

# 📌 2. Data Types

## 📖 Definition

A **Data Type** defines the type of data stored inside a variable.

Python has two categories of data types.

### 🔹 Simple Data Types

* 🔤 String
* 🔢 Integer
* 💰 Float
* ✅ Boolean

### 🔹 Complex Data Types

* 📋 List
* 📦 Tuple
* 📖 Dictionary
* 🎯 Set

---

# 🔤 String (str)

## 📖 Definition

A **String** is a collection of characters enclosed in single (' '), double (" "), or triple quotes.

### ✍️ Syntax

```python
name = "Ramesh"
```

### 💻 Example

```python
name = "Ramesh"

print(name)
print(type(name))
```

### 📤 Output

```
Ramesh
<class 'str'>
```

---

# 🔢 Integer (int)

## 📖 Definition

An **Integer** is a whole number without decimal values.

### ✍️ Syntax

```python
age = 25
```

### 💻 Example

```python
age = 25

print(age)
print(type(age))
```

### 📤 Output

```
25
<class 'int'>
```

---

# 💰 Float (float)

## 📖 Definition

A **Float** is a number containing a decimal point.

### ✍️ Syntax

```python
salary = 45000.75
```

### 💻 Example

```python
salary = 45000.75

print(salary)
```

### 📤 Output

```
45000.75
```

---

# ✅ Boolean (bool)

## 📖 Definition

A **Boolean** stores only two values.

✔ True

✔ False

### 💻 Example

```python
is_employee = True
```

---

# 📋 List

## 📖 Definition

A **List** is an ordered and mutable collection of items.

### ⭐ Features

✔ Ordered

✔ Mutable

✔ Allows duplicate values

### ✍️ Syntax

```python
employees = ["Ramesh", "Suresh", "Priya"]
```

### 📌 Access

```python
employees[0]
```

### ✏️ Update

```python
employees[1] = "Kiran"
```

---

# 📖 Dictionary

## 📖 Definition

A **Dictionary** is a mutable collection of key-value pairs.

### ⭐ Features

✔ Key-Value Pair

✔ Mutable

✔ Keys must be unique

### ✍️ Syntax

```python
employee = {
    "id":101,
    "name":"Ramesh",
    "salary":35000
}
```

### 📌 Access

```python
employee["name"]
```

### ✏️ Update

```python
employee["salary"] = 40000
```

---

# 📝 Practice Task

## 🎯 Create 5 Simple Variables

```python
employee_name = "Ramesh"
employee_age = 25
employee_salary = 45000.50
is_active = True
department = "IT"
```

---

## 🎯 Create 5 Complex Variables

```python
employee_ids = [101,102,103]

departments = ["IT","HR","Finance"]

salary_list = [30000,40000,50000]

employee = {
    "id":101,
    "name":"Ramesh"
}

company = {
    "name":"ABC Pvt Ltd",
    "location":"Hyderabad"
}
```

---

# 📚 Final Summary

## ✅ Variable

📦 Stores data.

---

## ✅ Data Types

🔤 String → Text

🔢 Integer → Whole Number

💰 Float → Decimal Number

✅ Boolean → True / False

📋 List → Ordered collection

📖 Dictionary → Key-Value pairs

---

# 🎯 Interview Questions & Answers

## ❓1. What is a variable?

✅ **Answer:**

A variable is a container used to store data in Python.

---

## ❓2. Why do we use variables?

✅ **Answer:**

Variables help us store, access, and modify data easily.

---

## ❓3. What is the syntax of a variable?

```python
variable_name = value
```

---

## ❓4. What is Snake Case?

✅ **Answer:**

Snake Case is a naming style where all letters are lowercase and words are separated using underscores.

**Example:**

```python
employee_name
company_name
```

---

## ❓5. What is a data type?

✅ **Answer:**

A data type defines the type of value stored in a variable.

---

## ❓6. Name the simple data types.

✅ **Answer:**

* 🔤 String
* 🔢 Integer
* 💰 Float
* ✅ Boolean

---

## ❓7. Name the complex data types.

✅ **Answer:**

* 📋 List
* 📦 Tuple
* 📖 Dictionary
* 🎯 Set

---

## ❓8. What is a list?

✅ **Answer:**

A list is an ordered, mutable collection that allows duplicate values.

---

## ❓9. What is a dictionary?

✅ **Answer:**

A dictionary stores data as key-value pairs.

---

## ❓10. Which data type is best for storing employee details?

✅ **Answer:**

A **Dictionary** is the best choice because it stores employee details as **key-value pairs**, such as Employee ID, Name, Department, Salary, Email, and Phone Number.

---

# 🌟 Quick Revision

📦 Variable → Stores Data

🔤 String → Text

🔢 Integer → Whole Number

💰 Float → Decimal Number

✅ Boolean → True / False

📋 List → Ordered Collection

📖 Dictionary → Key-Value Collection

🐍 Snake Case → Lowercase words separated by `_`
