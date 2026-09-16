# ============================================================
# NumPy Indexing and Slicing
# ============================================================

import numpy as np


# ============================================================
# 1. Create a 1D NumPy Array
# ============================================================

arr = np.array(
    [4, 3, 6, 8, 7, 2, 3, 1],
    dtype="int32"
)

print("Array:")
print(arr)


# ============================================================
# 2. Indexing in 1D Array
# ============================================================

# Index starts from 0
#
# Index:   0  1  2  3  4  5  6  7
# Value:  [4, 3, 6, 8, 7, 2, 3, 1]

print("\n1D Indexing:")

print(arr[0])       # First element -> 4
print(arr[3])       # Fourth element -> 8
print(arr[-1])      # Last element -> 1
print(arr[-2])      # Second-last element -> 3


# ============================================================
# 3. Slicing in 1D Array
# ============================================================

# Syntax:
#
# array[start : stop : step]
#
# start -> Starting index
# stop  -> Ending index (NOT included)
# step  -> Number of positions to jump


# Example 1: Start to stop

print("\nSlicing:")

print(arr[2:5])

# Index positions:
#       0  1  2  3  4  5  6  7
#       4  3  6  8  7  2  3  1
#
# arr[2:5]
#       ↑     ↑
#     start  stop
#
# Result -> [6, 8, 7]


# Example 2: Start omitted

print(arr[:4])

# Means:
# Start from beginning
# Stop before index 4
#
# Result -> [4, 3, 6, 8]


# Example 3: Stop omitted

print(arr[4:])

# Start from index 4
# Continue until the end
#
# Result -> [7, 2, 3, 1]


# Example 4: Step

print(arr[::2])

# Start -> beginning
# Stop  -> end
# Step  -> 2
#
# Result -> [4, 6, 7, 3]


# Example 5: Reverse the array

print(arr[::-1])

# Step = -1 means move from right to left
#
# Result -> [1, 3, 2, 7, 8, 6, 3, 4]


# Example 6: Reverse part of an array

print(arr[2::-1])

# Start at index 2
# Move backwards
#
# Index 2 -> 6
# Index 1 -> 3
# Index 0 -> 4
#
# Result -> [6, 3, 4]


# ============================================================
# 4. Fancy Indexing — 1D Array
# ============================================================

# Fancy indexing means selecting specific indexes
# using a list/array of indexes.

print("\nFancy Indexing:")

print(arr[[0, 3, 5]])

# Select:
# index 0 -> 4
# index 3 -> 8
# index 5 -> 2
#
# Result -> [4, 8, 2]


# Another example

print(arr[[1, 4, 7]])

# index 1 -> 3
# index 4 -> 7
# index 7 -> 1
#
# Result -> [3, 7, 1]


# ============================================================
# 5. Boolean Indexing — 1D Array
# ============================================================

# Boolean indexing means selecting elements
# based on a condition.

print("\nBoolean Indexing:")

print(arr > 5)

# Result:
# [False, False, True, True, True, False, False, False]

# True  -> element satisfies condition
# False -> element does not satisfy condition


# Select only values greater than 5

print(arr[arr > 5])

# Result:
# [6, 8, 7]


# Select values less than 5

print(arr[arr < 5])

# Result:
# [4, 3, 2, 3, 1]


# ============================================================
# 6. Create a 2D NumPy Array
# ============================================================

arr1 = np.array([
    [2, 3, 4],
    [7, 6, 9],
    [5, 4, 9]
])

print("\n2D Array:")
print(arr1)


# ============================================================
# 7. Understanding 2D Array Indexing
# ============================================================

# 2D array has:
#
# Rows    -> first index
# Columns -> second index
#
#             Column
#             0  1  2
#
# Row 0 ->   [2, 3, 4]
# Row 1 ->   [7, 6, 9]
# Row 2 ->   [5, 4, 9]


# Syntax:
#
# array[row, column]


# Example 1

print("\n2D Indexing:")

print(arr1[0, 0])

# Row 0, Column 0
# Result -> 2


# Example 2

print(arr1[1, 1])

# Row 1, Column 1
# Result -> 6


# Example 3

print(arr1[2, 2])

# Row 2, Column 2
# Result -> 9


# ============================================================
# 8. Selecting an Entire Row
# ============================================================

print("\nEntire Row:")

print(arr1[0])

# Row 0
# Result -> [2, 3, 4]


print(arr1[1])

# Row 1
# Result -> [7, 6, 9]


# ============================================================
# 9. Selecting an Entire Column
# ============================================================

print("\nEntire Column:")

print(arr1[:, 0])

# : means all rows
# 0 means column 0
#
# Result -> [2, 7, 5]


print(arr1[:, 1])

# All rows, column 1
#
# Result -> [3, 6, 4]


print(arr1[:, 2])

# All rows, column 2
#
# Result -> [4, 9, 9]


# ============================================================
# 10. Slicing a 2D Array
# ============================================================

# Syntax:
#
# array[row_start:row_stop, column_start:column_stop]


# Example 1

print("\n2D Slicing:")

print(arr1[0:2, 0])

# Rows 0 and 1
# Column 0
#
# Result -> [2, 7]


# Example 2

print(arr1[0:2, 0:2])

# Rows:
# 0, 1
#
# Columns:
# 0, 1
#
# Result:
#
# [[2, 3],
#  [7, 6]]


# ============================================================
# 11. Select First 2 Rows and First 2 Columns
# ============================================================

print(arr1[:2, :2])

# Result:
#
# [[2, 3],
#  [7, 6]]


# ============================================================
# 12. Select All Rows and First 2 Columns
# ============================================================

print(arr1[:, :2])

# Result:
#
# [[2, 3],
#  [7, 6],
#  [5, 4]]


# ============================================================
# 13. Select First 2 Rows and All Columns
# ============================================================

print(arr1[:2, :])

# Result:
#
# [[2, 3, 4],
#  [7, 6, 9]]


# ============================================================
# 14. Reverse Rows in 2D Array
# ============================================================

print("\nReverse Rows:")

print(arr1[::-1])

# Result:
#
# [[5, 4, 9],
#  [7, 6, 9],
#  [2, 3, 4]]


# ============================================================
# 15. Select First Column While Reversing Rows
# ============================================================

print(arr1[::-1, 0])

# Reverse rows:
# Row 2 -> 5
# Row 1 -> 7
# Row 0 -> 2
#
# Result -> [5, 7, 2]


# ============================================================
# 16. Fancy Indexing — 2D Array
# ============================================================

# Select specific rows and columns.

print("\nFancy Indexing - 2D:")

print(arr1[[0, 2], [1, 2]])

# Select:
#
# arr1[0, 1] -> 3
# arr1[2, 2] -> 9
#
# Result -> [3, 9]


# ============================================================
# 17. Boolean Indexing — 2D Array
# ============================================================

print("\nBoolean Indexing - 2D:")

print(arr1 > 5)

# Every element is checked against > 5
#
# Result:
#
# [[False, False, False],
#  [ True,  True,  True],
#  [False, False,  True]]


# Select only values greater than 5

print(arr1[arr1 > 5])

# Result:
# [7, 6, 9, 9]


# Select only values less than 5

print(arr1[arr1 < 5])

# Result:
# [2, 3, 4, 4]


# ============================================================
# NUMPY PRACTICE
# Indexing, Slicing, Stacking, Splitting,
# Cumulative Operations and Mathematical Functions
# ============================================================

import numpy as np


# ============================================================
# 1. CREATE 2D ARRAY
# ============================================================

ar1 = np.array([
    [2, 3, 4],
    [7, 6, 9],
    [5, 4, 9]
])

print("Original Array:")
print(ar1)


# ============================================================
# 2. FANCY INDEXING
# ============================================================

result = ar1[0:3, 0:2]

print("\nFancy Indexing:")
print(result)


# ============================================================
# 3. BOOLEAN INDEXING
# ============================================================

result = ar1 > 5

print("\nBoolean Condition:")
print(result)


# Select values greater than 5

result = ar1[ar1 > 5]

print("\nValues Greater Than 5:")
print(result)


# ============================================================
# 4. ARRAY COPY
# ============================================================

ar2 = ar1.copy()

print("\nCopied Array:")
print(ar2)


# ============================================================
# 5. HORIZONTAL STACK
# ============================================================

result = np.hstack([ar1, ar2])

print("\nHorizontal Stack:")
print(result)


# ============================================================
# 6. VERTICAL STACK
# ============================================================

result = np.vstack([ar1, ar2])

print("\nVertical Stack:")
print(result)


# ============================================================
# 7. CONCATENATE - axis=0
# ============================================================

result = np.concatenate(
    [ar1, ar2],
    axis=0
)

print("\nConcatenate axis=0:")
print(result)


# ============================================================
# 8. CONCATENATE - axis=1
# ============================================================

result = np.concatenate(
    [ar1, ar2],
    axis=1
)

print("\nConcatenate axis=1:")
print(result)


# ============================================================
# 9. HORIZONTAL SPLIT
# ============================================================

result = np.hsplit(ar1, 3)

print("\nHorizontal Split:")
print(result)


# ============================================================
# 10. VERTICAL SPLIT
# ============================================================

result = np.vsplit(ar1, 3)

print("\nVertical Split:")
print(result)


# ============================================================
# 11. np.split()
# ============================================================

result = np.split(ar1, 3)

print("\nnp.split():")
print(result)


# ============================================================
# 12. CUMULATIVE SUM
# ============================================================

salaries = [
    2000,
    3000,
    4000,
    5000,
    6000
]

result = np.cumsum(salaries)

print("\nCumulative Sum:")
print(result)


# ============================================================
# 13. FINAL CUMULATIVE SUM
# ============================================================

result = np.cumsum(salaries)[-1]

print("\nFinal Cumulative Sum:")
print(result)


# ============================================================
# 14. CUMULATIVE PRODUCT
# ============================================================

result = np.cumprod(salaries)

print("\nCumulative Product:")
print(result)


# ============================================================
# 15. FINAL CUMULATIVE PRODUCT
# ============================================================

result = np.cumprod(salaries)[-1]

print("\nFinal Cumulative Product:")
print(result)


# ============================================================
# 16. MATHEMATICAL FUNCTIONS
# ============================================================

ar = np.array([
    4,
    3,
    6,
    8,
    7,
    2,
    3,
    1
])


# ------------------------------------------------------------
# Square Root
# ------------------------------------------------------------

result = np.sqrt(ar)

print("\nSquare Root:")
print(result)


# ------------------------------------------------------------
# Square
# ------------------------------------------------------------

result = np.square(ar)

print("\nSquare:")
print(result)


# ------------------------------------------------------------
# Power
# ------------------------------------------------------------

result = np.power(ar, 3)

print("\nPower:")
print(result)

# ========================================

# ============================================================
# NUMPY MATHEMATICAL FUNCTIONS
# ============================================================

import numpy as np


# ------------------------------------------------------------
# 1. Create an array
# ------------------------------------------------------------

ar = np.array([4, 3, 6, 8, 7, 2, 3, 1])

print("Original Array:")
print(ar)


# ------------------------------------------------------------
# 2. Square Root Function
# ------------------------------------------------------------
# np.sqrt() calculates the square root of every element.
#
# Example:
# sqrt(4) = 2
# sqrt(9) = 3
# sqrt(16) = 4

print("\nSquare Root:")
print(np.sqrt(ar))


# ------------------------------------------------------------
# 3. Square Function
# ------------------------------------------------------------
# np.square() calculates the square of every element.
#
# Example:
# 4² = 16
# 3² = 9
# 6² = 36

print("\nSquare:")
print(np.square(ar))


# ------------------------------------------------------------
# 4. Power Function
# ------------------------------------------------------------
# np.power(array, power)
#
# Here every element is raised to the power 3.
#
# Example:
# 4³ = 64
# 3³ = 27
# 6³ = 216

print("\nPower:")
print(np.power(ar, 3))


# ------------------------------------------------------------
# 5. Multiplication Function
# ------------------------------------------------------------
# np.multiply() performs element-by-element multiplication.
#
# Example:
# 2 × 5 = 10
# 3 × 6 = 18
# 4 × 7 = 28

a = np.array([2, 3, 4])
b = np.array([5, 6, 7])

print("\nMultiplication:")
print(np.multiply(a, b))


# ------------------------------------------------------------
# 6. Division Function
# ------------------------------------------------------------
# np.divide() performs element-by-element division.

ar = np.array([4, 6, 8, 10])

print("\nDivision:")
print(np.divide(ar, 2))


# ------------------------------------------------------------
# 7. Floor Division
# ------------------------------------------------------------
# // performs floor division.
#
# Example:
# 5 // 2 = 2
# 7 // 2 = 3
# 9 // 2 = 4

print("\nFloor Division:")
print(ar // 2)


# ============================================================
# WORKING WITH MISSING VALUES
# ============================================================

# ------------------------------------------------------------
# 8. Create an array containing missing values
# ------------------------------------------------------------
# np.nan means "Not a Number".
# It is commonly used to represent missing numerical data.

ar = np.array([
    45,
    65,
    23,
    12,
    67,
    89,
    np.nan,
    43,
    np.nan
])

print("\nArray with Missing Values:")
print(ar)


# ------------------------------------------------------------
# 9. Check for NaN values
# ------------------------------------------------------------
# np.isnan() checks each element.
#
# False → value is NOT NaN
# True  → value IS NaN

print("\nCheck NaN Values:")
print(np.isnan(ar))


# ------------------------------------------------------------
# 10. Select only the missing values
# ------------------------------------------------------------
# np.isnan(ar) creates a Boolean array.
#
# ar[condition] selects only the elements
# where the condition is True.

print("\nOnly Missing Values:")
print(ar[np.isnan(ar)])


# ============================================================
# VISUALIZATION WITH MATPLOTLIB AND SEABORN
# ============================================================

# Import libraries

import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------
# 11. Histogram
# ------------------------------------------------------------
# A histogram shows the distribution of numerical data.
#
# kde=True adds a smooth density curve.

age = np.array([
    23, 18, 34, 25, 43,
    27, 34, 32, 19,
    90, 89, 78
])

sns.histplot(age, kde=True)

plt.show()


# ------------------------------------------------------------
# 12. Box Plot
# ------------------------------------------------------------
# A box plot is useful for understanding:
#
# - Minimum
# - Q1
# - Median
# - Q3
# - Maximum
# - Outliers

age = np.array([
    23, 18, 34, 25, 43,
    27, 34, 32, 19,
    190, 800, 50
])

sns.boxplot(age)

plt.show()


# ============================================================
# BROADCASTING
# ============================================================

# ------------------------------------------------------------
# 13. Broadcasting — Basic Example
# ------------------------------------------------------------
#
# Broadcasting allows NumPy to perform arithmetic
# operations between arrays with compatible shapes.
#
# a shape = (4, 3)
# b shape = (3,)
#
# NumPy broadcasts b across every row of a.

a = np.arange(12).reshape(4, 3)

b = np.arange(3)

print("\nShape of a:")
print(a.shape)

print("\nShape of b:")
print(b.shape)

print("\nArray a:")
print(a)

print("\nArray b:")
print(b)

print("\nBroadcasting Addition:")
print(a + b)


# ------------------------------------------------------------
# 14. Broadcasting Example — Incompatible Shapes
# ------------------------------------------------------------
#
# a shape = (3, 4)
# b shape = (4, 3)
#
# These shapes cannot be broadcast together.
#
# Therefore:
# ValueError: operands could not be broadcast together

a = np.arange(12).reshape(3, 4)

b = np.arange(12).reshape(4, 3)

print("\nShape of a:")
print(a.shape)

print("\nShape of b:")
print(b.shape)

# This will produce a ValueError:
# print(a + b)


# ============================================================
# BROADCASTING WITH (1,3) AND (3,1)
# ============================================================

# ------------------------------------------------------------
# 15. Broadcasting Example
# ------------------------------------------------------------
#
# a shape = (1, 3)
# b shape = (3, 1)
#
# Both dimensions contain 1, so NumPy can expand them.

a = np.arange(3).reshape(1, 3)

b = np.arange(3).reshape(3, 1)

print("\nShape of a:")
print(a.shape)

print("\nShape of b:")
print(b.shape)

print("\nBroadcasting Result:")
print(a + b)


# ============================================================
# BROADCASTING — DIFFERENT NUMBER OF DIMENSIONS
# ============================================================

# ------------------------------------------------------------
# 16. Another Broadcasting Example
# ------------------------------------------------------------
#
# a shape = (4, 3)
# b shape = (3,)
#
# NumPy treats b as:
#
# (1, 3)
#
# Then broadcasts it to:
#
# (4, 3)

a = np.arange(12).reshape(4, 3)

b = np.arange(3)

print("\nShape of a:")
print(a.shape)

print("\nShape of b:")
print(b.shape)

print("\nResult:")
print(a + b)


# ============================================================
# BROADCASTING RULES
# ============================================================

# Broadcasting Rule 1:
#
# Compare dimensions from RIGHT to LEFT.
#
# Example:
#
#       (4, 3)
#       (3,)
#
# Think of (3,) as (1, 3)
#
#       (4, 3)
#       (1, 3)
#
# 3 == 3  -> Compatible
#
#
# Broadcasting Rule 2:
#
# Two dimensions are compatible when:
#
# 1. They are equal
# OR
# 2. One of them is 1
#
#
# Example:
#
# (3, 1)
# (1, 3)
#
# Compatible because 1 can be expanded.
#
#
# Example:
#
# (3, 4)
# (4, 3)
#
# Not compatible because:
#
# 4 != 3
# 3 != 4