# 🐼 Pandas — Loading Data & Data Operations  
## 📚 Complete Combined Notes from All Your Screenshots

I combined the concepts shown in **all the screenshots** into one clean, beginner-friendly chapter.

The main topics are:

1. `read_csv()`
2. Large CSV datasets
3. `shape`
4. `info()`
5. `describe()`
6. `describe(include="object")`
7. `head()`
8. `dtypes`
9. `astype()`
10. `pd.to_numeric()`
11. `pd.to_datetime()`
12. `sample()`
13. `value_counts()`
14. Data cleaning with `replace()`
15. Standardizing city names
16. Numeric vs categorical vs date columns
17. Complete data-cleaning workflow

---

# 📁 1. Import Pandas

```python
# ============================================================
# PANDAS - LOADING DATA AND OPERATIONS
# ============================================================

import pandas as pd
```

### 🧠 Meaning

`pandas` is used for:

- Reading datasets
- Cleaning data
- Analyzing data
- Changing data types
- Finding duplicate/unique values
- Filtering data
- Data transformation

---

# 📂 2. Load CSV File

```python
df = pd.read_csv(
    r"C:\Users\DELL\Downloads\large_sales_database_dataset_500k.csv"
)

print(df)
```

### 🧠 `pd.read_csv()`

It reads a CSV file and converts it into a **DataFrame**.

```text
CSV File
   ↓
pd.read_csv()
   ↓
DataFrame
```

---

# 📊 3. Check Dataset Shape

```python
print(df.shape)
```

Example:

```text
(500000, 14)
```

### 🧠 Meaning

```text
(500000, 14)
     ↓      ↓
   rows   columns
```

So:

- `500000` → number of rows
- `14` → number of columns

### Access separately

```python
# Number of rows
print(df.shape[0])

# Number of columns
print(df.shape[1])
```

---

# 🔍 4. `df.head()`

```python
print(df.head())
```

By default:

```python
df.head()
```

shows the **first 5 rows**.

You can specify the number:

```python
df.head(10)
```

This displays the first 10 rows.

### Example

```text
   order_id  order_date  customer_id gender       city
0    101568  2026-04-19         8238   Male     Jaipur
1    101569  2026-04-24         8515 Female  Bangalore
2    101570  2026-04-29         7747   Male     Mumbai
3    101571  2026-04-30         9734 Female Bhubaneswar
4    101572  2026-04-05         7646   Male      Delhi
```

### 🎯 Why use `head()`?

When a dataset has:

```text
500,000 rows
```

you don't want to print all 500,000 rows.

Instead:

```python
df.head()
```

quickly checks the first few records.

---

# 🔚 5. `df.tail()`

The opposite of `head()` is `tail()`.

```python
df.tail()
```

Shows the last 5 rows.

```python
df.tail(10)
```

Shows the last 10 rows.

---

# 🧾 6. `df.info()`

One of the **most important commands** for data analysis.

```python
df.info()
```

Example from your screenshot:

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):

#   Column          Non-Null Count   Dtype
0   order_id        1000 non-null    int64
1   order_date      1000 non-null    datetime64[ns]
2   customer_id     1000 non-null    int64
3   gender          1000 non-null    object
4   city            1000 non-null    object
5   region          1000 non-null    object
6   category        1000 non-null    object
7   product         1000 non-null    object
8   quantity        1000 non-null    int64
9   unit_price      1000 non-null    float64
10  discount_pct    1000 non-null    int64
11  sales_amount    1000 non-null    float64
```

---

# 🧠 Understanding `info()`

`df.info()` tells us:

| Information | Meaning |
|---|---|
| DataFrame | Pandas DataFrame |
| RangeIndex | Row/index information |
| Entries | Number of rows |
| Data columns | Number of columns |
| Column | Column name |
| Non-Null Count | Number of non-empty values |
| Dtype | Data type |
| Memory usage | RAM used by DataFrame |

---

# 🧮 7. Understanding Dtypes

Your dataset contains types such as:

```text
int64
float64
object
datetime64[ns]
```

### `int64`

Integer values:

```text
1
10
50
100
```

Example:

```python
customer_id
quantity
discount_pct
```

---

### `float64`

Decimal values:

```text
10.5
99.99
26187.18
```

Example:

```python
unit_price
sales_amount
```

---

### `object`

Usually text/string data.

Example:

```text
Male
Female
Hyderabad
Delhi
Electronics
Smartphone
```

---

### `datetime64[ns]`

Date/time values.

Example:

```text
2026-04-19
2026-04-24
2026-04-30
```

---

# 🔎 8. `df.dtypes`

```python
print(df.dtypes)
```

This displays the datatype of **every column**.

Example:

```text
order_id          int64
order_date       datetime64[ns]
customer_id       int64
gender           object
city             object
region           object
category         object
product          object
quantity          int64
unit_price       float64
discount_pct      int64
sales_amount     float64
```

---

# 📊 9. `df.describe()`

```python
print(df.describe())
```

`describe()` gives a **statistical summary of numerical columns**.

Example:

```text
             order_id  customer_id  quantity    unit_price
count     1000.000000  1000.000000  1000.0000
mean    102067.500000  8498.083000     3.0580
min     101568.000000  7007.000000     1.0000
25%     101817.750000  7771.750000     2.0000
50%     102067.500000  8483.500000     3.0000
75%     102317.250000  9243.750000     4.0000
max     102567.000000  9998.000000     5.0000
std        288.819436   868.065367     1.4369
```

---

# 🧠 10. Understand `describe()`

There are important statistical values.

### `count`

Number of non-null values.

```text
count = 1000
```

Means there are 1000 valid values.

---

### `mean`

Average.

Formula:

```text
mean = sum of values / number of values
```

Example:

```text
10 + 20 + 30
------------
     3

= 20
```

---

### `min`

Smallest value.

```text
10
20
30

min = 10
```

---

### `25%`

First quartile.

Also called:

```text
Q1
```

---

### `50%`

Median.

Also called:

```text
Q2
```

---

### `75%`

Third quartile.

Also called:

```text
Q3
```

---

### `max`

Largest value.

---

### `std`

Standard deviation.

It measures how spread out the values are.

For now, remember:

```text
small std → values are relatively close
large std → values are more spread out
```

---

# 📝 11. `describe()` Does Not Normally Show Object Columns

If you run:

```python
df.describe()
```

Pandas normally summarizes numerical columns.

But your dataset also contains:

```text
gender
city
region
category
product
```

These are categorical/object columns.

To analyze them:

```python
df.describe(include="object")
```

---

# 📊 12. `describe(include="object")`

```python
print(
    df.describe(
        include="object"
    )
)
```

Example from your screenshot:

```text
        gender       city       region       category      product
count   1000         1000       1000         1000          1000
unique     2           10          4            5            25
top     Female    Hyderabad      South  Electronics   Smartphone
freq     511         117         428          221            49
```

---

# 🧠 13. Understanding `unique`

Example:

```text
gender unique = 2
```

Because:

```text
Male
Female
```

There are 2 unique values.

For city:

```text
unique = 10
```

means there are 10 different city values.

---

# 🧠 14. Understanding `top`

`top` means the **most frequently occurring value**.

Example:

```text
gender → Female
```

means `Female` occurs more frequently than `Male`.

---

# 🧠 15. Understanding `freq`

`freq` means the number of times the `top` value appears.

Example:

```text
gender

top  = Female
freq = 511
```

So:

```text
Female appears 511 times
```

---

# 🔢 16. `value_counts()`

This is another **very important Pandas operation**.

```python
df["city"].value_counts()
```

Example:

```text
Hyderabad     18
delhi         12
Bangalore     12
Hyderabad     12
Delhi         12
mumbai        10
Mumbai         9
hyderabad      8
bangalore      7
```

### 🧠 Meaning

`value_counts()` counts how many times each value occurs.

---

# 🎯 17. Simple Example

Suppose:

```python
city = [
    "Hyderabad",
    "Delhi",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Hyderabad"
]
```

Then:

```python
pd.Series(city).value_counts()
```

Result:

```text
Hyderabad    3
Delhi        2
Mumbai       1
```

---

# ⚠️ 18. Problem in Your Dataset

Look carefully at your screenshot:

```text
Hyderabad
hyderabad
Hyderabad

Delhi
delhi

Mumbai
mumbai

Bangalore
bangalore
```

Pandas considers these **different values** because strings are case-sensitive.

For example:

```text
"Hyderabad"
"hyderabad"
"HYDERABAD"
```

are three different strings.

This creates a **data-cleaning problem**.

---

# 🧹 19. Clean City Names Using `replace()`

Your screenshot uses a dictionary:

```python
d = {
    "Hyderabad": "Hyd",
    "Hyderabad": "Hyd",
    "hyderabad": "Hyd"
}

df["city"] = df["city"].replace(d)
```

The idea is correct, but the duplicate `"Hyderabad"` key is unnecessary.

A cleaner version is:

```python
d = {
    "Hyderabad": "Hyd",
    "hyderabad": "Hyd"
}

df["city"] = df["city"].replace(d)
```

Now:

```text
Hyderabad → Hyd
hyderabad → Hyd
```

---

# ⭐ 20. Better Method — `str.lower()`

For real-world data cleaning, an even better approach is often to normalize the case first.

```python
df["city"] = df["city"].str.lower()
```

Now:

```text
Hyderabad → hyderabad
HYDERABAD → hyderabad
hyderabad → hyderabad
```

Then all variations become the same.

You can also use:

```python
df["city"] = df["city"].str.title()
```

Result:

```text
hyderabad → Hyderabad
delhi → Delhi
mumbai → Mumbai
bangalore → Bangalore
```

### ⭐ Recommended

```python
df["city"] = df["city"].str.strip().str.title()
```

This handles:

1. Extra spaces
2. Different capitalization

Example:

```text
" hyderabad "
"HYDERABAD"
"hyderabad"
```

becomes:

```text
"Hyderabad"
```

---

# 🔄 21. Check `value_counts()` Again

Before cleaning:

```python
df["city"].value_counts()
```

You may see:

```text
Hyderabad    18
hyderabad     8
Delhi        12
delhi        12
Mumbai        9
mumbai       10
```

After:

```python
df["city"] = (
    df["city"]
    .str.strip()
    .str.title()
)
```

Then:

```python
df["city"].value_counts()
```

You might get:

```text
Hyderabad    38
Delhi        24
Bangalore    19
Mumbai       19
```

The exact counts depend on the dataset.

---

# 🔢 22. `astype()`

Your screenshots demonstrate:

```python
df["experience"].astype("int32")
```

This converts a column into another datatype.

### Example

```python
df["experience"] = df["experience"].astype("int32")
```

Before:

```text
experience    object
```

After:

```text
experience    int32
```

---

# 🧠 23. Why Use `astype()`?

Suppose:

```text
experience
1
1
6
14
5
```

but Pandas says:

```text
dtype: object
```

This means Pandas is treating the values as text/object rather than integer.

We can convert them:

```python
df["experience"] = (
    df["experience"]
    .astype("int32")
)
```

Now:

```text
experience    int32
```

---

# ⚠️ 24. Important Difference: `astype()` vs `to_numeric()`

### `astype()`

```python
df["experience"].astype("int32")
```

Works when the values are already clean and convertible.

Example:

```text
1
2
5
10
```

---

### `pd.to_numeric()`

Better when the data may contain invalid values.

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

If the column contains:

```text
50000
60000
unknown
70000
```

then:

```text
50000
60000
NaN
70000
```

`errors="coerce"` converts invalid values into `NaN`.

---

# 🧮 25. `pd.to_numeric()`

Syntax:

```python
pd.to_numeric(
    column,
    errors="coerce"
)
```

Example:

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

Then check:

```python
df.dtypes
```

You should get something like:

```text
salary    int64
```

or:

```text
salary    float64
```

depending on missing values.

---

# ⚠️ 26. Why `errors="coerce"`?

Suppose:

```text
salary
50000
60000
70000
unknown
80000
```

Without `errors="coerce"`:

```python
pd.to_numeric(df["salary"])
```

can produce an error because:

```text
unknown
```

is not a number.

With:

```python
errors="coerce"
```

Pandas converts invalid values to:

```text
NaN
```

Result:

```text
50000
60000
70000
NaN
80000
```

---

# 📅 27. `pd.to_datetime()`

Your screenshot contains:

```python
df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)
```

This converts a column into a proper datetime datatype.

---

# 🧠 28. Why Convert Dates?

Your dataset contains different formats:

```text
03/20/2024
2024/04/25
15-02-2024
2024-01-15
May 10, 2024
```

These are all dates, but they are written differently.

Pandas should convert them into one consistent datetime representation.

```python
df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)
```

Then:

```python
df.dtypes
```

will show:

```text
join_date    datetime64[ns]
```

---

# 🔎 29. `errors="coerce"` with Dates

Suppose:

```text
join_date
03/20/2024
2024/04/25
wrong_date
15-02-2024
```

Using:

```python
pd.to_datetime(
    df["join_date"],
    errors="coerce"
)
```

gives:

```text
2024-03-20
2024-04-25
NaT
2024-02-15
```

### `NaT`

Means:

> Not a Time

It is the datetime equivalent of `NaN`.

---

# 🎲 30. `sample()`

Your screenshot shows:

```python
df["join_date"].sample(10)
```

This selects **10 random values**.

```python
print(
    df["join_date"].sample(10)
)
```

Example:

```text
40    03/20/2024
43    03/20/2024
32    2024/04/25
61    15-02-2024
48    2024/04/25
36    2024-01-15
25    May 10, 2024
6     May 10, 2024
41    May 10, 2024
72    May 10, 2024
```

### Why use `sample()`?

It is useful for checking random records.

Instead of:

```python
df.head()
```

which only shows the beginning, `sample()` gives random records.

---

# 🔄 31. Complete Data-Type Cleaning

Here is the clean version of the operations shown in your screenshots:

```python
# ============================================================
# MODIFY DATA TYPES
# ============================================================

# Check current data types
print(df.dtypes)


# ------------------------------------------------------------
# 1. Convert experience to integer
# ------------------------------------------------------------

df["experience"] = pd.to_numeric(
    df["experience"],
    errors="coerce"
)


# ------------------------------------------------------------
# 2. Convert salary to numeric
# ------------------------------------------------------------

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)


# ------------------------------------------------------------
# 3. Convert join_date to datetime
# ------------------------------------------------------------

df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)


# Check data types again

print(df.dtypes)
```

---

# 🧹 32. Clean City Column

```python
# ============================================================
# CLEAN CITY COLUMN
# ============================================================

# Remove leading/trailing spaces
# Convert all city names to proper title case.

df["city"] = (
    df["city"]
    .str.strip()
    .str.title()
)


# Check frequency

print(
    df["city"].value_counts()
)
```

---

# 🔁 33. Using Dictionary Replacement

If you specifically want abbreviations:

```python
city_mapping = {
    "Hyderabad": "Hyd",
    "Delhi": "Del",
    "Mumbai": "Mum",
    "Bangalore": "Blr"
}

df["city"] = df["city"].replace(
    city_mapping
)
```

Example:

```text
Hyderabad → Hyd
Delhi     → Del
Mumbai    → Mum
Bangalore → Blr
```

---

# 📊 34. Complete Data Inspection Workflow

This is the workflow I recommend you memorize.

```python
# ============================================================
# STEP 1: LOAD DATA
# ============================================================

import pandas as pd

df = pd.read_csv(
    "data.csv"
)


# ============================================================
# STEP 2: CHECK FIRST ROWS
# ============================================================

print(df.head())


# ============================================================
# STEP 3: CHECK DATASET SIZE
# ============================================================

print(df.shape)


# ============================================================
# STEP 4: CHECK COLUMN TYPES
# ============================================================

print(df.dtypes)


# ============================================================
# STEP 5: COMPLETE INFORMATION
# ============================================================

df.info()


# ============================================================
# STEP 6: NUMERICAL SUMMARY
# ============================================================

print(df.describe())


# ============================================================
# STEP 7: CATEGORICAL SUMMARY
# ============================================================

print(
    df.describe(
        include="object"
    )
)


# ============================================================
# STEP 8: RANDOM SAMPLE
# ============================================================

print(
    df.sample(5)
)


# ============================================================
# STEP 9: CHECK VALUE FREQUENCY
# ============================================================

print(
    df["city"].value_counts()
)


# ============================================================
# STEP 10: CLEAN TEXT
# ============================================================

df["city"] = (
    df["city"]
    .str.strip()
    .str.title()
)


# ============================================================
# STEP 11: CONVERT NUMERIC DATA
# ============================================================

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)


# ============================================================
# STEP 12: CONVERT DATE DATA
# ============================================================

df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)


# ============================================================
# STEP 13: CHECK AGAIN
# ============================================================

print(df.dtypes)

df.info()
```

---

# 🧠 35. Data Types — Easy Memory Trick

Think about your dataset like this:

```text
              DATA
                │
      ┌─────────┼─────────┐
      │         │         │
    NUMBER     TEXT      DATE
      │         │         │
      ▼         ▼         ▼
   int/float  object   datetime
```

### Example

| Column | Example | Type |
|---|---|---|
| `customer_id` | 8238 | `int64` |
| `age` | 32.0 | `float64` |
| `salary` | 50000 | `int64` |
| `name` | Customer_1 | `object` |
| `city` | Hyderabad | `object` |
| `gender` | Male | `object` |
| `join_date` | 2024-04-25 | `datetime64[ns]` |

---

# ⭐ 36. `astype()` vs `to_numeric()` vs `to_datetime()`

| Function | Purpose |
|---|---|
| `astype()` | Change datatype |
| `pd.to_numeric()` | Convert values to numbers |
| `pd.to_datetime()` | Convert values to dates |
| `errors="coerce"` | Invalid values → `NaN` / `NaT` |

### Examples

```python
# Datatype conversion
df["experience"] = df["experience"].astype("int32")


# Numeric conversion
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)


# Date conversion
df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)
```

---

# 🎯 37. Important Commands Summary

| Command | Use |
|---|---|
| `pd.read_csv()` | Read CSV |
| `df.head()` | First 5 rows |
| `df.tail()` | Last 5 rows |
| `df.shape` | Rows + columns |
| `df.shape[0]` | Number of rows |
| `df.shape[1]` | Number of columns |
| `df.info()` | Complete DataFrame information |
| `df.dtypes` | Datatypes |
| `df.describe()` | Numerical statistics |
| `df.describe(include="object")` | Categorical statistics |
| `df.sample(10)` | Random 10 rows |
| `df["city"].value_counts()` | Frequency count |
| `.astype()` | Change datatype |
| `pd.to_numeric()` | Convert to numeric |
| `pd.to_datetime()` | Convert to datetime |
| `.replace()` | Replace values |
| `.str.strip()` | Remove extra spaces |
| `.str.lower()` | Convert to lowercase |
| `.str.upper()` | Convert to uppercase |
| `.str.title()` | Title case |

---

# 🧪 38. Complete Practice Code

Use this as your **VS Code practice file**:

```python
# ============================================================
# PANDAS - LOADING DATA AND OPERATIONS
# ============================================================

import pandas as pd


# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv(
    r"C:\Users\DELL\Downloads\large_sales_database_dataset_500k.csv"
)


# ============================================================
# 2. VIEW FIRST 5 ROWS
# ============================================================

print("\nFIRST 5 ROWS")
print(df.head())


# ============================================================
# 3. VIEW LAST 5 ROWS
# ============================================================

print("\nLAST 5 ROWS")
print(df.tail())


# ============================================================
# 4. CHECK SHAPE
# ============================================================

print("\nSHAPE")
print(df.shape)


# ============================================================
# 5. CHECK DATA TYPES
# ============================================================

print("\nDATA TYPES")
print(df.dtypes)


# ============================================================
# 6. COMPLETE INFORMATION
# ============================================================

print("\nDATAFRAME INFORMATION")
df.info()


# ============================================================
# 7. NUMERICAL STATISTICS
# ============================================================

print("\nNUMERICAL SUMMARY")
print(df.describe())


# ============================================================
# 8. CATEGORICAL STATISTICS
# ============================================================

print("\nCATEGORICAL SUMMARY")

print(
    df.describe(
        include="object"
    )
)


# ============================================================
# 9. RANDOM SAMPLE
# ============================================================

print("\nRANDOM SAMPLE")

print(
    df.sample(5)
)


# ============================================================
# 10. CITY FREQUENCY
# ============================================================

print("\nCITY COUNTS")

print(
    df["city"].value_counts()
)


# ============================================================
# 11. CLEAN CITY VALUES
# ============================================================

df["city"] = (
    df["city"]
    .str.strip()
    .str.title()
)


# Check again

print("\nCITY COUNTS AFTER CLEANING")

print(
    df["city"].value_counts()
)


# ============================================================
# 12. CONVERT EXPERIENCE
# ============================================================

df["experience"] = pd.to_numeric(
    df["experience"],
    errors="coerce"
)


# ============================================================
# 13. CONVERT SALARY
# ============================================================

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)


# ============================================================
# 14. CONVERT JOIN DATE
# ============================================================

df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)


# ============================================================
# 15. CHECK FINAL DATA TYPES
# ============================================================

print("\nFINAL DATA TYPES")

print(df.dtypes)


# ============================================================
# 16. FINAL INFORMATION
# ============================================================

print("\nFINAL DATAFRAME INFORMATION")

df.info()
```

---

# 💡 One Important Correction From Your Screenshot

You showed:

```python
df["salary"] = df["salary"].astype("object")
```

This **changes salary into an object/text-like column**.

If your goal is to make salary usable for calculations, this is normally **not what you want**.

Instead use:

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

Similarly, for `experience`:

```python
df["experience"] = pd.to_numeric(
    df["experience"],
    errors="coerce"
)
```

And for `join_date`:

```python
df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)
```

---

# 🎓 Interview Questions

### ❓ 1. What does `df.shape` return?

**Answer:**

It returns a tuple containing:

```text
(number of rows, number of columns)
```

Example:

```python
df.shape
```

Output:

```text
(500000, 14)
```

---

### ❓ 2. What is the difference between `head()` and `tail()`?

**Answer:**

```python
df.head()
```

shows the first 5 rows.

```python
df.tail()
```

shows the last 5 rows.

---

### ❓ 3. What is `df.info()` used for?

**Answer:**

`df.info()` provides information about:

- Columns
- Non-null values
- Datatypes
- Number of rows
- Memory usage

---

### ❓ 4. What does `describe()` do?

**Answer:**

It provides statistical information such as:

```text
count
mean
min
25%
50%
75%
max
std
```

for numerical columns by default.

---

### ❓ 5. How do you analyze categorical columns?

```python
df.describe(include="object")
```

---

### ❓ 6. What does `value_counts()` do?

```python
df["city"].value_counts()
```

It counts the frequency of each unique value.

---

### ❓ 7. How do you convert a column to integer?

```python
df["experience"] = df["experience"].astype("int32")
```

---

### ❓ 8. How do you safely convert messy data to numeric?

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

---

### ❓ 9. How do you convert a column to datetime?

```python
df["join_date"] = pd.to_datetime(
    df["join_date"],
    errors="coerce"
)
```

---

### ❓ 10. What does `errors="coerce"` mean?

It tells Pandas:

> If a value cannot be converted, don't stop with an error; convert it to a missing value.

For numeric:

```text
invalid → NaN
```

For datetime:

```text
invalid → NaT
```

---

# 🧠 Final Mental Map

```text
                    PANDAS DATASET
                          │
                          ▼
                   pd.read_csv()
                          │
                          ▼
                       df
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
     head()             shape             info()
        │                 │                 │
     Preview        rows/columns       structure
        │                                   │
        └────────────────┬──────────────────┘
                         ▼
                       dtypes
                         │
             ┌───────────┼────────────┐
             ▼           ▼            ▼
           int/float   object       date
             │           │            │
             ▼           ▼            ▼
      to_numeric()   cleaning    to_datetime()
                         │
                         ▼
                    value_counts()
                         │
                         ▼
                      replace()
                         │
                         ▼
                    CLEAN DATA
```

### 🚀 The order you should practice

```text
1. read_csv()
      ↓
2. head()
      ↓
3. shape
      ↓
4. info()
      ↓
5. dtypes
      ↓
6. describe()
      ↓
7. describe(include="object")
      ↓
8. sample()
      ↓
9. value_counts()
      ↓
10. astype()
      ↓
11. to_numeric()
      ↓
12. to_datetime()
      ↓
13. replace()
      ↓
14. String cleaning
      ↓
15. Data cleaning
```

This is the **core Pandas "Loading Data & Operations" foundation** you need before moving into filtering, missing-value handling, duplicates, sorting, `loc`/`iloc`, `groupby`, merging, and more advanced data analysis.

I can see the screenshots from your **Pandas – Loading Data and Operations** class. The lesson is mainly about **cleaning a messy DataFrame and checking missing/unique values**.

There is also one **important mistake in the trainer's code** near the end. Let me explain everything in simple terms.

---

# 📘 Pandas Data Cleaning — Screenshot Explanation

## 1️⃣ Removing extra spaces

```python
df['city'] = df['city'].str.strip()
```

### What does `.str.strip()` do?

It removes spaces from the **beginning and end** of strings.

Example:

```text
" Hyderabad "
"Delhi "
" Mumbai"
```

After:

```python
df['city'] = df['city'].str.strip()
```

we get:

```text
"Hyderabad"
"Delhi"
"Mumbai"
```

### 🧠 Why is this important?

Without removing spaces:

```python
"Hyderabad" != " Hyderabad"
```

Pandas considers them as **different values**.

---

# 2️⃣ Replacing incorrect city names

The screenshot uses:

```python
d = {
    'Hyderabad': 'Hyd',
    'Hyderabad': 'Hyd',
    'hyderabad': 'Hyd'
}

df['city'] = df['city'].replace(d)
```

The idea is:

```text
Hyderabad → Hyd
hyderabad → Hyd
```

Then:

```python
df['city'].value_counts()
```

might give:

```text
Hyd       38
del       24
ban       19
mumbai    19
```

### ⚠️ Important Python point

This dictionary:

```python
{
    'Hyderabad': 'Hyd',
    'Hyderabad': 'Hyd'
}
```

contains the **same key twice**.

Python dictionaries cannot keep duplicate keys. The second one overwrites the first.

So normally you would write:

```python
d = {
    'Hyderabad': 'Hyd',
    'hyderabad': 'Hyd'
}
```

---

# 3️⃣ Replacing Mumbai

Screenshot:

```python
d = {
    'Mumbai': 'mumbai'
}

df['city'] = df['city'].replace(d)
```

This converts:

```text
Mumbai
```

into:

```text
mumbai
```

Now the city values have a consistent format.

---

# 4️⃣ Checking frequency of values

```python
df['city'].value_counts()
```

### Meaning

`value_counts()` tells us:

> How many times does each value appear?

Example:

```text
Hyd       38
del       24
ban       19
mumbai    19
```

Meaning:

| City | Count |
|---|---:|
| Hyd | 38 |
| del | 24 |
| ban | 19 |
| mumbai | 19 |

---

# 5️⃣ Cleaning Gender

Initially:

```python
df['gender'].value_counts()
```

Output:

```text
unknown    20
Male       16
male       16
female     15
M          13
F          11
Female      9
```

This is a **messy column**.

For example:

```text
Male
male
M
```

all represent the same thing.

Similarly:

```text
Female
female
F
```

represent the same thing.

---

## Step 1 — Remove spaces

```python
df['gender'] = df['gender'].str.strip()
```

---

## Step 2 — Standardize values

```python
d = {
    'Male': 'M',
    'male': 'M',
    'Female': 'F',
    'female': 'F'
}

df['gender'] = df['gender'].replace(d)
```

Now:

```text
Male   → M
male   → M

Female → F
female → F
```

Then:

```python
df['gender'].value_counts()
```

Output:

```text
M          45
F          35
unknown    20
```

### 🧠 This is called:

**Data Cleaning / Data Standardization**

We convert different representations of the same value into one standard representation.

---

# 6️⃣ Checking missing values

The screenshot uses:

```python
df.isnull()
```

This returns a DataFrame containing:

```text
True
False
```

Example:

```text
age
False
False
True
False
```

Meaning:

```text
False → value exists
True  → value is missing
```

---

# 7️⃣ Find rows containing missing values

Screenshot:

```python
df[df.isnull()]
```

This attempts to show missing values.

However, for beginners, a better way to see **rows containing at least one missing value** is:

```python
df[df.isnull().any(axis=1)]
```

### Understand it:

```python
df.isnull()
```

↓

Finds missing cells.

```python
.any(axis=1)
```

↓

Checks whether **any column in each row** contains a missing value.

Therefore:

```python
df[df.isnull().any(axis=1)]
```

shows rows having missing values.

---

# 8️⃣ Count missing values

This is very important:

```python
df.isnull().sum()
```

The screenshot shows:

```text
customer_id     0
name            0
age             8
gender          0
city            0
salary          0
experience      0
join_date      82
email          22
phone           25
```

This means:

| Column | Missing values |
|---|---:|
| customer_id | 0 |
| name | 0 |
| age | 8 |
| gender | 0 |
| city | 0 |
| salary | 0 |
| experience | 0 |
| join_date | 82 |
| email | 22 |
| phone | 25 |

### 🎯 Most important observation

`join_date` has:

```text
82 missing values
```

out of:

```text
100 rows
```

So only:

```text
100 - 82 = 18
```

non-null dates exist.

---

# 9️⃣ Why this code gives 92?

Screenshot:

```python
df['age'].value_counts().sum()
```

Output:

```text
92
```

Why?

There are:

```text
100 total rows
8 missing ages
```

Therefore:

```text
100 - 8 = 92
```

`value_counts()` normally ignores missing values.

So:

```python
df['age'].value_counts().sum()
```

means:

> Count all non-null values in age.

It does **NOT** mean number of unique ages.

---

# 🔴 10️⃣ VERY IMPORTANT MISTAKE IN THE LAST CODE

The screenshot uses:

```python
for col in df:
    counts_of_unique = df[col].value_counts().sum()

    print(
        'unique_values',
        counts_of_unique,
        end='-'
    )

    print(
        df.shape[0] - df[col].isnull().sum()
    )
```

The output is:

```text
unique_values 100-100
unique_values 100-100
unique_values 92-92
unique_values 100-100
...
```

It looks like the code is finding unique values.

### ❌ But it is NOT finding unique values.

This:

```python
df[col].value_counts().sum()
```

does **not** calculate the number of unique values.

It calculates:

> Number of non-null records.

---

# ✅ Correct way to find unique values

Use:

```python
df[col].nunique()
```

Example:

```python
df['gender'].nunique()
```

If:

```text
M
F
unknown
```

then:

```python
df['gender'].nunique()
```

returns:

```text
3
```

---

# 🔥 Difference You Must Remember

| Code | Meaning |
|---|---|
| `value_counts()` | Frequency of each value |
| `value_counts().sum()` | Number of non-null values |
| `nunique()` | Number of unique values |
| `isnull()` | Check missing values |
| `isnull().sum()` | Count missing values |
| `shape[0]` | Number of rows |

---

# 🧠 Example

Suppose:

```python
gender = [
    "M",
    "M",
    "F",
    "F",
    "unknown",
    None
]
```

There are:

```text
6 rows
```

### `value_counts()`

```python
df['gender'].value_counts()
```

Result:

```text
M          2
F          2
unknown    1
```

### `value_counts().sum()`

```python
df['gender'].value_counts().sum()
```

Result:

```text
5
```

Because `None` is missing.

### `nunique()`

```python
df['gender'].nunique()
```

Result:

```text
3
```

Because unique values are:

```text
M
F
unknown
```

---

# ⭐ Correct version of the last program

If your goal is to check **unique values and missing values for every column**, write:

```python
for col in df:

    unique_values = df[col].nunique()

    missing_values = df[col].isnull().sum()

    total_values = df.shape[0]

    non_null_values = total_values - missing_values

    print(
        f"{col}: "
        f"unique={unique_values}, "
        f"non_null={non_null_values}, "
        f"missing={missing_values}"
    )
```

Example output:

```text
customer_id: unique=100, non_null=100, missing=0
name:        unique=100, non_null=100, missing=0
age:         unique=18,  non_null=92,  missing=8
gender:      unique=3,  non_null=100, missing=0
city:        unique=4,  non_null=100, missing=0
```

---

# 🎯 Pandas Data Cleaning Flow

Remember this workflow:

```text
             RAW DATA
                ↓
        Check DataFrame
                ↓
             df.info()
                ↓
       Check missing values
                ↓
        df.isnull().sum()
                ↓
       Check categories
                ↓
       value_counts()
                ↓
        Clean text values
                ↓
          str.strip()
                ↓
       Standardize values
                ↓
           replace()
                ↓
       Check unique values
                ↓
           nunique()
                ↓
        Clean DataFrame
```

## 📝 Most Important Methods From These Screenshots

```python
df.info()

df.isnull()

df.isnull().sum()

df[df.isnull().any(axis=1)]

df['column'].str.strip()

df['column'].replace(dictionary)

df['column'].value_counts()

df['column'].nunique()

df.shape

df.shape[0]
```

### ⭐ One-line memory trick

> **`value_counts()` = "How many times?"**  
> **`nunique()` = "How many different?"**  
> **`isnull().sum()` = "How many missing?"**

This distinction is **very important for Pandas interviews and real-world data cleaning**.