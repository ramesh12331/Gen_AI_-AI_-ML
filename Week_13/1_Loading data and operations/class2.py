# ============================================================
# PANDAS DATA CLEANING - COMPLETE PRACTICE
# ============================================================
# Topics covered:
# 1. Check DataFrame shape
# 2. Check missing values
# 3. Count missing values
# 4. Calculate missing-value percentage
# 5. Clean string columns using strip()
# 6. Replace incorrect values using replace()
# 7. Count unique values
# 8. Find rows containing missing values
# 9. Remove rows containing missing values
# ============================================================


import pandas as pd


# ============================================================
# 1. LOAD DATA
# ============================================================

# Read CSV file into a DataFrame
df = pd.read_csv("customer_dataset.csv")

print("Original Data:")
print(df)


# ============================================================
# 2. CHECK DATAFRAME SHAPE
# ============================================================

# shape returns:
# (number_of_rows, number_of_columns)

print("\nDataFrame Shape:")
print(df.shape)

# Example:
# (100, 10)
#
# 100 -> rows
# 10  -> columns


# ============================================================
# 3. CHECK DATAFRAME INFORMATION
# ============================================================

# info() gives:
# - column names
# - number of non-null values
# - data types

print("\nDataFrame Information:")
df.info()


# ============================================================
# 4. CHECK MISSING VALUES
# ============================================================

# isnull() checks every cell.
#
# True  -> value is missing
# False -> value is available

print("\nMissing Value Check:")
print(df.isnull())


# ============================================================
# 5. COUNT MISSING VALUES
# ============================================================

# isnull() gives True/False.
#
# sum() converts:
# True  -> 1
# False -> 0
#
# Therefore, sum() gives the number of missing values.

print("\nNumber of Missing Values:")
print(df.isnull().sum())


# ============================================================
# 6. CHECK MISSING-VALUE PROPORTION
# ============================================================

# df.shape[0] gives the total number of rows.
#
# Formula:
#
# Missing proportion =
# Number of missing values / Total number of rows

missing_ratio = df.isnull().sum() / df.shape[0]

print("\nMissing Value Ratio:")
print(missing_ratio)


# ============================================================
# 7. CHECK MISSING-VALUE PERCENTAGE
# ============================================================

# Formula:
#
# Missing percentage =
# Missing values / Total rows × 100

missing_percentage = (
    df.isnull().sum() / df.shape[0]
) * 100

print("\nMissing Value Percentage:")
print(missing_percentage)


# ============================================================
# 8. FIND COLUMNS WITH MISSING VALUES
# ============================================================

# First calculate missing values.

missing_count = df.isnull().sum()

# Select only columns where missing count > 0.

print("\nColumns Having Missing Values:")
print(missing_count[missing_count > 0])


# ============================================================
# 9. CLEAN CITY COLUMN - REMOVE EXTRA SPACES
# ============================================================

# str.strip() removes spaces from:
#
# beginning:
# "  Hyderabad"
#
# ending:
# "Hyderabad  "
#
# both:
# "  Hyderabad  "
#
# Result:
# "Hyderabad"

df["city"] = df["city"].str.strip()


# ============================================================
# 10. CHECK CITY VALUES BEFORE STANDARDIZATION
# ============================================================

# value_counts() counts how many times each value appears.

print("\nCity Value Counts:")
print(df["city"].value_counts())


# ============================================================
# 11. REPLACE INCORRECT CITY VALUES
# ============================================================

# Dictionary format:
#
# "old_value": "new_value"

city_mapping = {
    "Hyderabad": "Hyd",
    "Hyderbad": "Hyd",
    "hyderabad": "Hyd",
    "Delhi": "del",
    "Delhi ": "del",
    "Mumbai": "mumbai",
}

# replace() searches for the old values
# and replaces them with the new values.

df["city"] = df["city"].replace(city_mapping)


# ============================================================
# 12. CHECK CITY VALUES AFTER CLEANING
# ============================================================

print("\nCity Values After Cleaning:")
print(df["city"].value_counts())


# ============================================================
# 13. CHECK GENDER VALUES
# ============================================================

print("\nOriginal Gender Values:")
print(df["gender"].value_counts())


# ============================================================
# 14. REMOVE EXTRA SPACES FROM GENDER
# ============================================================

df["gender"] = df["gender"].str.strip()


# ============================================================
# 15. STANDARDIZE GENDER VALUES
# ============================================================

# We have different representations:
#
# Male
# male
# M
#
# Female
# female
# F

gender_mapping = {
    "Male": "M",
    "male": "M",
    "Female": "F",
    "female": "F",
}

df["gender"] = df["gender"].replace(gender_mapping)


# ============================================================
# 16. CHECK GENDER AFTER CLEANING
# ============================================================

print("\nGender Values After Cleaning:")
print(df["gender"].value_counts())


# ============================================================
# 17. CHECK MISSING VALUES AGAIN
# ============================================================

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================================
# 18. FIND ROWS HAVING AT LEAST ONE MISSING VALUE
# ============================================================

# isnull() -> checks missing cells
#
# any(axis=1) -> checks each ROW
#
# If at least one column is missing,
# that row becomes True.

rows_with_missing = df[df.isnull().any(axis=1)]

print("\nRows Having At Least One Missing Value:")
print(rows_with_missing)


# ============================================================
# 19. FIND ROWS WITH NO MISSING VALUES
# ============================================================

# dropna() removes rows containing missing values.
#
# The resulting DataFrame contains only complete rows.

complete_rows = df.dropna()

print("\nRows With No Missing Values:")
print(complete_rows)


# ============================================================
# 20. CHECK MISSING-VALUE PERCENTAGE AGAIN
# ============================================================

missing_percentage = (
    df.isnull().sum() / df.shape[0]
) * 100

print("\nFinal Missing Value Percentage:")
print(missing_percentage)


# ============================================================
# 21. COUNT NON-NULL VALUES
# ============================================================

# notnull() is the opposite of isnull().
#
# True  -> value exists
# False -> value is missing

print("\nNon-Null Values:")
print(df.notnull().sum())


# ============================================================
# 22. COUNT UNIQUE VALUES
# ============================================================

# nunique() gives the number of unique values.

print("\nNumber of Unique Values:")
print(df.nunique())


# ============================================================
# 23. VALUE COUNTS FOR EVERY COLUMN
# ============================================================

# Loop through every column.

print("\nValue Counts For Every Column:")

for col in df:

    print("\nColumn:", col)

    # value_counts() counts each unique value.
    # sum() gives the number of non-null values
    # represented in the value counts.

    counts_of_unique = df[col].value_counts().sum()

    print("Non-null values:", counts_of_unique)


# ============================================================
# 24. COUNT NON-NULL VALUES USING SHAPE AND ISNULL
# ============================================================

# Total rows - missing values
#
# Example:
#
# Total rows = 100
# Missing age = 8
#
# Non-null age = 100 - 8
#              = 92

print("\nNon-Null Count For Every Column:")

for col in df:

    non_null_count = (
        df.shape[0] - df[col].isnull().sum()
    )

    print(col, ":", non_null_count)


# ============================================================
# 25. FINAL DATASET
# ============================================================

print("\nFinal Cleaned Data:")
print(df)


# ============================================================
# 26. FINAL SUMMARY
# ============================================================

print("\n========================================")
print("FINAL DATA QUALITY SUMMARY")
print("========================================")

print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMissing Values:")
print(df.isnull().sum())

print("\nMissing Percentage:")
print(
    (df.isnull().sum() / df.shape[0]) * 100
)

print("\nUnique Values:")
print(df.nunique())