# 📘 CHAPTER 2 — PYTHON `filter()` FUNCTION

## 🌱 Beginner → Step-by-Step → Real-Time → Interview Level

Now that we have covered **Generators**, the next topic from your code is **`filter()`**.

The name itself gives us a clue:

> **Filter = keep what we want and remove what we don't want.**

---

# 1. ✅ Definition — What is `filter()`?

`filter()` is a Python built-in function used to **select elements from an iterable based on a condition**.

### Simple English

Suppose we have:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

But we want only:

```text
2, 4, 6
```

We need to **filter** the even numbers.

Python provides:

```python
filter()
```

### 🎤 Interview Definition

> `filter()` is a built-in Python function that returns elements from an iterable for which the given function evaluates to true.

---

# 2. ✅ Why Do We Need `filter()`?

Imagine this list:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]
```

Requirement:

> Give me only numbers greater than `25`.

Without `filter()`, we can write:

```python
result = []

for num in numbers:
    if num > 25:
        result.append(num)

print(result)
```

Output:

```text
[30, 35, 40]
```

This is perfectly valid.

But Python also allows:

```python
result = list(filter(lambda num: num > 25, numbers))

print(result)
```

Output:

```text
[30, 35, 40]
```

So `filter()` is useful when we want to **select elements according to a condition**.

---

# 3. 🌍 Real-Life Example

Imagine a security guard standing at a company entrance.

Employees arrive:

```text
Ramesh → ID Card ✅
Rahul  → No ID   ❌
Ajay   → ID Card ✅
Anil   → No ID   ❌
```

Condition:

```text
Does the person have an ID card?
```

Only people satisfying the condition enter.

Conceptually:

```text
All People
    ↓
Security Check
    ↓
Has ID?
  /      \
Yes       No
 ↓         ↓
Allow    Reject
```

That's similar to `filter()`.

---

# 4. ✅ Syntax

The basic syntax is:

```python
filter(function, iterable)
```

There are **two important parts**.

### Part 1 — Function

```python
function
```

This checks the condition.

### Part 2 — Iterable

```python
iterable
```

This contains the values we want to check.

For example:

```python
filter(even, numbers)
```

Here:

```text
even
 ↓
Condition Function

numbers
 ↓
Iterable/Data
```

---

# 5. 🔄 Flow Diagram

Suppose:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

and our condition is:

```python
x % 2 == 0
```

Flow:

```text
              numbers
                 │
                 ▼
        [1, 2, 3, 4, 5, 6]
                 │
                 ▼
              filter()
                 │
                 ▼
         Check each number
                 │
        ┌────────┴────────┐
        │                 │
      True              False
        │                 │
       Keep             Ignore
        │
        ▼
     2, 4, 6
```

---

# 6. ✅ Simple Example

Let's use your example.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(x):
    return x % 2 == 0

result = filter(even, numbers)

print(result)
```

You might expect:

```text
[2, 4, 6, 8]
```

But you get something similar to:

```text
<filter object at ...>
```

## Why?

Because `filter()` returns a **filter object**.

To see all the filtered values as a list:

```python
result = list(filter(even, numbers))

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

---

# 7. 🔍 Dry Run — Line by Line

Consider:

```python
numbers = [1, 2, 3, 4]

def even(x):
    return x % 2 == 0

result = list(filter(even, numbers))
```

Let's understand exactly what happens.

### Step 1

Python gets:

```python
numbers = [1, 2, 3, 4]
```

### Step 2

Python knows the function:

```python
def even(x):
    return x % 2 == 0
```

### Step 3

`filter()` starts checking elements.

First value:

```text
x = 1
```

Condition:

```python
1 % 2 == 0
```

Result:

```text
False
```

So:

```text
1 ❌ rejected
```

Second:

```text
x = 2
```

Condition:

```python
2 % 2 == 0
```

Result:

```text
True
```

So:

```text
2 ✅ selected
```

Third:

```text
x = 3
```

Result:

```text
False
```

Rejected.

Fourth:

```text
x = 4
```

Result:

```text
True
```

Selected.

Final result:

```python
[2, 4]
```

---

# 8. 🧠 Memory / Processing Diagram

`filter()` in Python 3 returns a **lazy filter object**.

Conceptually:

```text
numbers
   │
   ▼
filter object
   │
   ▼
Check values as requested
   │
   ├── condition True  → produce value
   │
   └── condition False → skip value
```

If you do:

```python
result = filter(even, numbers)
```

Python does not first need to build a new list containing every matching value.

But:

```python
result = list(filter(even, numbers))
```

consumes the filter and creates a list containing the results.

This is similar to the lazy-processing idea you learned with generators.

---

# 9. ✅ Example — Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(x):
    return x % 2 == 0

result = list(filter(even, numbers))

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

### Logic

```text
number % 2 == 0
        ↓
       True
        ↓
     Keep it
```

---

# 10. ✅ Example — Odd Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def odd(x):
    return x % 2 != 0

result = list(filter(odd, numbers))

print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

---

# 11. 🔥 `filter()` with Lambda

You already learned lambda functions.

Normal function:

```python
def even(x):
    return x % 2 == 0
```

Lambda version:

```python
lambda x: x % 2 == 0
```

Therefore:

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(result)
```

Output:

```text
[2, 4, 6]
```

---

# 12. 🧠 Understand the Lambda

This:

```python
lambda x: x % 2 == 0
```

means:

```text
Take x
  ↓
Check
x % 2 == 0
  ↓
True / False
```

For:

```text
x = 4
```

Python checks:

```text
4 % 2 == 0
0 == 0
True
```

So `4` is kept.

---

# 13. 🔥 Multiple Example — Numbers Greater Than 50

```python
numbers = [10, 70, 20, 90, 45, 100]

result = list(
    filter(
        lambda x: x > 50,
        numbers
    )
)

print(result)
```

Output:

```text
[70, 90, 100]
```

---

# 14. 🔥 Multiple Conditions

Requirement:

> Select numbers that are even AND greater than 20.

```python
numbers = [10, 15, 20, 25, 30, 40, 45]

result = list(
    filter(
        lambda x: x % 2 == 0 and x > 20,
        numbers
    )
)

print(result)
```

Output:

```text
[30, 40]
```

Condition:

```text
Even
 AND
Greater than 20
```

Both conditions must be `True`.

---

# 15. 🔤 String Filtering

Your example:

```python
words = [
    "apple",
    "America",
    "andhra",
    "banana",
    "cat"
]

result = list(
    filter(
        lambda x: x.startswith("a"),
        words
    )
)

print(result)
```

Output:

```text
['apple', 'andhra']
```

Why isn't `"America"` selected?

Because:

```python
"America".startswith("a")
```

returns:

```text
False
```

Python strings are case-sensitive.

---

# 16. 🔤 Case-Insensitive Filtering

If you want both:

```text
apple
America
andhra
```

you can normalize the case:

```python
result = list(
    filter(
        lambda x: x.lower().startswith("a"),
        words
    )
)

print(result)
```

Output:

```text
['apple', 'America', 'andhra']
```

---

# 17. 🔥 Filter Words by Length

Suppose:

```python
languages = [
    "C",
    "Java",
    "Python",
    "JavaScript",
    "SQL"
]
```

Requirement:

> Select words whose length is greater than 4.

```python
result = list(
    filter(
        lambda word: len(word) > 4,
        languages
    )
)

print(result)
```

Output:

```text
['Python', 'JavaScript']
```

---

# 18. 📦 Dictionary Filtering

Now let's understand the dictionary example from your notes.

```python
restaurants = [
    {"name": "abc", "ratings": 4.8},
    {"name": "efg", "ratings": 3.5},
    {"name": "xyz", "ratings": 4.9},
    {"name": "pqr", "ratings": 4.2}
]
```

Notice something important.

This is actually:

```text
LIST
 │
 ├── Dictionary
 ├── Dictionary
 ├── Dictionary
 └── Dictionary
```

So each `x` inside `filter()` is one dictionary.

---

# 19. Dictionary Filter Example

Requirement:

> Select restaurants with ratings greater than `4.5`.

```python
result = list(
    filter(
        lambda x: x["ratings"] > 4.5,
        restaurants
    )
)

print(result)
```

Result contains:

```python
[
    {"name": "abc", "ratings": 4.8},
    {"name": "xyz", "ratings": 4.9}
]
```

---

# 20. 🔍 Dictionary Dry Run

First dictionary:

```python
x = {"name": "abc", "ratings": 4.8}
```

Condition:

```python
x["ratings"] > 4.5
```

becomes:

```text
4.8 > 4.5
True
```

Keep it. ✅

Second:

```text
3.5 > 4.5
False
```

Reject it. ❌

Third:

```text
4.9 > 4.5
True
```

Keep it. ✅

Fourth:

```text
4.2 > 4.5
False
```

Reject it. ❌

Final:

```text
abc ✅
xyz ✅
```

---

# 21. 💼 Interview Example — Employee Salary

Suppose:

```python
employees = [
    {"name": "Ramesh", "salary": 40000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Ajay", "salary": 30000},
    {"name": "Anil", "salary": 90000}
]
```

Requirement:

> Find employees earning more than ₹50,000.

```python
result = list(
    filter(
        lambda employee: employee["salary"] > 50000,
        employees
    )
)

print(result)
```

Result:

```text
Rahul
Anil
```

This type of logic is useful in interview questions because it combines:

```text
List
+
Dictionary
+
Lambda
+
filter()
```

---

# 22. 🌍 Real-Time Example — Product Filtering

Imagine an e-commerce application.

Products:

```python
products = [
    {"name": "Laptop", "price": 60000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500},
    {"name": "Mobile", "price": 30000}
]
```

Requirement:

> Show products below ₹2,000.

```python
result = list(
    filter(
        lambda product: product["price"] < 2000,
        products
    )
)

for product in result:
    print(product["name"])
```

Output:

```text
Mouse
Keyboard
```

Conceptually:

```text
All Products
     ↓
Price < 2000?
     ↓
 ┌───┴────┐
Yes       No
 ↓         ↓
Show      Skip
```

---

# 23. ❌ Common Mistake — Using `list` as Variable

Your notes contain this important mistake:

```python
list = [1, 2, 3]
```

Later:

```python
result = list(filter(even, list))
```

Problem:

You replaced the built-in name:

```python
list
```

with your variable.

So Python can no longer use `list()` normally in that scope.

You may get:

```text
TypeError:
'list' object is not callable
```

### Correct

```python
numbers = [1, 2, 3]

result = list(filter(even, numbers))
```

---

# 24. ❌ Common Mistake — Passing Function Incorrectly

Correct:

```python
filter(even, numbers)
```

Notice:

```python
even
```

not:

```python
even()
```

Why?

`filter()` needs the **function itself** so it can call it for each value.

---

# 25. ❌ Common Mistake — Forgetting `list()`

```python
result = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(result)
```

You'll see a filter-object representation.

If you specifically want a list:

```python
result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)
```

---

# 26. ❌ Common Mistake — Wrong Condition

Suppose you want even numbers.

Wrong:

```python
lambda x: x % 2
```

This can still be used as a truth test, but it selects values with a truthy remainder — for integers, that means it commonly selects odd numbers.

For beginner-readable even-number logic, use:

```python
lambda x: x % 2 == 0
```

This clearly returns:

```text
True / False
```

---

# 27. ⭐ Important Concept — `filter()` Does Not Change Values

Suppose:

```python
numbers = [1, 2, 3, 4]
```

`filter()` answers:

> Which values should I keep?

For example:

```text
Keep 2
Keep 4
```

It does **not** mean:

```text
1 → 10
2 → 20
3 → 30
```

Changing every value is usually a **mapping/transformation** task.

This distinction is important for interviews.

---

# 28. 📊 `filter()` vs Normal Loop

| Normal Loop                       | `filter()`                  |
| --------------------------------- | --------------------------- |
| Explicit step-by-step logic       | Compact filtering operation |
| Usually uses `if` + `append()`    | Uses predicate function     |
| Beginner-friendly                 | Functional style            |
| Easy for complex multi-step logic | Nice for simple conditions  |
| You control output structure      | Returns a filter iterator   |

Normal:

```python
result = []

for x in numbers:
    if x % 2 == 0:
        result.append(x)
```

Filter:

```python
result = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

Both can produce the same result.

---

# 29. 📊 `filter()` vs List Comprehension

`filter()`:

```python
result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)
```

List comprehension:

```python
result = [
    x
    for x in numbers
    if x % 2 == 0
]
```

| `filter()`                 | List Comprehension           |
| -------------------------- | ---------------------------- |
| Uses a predicate function  | Condition written directly   |
| Returns lazy filter object | Creates list immediately     |
| Often combined with lambda | Often very readable          |
| Functional style           | Pythonic comprehension style |

For simple filtering, many Python programmers find list comprehensions easier to read.

---

# 30. 📊 `filter()` vs Generator

This connects to your previous chapter.

| `filter()`                        | Generator                                   |
| --------------------------------- | ------------------------------------------- |
| Filters an existing iterable      | Can produce a sequence                      |
| Keeps values satisfying condition | Uses `yield` in generator functions         |
| Returns filter iterator           | Generator function returns generator object |
| Lazy                              | Lazy                                        |
| Condition-focused                 | Generation/iteration-focused                |

---

# 31. ✅ Advantages

`filter()` provides:

* ✅ Short code for simple filtering
* ✅ Works with many iterables
* ✅ Lazy evaluation
* ✅ Works nicely with lambda
* ✅ Useful for selecting data
* ✅ Can avoid building an intermediate result list until needed

---

# 32. ❌ Disadvantages

* ❌ Lambda expressions can become difficult to read if conditions are complicated.
* ❌ Beginners may be confused by the filter object.
* ❌ Debugging complex lambdas can be harder.
* ❌ List comprehension may be clearer for many simple cases.

---

# 33. ⭐ Important Notes

Remember these points:

```text
1. filter() is a built-in function.

2. Syntax:
   filter(function, iterable)

3. The condition determines which elements remain.

4. filter() returns a filter iterator in Python 3.

5. list() can consume it into a list.

6. filter() is commonly used with lambda.

7. It works with numbers, strings, dictionaries, etc.

8. Don't use built-in names such as list as variable names.

9. filter() selects values; it doesn't primarily transform them.

10. filter objects are lazy and are consumed as you iterate.
```

---

# 34. 🎤 Interview Questions & Answers

### Q1. What is `filter()`?

**Answer:**

> `filter()` is a built-in Python function used to select elements from an iterable based on a condition.

---

### Q2. What is the syntax?

```python
filter(function, iterable)
```

---

### Q3. What does `filter()` return in Python 3?

**Answer:**

A filter iterator/object.

---

### Q4. How do you convert it to a list?

```python
list(filter(function, iterable))
```

---

### Q5. Can we use lambda with `filter()`?

Yes.

```python
filter(lambda x: x > 10, numbers)
```

---

### Q6. Can `filter()` work with dictionaries?

Yes, for example when filtering a list of dictionaries.

```python
filter(
    lambda x: x["salary"] > 50000,
    employees
)
```

---

### Q7. What should the filtering function return?

Usually a truthy or falsy result indicating whether each element should be kept.

For clear conditions:

```python
return x % 2 == 0
```

---

### Q8. Is `filter()` lazy?

Yes.

It produces matching elements as the filter iterator is consumed.

---

### Q9. Difference between `filter()` and a list comprehension?

`filter()` uses a function/predicate and returns a lazy iterator.

A list comprehension directly creates a list.

---

### Q10. What happens if no element matches?

For example:

```python
numbers = [1, 3, 5]

result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(result)
```

Output:

```text
[]
```

---

# 35. 📝 MCQs

### Q1. What is the correct syntax?

A.

```python
filter(iterable, function)
```

B.

```python
filter(function, iterable)
```

C.

```python
filter(condition)
```

D.

```python
filter(iterable)
```

✅ **Answer: B**

---

### Q2. What does `filter()` return in Python 3?

A. Integer
B. String
C. Filter iterator/object
D. Dictionary

✅ **Answer: C**

---

### Q3. Which condition selects even numbers?

A.

```python
x % 2 == 0
```

B.

```python
x / 2
```

C.

```python
x == 2
```

D.

```python
x % 2 == 1
```

✅ **Answer: A**

---

### Q4. What is wrong with this?

```python
list = [1, 2, 3]

list(filter(...))
```

A. Nothing
B. `filter()` is invalid
C. Built-in `list()` was shadowed
D. Lists can't contain integers

✅ **Answer: C**

---

# 36. 💻 Practice Programs

Try these yourself without copying the answer first:

**Easy**

1. Filter even numbers from `1–20`
2. Filter odd numbers
3. Filter numbers greater than `50`
4. Filter numbers less than `20`
5. Filter positive numbers

**Medium**

6. Filter negative numbers
7. Filter numbers divisible by `5`
8. Filter numbers divisible by both `3` and `5`
9. Filter words beginning with `"p"`
10. Filter words with length greater than `5`

**Interview Practice**

11. Filter students with marks above `75`
12. Filter employees with salary above `50000`
13. Filter products below ₹1000
14. Filter restaurants with ratings above `4.5`
15. Filter active users from a list of dictionaries

---

# 37. 🧠 Coding Challenges

## Challenge 1

Given:

```python
numbers = [10, 15, 22, 30, 41, 50, 63]
```

Find numbers that are:

```text
Even
AND
Greater than 20
```

Expected:

```text
[22, 30, 50]
```

---

## Challenge 2

Given:

```python
names = [
    "Ramesh",
    "Ajay",
    "Anil",
    "Rahul",
    "Arun"
]
```

Find names starting with:

```text
A
```

Expected:

```text
['Ajay', 'Anil', 'Arun']
```

---

## Challenge 3

Given:

```python
students = [
    {"name": "Ramesh", "marks": 85},
    {"name": "Rahul", "marks": 40},
    {"name": "Ajay", "marks": 95},
    {"name": "Anil", "marks": 60}
]
```

Filter students whose marks are:

```text
>= 75
```

Expected names:

```text
Ramesh
Ajay
```

---

# 38. 🚀 Final Summary

```text
                    filter()
                       │
                       ▼
             Select wanted values
                       │
                       ▼
          filter(function, iterable)
                       │
            ┌──────────┴──────────┐
            │                     │
         Function              Iterable
            │                     │
       Condition              Input Data
            │
            ▼
        True / False
            │
      ┌─────┴─────┐
      │           │
    True        False
      │           │
    Keep         Skip
      │
      ▼
 Filter Iterator
      │
      ▼
 list(...) if a list is needed
```

# ⚡ 30-Second Interview Revision

```text
filter()
→ Built-in Python function
→ Used to select elements
→ Syntax: filter(function, iterable)
→ Condition decides which elements remain
→ Returns a filter iterator
→ list() can convert/consume it into a list
→ Commonly used with lambda
→ Works with numbers, strings and collections
→ Lazy evaluation
→ filter() selects values
```

## ⭐ One line to remember

> **`filter()` asks one question for every value: “Should I keep this value?” If the answer is true, it keeps it; if false, it skips it.**

Next topic in your notes is **Chapter 3 — First-Class Functions**, which is especially important because **you must understand first-class functions before Decorators make sense**.
___
---
