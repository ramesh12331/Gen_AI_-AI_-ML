# 📘 Python Strings – Final Revision & Interview Summary

## 🎯 Beginner to Interview Level (One-Shot Revision)

> **Goal:** Revise everything about Python Strings in **20–30 minutes** before an interview.

---

# 📚 1. What is a String?

## ✅ Definition

A **String** is a **sequence of characters** enclosed in:

* Single Quotes `' '`
* Double Quotes `" "`
* Triple Single Quotes `''' '''`
* Triple Double Quotes `""" """`

Example

```python
name = "Python"
```

---

## Features

* ✅ Ordered
* ✅ Immutable (Cannot Modify)
* ✅ Supports Indexing
* ✅ Supports Slicing
* ✅ Allows Duplicate Characters
* ✅ Iterable

---

# 📚 2. Creating Strings

```python
name = "Python"

city = 'Hyderabad'

message = """Welcome to Python"""

empty = ""
```

---

# 📚 3. String Properties

| Property   | String |
| ---------- | ------ |
| Ordered    | ✅      |
| Mutable    | ❌      |
| Duplicates | ✅      |
| Indexing   | ✅      |
| Slicing    | ✅      |
| Iterable   | ✅      |

---

# 📚 4. Indexing

Positive Index

```text
P  Y  T  H  O  N

0  1  2  3  4  5
```

```python
text[0]

text[3]
```

---

Negative Index

```text
-6 -5 -4 -3 -2 -1
```

```python
text[-1]

text[-2]
```

---

# 📚 5. Slicing

Syntax

```python
string[start:stop:step]
```

Examples

```python
text[:4]

text[2:]

text[1:5]

text[::2]

text[::-1]
```

Most Asked

```python
text[::-1]
```

Reverse String

---

# 📚 6. Loop Through String

Simple Loop

```python
for ch in text:
    print(ch)
```

Using Index

```python
for i in range(len(text)):
    print(i,text[i])
```

Alternate Characters

```python
for i in range(0,len(text),2):
    print(text[i])
```

---

# 📚 7. String Conditions

Membership

```python
"Py" in text

"Java" not in text
```

Email Validation

```python
if "@" in email:
    print("Valid")
```

---

# 📚 8. String Formatting

Method 1

```python
print("Hello",name)
```

Method 2

```python
print("Hello {}".format(name))
```

Method 3 ⭐

```python
print(f"Hello {name}")
```

**Interview Tip:** Prefer **f-strings** in modern Python.

---

# 📚 9. Case Conversion Methods

| Method       | Purpose                   |
| ------------ | ------------------------- |
| lower()      | Lowercase                 |
| upper()      | Uppercase                 |
| title()      | Every Word Capital        |
| capitalize() | Only First Letter Capital |
| swapcase()   | Reverse Case              |

Examples

```python
text.lower()

text.upper()

text.title()

text.capitalize()

text.swapcase()
```

---

# 📚 10. Space Removal Methods

| Method   | Purpose    |
| -------- | ---------- |
| strip()  | Both Sides |
| lstrip() | Left Side  |
| rstrip() | Right Side |

Example

```python
text.strip()
```

---

# 📚 11. Replace Method

```python
text.replace("a","A")

text.replace("a","A",2)
```

Used for

* Data Cleaning
* Search & Replace
* File Processing

---

# 📚 12. Split & Join

Split

```python
text.split()
```

Output

```text
List
```

Join

```python
",".join(list_data)
```

Output

```text
String
```

---

# 📚 13. Searching Methods

| Method       | Purpose                |
| ------------ | ---------------------- |
| find()       | Returns Index or -1    |
| index()      | Returns Index or Error |
| count()      | Count Occurrences      |
| startswith() | Beginning Check        |
| endswith()   | Ending Check           |

Examples

```python
text.find("Py")

text.index("P")

text.count("a")

text.startswith("Python")

text.endswith("ing")
```

---

# 📚 14. Validation Methods

| Method    | Checks            |
| --------- | ----------------- |
| isdigit() | Digits            |
| isalpha() | Letters           |
| isalnum() | Letters + Numbers |
| islower() | Lowercase         |
| isupper() | Uppercase         |
| isspace() | Spaces            |

---

# 📚 15. Frequently Used String Methods

| Method       | Purpose           |
| ------------ | ----------------- |
| lower()      | Lowercase         |
| upper()      | Uppercase         |
| title()      | Title Case        |
| capitalize() | Sentence Case     |
| swapcase()   | Reverse Case      |
| strip()      | Remove Spaces     |
| replace()    | Replace Text      |
| split()      | Split String      |
| join()       | Join Strings      |
| find()       | Search            |
| index()      | Search            |
| count()      | Count             |
| startswith() | Starts With       |
| endswith()   | Ends With         |
| isdigit()    | Digits            |
| isalpha()    | Letters           |
| isalnum()    | Letters + Numbers |

---

# 📚 16. Built-in Functions Used with Strings

```python
len(text)

max(text)

min(text)

sorted(text)

list(text)
```

---

# 📚 17. Most Asked Interview Programs

✅ Reverse String

```python
text[::-1]
```

---

✅ Count Vowels

```python
for ch in text:
    if ch in "aeiouAEIOU":
        count += 1
```

---

✅ Count Uppercase

```python
if ch.isupper():
```

---

✅ Count Lowercase

```python
if ch.islower():
```

---

✅ Count Digits

```python
if ch.isdigit():
```

---

✅ Count Spaces

```python
if ch.isspace():
```

---

✅ Count Special Characters

```python
if not ch.isalnum() and not ch.isspace():
```

---

✅ Palindrome

```python
text == text[::-1]
```

---

✅ Remove Duplicates

```python
if ch not in result:
```

---

✅ Character Frequency

```python
text.count(ch)
```

---

# 📚 18. Important Method Comparisons

## find() vs index()

| find()     | index()                   |
| ---------- | ------------------------- |
| Returns -1 | Raises ValueError         |
| Safer      | Use when value must exist |

---

## strip() vs replace()

| strip()                | replace()              |
| ---------------------- | ---------------------- |
| Removes spaces at ends | Replaces text anywhere |

---

## title() vs capitalize()

| title()    | capitalize()      |
| ---------- | ----------------- |
| Every Word | Only First Letter |

---

## lower() vs casefold()

| lower()          | casefold()                                                |
| ---------------- | --------------------------------------------------------- |
| Normal lowercase | More aggressive lowercase (useful for international text) |

> **Note:** For beginners and most interviews, `lower()` is sufficient.

---

## split() vs join()

| split()       | join()        |
| ------------- | ------------- |
| String → List | List → String |

---

# 📚 19. Common Errors

## IndexError

```python
text[100]
```

---

## ValueError

```python
text.index("Java")
```

---

## TypeError

```python
",".join([1,2,3])
```

Correct

```python
",".join(["1","2","3"])
```

---

# 📚 20. Time Complexity (Interview)

| Operation          | Complexity |
| ------------------ | ---------- |
| Index Access       | O(1)       |
| Slicing            | O(k)       |
| Reverse (`[::-1]`) | O(n)       |
| find()             | O(n)       |
| count()            | O(n)       |
| replace()          | O(n)       |
| split()            | O(n)       |
| join()             | O(n)       |
| startswith()       | O(m)       |
| endswith()         | O(m)       |

> **n** = length of the string, **m** = length of the prefix/suffix being checked, **k** = length of the slice.

---

# 📚 21. Top 30 Interview Questions

### Basic

1. What is a String?
2. Is String mutable?
3. What is indexing?
4. What is slicing?
5. Difference between positive and negative indexing?

### Intermediate

6. Difference between `find()` and `index()`
7. Difference between `strip()` and `replace()`
8. Difference between `split()` and `join()`
9. Difference between `title()` and `capitalize()`
10. Difference between `lower()` and `upper()`

### Methods

11. What does `isdigit()` do?
12. What does `isalpha()` do?
13. What does `isalnum()` do?
14. What does `startswith()` do?
15. What does `endswith()` do?

### Programs

16. Reverse a String.
17. Count vowels.
18. Count uppercase letters.
19. Count lowercase letters.
20. Count digits.
21. Count spaces.
22. Count special characters.
23. Check palindrome.
24. Remove duplicate characters.
25. Count character frequency.
26. Split email into username and domain.
27. Count words.
28. Replace all spaces with `-`.
29. Check whether a string contains a substring.
30. Convert a sentence into title case.

---

# 📚 22. Real-World Uses

| Task                | Method                                             |
| ------------------- | -------------------------------------------------- |
| Email Validation    | `in`, `split()`                                    |
| Username Validation | `isalnum()`                                        |
| Mobile Validation   | `isdigit()`                                        |
| Name Validation     | `isalpha()`                                        |
| Password Checks     | `isalnum()`, `isupper()`, `islower()`, `isdigit()` |
| CSV Processing      | `split()`, `join()`                                |
| Search              | `find()`, `startswith()`                           |
| Text Cleaning       | `strip()`, `replace()`                             |

---

# 🧠 Final Memory Map

```text
                    PYTHON STRINGS
                          │
      ┌───────────────────┼────────────────────┐
      │                   │                    │
  Creation           Indexing            Slicing
      │                   │                    │
 Quotes            Positive/Negative     start:stop:step
      │                                     │
      ├─────────────────────────────────────┤
      │                                     │
   Looping                             Formatting
      │                                     │
 for loop                           format()
 range()                             f-string ⭐
      │
      ├────────────────────────────────────────────┐
      │                                            │
   Case Methods                             Cleaning Methods
      │                                            │
 lower() upper()                          strip()
 title() capitalize()                     lstrip()
 swapcase()                               rstrip()
                                          replace()
      │
      ├────────────────────────────────────────────┐
      │                                            │
 Searching                               Validation
      │                                            │
 find()                                  isdigit()
 index()                                 isalpha()
 count()                                 isalnum()
 startswith()                            isupper()
 endswith()                              islower()
                                         isspace()
      │
      ├────────────────────────────────────────────┐
      │                                            │
 Practice Programs                       Interview Questions
      │                                            │
 Reverse                                Mutable?
 Palindrome                             find vs index
 Count Vowels                           split vs join
 Count Digits                           strip vs replace
 Character Frequency                    title vs capitalize
 Remove Duplicates
```

---

# 🏆 Final Interview Tips (Must Remember)

### ⭐ Remember these 15 points

1. ✅ Strings are **ordered**.
2. ✅ Strings are **immutable**.
3. ✅ Strings support **indexing**.
4. ✅ Strings support **slicing**.
5. ✅ `[::-1]` reverses a string.
6. ✅ `find()` returns **-1** if not found.
7. ✅ `index()` raises **ValueError** if not found.
8. ✅ `split()` converts **String → List**.
9. ✅ `join()` converts **List → String**.
10. ✅ `strip()` removes spaces from both ends.
11. ✅ `replace()` replaces text anywhere in the string.
12. ✅ `isdigit()` checks digits only.
13. ✅ `isalpha()` checks letters only.
14. ✅ `isalnum()` checks letters and numbers only.
15. ✅ **f-strings** are the preferred way to format strings in modern Python.

---

# 🎉 Congratulations!

You have successfully completed the **Python Strings Master Handbook**.

## ✅ Topics Covered

* ✔ Introduction to Strings
* ✔ String Properties
* ✔ Indexing & Slicing
* ✔ Looping Through Strings
* ✔ Conditions & Formatting
* ✔ Case Conversion Methods
* ✔ Space Removal & Replace
* ✔ Split, Join & Searching
* ✔ Validation Methods
* ✔ Practice Programs
* ✔ Interview Questions
* ✔ Method Comparisons
* ✔ Time Complexity
* ✔ Common Errors
* ✔ Final Revision & Memory Map

---

## 📚 Your Python Learning Progress

You now have complete notes for:

* ✅ Python Functions
* ✅ While Loops
* ✅ Lists
* ✅ Tuples
* ✅ Sets
* ✅ Strings

**Next recommended topics (in interview order):**

1. 📘 Dictionaries
2. 📘 Files (File Handling)
3. 📘 Exception Handling
4. 📘 Modules & Packages
5. 📘 Object-Oriented Programming (OOP)
6. 📘 Regular Expressions (Regex)
7. 📘 Date & Time
8. 📘 NumPy
9. 📘 Pandas
10. 📘 SQL with Python

Following this sequence will take you from **beginner to Python interview-ready** in a structured way.
