# ============================================================
#                 PANDAS DATA CLEANING PRACTICE
# ============================================================
#
# Topics from the class screenshots:
#
# 1. Load customer dataset
# 2. Convert salary to numeric
# 3. Convert join_date to datetime
# 4. Remove spaces from city
# 5. Replace incorrect city names
# 6. Check city value counts
# 7. Remove spaces from gender
# 8. Replace incorrect gender values
# 9. Check gender value counts
# 10. Check missing values
# 11. Find rows containing missing values
# 12. Count missing values
# 13. Find non-null values
# 14. Find unique values
# 15. Calculate missing percentage
# 16. Calculate data quality for every column
#
# ============================================================


import pandas as pd


# ============================================================
# 1. LOAD DATA
# ============================================================

# Read the CSV file and create a DataFrame.

df = pd.read_csv("customer_dataset.csv")


# Display first 5 rows

print("\n================ FIRST 5 ROWS ================\n")

print(df.head())


# ============================================================
# 2. CHECK DATA INFORMATION
# ============================================================

# info() gives:
#
# - number of rows
# - column names
# - non-null count
# - data types

print("\n================ DATA INFO ================\n")

df.info()


# ============================================================
# 3. CONVERT SALARY INTO NUMERIC
# ============================================================

# pd.to_numeric() converts values into numbers.
#
# errors="coerce"
#
# If Pandas finds an invalid value such as:
#
# "abc"
# "unknown"
# "not available"
#
# it converts that value into NaN.

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)


# ============================================================
# 4. CONVERT JOIN_DATE INTO DATETIME
# ============================================================

# pd.to_datetime() converts a column into
# Pandas datetime format.
#
# errors="coerce"
#
# Invalid dates become NaT.
#
# NaT = Not a Time

df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)


# ============================================================
# 5. REMOVE EXTRA SPACES FROM CITY
# ============================================================

# str.strip() removes spaces from the beginning
# and end of every string.
#
# Example:
#
# " Hyderabad " -> "Hyderabad"
#
# " Delhi"      -> "Delhi"
#
# "Mumbai "     -> "Mumbai"

df["city"] = df["city"].str.strip()


# ============================================================
# 6. CHECK CITY VALUES
# ============================================================

# value_counts() tells us how many times
# each city appears.

print("\n================ CITY VALUE COUNTS ================\n")

print(df["city"].value_counts())


# ============================================================
# 7. REPLACE INCORRECT CITY VALUES
# ============================================================

# We can create a dictionary:
#
# old value -> new value

city_mapping = {
    "Hyderabad": "Hyd",
    "Hyderbad": "Hyd",
    "hyderabad": "Hyd"
}


# replace() replaces the incorrect values.

df["city"] = df["city"].replace(city_mapping)


# ============================================================
# 8. SECOND CITY CLEANING
# ============================================================

# Another example from the class:
#
# Delhi -> del

city_mapping_2 = {
    "Delhi": "del",
    "Delhi ": "del"
}


df["city"] = df["city"].replace(city_mapping_2)


# ============================================================
# 9. REPLACE MUMBAI
# ============================================================

# Standardize Mumbai.

city_mapping_3 = {
    "Mumbai": "mumbai"
}


df["city"] = df["city"].replace(city_mapping_3)


# ============================================================
# 10. CHECK CITY VALUES AFTER CLEANING
# ============================================================

print("\n================ CLEANED CITY VALUES ================\n")

print(df["city"].value_counts())


# ============================================================
# 11. CHECK GENDER VALUES BEFORE CLEANING
# ============================================================

print("\n================ ORIGINAL GENDER VALUES ================\n")

print(df["gender"].value_counts())


# ============================================================
# 12. REMOVE EXTRA SPACES FROM GENDER
# ============================================================

# Remove unnecessary spaces.

df["gender"] = df["gender"].str.strip()


# ============================================================
# 13. STANDARDIZE GENDER VALUES
# ============================================================

# Dataset may contain:
#
# Male
# male
# M
#
# Female
# female
# F
#
# We convert them into:
#
# Male / male -> M
# Female / female -> F

gender_mapping = {

    "Male": "M",
    "male": "M",

    "Female": "F",
    "female": "F"
}


df["gender"] = df["gender"].replace(
    gender_mapping
)


# ============================================================
# 14. CHECK GENDER AFTER CLEANING
# ============================================================

print("\n================ CLEANED GENDER VALUES ================\n")

print(df["gender"].value_counts())


# Expected type of output:
#
# M        45
# F        35
# unknown  20


# ============================================================
# 15. CHECK NULL VALUES
# ============================================================

# isnull() checks every cell.
#
# True  -> value is missing
# False -> value is present

print("\n================ ISNULL() ================\n")

print(df.isnull())


# ============================================================
# 16. COUNT NULL VALUES
# ============================================================

# sum() converts:
#
# True  -> 1
# False -> 0
#
# Therefore:
#
# isnull().sum()
#
# gives the number of missing values
# in each column.

print("\n================ MISSING VALUE COUNT ================\n")

print(df.isnull().sum())


# ============================================================
# 17. CHECK DATAFRAME SHAPE
# ============================================================

# shape returns:
#
# (rows, columns)

print("\n================ DATAFRAME SHAPE ================\n")

print(df.shape)


# Example:
#
# (100, 10)
#
# 100 = number of rows
# 10  = number of columns


# ============================================================
# 18. COUNT MISSING VALUES USING SUM()
# ============================================================

missing_values = df.isnull().sum()

print("\n================ MISSING VALUES ================\n")

print(missing_values)


# ============================================================
# 19. CALCULATE MISSING VALUE RATIO
# ============================================================

# df.shape[0]
#
# gives the total number of rows.
#
# Formula:
#
# missing values / total rows

missing_ratio = (
    df.isnull().sum()
    / df.shape[0]
)


print("\n================ MISSING VALUE RATIO ================\n")

print(missing_ratio)


# ============================================================
# 20. CALCULATE MISSING VALUE PERCENTAGE
# ============================================================

# Formula:
#
# missing values / total rows * 100

missing_percentage = (
    df.isnull().sum()
    / df.shape[0]
    * 100
)


print("\n================ MISSING VALUE PERCENTAGE ================\n")

print(missing_percentage)


# ============================================================
# 21. FIND ROWS HAVING NULL VALUES
# ============================================================

# isnull() gives True/False for every cell.
#
# any(axis=1) checks each row.
#
# If at least one value is missing,
# that row will be selected.

rows_with_null = df[
    df.isnull().any(axis=1)
]


print("\n================ ROWS WITH NULL VALUES ================\n")

print(rows_with_null)


# ============================================================
# 22. FIND ONLY NULL VALUES
# ============================================================

# This is useful when we want to see
# where the missing values are.

null_values = df[
    df.isnull()
]


print("\n================ NULL VALUES ================\n")

print(null_values)


# ============================================================
# 23. FIND NON-NULL VALUES
# ============================================================

# notnull() is the opposite of isnull().
#
# True  -> value exists
# False -> value is missing

print("\n================ NON-NULL CHECK ================\n")

print(df.notnull())


# ============================================================
# 24. COUNT NON-NULL VALUES
# ============================================================

print("\n================ NON-NULL COUNT ================\n")

print(df.notnull().sum())


# ============================================================
# 25. COUNT UNIQUE VALUES
# ============================================================

# value_counts() returns the frequency
# of every value.
#
# sum() gives the total number of
# non-null records.

print("\n================ UNIQUE VALUE COUNTS ================\n")

for col in df:

    counts_of_unique = (
        df[col]
        .value_counts()
        .sum()
    )

    print(
        col,
        "->",
        counts_of_unique
    )


# ============================================================
# 26. COUNT ACTUAL UNIQUE VALUES
# ============================================================

# nunique() gives the number of
# distinct values in each column.
#
# Example:
#
# city:
#
# Hyd
# del
# ban
# mumbai
#
# unique count = 4

print("\n================ NUMBER OF UNIQUE VALUES ================\n")

print(df.nunique())


# ============================================================
# 27. UNIQUE VALUES FOR EVERY COLUMN
# ============================================================

# unique() displays the actual unique values.

print("\n================ ACTUAL UNIQUE VALUES ================\n")

for col in df:

    print("\nColumn:", col)

    print(df[col].unique())


# ============================================================
# 28. UNIQUE COUNT AND NULL COUNT
# ============================================================

# The class demonstrated looping through
# every column.
#
# value_counts().sum()
# gives the number of non-null records.
#
# df[col].isnull().sum()
# gives the number of null records.

print("\n================ COLUMN DATA CHECK ================\n")

for col in df:

    non_null_count = (
        df[col]
        .value_counts()
        .sum()
    )

    null_count = (
        df[col]
        .isnull()
        .sum()
    )

    print(
        col,
        "-> Non-null:",
        non_null_count,
        "| Null:",
        null_count
    )


# ============================================================
# 29. TOTAL ROWS AND NON-NULL VALUES
# ============================================================

# Another way to calculate non-null count:
#
# total rows - null values
#
# Example:
#
# Total rows = 100
# Null values = 8
#
# Non-null = 100 - 8
#          = 92

print("\n================ NON-NULL COUNT ================\n")

for col in df:

    non_null_count = (
        df.shape[0]
        - df[col].isnull().sum()
    )

    print(
        col,
        "->",
        non_null_count
    )


# ============================================================
# 30. DATA QUALITY CHECK
# ============================================================

print("\n================ DATA QUALITY CHECK ================\n")

for col in df:

    # Total number of rows
    total_rows = df.shape[0]

    # Number of missing values
    null_count = df[col].isnull().sum()

    # Number of available values
    non_null_count = total_rows - null_count

    # Percentage of available data
    non_null_percentage = (
        non_null_count / total_rows
    ) * 100

    print(
        col,
        "->",
        "Non-null:",
        non_null_count,
        "|",
        "Null:",
        null_count,
        "|",
        "Available:",
        round(non_null_percentage, 2),
        "%"
    )


# ============================================================
# 31. FINAL MISSING VALUE REPORT
# ============================================================

print("\n================================================")
print("             FINAL MISSING VALUE REPORT")
print("================================================")

print(
    df.isnull().sum()
)


# ============================================================
# 32. FINAL MISSING PERCENTAGE REPORT
# ============================================================

print("\n================================================")
print("          FINAL MISSING PERCENTAGE REPORT")
print("================================================")

print(
    (
        df.isnull().sum()
        / df.shape[0]
    ) * 100
)


# ============================================================
# 33. FINAL DATAFRAME
# ============================================================

print("\n================================================")
print("                 FINAL DATA")
print("================================================")

print(df)


# ============================================================
#                     END
# ============================================================