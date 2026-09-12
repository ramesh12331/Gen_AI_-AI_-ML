# 📘 CHAPTER 3 — FIRST-CLASS FUNCTIONS IN PYTHON

## 🌱 Beginner → Step-by-Step → Interview Level

From your original code, Chapter 3 is **First-Class Functions**. This topic is very important before **Chapter 4: Decorators**.

---

# 1. ✅ Definition — What is a First-Class Function?

In Python, **functions are first-class objects**.

### Simple English

It means Python treats a function like other values/objects.

For example, we can:

* Store a function in a variable
* Pass a function to another function
* Return a function from another function
* Store functions inside collections

### 🎤 Interview Definition

> In Python, functions are first-class objects, meaning they can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures.

---

# 2. ✅ Why Do We Need First-Class Functions?

Normally, you learned:

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Output:

```text
30
```

But Python allows us to do something interesting:

```python
def add(a, b):
    return a + b

a = add

print(a(10, 20))
```

Output:

```text
30
```

Here:

```python
a = add
```

means:

> Store/reference the `add` function using another variable `a`.

Now both can call the same function:

```python
add(10, 20)

a(10, 20)
```

This ability is the foundation for:

```text
First-Class Functions
        ↓
Higher-Order Functions
        ↓
Nested Functions
        ↓
Closures
        ↓
Decorators
```

---

# 3. 🌍 Real-Life Example

Think about a **remote control**.

```text
TV
 ↑
Remote Button
```

The button gives us another way to trigger an operation.

Similarly:

```python
def greet():
    print("Hello")

a = greet
```

Now:

```text
greet
  │
  └────────┐
           ▼
      Function Object
           ▲
           │
           a
```

Calling:

```python
greet()
```

or:

```python
a()
```

executes the same function.

---

# 4. ✅ Basic Syntax

```python
def function_name():
    statements

variable = function_name

variable()
```

Example:

```python
def greet():
    print("Hello")

a = greet

a()
```

Output:

```text
Hello
```

---

# 5. ⭐ Very Important — `fun` vs `fun()`

Beginners must understand this difference.

Suppose:

```python
def fun():
    print("Hello")
```

## `fun`

```python
a = fun
```

means we are referring to the **function object**.

The function is not called here.

## `fun()`

```python
a = fun()
```

means:

> Execute the function now and store its returned result in `a`.

---

# 6. 🔍 Dry Run

Consider:

```python
def greet():
    print("Hello Ramesh")

a = greet

a()
```

### Step 1

Python creates the function:

```python
def greet():
```

Conceptually:

```text
greet
  │
  ▼
Function Object
```

### Step 2

```python
a = greet
```

Now:

```text
greet ─────┐
           │
           ▼
      Function Object
           ▲
           │
a ─────────┘
```

Both names refer to the function.

### Step 3

```python
a()
```

Python executes the function.

Output:

```text
Hello Ramesh
```

---

# 7. 🧠 Memory Diagram

Consider:

```python
def add(a, b):
    return a + b

x = add
```

Conceptually:

```text
        MEMORY

     Function Object
    ┌───────────────┐
    │ add(a, b)     │
    │ return a + b  │
    └───────────────┘
        ▲       ▲
        │       │
       add      x
```

Therefore:

```python
add(10, 20)
```

and:

```python
x(10, 20)
```

both produce:

```text
30
```

---

# 8. ✅ Simple Example

```python
def message():
    print("Welcome to Python")

a = message

a()
```

Output:

```text
Welcome to Python
```

You can also call:

```python
message()
```

Both work.

---

# 9. ✅ Example With Arguments

```python
def add(a, b):
    print(a + b)

result = add

result(10, 20)
```

Output:

```text
30
```

Here:

```python
result = add
```

doesn't execute `add()`.

Later:

```python
result(10, 20)
```

executes it.

---

# 10. 🔥 Function Can Be Passed as an Argument

This is another important feature.

```python
def greet():
    print("Hello")

def display(func):
    func()

display(greet)
```

Output:

```text
Hello
```

Notice:

```python
display(greet)
```

We passed:

```python
greet
```

not:

```python
greet()
```

---

# 11. 🔍 Dry Run — Function as Argument

```python
def greet():
    print("Hello")

def display(func):
    func()

display(greet)
```

### Step 1

`greet` function exists.

### Step 2

`display` function exists.

### Step 3

```python
display(greet)
```

means conceptually:

```text
func = greet
```

Inside `display()`:

```python
func()
```

becomes effectively:

```python
greet()
```

Output:

```text
Hello
```

---

# 12. 🔄 Flow Diagram

```text
greet()
   │
   │ function passed
   ▼
display(greet)
   │
   ▼
func = greet
   │
   ▼
func()
   │
   ▼
greet()
   │
   ▼
"Hello"
```

---

# 13. 🔥 Passing Different Functions

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(func, x, y):
    return func(x, y)

print(calculate(add, 10, 20))
print(calculate(multiply, 10, 20))
```

Output:

```text
30
200
```

Look at the same function:

```python
calculate()
```

It can perform different operations depending on which function we pass.

---

# 14. 🌍 Real-Life Example — Calculator

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def calculator(operation, a, b):
    return operation(a, b)
```

Now:

```python
print(calculator(add, 10, 5))
```

Output:

```text
15
```

```python
print(calculator(subtract, 10, 5))
```

Output:

```text
5
```

```python
print(calculator(multiply, 10, 5))
```

Output:

```text
50
```

This is a practical example of passing functions around.

---

# 15. 🔥 Function Returning Another Function

Now we come to the exact concept from your original notes.

You wrote:

```python
def fun():

    a = 10
    b = 20

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

This is very important for understanding decorators.

---

# 16. 🔍 Understand the Program

Outer function:

```python
def fun():
```

Inside it:

```python
def add(x, y):
    print(x + y)
```

So `add()` is a **nested function**.

Then:

```python
return add
```

Notice:

```python
add
```

not:

```python
add()
```

Therefore Python returns the **function object**.

---

# 17. 🔍 Complete Dry Run

Program:

```python
def fun():

    def add(x, y):
        print(x + y)

    return add


a = fun()

a(10, 20)
```

### Step 1

```python
a = fun()
```

`fun()` executes.

### Step 2

Inside `fun()` Python creates:

```python
def add(x, y):
```

### Step 3

Python reaches:

```python
return add
```

It returns the inner function.

Conceptually:

```text
a = add
```

### Step 4

Now:

```python
a(10, 20)
```

effectively calls the returned `add` function.

### Step 5

```python
print(x + y)
```

becomes:

```text
10 + 20
```

Output:

```text
30
```

---

# 18. 🔄 Flow Diagram

```text
fun()
 │
 ▼
Create add()
 │
 ▼
return add
 │
 ▼
a receives function
 │
 ▼
a(10,20)
 │
 ▼
add(10,20)
 │
 ▼
10 + 20
 │
 ▼
30
```

---

# 19. 🔥 Your Second Example

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

Let's understand it carefully.

---

# 20. 🔍 Dry Run

First:

```python
a = add(30, 40)
```

Inside:

```python
print(a + b)
```

means:

```text
30 + 40
```

Output:

```text
70
```

Then Python creates:

```python
def mul(e, f):
```

Finally:

```python
return mul
```

So the returned `mul` function is stored in the outer variable `a`.

Then:

```python
a(3, 4)
```

calls that returned function.

```text
3 × 4
```

Output:

```text
12
```

Final output:

```text
70
12
```

---

# 21. ⭐ What is a Nested Function?

A function defined inside another function is called a **nested function** or **inner function**.

Syntax:

```python
def outer():

    def inner():
        print("Inner")

    inner()
```

Call:

```python
outer()
```

Output:

```text
Inner
```

Structure:

```text
outer()
   │
   └── inner()
```

---

# 22. Nested Function Example

```python
def outer():

    print("Outer Function")

    def inner():

        print("Inner Function")

    inner()


outer()
```

Output:

```text
Outer Function
Inner Function
```

---

# 23. ⭐ What is a Higher-Order Function?

This is an important interview term.

### Definition

A **higher-order function** is a function that:

* accepts another function as an argument, **or**
* returns another function.

Example:

```python
def display(func):
    func()
```

`display()` receives another function.

So it is a higher-order function.

Another example:

```python
def outer():

    def inner():
        print("Hello")

    return inner
```

`outer()` returns another function.

So it also acts as a higher-order function.

---

# 24. ⭐ First-Class vs Higher-Order Function

Don't confuse these.

| First-Class Functions                   | Higher-Order Function     |
| --------------------------------------- | ------------------------- |
| General property of functions in Python | A particular function     |
| Functions can be treated as values      | Accepts/returns functions |
| Can assign function to variable         | Uses another function     |
| Can pass functions                      | Can receive function      |
| Can return functions                    | Can return function       |

Easy memory:

```text
FIRST-CLASS
     ↓
Python allows functions
to behave like values


HIGHER-ORDER
     ↓
A function that accepts
or returns functions
```

---

# 25. ⭐ Introduction to Closure

You will encounter this when learning decorators.

Look at:

```python
def outer():

    message = "Hello"

    def inner():

        print(message)

    return inner


a = outer()

a()
```

Output:

```text
Hello
```

Interesting question:

`outer()` already finished.

Then how can `inner()` still use:

```python
message
```

?

This behavior is related to a **closure**.

### Simple Definition

> A closure is an inner function that remembers values from its enclosing scope even after the outer function has finished.

---

# 26. 🧠 Closure Diagram

```text
outer()
   │
   ├── message = "Hello"
   │
   └── inner()
          │
          └── uses message
                 │
                 ▼
              "Hello"

return inner
      │
      ▼
a = inner
      │
      ▼
a()
      │
      ▼
"Hello"
```

The inner function retains access to the relevant enclosing value.

---

# 27. 🔥 Closure Example

```python
def multiply_by(x):

    def multiply(y):
        return x * y

    return multiply
```

Now:

```python
double = multiply_by(2)
```

The returned function remembers:

```text
x = 2
```

Then:

```python
print(double(5))
```

Output:

```text
10
```

Because:

```text
x × y

2 × 5

10
```

Another:

```python
triple = multiply_by(3)

print(triple(5))
```

Output:

```text
15
```

---

# 28. 💼 Interview Example

Create a function that receives another function.

```python
def square(x):
    return x * x


def calculate(func, number):
    return func(number)


print(calculate(square, 5))
```

Output:

```text
25
```

Dry run:

```text
calculate(square, 5)

func = square
number = 5

func(number)

↓

square(5)

↓

5 × 5

↓

25
```

---

# 29. 🌍 Real-Time Example — Payment Processing

Imagine an application supports different payment methods.

```python
def card_payment(amount):
    print("Card Payment:", amount)


def upi_payment(amount):
    print("UPI Payment:", amount)


def process_payment(payment_method, amount):

    payment_method(amount)
```

Now:

```python
process_payment(card_payment, 5000)
```

Output:

```text
Card Payment: 5000
```

Or:

```python
process_payment(upi_payment, 2000)
```

Output:

```text
UPI Payment: 2000
```

Same:

```python
process_payment()
```

Different function passed depending on what operation we want.

---

# 30. ❌ Common Mistake — `function` vs `function()`

Suppose:

```python
def greet():
    print("Hello")
```

If you want to store the function:

```python
a = greet
```

Correct.

If you write:

```python
a = greet()
```

the function executes immediately and `a` receives whatever `greet()` returns.

Since there is no explicit `return`, it returns:

```text
None
```

---

# 31. ❌ Common Mistake — Calling Returned Function Incorrectly

```python
def outer():

    def inner():
        print("Hello")

    return inner


a = outer()
```

Correct:

```python
a()
```

because `a` refers to the returned inner function.

---

# 32. ❌ Common Mistake — `return inner()`

Compare:

```python
return inner
```

with:

```python
return inner()
```

They are different.

### `return inner`

Returns the function object.

### `return inner()`

Calls `inner()` immediately and returns its result.

This distinction is extremely important for decorators.

---

# 33. 📊 `return function` vs `return function()`

| `return function`            | `return function()`              |
| ---------------------------- | -------------------------------- |
| Returns function object      | Calls function                   |
| Function can be called later | Function executes immediately    |
| Common in decorators         | Returns called function's result |
| No `()`                      | Uses `()`                        |

---

# 34. 📊 Normal Function vs Higher-Order Function

| Normal Example                | Higher-Order Example        |
| ----------------------------- | --------------------------- |
| Performs normal task          | Works with another function |
| `add(10,20)`                  | `calculate(add,10,20)`      |
| Doesn't need another function | Accepts or returns function |

---

# 35. ✅ Advantages

First-class functions allow:

* ✅ Flexible code
* ✅ Reusable functions
* ✅ Functions as arguments
* ✅ Functions as return values
* ✅ Higher-order functions
* ✅ Closures
* ✅ Decorators
* ✅ Functional programming patterns

---

# 36. ❌ Disadvantages / Difficulties

For beginners:

* ❌ Function references can be confusing
* ❌ `fun` vs `fun()` can cause mistakes
* ❌ Nested functions can become difficult to follow
* ❌ Closures require understanding scope
* ❌ Too many nested functions can reduce readability

---

# 37. ⭐ Important Notes

Remember:

```text
Function can be:

1. Assigned to variable

2. Passed as argument

3. Returned from function

4. Defined inside another function

5. Stored in collections
```

Most important:

```text
fun
↓
Function Object / Reference


fun()
↓
Function Call / Execution
```

---

# 38. 🎤 Interview Questions & Answers

### Q1. What are first-class functions?

> Python functions are first-class objects, meaning they can be assigned to variables, passed as arguments, and returned from other functions.

### Q2. Can a function be assigned to a variable?

Yes.

```python
a = greet
```

### Q3. Can a function be passed to another function?

Yes.

```python
display(greet)
```

### Q4. Can a function return another function?

Yes.

```python
def outer():

    def inner():
        pass

    return inner
```

### Q5. What is a nested function?

A function defined inside another function.

### Q6. What is a higher-order function?

A function that accepts another function as an argument or returns another function.

### Q7. Difference between `fun` and `fun()`?

`fun` refers to the function object.

`fun()` calls the function.

### Q8. What is a closure?

An inner function that retains access to values from its enclosing scope even after the outer function has finished.

### Q9. Why are first-class functions important?

They make higher-order functions, callbacks, closures and decorators possible.

### Q10. Are functions objects in Python?

Yes.

---

# 39. 📝 MCQs

### Q1. Can Python functions be assigned to variables?

A. Yes
B. No

✅ **Answer: A**

### Q2. What does this do?

```python
a = fun
```

A. Calls `fun()`
B. Deletes `fun`
C. Assigns the function object to `a`
D. Error

✅ **Answer: C**

### Q3. What does this do?

```python
a = fun()
```

A. Calls `fun()` and stores its return value
B. Stores only the function reference
C. Deletes function
D. Creates class

✅ **Answer: A**

### Q4. A function that accepts another function is called:

A. Constructor
B. Higher-order function
C. Generator only
D. Class method

✅ **Answer: B**

### Q5. A function inside another function is called:

A. Nested function
B. Class
C. Generator
D. Operator

✅ **Answer: A**

---

# 40. 💻 Practice Programs

Practice in this order:

1. Assign a function to another variable
2. Call function through another variable
3. Pass function as argument
4. Create calculator using function arguments
5. Create nested function
6. Return inner function
7. Call returned function
8. Create `add()` returning `multiply()`
9. Create basic closure
10. Create `double()` using closure

---

# 41. 🧠 Coding Challenge

Create:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, a, b):
    # your code
```

These should work:

```python
print(calculate(add, 20, 10))
print(calculate(subtract, 20, 10))
```

Expected:

```text
30
10
```

### Challenge 2

Create:

```python
def outer(message):

    def inner():
        # print message

    return inner
```

Then:

```python
a = outer("Welcome to Python")

a()
```

Expected:

```text
Welcome to Python
```

---

# 🚀 FINAL CHAPTER 3 SUMMARY

```text
             FIRST-CLASS FUNCTIONS
                      │
          Python treats functions
              like other objects
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ▼              ▼              ▼
   Assign to       Pass to         Return from
   variable        function         function
       │              │              │
       ▼              ▼              ▼
   a = fun      display(fun)     return inner
                                      │
                                      ▼
                              Nested Functions
                                      │
                                      ▼
                                   Closure
                                      │
                                      ▼
                                  Decorators
```

## ⚡ 30-Second Interview Revision

```text
First-Class Function:
Functions are treated like objects.

Assign:
a = fun

Call:
a()

Pass Function:
display(fun)

Return Function:
return inner

Nested Function:
Function inside another function.

Higher-Order Function:
Accepts or returns another function.

Closure:
Inner function remembers enclosing values.

Important:
fun   = function object
fun() = function call
```

### ⭐ Most important concept before Chapter 4

```python
def outer():

    def inner():
        print("Hello")

    return inner


a = outer()
a()
```

Understand this flow clearly:

**`outer()` → creates `inner()` → returns `inner` function → `a` receives it → `a()` executes `inner()`**.

That exact idea is the **foundation of Chapter 4 — Decorators**.
