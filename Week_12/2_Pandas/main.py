import pandas as pd

# ============================================================
# 1. CREATE SERIES USING A LIST
# ============================================================
numbers = [23, 45, 64, 53, 21]

s = pd.Series(numbers)
print(s)

# ============================================================
# 2. SERIES SLICING
# ============================================================
print(s[0:3])

# ============================================================
# 3. CREATE SERIES USING LIST + CUSTOM INDEX
# ============================================================

s = pd.Series(numbers, index=['A', 'B', 'C', 'D', 'E'])
print(s)

# ============================================================
# ACCESS VALUE USING CUSTOM INDEX
# ============================================================
print(s['C'])

# ============================================================
# 4. CREATE SERIES USING A DICTIONARY
# ============================================================
student_data = {
    'name': ['Rahul', 'Mishra', 'Abdul', 'Venky'],
    'age': [20, 30, 40, 50],
    'city': ['Hyderabad', 'Bangalore', 'Chennai', 'AP']
}

s = pd.Series(student_data)
print(s)

print(s["name"])
print(s["name"][1])

# ============================================================
# 5. CREATE SERIES USING NUMPY ARRAY
# ============================================================
import numpy as np

# Create a NumPy array
arr = np.array([2, 3, 4, 5, 6])

s = pd.Series(
    arr,
    name = 'num',
    index=[1, 2, 3, 4, 5],
    dtype='int32'
)
print(s)

# ============================================================
# 6. SERIES NAME
# ============================================================

# Access the name of the Series
print(s.name)

# ============================================================
# 8. REVERSE A SERIES
# ============================================================
print(s[::-1])
# ============================================================
# 9. INDEXING
# ============================================================

# Access value using index
print(s[2])
# ============================================================
# 10. SLICING
# ============================================================

# Get values from position 1 to position 3
# Stop position is excluded
print("\n SLICING")
print(s[1:4])

# ============================================================
# 11. DTYPE
# ============================================================

# Check the data type of Series
print(s.dtype)

# ============================================================
# 12. VALUES
# ============================================================

# Get only the values
print(s.values)

# ============================================================
# 13. INDEX
# ============================================================

# Get the index values
print(s.index)

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

print(marks.loc['SQL'])
# ============================================================
# 15. ILOC - POSITION BASED INDEXING
# ============================================================

# .iloc[] is used for POSITION-based indexing.
print(marks.iloc[1])

# ============================================================
# LOC vs ILOC
# ============================================================

# loc  -> Label based
# iloc -> Position based

print(marks.loc['Python'])   # Label = Python
print(marks.iloc[0])         # Position = 0

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

# ============================================================
# 21. SHAPE
# ============================================================
print(df.shape)

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