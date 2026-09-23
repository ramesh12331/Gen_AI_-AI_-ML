import pandas as pd 

data = {
    "name": ["a", "b", "c"],
    "age": [20, 30, 40]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# 3. CREATE DATAFRAME USING NESTED DICTIONARY
# ============================================================

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

df = pd.DataFrame(data)
print(df)

# ============================================================
# 4. CREATE EMPTY DATAFRAME
# ============================================================
empty_df = pd.DataFrame()
print(empty_df)

# ============================================================
# 5. READ CSV FILE
# ============================================================
df = pd.read_csv('demo90.csv')
print(df)
# ============================================================
# 6. DISPLAY FIRST 5 ROWS
# ============================================================
print(df.head())

# ============================================================
# 7. DISPLAY FIRST 10 ROWS
# ============================================================

# We can pass a number to head().
#
# head(10) -> first 10 rows

print("\nFirst 4 rows:")
print(df.head(4))

# ============================================================
# 8. DISPLAY LAST 5 ROWS
# ============================================================
print(df.tail())

# ============================================================
# 9. DISPLAY LAST 10 ROWS
# ============================================================

print("\nLast 4 rows:")
print(df.tail(4))

# ============================================================
# 10. READ CSV USING FULL FILE PATH
# ============================================================
df = pd.read_csv('D:/RAMESH/Gen_AI_ AI_ ML/Week_12/3_Pandas - DataFrames/data.csv')
print(df)
print(df.head())
print(df.tail())

# ============================================================
# 11. WINDOWS PATH USING RAW STRING
# ============================================================
df = pd.read_csv(r'D:/RAMESH/Gen_AI_ AI_ ML/Week_12/3_Pandas - DataFrames/data.csv')
print(df)
print(df.head())
print(df.tail(20))

# ============================================================
# 12. READ CSV WITH ENCODING
# ============================================================
df = pd.read_csv("data.csv", encoding="latin1")
print(df.head())

# ============================================================
# 13. REMOVE UNWANTED INDEX COLUMN
# ============================================================

df = pd.read_csv("data.csv")
df = df.drop(columns=["Unnamed: 0"], errors="ignore")
print(df.head())

# ============================================================
#                 READING EXCEL FILES
# ============================================================

df = pd.read_excel("student_dataset.xlsx")
print(df)

# ============================================================
# 16. READ EXCEL USING FULL PATH
# ============================================================
df = pd.read_excel("D:/RAMESH/Gen_AI_ AI_ ML/Week_12/3_Pandas - DataFrames/student_dataset.xlsx")
print(df.tail(100))

# ============================================================
# 18. READ SPECIFIC EXCEL SHEET
# ============================================================

# If an Excel file contains multiple sheets,
# we can specify the sheet name.

df = pd.read_excel(
    "student_dataset.xlsx",
    sheet_name="Students"
)


print("\nSpecific Excel Sheet:")
print(df.tail())
# ============================================================
# 19. CHECK DATAFRAME SHAPE
# ============================================================
print(df.shape)

# ============================================================
# 20. GET NUMBER OF ROWS
# ============================================================
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
print(df.columns)

# ============================================================
# 23. CONVERT COLUMN NAMES INTO LIST
# ============================================================
column_names = df.columns.tolist()
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

df.info()

# ============================================================
# 26. STATISTICAL SUMMARY
# ============================================================
print(df.describe())

# ============================================================
# 28. SELECT MULTIPLE COLUMNS
# ============================================================
selected_columns = df[["name", "age", "gender", "total_marks"]]
print(selected_columns)

# ============================================================
# 32. API URL
# ============================================================
import requests

user_url = ("https://jsonplaceholder.typicode.com/users")
# ============================================================
# 33. SEND GET REQUEST
# ============================================================

users_response = requests.get(user_url)
print(users_response.status_code)

data = users_response.json()
print(data)

# ============================================================
# 36. CONVERT API DATA INTO DATAFRAME
# ============================================================
df = pd.DataFrame(data)
print(df)
print(df.head())

# ============================================================
# 37. USE pd.json_normalize()
# ============================================================
df = pd.json_normalize(data)
print(df.head())

# ============================================================
# 38. SELECT REQUIRED API COLUMNS
# ============================================================
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

column_names = df.columns.tolist()

print("\nAPI Column Names as List:")

print(column_names)