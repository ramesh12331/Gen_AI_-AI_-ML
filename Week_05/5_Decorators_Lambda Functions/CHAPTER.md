# 📘 CHAPTER 1 — PYTHON GENERATORS

We’ll learn **Generators from zero**, using the same examples from your notes.

---

# 1️⃣ What is a Generator? ⚙️

## ✅ Definition

A **Generator is a special type of function that produces values one at a time instead of creating and storing all values at once.**

### ⭐ Easy definition

> **Generator = Generate one value → pause → generate next value → pause.**

The most important keyword is:

```python
yield
```

Normal function commonly uses:

```python
return
```

Generator function uses:

```python
yield
```

---

# 2️⃣ Why Do We Need Generators? 🤔

In your notes, first you created numbers from `0` to `200` using a list:

```python
numbers = []

i = 0

while i <= 200:
    numbers.append(i)
    i += 1

print(numbers)
```

This creates:

```text
[0, 1, 2, 3, 4, 5, ..., 200]
```

Here, all the generated numbers are collected in the list.

Your notes then check the list object's size using:

```python
import sys

print(sys.getsizeof(numbers))
```

The generator example takes a different approach: it uses `yield` to produce values one by one.

---

# 3️⃣ Real-Life Example 🌍

Think about **YouTube videos**.

Suppose YouTube has millions of videos.

You don't need to load every video before watching the first one.

Instead:

```text
Request
   ↓
Video 1
   ↓
Watch
   ↓
Next
   ↓
Video 2
   ↓
Watch
   ↓
Next...
```

Generator idea:

```text
Ask for value
     ↓
Generate value
     ↓
Pause ⏸️
     ↓
Ask next()
     ↓
Continue
     ↓
Generate next value
```

---

# 4️⃣ Generator Syntax 📝

Basic syntax:

```python
def function_name():

    yield value
```

Example:

```python
def generate():

    yield 10
```

Calling:

```python
a = generate()
```

Important:

```python
print(a)
```

does **not** directly print:

```text
10
```

It gives a generator object representation.

To retrieve the generated value:

```python
print(next(a))
```

Output:

```text
10
```

---

# 5️⃣ Normal Function vs Generator ⚖️

Your normal-function example is:

```python
def generate():

    i = 0

    while i <= 200:
        print(i, end=" ")
        i += 1


generate()
```

Here the function directly prints each value.

Conceptually:

```text
generate()
    ↓
i = 0
    ↓
print(0)
    ↓
i = 1
    ↓
print(1)
    ↓
i = 2
    ↓
print(2)
    ↓
...
    ↓
200
```

---

# 6️⃣ Generator Version ⚙️

Your generator code:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


print(generate())
```

The major difference is:

```python
yield i
```

instead of:

```python
print(i)
```

---

# 7️⃣ What Does `yield` Mean? ⭐⭐⭐

This is the most important concept.

`yield`:

> **produces a value and pauses the generator's execution so it can continue later.**

Example:

```python
def generate():

    yield 10
    yield 20
    yield 30
```

Create generator:

```python
a = generate()
```

Get first value:

```python
print(next(a))
```

Output:

```text
10
```

Generator pauses after that `yield`.

Again:

```python
print(next(a))
```

Output:

```text
20
```

Again:

```python
print(next(a))
```

Output:

```text
30
```

---

# 8️⃣ Flow Diagram 🔄

```text
        generate()
            ↓
    Generator Object
            ↓
        next(a)
            ↓
        yield 10
            ↓
          10
            ↓
        ⏸️ PAUSE
            ↓
        next(a)
            ↓
       Continue
            ↓
        yield 20
            ↓
          20
            ↓
        ⏸️ PAUSE
            ↓
        next(a)
            ↓
        yield 30
            ↓
          30
```

### 🧠 Shortcut

```text
next()
  ↓
Run
  ↓
yield
  ↓
Give value
  ↓
PAUSE
```

---

# 9️⃣ Your `while` Generator Example

Your notes use:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()
```

Now:

```python
print(next(a))
```

Output:

```text
0
```

Again:

```python
print(next(a))
```

Output:

```text
1
```

Again:

```python
print(next(a))
```

Output:

```text
2
```

---

# 🔟 Dry Run — Line by Line 🔍

Let's understand carefully.

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1
```

Then:

```python
a = generate()
```

At this point, `a` refers to the generator object.

Now:

```python
next(a)
```

Execution begins.

### Step 1

```python
i = 0
```

So:

```text
i → 0
```

### Step 2

Check:

```python
i <= 200
```

Becomes:

```text
0 <= 200
```

Result:

```text
True
```

### Step 3

Execute:

```python
yield i
```

Current `i`:

```text
0
```

Therefore generator gives:

```text
0
```

and pauses.

---

# 1️⃣1️⃣ What Happens on Second `next()`?

Call:

```python
next(a)
```

The generator continues from where it paused.

Next statement:

```python
i += 1
```

So:

```text
i = 0 + 1
```

Now:

```text
i = 1
```

Check:

```python
1 <= 200
```

True.

Then:

```python
yield i
```

gives:

```text
1
```

Pause again.

---

# 1️⃣2️⃣ Third `next()`

Again:

```python
next(a)
```

Continue:

```python
i += 1
```

Now:

```text
i = 2
```

Then:

```python
yield i
```

Output:

```text
2
```

So your code:

```python
print(next(a))
print(next(a))
print(next(a))
```

produces:

```text
0
1
2
```

---

# 1️⃣3️⃣ Generator Memory Idea 🧠

A useful beginner mental model is:

```text
a
│
▼
┌─────────────────────────┐
│ Generator               │
├─────────────────────────┤
│ Current position        │
│ Current local state     │
└─────────────────────────┘
```

After first `next()`:

```text
yield 0
  ↓
PAUSE
```

Later:

```text
next()
  ↓
Continue from pause
```

This ability to **pause and resume** is the key generator concept.

---

# 1️⃣4️⃣ Generator Using `for` Loop 🔁

Your notes contain:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

for value in a:
    print(value, end=" ")
```

Output starts:

```text
0 1 2 3 4 5 6 ...
```

and continues through:

```text
200
```

---

# 1️⃣5️⃣ How `for` Loop Helps

With `next()` you manually request values:

```python
next(a)
next(a)
next(a)
```

With:

```python
for value in a:
```

the loop repeatedly retrieves generated values for you until the generator is finished.

Beginner shortcut:

```text
next() → Manual 👤

for loop → Automatic 🔄
```

---

# 1️⃣6️⃣ Convert Generator to List 📋

Your notes do this manually:

```python
a = generate()

numbers = []

for value in a:
    numbers.append(value)

print(numbers)
```

Flow:

```text
Generator
   ↓
yield 0
   ↓
append(0)
   ↓
yield 1
   ↓
append(1)
   ↓
yield 2
   ↓
append(2)
   ↓
...
   ↓
List
```

Eventually:

```text
[0, 1, 2, 3, ..., 200]
```

---

# 1️⃣7️⃣ Important Memory Point ⭐

Your notes then check:

```python
print(sys.getsizeof(numbers))
```

But notice what happened:

```text
Generator
   ↓
Generate values
   ↓
Append every value
   ↓
Create List
```

Once you collect all generated values into a list, you are again storing those values in that list.

So the generator's main benefit is clearest when you **process values one at a time** rather than immediately collecting all of them.

---

# 1️⃣8️⃣ Wrong List Example ❌

Your notes contain:

```python
for i in range(1, 201):
    numbers = []
    numbers.append(i)

print(numbers)
```

Output:

```text
[200]
```

Why?

Because this line:

```python
numbers = []
```

is **inside the loop**.

Every iteration creates a fresh empty list.

Conceptually:

```text
i = 1
numbers = []
append(1)

↓ next iteration

i = 2
numbers = []   ← old contents replaced
append(2)

↓ next

i = 3
numbers = []
append(3)

...

i = 200
numbers = []
append(200)
```

Finally:

```text
[200]
```

---

# 1️⃣9️⃣ Correct Version ✅

Create the list **before** the loop.

```python
numbers = []

for i in range(1, 201):

    numbers.append(i)

print(numbers)
```

Now:

```text
numbers = []

i=1 → [1]

i=2 → [1,2]

i=3 → [1,2,3]

...

i=200 → [1,2,3,...,200]
```

### ⭐ Shortcut

```text
Want to KEEP previous values?

Create list OUTSIDE loop. ✅
```

---

# 2️⃣0️⃣ `return` vs `yield` ⚖️

| `return`                                | `yield`                        |
| --------------------------------------- | ------------------------------ |
| Used in normal functions                | Makes the function a generator |
| Returns a result and finishes that call | Produces a value and pauses    |
| Function execution ends at `return`     | Generator can continue later   |
| Normal function call                    | Generator object is created    |

Example with `return`:

```python
def test():

    return 10

    return 20
```

The first `return` ends that function call, so the second one is not reached.

Generator:

```python
def test():

    yield 10
    yield 20
```

Now:

```python
a = test()

print(next(a))
print(next(a))
```

Output:

```text
10
20
```

---

# 2️⃣1️⃣ Common Mistakes ❌

### ❌ Mistake 1 — Expecting generator call to print values

```python
print(generate())
```

This shows a generator object representation, not all generated values.

Use:

```python
a = generate()

print(next(a))
```

or:

```python
for value in generate():
    print(value)
```

---

### ❌ Mistake 2 — Forgetting `yield`

```python
def generate():

    i = 0

    while i <= 10:
        i += 1
```

That's not a generator because there is no `yield`.

---

### ❌ Mistake 3 — Infinite generator accidentally

Be careful with:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
```

Notice:

```python
i += 1
```

is missing.

So `i` remains:

```text
0
```

and the generator keeps yielding `0`.

Correct:

```python
def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1
```

---

# 2️⃣2️⃣ Advantages ✅

Generators are useful because they:

```text
✅ Produce values one at a time
✅ Can pause and resume
✅ Work naturally with loops
✅ Avoid requiring one big result collection first
✅ Are useful for sequences of values
```

---

# 2️⃣3️⃣ Disadvantages ⚠️

For a beginner, remember:

```text
❌ Generator logic can initially be harder to understand

❌ Values are consumed as you iterate

❌ You need list/tuple conversion if you specifically need
   a fully materialized collection

❌ Calling next() after the generator is finished
   leads to StopIteration
```

---

# 2️⃣4️⃣ Interview Questions & Answers 🎤

### Q1. What is a generator?

A generator is a special function that produces values one at a time using `yield`.

### Q2. Which keyword is used?

```python
yield
```

### Q3. What does `yield` do?

It produces a value and pauses the generator so execution can continue later.

### Q4. How do you retrieve the next value?

```python
next(generator)
```

### Q5. Can we use a `for` loop?

Yes.

```python
for value in generator:
    print(value)
```

### Q6. What is the major difference between `return` and `yield`?

`return` finishes the function call; `yield` produces a value and pauses the generator.

### Q7. What happens when a generator finishes?

Further manual `next()` calls raise:

```text
StopIteration
```

---

# 2️⃣5️⃣ MCQs 📝

### Q1. Which keyword creates generator behavior?

A. `return`
B. `yield`
C. `break`
D. `continue`

✅ **Answer: B — `yield`**

### Q2. Which function retrieves the next generator value?

A. `get()`
B. `yield()`
C. `next()`
D. `value()`

✅ **Answer: C — `next()`**

### Q3. What does `yield` do?

A. Deletes function
B. Produces a value and pauses
C. Stops Python
D. Creates class

✅ **Answer: B**

---

# 2️⃣6️⃣ Practice Program 💪

Try this yourself:

```python
def even_numbers():

    i = 2

    while i <= 20:

        yield i

        i += 2


a = even_numbers()

for value in a:

    print(value)
```

Expected:

```text
2
4
6
8
10
12
14
16
18
20
```

---

# 2️⃣7️⃣ Coding Challenge 🔥

Create a generator that produces:

```text
5
10
15
20
25
30
35
40
45
50
```

Hint:

```python
def generate():

    i = _____

    while i <= _____:

        yield _____

        i += _____
```

Try filling the blanks yourself.

---

# 🏆 CHAPTER 1 — GENERATOR FINAL SUMMARY

Remember this diagram:

```text
             GENERATOR FUNCTION
                    │
                    ▼
                  yield
                    │
                    ▼
             Generator Object
                    │
                    ▼
                 next()
                    │
                    ▼
               Get Value
                    │
                    ▼
                ⏸️ Pause
                    │
                    ▼
                 next()
                    │
                    ▼
               Continue
```

## ⚡ Generator Shortcuts

```text
Normal Function → return

Generator       → yield

Get next value  → next()

All values      → for loop

yield           → value + pause

next()          → resume execution
```

### ⭐ Most Important Interview Line

> **A generator is a special function that uses `yield` to produce values one at a time, pausing between values and continuing when the next value is requested.**

### 🧠 One-line memory trick

**`yield` = GIVE VALUE + PAUSE ⏸️**

Next is **📘 Chapter 2 — `filter()` + Lambda Functions**, using your even numbers, odd numbers, strings, and restaurant-rating examples.
===
# 📘 CHAPTER 2 — PYTHON `filter()` + LAMBDA FUNCTIONS

Now we continue with the next topic from your notes.

We will understand:

```text
🔍 filter()
🧠 How filter() works
⚙️ Filter object
📋 Converting filter → list
⚡ Lambda with filter()
🔢 Even / Odd filtering
🔤 String filtering
🍴 Dictionary filtering
❌ Common mistakes
🎤 Interview questions
🏆 Final shortcuts
```

---

# 1️⃣ What is `filter()`? 🔍

## ✅ Definition

`filter()` is a Python built-in function used to **select only the elements that satisfy a condition**.

### ⭐ Simple Definition

> `filter()` checks every element and keeps only the elements for which the condition is `True`.

Example:

Suppose:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

We want only:

```text
Even Numbers
↓
2, 4, 6
```

We can use:

```python
filter()
```

---

# 2️⃣ Why Do We Need `filter()`? 🤔

Imagine we have:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

But we only need even numbers.

Without `filter()`:

```python
result = []

for num in numbers:

    if num % 2 == 0:
        result.append(num)

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

This works.

But your notes show another way:

```python
result = list(
    filter(even, numbers)
)
```

This expresses the operation as:

```text
Take numbers
    ↓
Check condition
    ↓
Keep matching numbers
```

---

# 3️⃣ Real-Life Example 🌍

Imagine a restaurant application.

Restaurants:

```text
ABC → ⭐ 4.8
EFG → ⭐ 3.5
XYZ → ⭐ 4.9
PQR → ⭐ 4.2
```

Requirement:

> Show only restaurants with ratings greater than `4.5`.

Think:

```text
All Restaurants
       ↓
Check Rating
       ↓
rating > 4.5 ?
   /         \
 YES          NO
  ↓            ↓
KEEP         REMOVE
```

Result:

```text
ABC → 4.8 ✅
XYZ → 4.9 ✅
```

That's exactly the type of problem `filter()` handles.

---

# 4️⃣ `filter()` Syntax 📝

```python
filter(function, iterable)
```

### Two important parts

```text
filter(function, iterable)
       ↑          ↑
       │          │
    condition    data
```

Example:

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
Input Data
```

---

# 5️⃣ Your First `filter()` Example

From your notes:

```python
numbers = [1,2,3,4,5,6,7,8,9]


def even(x):

    return x % 2 == 0


result = filter(even, numbers)

print(result)
```

Notice:

```python
print(result)
```

doesn't directly print:

```text
[2, 4, 6, 8]
```

Instead, it displays a `filter` object representation.

---

# 6️⃣ Why Does `filter()` Return a Filter Object? ⚙️

Think of it like:

```text
numbers
   │
   ▼
filter(even, numbers)
   │
   ▼
Filter Object
```

To see the selected values as a list, your notes use:

```python
list(...)
```

So:

```python
result = list(
    filter(even, numbers)
)
```

Output:

```text
[2, 4, 6, 8]
```

---

# 7️⃣ How Does `filter()` Work? 🔄

Code:

```python
numbers = [1,2,3,4,5,6,7,8,9]


def even(x):
    return x % 2 == 0


result = list(
    filter(even, numbers)
)
```

Flow:

```text
numbers
   ↓
1 2 3 4 5 6 7 8 9
   ↓
even(x)
   ↓
True / False
   ↓
Keep only True values
   ↓
2 4 6 8
```

---

# 8️⃣ Dry Run — Line by Line 🔍

Let's take:

```python
numbers = [1, 2, 3, 4]
```

Function:

```python
def even(x):
    return x % 2 == 0
```

Python checks each value.

### Value 1

```python
even(1)
```

Inside:

```python
1 % 2 == 0
```

Result:

```text
False ❌
```

So `1` is not selected.

---

### Value 2

```python
even(2)
```

Check:

```text
2 % 2 == 0

0 == 0

True ✅
```

Keep:

```text
2
```

---

### Value 3

```text
3 % 2 == 0
     ↓
False ❌
```

Don't keep `3`.

---

### Value 4

```text
4 % 2 == 0
     ↓
True ✅
```

Keep `4`.

Final:

```text
[2, 4]
```

---

# 9️⃣ Easy Memory Diagram 🧠

```text
          [1, 2, 3, 4]
                 │
                 ▼
              filter()
                 │
                 ▼
              even(x)
                 │
       ┌─────────┴─────────┐
       │                   │
     True                 False
       │                   │
       ▼                   ▼
     KEEP                REMOVE
       │
       ▼
     [2, 4]
```

### ⭐ Shortcut

> `filter()` = **Condition True → KEEP**

---

# 🔟 What is Lambda? ⚡

Your notes then replace the normal `even()` function with a lambda.

## ✅ Definition

A lambda is a **small anonymous function** written using the `lambda` keyword.

Anonymous means:

> A function that can be written without defining it with the normal `def` syntax.

---

# 1️⃣1️⃣ Normal Function vs Lambda

Normal function:

```python
def even(x):

    return x % 2 == 0
```

Lambda:

```python
lambda x: x % 2 == 0
```

Both represent the same condition here.

### Easy comparison

```text
NORMAL FUNCTION

def even(x):
    return x % 2 == 0


LAMBDA

lambda x: x % 2 == 0
```

---

# 1️⃣2️⃣ Lambda Syntax 📝

```python
lambda arguments: expression
```

Example:

```python
lambda x: x * 2
```

Think:

```text
lambda
  ↓
Create small function

x
 ↓
Input

:
 ↓
Separate arguments and expression

x * 2
 ↓
Result expression
```

---

# 1️⃣3️⃣ Simple Lambda Example

Normal:

```python
def square(x):
    return x * x
```

Call:

```python
print(square(5))
```

Output:

```text
25
```

Lambda equivalent:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

---

# 1️⃣4️⃣ `filter()` + Lambda ⭐⭐⭐

This is the main combination from your notes.

Instead of:

```python
def even(x):
    return x % 2 == 0


result = list(
    filter(even, numbers)
)
```

write:

```python
result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)
```

Short version:

```python
result = list(filter(lambda x: x % 2 == 0, numbers))
```

---

# 1️⃣5️⃣ Understand Every Part 🧠

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

Break it into pieces:

```text
numbers
   ↓
Input Data

lambda x: x % 2 == 0
   ↓
Condition

filter(...)
   ↓
Select matching values

list(...)
   ↓
Convert result to list
```

### ⭐ Master Formula

```text
DATA
 ↓
LAMBDA CONDITION
 ↓
FILTER
 ↓
LIST
 ↓
RESULT
```

---

# 1️⃣6️⃣ Even Numbers Example 🔢

Your code:

```python
numbers = [1,2,3,4,5,6,7,8,9]

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
[2, 4, 6, 8]
```

Why?

```text
1 → False ❌
2 → True  ✅
3 → False ❌
4 → True  ✅
5 → False ❌
6 → True  ✅
7 → False ❌
8 → True  ✅
9 → False ❌
```

Result:

```text
[2, 4, 6, 8]
```

---

# 1️⃣7️⃣ Odd Numbers Example 🔢

Your notes:

```python
numbers = [1,2,3,4,5,6,7,8,9]

result = list(
    filter(
        lambda x: x % 2 != 0,
        numbers
    )
)

print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

### Shortcut

Even:

```python
x % 2 == 0
```

Odd:

```python
x % 2 != 0
```

Remember:

```text
Even → remainder = 0

Odd  → remainder ≠ 0
```

---

# 1️⃣8️⃣ String Filtering 🔤

Your notes:

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

Condition:

```python
x.startswith("a")
```

Check:

```text
apple
 ↓
starts with lowercase "a"
 ↓
True ✅


America
 ↓
starts with uppercase "A"
 ↓
False ❌


andhra
 ↓
starts with lowercase "a"
 ↓
True ✅


banana
 ↓
False ❌


cat
 ↓
False ❌
```

Output:

```text
['apple', 'andhra']
```

---

# 1️⃣9️⃣ Important String Point ⭐

Python strings are case-sensitive here.

```text
"a" ≠ "A"
```

Therefore:

```python
"America".startswith("a")
```

is:

```text
False
```

If you wanted to treat uppercase and lowercase the same, that would require an additional normalization step; that is beyond what your current notes demonstrate.

---

# 2️⃣0️⃣ Dictionary Filtering 🍴

This is an important real-time example from your notes.

```python
restaurants = [
    {"name": "abc", "ratings": 4.8},
    {"name": "efg", "ratings": 3.5},
    {"name": "xyz", "ratings": 4.9},
    {"name": "pqr", "ratings": 4.2}
]
```

Requirement:

```text
Show restaurants
whose rating > 4.5
```

Code:

```python
result = list(
    filter(
        lambda x: x["ratings"] > 4.5,
        restaurants
    )
)

print(result)
```

---

# 2️⃣1️⃣ Dry Run — Restaurant Example 🔍

First dictionary:

```python
{
    "name": "abc",
    "ratings": 4.8
}
```

Here `x` refers to that dictionary.

Condition:

```python
x["ratings"] > 4.5
```

becomes:

```text
4.8 > 4.5
   ↓
True ✅
```

Keep it.

---

Second:

```text
EFG → 3.5

3.5 > 4.5
   ↓
False ❌
```

Remove it.

---

Third:

```text
XYZ → 4.9

4.9 > 4.5
   ↓
True ✅
```

Keep it.

---

Fourth:

```text
PQR → 4.2

4.2 > 4.5
   ↓
False ❌
```

Remove it.

Result contains the `abc` and `xyz` dictionaries.

---

# 2️⃣2️⃣ Why Is `x` a Dictionary? 🧠

Look at:

```python
filter(
    lambda x: x["ratings"] > 4.5,
    restaurants
)
```

`restaurants` is a:

```text
List
```

Each element inside it is a:

```text
Dictionary
```

Therefore, one by one:

```text
x = {"name": "abc", "ratings": 4.8}

x = {"name": "efg", "ratings": 3.5}

x = {"name": "xyz", "ratings": 4.9}

x = {"name": "pqr", "ratings": 4.2}
```

That's why this works:

```python
x["ratings"]
```

---

# 2️⃣3️⃣ Real-Time Examples 🌍

The same filtering idea can represent situations like:

```text
👨‍💼 Employees
salary > required amount

🎓 Students
marks >= pass mark

🛒 Products
price within a condition

🍴 Restaurants
ratings > 4.5
```

General pattern:

```python
list(
    filter(
        lambda item: condition,
        data
    )
)
```

---

# 2️⃣4️⃣ Common Mistake From Your Notes ❌

You wrote:

```python
list = [1,2,3]
```

This is a problem because:

```text
list
```

is also the name of Python's built-in `list()`.

Normally:

```python
list(filter(...))
```

uses the built-in `list`.

But after:

```python
list = [1,2,3]
```

the name `list` now refers to your list object in that scope.

Then:

```python
list(filter(even, list))
```

can produce:

```text
TypeError:
'list' object is not callable
```

---

# 2️⃣5️⃣ Correct Way ✅

Don't use:

```python
list = [1,2,3]
```

Use:

```python
numbers = [1,2,3]
```

Then:

```python
result = list(
    filter(even, numbers)
)
```

### ⭐ Important Naming Rule

Avoid using built-in names as your variable names.

Examples:

```text
❌ list
❌ str
❌ int
❌ dict
❌ sum
```

Prefer descriptive names:

```text
✅ numbers
✅ students
✅ restaurants
✅ products
✅ employees
```

---

# 2️⃣6️⃣ `filter()` vs Normal Loop ⚖️

### Normal Loop

```python
result = []

for num in numbers:

    if num % 2 == 0:
        result.append(num)
```

### `filter()`

```python
result = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)
```

For beginners, the loop version can be easier to trace line by line, while the `filter()` version expresses the filtering operation compactly.

---

# 2️⃣7️⃣ Lambda vs Normal Function ⚖️

| Normal Function                           | Lambda                                      |
| ----------------------------------------- | ------------------------------------------- |
| Uses `def`                                | Uses `lambda`                               |
| Has a function name when defined normally | Often used anonymously                      |
| Can contain multiple statements           | Lambda body is a single expression          |
| Good for larger logic                     | Good for small expressions                  |
| Can use explicit `return`                 | Expression result is returned automatically |

Example:

```python
def even(x):
    return x % 2 == 0
```

vs:

```python
lambda x: x % 2 == 0
```

---

# 2️⃣8️⃣ `filter()` vs Lambda ⚠️

Don't confuse them.

`filter()` and lambda are **not the same thing**.

```text
filter()
   ↓
Selects elements

lambda
   ↓
Creates a small function
```

They are often used together:

```python
filter(
    lambda x: condition,
    data
)
```

Think:

> **Lambda tells `filter()` WHAT to check.**

---

# 2️⃣9️⃣ Interview Questions & Answers 🎤

### Q1. What is `filter()`?

`filter()` selects elements from an iterable based on a condition function.

### Q2. What is the syntax?

```python
filter(function, iterable)
```

### Q3. What does the condition need to indicate?

Whether each item should be kept or not, typically through a truthy or falsy result.

### Q4. Why do we use `list()` in your examples?

Because `filter()` returns a filter object, and `list()` collects its selected values into a list.

### Q5. What is lambda?

A lambda is a small anonymous function created with the `lambda` keyword.

### Q6. Lambda syntax?

```python
lambda arguments: expression
```

### Q7. Can lambda work with `filter()`?

Yes.

```python
filter(
    lambda x: x % 2 == 0,
    numbers
)
```

### Q8. What happens when the condition is `True`?

That element is kept by `filter()`.

### Q9. What happens when it is `False`?

That element is not included.

---

# 3️⃣0️⃣ MCQs 📝

### Q1. Which function selects values based on a condition?

A. `map()`
B. `filter()`
C. `print()`
D. `input()`

✅ **Answer: B**

### Q2. What is the lambda keyword?

A. `def`
B. `function`
C. `lambda`
D. `yield`

✅ **Answer: C**

### Q3. Which selects even numbers?

```text
A. x % 2 == 0
B. x % 2 != 0
C. x / 2
D. x + 2
```

✅ **Answer: A**

### Q4. `filter()` returns what in your examples?

A. String
B. Filter object
C. Dictionary
D. Integer

✅ **Answer: B**

---

# 3️⃣1️⃣ Practice Programs 💪

Practice these based on the same pattern:

```text
1️⃣ Numbers greater than 10

2️⃣ Numbers less than 50

3️⃣ Even numbers

4️⃣ Odd numbers

5️⃣ Words starting with "a"

6️⃣ Restaurants rating > 4.5

7️⃣ Students marks >= 35

8️⃣ Employees salary > 30000
```

Example starting data:

```python
numbers = [5, 10, 15, 20, 25, 30]
```

Try:

```python
result = list(
    filter(
        lambda x: x > 10,
        numbers
    )
)

print(result)
```

Expected:

```text
[15, 20, 25, 30]
```

---

# 🏆 CHAPTER 2 — FINAL SUMMARY

Remember this:

```text
              DATA
               │
               ▼
             filter()
               │
               ▼
         Condition Function
               │
        ┌──────┴──────┐
        │             │
      True          False
        │             │
        ▼             ▼
      KEEP          REMOVE
        │
        ▼
    Filter Object
        │
        ▼
      list()
        │
        ▼
      RESULT
```

## ⚡ Final Shortcuts

```text
🔍 filter() → Select data

⚡ lambda → Small function

✅ True → Keep

❌ False → Remove

📋 list() → Collect filter results into list

🔢 Even → x % 2 == 0

🔢 Odd → x % 2 != 0

🔤 Starts with a → x.startswith("a")

⭐ Rating → x["ratings"] > 4.5
```

### ⭐ Master Syntax

```python
result = list(
    filter(
        lambda x: condition,
        data
    )
)
```

### 🧠 One-line memory trick

> **`filter()` = CHECK → TRUE? → KEEP ✅**

And:

> **`lambda` = small function written in one expression ⚡**

**Next: 📘 Chapter 3 — Python Decorators**: function objects → function inside function → wrapper → manual decoration → `@decorator` → timer decorator → `*args` → `**kwargs` → dry run → real-time uses → interview shortcuts.
===
# 📘 CHAPTER 3 — PYTHON DECORATORS

Now we continue with **Decorators** from your notes.

Decorators can look confusing at first because they depend on understanding **functions as objects**, **nested functions**, and **returning functions**. So we'll build the concept slowly.

---

# 1️⃣ What is a Decorator? 🎁

## ✅ Definition

A **decorator is a function that adds extra functionality to another function without changing that function's original code.**

### 🧠 Simple English

Suppose you already have:

```python
def greet():
    print("Hello User")
```

Output:

```text
Hello User
```

Now you want:

```text
************************
Hello User
************************
```

You could edit `greet()`.

But with a decorator, you can add the extra behavior **around** `greet()`.

### ⭐ Easy definition

> **Decorator = Add extra functionality to an existing function.**

---

# 2️⃣ Why Do We Need Decorators? 🤔

Suppose your application has:

```text
login()
payment()
shopping()
message()
register()
```

You want to measure how long each function takes.

Without a decorator, you may repeat:

```python
start = time.time()

# function code

end = time.time()

print(end - start)
```

in many places.

With a decorator:

```python
@timer
def message():
    ...
```

You can reuse the timer logic.

So the main idea is:

```text
Existing Function
       +
Extra Functionality
       ↓
Decorated Function
```

---

# 3️⃣ Real-Life Example 🌍

Think about a **gift**. 🎁

You have the original item:

```text
📦 Gift
```

You add wrapping:

```text
🎀 Wrapper
    ↓
📦 Gift
```

The gift is still inside.

The wrapper adds something around it.

Similarly:

```text
Decorator
    ↓
Wrapper Function
    ↓
Original Function
```

This is why the inner function in your notes is named:

```python
wrapper()
```

or:

```python
wrap()
```

---

# 4️⃣ Before Decorators — Important Concept ⭐

To understand decorators, first understand:

> **Functions are objects in Python.**

Your earlier notes demonstrate this idea by returning one function from another.

Example:

```python
def fun():

    def add(x, y):
        print(x + y)

    return add
```

Then:

```python
a = fun()
```

And:

```python
a(10, 20)
```

Output:

```text
30
```

This concept is very important for decorators.

---

# 5️⃣ Function Returning Another Function 🔄

From your notes:

```python
def add(a, b):

    print(a + b)

    def mul(e, f):
        print(e * f)

    return mul


a = add(30, 40)

a(3, 4)
```

Let's understand this carefully.

---

# 6️⃣ Dry Run 🔍

First:

```python
a = add(30, 40)
```

Python enters:

```python
def add(a, b):
```

Values:

```text
a = 30
b = 40
```

Execute:

```python
print(a + b)
```

Result:

```text
70
```

Then Python creates:

```python
def mul(e, f):
    print(e * f)
```

Finally:

```python
return mul
```

Notice:

```python
return mul
```

not:

```python
return mul()
```

We are returning the **function itself**.

Therefore:

```python
a = add(30, 40)
```

means conceptually:

```text
a
↓
mul function
```

Now:

```python
a(3, 4)
```

is effectively calling that returned function with:

```text
e = 3
f = 4
```

So:

```text
3 * 4
 ↓
12
```

Output:

```text
70
12
```

---

# 7️⃣ Memory Diagram 🧠

Think of it like:

```text
add(30,40)
     │
     ├── print(70)
     │
     └── return mul
              │
              ▼
              a
              │
              ▼
          a(3,4)
              │
              ▼
           mul(3,4)
              │
              ▼
              12
```

This idea leads directly to decorators.

---

# 8️⃣ Simple Decorator 🎁

Your notes:

```python
def dec(func):

    def wrap():

        print("****************************************")

        func()

        print("****************************************")

    return wrap
```

This is your decorator.

Let's understand every line.

---

# 9️⃣ Decorator Syntax 📝

General beginner structure:

```python
def decorator(function):

    def wrapper():

        # before

        function()

        # after

    return wrapper
```

Think:

```text
decorator
    │
    ├── receives original function
    │
    └── creates wrapper
             │
             ├── before code
             │
             ├── original function
             │
             └── after code
```

---

# 🔟 Original Function

Your notes use:

```python
def greet():
    print("Hello User!!!")
```

Normal call:

```python
greet()
```

Output:

```text
Hello User!!!
```

No decorator yet.

---

# 1️⃣1️⃣ Manual Decoration ⭐

Your notes then do:

```python
a = dec(greet)

a()
```

This is extremely important.

Let's understand:

```python
dec(greet)
```

You are passing the `greet` function into:

```python
dec()
```

So inside:

```python
def dec(func):
```

we can think:

```text
func → greet
```

---

# 1️⃣2️⃣ What Does `dec()` Return?

Inside:

```python
def dec(func):

    def wrap():

        print("****************************************")

        func()

        print("****************************************")

    return wrap
```

It returns:

```python
wrap
```

Therefore:

```python
a = dec(greet)
```

means:

```text
a
↓
wrap
```

Then:

```python
a()
```

calls:

```python
wrap()
```

---

# 1️⃣3️⃣ Full Dry Run 🔍

Code:

```python
a = dec(greet)
a()
```

### Step 1

```python
dec(greet)
```

Now:

```text
func = greet
```

### Step 2

Python defines:

```python
wrap()
```

### Step 3

Decorator returns:

```python
return wrap
```

Therefore:

```text
a = wrap
```

### Step 4

Execute:

```python
a()
```

which calls `wrap()`.

### Step 5

First:

```python
print("****************************************")
```

Output:

```text
****************************************
```

### Step 6

Then:

```python
func()
```

Remember:

```text
func = greet
```

So effectively:

```python
greet()
```

Output:

```text
Hello User!!!
```

### Step 7

Finally:

```python
print("****************************************")
```

Final output:

```text
****************************************
Hello User!!!
****************************************
```

---

# 1️⃣4️⃣ Flow Diagram 🔄

```text
             greet
               │
               ▼
          dec(greet)
               │
               ▼
         func = greet
               │
               ▼
        Create wrap()
               │
               ▼
         return wrap
               │
               ▼
               a
               │
             a()
               │
               ▼
           wrap()
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
   Before    greet()   After
```

### 🧠 Shortcut

> **Decorator receives function → creates wrapper → returns wrapper.**

---

# 1️⃣5️⃣ `@decorator` Syntax ⭐⭐⭐

Instead of manually writing:

```python
a = dec(greet)
a()
```

Python provides decorator syntax:

```python
@dec
def message():
    print("Welcome to Python Decorators")
```

Then:

```python
message()
```

Your notes use exactly this pattern.

---

# 1️⃣6️⃣ What Does `@dec` Mean?

This:

```python
@dec
def message():
    print("Welcome")
```

is essentially decorator syntax for applying `dec` to `message`.

Beginner mental model:

```text
message
   ↓
dec(message)
   ↓
wrapper returned
   ↓
message now calls decorated behavior
```

### ⭐ Interview Shortcut

```text
@dec
   ↓
Apply decorator dec
to the function below it
```

---

# 1️⃣7️⃣ Multiple Functions Using Same Decorator ♻️

One important advantage is reusability.

Example based on your notes:

```python
def dec(func):

    def wrap():

        print("****************")

        func()

        print("****************")

    return wrap
```

Now:

```python
@dec
def message():
    print("Hello")
```

And:

```python
@dec
def display():
    print("Displaying...")
```

Both can use the same decorator.

```python
message()
display()
```

This is code reuse.

---

# 1️⃣8️⃣ Problem — What About Function Arguments? 🤔

Our first wrapper was:

```python
def wrap():
```

That works for:

```python
def message():
```

because `message()` requires no arguments.

But what about:

```python
def add(a, b):
    print(a + b)
```

We need to pass:

```text
a
b
```

through the wrapper.

This is where your notes use:

```python
*args
```

and:

```python
**kwargs
```

---

# 1️⃣9️⃣ What is `*args`? 📦

Simple definition:

> `*args` allows a function to receive multiple positional arguments.

Example:

```python
def test(*args):
    print(args)
```

Call:

```python
test(10, 20, 30)
```

Conceptually:

```text
args
 ↓
(10, 20, 30)
```

---

# 2️⃣0️⃣ What is `**kwargs`? 📦

Simple definition:

> `**kwargs` allows a function to receive multiple keyword arguments.

Example:

```python
def test(**kwargs):
    print(kwargs)
```

Call:

```python
test(
    name="pizza",
    price=500
)
```

Conceptually:

```text
kwargs
   ↓
{
 "name": "pizza",
 "price": 500
}
```

---

# 2️⃣1️⃣ `*args` vs `**kwargs` ⚖️

| `*args`              | `**kwargs`               |
| -------------------- | ------------------------ |
| Positional arguments | Keyword arguments        |
| Collected as tuple   | Collected as dictionary  |
| `add(10,20)`         | `shopping(name="pizza")` |

### 🧠 Shortcut

```text
*args
 ↓
Values by POSITION
 ↓
Tuple


**kwargs
 ↓
Values by KEYWORD
 ↓
Dictionary
```

---

# 2️⃣2️⃣ Decorator with Arguments ⭐

Your notes:

```python
import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        func(*args, **kwargs)

        print(
            "Time taken to execute by this",
            func.__name__,
            time.time() - start,
            "secs"
        )

    return wrapper
```

Then:

```python
@timer
def add(a, b):

    print(a + b)

    time.sleep(3)
```

Call:

```python
add(2, 4)
```

---

# 2️⃣3️⃣ Dry Run of `add(2, 4)` 🔍

Because of:

```python
@timer
```

the call goes through the wrapper.

You call:

```python
add(2, 4)
```

The wrapper receives:

```text
args = (2, 4)

kwargs = {}
```

Then:

```python
start = time.time()
```

stores the starting time.

Next:

```python
func(*args, **kwargs)
```

Here:

```text
func → original add function
```

So conceptually:

```python
add(2, 4)
```

runs.

Inside:

```python
print(a + b)
```

Output:

```text
6
```

Then:

```python
time.sleep(3)
```

waits about 3 seconds.

After the function finishes:

```python
time.time() - start
```

calculates elapsed time.

---

# 2️⃣4️⃣ Timer Flow Diagram ⏱️

```text
          add(2,4)
              │
              ▼
           wrapper
              │
              ▼
       Save start time
              │
              ▼
         Original add
              │
              ▼
           2 + 4
              │
              ▼
              6
              │
              ▼
        sleep(3)
              │
              ▼
       Current time
              │
              ▼
Current time - Start time
              │
              ▼
       Execution Time
```

---

# 2️⃣5️⃣ What is `func.__name__`? 🏷️

Your code contains:

```python
func.__name__
```

This gives the name of the function.

For example:

```python
def message():
    pass
```

Then:

```python
print(message.__name__)
```

Output:

```text
message
```

So your timer can print which function was executed.

---

# 2️⃣6️⃣ Decorator with `**kwargs` 🛒

Your notes:

```python
@timer
def shopping(**values):

    print(values)
```

Call:

```python
shopping(
    name="pizza",
    price=500
)
```

Inside `shopping()`:

```text
values
   ↓
{
    "name": "pizza",
    "price": 500
}
```

The decorator's:

```python
wrapper(*args, **kwargs)
```

can receive those keyword arguments and forward them with:

```python
func(*args, **kwargs)
```

---

# 2️⃣7️⃣ Why Use Both `*args` and `**kwargs`? ⭐

Because then the wrapper can handle many different function signatures.

```python
def wrapper(*args, **kwargs):
```

can forward:

```python
func(*args, **kwargs)
```

This makes the decorator much more reusable.

### 🧠 Master Shortcut

```text
*args    → positional arguments 📦

**kwargs → keyword arguments 📦

Both     → flexible wrapper 🔥
```

---

# 2️⃣8️⃣ Decorator with Return Value 🔙

Your earlier notes also contain:

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before Function")

        result = func(*args, **kwargs)

        print("After Function")

        return result

    return wrapper
```

Then:

```python
@decorator
def square(num):

    return num * num
```

Call:

```python
print(square(5))
```

---

# 2️⃣9️⃣ Why `return result` Matters ⭐

Original function:

```python
def square(num):
    return num * num
```

For:

```text
num = 5
```

result:

```text
25
```

Inside wrapper:

```python
result = func(*args, **kwargs)
```

means:

```text
result = 25
```

Then:

```python
return result
```

sends `25` back to the caller.

### Flow

```text
square(5)
    ↓
wrapper
    ↓
Original square(5)
    ↓
25
    ↓
result = 25
    ↓
return result
    ↓
25
```

---

# 3️⃣0️⃣ Common Mistake — Forgetting Return ❌

Suppose the original function returns something:

```python
def square(x):
    return x * x
```

If your wrapper only does:

```python
func(*args, **kwargs)
```

but does not return that result, the decorated function won't pass that original return value back to its caller.

A better pattern for return-value functions is:

```python
def wrapper(*args, **kwargs):

    result = func(*args, **kwargs)

    return result
```

---

# 3️⃣1️⃣ Common Mistakes ❌

### ❌ Mistake 1 — Calling instead of passing

These are different:

```python
dec(greet)
```

and:

```python
dec(greet())
```

For your decorator pattern, you want to pass the function itself:

```python
dec(greet)
```

---

### ❌ Mistake 2 — Forgetting to return wrapper

Wrong:

```python
def dec(func):

    def wrapper():
        func()
```

Your decorator needs:

```python
return wrapper
```

in this pattern.

---

### ❌ Mistake 3 — Wrapper doesn't accept arguments

```python
def wrapper():
```

will not work for a decorated function that needs arguments if the wrapper must receive and forward them.

Use:

```python
def wrapper(*args, **kwargs):
```

---

### ❌ Mistake 4 — Not forwarding arguments

If wrapper receives:

```python
*args, **kwargs
```

you normally forward them:

```python
func(*args, **kwargs)
```

---

# 3️⃣2️⃣ Advantages ✅

Decorators help with:

```text
✅ Code reuse

✅ Adding extra functionality

✅ Avoiding repeated wrapper logic

✅ Keeping the main function focused

✅ Applying the same behavior to multiple functions
```

Your timer decorator is a good example:

```text
message()
add()
shopping()
```

can all use reusable timing logic.

---

# 3️⃣3️⃣ Disadvantages ⚠️

For beginners:

```text
❌ Can be confusing initially

❌ Nested functions make execution flow harder to trace

❌ Debugging can feel harder

❌ Arguments and return values must be handled carefully
```

---

# 3️⃣4️⃣ Decorator vs Normal Function ⚖️

| Normal Function               | Decorator                               |
| ----------------------------- | --------------------------------------- |
| Performs its own task         | Wraps/adds behavior to another function |
| Called normally               | Often applied with `@name`              |
| Doesn't need another function | Decorator receives a function           |
| Example: `add()`              | Example: `timer()`                      |

---

# 3️⃣5️⃣ Interview Questions & Answers 🎤

### Q1. What is a decorator?

A decorator is a function that adds extra functionality to another function without directly changing that function's original code.

### Q2. What is decorator syntax?

```python
@decorator_name
def function():
    pass
```

### Q3. What is a wrapper function?

It is the inner function that surrounds the call to the original function with additional behavior.

### Q4. Why use `*args`?

To accept positional arguments.

### Q5. Why use `**kwargs`?

To accept keyword arguments.

### Q6. What does `*args` collect?

A tuple of positional arguments.

### Q7. What does `**kwargs` collect?

A dictionary of keyword arguments.

### Q8. Why return `wrapper`?

So the decorator provides the wrapped function behavior.

### Q9. What does `func.__name__` provide?

The function's name.

### Q10. Give one example from your notes.

A timer decorator that measures function execution time.

---

# 3️⃣6️⃣ MCQs 📝

### Q1. Which symbol is used for decorator syntax?

A. `#`
B. `$`
C. `@`
D. `&`

✅ **Answer: C — `@`**

### Q2. `*args` stores arguments as?

A. Dictionary
B. Tuple
C. Set
D. String

✅ **Answer: B — Tuple**

### Q3. `**kwargs` stores arguments as?

A. Tuple
B. List
C. Dictionary
D. Integer

✅ **Answer: C — Dictionary**

### Q4. Which gets the function name?

A. `func.name`
B. `func.__name__`
C. `func.getname()`
D. `name(func)`

✅ **Answer: B**

### Q5. Which module is used by your timer decorator?

A. `sys`
B. `math`
C. `time`
D. `random`

✅ **Answer: C**

---

# 3️⃣7️⃣ Practice Program 💪

Try creating this:

```python
def star(func):

    def wrapper():

        print("****************")

        func()

        print("****************")

    return wrapper


@star
def welcome():

    print("Welcome Ramesh")


welcome()
```

Expected:

```text
****************
Welcome Ramesh
****************
```

---

# 3️⃣8️⃣ Coding Challenge 🔥

Create a decorator that changes:

```text
Login Successful
```

into:

```text
====================
Login Successful
====================
```

Hint:

```python
def design(func):

    def wrapper():

        # print line

        func()

        # print line

    return wrapper


@design
def login():

    print("Login Successful")


login()
```

---

# 🏆 CHAPTER 3 — DECORATORS FINAL SUMMARY

## 🔥 Complete Flow

```text
          Original Function
                 │
                 ▼
             Decorator
                 │
                 ▼
        Receives Function
                 │
                 ▼
          Creates Wrapper
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
     Before   Original   After
               Function
                 │
                 ▼
         Return Wrapper
                 │
                 ▼
        Decorated Function
```

## ⚡ Interview Shortcuts

```text
🎁 Decorator
   → Adds extra functionality

📦 func
   → Original function

🎀 wrapper
   → Wraps original function

@decorator
   → Apply decorator

*args
   → Positional arguments
   → Tuple

**kwargs
   → Keyword arguments
   → Dictionary

func(*args, **kwargs)
   → Forward arguments

return result
   → Preserve function result

func.__name__
   → Function name

time.time()
   → Current time used for timing
```

## 🧠 Most Important Formula

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        # Before

        result = func(*args, **kwargs)

        # After

        return result

    return wrapper
```

Use:

```python
@decorator
def function():
    pass
```

### ⭐ One-line memory trick

> **Decorator = RECEIVE FUNCTION → WRAP FUNCTION → ADD EXTRA WORK → RETURN WRAPPER 🎁**

### 🔗 All 3 Chapters Connection

```text
CHAPTER 1
⚙️ Generator
→ yield
→ one value at a time


CHAPTER 2
🔍 filter()
→ check condition
→ keep matching values

⚡ lambda
→ small anonymous function


CHAPTER 3
🎁 Decorator
→ wrap a function
→ add extra functionality
```

**Generator → `yield` ⚙️ | Filter → Select 🔍 | Lambda → Small Function ⚡ | Decorator → Add Functionality 🎁**
