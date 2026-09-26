# 🐼 PANDAS — GROUPBY, FILTERING, APPLY & OUTLIERS

## 📚 Topics Covered

1. 🎲 NumPy Random Data
2. 🔢 Random Seed
3. 📊 Creating Employee Data
4. 🗃️ DataFrame
5. ⚠️ Outliers
6. 🔍 `head()`
7. 📐 `dtypes`
8. 📏 `shape`
9. 📊 `describe()`
10. 📦 `groupby()`
11. 📈 `mean()`
12. ➕ `sum()`
13. 🔃 `sort_values()`
14. 🔝 `head(1)`
15. 🧮 Multiple Grouping
16. 🧰 `agg()`
17. 🏷️ Custom Buckets
18. ⚡ `apply()`
19. 🏹 Lambda
20. 🔎 Boolean Filtering
21. 🔗 `&`
22. 📍 `.loc`
23. 🔢 Numeric Columns
24. 🎤 Interview Questions

---

# 🎲 CHAPTER 1 — `np.random.seed()`

## 🔹 What?

`np.random.seed()` controls the random number generation.

## 🎯 Why?

Your dataset contains randomly generated values.

Without a seed, the random values can change every time the program runs.

With:

```python
np.random.seed(42)
```

you get the same random values every time the code is executed.

## 📖 Definition

> `np.random.seed()` initializes NumPy's random number generator so that random results can be reproduced.

## 🧩 Syntax

```python
np.random.seed(number)
```

## 💻 Example

```python
import numpy as np

np.random.seed(42)

print(np.random.randint(1, 10, 5))
```

Running the same code again produces the same sequence.

## 📝 Summary

```text
🎲 Random numbers
       ↓
np.random.seed(42)
       ↓
🔒 Reproducible results
```

---

# 🔢 CHAPTER 2 — `np.random.randint()`

## 🔹 What?

Generates random integers.

## 🎯 Why?

Useful for creating sample datasets and simulations.

## 🧩 Syntax

```python
np.random.randint(start, stop, size)
```

⚠️ `stop` is excluded.

## 💻 Example

```python
np.random.randint(21, 56, 100)
```

This generates 100 random integers from:

```text
21 → 55
```

Your employee dataset uses this for age, experience, salary, projects, and training hours.

---

# 📊 CHAPTER 3 — Creating Employee Data

Your code creates a dataset containing **100 employees**:

```python
n = 100
```

The dataset contains fields such as:

```text
employee_id
age
experience_years
salary
working_hours
projects_completed
performance_score
training_hours
monthly_sales
satisfaction_score
department
job_role
country
employment_type
education_level
gender
```

These fields are generated using NumPy random functions and categorical choices.

---

# 🐼 CHAPTER 4 — `pd.DataFrame()`

## 🔹 What?

Creates a Pandas DataFrame from structured data.

## 🎯 Why?

A DataFrame allows us to analyze the employee dataset using Pandas.

## 🧩 Syntax

```python
df = pd.DataFrame(data)
```

## 💻 Example

```python
df = pd.DataFrame(data)

print(df.head())
```

Your uploaded code creates the employee DataFrame this way.

---

# ⚠️ CHAPTER 5 — OUTLIERS

## 🔹 What?

An outlier is a value that is unusually different from most other values.

Example:

```text
Normal salaries:

30000
45000
50000
60000
70000

Outlier:

350000
```

## 🎯 Why?

Outliers can significantly affect:

* Mean
* Standard deviation
* Data visualization
* Statistical analysis
* Machine Learning models

---

## 💻 Your Dataset

Your code intentionally creates outliers.

For example, age normally ranges from the generated values, but these values are inserted:

```python
df.loc[[5, 25, 75], "age"] = [70, 75, 80]
```

Similarly, unusually high salary values are inserted:

```python
df.loc[[15, 50, 85], "salary"] = [
    250000,
    300000,
    350000
]
```

Your file intentionally adds outliers to several numerical columns.

---

# 🔍 CHAPTER 6 — `head()`

## 🔹 What?

Displays the first rows.

## 🧩 Syntax

```python
df.head()
```

## 💻 Example

```python
print(df.head())
```

Your code uses this to inspect the generated employee dataset.

---

# 🔢 CHAPTER 7 — `dtypes`

## 🔹 What?

Displays the data type of every column.

## 🧩 Syntax

```python
df.dtypes
```

## 💻 Example

```python
print(df.dtypes)
```

Useful for checking whether columns are:

```text
int
float
object
bool
datetime
```

Your code prints the data types after creating the DataFrame.

---

# 📏 CHAPTER 8 — `shape`

## 🔹 What?

Returns:

```text
(rows, columns)
```

## 🧩 Syntax

```python
df.shape
```

## 💻 Example

```python
print(df.shape)
```

Since your dataset starts with:

```python
n = 100
```

the DataFrame has 100 rows initially.

---

# 📊 CHAPTER 9 — `describe()`

## 🔹 What?

`describe()` generates descriptive statistics for numerical columns.

## 🎯 Why?

It gives a quick statistical summary.

## 🧩 Syntax

```python
df.describe()
```

## 💻 Example

```python
print(df.describe())
```

It commonly shows:

```text
count
mean
std
min
25%
50%
75%
max
```

Your code uses `describe()` to inspect the employee numerical data.

---

# 📦 CHAPTER 10 — `groupby()`

## 🔹 What?

`groupby()` divides data into groups based on one or more columns.

## 🎯 Why?

It is one of the most important Pandas tools for data analysis.

For example:

> What is the average salary for each department?

We can use:

```python
df.groupby("department")["salary"].mean()
```

---

## 📖 Definition

> `groupby()` groups rows that have the same value in one or more columns so that aggregate calculations can be performed on each group.

---

# 🧩 CHAPTER 11 — Basic `groupby()` Syntax

```python
df.groupby("column")["value_column"].operation()
```

Example:

```python
df.groupby("department")["salary"].mean()
```

Meaning:

```text
department
    ↓
Create groups

salary
    ↓
Select salary

mean()
    ↓
Calculate average
```

---

# 💰 CHAPTER 12 — Salary by Department

```python
print(
    df.groupby("department")["salary"].mean()
)
```

This answers:

> What is the average salary in each department?

Your code performs this analysis.

---

# 🌍 CHAPTER 13 — Salary by Country

```python
print(
    df.groupby("country")["salary"].mean()
)
```

Meaning:

```text
Country
   ↓
Group employees
   ↓
Salary
   ↓
Mean
```

Your code uses this to calculate average salary by country.

---

# 🎓 CHAPTER 14 — Salary by Education

```python
print(
    df.groupby("education_level")["salary"].mean()
)
```

This calculates average salary for each education level.

Your code performs this grouping.

---

# 👤 CHAPTER 15 — Salary by Gender

```python
print(
    df.groupby("gender")["salary"].mean()
)
```

This calculates the average salary within each gender category in the generated dataset.

---

# 💼 CHAPTER 16 — Salary by Job Role

```python
print(
    df.groupby("job_role")["salary"].mean()
)
```

This calculates average salary for each job role.

---

# 📈 CHAPTER 17 — `mean()`

## 🔹 What?

`mean()` calculates the average.

## 🧩 Formula

```text
Mean = Sum of values / Number of values
```

## 💻 Example

```python
df.groupby("department")["salary"].mean()
```

---

# ➕ CHAPTER 18 — `sum()`

## 🔹 What?

`sum()` calculates the total.

## 💻 Example

```python
df.groupby("country")["salary"].sum()
```

This gives the total salary for each country.

Your code uses this operation.

---

# 🔗 CHAPTER 19 — GROUP BY MULTIPLE COLUMNS

## 🔹 What?

You can group by more than one column.

## 🧩 Syntax

```python
df.groupby(
    ["column1", "column2"]
)["value"].sum()
```

## 💻 Example

```python
df.groupby(
    ["country", "department"]
)["salary"].sum()
```

This answers:

> What is the total salary for each country + department combination?

Your code uses this exact analysis.

---

# 🔃 CHAPTER 20 — `sort_values()`

## 🔹 What?

Sorts values.

## 🎯 Why?

Useful when you want:

* Highest values
* Lowest values
* Ranking
* Top performers

## 🧩 Syntax

```python
df.sort_values(
    ascending=False
)
```

For a Series:

```python
series.sort_values(
    ascending=False
)
```

---

## 💻 Example

```python
df.groupby(
    ["country", "department"]
)["salary"].sum().sort_values(
    ascending=False
)
```

This sorts total salaries from highest to lowest.

Your code uses this pattern.

---

# 🔝 CHAPTER 21 — `head(1)`

## 🔹 What?

Returns the first row.

When data has been sorted descending, `head(1)` gives the highest value.

## 💻 Example

```python
df.groupby(
    "department"
)["experience_years"].mean().sort_values(
    ascending=False
).head(1)
```

Your code uses this to obtain the department with the highest average experience.

---

# 🧮 CHAPTER 22 — `agg()`

## 🔹 What?

`agg()` allows you to perform multiple aggregate calculations.

## 🎯 Why?

Instead of calculating one statistic at a time, you can calculate several statistics together.

## 🧩 Syntax

```python
df.groupby("group_column").agg({
    "column1": "sum",
    "column2": "mean"
})
```

## 💻 Example

```python
df.groupby(
    ["country", "department"]
).agg({
    "salary": "sum",
    "experience_years": "mean"
})
```

Meaning:

```text
Country + Department
        ↓
Total Salary
        +
Average Experience
```

Your code uses this exact pattern.

---

# 🏷️ CHAPTER 23 — CUSTOM BUCKETS

## 🔹 What?

A bucket converts numerical values into categories.

For example:

```text
Age >= 60       → high aged
Age >= 40       → moderate age
Otherwise       → Below age
```

## 🎯 Why?

Categorical labels can make numerical data easier to analyze.

---

# 🧩 CHAPTER 24 — Custom Function

Your function:

```python
def buckets(x):
    if x >= 60:
        return "high aged"
    elif x >= 40:
        return "moderate age"
    else:
        return "Below age"
```

## Step-by-step

```text
x >= 60
   ↓
high aged

x >= 40
   ↓
moderate age

otherwise
   ↓
Below age
```

Your uploaded code defines this function and applies it to the `age` column.

---

# ⚡ CHAPTER 25 — `apply()`

## 🔹 What?

`apply()` applies a function to each value.

## 🧩 Syntax

```python
df["new_column"] = df["column"].apply(function)
```

## 💻 Example

```python
df["age_bucket"] = df["age"].apply(buckets)
```

For every age, the `buckets()` function is called.

Your code creates the `age_bucket` column this way.

---

# 🏹 CHAPTER 26 — `lambda`

## 🔹 What?

A lambda is a small anonymous function.

## 🧩 Syntax

```python
lambda argument: expression
```

## 💻 Example

Your code performs the same bucket operation using lambda:

```python
df["age_bucket"] = df["age"].apply(
    lambda x:
        "high aged"
        if x >= 60
        else "moderate age"
        if x >= 40
        else "Below age"
)
```

This is an alternative to defining a separate `buckets()` function.

---

# 🔎 CHAPTER 27 — BOOLEAN FILTERING

## 🔹 What?

Boolean filtering selects rows that satisfy a condition.

## 🎯 Why?

To answer questions such as:

> Find employees whose age is 49.

## 🧩 Syntax

```python
df[df["column"] == value]
```

## 💻 Example

```python
result = df[df["age"] == 49]

print(result)
```

---

# 🎯 CHAPTER 28 — FILTER WITH TWO CONDITIONS

Your code:

```python
df[
    (df["age"] == 49) &
    (df["experience_years"] > 8)
]
```

Meaning:

```text
Age = 49
     AND
Experience > 8
```

Both conditions must be `True`.

Your file uses this pattern.

---

# 🔗 CHAPTER 29 — `&`

## 🔹 What?

`&` means **AND** when combining Pandas boolean conditions.

## 🧩 Syntax

```python
(condition1) & (condition2)
```

## 💻 Example

```python
df[
    (df["age"] == 50) &
    (df["experience_years"] > 8)
]
```

---

# ⚠️ Important Rule

Always put each condition inside parentheses:

```python
(df["age"] == 50) & (df["experience_years"] > 8)
```

Don't write:

```python
df["age"] == 50 & df["experience_years"] > 8
```

The parentheses prevent operator-precedence problems.

---

# 🌎 CHAPTER 30 — THREE CONDITIONS

Your code:

```python
result = df[
    (df["age"] == 50) &
    (df["experience_years"] > 8) &
    (df["country"] == "USA")
]
```

Meaning:

```text
Age = 50
   AND
Experience > 8
   AND
Country = USA
```

All three conditions must be true.

---

# 📍 CHAPTER 31 — `.loc` AFTER FILTERING

You created:

```python
res = result.loc[
    :,
    ["age", "experience_years", "country"]
]
```

## What does `:` mean?

```text
:
↓
All rows
```

So:

```python
result.loc[
    :,
    ["age", "experience_years", "country"]
]
```

means:

> Select all rows and only these three columns.

---

# 🔢 CHAPTER 32 — `select_dtypes()`

## 🔹 What?

`select_dtypes()` selects columns based on their data type.

## 🎯 Why?

Sometimes we want only numerical columns for:

* Correlation
* Statistics
* Machine Learning
* Visualization
* Mathematical calculations

## 🧩 Syntax

```python
df.select_dtypes(
    include="number"
)
```

## 💻 Example

```python
print(
    df.select_dtypes(
        include="number"
    ).columns
)
```

Your code uses this to display all numerical column names.

---

# 📊 CHAPTER 33 — Numeric Columns

Your DataFrame contains numerical columns such as:

```text
employee_id
age
experience_years
salary
working_hours
projects_completed
performance_score
training_hours
monthly_sales
satisfaction_score
```

Using:

```python
df.select_dtypes(include="number")
```

helps select numerical data without manually listing every column.

---

# 🧠 COMPLETE GROUPBY FLOW

Remember this pattern:

```text
                 GROUPBY
                    ↓
             Choose groups
                    ↓
            Choose column
                    ↓
          Choose calculation
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
     mean()       sum()        agg()
```

Example:

```python
df.groupby("department")["salary"].mean()
```

---

# 🧠 COMPLETE FILTERING FLOW

```text
              FILTERING
                  ↓
            Create condition
                  ↓
             True / False
                  ↓
           Select matching rows
```

Example:

```python
df[
    (df["age"] == 49) &
    (df["experience_years"] > 8)
]
```

---

# 🧠 COMPLETE TRANSFORMATION FLOW

```text
             COLUMN
                ↓
             apply()
                ↓
        function / lambda
                ↓
          NEW COLUMN
```

Example:

```python
df["age_bucket"] = df["age"].apply(
    lambda x: "high aged"
    if x >= 60
    else "moderate age"
    if x >= 40
    else "Below age"
)
```

---

# 📋 IMPORTANT SYNTAX CHEAT SHEET

## 🎲 Random

```python
np.random.seed(42)

np.random.randint(1, 10, 5)

np.random.normal(8, 1, 100)

np.random.uniform(1, 10, 100)

np.random.choice(
    ["IT", "HR", "Sales"],
    100
)
```

---

## 🔍 Inspect

```python
df.head()

df.dtypes

df.shape

df.describe()

df.columns
```

---

## 📦 GroupBy

```python
df.groupby("department")["salary"].mean()
```

```python
df.groupby("country")["salary"].sum()
```

```python
df.groupby(
    ["country", "department"]
)["salary"].sum()
```

---

## 🔃 Sort

```python
df.sort_values(
    ascending=False
)
```

---

## 🧮 Aggregate

```python
df.groupby("department").agg({
    "salary": "sum",
    "experience_years": "mean"
})
```

---

## ⚡ Apply

```python
df["new_column"] = df["column"].apply(function)
```

---

## 🏹 Lambda

```python
lambda x: x + 10
```

---

## 🔎 Filtering

```python
df[df["age"] == 49]
```

```python
df[
    (df["age"] == 49) &
    (df["experience_years"] > 8)
]
```

---

## 📍 Select Columns

```python
df.loc[:, ["age", "salary"]]
```

---

## 🔢 Numeric Columns

```python
df.select_dtypes(
    include="number"
)
```

---

# 📝 SUMMARY

| Concept                  | Purpose                   |
| ------------------------ | ------------------------- |
| 🎲 `np.random.seed()`    | Reproducible random data  |
| 🔢 `np.random.randint()` | Random integers           |
| 🎯 `np.random.choice()`  | Random categorical values |
| 🐼 `DataFrame()`         | Create DataFrame          |
| 🔍 `head()`              | First rows                |
| 📐 `dtypes`              | Data types                |
| 📏 `shape`               | Size                      |
| 📊 `describe()`          | Statistics                |
| 📦 `groupby()`           | Group data                |
| 📈 `mean()`              | Average                   |
| ➕ `sum()`                | Total                     |
| 🔃 `sort_values()`       | Sort data                 |
| 🔝 `head(1)`             | First row after sorting   |
| 🧮 `agg()`               | Multiple aggregations     |
| ⚡ `apply()`              | Apply function            |
| 🏹 `lambda`              | Anonymous function        |
| 🔎 Boolean filtering     | Filter rows               |
| 🔗 `&`                   | AND condition             |
| 📍 `.loc`                | Label-based selection     |
| 🔢 `select_dtypes()`     | Select by data type       |
| ⚠️ Outlier               | Unusually different value |

---

# 🎤 INTERVIEW QUESTIONS & ANSWERS

## ❓ 1. What is `groupby()` in Pandas?

### ✅ Answer

`groupby()` is used to divide a DataFrame into groups based on one or more columns and then perform aggregate operations such as `mean()`, `sum()`, `count()`, `min()`, and `max()`.

Example:

```python
df.groupby("department")["salary"].mean()
```

---

## ❓ 2. Why do we use `groupby()`?

### ✅ Answer

We use `groupby()` to perform category-wise analysis.

For example:

```text
Average salary by department
Total sales by country
Average experience by job role
```

---

## ❓ 3. What is aggregation?

### ✅ Answer

Aggregation means summarizing multiple values into a single value.

Examples:

```python
mean()
sum()
min()
max()
count()
```

---

## ❓ 4. Difference between `mean()` and `sum()`?

### ✅ Answer

`mean()` calculates the average.

`sum()` calculates the total.

```python
df.groupby("department")["salary"].mean()
```

calculates average salary.

```python
df.groupby("department")["salary"].sum()
```

calculates total salary.

---

## ❓ 5. What is `agg()`?

### ✅ Answer

`agg()` allows us to perform multiple aggregate calculations on one or more columns.

Example:

```python
df.groupby("department").agg({
    "salary": "sum",
    "experience_years": "mean"
})
```

---

## ❓ 6. What is `sort_values()`?

### ✅ Answer

`sort_values()` sorts data based on values.

Example:

```python
df.sort_values(
    "salary",
    ascending=False
)
```

---

## ❓ 7. What does `ascending=False` mean?

### ✅ Answer

It sorts values from **highest to lowest**.

```text
100
80
60
40
```

`ascending=True` sorts from lowest to highest.

---

## ❓ 8. What is an outlier?

### ✅ Answer

An outlier is a value that is significantly different from the general pattern of the dataset.

Example:

```text
50000
55000
60000
58000
350000 ← possible outlier
```

---

## ❓ 9. What is `apply()`?

### ✅ Answer

`apply()` applies a function to each value in a Series or DataFrame.

Example:

```python
df["age_bucket"] = df["age"].apply(buckets)
```

---

## ❓ 10. What is lambda?

### ✅ Answer

A lambda is a small anonymous function.

Example:

```python
lambda x: x + 10
```

---

## ❓ 11. Difference between a normal function and lambda?

### ✅ Answer

A normal function is usually defined with `def` and can contain multiple statements.

```python
def add_ten(x):
    return x + 10
```

Lambda is a compact one-expression function:

```python
lambda x: x + 10
```

---

## ❓ 12. How do you filter rows in Pandas?

### ✅ Answer

Use a Boolean condition.

```python
df[df["age"] > 40]
```

---

## ❓ 13. How do you apply two conditions?

### ✅ Answer

Use `&` for AND.

```python
df[
    (df["age"] > 40) &
    (df["salary"] > 50000)
]
```

---

## ❓ 14. Why are parentheses required?

### ✅ Answer

Each Boolean condition should be enclosed in parentheses so Pandas evaluates the conditions correctly when using operators such as `&` and `|`.

---

## ❓ 15. What does `&` mean?

### ✅ Answer

`&` represents **AND** between Pandas Boolean conditions.

```python
(condition1) & (condition2)
```

Both conditions must be `True`.

---

## ❓ 16. How do you filter using three conditions?

### ✅ Answer

```python
df[
    (df["age"] > 40) &
    (df["experience_years"] > 8) &
    (df["country"] == "USA")
]
```

---

## ❓ 17. What does `df.loc[:, ["age", "salary"]]` mean?

### ✅ Answer

It selects:

```text
: → all rows

["age", "salary"]
→ only age and salary columns
```

---

## ❓ 18. What is `select_dtypes()`?

### ✅ Answer

`select_dtypes()` selects DataFrame columns based on their data types.

Example:

```python
df.select_dtypes(
    include="number"
)
```

selects numerical columns.

---

## ❓ 19. Why use `select_dtypes(include="number")`?

### ✅ Answer

It is useful when we want to perform numerical analysis without manually specifying every numerical column.

---

## ❓ 20. How do you find the department with the highest average experience?

### ✅ Answer

```python
result = (
    df.groupby("department")["experience_years"]
      .mean()
      .sort_values(ascending=False)
      .head(1)
)
```

This follows:

```text
groupby
   ↓
mean
   ↓
sort descending
   ↓
head(1)
```

---

# 🎯 INTERVIEW QUICK REVISION

```text
🐼 Pandas
   ↓
📦 groupby()
   ↓
📈 mean()
   ↓
➕ sum()
   ↓
🧮 agg()
   ↓
🔃 sort_values()
   ↓
🔝 head(1)
   ↓
⚡ apply()
   ↓
🏹 lambda
   ↓
🔎 filtering
   ↓
🔗 &
   ↓
📍 loc
   ↓
🔢 select_dtypes()
   ↓
⚠️ outliers
```

# ⭐ GOLDEN RULES

```text
📦 groupby()
→ Group data

📈 mean()
→ Average

➕ sum()
→ Total

🧮 agg()
→ Multiple calculations

🔃 sort_values()
→ Sort

⚡ apply()
→ Apply function

🏹 lambda
→ Small anonymous function

🔎 df[condition]
→ Filter rows

🔗 &
→ AND

📍 loc
→ Label-based selection

🔢 iloc
→ Position-based selection

⚠️ Outlier
→ Unusually different value

🔢 select_dtypes()
→ Select columns by data type
```

# 🏆 ONE REAL-WORLD EXAMPLE

Suppose an interviewer asks:

> "Find the top department based on average salary."

Think step-by-step:

```text
1️⃣ Group by department
        ↓
2️⃣ Select salary
        ↓
3️⃣ Calculate mean
        ↓
4️⃣ Sort descending
        ↓
5️⃣ Take first result
```

Code:

```python
result = (
    df.groupby("department")["salary"]
      .mean()
      .sort_values(ascending=False)
      .head(1)
)

print(result)
```

This pattern is extremely important for Pandas interviews.
c