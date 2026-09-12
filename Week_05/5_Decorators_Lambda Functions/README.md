# 📘 Python Advanced Functions – Final Interview Revision

## Generators → `filter()` → First-Class Functions → Decorators

Based on the code you shared, we'll revise these topics in the same beginner-friendly style.

---

# 1️⃣ GENERATORS

## ✅ Definition

A **Generator** is a special type of function that produces values **one at a time** using the `yield` keyword.

### Easy Interview Definition

> A generator is a function that uses `yield` to return values one by one instead of producing all values at once.

---

# 🔹 Why Generators?

Suppose we need numbers from `0` to `200`.

### Normal List

```python
numbers = []

i = 0

while i <= 200:
    numbers.append(i)
    i += 1
```

Here, all numbers are stored inside the list.

For very large data, this can require more memory.

---

# 🔹 Generator Syntax

```python
def function_name():
    yield value
```

The important keyword is:

```python
yield
```

---

# 🔹 Simple Generator

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

print(a)
```

You get a **generator object**, not all the numbers immediately.

---

# 🔹 `yield` vs `return`

This is very important for interviews.

### `return`

```python
def test():
    return 10
```

`return` sends the value back and finishes the function.

### `yield`

```python
def test():
    yield 10
    yield 20
    yield 30
```

`yield` gives one value and **pauses the function**.

When requested again, execution continues.

---

# 🔹 Using `next()`

Your example:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

print(next(a))
print(next(a))
print(next(a))
print(next(a))
```

Output:

```text
0
1
2
3
```

### Working

First:

```python
next(a)
```

→ `yield 0`

Function pauses.

Second:

```python
next(a)
```

Function continues:

```python
i += 1
```

→ `yield 1`

And so on.

---

# 🧠 Generator Execution Flow

```text
generate()
    ↓
Generator Object
    ↓
next(a)
    ↓
yield 0
    ↓
PAUSE
    ↓
next(a)
    ↓
Continue
    ↓
yield 1
    ↓
PAUSE
```

This **pause and resume behavior** is the heart of generators.

---

# 🔹 Generator with `for` Loop

Instead of calling `next()` manually:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

for value in a:
    print(value)
```

The `for` loop automatically requests the next value.

---

# 🔹 Generator to List

Your example:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

numbers = []

for value in a:
    numbers.append(value)

print(numbers)
```

Now the generated values are stored in a list.

---

# ⚠️ Important Point

Once you store all generator values in a list, the list itself uses memory for those values.

So the main generator memory advantage is useful when you **process values one at a time without storing all of them**.

---

# 📊 Normal Function vs Generator

| Normal Function                  | Generator                       |
| -------------------------------- | ------------------------------- |
| Usually uses `return`            | Uses `yield`                    |
| Function finishes after `return` | Pauses at `yield`               |
| Returns a normal value           | Returns generator object        |
| Cannot resume after `return`     | Can resume                      |
| Good for normal calculations     | Good for sequential/larger data |

---

# 🎯 Generator Interview Questions

### Q1. What is a Generator?

A generator is a special function that uses `yield` to produce values one at a time.

### Q2. Which keyword is used?

```python
yield
```

### Q3. What does `next()` do?

It retrieves the next value from the generator.

### Q4. Difference between `yield` and `return`?

`return` finishes the function.

`yield` pauses the function and allows it to continue later.

---

# 📌 Generator Summary

```text
GENERATOR
   ↓
Special Function
   ↓
yield
   ↓
One Value at a Time
   ↓
Pause
   ↓
next()
   ↓
Resume
```

---

# 2️⃣ `filter()` FUNCTION

## ✅ Definition

`filter()` is used to select elements from an iterable based on a condition.

### Easy Interview Definition

> `filter()` filters elements that satisfy a given condition.

---

# 🔹 Syntax

```python
filter(function, iterable)
```

Example:

```python
filter(even, numbers)
```

---

# 🔹 Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(x):
    return x % 2 == 0


result = filter(even, numbers)

print(result)
```

This gives a **filter object**.

To see the values:

```python
result = list(filter(even, numbers))

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

---

# 🔹 `filter()` with Lambda

Instead of:

```python
def even(x):
    return x % 2 == 0
```

We can write:

```python
result = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

Output:

```text
[2, 4, 6, 8]
```

---

# 🔹 Odd Numbers

```python
result = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

---

# 🔹 Filtering Strings

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

Notice:

```python
"America".startswith("a")
```

is `False` because string comparison is case-sensitive.

---

# 🔹 Filtering Dictionaries

```python
restaurants = [
    {"name": "abc", "ratings": 4.8},
    {"name": "efg", "ratings": 3.5},
    {"name": "xyz", "ratings": 4.9},
    {"name": "pqr", "ratings": 4.2}
]

result = list(
    filter(
        lambda x: x["ratings"] > 4.5,
        restaurants
    )
)

print(result)
```

The result contains restaurants with ratings greater than `4.5`.

---

# ⚠️ Common Mistake

Don't do:

```python
list = [1, 2, 3]
```

Then later:

```python
list(filter(...))
```

You used `list` as a variable name, so it shadows Python's built-in `list()`.

Prefer:

```python
numbers = [1, 2, 3]
```

---

# 📌 `filter()` Summary

```text
filter()
   ↓
Takes
   ↓
Function + Iterable
   ↓
Checks Condition
   ↓
Keeps Matching Values
   ↓
Filter Object
   ↓
list()
   ↓
Final List
```

---

# 3️⃣ FIRST-CLASS FUNCTIONS

This topic is extremely important before learning decorators.

## ✅ Definition

In Python, **functions are first-class objects**.

This means functions can be treated like other objects.

For example, a function can be:

* Assigned to a variable
* Passed to another function
* Returned from another function

Your code mainly demonstrates **returning a function from another function**.

---

# 🔹 Function Returning Function

```python
def fun():

    def add(x, y):
        print(x + y)

    return add


a = fun()

a(10, 20)
```

Output:

```text
30
```

---

# 🧠 Dry Run

### Step 1

```python
a = fun()
```

`fun()` executes.

Inside it:

```python
def add(x, y):
```

is created.

Then:

```python
return add
```

returns the function.

So conceptually:

```text
a → add function
```

Now:

```python
a(10, 20)
```

is effectively calling the returned `add` function.

---

# 🔹 Your Second Example

```python
def add(a, b):

    print(a + b)

    def mul(e, f):
        print(e * f)

    return mul


a = add(30, 40)

a(3, 4)
```

Output:

```text
70
12
```

This concept leads directly to **Decorators**.

---

# 📌 First-Class Function Summary

```text
FUNCTION
   ↓
Can be treated like an object
   ↓
Can be assigned
Can be passed
Can be returned
   ↓
Foundation of
   ↓
DECORATORS
```

---

# 4️⃣ DECORATORS

## ✅ Definition

A **Decorator** is a function that adds extra functionality to another function without changing the original function's main code.

### Easy Interview Definition

> A decorator is a function that takes another function, adds extra functionality, and returns a wrapper function.

---

# 🔹 Basic Syntax

```python
def decorator(func):

    def wrapper():

        # extra code

        func()

        # extra code

    return wrapper
```

---

# 🔹 Simple Decorator

Your example:

```python
def dec(func):

    def wrap():

        print("****************")

        func()

        print("****************")

    return wrap
```

Original function:

```python
def greet():
    print("Hello User!!!")
```

---

# 🔹 Manual Decoration

```python
a = dec(greet)

a()
```

Conceptually:

```text
greet
  ↓
dec(greet)
  ↓
wrap
  ↓
a
  ↓
a()
```

Output:

```text
****************
Hello User!!!
****************
```

---

# 🔹 `@decorator` Syntax

Instead of manually writing:

```python
a = dec(greet)
```

Python provides:

```python
@dec
def greet():
    print("Hello User!!!")
```

Then:

```python
greet()
```

---

# ⭐ Important Interview Point

```python
@dec
def greet():
    ...
```

is essentially decorator syntax for applying:

```python
greet = dec(greet)
```

---

# 5️⃣ Decorator with Function Arguments

Basic wrapper:

```python
def wrapper():
```

only works naturally with functions that don't require arguments.

For:

```python
add(10, 20)
```

we use:

```python
def wrapper(*args, **kwargs):
```

---

# 🔹 Example

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper
```

Now it can decorate many kinds of functions.

---

# 6️⃣ Timer Decorator

Your timer example is a very useful real-world decorator.

```python
import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(
            "Time:",
            end - start
        )

        return result

    return wrapper
```

Use:

```python
@timer
def add(a, b):

    print(a + b)

    time.sleep(3)


add(2, 4)
```

The decorator measures how long `add()` takes.

---

# 🔹 Decorator with `**kwargs`

Your example:

```python
@timer
def shopping(**values):
    print(values)


shopping(
    name="pizza",
    price=500
)
```

Here:

```python
**kwargs
```

allows keyword arguments.

---

# 🔹 Decorator with Return Value

Very important:

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before Function")

        result = func(*args, **kwargs)

        print("After Function")

        return result

    return wrapper
```

Function:

```python
@decorator
def square(num):
    return num * num


print(square(5))
```

Output:

```text
Before Function
After Function
25
```

---

# 🌍 Common Uses of Decorators

Decorators are commonly useful for concepts such as:

* Timing
* Logging
* Authentication
* Validation
* Permissions
* Reusing common before/after logic

---

# 📊 Normal Function vs Decorator

| Normal Function    | Decorator                 |
| ------------------ | ------------------------- |
| Performs main task | Adds extra behavior       |
| Called directly    | Wraps another function    |
| Simple execution   | Before/after logic        |
| Independent        | Receives another function |

---

# 🎓 Decorator Interview Questions

### Q1. What is a Decorator?

A decorator is a function that adds extra functionality to another function.

### Q2. What is a Wrapper Function?

It is the inner function that wraps and calls the original function.

### Q3. Why are functions first-class objects important?

Because functions can be passed and returned, which makes decorators possible.

### Q4. Why use `*args` and `**kwargs`?

To allow the decorator to work with functions having different arguments.

### Q5. What does `@decorator` mean?

It applies the decorator to the function.

---

# 🏆 FINAL INTERVIEW SUMMARY

```text
ADVANCED PYTHON FUNCTIONS
          │
 ┌────────┼─────────────┐
 │        │             │
Generator filter()   First-Class
 │        │          Functions
yield    condition       │
 │        │          Functions can
next()   lambda       be returned
 │        │             │
One      Filter        Decorators
value    values          │
at time                  │
                       wrapper
                         │
                    @decorator
                         │
                  *args / **kwargs
                         │
                  Timer / Logging
```

## 🚀 30-Second Revision

```text
✔ Generator uses yield.
✔ yield pauses and resumes a function.
✔ next() gets the next generator value.
✔ Generators produce values one at a time.

✔ filter() selects values based on a condition.
✔ filter() returns a filter object.
✔ filter() is commonly used with lambda.

✔ Python functions are first-class objects.
✔ Functions can be assigned, passed and returned.

✔ Decorators add extra functionality to functions.
✔ A decorator contains a wrapper function.
✔ @decorator applies a decorator.
✔ *args handles positional arguments.
✔ **kwargs handles keyword arguments.
✔ Decorators are useful for timing, logging and reusable before/after logic.
```

### ⭐ Most important interview connection

**First-Class Functions → Functions Returning Functions → Wrapper → Decorator → `@decorator`**

That connection is the key to understanding **why Python decorators work**.
