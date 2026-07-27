# 📘 Python Lambda Functions – Final Revision & Interview Summary

## 🎯 Beginner to Interview Level (One-Shot Revision)

> **Goal:** Revise the complete Lambda Function topic in **10–15 minutes** before an interview.

---

# 📚 1. What is a Lambda Function?

## ✅ Definition

A **Lambda Function** is a **small anonymous (nameless) function** used for writing short, one-line functions.

* Uses the `lambda` keyword.
* Can take **any number of arguments**.
* Contains **only one expression**.
* Automatically returns the result.

---

## Syntax

```python
lambda arguments : expression
```

Example

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output

```
30
```

---

# 📚 2. Normal Function vs Lambda Function

## Normal Function

```python
def add(a, b):
    return a + b

print(add(10,20))
```

---

## Lambda Function

```python
add = lambda a, b: a + b

print(add(10,20))
```

---

## Difference

| Normal Function                 | Lambda Function       |
| ------------------------------- | --------------------- |
| Uses `def`                      | Uses `lambda`         |
| Has function name               | Usually anonymous     |
| Can contain multiple statements | Only one expression   |
| Uses `return`                   | Automatically returns |
| Best for large programs         | Best for short logic  |

---

# 📚 3. Lambda with Multiple Arguments

## One Argument

```python
square = lambda x: x*x

print(square(5))
```

Output

```
25
```

---

## Two Arguments

```python
add = lambda a,b: a+b

print(add(10,20))
```

---

## Three Arguments

```python
total = lambda a,b,c:a+b+c

print(total(10,20,30))
```

---

## Multiple Arguments

```python
calculate = lambda a,b,c,d,e:a+b+c+d+e

print(calculate(10,20,30,40,50))
```

---

# 📚 4. Lambda with Comparison Operators

| Operator | Example                      |
| -------- | ---------------------------- |
| `>`      | `lambda x:x>10`              |
| `<`      | `lambda x:x<50`              |
| `==`     | `lambda x:x==100`            |
| `!=`     | `lambda x:x!=10`             |
| `>=`     | `lambda age:age>=18`         |
| `<=`     | `lambda amount:amount<=5000` |

Example

```python
eligible = lambda age: age>=18

print(eligible(20))
```

Output

```
True
```

---

# 📚 5. Lambda with if-else

Syntax

```python
lambda arguments:
    value_if_true
    if condition
    else value_if_false
```

Example

```python
result = lambda marks:"Pass" if marks>=35 else "Fail"

print(result(90))
print(result(20))
```

Output

```
Pass
Fail
```

---

# 📚 6. Lambda with `and`

Example

```python
check = lambda age,citizen:(
"Eligible"
if age>=18 and citizen
else "Not Eligible"
)

print(check(20,True))
```

Output

```
Eligible
```

---

# 📚 7. Lambda with `or`

Example

```python
offer = lambda student,employee:(
"Discount"
if student or employee
else "No Discount"
)

print(offer(True,False))
```

Output

```
Discount
```

---

# 📚 8. Lambda with `map()`

## Purpose

Apply a function to **every element**.

Example

```python
numbers=[1,2,3,4]

result=list(map(lambda x:x*2,numbers))

print(result)
```

Output

```
[2,4,6,8]
```

---

# 📚 9. Lambda with `filter()`

## Purpose

Keep only matching elements.

Example

```python
numbers=[10,15,20,25,30]

result=list(filter(lambda x:x%2==0,numbers))

print(result)
```

Output

```
[10,20,30]
```

---

# 📚 10. Lambda with `sorted()`

## Purpose

Sort elements using a custom key.

Example

```python
names=["Rahul","Ajay","Venky"]

result=sorted(names,key=lambda x:len(x))

print(result)
```

Output

```
['Ajay','Rahul','Venky']
```

---

# 📚 11. `map()` vs `filter()` vs `sorted()`

| Function   | Purpose                 | Returns           |
| ---------- | ----------------------- | ----------------- |
| `map()`    | Transform every element | Modified iterable |
| `filter()` | Keep matching elements  | Filtered iterable |
| `sorted()` | Arrange elements        | Sorted list       |

---

# 📚 12. Real-Life Applications

### `map()`

* GST calculation
* Salary increment
* Uppercase conversion

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

# 📚 13. Common Beginner Mistakes

### ❌ Using `return`

Wrong

```python
lambda x:return x+1
```

Correct

```python
lambda x:x+1
```

---

### ❌ Writing Multiple Statements

Wrong

```python
lambda x:
    print(x)
    x+1
```

Lambda supports **only one expression**.

---

### ❌ Forgetting `list()`

Wrong

```python
map(lambda x:x+2,numbers)
```

Output

```
<map object ...>
```

Correct

```python
list(map(lambda x:x+2,numbers))
```

---

### ❌ Forgetting `key=`

Wrong

```python
sorted(names,lambda x:len(x))
```

Correct

```python
sorted(names,key=lambda x:len(x))
```

---

# 📚 14. Advantages of Lambda

✅ Short syntax

✅ Easy to read for small functions

✅ Works well with `map()`, `filter()`, `sorted()`

✅ Saves coding time

---

# 📚 15. Limitations of Lambda

❌ Only one expression

❌ Cannot contain loops directly

❌ Cannot contain multiple statements

❌ Not suitable for large logic

---

# 📚 16. Lambda vs def (When to Use?)

| Use Lambda        | Use `def`            |
| ----------------- | -------------------- |
| Small logic       | Large logic          |
| One-line function | Multiple statements  |
| `map()`           | Complex calculations |
| `filter()`        | Loops                |
| `sorted()`        | Recursion            |
| Short programs    | Big projects         |

---

# 🎓 Top 25 Interview Questions

### Basic

1. What is a Lambda Function?
2. Why is it called an anonymous function?
3. What keyword is used?
4. Can Lambda have a name?
5. What is its syntax?

### Arguments

6. Can Lambda accept multiple arguments?
7. Can it accept zero arguments?
8. Does Lambda automatically return values?

### Expressions

9. Why can Lambda contain only one expression?
10. Can Lambda contain multiple statements?
11. Can Lambda use loops?
12. Can Lambda use recursion?

### Conditions

13. Can Lambda use `if-else`?
14. Can Lambda use comparison operators?
15. Can Lambda use `and` and `or`?

### Built-in Functions

16. What is `map()`?
17. What is `filter()`?
18. What is `sorted()`?
19. Difference between `map()` and `filter()`?
20. Difference between `sorted()` and `sort()`?

### Comparison

21. Difference between Lambda and Normal Function?
22. When should you use Lambda?
23. What are the advantages?
24. What are the disadvantages?
25. Give one real-world use case of Lambda.

---

# ⭐ MCQs

### Q1

Which keyword creates a Lambda function?

A. `def`

B. `lambda`

C. `function`

D. `fun`

✅ **Answer:** **B**

---

### Q2

Lambda supports:

A. Multiple statements

B. One expression

C. Loops

D. Classes

✅ **Answer:** **B**

---

### Q3

Which function transforms every element?

A. `filter()`

B. `map()`

C. `sorted()`

D. `tuple()`

✅ **Answer:** **B**

---

### Q4

Which function filters elements?

A. `map()`

B. `filter()`

C. `sorted()`

D. `list()`

✅ **Answer:** **B**

---

### Q5

Which function sorts data?

A. `sort()`

B. `map()`

C. `filter()`

D. `sorted()`

✅ **Answer:** **D**

---

# 🧠 Memory Tricks

```text
lambda
   │
Anonymous Function
```

```text
One Expression
     │
Automatic Return
```

```text
map()
   │
Transform
```

```text
filter()
    │
Select
```

```text
sorted()
     │
Arrange
```

```text
if-else
    │
Decision
```

```text
and
 │
All True
```

```text
or
 │
Any One True
```

---

# 🧠 One-Page Mind Map

```text
                 PYTHON LAMBDA
                      │
        ┌─────────────┼─────────────┐
        │             │             │
    Anonymous     One Expression  Auto Return
        │
 ┌──────┼──────────────────────────┐
 │      │          │               │
Args  Compare   if-else       map()
 │      │          │               │
Any     > < ==   Ternary      Transform
Number  != >= <=
        │
 ┌──────┼──────────────┐
 │                     │
filter()           sorted()
 │                     │
Select             Arrange
Matching           Elements
```

---

# 🎯 30-Second Interview Revision

```text
✓ Lambda is an anonymous function.
✓ Uses the lambda keyword.
✓ Syntax: lambda arguments : expression.
✓ Can take any number of arguments.
✓ Supports only one expression.
✓ Automatically returns the result.
✓ Supports comparison operators.
✓ Supports if-else (ternary).
✓ Supports logical operators (and, or).
✓ Works perfectly with map(), filter(), and sorted().
✓ Best for short, simple functions.
✓ Use def for complex functions.
```

---

# 🏆 Perfect 2-Minute Interview Answer

> **"A Lambda Function is a small anonymous function created using the `lambda` keyword. It can accept any number of arguments but contains only one expression, and it automatically returns the result. Lambda functions are mainly used for short operations and are commonly combined with built-in functions like `map()` to transform data, `filter()` to select matching data, and `sorted()` to customize sorting. For large or complex logic, we generally use normal functions (`def`), while Lambda is preferred for concise, one-line operations."**

---

# 🎉 Congratulations!

You have now completed **Python Master Notes** for:

* ✅ Functions
* ✅ While Loops
* ✅ Lists
* ✅ Strings
* ✅ Sets
* ✅ Tuples
* ✅ Dictionaries
* ✅ Lambda Functions

These notes provide a strong foundation for **Python interviews**, **coding tests**, **automation**, **Django/Flask**, **data science**, and **real-world Python development**.
