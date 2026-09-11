# 🧮 NumPy — Beginner Level

> 🐍 **NumPy** is a Python library mainly used for numerical calculations and working with arrays.

---

## 📚 Table of Contents

* 🔹 What is NumPy?
* 🔹 Python List vs NumPy Array
* 🔹 Creating Arrays
* 🔹 Array Dimensions
* 🔹 Array Creation Functions
* 🔹 Array Attributes
* 🔹 Reshaping
* 🔹 flatten() vs ravel()
* 🔹 View vs Copy
* 🔹 Vectorized Operations
* 🔹 Indexing & Slicing
* 🔹 Boolean & Fancy Indexing
* 🔹 Mathematical Functions
* 🔹 axis
* 🔹 Dot Product
* 🔹 Performance
* 🔹 Final Summary
* 🎯 Interview Questions & Answers

---

# 🔹 1. What is NumPy?

### 📖 Definition

**NumPy** stands for **Numerical Python**.

It is a Python library used for:

* 🔢 Numerical calculations
* 📦 Working with arrays
* 📊 Multidimensional data
* ⚡ Fast mathematical operations

### 📌 Import NumPy

```python
import numpy as np
```

Here:

* `numpy` → library name
* `np` → short name/alias

### 💡 Example

```python
import numpy as np

arr = np.array([3, 4, 5])

print(arr)
```

### 🖥️ Output

```text
[3 4 5]
```

---

# 🔹 2. Python List vs NumPy Array

| Feature                      | 🐍 Python List                    | 🔢 NumPy Array                   |
| ---------------------------- | --------------------------------- | -------------------------------- |
| Size                         | Can grow/shrink                   | Generally fixed                  |
| Data types                   | Can contain different types       | Generally one common type        |
| Arithmetic                   | No direct element-wise arithmetic | Supports element-wise operations |
| Multidimensional data        | More difficult                    | Easy                             |
| Large numerical calculations | Generally slower                  | Generally faster                 |

---

# 🔹 3. Python List Addition

### 📖 Important

With Python lists, `+` means **concatenation**.

### 💻 Example

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_1 + list_2)
```

### 🖥️ Output

```text
[1, 2, 3, 4, 5, 6]
```

### 🧠 Remember

```text
List + List
     ↓
Concatenation
     ↓
Joins two lists
```

---

# 🔹 4. Creating a NumPy Array

### 📖 Definition

`np.array()` converts data such as a Python list into a NumPy array.

### 🔤 Syntax

```python
np.array(data)
```

### 💻 Example

```python
numbers = [4, 5, 6, 7]

arr = np.array(numbers)

print(arr)
```

### 🖥️ Output

```text
[4 5 6 7]
```

---

# 🔹 5. 1D Array

A one-dimensional array contains values in a single direction.

```python
arr = np.array([3, 4, 5])

print(arr)
print(arr.ndim)
```

### 🖥️ Output

```text
[3 4 5]
1
```

👉 `ndim` tells us the number of dimensions.

---

# 🔹 6. 2D Array

A 2D array contains **rows and columns**.

### 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
print(arr.ndim)
print(arr.shape)
```

### 🖥️ Output

```text
[[1 2 3]
 [4 5 6]]

2

(2, 3)
```

### 👀 Visual

```text
        Columns
       ↓   ↓   ↓
      [1   2   3]  ← Row 1
      [4   5   6]  ← Row 2

        2 × 3
        ↓   ↓
      rows columns
```

---

# 🔹 7. `ndim`

### 📖 Definition

`ndim` returns the **number of dimensions**.

### 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.ndim)
```

### 🖥️ Output

```text
2
```

### 🧠 Remember

```text
1D → [1 2 3]

2D → [[1 2]
      [3 4]]

3D → collection of 2D arrays
```

---

# 🔹 8. `shape`

### 📖 Definition

`shape` tells us the size of each dimension.

For a 2D array:

```text
(rows, columns)
```

### 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
```

### 🖥️ Output

```text
(2, 3)
```

### 👀 Visual

```text
[[1 2 3]
 [4 5 6]]

  ↑   ↑
  2   3
rows columns
```

---

# 🔹 9. `size`

### 📖 Definition

`size` returns the **total number of elements**.

### 💻 Example

```python
arr = np.array([
    [2, 3, 4],
    [5, 6, 7]
])

print(arr.size)
```

### 🖥️ Output

```text
6
```

Because:

```text
2 rows × 3 columns = 6 elements
```

---

# 🔹 10. `dtype`

### 📖 Definition

`dtype` tells us the data type stored in the array.

### 💻 Example

```python
arr = np.array([10, 20, 30])

print(arr.dtype)
```

### 🖥️ Example Output

```text
int64
```

> ⚠️ The exact integer type can depend on your system.

---

# 🔹 11. Element-Wise Operations

One of NumPy's important features is performing operations on **each element**.

### 💻 Example

```python
arr = np.array([4, 5, 6, 7])

result = arr + 10

print(result)
```

### 🖥️ Output

```text
[14 15 16 17]
```

### 👀 Visual

```text
Original:

[4   5   6   7]
 ↓   ↓   ↓   ↓
+10 +10 +10 +10
 ↓   ↓   ↓   ↓
[14 15 16 17]
```

---

# 🔹 12. `np.ones()`

### 📖 Definition

Creates an array containing `1`s.

### 🔤 Syntax

```python
np.ones(shape)
```

### 💻 Example

```python
arr = np.ones((3, 4))

print(arr)
```

### 🖥️ Output

```text
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
```

---

# 🔹 13. `np.zeros()`

### 📖 Definition

Creates an array containing `0`s.

### 🔤 Syntax

```python
np.zeros(shape)
```

### 💻 Example

```python
arr = np.zeros((2, 3))

print(arr)
```

### 🖥️ Output

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

---

# 🔹 14. `np.eye()`

### 📖 Definition

Creates an identity-like matrix with `1`s on the main diagonal.

### 💻 Example

```python
arr = np.eye(4)

print(arr)
```

### 🖥️ Output

```text
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

---

# 🔹 15. `np.identity()`

### 📖 Definition

Creates an identity matrix.

### 💻 Example

```python
arr = np.identity(5)

print(arr)
```

### 🖥️ Output

```text
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
```

---

# 🔹 16. `np.diag()`

### 📖 Definition

Creates a matrix with the given values on the diagonal.

### 💻 Example

```python
arr = np.diag([2, 3, 4, 5])

print(arr)
```

### 🖥️ Output

```text
[[2 0 0 0]
 [0 3 0 0]
 [0 0 4 0]
 [0 0 0 5]]
```

---

# 🔹 17. `np.empty()`

### 📖 Definition

Creates an array **without initializing its values**.

### 🔤 Syntax

```python
np.empty(shape)
```

### 💻 Example

```python
arr = np.empty((2, 4))

print(arr)
```

### ⚠️ Important

The output is **not fixed**.

It may contain existing memory values.

```text
np.empty()
     ↓
Memory allocated
     ↓
Values not initialized
     ↓
Unpredictable values
```

---

# 🔹 18. `np.arange()`

### 📖 Definition

Creates a sequence of values.

### 🔤 Syntax

```python
np.arange(start, stop, step)
```

⚠️ `stop` is **not included**.

### 💻 Example

```python
arr = np.arange(1, 10)

print(arr)
```

### 🖥️ Output

```text
[1 2 3 4 5 6 7 8 9]
```

### 🧠 Remember

```python
np.arange(1, 10)
```

means:

```text
Start = 1
Stop  = 10
Step  = 1
```

But `10` is excluded.

---

# 🔹 19. Reverse `np.arange()`

### 💻 Example

```python
arr = np.arange(100, 10, -2)

print(arr)
```

### 🖥️ Output

```text
[100 98 96 94 92 ... 16 14 12]
```

### 🧠 Trick

Negative step means:

```text
100 → 98 → 96 → 94 → ...
```

---

# 🔹 20. `np.linspace()`

### 📖 Definition

Creates a specified number of **equally spaced values**.

### 🔤 Syntax

```python
np.linspace(start, stop, number_of_values)
```

### 💻 Example

```python
arr = np.linspace(1, 10, 9)

print(arr)
```

### 🖥️ Output

```text
[ 1.     2.125  3.25   4.375  5.5    6.625  7.75   8.875 10.   ]
```

### 🆚 `arange()` vs `linspace()`

```text
arange()
   ↓
Controls STEP

linspace()
   ↓
Controls NUMBER OF VALUES
```

---

# 🔹 21. Random Arrays

## 🎲 `np.random.rand()`

Creates random decimal values.

```python
arr = np.random.rand(2, 3)

print(arr)
```

Example output:

```text
[[0.52 0.18 0.91]
 [0.34 0.76 0.12]]
```

⚠️ Values change each time.

---

# 🔹 22. `np.random.randint()`

Creates random integers.

### 🔤 Syntax

```python
np.random.randint(start, stop, number)
```

### 💻 Example

```python
arr = np.random.randint(2, 10, 5)

print(arr)
```

Example output:

```text
[4 8 2 7 5]
```

### 🧠 Remember

```python
np.random.randint(2, 10, 5)
```

```text
2  → start
10 → stop, excluded
5  → number of values
```

---

# 🔹 23. `np.random.randn()`

Creates random values from a standard normal distribution.

```python
arr = np.random.randn(5)

print(arr)
```

Example:

```text
[ 0.45 -1.21  0.18  0.76 -0.32]
```

Generally:

```text
Mean ≈ 0
Standard deviation ≈ 1
```

---

# 🔹 24. Reshaping an Array

### 📖 Definition

`reshape()` changes the shape of an array.

### 🔤 Syntax

```python
array.reshape(rows, columns)
```

### 💻 Example

```python
arr = np.array([
    [2, 3, 4],
    [5, 6, 7]
])

new_arr = arr.reshape(3, 2)

print(new_arr)
```

### 🖥️ Output

```text
[[2 3]
 [4 5]
 [6 7]]
```

### ⚠️ Important Rule

The number of elements must remain the same.

```text
Original:

2 × 3 = 6

New:

3 × 2 = 6
```

---

# 🔹 25. `flatten()`

### 📖 Definition

`flatten()` converts an array into one dimension and creates a **copy**.

### 💻 Example

```python
arr = np.array([
    [2, 3, 4],
    [5, 6, 7]
])

flat = arr.flatten()

flat[1] = 30

print(flat)
print(arr)
```

### 🖥️ Output

```text
[ 2 30  4  5  6  7]

[[2 3 4]
 [5 6 7]]
```

### 🧠 Key Point

Changing the flattened array does **not** change the original.

---

# 🔹 26. `ravel()`

### 📖 Definition

`ravel()` converts an array into one dimension and **usually returns a view**.

```python
arr = np.array([
    [2, 3, 4],
    [5, 6, 7]
])

flat = arr.ravel()

flat[2] = 40

print(arr)
```

### 🖥️ Output

```text
[[ 2  3 40]
 [ 5  6  7]]
```

### ⚠️ Key Point

Changing the ravelled array **may affect** the original array.

---

# 🔥 27. `flatten()` vs `ravel()`

| Feature            | `flatten()`       | `ravel()`                  |
| ------------------ | ----------------- | -------------------------- |
| Result             | Copy              | Usually view               |
| Original affected? | ❌ No              | ⚠️ May be                  |
| Memory             | More              | Less when view possible    |
| Use                | Independent array | Memory-efficient operation |

### 🧠 Easy Trick

```text
flatten()
    ↓
COPY

ravel()
    ↓
VIEW
```

---

# 🔹 28. Transpose

### 📖 Definition

Transpose changes rows into columns and columns into rows.

### 💻 Example

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)
```

### 🖥️ Output

```text
[[1 4]
 [2 5]
 [3 6]]
```

### 👀 Visual

```text
Original        Transpose

1 2 3           1 4
4 5 6    →      2 5
                3 6
```

---

# 🔹 29. View vs Copy

## 👀 View

A view shares memory with the original array.

```python
arr = np.array([10, 20, 30])

view_array = arr.view()

view_array[0] = 100

print(arr)
```

Output:

```text
[100  20  30]
```

---

## 📋 Copy

A copy creates an independent array.

```python
arr = np.array([10, 20, 30])

copy_array = arr.copy()

copy_array[1] = 200

print(arr)
print(copy_array)
```

Output:

```text
[10 20 30]
[ 10 200  30]
```

### 🧠 Easy Trick

```text
view()
  ↓
Same memory

copy()
  ↓
Separate memory
```

---

# 🔹 30. Vectorized Operations

NumPy allows operations directly on arrays.

```python
a = np.array([3, 4, 5])
b = np.array([6, 7, 8])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

### 🖥️ Output

```text
[ 9 11 13]
[-3 -3 -3]
[18 28 40]
[0.5        0.57142857 0.625     ]
```

### 👀 Visual

```text
a = [3 4 5]
b = [6 7 8]

a + b

[3+6  4+7  5+8]

= [9 11 13]
```

---

# 🔹 31. Scalar Operations

A scalar is a single value.

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)
print(arr - 10)
print(arr * 10)
print(arr / 10)
```

Output:

```text
[11 12 13 14 15]

[-9 -8 -7 -6 -5]

[10 20 30 40 50]

[0.1 0.2 0.3 0.4 0.5]
```

---

# 🔹 32. Relational Operators

NumPy can compare every element.

```python
arr = np.array([1, 2, 11, 4, 2, 3, 1])

print(arr[arr > 8])
print(arr[arr < 5])
print(arr[arr == 2])
```

Output:

```text
[11]

[1 2 4 2 3 1]

[2 2]
```

---

# 🔹 33. Boolean Indexing

### 📖 Definition

Boolean indexing selects values based on a condition.

```python
arr = np.array([10, 20, 30, 40, 50])

condition = arr > 25

print(condition)
print(arr[condition])
```

Output:

```text
[False False  True  True  True]

[30 40 50]
```

### 👀 Visual

```text
Values:
10   20   30   40   50

>25 ?
 F    F    T    T    T

Result:
30   40   50
```

---

# 🔹 34. Fancy Indexing

### 📖 Definition

Fancy indexing selects multiple indexes at once.

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr[[0, 2, 4]]

print(result)
```

Output:

```text
[10 30 50]
```

### 🧠 Meaning

```text
Index →  0   1   2   3   4
Value → 10  20  30  40  50

Select indexes:
0, 2, 4

Result:
10, 30, 50
```

---

# 🔹 35. 1D Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])
```

Output:

```text
10
30
50
```

### 🧠 Remember

```text
Index:  0   1   2   3   4
Value: 10  20  30  40  50
```

---

# 🔹 36. 1D Slicing

### 🔤 Syntax

```python
array[start:stop:step]
```

### 💻 Example

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[-2:])
print(arr[::2])
```

### 🖥️ Output

```text
[20 30 40]

[10 20 30]

[40 50]

[10 30 50]
```

---

# 🔹 37. 2D Indexing

### 🔤 Syntax

```python
array[row, column]
```

### 💻 Example

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1])
print(arr[1, 2])
```

### 🖥️ Output

```text
20
60
```

### 👀 Visual

```text
       Column
       0   1   2
       ↓   ↓   ↓
Row 0 [10 20 30]
Row 1 [40 50 60]

arr[0,1] → 20
arr[1,2] → 60
```

---

# 🔹 38. 2D Slicing

### 🔤 Syntax

```python
arr[row_start:row_end, column_start:column_end]
```

### 💻 Example

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

### 🖥️ Output

```text
[[10 20 30]
 [40 50 60]]

[[10 20]
 [40 50]
 [70 80]]

[[50 60]
 [80 90]]
```

---

# 🔹 39. Mathematical Functions

NumPy provides many mathematical functions.

```python
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.prod(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
```

### 🖥️ Output

```text
150
10
50
12000000
30.0
30.0
14.142135623730951
```

### 📌 Important Functions

| Function      | Meaning            |
| ------------- | ------------------ |
| `np.sum()`    | Total              |
| `np.min()`    | Minimum            |
| `np.max()`    | Maximum            |
| `np.prod()`   | Product            |
| `np.mean()`   | Average            |
| `np.median()` | Middle value       |
| `np.std()`    | Standard deviation |

---

# 🔹 40. `argmin()` and `argmax()`

### 📖 Definition

* `argmin()` → index of minimum value
* `argmax()` → index of maximum value

### 💻 Example

```python
arr = np.array([10, 5, 30, 2, 50])

print(np.argmin(arr))
print(np.argmax(arr))
```

### 🖥️ Output

```text
3
4
```

### 👀 Why?

```text
Index:  0   1   2   3   4
Value: 10   5  30   2  50
                  ↑       ↑
                min      max
```

---

# 🔹 41. `axis`

`axis` tells NumPy **which direction to perform an operation**.

Consider:

```text
[[10 20 30]
 [40 50 60]]
```

## `axis=0`

Works down the rows → column-wise.

```python
np.sum(arr, axis=0)
```

Output:

```text
[50 70 90]
```

## `axis=1`

Works across the columns → row-wise.

```python
np.sum(arr, axis=1)
```

Output:

```text
[60 150]
```

### 🧠 Easy Trick

```text
axis=0 → columns

axis=1 → rows
```

---

# 🔹 42. `round()`, `ceil()` and `floor()`

```python
arr = np.array([1.2, 2.7, 3.5, 4.9])

print(np.round(arr))
print(np.ceil(arr))
print(np.floor(arr))
```

Output:

```text
[1. 3. 4. 5.]

[2. 3. 4. 5.]

[1. 2. 3. 4.]
```

### 🧠 Remember

```text
round → nearest value
ceil  → upward
floor → downward
```

---

# 🔹 43. Dot Product

### 📖 Definition

`np.dot()` performs a dot product operation between arrays/matrices.

### 💻 Example

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

### 🖥️ Output

```text
[[ 8 43]
 [14 77]]
```

### 🧮 Example Calculation

First element:

```text
(2 × 1) + (3 × 2)

= 2 + 6

= 8
```

---

# 🔹 44. Performance

NumPy is generally faster than Python lists for large numerical calculations.

Example concept:

```python
arr = np.arange(10_000_000)

result = arr ** 2
```

A Python list can perform the same calculation using a loop/list comprehension, but NumPy uses optimized array operations.

### ⚡ Example Result

```text
Python List  → 1.85 seconds
NumPy Array  → 0.08 seconds
```

⚠️ These are only example timings. Actual execution time depends on the computer and environment.

---

# 🧠 Final Summary

| #  | Topic              | Remember                 |
| -- | ------------------ | ------------------------ |
| 1  | NumPy              | Numerical Python library |
| 2  | `np.array()`       | Creates arrays           |
| 3  | `ndim`             | Number of dimensions     |
| 4  | `shape`            | Dimensions/size          |
| 5  | `size`             | Total elements           |
| 6  | `dtype`            | Data type                |
| 7  | `ones()`           | Creates ones             |
| 8  | `zeros()`          | Creates zeros            |
| 9  | `eye()`            | Identity-like matrix     |
| 10 | `identity()`       | Identity matrix          |
| 11 | `diag()`           | Diagonal matrix          |
| 12 | `empty()`          | Uninitialized array      |
| 13 | `arange()`         | Sequence using step      |
| 14 | `linspace()`       | Equally spaced values    |
| 15 | `random.rand()`    | Random decimals          |
| 16 | `random.randint()` | Random integers          |
| 17 | `random.randn()`   | Normal random values     |
| 18 | `reshape()`        | Changes shape            |
| 19 | `flatten()`        | Creates copy             |
| 20 | `ravel()`          | Usually creates view     |
| 21 | `.T`               | Transpose                |
| 22 | `view()`           | Shares memory            |
| 23 | `copy()`           | Independent data         |
| 24 | Vectorization      | Element-wise operations  |
| 25 | Boolean indexing   | Filter using condition   |
| 26 | Fancy indexing     | Select multiple indexes  |
| 27 | Slicing            | Select a range           |
| 28 | `axis=0`           | Column-wise              |
| 29 | `axis=1`           | Row-wise                 |
| 30 | `np.dot()`         | Dot product              |

---

# 🎯 Interview Questions & Answers

## ❓ 1. What is NumPy?

### ✅ Answer

NumPy is a Python library used for numerical calculations and working with arrays. It supports multidimensional arrays and fast mathematical operations.

---

## ❓ 2. Why is NumPy faster than Python lists?

### ✅ Answer

NumPy uses optimized array operations and is designed for numerical computation. For large numerical calculations, this can make NumPy generally faster than Python lists.

---

## ❓ 3. How do you create a NumPy array?

### ✅ Answer

Use `np.array()`.

```python
import numpy as np

arr = np.array([1, 2, 3])
```

---

## ❓ 4. What does `ndim` do?

### ✅ Answer

`ndim` returns the number of dimensions of an array.

```python
arr.ndim
```

---

## ❓ 5. What does `shape` return?

### ✅ Answer

`shape` returns the size of each dimension.

For a 2 × 3 array:

```python
arr.shape
```

returns:

```text
(2, 3)
```

---

## ❓ 6. What is the difference between `shape` and `size`?

### ✅ Answer

`shape` tells us the dimensions, while `size` tells us the total number of elements.

```text
shape → (2, 3)

size → 6
```

---

## ❓ 7. What is `dtype`?

### ✅ Answer

`dtype` tells us the data type stored in a NumPy array.

Example:

```python
arr.dtype
```

---

## ❓ 8. What is element-wise operation?

### ✅ Answer

An operation performed independently on each array element is called an element-wise operation.

```python
arr = np.array([1, 2, 3])

arr + 10
```

Output:

```text
[11 12 13]
```

---

## ❓ 9. What is the difference between `arange()` and `linspace()`?

### ✅ Answer

`arange()` is based on a **step**, while `linspace()` is based on the **number of values**.

```text
arange → start, stop, step

linspace → start, stop, number of values
```

---

## ❓ 10. What does `reshape()` do?

### ✅ Answer

`reshape()` changes the shape of an array without changing the total number of elements.

```python
arr.reshape(3, 2)
```

---

## ❓ 11. What is the difference between `flatten()` and `ravel()`?

### ✅ Answer

`flatten()` creates a copy, whereas `ravel()` usually returns a view.

```text
flatten → copy
ravel   → usually view
```

---

## ❓ 12. What is a view?

### ✅ Answer

A view is an array that shares memory with the original array. Changes to the view may affect the original array.

---

## ❓ 13. What is a copy?

### ✅ Answer

A copy creates an independent array with separate data.

Changes to the copy do not affect the original array.

---

## ❓ 14. What is Boolean indexing?

### ✅ Answer

Boolean indexing selects elements based on a condition.

```python
arr[arr > 10]
```

It returns values greater than `10`.

---

## ❓ 15. What is fancy indexing?

### ✅ Answer

Fancy indexing allows us to select multiple indexes at once.

```python
arr[[0, 2, 4]]
```

---

## ❓ 16. What does `axis=0` mean?

### ✅ Answer

For the 2D examples in these notes, `axis=0` performs the operation down the rows and produces a column-wise result.

---

## ❓ 17. What does `axis=1` mean?

### ✅ Answer

For the 2D examples, `axis=1` performs the operation across the columns and produces a row-wise result.

---

## ❓ 18. What does `argmin()` return?

### ✅ Answer

`argmin()` returns the index of the minimum value.

```python
arr = np.array([10, 5, 30, 2])

np.argmin(arr)
```

Output:

```text
3
```

---

## ❓ 19. What does `argmax()` return?

### ✅ Answer

`argmax()` returns the index of the maximum value.

---

## ❓ 20. What does `np.empty()` do?

### ✅ Answer

`np.empty()` creates an array without initializing its values. Therefore, the contents are not fixed and may contain existing memory values.

---

# 🏆 Beginner Memory Tricks

```text
🧮 NumPy
   ↓
Numerical calculations

📦 array()
   ↓
Create array

📏 ndim
   ↓
How many dimensions?

📐 shape
   ↓
Rows + Columns / dimension sizes

🔢 size
   ↓
Total elements

🏷️ dtype
   ↓
Data type

🔄 reshape()
   ↓
Change shape

📋 flatten()
   ↓
Copy

👀 ravel()
   ↓
Usually View

👁️ view()
   ↓
Shares memory

📑 copy()
   ↓
Independent data

🎯 Boolean indexing
   ↓
Condition

🎯 Fancy indexing
   ↓
Multiple indexes

⬇️ axis=0
   ↓
Column-wise

➡️ axis=1
   ↓
Row-wise

⚡ Vectorization
   ↓
Fast element-wise operations

🔗 np.dot()
   ↓
Dot product
```

# 🚀 One-Line Interview Revision

> **NumPy = Python library for numerical computing using fast, multidimensional arrays.**
