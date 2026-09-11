# 🧮 NumPy Arrays & Array Creation

## 📚 Topics Covered

1. 🧮 NumPy Array
2. 🐍 Python List vs NumPy Array
3. 📦 Creating NumPy Arrays
4. 1️⃣ 1D Array
5. 2️⃣ 2D Array
6. 3️⃣ 3D Array
7. 📊 Array Attributes
8. ⚡ Element-wise Operations
9. 🏷️ `dtype`
10. 🔢 Homogeneous Arrays
11. ➕ `ones()` and `zeros()`
12. 🪪 Identity Matrix
13. 🔷 Diagonal Matrix
14. 📭 `empty()`
15. 🔢 `arange()`
16. 📏 `linspace()`
17. 🎲 Random Arrays
18. 🔄 `reshape()`
19. 📋 `flatten()`
20. 🧵 `ravel()`
21. 🔃 Transpose
22. 👀 View vs Copy

---

# 1. 🧮 NumPy Array

## 📖 Definition

A **NumPy array** is a data structure provided by NumPy for storing numerical values.

First import NumPy:

```python
import numpy as np
```

Here:

```text
numpy → library
np    → alias / short name
```

## 🔤 Syntax

```python
np.array(data)
```

## 💻 Example

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

## 🖥️ Output

```text
[10 20 30 40]
```

### 🔍 Dry Run

```text
Python list
    ↓
[10, 20, 30, 40]
    ↓
np.array()
    ↓
NumPy array
    ↓
[10 20 30 40]
```

---

# 2. 🐍 Python List vs NumPy Array

This is an important beginner concept.

## 🐍 Python List

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_1 + list_2)
```

### 🖥️ Output

```text
[1, 2, 3, 4, 5, 6]
```

### 🔍 What happened?

For Python lists:

```text
[1, 2, 3] + [4, 5, 6]
          ↓
      Concatenation
          ↓
[1, 2, 3, 4, 5, 6]
```

`+` joins the two lists.

---

# 3. 🔢 NumPy Array Addition

Now convert the lists into NumPy arrays.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
```

## 🖥️ Output

```text
[5 7 9]
```

## 🔍 Dry Run

NumPy performs addition **element by element**.

```text
a = [1  2  3]
b = [4  5  6]
```

Calculation:

```text
1 + 4 = 5
2 + 5 = 7
3 + 6 = 9
```

Result:

```text
[5 7 9]
```

### 🧠 Important Difference

```text
Python List
[1,2,3] + [4,5,6]
       ↓
[1,2,3,4,5,6]

NumPy Array
[1,2,3] + [4,5,6]
       ↓
[5,7,9]
```

---

# 4. 📦 Creating a NumPy Array

## 📖 Definition

`np.array()` creates a NumPy array from data such as a Python list.

## 🔤 Syntax

```python
np.array(data)
```

## 💻 Example

```python
arr = np.array([3, 4, 5])

print(arr)
```

## 🖥️ Output

```text
[3 4 5]
```

---

# 5. 📋 Creating an Array from a Python List

```python
numbers = [10, 20, 30, 40]

arr = np.array(numbers)

print(arr)
```

## 🖥️ Output

```text
[10 20 30 40]
```

## 🔍 Operation

```text
Python List
    ↓
[10, 20, 30, 40]
    ↓
np.array()
    ↓
NumPy Array
    ↓
[10 20 30 40]
```

---

# 6. 1️⃣ 1D Array

## 📖 Definition

A **1D array** is an array containing values in one dimension.

## 💻 Example

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

## 🖥️ Output

```text
[1 2 3 4 5]
```

### 👀 Visual

```text
Index:   0   1   2   3   4
         ↓   ↓   ↓   ↓   ↓
Array:  [1   2   3   4   5]
```

---

# 7. 2️⃣ 2D Array

## 📖 Definition

A **2D array** contains rows and columns.

## 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.ndim)
```

## 🖥️ Output

```text
2
```

### 👀 Visual

```text
        Columns
       0   1   2
       ↓   ↓   ↓

Row 0 [1   2   3]
Row 1 [4   5   6]
```

There are:

```text
2 rows
3 columns
```

So:

```text
shape = (2, 3)
```

---

# 8. 3️⃣ 3D Array

## 📖 Definition

A **3D array** is an array containing multiple 2D arrays.

## 💻 Example

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr.ndim)
```

## 🖥️ Output

```text
3
```

### 👀 Visual

```text
3D Array
   ↓
┌─────────────┐
│ 1  2        │
│ 3  4        │
└─────────────┘

┌─────────────┐
│ 5  6        │
│ 7  8        │
└─────────────┘
```

Think:

```text
3D
 ↓
Collection of 2D arrays
```

---

# 9. 📊 Array Attributes

Consider:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

NumPy provides important attributes.

```python
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
```

---

## 🔹 `ndim`

### Definition

Returns the number of dimensions.

```python
arr.ndim
```

Output:

```text
2
```

---

## 🔹 `shape`

### Definition

Returns the size of each dimension.

```python
arr.shape
```

Output:

```text
(2, 3)
```

Meaning:

```text
2 → rows
3 → columns
```

---

## 🔹 `size`

### Definition

Returns the total number of elements.

```python
arr.size
```

Output:

```text
6
```

Calculation:

```text
2 × 3 = 6
```

---

## 🔹 `dtype`

### Definition

Returns the data type of the array.

```python
arr.dtype
```

Example output:

```text
int64
```

The exact integer type can depend on the system.

---

# 10. ⚡ Element-wise Operations

## 📖 Definition

Element-wise operation means performing the operation on corresponding elements of arrays.

## 💻 Example

```python
a = np.array([3, 4, 5])
b = np.array([6, 7, 8])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## ➕ Addition

```text
3 + 6 = 9
4 + 7 = 11
5 + 8 = 13
```

Result:

```text
[9 11 13]
```

---

## ➖ Subtraction

```text
3 - 6 = -3
4 - 7 = -3
5 - 8 = -3
```

Result:

```text
[-3 -3 -3]
```

---

## ✖️ Multiplication

```text
3 × 6 = 18
4 × 7 = 28
5 × 8 = 40
```

Result:

```text
[18 28 40]
```

---

## ➗ Division

```text
3 / 6 = 0.5
4 / 7 ≈ 0.5714
5 / 8 = 0.625
```

Result:

```text
[0.5        0.57142857 0.625     ]
```

---

# 11. ➕ Adding a Single Number

A single number is called a **scalar**.

```python
arr = np.array([10, 20, 30, 40])

print(arr + 5)
```

## 🔍 Dry Run

```text
10 + 5 = 15
20 + 5 = 25
30 + 5 = 35
40 + 5 = 45
```

## 🖥️ Output

```text
[15 25 35 45]
```

### 👀 Visual

```text
[10 20 30 40]
 ↓  ↓  ↓  ↓
+5 +5 +5 +5
 ↓  ↓  ↓  ↓
[15 25 35 45]
```

---

# 12. 🏷️ `dtype`

## 📖 Definition

`dtype` specifies the data type stored in the NumPy array.

## 💻 Example

```python
arr = np.array(
    [45, 67, 899874564675, 23],
    dtype="int64"
)

print(arr.dtype)
```

## 🖥️ Output

```text
int64
```

### 🧠 Remember

```text
dtype
  ↓
Data Type
```

---

# 13. 🔢 NumPy is Usually Homogeneous

## 📖 Definition

NumPy arrays generally store values using one common data type.

Consider:

```python
arr = np.array([34, 56, 78, 23, 45.7])

print(arr)
print(arr.dtype)
```

## 🔍 Dry Run

We have:

```text
34    → integer
56    → integer
78    → integer
23    → integer
45.7  → float
```

Because one value is a float, NumPy converts the integers to floats.

Result:

```text
[34.  56.  78.  23.  45.7]
```

## 🖥️ Output

```text
[34.  56.  78.  23.  45.7]
float64
```

### 🧠 Important

```text
Integer + Float
       ↓
NumPy converts to
       ↓
Float
```

---

# 14. 1️⃣ `np.ones()`

## 📖 Definition

Creates an array filled with ones.

## 🔤 Syntax

```python
np.ones(shape)
```

## 💻 Example

```python
arr = np.ones((3, 4))

print(arr)
```

## 🖥️ Output

```text
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
```

### 🔍 Dry Run

```text
(3, 4)
 ↓
3 rows
4 columns
 ↓
Fill every position with 1
```

---

# 15. 0️⃣ `np.zeros()`

## 📖 Definition

Creates an array filled with zeros.

## 🔤 Syntax

```python
np.zeros(shape)
```

## 💻 Example

```python
arr = np.zeros((3, 4))

print(arr)
```

## 🖥️ Output

```text
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
```

### 🧠 Remember

```text
ones()  → 1
zeros() → 0
```

---

# 16. 🪪 Identity Matrix — `np.eye()`

## 📖 Definition

`np.eye()` creates a matrix with `1`s on the main diagonal and `0`s elsewhere.

## 🔤 Syntax

```python
np.eye(n)
```

## 💻 Example

```python
arr = np.eye(4)

print(arr)
```

## 🖥️ Output

```text
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

### 👀 Visual

```text
[ 1  0  0  0 ]
[ 0  1  0  0 ]
[ 0  0  1  0 ]
[ 0  0  0  1 ]

  ↑     ↑
Main diagonal
```

---

# 17. 🪪 Identity Matrix — `np.identity()`

## 📖 Definition

`np.identity()` creates a square identity matrix.

## 🔤 Syntax

```python
np.identity(n)
```

## 💻 Example

```python
arr = np.identity(5)

print(arr)
```

## 🖥️ Output

```text
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
```

---

# 18. 🔷 Diagonal Matrix — `np.diag()`

## 📖 Definition

`np.diag()` creates a matrix with given values on the main diagonal.

## 🔤 Syntax

```python
np.diag(values)
```

## 💻 Example

```python
arr = np.diag([2, 3, 4, 5, 6])

print(arr)
```

## 🖥️ Output

```text
[[2 0 0 0 0]
 [0 3 0 0 0]
 [0 0 4 0 0]
 [0 0 0 5 0]
 [0 0 0 0 6]]
```

### 🧠 Difference

```text
np.eye()
   ↓
Diagonal values are 1

np.diag([2,3,4])
   ↓
Diagonal values are 2,3,4
```

---

# 19. 📭 Empty Array — `np.empty()`

## 📖 Definition

`np.empty()` creates an array without initializing its values.

## 🔤 Syntax

```python
np.empty(shape)
```

## 💻 Example

```python
arr = np.empty([2, 4])

print(arr)
```

### ⚠️ Important

The values are **not fixed**.

You may see different values on different executions.

### 🧠 Remember

```text
np.empty()
     ↓
Memory allocated
     ↓
Values not initialized
     ↓
Unpredictable values
```

Do not use `empty()` when you need an array filled with zeros. Use:

```python
np.zeros()
```

instead.

---

# 20. 🔢 `np.arange()`

## 📖 Definition

`np.arange()` creates a sequence of numbers using a specified step.

## 🔤 Syntax

```python
np.arange(start, stop, step)
```

⚠️ `stop` is excluded.

---

## 💻 Example 1

```python
arr = np.arange(2, 10, 2)

print(arr)
```

## 🔍 Dry Run

Start at `2`.

Add `2` each time:

```text
2
2 + 2 = 4
4 + 2 = 6
6 + 2 = 8
8 + 2 = 10
```

But `10` is excluded.

Therefore:

```text
[2 4 6 8]
```

## 🖥️ Output

```text
[2 4 6 8]
```

---

# 21. 🔢 Reverse `np.arange()`

```python
arr = np.arange(100, 10, -10)

print(arr)
```

## 🔍 Dry Run

```text
Start = 100
Stop  = 10
Step  = -10
```

Sequence:

```text
100
90
80
70
60
50
40
30
20
10
```

`10` is excluded.

## 🖥️ Output

```text
[100  90  80  70  60  50  40  30  20]
```

---

# 22. 📏 `np.linspace()`

## 📖 Definition

`np.linspace()` creates a specified number of equally spaced values between two numbers.

## 🔤 Syntax

```python
np.linspace(start, stop, number_of_values)
```

## 💻 Example

```python
arr = np.linspace(1, 10, 9)

print(arr)
```

## 🖥️ Output

```text
[ 1.     2.125  3.25   4.375  5.5    6.625  7.75   8.875 10.   ]
```

### 🧠 Important Difference

```text
arange()
   ↓
You specify STEP

linspace()
   ↓
You specify NUMBER OF VALUES
```

---

# 23. 🎲 Random Arrays

## 📖 Definition

Random functions generate values that are not predetermined.

### `np.random.rand()`

Creates random decimal values.

## 🔤 Syntax

```python
np.random.rand(rows, columns)
```

## 💻 Example

```python
arr = np.random.rand(4, 5)

print(arr)
```

The output changes each time.

Example:

```text
[[0.52 0.18 0.91 0.34 0.76]
 [0.12 0.65 0.44 0.83 0.27]
 [0.71 0.39 0.56 0.14 0.95]
 [0.22 0.87 0.31 0.68 0.49]]
```

### 🧠 Remember

```text
random.rand()
      ↓
Random decimal values
```

---

# 24. 🔄 Reshape

## 📖 Definition

`reshape()` changes the arrangement/shape of an array without changing the number of elements.

## 🔤 Syntax

```python
array.reshape(rows, columns)
```

## 💻 Example

```python
arr = np.arange(1, 7)

print(arr)

reshaped_arr = arr.reshape(2, 3)

print(reshaped_arr)
```

## 🖥️ Output

```text
[1 2 3 4 5 6]

[[1 2 3]
 [4 5 6]]
```

---

## 🔍 Dry Run

Original:

```text
[1 2 3 4 5 6]
```

Number of elements:

```text
6
```

Requested shape:

```text
2 × 3 = 6
```

Therefore reshape is possible.

```text
1 2 3 4 5 6
      ↓
2 rows × 3 columns

[1 2 3]
[4 5 6]
```

### ⚠️ Rule

The total number of elements must remain the same.

```text
2 × 3 = 6
3 × 2 = 6
1 × 6 = 6
```

All are possible.

But:

```text
2 × 4 = 8
```

❌ Not possible because the original contains only 6 elements.

---

# 25. 📋 `flatten()`

## 📖 Definition

`flatten()` converts a multidimensional array into a 1D array and returns a **copy**.

## 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flattened = arr.flatten()

print(flattened)
```

## 🖥️ Output

```text
[1 2 3 4 5 6]
```

### 👀 Visual

```text
Original:

[1 2 3]
[4 5 6]

      ↓ flatten()

[1 2 3 4 5 6]
```

### 🧠 Key Point

```text
flatten()
    ↓
Creates COPY
```

---

# 26. 🧵 `ravel()`

## 📖 Definition

`ravel()` converts an array into 1D and usually returns a **view** when possible.

## 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

raveled = arr.ravel()

print(raveled)
```

## 🖥️ Output

```text
[1 2 3 4 5 6]
```

### 🧠 Key Point

```text
ravel()
   ↓
Usually VIEW
```

---

# 27. 🔥 `flatten()` vs `ravel()`

| Feature             | `flatten()` | `ravel()`    |
| ------------------- | ----------- | ------------ |
| Converts to 1D      | ✅           | ✅            |
| Returns copy        | ✅           | Usually ❌    |
| Returns view        | ❌           | Usually ✅    |
| Memory usage        | More        | Usually less |
| Original may change | ❌           | ⚠️ Yes       |

### 🧠 Easy Memory Trick

```text
flatten()
     ↓
COPY 📋

ravel()
     ↓
VIEW 👀
```

---

# 28. 🔃 Transpose

## 📖 Definition

Transpose changes rows into columns and columns into rows.

## 🔤 Syntax

```python
array.T
```

## 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)
```

## 🖥️ Output

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

## 🔍 Dry Run

Original:

```text
1 2 3
4 5 6
```

Rows become columns:

```text
1 4
2 5
3 6
```

### Shape

Original:

```text
(2, 3)
```

After transpose:

```text
(3, 2)
```

### 🧠 Visual

```text
Original       Transpose

1 2 3            1 4
4 5 6     →      2 5
                 3 6
```

---

# 29. 👀 View vs Copy

## 👀 View

A view shares memory with the original array.

```python
arr = np.array([1, 2, 3])

arr_view = arr.view()

print(arr_view)
```

Output:

```text
[1 2 3]
```

The important point is memory sharing.

---

# 30. 📋 Copy

A copy creates an independent array.

```python
arr = np.array([1, 2, 3])

arr_copy = arr.copy()

print(arr_copy)
```

Output:

```text
[1 2 3]
```

---

# 🔍 View vs Copy — Dry Run

Start:

```text
arr = [1 2 3]
```

Create view:

```text
arr_view = arr.view()
```

Create copy:

```text
arr_copy = arr.copy()
```

Think of memory like this:

```text
                 Original
                    arr
                     │
             ┌───────┴───────┐
             ↓               ↓
           View             Copy
        arr_view          arr_copy
             │               │
       Same memory       Separate memory
```

### 👀 View

```text
Original ←→ View
 Same memory
```

### 📋 Copy

```text
Original     Copy
   ↓           ↓
Memory A    Memory B
```

---

# 🧠 Most Important Differences

## 🐍 List vs NumPy Array

```text
List + List
     ↓
Concatenation

Array + Array
     ↓
Element-wise addition
```

---

## 📊 Dimensions

```text
1D → [1 2 3]

2D → [[1 2]
      [3 4]]

3D → collection of 2D arrays
```

---

## 📏 Attributes

```text
ndim  → number of dimensions
shape → dimensions/size
size  → total elements
dtype → data type
```

---

## 🔢 Array Creation

```text
array()    → create array
ones()     → ones
zeros()    → zeros
eye()      → identity-like matrix
identity() → identity matrix
diag()     → diagonal matrix
empty()    → uninitialized array
```

---

## 🔢 Number Generation

```text
arange()
   ↓
start, stop, step

linspace()
   ↓
start, stop, number of values
```

---

## 🔄 Array Transformation

```text
reshape() → change shape
flatten() → 1D copy
ravel()   → 1D view usually
.T        → transpose
```

---

# 🎯 Final Summary

| Concept         | Syntax                    | Purpose                |
| --------------- | ------------------------- | ---------------------- |
| 🧮 Array        | `np.array()`              | Create array           |
| 1️⃣ 1D          | `np.array([1,2,3])`       | One-dimensional data   |
| 2️⃣ 2D          | `np.array([[1,2],[3,4]])` | Rows + columns         |
| 3️⃣ 3D          | Nested arrays             | Multiple 2D arrays     |
| 📏 `ndim`       | `arr.ndim`                | Number of dimensions   |
| 📐 `shape`      | `arr.shape`               | Dimension sizes        |
| 🔢 `size`       | `arr.size`                | Total elements         |
| 🏷️ `dtype`     | `arr.dtype`               | Data type              |
| ⚡ Vectorized    | `a + b`                   | Element-wise operation |
| 1️⃣ `ones()`    | `np.ones()`               | Fill with 1            |
| 0️⃣ `zeros()`   | `np.zeros()`              | Fill with 0            |
| 🪪 `eye()`      | `np.eye()`                | Identity-like matrix   |
| 🔷 `diag()`     | `np.diag()`               | Diagonal matrix        |
| 📭 `empty()`    | `np.empty()`              | Uninitialized array    |
| 🔢 `arange()`   | `np.arange()`             | Sequence using step    |
| 📏 `linspace()` | `np.linspace()`           | Equally spaced values  |
| 🎲 `rand()`     | `np.random.rand()`        | Random decimals        |
| 🔄 `reshape()`  | `arr.reshape()`           | Change shape           |
| 📋 `flatten()`  | `arr.flatten()`           | 1D copy                |
| 🧵 `ravel()`    | `arr.ravel()`             | 1D view usually        |
| 🔃 Transpose    | `arr.T`                   | Rows ↔ columns         |
| 👀 View         | `arr.view()`              | Shares memory          |
| 📋 Copy         | `arr.copy()`              | Independent data       |

---

# 🏆 Interview Questions & Answers

## ❓ 1. What is NumPy?

### ✅ Answer

NumPy is a Python library used for numerical calculations and working with arrays.

---

## ❓ 2. How do you create a NumPy array?

### ✅ Answer

Using `np.array()`.

```python
arr = np.array([1, 2, 3])
```

---

## ❓ 3. What is the difference between a Python list and NumPy array?

### ✅ Answer

Python list `+` performs concatenation, while NumPy array `+` performs element-wise addition.

```text
List:
[1,2] + [3,4]
→ [1,2,3,4]

NumPy:
[1,2] + [3,4]
→ [4,6]
```

---

## ❓ 4. What does `ndim` return?

### ✅ Answer

It returns the number of dimensions of the array.

```python
arr.ndim
```

---

## ❓ 5. What does `shape` return?

### ✅ Answer

It returns the size of each dimension.

For a 2 × 3 array:

```text
(2, 3)
```

---

## ❓ 6. What does `size` return?

### ✅ Answer

It returns the total number of elements.

For a 2 × 3 array:

```text
2 × 3 = 6
```

---

## ❓ 7. What does `dtype` mean?

### ✅ Answer

`dtype` tells us the data type of the values stored in the array.

---

## ❓ 8. What is a 1D array?

### ✅ Answer

A 1D array contains elements in one dimension.

```python
np.array([1, 2, 3])
```

---

## ❓ 9. What is a 2D array?

### ✅ Answer

A 2D array contains rows and columns.

```python
np.array([
    [1, 2],
    [3, 4]
])
```

---

## ❓ 10. What is `np.ones()`?

### ✅ Answer

It creates an array filled with ones.

```python
np.ones((2, 3))
```

---

## ❓ 11. What is `np.zeros()`?

### ✅ Answer

It creates an array filled with zeros.

```python
np.zeros((2, 3))
```

---

## ❓ 12. What is `np.eye()`?

### ✅ Answer

It creates a matrix with ones on the main diagonal and zeros elsewhere.

---

## ❓ 13. What is `np.diag()`?

### ✅ Answer

It creates a matrix with specified values on the main diagonal.

---

## ❓ 14. What is `np.empty()`?

### ✅ Answer

It creates an array without initializing its values, so its contents are not predictable.

---

## ❓ 15. What is the difference between `arange()` and `linspace()`?

### ✅ Answer

`arange()` uses a **step**, while `linspace()` uses a **number of values**.

```text
arange   → start, stop, step
linspace → start, stop, number of values
```

---

## ❓ 16. What does `reshape()` do?

### ✅ Answer

It changes the shape of an array while keeping the same number of elements.

---

## ❓ 17. What is `flatten()`?

### ✅ Answer

`flatten()` converts an array into 1D and creates a copy.

---

## ❓ 18. What is `ravel()`?

### ✅ Answer

`ravel()` converts an array into 1D and usually returns a view when possible.

---

## ❓ 19. Difference between `flatten()` and `ravel()`?

### ✅ Answer

```text
flatten() → copy
ravel()   → usually view
```

---

## ❓ 20. What is transpose?

### ✅ Answer

Transpose changes rows into columns and columns into rows.

```python
arr.T
```

---

## ❓ 21. What is a view?

### ✅ Answer

A view shares memory with the original array, so changes to the view may affect the original.

---

## ❓ 22. What is a copy?

### ✅ Answer

A copy creates independent data. Changes to the copy do not affect the original.

---

# 🚀 One-Minute Revision

```text
🧮 np.array()
     ↓
Create NumPy array

📊 ndim
     ↓
How many dimensions?

📐 shape
     ↓
Rows / columns / dimensions

🔢 size
     ↓
Total elements

🏷️ dtype
     ↓
Data type

⚡ a + b
     ↓
Element-wise operation

1️⃣ ones()
     ↓
Fill with 1

0️⃣ zeros()
     ↓
Fill with 0

🪪 eye()
     ↓
Identity matrix

🔷 diag()
     ↓
Diagonal matrix

📭 empty()
     ↓
Uninitialized values

🔢 arange()
     ↓
Step-based sequence

📏 linspace()
     ↓
Equal spacing / number of values

🎲 random.rand()
     ↓
Random decimals

🔄 reshape()
     ↓
Change shape

📋 flatten()
     ↓
1D copy

🧵 ravel()
     ↓
1D view usually

🔃 .T
     ↓
Transpose

👀 view()
     ↓
Shares memory

📋 copy()
     ↓
Separate memory
```

# 🏁 Final Interview Line

> **NumPy provides efficient multidimensional arrays and powerful operations for creating, transforming, and calculating numerical data.**
