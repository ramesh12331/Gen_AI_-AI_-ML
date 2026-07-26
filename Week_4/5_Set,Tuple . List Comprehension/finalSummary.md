# 📘 Python Sets – Final Revision & Interview Summary

## 🎯 Beginner to Interview Level (One-Shot Revision)

> **Goal:** Revise Python Sets in **15–20 minutes** before an interview.

---

# 📚 1. What is a Set?

## ✅ Definition

A **Set** is an **unordered collection of unique elements**.

It automatically removes duplicate values.

### Syntax

```python
numbers = {10, 20, 30}
```

---

# 📚 2. Features of Set

| Feature     | Set           |
| ----------- | ------------- |
| Ordered     | ❌ No          |
| Mutable     | ✅ Yes         |
| Duplicates  | ❌ Not Allowed |
| Indexing    | ❌ No          |
| Slicing     | ❌ No          |
| Fast Search | ✅ Yes         |

---

# 📚 3. Creating Sets

```python
numbers = {10, 20, 30}
```

### Empty Set

❌ Wrong

```python
s = {}
```

Output

```python
<class 'dict'>
```

✅ Correct

```python
s = set()
```

Output

```python
<class 'set'>
```

---

# 📚 4. Important Methods

## add()

Adds one element.

```python
s = {10,20}

s.add(30)
```

---

## update()

Adds multiple elements.

```python
s.update([40,50])

s.update((60,70))
```

---

## remove()

Removes an element.

Raises **KeyError** if not found.

```python
s.remove(20)
```

---

## discard()

Removes an element safely.

No error if the element does not exist.

```python
s.discard(100)
```

---

## pop()

Removes and returns **one arbitrary element**.

```python
value = s.pop()
```

---

## clear()

Removes all elements.

```python
s.clear()
```

---

## copy()

Creates another Set.

```python
new_set = s.copy()
```

---

# 📚 5. Accessing Elements

Sets do **not support indexing**.

❌ Wrong

```python
s[0]
```

Use a loop instead.

```python
for item in s:
    print(item)
```

---

# 📚 6. Membership Operator

```python
if 20 in s:
    print("Found")
```

Returns

* `True`
* `False`

---

# 📚 7. Set Operators

Assume

```python
A = {1,2,3,4}

B = {3,4,5,6}
```

---

## Union (`|`)

Returns all unique elements.

```python
A | B
```

Output

```python
{1,2,3,4,5,6}
```

---

## Intersection (`&`)

Returns common elements.

```python
A & B
```

Output

```python
{3,4}
```

---

## Difference (`-`)

Returns elements in the first Set but not in the second.

```python
A - B
```

Output

```python
{1,2}
```

---

## Symmetric Difference (`^`)

Returns elements that are in either Set but **not in both**.

```python
A ^ B
```

Output

```python
{1,2,5,6}
```

---

# 📚 8. Subset & Superset

## issubset()

```python
A = {1,2}

B = {1,2,3}

print(A.issubset(B))
```

Output

```python
True
```

---

## issuperset()

```python
print(B.issuperset(A))
```

Output

```python
True
```

---

# 📚 9. Set Comprehension

### Syntax

```python
{
    expression
    for variable in iterable
}
```

Example

```python
numbers = {x*x for x in range(1,6)}

print(numbers)
```

Output

```python
{1,4,9,16,25}
```

With Condition

```python
even = {x for x in range(1,11) if x%2==0}
```

---

# 📚 10. Modifying a Set During Iteration

❌ Wrong

```python
for i in s:
    s.add(100)
```

Output

```python
RuntimeError
```

---

✅ Correct

```python
for i in s.copy():
    if i == 3:
        s.add(300)
```

---

# 📚 11. Time Complexity

| Operation         | Complexity   |
| ----------------- | ------------ |
| Add               | O(1)         |
| Remove            | O(1)         |
| Discard           | O(1)         |
| Membership (`in`) | O(1)         |
| Union             | O(n + m)     |
| Intersection      | O(min(n, m)) |
| Difference        | O(n)         |
| Copy              | O(n)         |
| Clear             | O(n)         |

---

# 📚 12. Method Summary

| Method                         | Purpose                      |                     |
| ------------------------------ | ---------------------------- | ------------------- |
| `add()`                        | Add one element              |                     |
| `update()`                     | Add multiple elements        |                     |
| `remove()`                     | Remove (error if missing)    |                     |
| `discard()`                    | Remove safely                |                     |
| `pop()`                        | Remove one arbitrary element |                     |
| `clear()`                      | Remove all elements          |                     |
| `copy()`                       | Create a copy                |                     |
| `union()` / `                  | `                            | All unique elements |
| `intersection()` / `&`         | Common elements              |                     |
| `difference()` / `-`           | First Set only               |                     |
| `symmetric_difference()` / `^` | Non-common elements          |                     |
| `issubset()`                   | Check subset                 |                     |
| `issuperset()`                 | Check superset               |                     |

---

# 📚 13. Set vs List vs Tuple

| Feature       | List | Tuple | Set |
| ------------- | ---- | ----- | --- |
| Ordered       | ✅    | ✅     | ❌   |
| Mutable       | ✅    | ❌     | ✅   |
| Duplicates    | ✅    | ✅     | ❌   |
| Indexing      | ✅    | ✅     | ❌   |
| Slicing       | ✅    | ✅     | ❌   |
| Unique Values | ❌    | ❌     | ✅   |

---

# 📚 14. Common Errors

### ❌ Using `{}` for an Empty Set

```python
s = {}
```

Creates a **Dictionary**, not a Set.

Correct

```python
s = set()
```

---

### ❌ Using Indexing

```python
s[0]
```

Output

```python
TypeError
```

---

### ❌ Using `remove()` for a Missing Element

```python
s.remove(100)
```

Output

```python
KeyError
```

Use

```python
s.discard(100)
```

---

### ❌ Modifying a Set During Iteration

```python
for i in s:
    s.add(10)
```

Output

```python
RuntimeError
```

---

# 📚 15. Real-Life Applications

Sets are used in:

* 👨‍🎓 Student IDs
* 📧 Email Deduplication
* 📱 Unique Phone Numbers
* 🛒 Product Categories
* 🏷️ Social Media Tags
* 📊 Data Analysis
* 🤖 Machine Learning
* 🔍 Fast Membership Testing

---

# 📚 16. Top 20 Interview Questions

1. What is a Set?
2. What are the characteristics of a Set?
3. Are Sets ordered?
4. Are Sets mutable?
5. Do Sets allow duplicate values?
6. Can Sets be indexed?
7. Difference between `add()` and `update()`.
8. Difference between `remove()` and `discard()`.
9. What does `pop()` do?
10. What does `clear()` do?
11. What does `copy()` do?
12. What is Union?
13. What is Intersection?
14. What is Difference?
15. What is Symmetric Difference?
16. What is a Subset?
17. What is a Superset?
18. What is Set Comprehension?
19. Why are Sets fast for searching?
20. Why can't we modify a Set while iterating?

---

# 📚 17. Memory Tricks

```text
Set

↓

Unique Values
```

```text
{}

↓

Dictionary ❌
```

```text
set()

↓

Empty Set ✅
```

```text
add()

↓

One Element
```

```text
update()

↓

Multiple Elements
```

```text
remove()

↓

Error if Missing
```

```text
discard()

↓

Safe Remove
```

```text
pop()

↓

Remove One Arbitrary Element
```

```text
Union (|)

↓

Everything
```

```text
Intersection (&)

↓

Common Elements
```

```text
Difference (-)

↓

First Set Only
```

```text
Symmetric Difference (^)

↓

Everything Except Common
```

```text
Subset

↓

Small Set Inside Large Set
```

```text
Superset

↓

Large Set Contains Small Set
```

---

# 📚 18. One-Page Mind Map

```text
                     PYTHON SETS
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Characteristics      Creation          Access
        │                  │                  │
  Unique Values         {} ❌            for loop
  Unordered             set() ✅         in operator
  Mutable
  No Indexing
        │
        ├──────────────────┼──────────────────┐
        │                  │                  │
      Methods          Operators        Relationships
        │                  │                  │
 add()                Union (|)
 update()             Intersection (&)
 remove()             Difference (-)
 discard()            Symmetric (^)
 pop()                │
 clear()         issubset()
 copy()          issuperset()
        │
        └──────────────────┬──────────────────┘
                           │
                   Set Comprehension
                   {x for x in iterable}
```

---

# 🏆 Final Interview Tips

### ⭐ Remember these 15 points

1. ✅ Sets store **unique values only**.
2. ✅ Sets are **unordered**.
3. ✅ Sets are **mutable**.
4. ✅ Sets **do not support indexing**.
5. ✅ `{}` creates a **Dictionary**, not a Set.
6. ✅ Use `set()` to create an empty Set.
7. ✅ `add()` adds one element.
8. ✅ `update()` adds multiple elements.
9. ✅ `remove()` raises `KeyError` if the element is missing.
10. ✅ `discard()` safely removes elements.
11. ✅ `pop()` removes an **arbitrary** element.
12. ✅ Sets are fast for membership testing because of **hash tables**.
13. ✅ Do not modify a Set while iterating; iterate over `s.copy()` if needed.
14. ✅ Use Set Comprehension for concise Set creation.
15. ✅ Know the four operators: `|`, `&`, `-`, and `^`.

---

# 🎉 Congratulations!

You have completed the **Python Sets Master Handbook**.

## ✅ Topics Covered

* ✔ Introduction to Sets
* ✔ Creating Sets
* ✔ Empty Set vs Dictionary
* ✔ `add()` & `update()`
* ✔ Accessing Elements
* ✔ `remove()`, `discard()`, `pop()`, `clear()`, `copy()`
* ✔ Set Operators
* ✔ `issubset()` & `issuperset()`
* ✔ Set Comprehension
* ✔ Modifying Sets Safely
* ✔ Interview Questions
* ✔ MCQs
* ✔ Practice Programs
* ✔ Final Revision & Cheat Sheet

> **Interview Tip:** If an interviewer asks, **"Why would you use a Set instead of a List?"**, the best answer is:
>
> **"I use a Set when I need unique values and fast membership testing. Sets automatically remove duplicates and provide average O(1) lookup time, while Lists preserve order and allow duplicates."**
