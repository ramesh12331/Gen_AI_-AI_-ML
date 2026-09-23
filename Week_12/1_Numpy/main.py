import numpy as np

# ============================================================
# 1. Creating a 1D NumPy Array
# ============================================================
arr = np.array([4, 3, 6, 8, 7, 2, 3, 1], dtype="int32")
print("Original 1D array:")
print(arr)

# ============================================================
# 2. Indexing in 1D Array
# ============================================================
print(arr[0])
print(arr[2])
print(arr[-1])
print(arr[-2])

# ============================================================
# 3. Slicing in 1D Array
# ============================================================
print(arr[2:])
print(arr[2:5])
print(arr[::2])
print(arr[::-1])
print(arr[:3:-1])
print(arr[1:7:2])
# ============================================================
# 5. Fancy Indexing in 1D Array
# ============================================================
print(arr[[0, 2, 4, 7]]) 
print(arr[[1, 3, 5, 7]]) 

# ============================================================
# 6. Boolean Indexing in 1D Array
# ============================================================
print(arr>5)
print(arr[arr>5])

print(arr[arr%2 == 0])
print(arr[arr%2 != 0])
print(arr[arr <= 4])

# ============================================================
# 7. Creating a 2D NumPy Array
# ============================================================

ar1 = np.array(
    [
        [2, 3, 4],
        [7, 6, 9],
        [5, 4, 9]
    ]
)

print("\nOriginal 2D array:")
print(ar1)

# ============================================================
# 8. Indexing in 2D Array
# ============================================================
print(ar1[0,0])
print(ar1[0,1])
print(ar1[1, 2])
print(ar1[-1, -1])

# ============================================================
# 9. Selecting a Complete Row
# ============================================================
print(ar1[0])
print(ar1[1])
print(ar1[2])
print(ar1[-1])

# ============================================================
# 10. Selecting a Complete Column
# ============================================================
print("\nFirst column:")
print(ar1[:, 0])
print(ar1[:, 1])
print(ar1[:, 2])
print(ar1[:, -1])

# ============================================================
# 11. Slicing of 2D Array
# ============================================================

# Syntax:
# array[row_start:row_stop, column_start:column_stop]
print(ar1[0:2,0])

print("\nSlicing ar1[0:2, 0:2]:")
print(ar1[0:2, 0:2])

print(ar1[:, 0:2])

print(ar1[0:2, :])
print(ar1[1:, :])

# ============================================================
# 12. Reverse Rows in 2D Array
# ============================================================
print(ar1[::-1, :])

# ============================================================
# 13. Reverse Columns in 2D Array
# ============================================================
print(ar1[:, ::-1])

# ============================================================
# 14. Reverse Rows and Columns
# ============================================================
print(ar1[::-1, ::-1])

# ============================================================
# 15. Slicing Example from the Class
# ============================================================

print(ar1[0:3, 0:2])

# ============================================================
# 16. Fancy Indexing in 2D Array
# ============================================================
print(ar1[[0, 2]])

# Select specific elements:
# ar1[[row_indexes], [column_indexes]]

print("\nSelect ar1[0, 1] and ar1[2, 2]:")
print(ar1[[0, 2], [1, 2]])

print("\nSelect diagonal elements:")
print(ar1[[0, 1, 2], [0, 1, 2]])

# ============================================================
# 17. Boolean Indexing in 2D Array
# ============================================================
print(ar1 > 5)
print(ar1[ar1 > 5])
print(ar1[ar1 == 9])
print(ar1[ar1 % 2 == 0])

# ============================================================
# 18. Updating Values Using Indexing
# ============================================================

# Create a copy so the original array is not changed
updated_array = ar1.copy()

print("\nOriginal copied array:")
print(updated_array)

# Update one element
updated_array[0, 0] = 100

print("\nAfter updating ar1[0, 0] to 100:")
print(updated_array)

# ============================================================
# 19. Updating Multiple Values Using Boolean Indexing
# ============================================================

updated_array = ar1.copy()

# Replace all values greater than 5 with 0
updated_array[updated_array > 5] = 0

print("\nReplace values greater than 5 with 0:")
print(updated_array)

# ============================================================
# 5. HORIZONTAL STACK
# ============================================================

ar2 = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
)
result = np.hstack([ar1, ar2])

print("\nHorizontal Stack:")
print(result)

# ============================================================
# 6. VERTICAL STACK
# ============================================================

# np.vstack() joins arrays vertically.

result = np.vstack([ar1, ar2])
print(result)

# ============================================================
# 7. CONCATENATE - axis=0
# ============================================================

# axis=0 means joining row-wise.

result = np.concatenate(
    [ar1, ar2],
    axis=0
)

print("\nConcatenate axis=0:")
print(result)

# ============================================================
# 8. CONCATENATE - axis=1
# ============================================================

# axis=1 means joining column-wise.

result = np.concatenate(
    [ar1, ar2],
    axis=1
)

print("\nConcatenate axis=1:")
print(result)

# ============================================================
# 9. HORIZONTAL SPLIT
# ============================================================

# np.hsplit() splits an array column-wise.

# For example, a 3-column array
# can be split into 3 parts.

ar1 = np.array([
    [2, 3, 4],
    [7, 6, 9],
    [5, 4, 9]
])

result = np.hsplit(ar1, 3)

print("\nHorizontal Split:")
print(result)

# ============================================================
# 10. VERTICAL SPLIT
# ============================================================

# np.vsplit() splits an array row-wise.

result = np.vsplit(ar1, 3)

print("\nVertical Split:")
print(result)

# ============================================================
# 11. np.split()
# ============================================================

# np.split() can split an array.
#
# For a 3 x 3 array:
# np.split(ar1, 3)
# splits it into 3 equal parts along axis=0.

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

# ============================================================
# 5. MULTIPLICATION FUNCTION
# ============================================================

# np.multiply() performs
# element-by-element multiplication.

a = np.array([2, 3, 4])
b = np.array([5, 6, 7])

print("\nMultiplication:")
print(np.multiply(a, b))

# ============================================================
# 6. DIVISION FUNCTION
# ============================================================

# np.divide() performs
# element-by-element division.

ar = np.array([
    4,
    6,
    8,
    10
])

print("\nDivision:")
print(np.divide(ar, 2))

# ============================================================
# 7. FLOOR DIVISION
# ============================================================

# // performs floor division.

print("\nFloor Division:")
print(ar // 2)


# ============================================================
# WORKING WITH MISSING VALUES
# ============================================================


# ============================================================
# 8. CREATE AN ARRAY CONTAINING MISSING VALUES
# ============================================================

# np.nan means "Not a Number".
# It is commonly used to represent
# missing numerical data.

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

# ============================================================
# 9. CHECK FOR NaN VALUES
# ============================================================

# np.isnan() checks each element.
#
# False -> value is NOT NaN
# True  -> value IS NaN

print("\nCheck NaN Values:")
print(np.isnan(ar))

# ============================================================
# 10. SELECT ONLY THE MISSING VALUES
# ============================================================

print("\nOnly Missing Values:")
print(ar[np.isnan(ar)])