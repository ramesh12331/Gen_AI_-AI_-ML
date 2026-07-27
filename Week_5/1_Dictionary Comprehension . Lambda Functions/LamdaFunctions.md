# 📘 Python Lambda Functions Master Handbook

# 📖 Chapter 1 – Lambda Functions with Multiple Arguments (Beginner to Interview Level)

> ⭐ In this chapter, you'll learn how Lambda functions work with **two arguments, three arguments, and multiple arguments**. These are common interview questions and help you write short, simple functions.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand Lambda functions with multiple arguments.
* ✅ Convert normal functions into Lambda functions.
* ✅ Pass two, three, or many arguments.
* ✅ Know when to use Lambda.
* ✅ Solve interview questions.

---

# 📖 What is a Lambda Function?

## ✅ Definition

A **Lambda Function** is an **anonymous (nameless) function** used to write **small, one-line functions**.

* Uses the `lambda` keyword.
* Can take **any number of arguments**.
* Can contain **only one expression**.
* Automatically returns the result.

---

## Syntax

```python
lambda arguments: expression
```

---

# 📖 Normal Function vs Lambda Function

## Normal Function

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

### Output

```text
30
```

---

## Lambda Function

```python
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```text
30
```

---

## Dry Run

```text
a = 10
b = 20

↓

a + b

↓

30
```

---

# 📖 Lambda Function with Two Arguments

## Normal Function

```python
def add(a, b):
    return a + b

print(add(12, 16))
```

### Output

```text
28
```

---

## Lambda Function

```python
add = lambda a, b: a + b

print(add(20, 30))
```

### Output

```text
50
```

---

## Memory Diagram

```text
Arguments

20   30

↓

Lambda

a + b

↓

50
```

---

# 📖 Lambda Function with Three Arguments

## Normal Function

```python
def total(a, b, c):
    return a + b + c

print(total(10, 20, 30))
```

### Output

```text
60
```

---

## Lambda Function

```python
result = lambda a, b, c: a + b + c

print(result(90, 80, 70))
```

### Output

```text
240
```

---

## Dry Run

```text
90 + 80 + 70

↓

240
```

---

# 📖 Lambda Function with Multiple Arguments

A Lambda function can accept **any number of arguments**, but it must contain **only one expression**.

---

## Example

```python
calculate = lambda a, b, c, d, e: a + b + c + d + e

print(calculate(90, 70, 80, 60, 50))
```

### Output

```text
350
```

---

## Dry Run

```text
90 + 70 + 80 + 60 + 50

↓

350
```

---

# 📖 Example – Student Details

Lambda can also return strings.

```python
student = lambda name, age, city: (
    f"Name: {name}, Age: {age}, City: {city}"
)

print(student("Ramesh", 30, "Hyderabad"))
```

### Output

```text
Name: Ramesh, Age: 30, City: Hyderabad
```

---

# 📖 More Examples

## Multiplication

```python
multiply = lambda a, b: a * b

print(multiply(10, 5))
```

Output

```text
50
```

---

## Division

```python
divide = lambda a, b: a / b

print(divide(20, 5))
```

Output

```text
4.0
```

---

## Largest Number

```python
largest = lambda a, b: a if a > b else b

print(largest(25, 40))
```

Output

```text
40
```

---

## Greeting Message

```python
greet = lambda name: f"Hello {name}"

print(greet("Ramesh"))
```

Output

```text
Hello Ramesh
```

---

# 📊 Normal Function vs Lambda Function

| Normal Function             | Lambda Function        |
| --------------------------- | ---------------------- |
| Uses `def`                  | Uses `lambda`          |
| Has function name           | Usually anonymous      |
| Multiple statements allowed | Only one expression    |
| Uses `return`               | Returns automatically  |
| Better for large programs   | Better for short logic |

---

# 🌍 Real-Life Applications

Lambda functions are used in:

* 📊 Data processing
* 🔍 Sorting data
* 🧹 Filtering data
* 🔄 Data transformation
* 🤖 Automation scripts
* 📈 Data Science
* 🌐 Web applications

---

# ⚠ Common Beginner Mistakes

## ❌ Mistake 1

Using `return` inside Lambda.

Wrong

```python
lambda a, b: return a + b
```

Correct

```python
lambda a, b: a + b
```

---

## ❌ Mistake 2

Writing multiple statements.

Wrong

```python
lambda a, b:
    c = a + b
    return c
```

Lambda supports only **one expression**.

---

## ❌ Mistake 3

Thinking Lambda cannot take multiple arguments.

Wrong

```text
Lambda accepts only one argument.
```

Correct

```python
lambda a, b, c, d: a + b + c + d
```

---

# 💡 Programmer Tips

Remember

```text
lambda

↓

One Expression
```

```text
Arguments

↓

Any Number
```

```text
return

↓

Automatic
```

```text
Small Logic

↓

Lambda
```

```text
Large Logic

↓

def Function
```

---

# 🎓 Interview Questions with Answers

### ❓1. What is a Lambda Function?

✅ **Answer:**

A Lambda Function is an anonymous function used to write short, one-line functions.

---

### ❓2. Can Lambda accept multiple arguments?

✅ **Answer:**

Yes. A Lambda function can accept any number of arguments.

---

### ❓3. Can Lambda contain multiple statements?

✅ **Answer:**

No. It can contain only one expression.

---

### ❓4. Does Lambda require the `return` keyword?

✅ **Answer:**

No. Lambda automatically returns the result of its expression.

---

### ❓5. When should you use Lambda?

✅ **Answer:**

Use Lambda for small, simple functions. Use `def` for larger functions with multiple statements.

---

# ⭐ MCQs

### Q1. Which keyword is used to create a Lambda function?

A. `function`

B. `lambda`

C. `def`

D. `fun`

✅ **Answer:** **B**

---

### Q2. How many expressions can a Lambda function contain?

A. One

B. Two

C. Three

D. Unlimited

✅ **Answer:** **A**

---

### Q3. Can a Lambda function accept five arguments?

A. No

B. Yes

✅ **Answer:** **B**

---

### Q4. Which function is better for long programs?

A. Lambda

B. `def`

C. Both are the same

D. None

✅ **Answer:** **B**

---

# 📝 Practice Programs

## ⭐ Easy

### Add Two Numbers

```python
add = lambda a, b: a + b

print(add(15, 25))
```

---

### Multiply Two Numbers

```python
multiply = lambda a, b: a * b

print(multiply(8, 6))
```

---

## ⭐⭐ Medium

### Find Largest Number

```python
largest = lambda a, b: a if a > b else b

print(largest(45, 60))
```

---

### Create Student Details

```python
student = lambda name, age, city: (
    f"Name: {name}, Age: {age}, City: {city}"
)

print(student("Ajay", 22, "Mumbai"))
```

---

## ⭐⭐⭐ Challenge

Create Lambda functions for:

1. Addition of four numbers.
2. Multiplication of three numbers.
3. Average of five numbers.
4. Return the smallest of two numbers.
5. Create an employee information string.

### Answer

```python
# Addition
add4 = lambda a, b, c, d: a + b + c + d
print(add4(1, 2, 3, 4))

# Multiplication
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))

# Average
average = lambda a, b, c, d, e: (a + b + c + d + e) / 5
print(average(10, 20, 30, 40, 50))

# Smallest
smallest = lambda a, b: a if a < b else b
print(smallest(15, 8))

# Employee Details
employee = lambda name, salary, city: (
    f"Employee: {name}, Salary: {salary}, City: {city}"
)
print(employee("Ramesh", 50000, "Hyderabad"))
```

---

# 📌 Chapter Summary

```text
            LAMBDA FUNCTIONS
                  │
      ┌───────────┼────────────┐
      │           │            │
   Two Args   Three Args   Multiple Args
      │           │            │
   a+b       a+b+c      a+b+c+d+e
                  │
           One Expression
                  │
          Automatic Return
```

---

# 🏆 Chapter Revision (30 Seconds)

```text
✓ Lambda = Anonymous Function
✓ Uses the lambda keyword
✓ Syntax: lambda arguments : expression
✓ Can accept any number of arguments
✓ Contains only one expression
✓ Automatically returns the result
✓ Best for small and simple functions
✓ Commonly used with map(), filter(), and sorted()
```

---

## 📖 Next Chapter

**Chapter 2 – Lambda with Comparison Operators, `if-else`, `and`, `or`, and Boolean Expressions**

You'll learn:

* ✅ `>`
* ✅ `<`
* ✅ `==`
* ✅ `!=`
* ✅ `>=`
* ✅ `<=`
* ✅ Ternary (`if-else`)
* ✅ `and` / `or`
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice programs
---
# 📘 Python Lambda Functions Master Handbook

# 📖 Chapter 2 – Lambda with Comparison Operators, `if-else`, `and`, `or` & Boolean Expressions (Beginner to Interview Level)

> ⭐ In this chapter, you'll learn how Lambda functions work with **comparison operators**, **Boolean values**, **conditional (if-else) expressions**, and **logical operators (`and`, `or`)**. These are frequently asked in Python interviews.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Use comparison operators with Lambda
* ✅ Return `True` or `False`
* ✅ Use `if-else` (ternary operator)
* ✅ Use `and` and `or`
* ✅ Build real-world decision-making functions
* ✅ Answer interview questions

---

# 📖 What are Comparison Operators?

Comparison operators compare two values and return a **Boolean** value.

| Operator | Meaning               | Example              |
| -------- | --------------------- | -------------------- |
| `>`      | Greater than          | `10 > 5` → `True`    |
| `<`      | Less than             | `5 < 2` → `False`    |
| `==`     | Equal to              | `10 == 10` → `True`  |
| `!=`     | Not equal to          | `10 != 5` → `True`   |
| `>=`     | Greater than or equal | `18 >= 18` → `True`  |
| `<=`     | Less than or equal    | `50 <= 100` → `True` |

---

# 📖 1. Greater Than (`>`)

```python
greater = lambda x: x > 10

print(greater(15))
print(greater(5))
```

### Output

```text
True
False
```

### Dry Run

```text
Input = 15

15 > 10

↓

True
```

---

# 📖 2. Less Than (`<`)

```python
less = lambda x: x < 50

print(less(40))
print(less(60))
```

### Output

```text
True
False
```

---

# 📖 3. Equal To (`==`)

```python
equal = lambda x: x == 100

print(equal(100))
print(equal(50))
```

### Output

```text
True
False
```

---

# 📖 4. Not Equal To (`!=`)

```python
not_equal = lambda x: x != 10

print(not_equal(5))
print(not_equal(10))
```

### Output

```text
True
False
```

---

# 📖 5. Greater Than or Equal (`>=`)

### Real-Life Example: Voting Eligibility

```python
eligible = lambda age: age >= 18

print(eligible(20))
print(eligible(15))
```

### Output

```text
True
False
```

---

# 📖 6. Less Than or Equal (`<=`)

### Real-Life Example: Discount

```python
discount = lambda amount: amount <= 5000

print(discount(4500))
print(discount(7000))
```

### Output

```text
True
False
```

---

# 📖 Lambda with `if-else`

A Lambda function cannot use a normal `if` statement, but it **can use a ternary expression**.

## Syntax

```python
lambda arguments: value_if_true if condition else value_if_false
```

---

## Example

```python
result = lambda marks: "Pass" if marks >= 35 else "Fail"

print(result(90))
print(result(20))
```

### Output

```text
Pass
Fail
```

---

## Dry Run

```text
Marks = 90

90 >= 35

↓

Pass
```

---

# 📖 Lambda with `and`

`and` returns **True only if all conditions are True**.

### Example

```python
check = lambda age, citizen: (
    "Eligible"
    if age >= 18 and citizen
    else "Not Eligible"
)

print(check(20, True))
print(check(16, True))
print(check(25, False))
```

### Output

```text
Eligible
Not Eligible
Not Eligible
```

---

## Truth Table

| Age ≥ 18 | Citizen | Result       |
| -------- | ------- | ------------ |
| ✅        | ✅       | Eligible     |
| ❌        | ✅       | Not Eligible |
| ✅        | ❌       | Not Eligible |
| ❌        | ❌       | Not Eligible |

---

# 📖 Lambda with `or`

`or` returns **True if at least one condition is True**.

### Example

```python
offer = lambda student, employee: (
    "Discount"
    if student or employee
    else "No Discount"
)

print(offer(True, False))
print(offer(False, True))
print(offer(False, False))
```

### Output

```text
Discount
Discount
No Discount
```

---

## Truth Table

| Student | Employee | Result      |
| ------- | -------- | ----------- |
| ✅       | ❌        | Discount    |
| ❌       | ✅        | Discount    |
| ❌       | ❌        | No Discount |

---

# 📖 More Real-Life Examples

## Even Number

```python
even = lambda x: x % 2 == 0

print(even(8))
print(even(5))
```

Output

```text
True
False
```

---

## Adult or Minor

```python
status = lambda age: "Adult" if age >= 18 else "Minor"

print(status(20))
print(status(15))
```

Output

```text
Adult
Minor
```

---

## Largest Number

```python
largest = lambda a, b: a if a > b else b

print(largest(20, 40))
```

Output

```text
40
```

---

## Pass with Attendance

```python
result = lambda marks, attendance: (
    "Pass"
    if marks >= 35 and attendance >= 75
    else "Fail"
)

print(result(80, 90))
print(result(80, 60))
```

Output

```text
Pass
Fail
```

---

# 📊 Lambda vs Normal Function

| Normal Function        | Lambda Function       |
| ---------------------- | --------------------- |
| Uses `def`             | Uses `lambda`         |
| Multiple statements    | One expression only   |
| Uses `return`          | Returns automatically |
| Best for complex logic | Best for short logic  |

---

# 🌍 Real-Life Applications

Lambda with conditions is commonly used for:

* 👨‍🎓 Student grading
* 🗳️ Voting eligibility
* 🛒 Discount systems
* 🏦 Loan eligibility
* 🎟️ Ticket booking
* 📊 Data filtering

---

# ⚠ Common Beginner Mistakes

### ❌ Using `return`

Wrong

```python
lambda x: return x > 10
```

Correct

```python
lambda x: x > 10
```

---

### ❌ Forgetting `else`

Wrong

```python
lambda x: "Pass" if x >= 35
```

Correct

```python
lambda x: "Pass" if x >= 35 else "Fail"
```

---

### ❌ Using multiple statements

Wrong

```python
lambda x:
    print(x)
    x + 1
```

Lambda supports only **one expression**.

---

# 💡 Programmer Tips

Remember

```text
lambda

↓

One Expression
```

```text
>

↓

Greater Than
```

```text
>=

↓

Eligibility
```

```text
if-else

↓

Decision Making
```

```text
and

↓

All Conditions True
```

```text
or

↓

Any One Condition True
```

---

# 🎓 Interview Questions

### 1. Can a Lambda return `True` or `False`?

✅ Yes. Comparison operators return Boolean values.

---

### 2. Can Lambda use `if-else`?

✅ Yes, by using the ternary expression.

---

### 3. Can Lambda use `and` and `or`?

✅ Yes.

---

### 4. Can Lambda contain multiple `if` statements?

❌ No. It supports only one expression.

---

### 5. What is the syntax of Lambda?

```python
lambda arguments: expression
```

---

# ⭐ MCQs

### Q1

```python
greater = lambda x: x > 10

print(greater(5))
```

A. True

B. False

C. 5

D. Error

✅ **Answer:** **B**

---

### Q2

Which operator checks equality?

A. `=`

B. `==`

C. `!=`

D. `>=`

✅ **Answer:** **B**

---

### Q3

Which keyword is required in Lambda's conditional expression?

A. `elif`

B. `return`

C. `else`

D. `pass`

✅ **Answer:** **C**

---

### Q4

`and` returns `True` when:

A. Any one condition is True

B. All conditions are True

C. Both conditions are False

D. None

✅ **Answer:** **B**

---

### Q5

`or` returns `True` when:

A. All conditions are True

B. At least one condition is True

C. All conditions are False

D. None

✅ **Answer:** **B**

---

# 📝 Practice Programs

## ⭐ Easy

```python
# Greater than 100
greater = lambda x: x > 100
print(greater(150))

# Even number
even = lambda x: x % 2 == 0
print(even(12))
```

---

## ⭐⭐ Medium

```python
# Adult or Minor
status = lambda age: "Adult" if age >= 18 else "Minor"
print(status(16))

# Largest number
largest = lambda a, b: a if a > b else b
print(largest(25, 30))
```

---

## ⭐⭐⭐ Challenge

```python
# Vote eligibility
vote = lambda age: age >= 18
print(vote(21))

# Discount
discount = lambda student, employee: (
    "Discount" if student or employee else "No Discount"
)
print(discount(False, True))

# Pass with attendance
result = lambda marks, attendance: (
    "Pass"
    if marks >= 35 and attendance >= 75
    else "Fail"
)
print(result(70, 80))
```

---

# 📌 Chapter Summary

```text
             LAMBDA CONDITIONS
                    │
      ┌─────────────┼─────────────┐
      │             │             │
 Comparison      if-else      Logical
      │             │             │
 > < == !=     Ternary      and / or
 >= <=
      │
 Boolean Output
(True / False)
```

---

# 🏆 Congratulations!

You have completed **Python Lambda Functions – Chapter 2: Comparison Operators, `if-else`, `and`, `or`, and Boolean Expressions**.

### ✅ You learned:

* Comparison operators (`>`, `<`, `==`, `!=`, `>=`, `<=`)
* Boolean return values
* Ternary (`if-else`) in Lambda
* Logical operators (`and`, `or`)
* Real-world examples
* Interview questions
* MCQs
* Practice programs

---

# 📖 Next Chapter

## **Chapter 3 – Lambda with `map()`, `filter()`, and `sorted()`**

You'll learn:

* ✅ `map()` with Lambda
* ✅ `filter()` with Lambda
* ✅ `sorted()` with Lambda
* ✅ Sorting dictionaries and lists
* ✅ Interview questions
* ✅ MCQs
* ✅ Practice programs
---
# 📘 Python Lambda Functions Master Handbook

# 📖 Chapter 3 – Lambda with `map()`, `filter()` and `sorted()` (Beginner to Interview Level)

> ⭐ **`map()`**, **`filter()`**, and **`sorted()`** are the **most frequently asked Lambda interview topics**. They are widely used in **Data Science**, **Automation**, **Web Development**, and **Coding Interviews**.

---

# 🎯 Learning Objectives

After completing this chapter, you will be able to:

* ✅ Understand `map()`
* ✅ Understand `filter()`
* ✅ Understand `sorted()`
* ✅ Use Lambda with all three
* ✅ Solve interview questions

---

# 📖 1. `map()` Function

## ✅ Definition

The `map()` function applies a function to **every element** in an iterable and returns a **map object**.

Usually, we convert it into a list.

---

## Syntax

```python
map(function, iterable)
```

or

```python
list(map(function, iterable))
```

---

# 📖 Example 1 – Add 2 to Every Number

## Without Lambda

```python
numbers = [12, 34, 56]

result = []

for num in numbers:
    result.append(num + 2)

print(result)
```

### Output

```text
[14, 36, 58]
```

---

## Using Lambda

```python
numbers = [12, 34, 56]

result = list(map(lambda x: x + 2, numbers))

print(result)
```

### Output

```text
[14, 36, 58]
```

---

## Dry Run

```text
Numbers

12   34   56

↓

Lambda

x + 2

↓

14   36   58

↓

List
```

---

# 📖 Example 2 – Square Every Number

```python
numbers = [1,2,3,4,5]

result = list(map(lambda x:x*x, numbers))

print(result)
```

### Output

```text
[1,4,9,16,25]
```

---

# 📖 Example 3 – Convert to Uppercase

```python
names = ["python","java","sql"]

result = list(map(lambda x:x.upper(), names))

print(result)
```

### Output

```text
['PYTHON', 'JAVA', 'SQL']
```

---

# 📖 Example 4 – Calculate GST

```python
prices = [100,200,300]

gst = list(map(lambda x:x+18, prices))

print(gst)
```

### Output

```text
[118,218,318]
```

---

# 📖 2. `filter()` Function

## ✅ Definition

`filter()` returns only those elements that satisfy a condition.

---

## Syntax

```python
filter(function, iterable)
```

Usually converted to a list.

```python
list(filter(function, iterable))
```

---

# 📖 Example 1 – Even Numbers

```python
numbers = [10,15,20,25,30]

result = list(filter(lambda x:x%2==0, numbers))

print(result)
```

### Output

```text
[10,20,30]
```

---

## Dry Run

```text
10 ✓

15 ✗

20 ✓

25 ✗

30 ✓

↓

[10,20,30]
```

---

# 📖 Example 2 – Greater Than 50

```python
numbers = [20,60,80,15,45]

result = list(filter(lambda x:x>50, numbers))

print(result)
```

### Output

```text
[60,80]
```

---

# 📖 Example 3 – Long Names

```python
names = ["Ajay","Rahul","An","Python"]

result = list(filter(lambda x:len(x)>4, names))

print(result)
```

### Output

```text
['Rahul', 'Python']
```

---

# 📖 Example 4 – Passed Students

```python
marks = [25,40,90,60,18]

passed = list(filter(lambda x:x>=35, marks))

print(passed)
```

### Output

```text
[40,90,60]
```

---

# 📖 3. `sorted()` Function

## ✅ Definition

`sorted()` sorts an iterable and returns a **new sorted list**.

---

## Syntax

```python
sorted(iterable, key=function)
```

---

# 📖 Example 1 – Sort Numbers

```python
numbers = [40,10,20,30]

result = sorted(numbers)

print(result)
```

### Output

```text
[10,20,30,40]
```

---

# 📖 Example 2 – Descending Order

```python
numbers = [40,10,20,30]

result = sorted(numbers, reverse=True)

print(result)
```

### Output

```text
[40,30,20,10]
```

---

# 📖 Example 3 – Sort by Length

```python
names = ["Rahul","Ajay","Venky","Annu"]

result = sorted(names, key=lambda x:len(x))

print(result)
```

### Output

```text
['Ajay','Annu','Rahul','Venky']
```

---

## Dry Run

```text
Ajay → 4

Annu → 4

Rahul → 5

Venky → 5

↓

Sorted by Length
```

---

# 📖 Example 4 – Sort Dictionary by Marks

```python
students = [

    {"name":"Ajay","marks":80},

    {"name":"Rahul","marks":95},

    {"name":"Annu","marks":70}

]

result = sorted(students, key=lambda x:x["marks"])

print(result)
```

### Output

```text
[
 {'name':'Annu','marks':70},
 {'name':'Ajay','marks':80},
 {'name':'Rahul','marks':95}
]
```

---

# 📊 Difference Between `map()`, `filter()`, and `sorted()`

| Function   | Purpose                | Returns           |
| ---------- | ---------------------- | ----------------- |
| `map()`    | Modify every element   | Modified iterable |
| `filter()` | Keep matching elements | Filtered iterable |
| `sorted()` | Arrange elements       | Sorted list       |

---

# 🌍 Real-Life Applications

### `map()`

* Add GST to prices
* Convert names to uppercase
* Calculate salaries

### `filter()`

* Passed students
* Eligible voters
* Even numbers
* High salaries

### `sorted()`

* Students by marks
* Employees by salary
* Products by price
* Files by name

---

# ⚠ Common Beginner Mistakes

## ❌ Forgetting `list()`

Wrong

```python
result = map(lambda x:x+2, numbers)

print(result)
```

Output

```text
<map object at 0x...>
```

Correct

```python
print(list(result))
```

---

## ❌ Using `filter()` to Modify Values

Wrong thinking:

```python
filter() changes values
```

Actually:

```text
filter()

↓

Keeps or Removes

It does NOT modify values.
```

---

## ❌ Forgetting `key=`

Wrong

```python
sorted(names, lambda x:len(x))
```

Correct

```python
sorted(names, key=lambda x:len(x))
```

---

# 💡 Programmer Tips

Remember

```text
map()

↓

Transform

Every Item
```

```text
filter()

↓

Select

Matching Items
```

```text
sorted()

↓

Arrange

Ascending / Descending
```

---

# 🎓 Interview Questions

### 1. What does `map()` do?

✅ Applies a function to every element.

---

### 2. What does `filter()` do?

✅ Returns only elements that satisfy a condition.

---

### 3. What does `sorted()` return?

✅ A new sorted list.

---

### 4. Why do we use `list(map())`?

✅ Because `map()` returns a map object, not a list.

---

### 5. Does `filter()` modify values?

❌ No.

It only filters elements.

---

### 6. What is the purpose of `key=` in `sorted()`?

✅ It specifies how sorting should be performed.

---

# ⭐ MCQs

### Q1

Which function transforms every element?

A. `filter()`

B. `map()`

C. `sorted()`

D. `lambda`

✅ **Answer:** **B**

---

### Q2

Which function removes unwanted elements?

A. `map()`

B. `filter()`

C. `sorted()`

D. `tuple()`

✅ **Answer:** **B**

---

### Q3

Which function returns a sorted list?

A. `map()`

B. `filter()`

C. `sorted()`

D. `sort()`

✅ **Answer:** **C**

---

### Q4

Which parameter customizes sorting?

A. `func`

B. `key`

C. `value`

D. `sort`

✅ **Answer:** **B**

---

# 📝 Practice Programs

## ⭐ Easy

```python
# Double every number
numbers = [1,2,3,4,5]

print(list(map(lambda x:x*2, numbers)))
```

---

```python
# Square every number

print(list(map(lambda x:x*x, numbers)))
```

---

## ⭐⭐ Medium

```python
# Filter Odd Numbers

print(list(filter(lambda x:x%2!=0, numbers)))
```

---

```python
# Filter Greater Than 20

nums = [5,15,25,35]

print(list(filter(lambda x:x>20, nums)))
```

---

## ⭐⭐⭐ Challenge

```python
# Sort Employees by Salary

employees = [

    {"name":"Ajay","salary":50000},

    {"name":"Rahul","salary":70000},

    {"name":"Annu","salary":45000}

]

result = sorted(
    employees,
    key=lambda x:x["salary"]
)

print(result)
```

---

# 📌 Chapter Summary

```text
                LAMBDA + BUILT-IN FUNCTIONS
                        │
        ┌───────────────┼────────────────┐
        │               │                │
      map()          filter()        sorted()
        │               │                │
 Modify Every      Keep Matching      Arrange
    Element          Elements          Elements
        │
 Commonly Used in
 Data Science, Automation,
 Web Development
```

---

# 🏆 Congratulations!

You have completed **Python Lambda Functions – Chapter 3: `map()`, `filter()`, and `sorted()`**.

### ✅ You learned:

* `map()` with Lambda
* `filter()` with Lambda
* `sorted()` with Lambda
* Real-world examples
* Interview questions
* MCQs
* Practice programs

---

# 📖 Next Chapter

## **Chapter 4 – Final Revision & Interview Summary of Lambda Functions**

We'll cover:

* ✅ Complete Lambda cheat sheet
* ✅ Lambda vs Normal Function
* ✅ `map()` vs `filter()` vs `sorted()`
* ✅ Top 30 interview questions
* ✅ Common mistakes
* ✅ Memory tricks
* ✅ One-page interview revision sheet
* ✅ Final interview preparation for Lambda Functions
