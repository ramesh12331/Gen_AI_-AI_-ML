# ============================================================
#                    PANDAS DATAFRAME
# ============================================================
#
# Topics Covered:
#
# 1. Import Pandas
# 2. Create DataFrame using Dictionary
# 3. Create DataFrame using Nested Dictionary
# 4. Create Empty DataFrame
# 5. Read CSV File
# 6. Read CSV using Full Path
# 7. CSV Encoding
# 8. Remove Unwanted Columns
# 9. Read Excel File
# 10. Read Excel using Full Path
# 11. Read Specific Excel Sheet
# 12. DataFrame Shape
# 13. Rows and Columns
# 14. Column Names
# 15. DataFrame Info
# 16. head()
# 17. tail()
# 18. Read JSON/API Data
# 19. json_normalize()
# 20. Select Required Columns
# 21. Read Large CSV Dataset
# 22. usecols
#
# ============================================================


# ============================================================
# 1. IMPORT PANDAS
# ============================================================

# Pandas is a Python library used for:
#
# - Data manipulation
# - Data analysis
# - Data cleaning
# - Working with tabular data
#
# "pd" is the commonly used alias for pandas.

import pandas as pd


# ============================================================
# 2. CREATE DATAFRAME USING A DICTIONARY
# ============================================================

# A dictionary can be converted into a DataFrame.
#
# Dictionary:
#     key   -> column name
#     value -> column data

data = {
    "name": ["a", "b", "c"],
    "age": [20, 30, 40]
}


# Convert dictionary into DataFrame

df = pd.DataFrame(data)


# Display DataFrame

print("DataFrame:")
print(df)


# Expected output:
#
#   name  age
# 0    a   20
# 1    b   30
# 2    c   40


# ============================================================
# 3. CREATE DATAFRAME USING NESTED DICTIONARY
# ============================================================

# A nested dictionary contains dictionaries inside a dictionary.
#
# Outer dictionary:
#     column names
#
# Inner dictionary:
#     index -> value

data = {

    "student_id": {
        1: 101,
        2: 102,
        3: 103,
        4: 104,
        5: 105
    },

    "name": {
        1: "Rahul",
        2: "Priya",
        3: "Arjun",
        4: "Sneha",
        5: "Kiran"
    },

    "age": {
        1: 21,
        2: 22,
        3: 20,
        4: 23,
        5: 21
    },

    "course": {
        1: "Python",
        2: "Data Science",
        3: "Power BI",
        4: "Python",
        5: "SQL"
    },

    "marks": {
        1: 85,
        2: 92,
        3: 78,
        4: 88,
        5: 75
    }
}


# Convert nested dictionary into DataFrame

df = pd.DataFrame(data)


# Display DataFrame

print("\nNested Dictionary DataFrame:")
print(df)


# ============================================================
# 4. CREATE EMPTY DATAFRAME
# ============================================================

# Sometimes we need an empty DataFrame.
#
# We can add data later.

empty_df = pd.DataFrame()


print("\nEmpty DataFrame:")
print(empty_df)


# ============================================================
#                 READING DATA FROM FILES
# ============================================================
#
# Pandas can read data from many sources:
#
# CSV
# Excel
# JSON
# SQL Database
# HTML
# API
#
# ============================================================


# ============================================================
# 5. READ CSV FILE
# ============================================================

# CSV means:
# Comma Separated Values
#
# Syntax:
#
# pd.read_csv("file_name.csv")

df = pd.read_csv("demo90.csv")


# Display DataFrame

print("\nCSV Data:")
print(df)


# ============================================================
# 6. DISPLAY FIRST 5 ROWS
# ============================================================

# head() returns the first 5 rows by default.

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 7. DISPLAY FIRST 10 ROWS
# ============================================================

# We can pass a number to head().
#
# head(10) -> first 10 rows

print("\nFirst 10 rows:")
print(df.head(10))


# ============================================================
# 8. DISPLAY LAST 5 ROWS
# ============================================================

# tail() returns the last 5 rows by default.

print("\nLast 5 rows:")
print(df.tail())


# ============================================================
# 9. DISPLAY LAST 10 ROWS
# ============================================================

print("\nLast 10 rows:")
print(df.tail(10))


# ============================================================
# 10. READ CSV USING FULL FILE PATH
# ============================================================

# We can provide the complete path of the CSV file.
#
# Forward slash "/" can be used in Windows paths.

df = pd.read_csv(
    "C:/Users/DELL/Downloads/db.data.csv"
)


print("\nCSV from full path:")
print(df.head())


# ============================================================
# 11. WINDOWS PATH USING RAW STRING
# ============================================================

# Another way to write a Windows path is:
#
# r"C:\Users\DELL\Downloads\db.data.csv"
#
# The "r" creates a raw string.
#
# This prevents backslash characters from being treated
# as escape characters.

df = pd.read_csv(
    r"C:\Users\DELL\Downloads\db.data.csv"
)


print("\nCSV using raw string path:")
print(df.head())


# ============================================================
# 12. READ CSV WITH ENCODING
# ============================================================

# Some CSV files contain special characters.
#
# Sometimes Python may show:
#
# UnicodeDecodeError
#
# We can specify the encoding.

df = pd.read_csv(
    "data.csv",
    encoding="latin1"
)


print("\nCSV with latin1 encoding:")
print(df.head())


# Common encodings:
#
# UTF-8:
# encoding="utf-8"
#
# Latin-1:
# encoding="latin1"
#
# Windows:
# encoding="cp1252"


# ============================================================
# 13. REMOVE UNWANTED INDEX COLUMN
# ============================================================

# Sometimes a CSV file contains a column:
#
# Unnamed: 0
#
# This usually happens when a DataFrame index
# was previously saved into the CSV file.

df = pd.read_csv("demo90.csv")


# Remove the unwanted column.

df = df.drop(
    columns=["Unnamed: 0"],
    errors="ignore"
)


print("\nAfter removing unwanted column:")
print(df.head())


# ============================================================
#                 READING EXCEL FILES
# ============================================================


# ============================================================
# 14. INSTALL OPENPYXL
# ============================================================

# Pandas commonly uses openpyxl to read .xlsx files.
#
# Install from VS Code terminal:
#
# pip install openpyxl
#
# If using Jupyter Notebook:
#
# !pip install openpyxl


# ============================================================
# 15. READ EXCEL FILE
# ============================================================

# Syntax:
#
# pd.read_excel("file_name.xlsx")

df = pd.read_excel(
    "small_student_dataset.xlsx"
)


print("\nExcel Data:")
print(df)


# ============================================================
# 16. READ EXCEL USING FULL PATH
# ============================================================

df = pd.read_excel(
    r"C:\Users\DELL\Downloads\data0.xlsx"
)


print("\nExcel from full path:")
print(df.head())


# ============================================================
# 17. READ EXCEL FROM ANOTHER LOCATION
# ============================================================

# Example from the screenshot:

df = pd.read_excel(
    r"C:\Users\DELL\OneDrive\Desktop\Aimp part1.xlsx"
)


print("\nExcel from another location:")
print(df.head())


# ============================================================
# 18. READ SPECIFIC EXCEL SHEET
# ============================================================

# If an Excel file contains multiple sheets,
# we can specify the sheet name.

df = pd.read_excel(
    "students.xlsx",
    sheet_name="Sheet1"
)


print("\nSpecific Excel Sheet:")
print(df.head())


# ============================================================
#                 DATAFRAME INFORMATION
# ============================================================


# ============================================================
# 19. CHECK DATAFRAME SHAPE
# ============================================================

# shape returns:
#
#     (number_of_rows, number_of_columns)
#
# Example:
#
# (7905, 8)
#
# means:
#
# 7905 rows
# 8 columns

print("\nDataFrame Shape:")
print(df.shape)


# ============================================================
# 20. GET NUMBER OF ROWS
# ============================================================

# shape[0] gives the number of rows.

number_of_rows = df.shape[0]

print("\nNumber of rows:")
print(number_of_rows)


# ============================================================
# 21. GET NUMBER OF COLUMNS
# ============================================================

# shape[1] gives the number of columns.

number_of_columns = df.shape[1]

print("\nNumber of columns:")
print(number_of_columns)


# ============================================================
# 22. GET COLUMN NAMES
# ============================================================

# df.columns returns all column names.

print("\nColumn names:")
print(df.columns)


# ============================================================
# 23. CONVERT COLUMN NAMES INTO LIST
# ============================================================

# tolist() converts the column names into
# a normal Python list.

column_names = df.columns.tolist()

print("\nColumn names as list:")
print(column_names)


# ============================================================
# 24. CHECK DATA TYPES
# ============================================================

# dtypes tells us the data type of each column.

print("\nData types:")
print(df.dtypes)


# ============================================================
# 25. DATAFRAME INFORMATION USING info()
# ============================================================

# info() displays:
#
# - Number of rows
# - Column names
# - Non-null values
# - Data types
# - Memory usage

print("\nDataFrame Information:")

df.info()


# ============================================================
# 26. STATISTICAL SUMMARY
# ============================================================

# describe() gives statistical information
# about numerical columns.
#
# Examples:
# - count
# - mean
# - standard deviation
# - minimum
# - maximum

print("\nStatistical Summary:")

print(df.describe())


# ============================================================
#                 WORKING WITH COLUMNS
# ============================================================


# ============================================================
# 27. SELECT ONE COLUMN
# ============================================================

# Syntax:
#
# df["column_name"]

# Example:

# print(df["Name"])


# ============================================================
# 28. SELECT MULTIPLE COLUMNS
# ============================================================

# Syntax:
#
# df[["column1", "column2"]]

# Example:

# selected_columns = df[
#     ["Name", "Course", "Marks"]
# ]

# print(selected_columns)


# ============================================================
# 29. FILTER DATA
# ============================================================

# Example:
#
# Get students whose marks are greater than 80.

# result = df[
#     df["Marks"] > 80
# ]

# print(result)


# ============================================================
# 30. FILTER BY COURSE
# ============================================================

# Example:
#
# Get students studying Python.

# result = df[
#     df["Course"] == "Python"
# ]

# print(result)


# ============================================================
#                 FETCH DATA FROM API
# ============================================================


# ============================================================
# 31. IMPORT REQUESTS
# ============================================================

# requests is used to communicate with APIs.

import requests


# ============================================================
# 32. API URL
# ============================================================

# JSONPlaceholder is a test API.
#
# It provides sample JSON data.

users_url = (
    "https://jsonplaceholder.typicode.com/users"
)


# ============================================================
# 33. SEND GET REQUEST
# ============================================================

# requests.get() sends a GET request to the API.

users_response = requests.get(
    users_url
)


# ============================================================
# 34. CHECK RESPONSE STATUS CODE
# ============================================================

print("\nAPI Status Code:")

print(users_response.status_code)


# Common status codes:
#
# 200 -> Request successful
# 404 -> Resource not found
# 500 -> Server error


# ============================================================
# 35. CONVERT API RESPONSE TO JSON
# ============================================================

# .json() converts the JSON response
# into a Python object.

data = users_response.json()


# Display API data

print("\nAPI JSON Data:")

print(data)


# ============================================================
# 36. CONVERT API DATA INTO DATAFRAME
# ============================================================

# If the JSON contains a simple list of dictionaries,
# we can directly use pd.DataFrame().

df = pd.DataFrame(data)


print("\nAPI DataFrame:")

print(df.head())


# ============================================================
#                 JSON NORMALIZE
# ============================================================


# ============================================================
# 37. USE pd.json_normalize()
# ============================================================

# API JSON data can contain nested dictionaries.
#
# Example:
#
# address
#     street
#     city
#     zipcode
#
# json_normalize() converts nested JSON
# into tabular DataFrame format.

df = pd.json_normalize(data)


print("\nNormalized JSON Data:")

print(df.head())


# ============================================================
# 38. SELECT REQUIRED API COLUMNS
# ============================================================

# We don't always need every column.
#
# We can select only the columns we need.

df = df[
    [
        "id",
        "name",
        "email",
        "phone",
        "website"
    ]
]


print("\nSelected API Columns:")

print(df.head())


# ============================================================
# 39. GET API COLUMN NAMES
# ============================================================

print("\nAPI Column Names:")

print(df.columns)


# Convert into list

column_names = df.columns.tolist()

print("\nAPI Column Names as List:")

print(column_names)


# ============================================================
#                 LARGE CSV DATASET
# ============================================================


# ============================================================
# 40. READ LARGE CSV FILE
# ============================================================

# Example:
#
# large_sales_database_dataset_500k.csv
#
# This dataset contains:
#
# 500,000 rows
# 14 columns

large_df = pd.read_csv(
    r"C:\Users\DELL\Downloads\large_sales_database_dataset_500k.csv"
)


# Display first 5 rows

print("\nLarge Dataset:")

print(large_df.head())


# ============================================================
# 41. CHECK LARGE DATASET SHAPE
# ============================================================

print("\nLarge Dataset Shape:")

print(large_df.shape)


# Example output:
#
# (500000, 14)
#
# 500000 -> rows
# 14     -> columns


# ============================================================
# 42. READ ONLY REQUIRED COLUMNS
# ============================================================

# Large datasets can contain many columns.
#
# If we only need some columns,
# use the usecols parameter.

large_df = pd.read_csv(
    r"C:\Users\DELL\Downloads\large_sales_database_dataset_500k.csv",

    usecols=[
        "customer_id",
        "customer_name",
        "country",
        "city",
        "age",
        "gender",
        "product",
        "category"
    ]
)


# Display first 5 rows

print("\nSelected Columns From Large Dataset:")

print(large_df.head())


# ============================================================
# 43. CHECK SELECTED DATASET SHAPE
# ============================================================

print("\nSelected Dataset Shape:")

print(large_df.shape)


# ============================================================
#              COMPLETE STUDENT EXAMPLE
# ============================================================


# ============================================================
# 44. CREATE STUDENT DATAFRAME
# ============================================================

student_data = {

    "Student_ID": [
        101,
        102,
        103,
        104,
        105
    ],

    "Name": [
        "Rahul",
        "Priya",
        "Arjun",
        "Sneha",
        "Kiran"
    ],

    "Age": [
        21,
        22,
        20,
        23,
        21
    ],

    "Course": [
        "Python",
        "SQL",
        "Power BI",
        "Python",
        "Data Science"
    ],

    "Marks": [
        85,
        92,
        78,
        88,
        95
    ]
}


# Create DataFrame

students = pd.DataFrame(student_data)


# Display DataFrame

print("\nStudent DataFrame:")

print(students)


# ============================================================
# 45. DISPLAY FIRST 5 STUDENTS
# ============================================================

print("\nFirst 5 Students:")

print(students.head())


# ============================================================
# 46. DISPLAY LAST 2 STUDENTS
# ============================================================

print("\nLast 2 Students:")

print(students.tail(2))


# ============================================================
# 47. STUDENT DATAFRAME SHAPE
# ============================================================

print("\nStudent DataFrame Shape:")

print(students.shape)


# ============================================================
# 48. STUDENT COLUMN NAMES
# ============================================================

print("\nStudent Column Names:")

print(students.columns)


# ============================================================
# 49. SELECT STUDENT NAMES
# ============================================================

print("\nStudent Names:")

print(students["Name"])


# ============================================================
# 50. SELECT MULTIPLE COLUMNS
# ============================================================

print("\nName, Course and Marks:")

print(
    students[
        [
            "Name",
            "Course",
            "Marks"
        ]
    ]
)


# ============================================================
# 51. FILTER STUDENTS WITH MARKS > 80
# ============================================================

result = students[
    students["Marks"] > 80
]


print("\nStudents with Marks greater than 80:")

print(result)


# ============================================================
# 52. FILTER PYTHON STUDENTS
# ============================================================

python_students = students[
    students["Course"] == "Python"
]


print("\nPython Students:")

print(python_students)


# ============================================================
#                    IMPORTANT SUMMARY
# ============================================================

# DataFrame creation:
#
# pd.DataFrame()
#
#
# CSV:
#
# pd.read_csv()
#
#
# Excel:
#
# pd.read_excel()
#
#
# API:
#
# requests.get()
#
#
# JSON:
#
# response.json()
#
#
# Nested JSON:
#
# pd.json_normalize()
#
#
# First rows:
#
# df.head()
#
#
# Last rows:
#
# df.tail()
#
#
# Shape:
#
# df.shape
#
#
# Number of rows:
#
# df.shape[0]
#
#
# Number of columns:
#
# df.shape[1]
#
#
# Column names:
#
# df.columns
#
#
# Column names as list:
#
# df.columns.tolist()
#
#
# Data types:
#
# df.dtypes
#
#
# Information:
#
# df.info()
#
#
# Statistics:
#
# df.describe()
#
#
# Select one column:
#
# df["column"]
#
#
# Select multiple columns:
#
# df[["column1", "column2"]]
#
#
# Filter rows:
#
# df[df["column"] > value]
#
#
# Read selected CSV columns:
#
# pd.read_csv(
#     "file.csv",
#     usecols=["col1", "col2"]
# )
#
# ============================================================
#                         END
# ============================================================