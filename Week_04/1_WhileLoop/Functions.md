Perfect! This starts the **Functions** section of your handbook.

Since we finished **While Loops**, we now begin **Part 2 – Functions**.

---

# 📘 Python Functions Master Handbook

# 📖 Chapter 1 – Introduction to Functions

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand what a function is.
* ✅ Know why functions are used.
* ✅ Learn the advantages of functions.
* ✅ Understand function syntax.
* ✅ Create and call simple functions.
* ✅ Perform a dry run.
* ✅ Answer interview questions.

---

# 📖 What is a Function?

## ✅ Definition

A **function** is a **named block of reusable code** that performs a specific task.

Instead of writing the same code many times, we write it **once** inside a function and **call** it whenever needed.

---

# 🌍 Real-Life Example – TV Remote 📺

Imagine a TV remote.

Buttons:

```text
Power

Volume +

Volume -

Channel +

Channel -
```

When you press

```text
Volume +
```

the TV performs one task.

Every time you press it,

the same task is repeated.

A Python function works the same way.

---

# 🌍 Real-Life Example – Calculator 🧮

Calculator

```
Addition Button

↓

Adds Two Numbers

↓

Returns Answer
```

Instead of rewriting addition every time,

we create

```python
def add():
```

and call it whenever needed.

---

# 🤔 Why Do We Use Functions?

Without functions:

```python
print("Hello User!")
print("Hello User!")
print("Hello User!")
print("Hello User!")
print("Hello User!")
```

With functions:

```python
def greet():
    print("Hello User!")

greet()
greet()
greet()
greet()
greet()
```

Much shorter.

Much cleaner.

Easy to maintain.

---

# 🎯 Advantages of Functions

✅ Reusable Code

Write once.

Use many times.

---

✅ Less Code

Avoid repeating the same code.

---

✅ Easy Maintenance

If you change the function,

every function call automatically uses the updated code.

---

✅ Better Readability

Programs become easier to understand.

---

✅ Easier Testing

Each function can be tested separately.

---

# 🧠 Think Like a Programmer

Whenever you see a repeated task, ask yourself:

> **Can I make this into a function?**

If the answer is **Yes**, create a function.

---

# 🏗️ Function Syntax

```python
def function_name():
    statements
```

Example

```python
def greet():
    print("Hello")
```

---

# 📌 Parts of a Function

```python
def greet():
    print("Hello")
```

| Part          | Meaning                                    |
| ------------- | ------------------------------------------ |
| `def`         | Keyword used to define a function          |
| `greet`       | Function name                              |
| `()`          | Parentheses (can contain parameters later) |
| `:`           | Starts the function body                   |
| Indented code | Function body                              |

---

# 🔄 Function Flow

```text
Program Starts
      │
      ▼
Function Created
      │
      ▼
Function Called
      │
      ▼
Function Executes
      │
      ▼
Returns to Main Program
```

---

# 🎨 Memory Diagram

```text
Program

│

├── greet()

│

▼

Hello User!

│

▼

Return Back
```

---

# 🌍 Real-Life Examples of Functions

ATM

```text
Withdraw()

Deposit()

Balance()

Transfer()
```

Mobile Phone

```text
Call()

Message()

Camera()

Gallery()
```

Car

```text
Start()

Stop()

Brake()

Horn()
```

Python functions work exactly like these actions.

---

# 💻 Your First Function

```python
def greet():
    print("Hello User!")

greet()
```

---

# 🔍 Line-by-Line Explanation

### Line 1

```python
def greet():
```

Create a function named

```text
greet
```

Nothing executes yet.

Python only remembers the function.

---

### Line 2

```python
print("Hello User!")
```

This code belongs to the function.

It runs only when the function is called.

---

### Line 3

```python
greet()
```

Call the function.

Python jumps to the function.

Executes

```python
print("Hello User!")
```

Returns back.

---

# 🎨 Execution Flow

```text
Program Starts

↓

def greet()

↓

Function Stored

↓

greet()

↓

Jump to Function

↓

Print Hello User!

↓

Return Back

↓

Program Ends
```

---

# 👣 Complete Dry Run

Before execution

| Function | Status  |
| -------- | ------- |
| greet    | Created |

---

Execution

```python
greet()
```

Python jumps to

```python
def greet():
```

Executes

```python
print("Hello User!")
```

Returns.

---

# 🖥 Output

```text
Hello User!
```

---

# 🌍 Calling a Function Multiple Times

```python
def greet():
    print("Hello User!")

greet()
greet()
greet()
```

Output

```text
Hello User!
Hello User!
Hello User!
```

Notice

We wrote

```python
print("Hello User!")
```

only **once**.

---

# ⚠ Common Beginner Mistakes

## ❌ Forgetting Parentheses

Wrong

```python
greet
```

Correct

```python
greet()
```

---

## ❌ Forgetting Indentation

Wrong

```python
def greet():
print("Hello")
```

Correct

```python
def greet():
    print("Hello")
```

---

## ❌ Forgetting to Call the Function

```python
def greet():
    print("Hello")
```

Output

```text
Nothing
```

Because the function was never called.

---

# 💡 Programmer Tips

Remember the two steps:

```text
Create Function

↓

Call Function
```

Creating a function does **not** execute it.

Calling a function executes it.

---

# 🎓 Interview Questions with Answers

### ❓1. What is a function?

✅ **Answer:**

A function is a reusable block of code that performs a specific task.

---

### ❓2. Which keyword is used to create a function?

✅ **Answer:**

`def`

---

### ❓3. Does a function execute when it is defined?

✅ **Answer:**

No.

It executes only when it is called.

---

### ❓4. What is the benefit of functions?

✅ **Answer:**

Functions reduce code duplication and make programs easier to maintain and reuse.

---

# ⭐ MCQs

### Q1. Which keyword defines a function?

A. `fun`

B. `define`

C. `def`

D. `function`

✅ **Answer:** **C**

---

### Q2. What is required to execute a function?

A. `print()`

B. `call`

C. Function call using parentheses `()`

D. `return`

✅ **Answer:** **C**

---

### Q3. What happens when a function is defined?

A. It runs immediately.

B. Python stores it for later use.

C. It returns a value.

D. It prints output.

✅ **Answer:** **B**

---

# 📝 Practice Questions

### ⭐ Easy

Create a function that prints:

```text
Welcome
```

---

### ⭐⭐ Medium

Create a function that prints your name.

---

### ⭐⭐⭐ Challenge

Create a function called `college()` that prints:

```text
Welcome to Engineering College
```

Call it three times.

---

# ✅ Practice Answers

### Answer 1

```python
def welcome():
    print("Welcome")

welcome()
```

---

### Answer 2

```python
def my_name():
    print("Ramesh")

my_name()
```

---

### Answer 3

```python
def college():
    print("Welcome to Engineering College")

college()
college()
college()
```

---

# 📌 Chapter Summary

```text
Need Repeated Task?
        │
       Yes
        │
        ▼
Create Function
        │
        ▼
Call Function
        │
        ▼
Function Executes
        │
        ▼
Return Back
```

---

# 🏆 Congratulations!

You have completed **Functions – Chapter 1: Introduction to Functions**.

You learned:

* ✅ What is a function?
* ✅ Why functions are used
* ✅ Function syntax
* ✅ Function creation
* ✅ Function calling
* ✅ Dry run
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice questions

---

# 📖 Next Chapter

## **Chapter 2 – Functions with Arguments**

We'll explain this program from your code:

```python
def greet(name, age):
    print("Name :", name)
    print("Age :", age)

greet("Ramesh", 24)
```

You'll learn:

* 📖 What are parameters?
* 📖 What are arguments?
* 🔍 Parameter vs argument
* 👣 Complete dry run
* 🎨 Memory diagrams
* 🎓 Interview questions
* ⭐ MCQs
* 📝 Practice programs

This chapter introduces one of the most important concepts in Python: **passing data into functions**.
---
Excellent! 🎉 Now we move to one of the **most important topics in Python Functions**.

This chapter is frequently asked in **interviews** and is essential before learning **`return`**, **`*args`**, and **`**kwargs`**.

---

# 📘 Python Functions Master Handbook

# 📖 Chapter 2 – Functions with Arguments

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand parameters and arguments.
* ✅ Learn the difference between parameters and arguments.
* ✅ Pass values to functions.
* ✅ Perform complete dry runs.
* ✅ Answer interview questions.

---

# 📖 What are Function Arguments?

## ✅ Definition

A function **argument** is the **actual value** that we pass to a function when calling it.

Example:

```python
greet("Ramesh", 24)
```

Here:

* `"Ramesh"` is an argument.
* `24` is an argument.

Arguments provide data to the function.

---

# 📖 What are Parameters?

## ✅ Definition

A **parameter** is a variable declared in the function definition that receives the value from an argument.

Example:

```python
def greet(name, age):
```

Here:

* `name` is a parameter.
* `age` is a parameter.

---

# 🎯 Easy Memory Trick

```text
Function Definition

↓

Parameters

↓

Function Call

↓

Arguments
```

---

# 🌍 Real-Life Example – Food Delivery 🍕

Imagine ordering pizza.

Restaurant Menu:

```text
Pizza(Size, Topping)
```

Here:

* Size → Parameter
* Topping → Parameter

Customer Orders:

```text
Pizza("Large", "Cheese")
```

Here:

* Large → Argument
* Cheese → Argument

The restaurant receives these values and prepares the pizza.

Python functions work exactly the same way.

---

# 💻 Program

```python
def greet(name, age):
    print("Name :", name)
    print("Age :", age)

greet("Ramesh", 24)
```

---

# 🔍 Line-by-Line Explanation

## Line 1

```python
def greet(name, age):
```

Create a function.

Parameters:

```text
name

age
```

At this point, they **do not have values**.

---

## Line 2

```python
print("Name :", name)
```

Print the value stored in `name`.

---

## Line 3

```python
print("Age :", age)
```

Print the value stored in `age`.

---

## Line 4

```python
greet("Ramesh", 24)
```

Function call.

Arguments:

```text
"Ramesh"

24
```

Python matches them like this:

```text
Parameter        Argument

name       ←→    "Ramesh"

age        ←→    24
```

---

# 🎨 Memory Diagram

Before calling the function:

```text
name = ?

age = ?
```

After calling:

```text
name = Ramesh

age = 24
```

---

# 👣 Complete Dry Run

### Step 1

Python reads:

```python
def greet(name, age):
```

Function is stored in memory.

Nothing is printed yet.

---

### Step 2

Python reaches:

```python
greet("Ramesh", 24)
```

Arguments:

```text
"Ramesh"

24
```

---

### Step 3

Memory becomes:

| Parameter | Value  |
| --------- | ------ |
| name      | Ramesh |
| age       | 24     |

---

### Step 4

Execute

```python
print("Name :", name)
```

Output

```text
Name : Ramesh
```

---

### Step 5

Execute

```python
print("Age :", age)
```

Output

```text
Age : 24
```

---

### Step 6

Function finishes.

Control returns to the main program.

---

# 🖥 Output

```text
Name : Ramesh
Age : 24
```

---

# 🎨 Execution Flow

```text
Program Starts

↓

Create Function

↓

Call Function

↓

Arguments Sent

↓

Parameters Receive Values

↓

Execute Function

↓

Return to Main Program

↓

Program Ends
```

---

# 🌍 Calling the Same Function with Different Values

```python
def greet(name, age):
    print(name, age)

greet("Ramesh", 24)

greet("Sita", 20)

greet("Rahul", 30)
```

Output

```text
Ramesh 24

Sita 20

Rahul 30
```

One function.

Different arguments.

---

# 📊 Parameter vs Argument

| Parameter                           | Argument                        |
| ----------------------------------- | ------------------------------- |
| Declared in the function definition | Passed during the function call |
| Receives data                       | Sends data                      |
| Variable                            | Actual value                    |

Example:

```python
def add(a, b):     # a, b → Parameters
    print(a + b)

add(10, 20)        # 10, 20 → Arguments
```

---

# 🌍 Real-Life Examples

### ATM

```text
Withdraw(amount)
```

Parameter:

```text
amount
```

User:

```text
Withdraw(5000)
```

Argument:

```text
5000
```

---

### Mobile Recharge

```text
Recharge(number, amount)
```

Arguments:

```text
9876543210

399
```

---

### Online Shopping

```text
Shipping(company, price)
```

Arguments:

```text
Puma

5000
```

Exactly like your program.

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Wrong number of arguments.

```python
def greet(name, age):
    print(name)

greet("Ramesh")
```

Error:

```text
TypeError

missing required positional argument: age
```

---

## ❌ Mistake 2

Too many arguments.

```python
greet("Ramesh", 24, "Hyderabad")
```

Error:

```text
TypeError
```

---

## ❌ Mistake 3

Confusing parameters and arguments.

Remember:

```text
Definition

↓

Parameters

Call

↓

Arguments
```

---

# 💡 Programmer Tips

A simple sentence to remember:

> **Parameters receive values. Arguments send values.**

---

# 🎓 Interview Questions with Answers

### ❓1. What is a parameter?

✅ **Answer:**

A parameter is a variable in the function definition that receives a value.

---

### ❓2. What is an argument?

✅ **Answer:**

An argument is the actual value passed to a function during a function call.

---

### ❓3. Can a function have multiple parameters?

✅ **Answer:**

Yes. A function can have one, two, or many parameters.

---

### ❓4. What happens if the number of arguments does not match the number of parameters?

✅ **Answer:**

Python raises a `TypeError`.

---

# ⭐ MCQs

### Q1. In the function below, which are the parameters?

```python
def greet(name, age):
    pass
```

A. `"Ramesh"` and `24`

B. `name` and `age`

C. `greet`

D. `pass`

✅ **Answer:** **B**

---

### Q2. Which are the arguments?

```python
greet("Ramesh", 24)
```

A. `name`, `age`

B. `"Ramesh"`, `24`

C. `greet`

D. `print`

✅ **Answer:** **B**

---

### Q3. What happens if you pass fewer arguments than required?

A. The function runs normally.

B. Python ignores the missing values.

C. A `TypeError` occurs.

D. The function returns `None`.

✅ **Answer:** **C**

---

# 📝 Practice Questions

## ⭐ Easy

### Q1

Create a function `student(name)` that prints the student's name.

---

### Q2

Create a function `square(number)` that prints the number and its square.

---

## ⭐⭐ Medium

Create a function `employee(name, salary)` that displays employee details.

---

## ⭐⭐⭐ Challenge

Create a function `movie(title, year, rating)` that prints:

```text
Title  : Leo
Year   : 2023
Rating : 8.5
```

---

# ✅ Practice Answers

### Answer 1

```python
def student(name):
    print("Student :", name)

student("Ramesh")
```

---

### Answer 2

```python
def square(number):
    print("Number :", number)
    print("Square :", number * number)

square(5)
```

---

### Answer 3

```python
def employee(name, salary):
    print("Name :", name)
    print("Salary :", salary)

employee("Ravi", 50000)
```

---

### Answer 4

```python
def movie(title, year, rating):
    print("Title :", title)
    print("Year :", year)
    print("Rating :", rating)

movie("Leo", 2023, 8.5)
```

---

# 📌 Chapter Summary

```text
Function Definition
        │
        ▼
    Parameters
        │
        ▼
   Function Call
        │
        ▼
    Arguments
        │
        ▼
Parameters Receive Values
        │
        ▼
Execute Function
        │
        ▼
Return to Main Program
```

---

# 🏆 Congratulations!

You have completed **Functions – Chapter 2: Functions with Arguments**.

You learned:

* ✅ Parameters
* ✅ Arguments
* ✅ Parameter vs Argument
* ✅ Passing values to functions
* ✅ Dry run
* ✅ Memory diagram
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice questions

---

# 📖 Next Chapter

## **Chapter 3 – Return Statement**

We'll explain this program from your code:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

In the next chapter, you'll learn:

* 🔄 What `return` means
* 🆚 `print()` vs `return`
* 📦 Returning values from functions
* 👣 Complete dry runs
* 🎨 Memory diagrams
* 🎓 Interview questions
* ⭐ MCQs
* 📝 Practice programs

The **`return` statement** is one of the most important concepts in Python because it allows functions to produce values that can be stored, reused, or passed to other functions.
---
Excellent! 🎉 Now we are learning one of the **most important concepts in Python**.

> 💡 **If you understand `return`, you can understand 80% of function-based programming.**

Many beginners confuse **`print()`** and **`return`**, so this chapter explains them in a simple way.

---

# 📘 Python Functions Master Handbook

# 📖 Chapter 3 – Return Statement

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand the `return` statement.
* ✅ Learn the difference between `print()` and `return`.
* ✅ Store values returned by a function.
* ✅ Reuse returned values.
* ✅ Perform a complete dry run.
* ✅ Answer interview questions.

---

# 📖 What is a Return Statement?

## ✅ Definition

The **`return`** statement sends a value **back to the place where the function was called**.

In simple words:

> **`return` gives the answer back to the caller.**

---

# 🌍 Real-Life Example – Calculator 🧮

Imagine you use a calculator.

You press:

```text
10 + 20
```

The calculator does the calculation and gives back:

```text
30
```

That is exactly what `return` does.

```text
Numbers

↓

Function

↓

Calculation

↓

Return Answer

↓

Use Answer
```

---

# 🌍 Real-Life Example – Restaurant 🍕

You order a pizza.

```text
Customer

↓

Places Order

↓

Chef Makes Pizza

↓

Returns Pizza

↓

Customer Receives Pizza
```

The chef doesn't keep the pizza.

He **returns** it to the customer.

A function works the same way.

---

# 💻 Program

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

---

# 🔍 Line-by-Line Explanation

---

## Line 1

```python
def add(a, b):
```

Create a function.

Parameters:

```text
a

b
```

---

## Line 2

```python
return a + b
```

Python adds:

```text
10 + 20

↓

30
```

Then sends

```text
30
```

back to the function call.

---

## Line 3

```python
result = add(10, 20)
```

Arguments:

```text
10

20
```

Python calls

```python
add(10,20)
```

The function returns

```text
30
```

Now

```text
result

↓

30
```

---

## Line 4

```python
print(result)
```

Displays

```text
30
```

---

# 🎨 Memory Diagram

Before Function Call

```text
result

↓

?
```

After Function Call

```text
add(10,20)

↓

30

↓

result = 30
```

---

# 👣 Complete Dry Run

### Step 1

Python stores the function.

Nothing is printed.

---

### Step 2

Python executes

```python
add(10,20)
```

Memory

| Variable | Value |
| -------- | ----: |
| a        |    10 |
| b        |    20 |

---

### Step 3

Execute

```python
return a+b
```

Calculation

```text
10+20

↓

30
```

Return

```text
30
```

---

### Step 4

Store

```text
result

↓

30
```

---

### Step 5

Print

```text
30
```

---

# 🖥 Output

```text
30
```

---

# 🔄 Function Flow

```text
Program

↓

Call Function

↓

Arguments Sent

↓

Calculation

↓

Return Value

↓

Store in Variable

↓

Use Value
```

---

# 🌟 Why Use `return`?

Because the returned value can be reused.

Example:

```python
def add(a, b):
    return a + b

x = add(5, 3)
y = add(10, 20)

print(x)
print(y)
```

Output

```text
8
30
```

---

# 🆚 Difference Between `print()` and `return`

## Example 1 – `print()`

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output

```text
30
None
```

Why?

`print()` only displays the value.

It **does not send it back**.

So

```text
result

↓

None
```

---

## Example 2 – `return`

```python
def add(a, b):
    return a + b

result = add(10,20)

print(result)
```

Output

```text
30
```

Here

```text
result

↓

30
```

because `return` sends the value back.

---

# 📊 print() vs return()

| `print()`                 | `return`                                |
| ------------------------- | --------------------------------------- |
| Displays output           | Sends value back                        |
| Cannot be reused          | Can be stored in a variable             |
| Returns `None` by default | Returns the specified value             |
| Mainly for display        | Mainly for calculations and further use |

---

# 🌍 Real-Life Examples

### ATM

```text
Balance()

↓

Returns

₹10,000
```

---

### Online Shopping

```text
Total Price()

↓

Returns

₹4,500
```

---

### Calculator

```text
Multiply()

↓

Returns

200
```

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using `print()` instead of `return`.

Wrong

```python
def square(n):
    print(n*n)
```

Correct

```python
def square(n):
    return n*n
```

---

## ❌ Mistake 2

Writing code after `return`.

```python
def test():
    return 10
    print("Hello")
```

The `print()` statement **never executes**.

Once Python reaches `return`, the function ends immediately.

---

## ❌ Mistake 3

Forgetting to store the returned value.

```python
add(10,20)
```

Better

```python
result = add(10,20)
```

---

# 💡 Programmer Tips

Remember this sentence:

> **`print()` shows the answer. `return` gives the answer back.**

---

# 🎓 Interview Questions with Answers

### ❓1. What is the purpose of `return`?

✅ **Answer:**

It sends a value back to the caller of the function.

---

### ❓2. What is the difference between `print()` and `return`?

✅ **Answer:**

* `print()` displays the value.
* `return` sends the value back so it can be stored or reused.

---

### ❓3. Can a function have more than one `return` statement?

✅ **Answer:**

Yes, but only one `return` statement is executed during a single function call.

---

### ❓4. What happens after a `return` statement is executed?

✅ **Answer:**

The function immediately ends, and control returns to the caller.

---

# ⭐ MCQs

### Q1. What does `return` do?

A. Prints a value

B. Ends the program

C. Sends a value back to the caller

D. Creates a variable

✅ **Answer:** **C**

---

### Q2. What is stored in `result`?

```python
def add(a, b):
    return a + b

result = add(2, 3)
```

A. `None`

B. `5`

C. `"2+3"`

D. `add`

✅ **Answer:** **B**

---

### Q3. What happens after a `return` statement?

A. The function continues.

B. The next line in the function runs.

C. The function exits immediately.

D. The program restarts.

✅ **Answer:** **C**

---

# 📝 Practice Questions

## ⭐ Easy

### Q1

Create a function `square(n)` that returns the square of a number.

---

### Q2

Create a function `cube(n)` that returns the cube of a number.

---

## ⭐⭐ Medium

Create a function `maximum(a, b)` that returns the larger number.

---

## ⭐⭐⭐ Challenge

Create a function `percentage(total, marks)` that returns the percentage.

Example:

```text
Total = 500

Marks = 420

Output = 84.0
```

---

# ✅ Practice Answers

### Answer 1

```python
def square(n):
    return n * n

result = square(5)
print(result)
```

Output:

```text
25
```

---

### Answer 2

```python
def cube(n):
    return n * n * n

result = cube(3)
print(result)
```

Output:

```text
27
```

---

### Answer 3

```python
def maximum(a, b):
    if a > b:
        return a
    return b

print(maximum(10, 20))
```

Output:

```text
20
```

---

### Answer 4

```python
def percentage(total, marks):
    return (marks / total) * 100

print(percentage(500, 420))
```

Output:

```text
84.0
```

---

# 📌 Chapter Summary

```text
Function Call
      │
      ▼
Arguments Sent
      │
      ▼
Function Executes
      │
      ▼
return Value
      │
      ▼
Caller Receives Value
      │
      ▼
Store or Use the Value
```

---

# 🏆 Congratulations!

You have completed **Functions – Chapter 3: Return Statement**.

You learned:

* ✅ What `return` is
* ✅ Difference between `print()` and `return`
* ✅ How to return values
* ✅ How to store returned values
* ✅ Dry-run tables
* ✅ Memory diagrams
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice questions

---

# 📖 Next Chapter

## **Chapter 4 – Multiple Functions (Shipping, Address & Grade System)**

We'll explain these programs from your code:

```python
def shipping(company, price):
    print(company, ":", price)

shipping("Puma", 5000)
```

```python
def address(pincode, city, house_no):
    print("City :", city)
    print("Pincode :", pincode)
    print("House No :", house_no)
```

```python
def grading_system(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    else:
        print("Fail")
```

In this chapter, you'll learn how to build **real-world functions** that accept multiple inputs, use decision-making with `if-elif-else`, and organize related tasks into reusable functions.
---
Excellent! 🎉 Now we'll learn how functions are used in **real-world applications**.

These examples show that a function can perform **different tasks** based on the values passed to it.

---

# 📘 Python Functions Master Handbook

# 📖 Chapter 4 – Real-World Functions (Shipping, Address & Grade System)

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Create functions with multiple parameters.
* ✅ Pass different types of data.
* ✅ Use `if-elif-else` inside functions.
* ✅ Build reusable real-world functions.
* ✅ Perform complete dry runs.
* ✅ Answer interview questions.

---

# 📖 What is a Real-World Function?

A real-world function performs a specific task, such as:

* 📦 Shipping details
* 🏠 Address details
* 🎓 Grade calculation
* 💰 Salary calculation
* 🏦 Bank transactions

Instead of writing the same code again and again, we write a function once and call it whenever needed.

---

# 🌍 Real-Life Example

Think about an online shopping website.

When you place an order:

```text
Customer Places Order
        │
        ▼
Shipping Function
        │
        ▼
Displays Company & Price
```

The same shipping function can be used for thousands of customers.

---

# 🟢 Program 1 – Shipping Function

## 💻 Program

```python
def shipping(company, price):
    print(company, ":", price)

shipping("Puma", 5000)
```

---

# 📖 What Does This Program Do?

It displays the company name and product price.

Output

```text
Puma : 5000
```

---

# 🔍 Line-by-Line Explanation

### Line 1

```python
def shipping(company, price):
```

Create a function.

Parameters:

```text
company

price
```

---

### Line 2

```python
print(company, ":", price)
```

Display the values.

---

### Line 3

```python
shipping("Puma", 5000)
```

Arguments

```text
company → Puma

price → 5000
```

---

# 👣 Dry Run

### Before Function Call

| Parameter | Value |
| --------- | ----- |
| company   | ?     |
| price     | ?     |

---

### Function Call

```python
shipping("Puma",5000)
```

Memory

| Parameter | Value |
| --------- | ----- |
| company   | Puma  |
| price     | 5000  |

---

### Output

```text
Puma : 5000
```

---

# 🌍 More Examples

```python
shipping("Nike", 6500)
shipping("Adidas", 4200)
shipping("Reebok", 3800)
```

Output

```text
Nike : 6500
Adidas : 4200
Reebok : 3800
```

---

# 🟢 Program 2 – Address Function

## 💻 Program

```python
def address(pincode, city, house_no):
    print("City :", city)
    print("Pincode :", pincode)
    print("House No :", house_no)

address(500002, "Hyderabad", 321)
```

---

# 📖 What Does This Program Do?

Displays address details.

Output

```text
City : Hyderabad
Pincode : 500002
House No : 321
```

---

# 🔍 Line-by-Line Explanation

### Line 1

```python
def address(pincode, city, house_no):
```

Parameters

```text
pincode

city

house_no
```

---

### Function Call

```python
address(500002, "Hyderabad", 321)
```

Python matches:

| Parameter | Argument  |
| --------- | --------- |
| pincode   | 500002    |
| city      | Hyderabad |
| house_no  | 321       |

---

### Output

```text
City : Hyderabad
Pincode : 500002
House No : 321
```

---

# 🎨 Memory Diagram

```text
address()

│

├── pincode = 500002

├── city = Hyderabad

└── house_no = 321
```

---

# 🌍 Real-Life Example

Courier Delivery

```text
House Number

↓

Street

↓

City

↓

Pincode

↓

Package Delivered
```

---

# 🟢 Program 3 – Grade System

## 💻 Program

```python
def grading_system(marks):

    if marks >= 90:
        print("Grade A")

    elif marks >= 75:
        print("Grade B")

    elif marks >= 60:
        print("Grade C")

    else:
        print("Fail")

grading_system(90)
```

---

# 📖 What Does This Program Do?

It checks the student's marks and prints the appropriate grade.

---

# 🌍 Grade Rules

|    Marks | Grade |
| -------: | ----- |
| 90 – 100 | A     |
|  75 – 89 | B     |
|  60 – 74 | C     |
| Below 60 | Fail  |

---

# 🔍 Line-by-Line Explanation

### Line 1

```python
def grading_system(marks):
```

Parameter

```text
marks
```

---

### Function Call

```python
grading_system(90)
```

Memory

```text
marks = 90
```

---

### Condition 1

```python
if marks >= 90:
```

Check

```text
90 >= 90

True
```

Output

```text
Grade A
```

The remaining `elif` and `else` blocks are skipped.

---

# 👣 Dry Run

| Marks | Condition | Output  |
| ----: | --------- | ------- |
|    90 | ≥ 90      | Grade A |
|    80 | ≥ 75      | Grade B |
|    65 | ≥ 60      | Grade C |
|    45 | Else      | Fail    |

---

# 🌍 More Examples

```python
grading_system(95)
grading_system(80)
grading_system(65)
grading_system(40)
```

Output

```text
Grade A
Grade B
Grade C
Fail
```

---

# 🎨 Execution Flow

```text
Function Called

↓

Receive Marks

↓

Check ≥90 ?

↓

Yes

↓

Grade A

↓

No

↓

Check ≥75 ?

↓

Yes

↓

Grade B

↓

No

↓

Check ≥60 ?

↓

Yes

↓

Grade C

↓

No

↓

Fail
```

---

# 📊 Summary of All Three Functions

| Function           | Purpose                        |
| ------------------ | ------------------------------ |
| `shipping()`       | Displays shipping details      |
| `address()`        | Displays address information   |
| `grading_system()` | Calculates and displays grades |

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Passing arguments in the wrong order.

Wrong

```python
address("Hyderabad",500002,321)
```

Output

```text
City : 500002
```

The values will be assigned incorrectly because arguments are matched by position.

---

## ❌ Mistake 2

Missing an argument.

```python
shipping("Puma")
```

Error

```text
TypeError
missing 1 required positional argument: 'price'
```

---

## ❌ Mistake 3

Incorrect condition order.

Wrong

```python
if marks >= 60:
```

before

```python
if marks >= 90:
```

A score of `95` would satisfy the first condition (`>= 60`), so it would incorrectly print **Grade C**.

Always check the **highest range first**.

---

# 💡 Programmer Tips

Design one function to perform **one task only**.

Good examples:

* `shipping()` → Shipping details
* `address()` → Address details
* `grading_system()` → Grade calculation

This makes your code easier to read and maintain.

---

# 🎓 Interview Questions with Answers

### ❓1. Can a function have multiple parameters?

✅ **Answer:**

Yes. A function can accept one, two, or many parameters.

---

### ❓2. Why do we use functions for tasks like shipping or grading?

✅ **Answer:**

Because the same logic can be reused with different input values.

---

### ❓3. Why is the order of `if-elif` conditions important?

✅ **Answer:**

Python checks conditions from top to bottom. The first matching condition executes, and the remaining conditions are skipped.

---

### ❓4. What happens if we pass fewer arguments than parameters?

✅ **Answer:**

Python raises a `TypeError` because required arguments are missing.

---

# ⭐ MCQs

### Q1. Which function calculates grades?

A.

```python
shipping()
```

B.

```python
address()
```

C.

```python
grading_system()
```

D.

```python
add()
```

✅ **Answer:** **C**

---

### Q2. How many parameters does `address()` have?

A. 1

B. 2

C. 3

D. 4

✅ **Answer:** **C**

---

### Q3. Which grade is printed for `marks = 80`?

A. Grade A

B. Grade B

C. Grade C

D. Fail

✅ **Answer:** **B**

---

# 📝 Practice Questions

## ⭐ Easy

### Q1

Create a function `student(name, roll)` that displays a student's name and roll number.

---

### Q2

Create a function `product(name, price)` that displays product details.

---

## ⭐⭐ Medium

Create a function `employee(name, department, salary)` that prints employee information.

---

## ⭐⭐⭐ Challenge

Create a function `electricity_bill(units)`.

Rules:

* Above 300 units → High Bill
* 151–300 units → Medium Bill
* 0–150 units → Low Bill

---

# ✅ Practice Answers

### Answer 1

```python
def student(name, roll):
    print("Name :", name)
    print("Roll :", roll)

student("Ramesh", 101)
```

---

### Answer 2

```python
def product(name, price):
    print("Product :", name)
    print("Price :", price)

product("Laptop", 65000)
```

---

### Answer 3

```python
def employee(name, department, salary):
    print("Name :", name)
    print("Department :", department)
    print("Salary :", salary)

employee("Ravi", "IT", 50000)
```

---

### Answer 4

```python
def electricity_bill(units):
    if units > 300:
        print("High Bill")
    elif units >= 151:
        print("Medium Bill")
    else:
        print("Low Bill")

electricity_bill(220)
```

---

# 📌 Chapter Summary

```text
Create Function
        │
        ▼
Pass Arguments
        │
        ▼
Parameters Receive Values
        │
        ▼
Perform Task
        │
        ▼
Display Result
        │
        ▼
Return to Main Program
```

---

# 🏆 Congratulations!

You have completed **Functions – Chapter 4: Real-World Functions (Shipping, Address & Grade System)**.

You learned:

* ✅ Functions with multiple parameters
* ✅ Passing different data types
* ✅ Using `if-elif-else` inside functions
* ✅ Real-world function examples
* ✅ Dry runs
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice questions

---

# 📖 Next Chapter

## **Chapter 5 – Variable-Length Arguments (`*args`)**

We'll explain these programs from your code:

```python
def add(*numbers):
    print(sum(numbers))

add(2, 3, 4, 5)
```

```python
def shipping(*items):
    print(items)

shipping("Rice", "Sugar", "Oil", "Dal")
```

In the next chapter, you'll learn:

* ⭐ What `*args` is
* 📦 How Python packs multiple values into a tuple
* 🔄 Why `*args` is useful
* 👣 Complete dry runs
* 🎨 Memory diagrams
* 🎓 Interview questions
* ⭐ MCQs
* 📝 Practice programs

This chapter introduces **variable-length arguments**, allowing your functions to accept **any number of values**.
---
Excellent! 🎉 Now we are learning one of the most useful Python features.

Many beginners think a function must always receive a fixed number of arguments. That's **not true**.

Python provides **`*args`** to accept **any number of arguments**.

---

# 📘 Python Functions Master Handbook

# 📖 Chapter 5 – Variable-Length Arguments (`*args`)

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand `*args`.
* ✅ Learn why `*args` is used.
* ✅ Know how Python stores multiple values.
* ✅ Use `sum()` with `*args`.
* ✅ Perform complete dry runs.
* ✅ Answer interview questions.

---

# 📖 What is `*args`?

## ✅ Definition

`*args` allows a function to accept **any number of positional arguments**.

Instead of fixing the number of parameters, Python collects all arguments into a **tuple**.

> **Think of `*args` as a bag that can hold any number of values.**

---

# 🌍 Real-Life Example – Shopping Bag 🛍️

Imagine you go shopping.

Some days you buy:

```text
Rice
```

Some days:

```text
Rice
Sugar
Oil
```

Some days:

```text
Rice
Sugar
Oil
Dal
Soap
Milk
```

You don't know in advance how many items you'll buy.

Instead of creating separate functions, we use one function:

```python
def shopping(*items):
```

---

# 🤔 Why Do We Need `*args`?

Without `*args`:

```python
def add(a, b):
    print(a + b)
```

Works only for **2 numbers**.

```python
add(10, 20)
```

But what if you want to add **5 numbers**?

You would have to rewrite the function.

With `*args`:

```python
def add(*numbers):
```

It works for **2, 5, 10, or even 100 numbers**.

---

# 🎨 Memory Trick

```text
Arguments

↓

Python Packs Them

↓

Tuple

↓

*args
```

---

# 🟢 Program 1 – Add Any Number of Values

## 💻 Program

```python
def add(*numbers):
    print(sum(numbers))

add(2, 3, 4, 5)
```

---

# 📖 What Does This Program Do?

It adds all the numbers passed to the function.

Output

```text
14
```

---

# 🔍 Line-by-Line Explanation

## Line 1

```python
def add(*numbers):
```

Create a function.

`*numbers` means:

> "Accept any number of arguments."

---

## Line 2

```python
print(sum(numbers))
```

`sum()` adds all values inside the tuple.

---

## Line 3

```python
add(2, 3, 4, 5)
```

Arguments:

```text
2

3

4

5
```

Python automatically creates:

```python
numbers = (2, 3, 4, 5)
```

Notice:

It is a **tuple**, not a list.

---

# 🎨 Memory Diagram

Before Function Call

```text
numbers

↓

?
```

After Function Call

```text
numbers

↓

(2, 3, 4, 5)
```

---

# 👣 Complete Dry Run

### Step 1

Python stores the function.

---

### Step 2

Call

```python
add(2,3,4,5)
```

---

### Step 3

Memory

| Variable | Value     |
| -------- | --------- |
| numbers  | (2,3,4,5) |

---

### Step 4

Execute

```python
sum(numbers)
```

Calculation

```text
2

+

3

+

4

+

5

=

14
```

---

### Step 5

Output

```text
14
```

---

# 🖥 Output

```text
14
```

---

# 🌍 More Examples

Example 1

```python
add(10,20)
```

Tuple

```text
(10,20)
```

Output

```text
30
```

---

Example 2

```python
add(5,10,15,20,25)
```

Tuple

```text
(5,10,15,20,25)
```

Output

```text
75
```

---

Example 3

```python
add(100)
```

Tuple

```text
(100,)
```

Output

```text
100
```

---

# 🟢 Program 2 – Shipping Items

## 💻 Program

```python
def shipping(*items):
    print(items)

shipping("Rice", "Sugar", "Oil", "Dal")
```

---

# 📖 What Does This Program Do?

It accepts any number of items.

Output

```text
('Rice', 'Sugar', 'Oil', 'Dal')
```

---

# 🔍 Line-by-Line Explanation

### Function

```python
def shipping(*items):
```

Accept unlimited items.

---

### Function Call

```python
shipping("Rice", "Sugar", "Oil", "Dal")
```

Python creates

```python
items = ("Rice", "Sugar", "Oil", "Dal")
```

---

### Output

```text
('Rice', 'Sugar', 'Oil', 'Dal')
```

---

# 🌍 More Examples

```python
shipping("Laptop")
```

Output

```text
('Laptop',)
```

---

```python
shipping("Book", "Pen")
```

Output

```text
('Book', 'Pen')
```

---

```python
shipping("Rice", "Oil", "Sugar", "Dal", "Soap")
```

Output

```text
('Rice', 'Oil', 'Sugar', 'Dal', 'Soap')
```

---

# 📦 Why Does Python Use a Tuple?

Because tuples are:

* ✅ Faster than lists
* ✅ Immutable (cannot be changed)
* ✅ Good for storing fixed arguments

---

# 📊 Normal Parameters vs `*args`

| Normal Parameters            | `*args`                        |
| ---------------------------- | ------------------------------ |
| Fixed number of arguments    | Any number of arguments        |
| Example: `add(a, b)`         | Example: `add(*numbers)`       |
| Receives values individually | Receives all values as a tuple |

---

# 🌍 Real-Life Applications

`*args` is useful in:

* 🛒 Shopping cart items
* 📦 Shipping multiple products
* ➕ Calculator with many numbers
* 📚 Library book list
* 📝 Student attendance list

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Thinking `*args` creates a list.

Wrong.

It creates a **tuple**.

```python
def test(*x):
    print(type(x))
```

Output

```text
<class 'tuple'>
```

---

## ❌ Mistake 2

Using `sum()` with strings.

```python
add("A","B")
```

Error:

```text
TypeError
```

`sum()` works only with numbers.

---

## ❌ Mistake 3

Forgetting the `*`.

Wrong

```python
def add(numbers):
```

Correct

```python
def add(*numbers):
```

---

# 💡 Programmer Tips

Remember:

```text
*args

↓

Many Arguments

↓

One Tuple
```

---

# 🎓 Interview Questions with Answers

### ❓1. What is `*args`?

✅ **Answer:**

`*args` allows a function to accept any number of positional arguments.

---

### ❓2. How are values stored in `*args`?

✅ **Answer:**

As a tuple.

---

### ❓3. Can `*args` accept zero arguments?

✅ **Answer:**

Yes.

Example:

```python
def show(*x):
    print(x)

show()
```

Output:

```text
()
```

---

### ❓4. Why is `*args` useful?

✅ **Answer:**

It makes functions flexible by allowing any number of arguments.

---

# ⭐ MCQs

### Q1. `*args` stores values in a:

A. List

B. Dictionary

C. Tuple

D. Set

✅ **Answer:** **C**

---

### Q2. Which function accepts unlimited positional arguments?

A.

```python
def add(a, b):
```

B.

```python
def add(*numbers):
```

C.

```python
def add():
```

D.

```python
def add(a):
```

✅ **Answer:** **B**

---

### Q3. What is the output?

```python
def show(*x):
    print(x)

show(1,2,3)
```

A.

```text
[1,2,3]
```

B.

```text
(1,2,3)
```

C.

```text
1 2 3
```

D.

```text
123
```

✅ **Answer:** **B**

---

# 📝 Practice Questions

## ⭐ Easy

### Q1

Create a function that prints all fruits passed using `*args`.

---

### Q2

Create a function that prints the largest number using `max()`.

---

## ⭐⭐ Medium

Create a function that finds the average of all numbers passed using `*args`.

---

## ⭐⭐⭐ Challenge

Create a function `shopping_cart(*items)` that prints:

```text
Items in Cart:
- Rice
- Sugar
- Oil
- Dal
```

---

# ✅ Practice Answers

### Answer 1

```python
def fruits(*items):
    print(items)

fruits("Apple", "Banana", "Mango")
```

---

### Answer 2

```python
def largest(*numbers):
    print(max(numbers))

largest(12, 45, 7, 89, 34)
```

Output:

```text
89
```

---

### Answer 3

```python
def average(*numbers):
    print(sum(numbers) / len(numbers))

average(10, 20, 30, 40)
```

Output:

```text
25.0
```

---

### Answer 4

```python
def shopping_cart(*items):
    print("Items in Cart:")
    for item in items:
        print("-", item)

shopping_cart("Rice", "Sugar", "Oil", "Dal")
```

Output:

```text
Items in Cart:
- Rice
- Sugar
- Oil
- Dal
```

---

# 📌 Chapter Summary

```text
Function Call
      │
      ▼
Arguments Passed
      │
      ▼
Python Packs Them
      │
      ▼
Tuple (*args)
      │
      ▼
Function Uses the Tuple
      │
      ▼
Output
```

---

# 🏆 Congratulations!

You have completed **Functions – Chapter 5: Variable-Length Arguments (`*args`)**.

You learned:

* ✅ What `*args` is
* ✅ How Python packs arguments into a tuple
* ✅ Why `*args` is useful
* ✅ Using `sum()` with `*args`
* ✅ Dry runs
* ✅ Memory diagrams
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice questions

---

# 📖 Next Chapter

## **Chapter 6 – Multiplication Function & Introduction to Lists**

We'll explain these programs from your code:

```python
def multiply(a, b):
    print(a * b)

multiply(10, 20)
```

Then we'll begin the next topic:

```python
numbers = [10, 20, 30, 40, 50]
mixed = [1, 2.5, True, "Python"]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

In this chapter, you'll learn:

* ➗ Creating multiplication functions
* 📋 What is a list?
* 🔢 List indexing
* 🧩 Mixed data types in lists
* 🧮 2D lists (Matrix)
* 👣 Dry runs
* 🎓 Interview questions
* ⭐ MCQs
* 📝 Practice programs

This chapter marks the beginning of **Python Collections**, starting with one of the most widely used data structures: **Lists**.
---
Excellent! 🎉 Now we are entering one of the **most important Python topics**.

> 💡 **Lists are used in almost every Python project**, whether it's web development, data analysis, automation, or machine learning.

We'll start from the basics so that even a complete beginner can understand.

---

# 📘 Python Collections Master Handbook

# 📖 Chapter 6 – Multiplication Function & Introduction to Lists

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Create a multiplication function.
* ✅ Understand what a list is.
* ✅ Create lists.
* ✅ Store different data types in a list.
* ✅ Access elements using indexing.
* ✅ Understand 2D lists (Matrix).
* ✅ Perform dry runs.
* ✅ Answer interview questions.

---

# 🟢 Part 1 – Multiplication Function

---

## 💻 Program

```python
def multiply(a, b):
    print(a * b)

multiply(10, 20)
```

---

# 📖 What Does This Program Do?

It multiplies two numbers.

Output

```text
200
```

---

# 🌍 Real-Life Example – Shopping 🛒

Suppose:

* Price of one notebook = ₹10
* Quantity = 20

Total cost:

```text
10 × 20 = ₹200
```

Instead of calculating manually every time, we create a function.

---

# 🔍 Line-by-Line Explanation

### Line 1

```python
def multiply(a, b):
```

Create a function.

Parameters:

```text
a

b
```

---

### Line 2

```python
print(a * b)
```

Multiply the two values.

---

### Line 3

```python
multiply(10,20)
```

Arguments

```text
a = 10

b = 20
```

Calculation

```text
10 × 20

↓

200
```

---

# 👣 Dry Run

| Parameter | Value |
| --------- | ----: |
| a         |    10 |
| b         |    20 |

Calculation

```text
10 × 20 = 200
```

Output

```text
200
```

---

# 🌍 More Examples

```python
multiply(5, 6)
```

Output

```text
30
```

---

```python
multiply(8, 9)
```

Output

```text
72
```

---

# ⚠ Common Mistake

Wrong

```python
multiply(10)
```

Error

```text
TypeError

missing required positional argument
```

---

# 🟢 Part 2 – Introduction to Lists

---

# 📖 What is a List?

## ✅ Definition

A **List** is an **ordered, mutable collection** that can store **multiple values** in a single variable.

In simple words:

> **A list is like a box that can hold many items.**

---

# 🌍 Real-Life Example – Shopping Basket 🛒

Imagine a shopping basket.

```text
Basket

↓

Rice

Sugar

Oil

Soap

Milk
```

Instead of creating five variables:

```python
rice = "Rice"
sugar = "Sugar"
oil = "Oil"
soap = "Soap"
milk = "Milk"
```

We create one list:

```python
items = ["Rice", "Sugar", "Oil", "Soap", "Milk"]
```

Much easier!

---

# 📖 Why Do We Use Lists?

Without a list:

```python
student1 = "Ramesh"
student2 = "Rahul"
student3 = "Sita"
student4 = "Ravi"
student5 = "Anjali"
```

With a list:

```python
students = ["Ramesh", "Rahul", "Sita", "Ravi", "Anjali"]
```

Cleaner, shorter, and easier to manage.

---

# 💻 Program 1 – Integer List

```python
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

---

# 🔍 Line-by-Line Explanation

### Line 1

```python
numbers = [10,20,30,40,50]
```

Python creates a list.

Memory

```text
numbers

↓

[10,20,30,40,50]
```

---

### Line 2

```python
print(numbers)
```

Display the complete list.

Output

```text
[10, 20, 30, 40, 50]
```

---

# 🎨 Memory Diagram

```text
numbers

↓

┌────┬────┬────┬────┬────┐
│10  │20  │30  │40  │50  │
└────┴────┴────┴────┴────┘
```

---

# 🟢 Program 2 – Mixed Data Types

```python
mixed = [1, 2.5, True, "Python"]

print(mixed)
```

---

# 📖 What Does This Program Do?

Creates a list containing different data types.

Output

```text
[1, 2.5, True, 'Python']
```

---

# 📊 Data Types Stored

| Value    | Data Type        |
| -------- | ---------------- |
| 1        | Integer (`int`)  |
| 2.5      | Float (`float`)  |
| True     | Boolean (`bool`) |
| "Python" | String (`str`)   |

---

# 🌍 Why Can Python Do This?

Python lists are **heterogeneous**, meaning they can store different types of data in the same list.

---

# 🟢 Program 3 – Matrix (2D List)

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
```

---

# 📖 What is a Matrix?

A **Matrix** is a **list containing other lists**.

Think of it as a table.

---

# 🎨 Matrix Diagram

```text
       Column

        0   1   2

      ┌───┬───┬───┐

Row 0 │ 1 │ 2 │ 3 │

      ├───┼───┼───┤

Row 1 │ 4 │ 5 │ 6 │

      ├───┼───┼───┤

Row 2 │ 7 │ 8 │ 9 │

      └───┴───┴───┘
```

---

# 🟢 Accessing Rows

Program

```python
print(matrix[1])
```

Output

```text
[4, 5, 6]
```

Explanation

```text
matrix

↓

Row 0

↓

Row 1 ✅

↓

[4,5,6]
```

---

# 🟢 Accessing Individual Elements

Program

```python
print(matrix[2][0])
```

---

### Step 1

```text
matrix[2]

↓

[7,8,9]
```

---

### Step 2

```text
[7,8,9][0]

↓

7
```

Output

```text
7
```

---

# 🎨 Memory Diagram

```text
matrix

↓

0 → [1,2,3]

1 → [4,5,6]

2 → [7,8,9]
```

---

# 👣 Dry Run

Program

```python
print(matrix[2][0])
```

Step 1

```text
matrix[2]

↓

[7,8,9]
```

Step 2

```text
[7,8,9][0]

↓

7
```

Output

```text
7
```

---

# 📊 Types of Lists

| Type         | Example             |
| ------------ | ------------------- |
| Integer List | `[10,20,30]`        |
| String List  | `["A","B","C"]`     |
| Mixed List   | `[1,"Python",True]` |
| Nested List  | `[[1,2],[3,4]]`     |

---

# 🌍 Real-World Applications

Lists are used in:

* 👨‍🎓 Student records
* 🛒 Shopping carts
* 📞 Contact lists
* 🎵 Music playlists
* 📸 Image pixels
* 📊 Excel-like tables
* 🎮 Game boards

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using parentheses.

Wrong

```python
numbers = (10,20,30)
```

This creates a **tuple**, not a list.

Correct

```python
numbers = [10,20,30]
```

---

## ❌ Mistake 2

Wrong index.

```python
numbers = [10,20,30]

print(numbers[5])
```

Error

```text
IndexError

list index out of range
```

---

## ❌ Mistake 3

Confusing rows and columns.

```python
matrix[2][0]
```

Means:

* First select **Row 2**
* Then select **Column 0**

---

# 💡 Programmer Tips

Remember:

```text
List

↓

Square Brackets

↓

[]
```

And:

```text
Index Starts

↓

0
```

---

# 🎓 Interview Questions with Answers

### ❓1. What is a list?

✅ **Answer:**

A list is an ordered, mutable collection that stores multiple values.

---

### ❓2. Can a list store different data types?

✅ **Answer:**

Yes. Python lists can store integers, floats, strings, booleans, and even other lists.

---

### ❓3. What is a nested list?

✅ **Answer:**

A list that contains one or more lists as its elements.

---

### ❓4. What does `matrix[2][0]` return?

✅ **Answer:**

`7`

---

# ⭐ MCQs

### Q1. Which brackets are used for lists?

A. `()`

B. `{}`

C. `[]`

D. `<>`

✅ **Answer:** **C**

---

### Q2. What is the index of the first element in a list?

A. `1`

B. `-1`

C. `0`

D. `2`

✅ **Answer:** **C**

---

### Q3. What is the output?

```python
numbers = [10,20,30]

print(numbers[1])
```

A. `10`

B. `20`

C. `30`

D. Error

✅ **Answer:** **B**

---

# 📝 Practice Questions

## ⭐ Easy

### Q1

Create a list of five fruits and print it.

---

### Q2

Create a list of five numbers and print the third element.

---

## ⭐⭐ Medium

Create a mixed list containing:

* Your name
* Your age
* Your city
* A boolean value

Print the list.

---

## ⭐⭐⭐ Challenge

Create the following matrix and print the value `8`.

```text
1 2 3

4 5 6

7 8 9
```

---

# ✅ Practice Answers

### Answer 1

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits)
```

---

### Answer 2

```python
numbers = [5, 10, 15, 20, 25]

print(numbers[2])
```

Output

```text
15
```

---

### Answer 3

```python
info = ["Ramesh", 24, "Hyderabad", True]

print(info)
```

---

### Answer 4

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[2][1])
```

Output

```text
8
```

---

# 📌 Chapter Summary

```text
Need Multiple Values?
        │
        ▼
Create a List
        │
        ▼
Store Values
        │
        ▼
Access Using Index
        │
        ▼
Modify or Use Values
```

---

# 🏆 Congratulations!

You have completed **Chapter 6 – Multiplication Function & Introduction to Lists**.

You learned:

* ✅ Multiplication function
* ✅ What is a list?
* ✅ Creating lists
* ✅ Mixed data types
* ✅ Nested lists (Matrix)
* ✅ Indexing
* ✅ Dry runs
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice questions

---

# 📖 Next Chapter

## **Chapter 7 – List Indexing, Slicing & List Methods**

We'll learn:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])

numbers.append(60)
numbers.insert(2, 25)
numbers.remove(40)
numbers.pop()
numbers.sort()
numbers.reverse()
```

You'll learn:

* 📍 Positive indexing
* 📍 Negative indexing
* ✂️ List slicing
* ➕ `append()`
* 📥 `insert()`
* ❌ `remove()`
* 🗑️ `pop()`
* 🔄 `sort()`
* ↩️ `reverse()`

This chapter is one of the **most important** because **list methods are used in almost every Python application and interview**.
