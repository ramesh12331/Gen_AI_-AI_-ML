# ============================================================
#                  PANDAS - SERIES
# ============================================================
#
# Series:
#   - A one-dimensional labeled array.
#   - It contains values and an index.
#   - Each Series normally has a single dtype.
#   - Index can be default (0, 1, 2...) or custom.
#
# DataFrame:
#   - A two-dimensional table.
#   - It contains rows and columns.
#   - Different columns can have different data types.
#
# ============================================================
#                  WAYS TO CREATE SERIES
# ============================================================


# ============================================================
# 1. CREATE SERIES USING A LIST
# ============================================================

import pandas as pd

# Create a Python list
numbers = [23, 45, 64, 53, 21]

# Convert the list into a Pandas Series
s = pd.Series(numbers)

# Display the Series
print(s)

# Output:
# 0    23
# 1    45
# 2    64
# 3    53
# 4    21
# dtype: int64


# ============================================================
# 2. SERIES SLICING
# ============================================================

# Get values from index 0 up to index 2
# Stop position 3 is excluded
print(s[0:3])

# Output:
# 0    23
# 1    45
# 2    64


# ============================================================
# 3. CREATE SERIES USING LIST + CUSTOM INDEX
# ============================================================

# Create a Series with custom labels
s = pd.Series(
    numbers,
    index=['A', 'B', 'C', 'D', 'E']
)

print(s)

# Output:
# A    23
# B    45
# C    64
# D    53
# E    21


# ============================================================
# ACCESS VALUE USING CUSTOM INDEX
# ============================================================

# Get the value whose index is 'C'
print(s['C'])

# Output:
# 64


# ============================================================
# 4. CREATE SERIES USING A DICTIONARY
# ============================================================

student_data = {
    'name': ['Rahul', 'Mishra', 'Abdul', 'Venky'],
    'age': [20, 30, 40, 50],
    'city': ['Hyderabad', 'Bangalore', 'Chennai', 'AP']
}

# Convert dictionary into a Series
s = pd.Series(student_data)

print(s)

# In this case:
# Dictionary keys become Series indexes.
# Dictionary values become Series values.


# ============================================================
# ACCESS DATA FROM DICTIONARY-BASED SERIES
# ============================================================

# Get the value stored under the 'name' index
print(s['name'])

# Output:
# ['Rahul', 'Mishra', 'Abdul', 'Venky']


# Get the second name
print(s['name'][1])

# Output:
# Mishra


# ============================================================
# 5. CREATE SERIES USING NUMPY ARRAY
# ============================================================

import numpy as np

# Create a NumPy array
arr = np.array([2, 3, 4, 5, 6])

# Create a Pandas Series from NumPy array
s = pd.Series(
    arr,
    name='num',
    index=[1, 2, 3, 4, 5],
    dtype='int32'
)

print(s)

# name  -> Series name
# index -> Custom index
# dtype -> Data type


# ============================================================
# 6. SERIES NAME
# ============================================================

# Access the name of the Series
print(s.name)

# Output:
# num


# ============================================================
# 7. CUSTOM INDEX
# ============================================================

# Display the Series with custom indexes
print(s)

# Output:
# 1    2
# 2    3
# 3    4
# 4    5
# 5    6


# ============================================================
# 8. REVERSE A SERIES
# ============================================================

# [::-1] reverses the Series
print(s[::-1])

# Output:
# 5    6
# 4    5
# 3    4
# 2    3
# 1    2


# ============================================================
# 9. INDEXING
# ============================================================

# Access value using index
print(s[2])

# Output:
# 3


# ============================================================
# 10. SLICING
# ============================================================

# Get values from position 1 to position 3
# Stop position is excluded
print(s[1:4])


# ============================================================
# 11. DTYPE
# ============================================================

# Check the data type of Series
print(s.dtype)

# Output:
# int32


# ============================================================
# 12. VALUES
# ============================================================

# Get only the values
print(s.values)

# Output:
# [2 3 4 5 6]


# ============================================================
# 13. INDEX
# ============================================================

# Get the index values
print(s.index)

# Output:
# Index([1, 2, 3, 4, 5], dtype='int64')


# ============================================================
# 14. LOC - LABEL BASED INDEXING
# ============================================================

# Create a Series with subject names as indexes
marks = pd.Series({
    'Python': 85,
    'SQL': 90,
    'Statistics': 78,
    'Power BI': 88,
    'Machine Learning': 82
})

print(marks)

# .loc[] is used for LABEL-based indexing.

print(marks.loc['SQL'])

# Output:
# 90


# ============================================================
# 15. ILOC - POSITION BASED INDEXING
# ============================================================

# .iloc[] is used for POSITION-based indexing.

print(marks.iloc[1])

# Position 1 means the second element.

# Output:
# 90


# ============================================================
# LOC vs ILOC
# ============================================================

# loc  -> Label based
# iloc -> Position based

print(marks.loc['Python'])   # Label = Python
print(marks.iloc[0])         # Position = 0


# ============================================================
# IMPORTANT DIFFERENCE
# ============================================================

# loc uses INDEX LABEL
# iloc uses INTEGER POSITION

#
# Example:
#
# marks.loc['SQL']
#              ↑
#          label
#
# marks.iloc[1]
#             ↑
#         position
#


# ============================================================
# 16. SERIES WITH MISSING VALUES
# ============================================================

# np.nan represents a missing value.
#
# np.nan = Not a Number
#
# It is commonly used to represent missing data in Pandas.

car_data = {

    'model': [
        np.nan,
        'KIA',
        'Toyota',
        np.nan,
        'Hundai',
        'Nissa',
        'Nano',
        'Fortuner'
    ],

    'prices': [
        2000000,
        np.nan,
        4000000,
        5000000,
        np.nan,
        450000,
        900000,
        6700000
    ],

    'color': [
        np.nan,
        'red',
        'white',
        'blue',
        np.nan,
        'grey',
        'rainbow',
        'yellow'
    ]
}


# ============================================================
# 17. CREATE DATAFRAME
# ============================================================

# A dictionary containing multiple lists is usually converted
# into a DataFrame.

df = pd.DataFrame(car_data)

print(df)


# ============================================================
# 18. HEAD()
# ============================================================

# head() displays the first 5 rows by default.

print(df.head())


# Display the first 3 rows
print(df.head(3))


# ============================================================
# 19. TAIL()
# ============================================================

# tail() displays the last 5 rows by default.

print(df.tail())


# Display the last 3 rows
print(df.tail(3))


# ============================================================
# 20. SAMPLE()
# ============================================================

# sample() randomly selects rows.

print(df.sample(5))

# 5 random rows are displayed.


# ============================================================
# 21. SHAPE
# ============================================================

# shape returns:
#
# (number_of_rows, number_of_columns)

print(df.shape)

# Example:
# (8, 3)
#
# 8    -> rows
# 3    -> columns


# ============================================================
# 22. DTYPES
# ============================================================

# dtypes displays the data type of every column.

print(df.dtypes)


# ============================================================
# 23. INFO()
# ============================================================

# info() gives a summary of the DataFrame:
#
# - Number of rows
# - Column names
# - Non-null values
# - Data types
# - Memory usage

df.info()


# ============================================================
# 24. DESCRIBE()
# ============================================================

# describe() provides statistical information
# for numerical columns.

print(df.describe())

# Common statistics:
#
# count
# mean
# std
# min
# 25%
# 50%
# 75%
# max


# ============================================================
#                    QUICK SUMMARY
# ============================================================

# Series
# ------------------------------------------------------------
# pd.Series(data)
#
# One-dimensional labeled data.
#
#
# DataFrame
# ------------------------------------------------------------
# pd.DataFrame(data)
#
# Two-dimensional table.


# ============================================================
# IMPORTANT SERIES ATTRIBUTES
# ============================================================

# s.dtype
#     -> Data type of Series
#
# s.values
#     -> Values
#
# s.index
#     -> Index labels
#
# s.name
#     -> Name of Series
#
# s.shape
#     -> Shape
#
# s.size
#     -> Number of elements


# ============================================================
# IMPORTANT DATAFRAME METHODS
# ============================================================

# df.head()
#     -> First 5 rows
#
# df.tail()
#     -> Last 5 rows
#
# df.sample()
#     -> Random rows
#
# df.info()
#     -> DataFrame information
#
# df.describe()
#     -> Statistical summary
#
# df.shape
#     -> Rows and columns
#
# df.dtypes
#     -> Data types of columns


# ============================================================
#                    FINAL CONCEPT
# ============================================================

#                 PANDAS
#                    |
#          ---------------------
#          |                   |
#        Series             DataFrame
#          |                   |
#     1 Dimension         2 Dimensions
#          |                   |
#      Index + Data       Rows + Columns
#
# ============================================================