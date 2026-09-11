# 🧮 NumPy Operations — Beginner Guide

This section covers:

1. ⚡ Vectorized Operations
2. 🔢 Scalar Operations
3. 🔍 Relational Operators
4. 🔵 Boolean Indexing
5. 🎯 Fancy Indexing
6. 📍 1D Indexing
7. ✂️ 1D Slicing
8. 📊 2D Indexing
9. ✂️ 2D Slicing
10. 🧮 Mathematical Functions
11. 📉 `argmin()` and `argmax()`
12. 🧭 `axis`
13. 🔄 `round()`, `ceil()`, `floor()`
14. ✖️ Dot Product

---

# 1. ⚡ Vectorized Operations

## 📖 Definition

**Vectorized operation** means performing an operation on all elements of a NumPy array at once, without explicitly writing a `for` loop.

### Example

```python
import numpy as np

a = np.array([3, 4, 5])
b = np.array([6, 7, 8])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## 🔤 Syntax

```python
array1 + array2
array1 - array2
array1 * array2
array1 / array2
```

---

## 🧮 Mathematical Formula

### Addition

```text
a + b = [a₁+b₁, a₂+b₂, a₃+b₃]
```

### Subtraction

```text
a - b = [a₁-b₁, a₂-b₂, a₃-b₃]
```

### Multiplication

```text
a × b = [a₁×b₁, a₂×b₂, a₃×b₃]
```

### Division

```text
a / b = [a₁/b₁, a₂/b₂, a₃/b₃]
```

---

## 🔍 Dry Run

Given:

```text
a = [3, 4, 5]
b = [6, 7, 8]
```

### ➕ Addition

```text
[3, 4, 5]
[6, 7, 8]
```

Element by element:

```text
3 + 6 = 9
4 + 7 = 11
5 + 8 = 13
```

Result:

```text
[9, 11, 13]
```

### ➖ Subtraction

```text
3 - 6 = -3
4 - 7 = -3
5 - 8 = -3
```

Result:

```text
[-3, -3, -3]
```

### ✖️ Multiplication

```text
3 × 6 = 18
4 × 7 = 28
5 × 8 = 40
```

Result:

```text
[18, 28, 40]
```

### ➗ Division

```text
3 / 6 = 0.5
4 / 7 = 0.57142857
5 / 8 = 0.625
```

Result:

```text
[0.5, 0.57142857, 0.625]
```

---

## 🖥️ Output

```text
[ 9 11 13]
[-3 -3 -3]
[18 28 40]
[0.5        0.57142857 0.625     ]
```

### 🧠 Remember

```text
Array + Array
      ↓
Element + Element
```

---

# 2. 🔢 Scalar Operations

## 📖 Definition

A **scalar** is a single value.

When we perform an operation between an array and a scalar, NumPy applies the operation to **every element**.

Example:

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)
```

---

## 🔤 Syntax

```python
array + scalar
array - scalar
array * scalar
array / scalar
```

---

## 🔍 Dry Run

Given:

```text
arr = [1, 2, 3, 4, 5]
scalar = 10
```

### Addition

```text
1 + 10 = 11
2 + 10 = 12
3 + 10 = 13
4 + 10 = 14
5 + 10 = 15
```

Result:

```text
[11 12 13 14 15]
```

### Subtraction

```text
1 - 10 = -9
2 - 10 = -8
3 - 10 = -7
4 - 10 = -6
5 - 10 = -5
```

Result:

```text
[-9 -8 -7 -6 -5]
```

### Multiplication

```text
1 × 10 = 10
2 × 10 = 20
3 × 10 = 30
4 × 10 = 40
5 × 10 = 50
```

Result:

```text
[10 20 30 40 50]
```

### Division

```text
1 / 10 = 0.1
2 / 10 = 0.2
3 / 10 = 0.3
4 / 10 = 0.4
5 / 10 = 0.5
```

---

## 🖥️ Output

```text
[11 12 13 14 15]
[-9 -8 -7 -6 -5]
[10 20 30 40 50]
[0.1 0.2 0.3 0.4 0.5]
```

### 🧠 Visual

```text
[1  2  3  4  5]
 ↓  ↓  ↓  ↓  ↓
+10 +10 +10 +10 +10
 ↓  ↓  ↓  ↓  ↓
[11 12 13 14 15]
```

---

# 3. 🔍 Relational Operators

## 📖 Definition

Relational operators compare array elements with a condition.

Common operators:

| Operator | Meaning               |
| -------- | --------------------- |
| `>`      | Greater than          |
| `<`      | Less than             |
| `==`     | Equal to              |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |
| `!=`     | Not equal             |

---

## 💻 Example

```python
arr = np.array([1, 2, 11, 4, 2, 3, 1])

print(arr[arr > 8])
print(arr[arr < 5])
print(arr[arr == 2])
```

---

## 🔍 Dry Run: `arr > 8`

```text
Array:

[1, 2, 11, 4, 2, 3, 1]

Check > 8:

1  > 8 → False
2  > 8 → False
11 > 8 → True
4  > 8 → False
2  > 8 → False
3  > 8 → False
1  > 8 → False
```

Boolean result:

```text
[False False True False False False False]
```

NumPy selects the `True` value:

```text
[11]
```

---

## 🖥️ Output

```text
[11]
[1 2 4 2 3 1]
[2 2]
```

---

# 4. 🔵 Boolean Indexing

## 📖 Definition

**Boolean indexing** means selecting array values using `True` and `False` conditions.

---

## 🔤 Syntax

```python
array[condition]
```

---

## 💻 Example

```python
arr = np.array([10, 20, 30, 40, 50])

condition = arr > 25

print(condition)
print(arr[condition])
```

---

## 🔍 Dry Run

```text
arr = [10 20 30 40 50]
```

Condition:

```text
arr > 25
```

Check each value:

```text
10 > 25 → False
20 > 25 → False
30 > 25 → True
40 > 25 → True
50 > 25 → True
```

Therefore:

```text
condition =
[False False True True True]
```

Now:

```python
arr[condition]
```

means:

```text
Take only values where condition = True
```

So:

```text
30
40
50
```

---

## 🖥️ Output

```text
[False False  True  True  True]
[30 40 50]
```

### 🧠 Remember

```text
Condition
   ↓
True / False
   ↓
Select True values
```

---

# 5. 🎯 Fancy Indexing

## 📖 Definition

**Fancy indexing** allows us to select multiple elements using their indexes.

---

## 🔤 Syntax

```python
array[[index1, index2, index3]]
```

---

## 💻 Example

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr[[0, 2, 4]]

print(result)
```

---

## 🔍 Dry Run

```text
Index:  0   1   2   3   4
Value: 10  20  30  40  50
```

We request:

```text
[0, 2, 4]
```

Therefore:

```text
Index 0 → 10
Index 2 → 30
Index 4 → 50
```

Result:

```text
[10 30 50]
```

---

## 🖥️ Output

```text
[10 30 50]
```

### 🧠 Remember

```text
Fancy Indexing
      ↓
Give multiple indexes
      ↓
Get multiple values
```

---

# 6. 📍 1D Indexing

## 📖 Definition

**Indexing** means accessing a specific element using its position.

Python uses **zero-based indexing**.

---

## 🔤 Syntax

```python
array[index]
```

---

## 💻 Example

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])
```

---

## 🔍 Dry Run

```text
Index:  0   1   2   3   4
Value: 10  20  30  40  50
```

### `arr[0]`

```text
→ 10
```

### `arr[2]`

```text
→ 30
```

### `arr[-1]`

Negative index starts from the end:

```text
-5  -4  -3  -2  -1
10  20  30  40  50
```

Therefore:

```text
arr[-1] → 50
```

---

## 🖥️ Output

```text
10
30
50
```

---

# 7. ✂️ 1D Slicing

## 📖 Definition

**Slicing** means selecting a range of elements.

---

## 🔤 Syntax

```python
array[start:stop:step]
```

⚠️ `stop` is not included.

---

## 💻 Example

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[-2:])
print(arr[::2])
```

---

## 🔍 Dry Run

### `arr[1:4]`

Indexes:

```text
1 → 20
2 → 30
3 → 40
```

Result:

```text
[20 30 40]
```

### `arr[:3]`

Means:

```text
Start from beginning
Stop before index 3
```

Result:

```text
[10 20 30]
```

### `arr[-2:]`

Means:

```text
Start from second-last element
Go until the end
```

Result:

```text
[40 50]
```

### `arr[::2]`

Means:

```text
Start = beginning
Stop = end
Step = 2
```

Indexes:

```text
0 → 10
2 → 30
4 → 50
```

Result:

```text
[10 30 50]
```

---

## 🖥️ Output

```text
[20 30 40]
[10 20 30]
[40 50]
[10 30 50]
```

---

# 8. 📊 2D Indexing

## 📖 Definition

2D indexing is used to access a value using:

```text
row + column
```

---

## 🔤 Syntax

```python
array[row, column]
```

---

## 💻 Example

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1])
print(arr[1, 2])
```

---

## 🔍 Dry Run

```text
          Column
          0   1   2
        ┌───┬───┬───┐
Row 0   │10 │20 │30 │
        ├───┼───┼───┤
Row 1   │40 │50 │60 │
        └───┴───┴───┘
```

### `arr[0,1]`

```text
Row = 0
Column = 1

→ 20
```

### `arr[1,2]`

```text
Row = 1
Column = 2

→ 60
```

---

## 🖥️ Output

```text
20
60
```

---

# 9. ✂️ 2D Slicing

## 📖 Definition

2D slicing selects a range of rows and columns.

---

## 🔤 Syntax

```python
array[row_start:row_stop, column_start:column_stop]
```

---

## 💻 Example

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[:2])
print(arr[:, :2])
print(arr[1:3, 1:3])
```

---

## 🔍 Dry Run

### `arr[:2]`

Take first two rows:

```text
[10 20 30]
[40 50 60]
```

Result:

```text
[[10 20 30]
 [40 50 60]]
```

---

### `arr[:, :2]`

Here:

```text
:
↓
All rows

:2
↓
Columns 0 and 1
```

Result:

```text
[[10 20]
 [40 50]
 [70 80]]
```

---

### `arr[1:3, 1:3]`

Rows:

```text
1 and 2
```

Columns:

```text
1 and 2
```

Selected:

```text
50 60
80 90
```

Result:

```text
[[50 60]
 [80 90]]
```

---

# 10. 🧮 Mathematical Functions

NumPy provides mathematical functions for arrays.

---

## 🔹 `np.sum()`

### Definition

Adds all elements.

### Formula

```text
Sum = x₁ + x₂ + x₃ + ... + xₙ
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
```

Calculation:

```text
10 + 20 + 30 + 40 + 50
= 150
```

Output:

```text
150
```

---

# 🔹 `np.min()`

Returns the smallest value.

```python
np.min(arr)
```

For:

```text
[10 20 30 40 50]
```

Result:

```text
10
```

---

# 🔹 `np.max()`

Returns the largest value.

```python
np.max(arr)
```

Result:

```text
50
```

---

# 🔹 `np.prod()`

Returns the product of all elements.

### Formula

```text
Product = x₁ × x₂ × x₃ × ... × xₙ
```

For:

```text
[10, 20, 30, 40, 50]
```

Calculation:

```text
10 × 20 × 30 × 40 × 50
= 12,000,000
```

---

# 🔹 `np.mean()`

Returns the average.

### Formula

```text
Mean = Sum of values / Number of values
```

For:

```text
10, 20, 30, 40, 50
```

```text
Mean = 150 / 5
     = 30
```

Output:

```text
30.0
```

---

# 🔹 `np.median()`

Returns the middle value after arranging values in order.

```text
10 20 30 40 50
       ↑
     Median
```

Result:

```text
30.0
```

---

# 🔹 `np.std()`

Returns the standard deviation.

### Formula

For population standard deviation:

```text
σ = √( Σ(x - μ)² / N )
```

Where:

```text
μ = mean
N = number of values
```

For the given array:

```text
[10, 20, 30, 40, 50]
```

Mean:

```text
30
```

Differences:

```text
10 - 30 = -20
20 - 30 = -10
30 - 30 =   0
40 - 30 =  10
50 - 30 =  20
```

Squares:

```text
400
100
0
100
400
```

Sum:

```text
1000
```

Variance:

```text
1000 / 5 = 200
```

Standard deviation:

```text
√200
≈ 14.1421
```

---

## 🖥️ Complete Output

```text
150
10
50
12000000
30.0
30.0
14.142135623730951
```

---

# 11. 📉 `argmin()` and `argmax()`

## 📖 Definition

These functions return **indexes**, not values.

```text
argmin() → index of minimum
argmax() → index of maximum
```

---

## 💻 Example

```python
arr = np.array([10, 5, 30, 2, 50])

print(np.argmin(arr))
print(np.argmax(arr))
```

---

## 🔍 Dry Run

```text
Index:  0   1   2   3   4
Value: 10   5  30   2  50
```

Minimum:

```text
Minimum value = 2
Index = 3
```

Therefore:

```python
np.argmin(arr)
```

returns:

```text
3
```

Maximum:

```text
Maximum value = 50
Index = 4
```

Therefore:

```python
np.argmax(arr)
```

returns:

```text
4
```

---

## 🖥️ Output

```text
3
4
```

### 🧠 Important

```text
min()     → value
argmin()  → index

max()     → value
argmax()  → index
```

---

# 12. 🧭 Axis

## 📖 Definition

`axis` tells NumPy **which direction to perform an operation**.

Consider:

```text
arr =
[[10 20 30]
 [40 50 60]]
```

---

## 🔹 `axis=0`

For this 2D example, the operation is performed **down the rows**, giving a column-wise result.

```python
np.sum(arr, axis=0)
```

### 🔍 Dry Run

```text
Column 1:
10 + 40 = 50

Column 2:
20 + 50 = 70

Column 3:
30 + 60 = 90
```

Result:

```text
[50 70 90]
```

---

## 🔹 `axis=1`

The operation is performed **across the columns**, giving a row-wise result.

```python
np.sum(arr, axis=1)
```

### 🔍 Dry Run

Row 1:

```text
10 + 20 + 30 = 60
```

Row 2:

```text
40 + 50 + 60 = 150
```

Result:

```text
[60 150]
```

---

## 🧠 Easy Trick

```text
axis=0
   ↓
Column-wise result

axis=1
   ↓
Row-wise result
```

---

# 13. 🔄 `round()`, `ceil()` and `floor()`

Given:

```python
arr = np.array([1.2, 2.7, 3.5, 4.9])
```

---

## 🔹 `np.round()`

### Definition

Rounds values to the nearest integer.

```python
np.round(arr)
```

Result:

```text
[1. 3. 4. 5.]
```

---

## 🔹 `np.ceil()`

### Definition

Returns the smallest integer greater than or equal to each value.

```python
np.ceil(arr)
```

Result:

```text
[2. 3. 4. 5.]
```

Examples:

```text
ceil(1.2) = 2
ceil(2.7) = 3
ceil(3.5) = 4
ceil(4.9) = 5
```

---

## 🔹 `np.floor()`

### Definition

Returns the largest integer less than or equal to each value.

```python
np.floor(arr)
```

Result:

```text
[1. 2. 3. 4.]
```

---

## 🧠 Memory Trick

```text
ROUND
  ↓
Nearest

CEIL
  ↓
UP ↑

FLOOR
  ↓
DOWN ↓
```

---

# 14. ✖️ Dot Product

## 📖 Definition

The **dot product** combines rows of the first matrix with columns of the second matrix using multiplication and addition.

---

## 🔤 Syntax

```python
np.dot(array1, array2)
```

---

## 💻 Example

```python
arr = np.array([
    [2, 3],
    [4, 5]
])

a1 = np.array([
    [1, 8],
    [2, 9]
])

result = np.dot(arr, a1)

print(result)
```

---

# 🧮 Mathematical Formula

For two 2 × 2 matrices:

```text
A = [a b]
    [c d]

B = [e f]
    [g h]
```

The result is:

```text
A × B =

[a×e + b×g    a×f + b×h]
[c×e + d×g    c×f + d×h]
```

---

# 🔍 Complete Dry Run

Given:

```text
A = [2 3]
    [4 5]

B = [1 8]
    [2 9]
```

---

## Position `[0,0]`

Take:

```text
First row of A
[2 3]

First column of B
[1]
[2]
```

Multiply and add:

```text
(2 × 1) + (3 × 2)

= 2 + 6

= 8
```

---

## Position `[0,1]`

First row of A:

```text
[2 3]
```

Second column of B:

```text
[8]
[9]
```

Calculation:

```text
(2 × 8) + (3 × 9)

= 16 + 27

= 43
```

---

## Position `[1,0]`

Second row of A:

```text
[4 5]
```

First column of B:

```text
[1]
[2]
```

Calculation:

```text
(4 × 1) + (5 × 2)

= 4 + 10

= 14
```

---

## Position `[1,1]`

Second row of A:

```text
[4 5]
```

Second column of B:

```text
[8]
[9]
```

Calculation:

```text
(4 × 8) + (5 × 9)

= 32 + 45

= 77
```

---

## 🖥️ Final Output

```text
[[ 8 43]
 [14 77]]
```

### 👀 Visual

```text
        B
      ┌───────┐
      │ 1   8 │
      │ 2   9 │
      └───────┘

A
┌───────┐
│ 2   3 │
│ 4   5 │
└───────┘

2×1 + 3×2 = 8
2×8 + 3×9 = 43

4×1 + 5×2 = 14
4×8 + 5×9 = 77

Result:

┌────────┐
│  8  43 │
│ 14  77 │
└────────┘
```

---

# 🧠 Complete Concept Map

```text
                    NumPy Operations
                          │
        ┌─────────────────┼──────────────────┐
        ↓                 ↓                  ↓
   Arithmetic        Selection           Statistics
        │                 │                  │
        ├─ Vectorized     ├─ Indexing        ├─ sum()
        ├─ Scalar         ├─ Slicing         ├─ min()
        └─ Operations     ├─ Boolean         ├─ max()
                          └─ Fancy           ├─ mean()
                                             ├─ median()
                                             └─ std()

                          │
                    Matrix Operations
                          │
                 ┌────────┴────────┐
                 ↓                 ↓
              axis              dot()
                 │
            ┌────┴────┐
            ↓         ↓
         axis=0     axis=1
        columns      rows
```

---

# 🎯 Final Summary

### ⚡ Vectorized Operations

```text
Array + Array
Array - Array
Array * Array
Array / Array
```

➡️ Operations happen element by element.

---

### 🔢 Scalar Operations

```text
Array + 10
Array - 10
Array * 10
Array / 10
```

➡️ The scalar is applied to every element.

---

### 🔍 Relational Operators

```text
>
<
==
>=
<=
!=
```

➡️ Produce `True`/`False` values.

---

### 🔵 Boolean Indexing

```python
arr[arr > 25]
```

➡️ Select values satisfying a condition.

---

### 🎯 Fancy Indexing

```python
arr[[0, 2, 4]]
```

➡️ Select multiple indexes.

---

### 📍 Indexing

```python
arr[2]
```

➡️ Select one element.

---

### ✂️ Slicing

```python
arr[start:stop:step]
```

➡️ Select a range.

---

### 📊 2D Indexing

```python
arr[row, column]
```

➡️ Select an element from a matrix.

---

### 🧮 Mathematical Functions

```text
sum()     → total
min()     → smallest value
max()     → largest value
prod()    → product
mean()    → average
median()  → middle value
std()     → standard deviation
```

---

### 📉 Index Functions

```text
argmin() → index of minimum
argmax() → index of maximum
```

---

### 🧭 Axis

```text
axis=0 → column-wise result
axis=1 → row-wise result
```

---

### 🔄 Rounding

```text
round() → nearest
ceil()  → upward
floor() → downward
```

---

### ✖️ Dot Product

```python
np.dot(A, B)
```

➡️ Multiply rows by columns and add the results.

---

# 🏆 Most Important Beginner Points

```text
1️⃣ NumPy works element-by-element for normal array arithmetic.

2️⃣ arr + 10 applies 10 to every element.

3️⃣ arr > 25 creates True/False values.

4️⃣ arr[arr > 25] selects the True values.

5️⃣ arr[[0, 2, 4]] selects specific indexes.

6️⃣ arr[index] accesses one element.

7️⃣ arr[start:stop] selects a range.

8️⃣ arr[row, column] accesses a 2D element.

9️⃣ axis=0 → column-wise result.

🔟 axis=1 → row-wise result.

1️⃣1️⃣ argmin/argmax return indexes.

1️⃣2️⃣ np.dot() performs matrix dot-product multiplication.
```

# 🚀 One-Line Revision

> **NumPy lets us perform fast array calculations, filtering, indexing, slicing, statistical calculations, and matrix operations without manually processing every element.**
