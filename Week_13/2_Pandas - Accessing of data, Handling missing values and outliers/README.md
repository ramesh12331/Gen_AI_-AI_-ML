# 🐼 PANDAS — COMPLETE BEGINNER NOTES

## 📚 Topics Covered

1. 🐼 What is Pandas?
2. 📊 DataFrame
3. 📦 Nested Dictionary → DataFrame
4. 🔍 Inspecting Data
5. ✏️ Rename
6. 🔄 Reset Index
7. 🗑️ Drop Rows & Columns
8. 📂 Read Excel
9. 🔎 Missing Values
10. 🩹 `fillna()`
11. 📐 Median
12. 📊 `value_counts()`
13. 📈 Histogram
14. 📦 Boxplot
15. 🎯 Column Selection
16. 📍 `.loc`
17. 🔢 `.iloc`
18. ➕ Add Columns
19. ⚡ `apply()`
20. 🏹 Lambda
21. 🎤 Interview Questions & Answers

---

# 🐼 CHAPTER 1 — WHAT IS PANDAS?

## 🔹 What?

Pandas is a Python library used to work with **structured/tabular data**.

You can think of Pandas as a tool that allows Python to work with data similar to:

* 📊 Excel
* 🗄️ SQL tables
* 📄 CSV files
* 📗 JSON data

---

## 🎯 Why do we use Pandas?

Pandas is useful for:

* Reading CSV files
* Reading Excel files
* Cleaning data
* Finding missing values
* Removing unwanted data
* Selecting rows and columns
* Filtering data
* Performing calculations
* Preparing data for Machine Learning
* Data analysis

---

## 📖 Definition

> **Pandas is an open-source Python library used for data manipulation, data cleaning, and data analysis.**

---

## 🧩 Syntax

```python
import pandas as pd
```

---

## 💻 Example

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Arjun"],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age
0  Rahul   21
1  Priya   22
2  Arjun   20
```

---

## 📝 Summary

```text
Pandas
  ↓
Python library
  ↓
Data manipulation
  ↓
Data cleaning
  ↓
Data analysis
```

---

# 📊 CHAPTER 2 — DATAFRAME

## 🔹 What?

A DataFrame is a table containing rows and columns.

---

## 🎯 Why?

We use DataFrames because real-world datasets are usually arranged as tables.

Example:

```text
Name    Age    City
Rahul   21     Hyderabad
Priya   22     Mumbai
Arjun   20     Delhi
```

---

## 📖 Definition

> **A DataFrame is a two-dimensional labeled data structure containing rows and columns.**

---

## 🧩 Syntax

```python
df = pd.DataFrame(data)
```

---

## 💻 Example

```python
data = {
    "Name": ["Rahul", "Priya", "Arjun"],
    "Age": [21, 22, 20],
    "City": ["Hyderabad", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

print(df)
```

---

## 📝 Summary

```text
DataFrame = Rows + Columns + Index
```

---

# 📦 CHAPTER 3 — NESTED DICTIONARY

## 🔹 What?

A nested dictionary is a dictionary containing other dictionaries.

---

## 🎯 Why?

Nested dictionaries are useful when data contains multiple columns with common index values.

---

## 📖 Definition

> **A nested dictionary is a dictionary where one or more values are themselves dictionaries.**

---

## 🧩 Syntax

```python
data = {
    "column1": {
        1: value,
        2: value
    },
    "column2": {
        1: value,
        2: value
    }
}
```

---

## 💻 Example

```python
data = {
    "student_id": {
        1: 101,
        2: 102,
        3: 103
    },

    "name": {
        1: "Rahul",
        2: "Priya",
        3: "Arjun"
    },

    "age": {
        1: 21,
        2: 22,
        3: 20
    }
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
   student_id   name  age
1         101  Rahul   21
2         102  Priya   22
3         103  Arjun   20
```

---

# 🔍 CHAPTER 4 — `head()`

## 🔹 What?

`head()` displays the first rows.

## 🎯 Why?

To quickly inspect the beginning of a dataset.

## 📖 Definition

> `head()` returns the first 5 rows by default.

## 🧩 Syntax

```python
df.head()
```

or:

```python
df.head(10)
```

## 💻 Example

```python
print(df.head())
```

```python
print(df.head(10))
```

## 📝 Summary

```text
head() → First rows
head(10) → First 10 rows
```

---

# 📏 CHAPTER 5 — `shape`

## 🔹 What?

`shape` tells us the number of rows and columns.

## 🎯 Why?

To understand the size of the dataset.

## 📖 Definition

> `shape` returns a tuple containing `(rows, columns)`.

## 🧩 Syntax

```python
df.shape
```

## 💻 Example

```python
print(df.shape)
```

Output:

```text
(15, 5)
```

Meaning:

```text
15 rows
5 columns
```

---

# 🏷️ CHAPTER 6 — `columns`

## 🔹 What?

`columns` gives the names of DataFrame columns.

## 🎯 Why?

To understand what variables are available.

## 🧩 Syntax

```python
df.columns
```

For a Python list:

```python
df.columns.tolist()
```

## 💻 Example

```python
print(df.columns.tolist())
```

Output:

```text
['student_id', 'name', 'age', 'course', 'marks']
```

---

# 🔤 CHAPTER 7 — `dtypes`

## 🔹 What?

`dtypes` tells us the data type of each column.

## 🎯 Why?

Before analysis, we need to know whether data is:

* 🔢 Integer
* 🔢 Float
* 🔤 Text
* 📅 Date
* ✅ Boolean

## 🧩 Syntax

```python
df.dtypes
```

## 💻 Example

```python
print(df.dtypes)
```

Example output:

```text
student_id     int64
name          object
age            int64
marks          int64
```

## 📝 Summary

```text
dtypes → Data types of columns
```

---

# ✏️ CHAPTER 8 — `rename()`

## 🔹 What?

`rename()` changes column or index names.

## 🎯 Why?

Sometimes column names are:

* Too long
* Incorrect
* Inconsistent
* Difficult to understand

## 📖 Definition

> `rename()` is used to change the labels of rows or columns.

## 🧩 Syntax

```python
df.rename(
    columns={"old_name": "new_name"},
    inplace=True
)
```

## 💻 Example

```python
df.rename(
    columns={"student_id": "id"},
    inplace=True
)
```

Now:

```text
student_id → id
```

---

# 🔢 CHAPTER 9 — RENAME INDEX

## 🔹 What?

You can also rename an index.

## 🧩 Syntax

```python
df.rename(
    index={old_index: new_index},
    inplace=True
)
```

## 💻 Example

```python
df.rename(
    index={2: 20},
    inplace=True
)
```

---

# 🔄 CHAPTER 10 — `reset_index()`

## 🔹 What?

`reset_index()` resets the DataFrame index.

## 🎯 Why?

After deleting or filtering rows, indexes may look like:

```text
0
3
7
10
```

We may want:

```text
0
1
2
3
```

## 📖 Definition

> `reset_index()` resets the DataFrame index to a new default integer index.

## 🧩 Syntax

```python
df.reset_index(
    drop=True,
    inplace=True
)
```

## 💻 Example

```python
df.reset_index(
    drop=True,
    inplace=True
)
```

## ⭐ `drop=True`

Without `drop=True`:

```python
df.reset_index()
```

The old index becomes a new column.

With:

```python
drop=True
```

The old index is removed.

## 📝 Summary

```text
reset_index()
      ↓
Reset index

drop=True
      ↓
Remove old index
```

---

# 🗑️ CHAPTER 11 — `drop()`

## 🔹 What?

`drop()` removes rows or columns.

## 🎯 Why?

To remove unwanted data.

## 📖 Definition

> `drop()` removes specified rows or columns from a DataFrame.

---

## 🗑️ Drop Column

### 🧩 Syntax

```python
df.drop(
    columns=["Name"],
    inplace=True
)
```

### 💻 Example

```python
df.drop(
    columns=["name", "age", "course"],
    inplace=True
)
```

---

# 🔢 CHAPTER 12 — `axis`

## 🔹 What?

`axis` tells Pandas whether we are working with rows or columns.

## 🎯 Why?

Pandas needs to know the direction of the operation.

## 🧩 Syntax

```python
axis=0
axis=1
```

## ⭐ Remember

```text
axis=0 → ROWS
axis=1 → COLUMNS
```

### Example

Drop rows:

```python
df.drop(
    index=[1, 2, 3],
    inplace=True
)
```

Drop columns:

```python
df.drop(
    ["Name", "Age"],
    axis=1,
    inplace=True
)
```

### ⭐ Recommended

Instead of:

```python
df.drop(
    ["Name", "Age"],
    axis=1
)
```

Use:

```python
df.drop(
    columns=["Name", "Age"]
)
```

It is easier to read.

---

# 📂 CHAPTER 13 — `read_excel()`

## 🔹 What?

`read_excel()` reads Excel files into a DataFrame.

## 🎯 Why?

Real-world datasets are often stored in Excel.

## 🧩 Syntax

```python
df = pd.read_excel("file.xlsx")
```

## 💻 Example

```python
df = pd.read_excel(
    "messy_dataset.xlsx"
)

print(df.head())
```

---

# 🔎 CHAPTER 14 — `isnull()`

## 🔹 What?

`isnull()` checks for missing values.

## 🎯 Why?

Missing data can cause problems during analysis and Machine Learning.

## 🧩 Syntax

```python
df.isnull()
```

## 💻 Example

```python
print(df.isnull())
```

Output:

```text
True
False
False
True
```

Meaning:

```text
True  → Missing
False → Not missing
```

---

# 🔢 CHAPTER 15 — `isnull().sum()`

## 🔹 What?

Counts missing values in each column.

## 🎯 Why?

To quickly understand how much data is missing.

## 🧩 Syntax

```python
df.isnull().sum()
```

## 💻 Example

```python
print(df.isnull().sum())
```

Example:

```text
Age           3
Salary        5
Rating        2
Department    4
```

---

# 🩹 CHAPTER 16 — `fillna()`

## 🔹 What?

`fillna()` replaces missing values.

## 🎯 Why?

To handle missing data before analysis.

## 📖 Definition

> `fillna()` replaces `NaN` or missing values with a specified value.

## 🧩 Syntax

```python
df["column"] = df["column"].fillna(value)
```

---

# 🔢 CHAPTER 17 — Fill Numeric Values with Median

## 💻 Example

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

Meaning:

```text
Age
 ↓
Find NaN
 ↓
Calculate median
 ↓
Replace NaN with median
```

---

# 📐 CHAPTER 18 — `median()`

## 🔹 What?

`median()` finds the middle value.

## 🎯 Why?

It is commonly used to replace missing numerical values.

## 🧩 Syntax

```python
df["Age"].median()
```

## 💻 Example

```python
age_median = df["Age"].median()

print(age_median)
```

For:

```text
10, 20, 30, 40, 50
```

Median:

```text
30
```

For:

```text
10, 20, 30, 40
```

Median:

```text
(20 + 30) / 2 = 25
```

---

# 💰 CHAPTER 19 — Fill Salary

```python
df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)
```

This replaces missing salary values with the median salary.

---

# ⭐ CHAPTER 20 — Fill Rating

```python
df["Rating"] = df["Rating"].fillna(
    df["Rating"].median()
)
```

---

# 🏢 CHAPTER 21 — Categorical Missing Values

For text/categorical columns, we can use:

```python
df["Department"] = df["Department"].fillna(
    "unknown"
)
```

## Why?

Because calculating a median for text doesn't make sense.

For example:

```text
Department
IT
HR
NaN
Sales
```

After:

```python
fillna("unknown")
```

we get:

```text
Department
IT
HR
unknown
Sales
```

---

# 🔢 CHAPTER 22 — `value_counts()`

## 🔹 What?

Counts how many times each unique value occurs.

## 🎯 Why?

Useful for understanding categorical data.

## 🧩 Syntax

```python
df["column"].value_counts()
```

## 💻 Example

```python
print(
    df["Department"].value_counts()
)
```

Example:

```text
IT        30
HR        20
Sales     15
Finance   10
unknown    5
```

---

# 📊 CHAPTER 23 — Histogram

## 🔹 What?

A histogram displays the distribution of numerical data.

## 🎯 Why?

It helps us understand:

* Distribution
* Frequency
* Concentration
* Shape of data

## 🧩 Syntax

```python
sns.histplot(
    x="Age",
    data=df,
    kde=True
)
```

## 💻 Example

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(
    x="Age",
    data=df,
    kde=True
)

plt.show()
```

---

# 📈 CHAPTER 24 — `kde=True`

## 🔹 What?

KDE means:

> **Kernel Density Estimate**

It adds a smooth curve showing the approximate distribution.

```python
sns.histplot(
    x="Age",
    data=df,
    kde=True
)
```

Remember:

```text
histplot() → kde=True ✅

boxplot() → kde=True ❌
```

---

# 📦 CHAPTER 25 — Boxplot

## 🔹 What?

A boxplot displays the distribution of numerical data.

## 🎯 Why?

It is especially useful for identifying possible **outliers**.

## 🧩 Syntax

```python
sns.boxplot(
    x="Rating",
    data=df
)
```

## 💻 Example

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(
    x="Rating",
    data=df
)

plt.show()
```

A boxplot helps show:

```text
Minimum
   ↓
Q1
   ↓
Median
   ↓
Q3
   ↓
Maximum
```

and possible outliers.

---

# 🎯 CHAPTER 26 — Select One Column

## 🧩 Syntax

```python
df["Name"]
```

## 💻 Example

```python
print(df["Name"])
```

---

# 🎯 CHAPTER 27 — Select Multiple Columns

## 🧩 Syntax

```python
df[["Name", "City"]]
```

## 💻 Example

```python
print(
    df[["Name", "City"]]
)
```

### 🧠 Remember

```text
One column:
df["Name"]

Multiple columns:
df[["Name", "City"]]
```

---

# 📍 CHAPTER 28 — `.loc`

## 🔹 What?

`.loc` performs **label-based selection**.

## 🎯 Why?

To select rows and columns using their labels/names.

## 🧩 Syntax

```python
df.loc[row_selection, column_selection]
```

---

## 💻 Example — One Row

```python
print(df.loc[2])
```

---

## 💻 Example — Multiple Rows

```python
print(df.loc[0:4])
```

Important:

`.loc` includes the ending label.

So:

```python
df.loc[0:4]
```

includes:

```text
0, 1, 2, 3, 4
```

---

# 🔢 CHAPTER 29 — `.loc` Step

```python
print(df.loc[0:8:2])
```

Output rows:

```text
0
2
4
6
8
```

Syntax:

```text
start : stop : step
```

---

# 🔢 CHAPTER 30 — `.iloc`

## 🔹 What?

`.iloc` performs **position-based selection**.

## 🎯 Why?

When you know the numerical position of rows/columns.

## 🧩 Syntax

```python
df.iloc[row_position, column_position]
```

---

## 💻 Example

```python
result = df.iloc[0:7, 0::2]

print(result)
```

Meaning:

```text
Rows:
0 to 6

Columns:
0, 2, 4, 6...
```

---

# 📍 `.loc` VS `.iloc`

| Feature   | `.loc`       | `.iloc`           |
| --------- | ------------ | ----------------- |
| Selection | Labels       | Positions         |
| Rows      | Labels       | Integer positions |
| Columns   | Names/labels | Integer positions |
| Example   | `df.loc[2]`  | `df.iloc[2]`      |

🧠 Easy memory:

```text
loc  → labels
iloc → integer positions
```

---

# ➕ CHAPTER 31 — Add a New Column

## 🔹 What?

You can create a new column using an existing column.

## 🧩 Syntax

```python
df["new_column"] = calculation
```

## 💻 Example

```python
df["Age1"] = df["Age"] + 20
```

If:

```text
Age = 25
```

then:

```text
Age1 = 45
```

---

# ⚡ CHAPTER 32 — `apply()`

## 🔹 What?

`apply()` applies a function to each value.

## 🎯 Why?

Useful when you need custom transformations.

## 🧩 Syntax

```python
df["new_column"] = df["column"].apply(function)
```

---

# 🏹 CHAPTER 33 — Lambda

## 🔹 What?

Lambda is a small anonymous function.

## 🧩 Syntax

```python
lambda argument: expression
```

## 💻 Example

```python
lambda x: x + 100
```

Meaning:

```text
Take x
 ↓
Add 100
 ↓
Return result
```

---

# 💰 CHAPTER 34 — `apply()` + Lambda

Your example:

```python
df["new_salary"] = df["Salary"].apply(
    lambda x: x + 100000
)
```

Suppose:

```text
Salary
500000
600000
700000
```

After:

```text
new_salary
600000
700000
800000
```

---

# 🧠 COMPLETE DATA CLEANING FLOW

```text
📂 Load Data
     ↓
🔍 Inspect Data
     ↓
📏 Check Shape
     ↓
🏷️ Check Columns
     ↓
🔢 Check Data Types
     ↓
❓ Check Missing Values
     ↓
📊 Visualize
     ↓
🩹 Handle Missing Values
     ↓
📦 Check Outliers
     ↓
🎯 Select Data
     ↓
✏️ Transform Data
     ↓
📈 Analyze Data
```

---

# 📝 COMPLETE SUMMARY

| Concept          | Meaning               |
| ---------------- | --------------------- |
| 🐼 Pandas        | Data analysis library |
| 📊 DataFrame     | Table of data         |
| `head()`         | First rows            |
| `shape`          | Rows + columns        |
| `columns`        | Column names          |
| `dtypes`         | Data types            |
| `rename()`       | Rename labels         |
| `reset_index()`  | Reset index           |
| `drop()`         | Remove data           |
| `axis=0`         | Rows                  |
| `axis=1`         | Columns               |
| `read_excel()`   | Read Excel            |
| `isnull()`       | Find missing values   |
| `fillna()`       | Fill missing values   |
| `median()`       | Middle value          |
| `value_counts()` | Frequency count       |
| `histplot()`     | Distribution          |
| `boxplot()`      | Distribution/outliers |
| `.loc`           | Label-based access    |
| `.iloc`          | Position-based access |
| `apply()`        | Apply function        |
| `lambda`         | Anonymous function    |

---

# 🎤 INTERVIEW QUESTIONS & ANSWERS

## ❓ 1. What is Pandas?

### ✅ Answer

Pandas is an open-source Python library used for data manipulation, data cleaning, and data analysis. It provides important data structures such as Series and DataFrame.

---

## ❓ 2. What is a DataFrame?

### ✅ Answer

A DataFrame is a two-dimensional labeled data structure containing rows and columns. It is similar to an Excel spreadsheet or a SQL table.

---

## ❓ 3. How do you create a DataFrame?

### ✅ Answer

```python
df = pd.DataFrame(data)
```

---

## ❓ 4. What is `head()`?

### ✅ Answer

`head()` displays the first five rows of a DataFrame by default.

```python
df.head()
```

---

## ❓ 5. What is `shape`?

### ✅ Answer

`shape` returns the number of rows and columns.

```python
df.shape
```

For example:

```text
(100, 5)
```

means 100 rows and 5 columns.

---

## ❓ 6. What does `dtypes` do?

### ✅ Answer

`dtypes` displays the data type of each column.

```python
df.dtypes
```

---

## ❓ 7. What is `rename()`?

### ✅ Answer

`rename()` is used to change row or column labels.

```python
df.rename(
    columns={"old": "new"},
    inplace=True
)
```

---

## ❓ 8. What is `inplace=True`?

### ✅ Answer

`inplace=True` modifies the original DataFrame directly instead of returning a separate DataFrame.

---

## ❓ 9. What is `reset_index()`?

### ✅ Answer

`reset_index()` resets the DataFrame index to the default integer index.

```python
df.reset_index(
    drop=True,
    inplace=True
)
```

---

## ❓ 10. What does `drop=True` mean?

### ✅ Answer

`drop=True` removes the old index instead of adding it as a new column.

---

## ❓ 11. What is `drop()`?

### ✅ Answer

`drop()` is used to remove rows or columns from a DataFrame.

---

## ❓ 12. What is `axis=0`?

### ✅ Answer

`axis=0` refers to rows.

---

## ❓ 13. What is `axis=1`?

### ✅ Answer

`axis=1` refers to columns.

---

## ❓ 14. What is `isnull()`?

### ✅ Answer

`isnull()` identifies missing values and returns `True` for missing values and `False` otherwise.

---

## ❓ 15. How do you count missing values?

### ✅ Answer

```python
df.isnull().sum()
```

---

## ❓ 16. What is `fillna()`?

### ✅ Answer

`fillna()` replaces missing or NaN values with a specified value.

Example:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

---

## ❓ 17. Why use median for missing numerical values?

### ✅ Answer

Median can be used to replace missing numerical values and is less affected by extreme values than the mean.

---

## ❓ 18. What is `value_counts()`?

### ✅ Answer

`value_counts()` counts the occurrences of each unique value.

```python
df["Department"].value_counts()
```

---

## ❓ 19. Difference between `.loc` and `.iloc`?

### ✅ Answer

`.loc` is label-based, while `.iloc` is position-based.

Example:

```python
df.loc[2]
```

uses the label.

```python
df.iloc[2]
```

uses the third row position.

---

## ❓ 20. Does `.loc[0:4]` include 4?

### ✅ Answer

Yes. `.loc` includes the ending label when using label slicing.

```python
df.loc[0:4]
```

includes:

```text
0, 1, 2, 3, 4
```

---

## ❓ 21. Does `.iloc[0:4]` include position 4?

### ✅ Answer

No.

```python
df.iloc[0:4]
```

selects:

```text
0, 1, 2, 3
```

---

## ❓ 22. How do you select multiple columns?

### ✅ Answer

Use a list of column names:

```python
df[["Name", "City"]]
```

---

## ❓ 23. What is `apply()`?

### ✅ Answer

`apply()` applies a function to values in a Series or DataFrame.

Example:

```python
df["Age2"] = df["Age"].apply(
    lambda x: x + 10
)
```

---

## ❓ 24. What is lambda?

### ✅ Answer

Lambda is a small anonymous function used for short operations.

Example:

```python
lambda x: x + 10
```

---

## ❓ 25. What is a histogram?

### ✅ Answer

A histogram is a graph used to visualize the distribution and frequency of numerical data.

Example:

```python
sns.histplot(
    x="Age",
    data=df,
    kde=True
)
```

---

## ❓ 26. What is a boxplot?

### ✅ Answer

A boxplot visualizes the distribution of numerical data and helps identify the median, quartiles, spread, and possible outliers.

Example:

```python
sns.boxplot(
    x="Rating",
    data=df
)
```

---

## ❓ 27. What is `kde=True`?

### ✅ Answer

`kde=True` adds a smooth density curve to a histogram.

```python
sns.histplot(
    x="Age",
    data=df,
    kde=True
)
```

---

## ❓ 28. How do you read an Excel file using Pandas?

### ✅ Answer

```python
df = pd.read_excel("file.xlsx")
```

---

## ❓ 29. How do you add a new column?

### ✅ Answer

```python
df["Age1"] = df["Age"] + 20
```

---

## ❓ 30. How do you remove a column?

### ✅ Answer

```python
df.drop(
    columns=["Name"],
    inplace=True
)
```

---

# 🎯 QUICK INTERVIEW REVISION

Before an interview, remember these:

```text
🐼 Pandas
    ↓
📊 DataFrame
    ↓
🔍 head()
    ↓
📏 shape
    ↓
🏷️ columns
    ↓
🔢 dtypes
    ↓
❓ isnull()
    ↓
🩹 fillna()
    ↓
📐 median()
    ↓
🔢 value_counts()
    ↓
🎯 loc
    ↓
🔢 iloc
    ↓
🗑️ drop()
    ↓
✏️ rename()
    ↓
🔄 reset_index()
    ↓
➕ Add columns
    ↓
⚡ apply()
    ↓
🏹 lambda
    ↓
📊 Visualization
```

# ⭐ GOLDEN RULES

```text
🧠 axis=0 → ROWS
🧠 axis=1 → COLUMNS

🧠 loc  → LABEL
🧠 iloc → POSITION

🧠 head() → FIRST ROWS
🧠 shape → SIZE
🧠 dtypes → DATA TYPES
🧠 isnull() → MISSING VALUES
🧠 fillna() → FILL MISSING VALUES
🧠 median() → MIDDLE VALUE
🧠 value_counts() → FREQUENCY
🧠 drop() → REMOVE
🧠 rename() → CHANGE NAME
🧠 reset_index() → RESET INDEX
🧠 apply() → APPLY FUNCTION
🧠 lambda → SMALL FUNCTION
```

# 🏆 FINAL INTERVIEW ANSWER

If the interviewer asks:

**"What have you learned in Pandas?"**

You can answer:

> "I have learned how to create and work with Pandas DataFrames, read Excel data, inspect datasets using `head()`, `shape`, `dtypes`, and `sample()`, select data using `.loc` and `.iloc`, rename and reset indexes, remove rows and columns using `drop()`, identify and handle missing values using `isnull()` and `fillna()`, calculate statistics such as median, analyze categorical data using `value_counts()`, visualize distributions using histograms and boxplots, and create or transform columns using `apply()` and lambda functions."
cd