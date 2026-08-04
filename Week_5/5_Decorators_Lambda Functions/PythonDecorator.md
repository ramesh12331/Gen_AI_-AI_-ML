# 📘 CHAPTER 4 — PYTHON DECORATORS

## 🌱 Beginner → Step-by-Step → Interview Level

Now we continue from **Chapter 3: First-Class Functions**.

Chapter 3 taught us this important concept:

```python
def outer():

    def inner():
        print("Hello")

    return inner

a = outer()
a()
```

This idea is the **foundation of decorators**.

---

# 1. ✅ What is a Decorator?

### Simple Definition

A **decorator is a function that adds extra functionality to another function without changing the original function's code.**

### 🎤 Interview Definition

> A decorator is a function that takes another function as an argument, adds or modifies its behavior, and returns a function.

The important idea is:

```text
Original Function
       ↓
   Decorator
       ↓
Extra Functionality
       ↓
Original Function
       ↓
Extra Functionality
```

---

# 2. 🤔 Why Do We Need Decorators?

Suppose we have:

```python
def greet():
    print("Hello User")

greet()
```

Output:

```text
Hello User
```

Now imagine we want:

```text
************************
Hello User
************************
```

One way is to change `greet()`:

```python
def greet():
    print("************************")
    print("Hello User")
    print("************************")
```

But what if we have:

```python
greet()
display()
message()
welcome()
login()
```

and want the same extra functionality around all of them?

We would repeat code.

Instead, we can create **one decorator**.

---

# 3. 🌍 Real-Life Example

Think about a gift.

```text
Original Gift
     ↓
Gift Wrapper
     ↓
Wrapped Gift
```

The gift is still the same gift.

The wrapper adds something around it.

Similarly:

```text
Original Function
       ↓
   Decorator
       ↓
Decorated Function
```

---

# 4. ✅ Basic Decorator Syntax

```python
def decorator(func):

    def wrapper():

        # Before function

        func()

        # After function

    return wrapper
```

Then:

```python
@decorator
def greet():
    print("Hello")
```

Call:

```python
greet()
```

---

# 5. ⭐ Understand `func` and `wrapper`

This is very important.

```python
def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper
```

Here:

### `func`

represents the original function.

### `wrapper`

is the new function that adds extra functionality.

### `return wrapper`

returns the wrapper function.

---

# 6. 🔥 Your Simple Decorator Example

From your notes:

```python
def dec(func):

    def wrap():

        print("****************************************")

        func()

        print("****************************************")

    return wrap
```

Original function:

```python
def greet():
    print("Hello User!!!")
```

Normally:

```python
greet()
```

Output:

```text
Hello User!!!
```

---

# 7. 🔥 Manual Decoration

You wrote:

```python
a = dec(greet)

a()
```

Output:

```text
****************************************
Hello User!!!
****************************************
```

This is the easiest way to understand decorators.

---

# 8. 🔍 Dry Run — Very Important

Consider:

```python
def dec(func):

    def wrap():

        print("********")

        func()

        print("********")

    return wrap


def greet():
    print("Hello")


a = dec(greet)

a()
```

Let's execute line by line.

### Step 1

Python creates:

```python
dec
```

### Step 2

Python creates:

```python
greet
```

### Step 3

Python executes:

```python
a = dec(greet)
```

Here we are passing:

```python
greet
```

as an argument.

So conceptually:

```text
func = greet
```

---

# 9. What Happens Inside `dec()`?

Python enters:

```python
def dec(func):
```

Now:

```text
func
 ↓
greet function
```

Then Python creates:

```python
def wrap():
```

Finally:

```python
return wrap
```

The `wrap` function is returned.

So:

```python
a = dec(greet)
```

conceptually results in:

```text
a = wrap
```

---

# 10. Now `a()` Executes

```python
a()
```

means the returned `wrap()` runs.

Inside:

```python
print("********")
```

Output:

```text
********
```

Then:

```python
func()
```

Since:

```text
func = greet
```

it effectively calls:

```python
greet()
```

Output:

```text
Hello
```

Then:

```python
print("********")
```

Final output:

```text
********
Hello
********
```

---

# 11. 🔄 Complete Flow Diagram

```text
greet
  │
  │ passed as argument
  ▼
dec(greet)
  │
  ▼
func = greet
  │
  ▼
create wrap()
  │
  ▼
return wrap
  │
  ▼
a = wrap
  │
  ▼
a()
  │
  ▼
wrap()
  │
  ├── print("********")
  │
  ├── func()
  │       ↓
  │     greet()
  │
  └── print("********")
```

This flow is the **heart of decorators**.

---

# 12. ⭐ Using `@decorator`

Python gives us a shortcut.

Instead of:

```python
def message():
    print("Welcome")

message = dec(message)
```

we write:

```python
@dec
def message():
    print("Welcome")
```

These are conceptually equivalent:

```text
@dec
def message():
    ...

        ≈

message = dec(message)
```

This is one of the most important interview points.

---

# 13. 🔥 Your `@dec` Example

```python
def dec(func):

    def wrap():

        print("****************************************")

        func()

        print("****************************************")

    return wrap


@dec
def message():

    print("Welcome to Python Decorators")


message()
```

Output:

```text
****************************************
Welcome to Python Decorators
****************************************
```

---

# 14. 🧠 Memory / Reference Diagram

Before decoration:

```text
message
   │
   ▼
Original message() function
```

After:

```python
@dec
def message():
    ...
```

conceptually:

```text
Original message()
       │
       ▼
   dec(message)
       │
       ▼
    wrapper
       │
       ▼
message now refers
to wrapper
```

Then:

```python
message()
```

runs the wrapper, which calls the original function inside it.

---

# 15. 🔥 Multiple Functions Using Same Decorator

This is one major advantage.

```python
def dec(func):

    def wrapper():

        print("----------------")

        func()

        print("----------------")

    return wrapper
```

Function 1:

```python
@dec
def greet():
    print("Hello")
```

Function 2:

```python
@dec
def message():
    print("Welcome")
```

Function 3:

```python
@dec
def display():
    print("Displaying Data")
```

Call:

```python
greet()
message()
display()
```

The same decorator can add the same behavior to multiple functions.

---

# 16. ❗ Problem With Function Arguments

Our first decorator uses:

```python
def wrapper():
```

This works for:

```python
def message():
```

because `message()` takes no arguments.

But what about:

```python
def add(a, b):
    print(a + b)
```

If our wrapper doesn't accept arguments, we have a problem.

This is why your notes use:

```python
*args
```

and:

```python
**kwargs
```

---

# 17. ⭐ Decorator With `*args`

Example:

```python
def decorator(func):

    def wrapper(*args):

        print("Before")

        func(*args)

        print("After")

    return wrapper


@decorator
def add(a, b):

    print(a + b)


add(10, 20)
```

Output:

```text
Before
30
After
```

---

# 18. 🔍 Dry Run of `*args`

We call:

```python
add(10, 20)
```

Because `add` has been decorated, the wrapper receives:

```text
args = (10, 20)
```

Then:

```python
func(*args)
```

passes those values to the original function.

Effectively:

```python
add(10, 20)
```

Original calculation:

```text
10 + 20
   ↓
  30
```

---

# 19. ⭐ What is `*args`?

`*args` allows a function to receive multiple positional arguments.

Example:

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)
```

Output:

```text
(10, 20, 30, 40)
```

`args` is a tuple.

In decorators, this makes the wrapper work with many different function signatures.

---

# 20. ⭐ Decorator With `**kwargs`

From your notes, you have:

```python
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

Output:

```text
{'name': 'pizza', 'price': 500}
```

`**kwargs` handles keyword arguments.

---

# 21. 🔥 Reusable Decorator

A common pattern is:

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before Function")

        result = func(*args, **kwargs)

        print("After Function")

        return result

    return wrapper
```

This wrapper can accept:

```text
No arguments
Positional arguments
Keyword arguments
Both types
```

---

# 22. 🔥 Example With Positional Arguments

```python
@decorator
def add(a, b):
    return a + b

print(add(10, 20))
```

Output:

```text
Before Function
After Function
30
```

---

# 23. 🔥 Example With Keyword Arguments

```python
@decorator
def student(name, age):

    return f"{name} is {age} years old"


print(
    student(
        name="Ramesh",
        age=30
    )
)
```

Here `kwargs` receives something conceptually like:

```python
{
    "name": "Ramesh",
    "age": 30
}
```

---

# 24. ⭐ Decorator With Return Value

This is another important concept from your notes.

Consider:

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before Function")

        result = func(*args, **kwargs)

        print("After Function")

        return result

    return wrapper
```

Original function:

```python
@decorator
def square(num):

    return num * num
```

Call:

```python
print(square(5))
```

Output:

```text
Before Function
After Function
25
```

---

# 25. ❓ Why Do We Need `return result`?

Suppose original function:

```python
def square(num):
    return num * num
```

returns:

```text
25
```

Inside wrapper:

```python
result = func(*args, **kwargs)
```

stores:

```text
result = 25
```

Now we must return it:

```python
return result
```

Otherwise the decorated function's result would be lost to the caller, and the wrapper would return `None`.

---

# 26. 🔄 Return Value Flow

```text
square(5)
    │
    ▼
wrapper(5)
    │
    ▼
func(5)
    │
    ▼
Original square(5)
    │
    ▼
return 25
    │
    ▼
result = 25
    │
    ▼
return result
    │
    ▼
25
```

---

# 27. ⏱️ Timer Decorator

This is the important real-time example from your code.

```python
import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(
            "Time taken:",
            end - start,
            "seconds"
        )

        return result

    return wrapper
```

Use:

```python
@timer
def message():

    print("Message Function")

    time.sleep(3)


message()
```

---

# 28. 🔍 Timer Decorator Dry Run

Call:

```python
message()
```

Because of:

```python
@timer
```

the wrapper executes.

First:

```python
start = time.time()
```

Suppose:

```text
start = 100
```

Then:

```python
func()
```

runs the original `message()`.

Inside:

```python
time.sleep(3)
```

waits approximately 3 seconds.

Then:

```python
end = time.time()
```

Suppose:

```text
end = 103
```

Calculation:

```text
end - start

103 - 100

= 3 seconds
```

So we measure approximately how long the function execution took.

---

# 29. 🌍 Where Are Decorators Used?

Decorators are commonly useful for cross-cutting behavior such as:

* Logging
* Timing
* Authentication
* Authorization
* Validation
* Caching
* Debugging
* Retry logic
* Framework routing

Conceptually:

```text
User Request
     ↓
Authentication Decorator
     ↓
Is User Allowed?
   /       \
 Yes        No
  ↓          ↓
Function    Reject
```

---

# 30. 🌍 Real-Time Example — Login Check

```python
def login_required(func):

    def wrapper(user_logged_in):

        if user_logged_in:

            func(user_logged_in)

        else:

            print("Please Login First")

    return wrapper
```

Use:

```python
@login_required
def dashboard(user_logged_in):

    print("Welcome to Dashboard")
```

Test:

```python
dashboard(True)
```

Output:

```text
Welcome to Dashboard
```

Test:

```python
dashboard(False)
```

Output:

```text
Please Login First
```

This demonstrates the general idea of checking something before allowing the original function to execute.

---

# 31. ⭐ Decorator and Closure Relationship

Remember Chapter 3:

```python
def outer():

    def inner():
        print("Hello")

    return inner
```

Decorator:

```python
def decorator(func):

    def wrapper():
        func()

    return wrapper
```

Very similar structure.

The wrapper remembers the original:

```python
func
```

even after `decorator()` has returned.

That's why understanding **first-class functions + nested functions + closures** makes decorators much easier.

---

# 32. ❌ Common Mistake 1 — Calling Function Too Early

Wrong:

```python
return wrapper()
```

This executes the wrapper immediately.

Usually for a decorator we want:

```python
return wrapper
```

because we want to return the function object.

Remember:

```text
wrapper
   ↓
Function object


wrapper()
   ↓
Function execution
```

---

# 33. ❌ Common Mistake 2 — Forgetting `*args`

Suppose:

```python
def decorator(func):

    def wrapper():
        func()

    return wrapper
```

Then:

```python
@decorator
def add(a, b):
    print(a + b)
```

Calling:

```python
add(10, 20)
```

fails because `wrapper()` accepts no arguments.

Better reusable pattern:

```python
def wrapper(*args, **kwargs):
```

---

# 34. ❌ Common Mistake 3 — Forgetting Return Value

Wrong:

```python
def wrapper(*args, **kwargs):

    func(*args, **kwargs)
```

If the original function returns something, it isn't forwarded to the caller.

Better:

```python
def wrapper(*args, **kwargs):

    result = func(*args, **kwargs)

    return result
```

Or simply:

```python
def wrapper(*args, **kwargs):

    return func(*args, **kwargs)
```

---

# 35. ❌ Common Mistake 4 — Confusing `@decorator`

Remember:

```python
@decorator
def greet():
    pass
```

is essentially shorthand for:

```python
greet = decorator(greet)
```

This single line is extremely important for interviews.

---

# 36. 📊 Normal Function vs Decorator

| Normal Function                      | Decorator               |
| ------------------------------------ | ----------------------- |
| Performs its own task                | Wraps another function  |
| Doesn't necessarily receive function | Receives a function     |
| Called normally                      | Often applied using `@` |
| No wrapper required                  | Commonly uses wrapper   |
| Simple behavior                      | Adds/modifies behavior  |

---

# 37. 📊 Manual Decoration vs `@`

### Manual

```python
def greet():
    print("Hello")

greet = dec(greet)
```

### `@` Syntax

```python
@dec
def greet():
    print("Hello")
```

Conceptually, both apply the decorator to `greet`.

---

# 38. 📊 `*args` vs `**kwargs`

| `*args`              | `**kwargs`               |
| -------------------- | ------------------------ |
| Positional arguments | Keyword arguments        |
| Stored as tuple      | Stored as dictionary     |
| `add(10,20)`         | `student(name="Ramesh")` |

Example:

```python
def test(*args, **kwargs):

    print(args)
    print(kwargs)
```

Call:

```python
test(
    10,
    20,
    name="Ramesh",
    city="Hyderabad"
)
```

Output:

```text
(10, 20)

{'name': 'Ramesh', 'city': 'Hyderabad'}
```

---

# 39. ✅ Advantages of Decorators

* Code reusability
* Avoid repeated code
* Add functionality without editing original function body
* Useful for logging
* Useful for timing
* Useful for validation
* Useful for access checks
* Cleaner separation of repeated behavior

---

# 40. ❌ Disadvantages

Decorators can also create difficulties:

* Harder for beginners to understand
* Multiple decorators can make execution flow harder to follow
* Debugging can become more difficult
* Poorly designed decorators can hide function behavior
* Function metadata can be changed unless handled properly

---

# 41. ⭐ Important Interview Improvement — `functools.wraps`

In real Python code, we commonly use:

```python
from functools import wraps
```

Example:

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper
```

Why?

Because a decorator replaces the function reference with the wrapper.

`@wraps(func)` helps preserve metadata such as the original function's name and documentation.

For beginner interviews, remember:

> `functools.wraps` preserves the metadata of the original decorated function.

---

# 42. 🎤 Interview Questions & Answers

### Q1. What is a decorator?

A decorator is a function that adds or modifies the behavior of another function without changing its original function body.

### Q2. What does a decorator accept?

Usually another function.

### Q3. What does a decorator commonly return?

A wrapper function.

### Q4. What is a wrapper?

An inner function that adds behavior around the original function.

### Q5. What does `@decorator` mean?

Conceptually:

```python
function = decorator(function)
```

### Q6. Why use `*args`?

To allow the wrapper to accept arbitrary positional arguments.

### Q7. Why use `**kwargs`?

To allow arbitrary keyword arguments.

### Q8. Why return `result` from wrapper?

To preserve the original function's return value for the caller.

### Q9. What is a practical use of decorators?

Logging, timing, validation, authentication, authorization, caching, etc.

### Q10. What is `functools.wraps`?

It helps preserve the decorated function's original metadata.

---

# 43. 📝 MCQs

### Q1. Which symbol is commonly used for decorators?

A. `#`
B. `@`
C. `$`
D. `&`

✅ **Answer: B — `@`**

### Q2. A decorator usually accepts:

A. Only integer
B. Function
C. Only string
D. Only list

✅ **Answer: B — Function**

### Q3. `@dec` is conceptually equivalent to:

A.

```python
func = dec(func)
```

B.

```python
func = func(dec)
```

C.

```python
dec = func()
```

D. None

✅ **Answer: A**

### Q4. `*args` stores arguments as:

A. List
B. Dictionary
C. Tuple
D. Set

✅ **Answer: C**

### Q5. `**kwargs` stores keyword arguments as:

A. Tuple
B. Dictionary
C. Set
D. String

✅ **Answer: B**

---

# 44. 💻 Practice Program 1

Create a decorator that prints:

```text
----------------
Hello Python
----------------
```

Starter:

```python
def decorator(func):

    # write wrapper

    pass


@decorator
def message():

    print("Hello Python")


message()
```

---

# 45. 💻 Practice Program 2

Create a decorator for:

```python
def add(a, b):
    return a + b
```

Expected:

```text
Calculation Started
30
Calculation Completed
```

for:

```python
add(10, 20)
```

---

# 46. 🧠 Coding Challenge

Create:

```python
@check_age
def vote(age):

    print("You can vote")
```

Required behavior:

```python
vote(25)
```

Output:

```text
You can vote
```

But:

```python
vote(15)
```

Output:

```text
Not Eligible
```

Think:

```text
vote(15)
    ↓
wrapper(15)
    ↓
age >= 18 ?
   /      \
 Yes       No
 ↓          ↓
vote()   Not Eligible
```

---

# 🚀 FINAL CHAPTER 4 SUMMARY

```text
                DECORATOR
                    │
                    ▼
          Receives a Function
                    │
                    ▼
             Creates Wrapper
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Before     func()     After
                    │
                    ▼
           Original Function
                    │
                    ▼
             return result
```

### Complete reusable structure

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Before Function")

        result = func(*args, **kwargs)

        print("After Function")

        return result

    return wrapper


@decorator
def add(a, b):

    return a + b


print(add(10, 20))
```

Output:

```text
Before Function
After Function
30
```

## ⚡ 30-Second Interview Revision

```text
Decorator:
Adds/modifies another function's behavior.

@decorator:
function = decorator(function)

func:
Original function

wrapper:
Adds extra functionality

*args:
Positional arguments → tuple

**kwargs:
Keyword arguments → dictionary

return result:
Preserves original return value

Common uses:
Logging
Timing
Validation
Authentication
Authorization
Caching

functools.wraps:
Preserves original function metadata
```

### ⭐ Most important line

**Decorator flow:**

```text
Original Function
       ↓
Pass to Decorator
       ↓
Decorator returns Wrapper
       ↓
Call Wrapper
       ↓
Extra Code Before
       ↓
Original Function
       ↓
Extra Code After
       ↓
Return Result
```

**Chapter 3 + Chapter 4 connection:**

**First-Class Functions → Nested Functions → Closures → Decorators.**
