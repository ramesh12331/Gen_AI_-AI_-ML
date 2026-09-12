# 📘 Python Lists – Final Revision & Interview Summary

## 🎯 Beginner to Interview Level (One-Shot Revision)

> **Goal:** Revise everything about Python Lists in 15–20 minutes before an interview.

---

# 📚 1. What is a List?

## ✅ Definition

A **List** is an **ordered, mutable collection** that can store **multiple values** in a single variable.

### Syntax

```python
numbers = [10, 20, 30, 40]
```

---

## Features

* ✅ Ordered
* ✅ Mutable (Can Modify)
* ✅ Allows Duplicate Values
* ✅ Supports Indexing
* ✅ Supports Slicing
* ✅ Can Store Different Data Types

Example

```python
data = [10, 2.5, "Python", True]
```

---

# 📚 2. Creating Lists

```python
numbers = [10,20,30]

names = ["A","B","C"]

mixed = [10,2.5,"Python",True]

empty = []

nested = [[1,2],[3,4]]
```

---

# 📚 3. Indexing

Positive Index

```text
0   1   2   3

↓

10 20 30 40
```

```python
numbers[0]
numbers[2]
```

Negative Index

```text
-4 -3 -2 -1
```

```python
numbers[-1]
numbers[-2]
```

---

# 📚 4. Slicing

Syntax

```python
list[start:stop:step]
```

Examples

```python
numbers[:3]

numbers[2:]

numbers[1:4]

numbers[::-1]
```

Output

```text
First 3

Last elements

Middle elements

Reverse list
```

---

# 📚 5. Updating List

```python
letters = ["A","B","C"]

letters[1]="Python"
```

Output

```python
['A','Python','C']
```

---

# 📚 6. Nested List

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
```

Access

```python
matrix[0][2]

matrix[2][1]
```

---

# 📚 7. List Methods

## append()

Adds element at end.

```python
numbers.append(50)
```

Before

```text
10 20 30
```

After

```text
10 20 30 50
```

---

## insert()

Adds at specified index.

```python
numbers.insert(1,100)
```

---

## extend()

Adds multiple elements.

```python
numbers.extend([60,70])
```

---

## remove()

Removes first occurrence.

```python
numbers.remove(20)
```

---

## pop()

Removes by index.

```python
numbers.pop()

numbers.pop(2)
```

---

## del

Deletes element or entire list.

```python
del numbers[1]

del numbers
```

---

## clear()

Removes everything.

```python
numbers.clear()
```

Output

```python
[]
```

---

# 📚 8. Operators

## Concatenation

```python
list1+list2
```

## Repetition

```python
list1*3
```

---

# 📚 9. Membership Operators

```python
10 in numbers

50 not in numbers
```

Returns

```python
True

False
```

---

# 📚 10. Looping

Simple Loop

```python
for num in numbers:
    print(num)
```

Using Index

```python
for i in range(len(numbers)):
    print(i,numbers[i])
```

Using enumerate()

```python
for index,value in enumerate(numbers):
    print(index,value)
```

---

# 📚 11. Conditions

```python
for num in numbers:

    if num>0:
        print("Positive")

    else:
        print("Negative")
```

---

# 📚 12. continue

Skips current iteration.

```python
for num in numbers:

    if num==20:
        continue

    print(num)
```

Output

```text
10
30
40
```

---

# 📚 13. break

Stops entire loop.

```python
for num in numbers:

    if num==20:
        break

    print(num)
```

Output

```text
10
```

---

# 📚 14. Searching Methods

## index()

Returns first occurrence.

```python
numbers.index(30)
```

---

## count()

Returns frequency.

```python
numbers.count(20)
```

---

# 📚 15. Sorting

Ascending

```python
numbers.sort()
```

Descending

```python
numbers.sort(reverse=True)
```

---

## reverse()

Reverses current order.

```python
numbers.reverse()
```

---

# 📚 16. Built-in Functions

Length

```python
len(numbers)
```

Total

```python
sum(numbers)
```

Smallest

```python
min(numbers)
```

Largest

```python
max(numbers)
```

Average

```python
sum(numbers)/len(numbers)
```

---

# 📚 17. List Comprehension

## Syntax

```python
[expression for item in iterable]
```

---

Squares

```python
[x**2 for x in range(1,6)]
```

Even Numbers

```python
[x for x in range(20) if x%2==0]
```

Uppercase

```python
[name.upper() for name in names]
```

Length

```python
[len(word) for word in words]
```

---

# 📚 18. List Properties

| Property      | List |
| ------------- | ---- |
| Ordered       | ✅    |
| Mutable       | ✅    |
| Duplicates    | ✅    |
| Indexing      | ✅    |
| Slicing       | ✅    |
| Heterogeneous | ✅    |

---

# 📚 19. Important List Methods

| Method    | Purpose               |
| --------- | --------------------- |
| append()  | Add one element       |
| insert()  | Insert at index       |
| extend()  | Add multiple elements |
| remove()  | Remove by value       |
| pop()     | Remove by index       |
| clear()   | Remove all            |
| index()   | Find position         |
| count()   | Count occurrences     |
| sort()    | Ascending order       |
| reverse() | Reverse order         |

---

# 📚 20. Important Built-in Functions

| Function    | Purpose           |
| ----------- | ----------------- |
| len()       | Count elements    |
| sum()       | Total             |
| min()       | Smallest          |
| max()       | Largest           |
| enumerate() | Index + Value     |
| range()     | Generate sequence |

---

# 📚 21. List vs Tuple vs Set

| Feature    | List | Tuple | Set |
| ---------- | ---- | ----- | --- |
| Syntax     | []   | ()    | {}  |
| Ordered    | ✅    | ✅     | ❌   |
| Mutable    | ✅    | ❌     | ✅   |
| Duplicates | ✅    | ✅     | ❌   |
| Indexing   | ✅    | ✅     | ❌   |
| Slicing    | ✅    | ✅     | ❌   |

---

# 📚 22. Time Complexity (Interview)

| Operation        | Complexity   |
| ---------------- | ------------ |
| Index Access     | O(1)         |
| Append           | O(1) Average |
| Insert Beginning | O(n)         |
| Delete           | O(n)         |
| Search (`in`)    | O(n)         |
| Sort             | O(n log n)   |

---

# 📚 23. Common Errors

## IndexError

```python
numbers=[10,20]

print(numbers[5])
```

---

## ValueError

```python
numbers.remove(100)
```

---

## TypeError

```python
sum(["A","B"])
```

---

# 📚 24. Most Asked Interview Questions

### 1. What is a List?

An ordered, mutable collection that stores multiple values.

---

### 2. Why do we use Lists?

To store multiple values in one variable and manage them easily.

---

### 3. Difference between List and Tuple?

| List         | Tuple          |
| ------------ | -------------- |
| Mutable      | Immutable      |
| More methods | Only 2 methods |
| Uses []      | Uses ()        |

---

### 4. Difference between append() and extend()?

| append()        | extend()               |
| --------------- | ---------------------- |
| Adds one object | Adds multiple elements |

Example

```python
a=[1,2]

a.append([3,4])

# [1,2,[3,4]]
```

```python
a=[1,2]

a.extend([3,4])

# [1,2,3,4]
```

---

### 5. Difference between remove() and pop()?

| remove()     | pop()                   |
| ------------ | ----------------------- |
| By value     | By index                |
| Returns None | Returns removed element |

---

### 6. Difference between sort() and reverse()?

| sort()          | reverse()           |
| --------------- | ------------------- |
| Arranges values | Only reverses order |

---

### 7. Difference between index() and count()?

| index()          | count()           |
| ---------------- | ----------------- |
| Returns position | Returns frequency |

---

### 8. Difference between append(), insert(), extend()

| Method   | Description       |
| -------- | ----------------- |
| append() | End of list       |
| insert() | Specific index    |
| extend() | Multiple elements |

---

### 9. What is List Comprehension?

A short and efficient way to create a new list using a single line of code.

---

### 10. Can Lists store different data types?

Yes.

Example

```python
[10,2.5,"Python",True]
```

---

# 📚 25. Frequently Asked Programs

```python
# Reverse List
numbers[::-1]
```

```python
# Largest
max(numbers)
```

```python
# Smallest
min(numbers)
```

```python
# Average
sum(numbers)/len(numbers)
```

```python
# Count Occurrence
numbers.count(20)
```

```python
# Position
numbers.index(30)
```

```python
# Even Numbers
[x for x in numbers if x%2==0]
```

```python
# Squares
[x*x for x in range(1,6)]
```

---

# 🎯 Final Memory Map

```text
                     PYTHON LISTS
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    Creation           Accessing         Updating
        │                  │                  │
      []              Indexing          Mutable
      list()          Slicing           Change Values
        │
        ├────────────────────────────────────────────┐
        │                                            │
     Methods                                 Built-in Functions
        │                                            │
 append() insert() extend()                len() sum()
 remove() pop() clear()                    min() max()
 index() count() sort() reverse()          enumerate()
        │
        ├────────────────────────────────────────────┐
        │                                            │
      Looping                                 List Comprehension
        │                                            │
   for loop                              [expression for item in iterable]
   range(len())                          if condition
   enumerate()                           nested comprehension
        │
        ├────────────────────────────────────────────┐
        │                                            │
     Conditions                               Interview Topics
        │                                            │
 if / elif / else                          List vs Tuple vs Set
 continue                                  append vs extend
 break                                     remove vs pop
                                           sort vs reverse
                                           index vs count
```

---

# 🏆 Final Interview Tips

### Always remember these 10 points:

1. ✅ Lists are **ordered**.
2. ✅ Lists are **mutable**.
3. ✅ Lists allow **duplicate values**.
4. ✅ Lists support **indexing and slicing**.
5. ✅ `append()` adds **one** element.
6. ✅ `extend()` adds **multiple** elements.
7. ✅ `remove()` removes by **value**.
8. ✅ `pop()` removes by **index** and returns the removed item.
9. ✅ `sort()` arranges elements; `reverse()` only reverses their current order.
10. ✅ **List Comprehension** is one of the most frequently asked Python interview topics.

## 🎉 Congratulations!

You now have a **complete interview revision** of **Python Lists**, covering definitions, syntax, methods, built-in functions, comparisons, common errors, interview questions, time complexity, and frequently asked coding patterns. This serves as an excellent last-minute revision sheet before interviews.
