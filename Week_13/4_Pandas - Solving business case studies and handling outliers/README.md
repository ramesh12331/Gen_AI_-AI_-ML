# 📊 Pandas – Solving Business Case Studies & Handling Outliers

## 📌 Overview

In real-world Data Analyst jobs, we don't use Pandas only to display data.

We use Pandas to answer **business questions** from data.

For example:

* Which city has the highest sales?
* Which products generate the most revenue?
* Which customers are Premium customers?
* What are the top 10 orders?
* How much discount was given?
* What is the final sales amount after discount?
* Are there unusual values in the data?
* Are those unusual values actual business transactions or data errors?

This chapter teaches how to use **Pandas to solve a sales business case study**.

---

# 🗂️ 1. Import Pandas

## What is Pandas?

Pandas is a Python library used for:

* Data analysis
* Data cleaning
* Data manipulation
* Data filtering
* Data aggregation
* Business analysis

## Syntax

```python
import pandas as pd
```

## Example

```python
import pandas as pd
```

---

# 📂 2. Read CSV File

We can load a CSV file using `read_csv()`.

## Syntax

```python
df = pd.read_csv("filename.csv")
```

## Example

```python
df = pd.read_csv("sales_data.csv")
```

Now the CSV data is stored inside the DataFrame `df`.

---

# 🔎 3. Filtering Data

Filtering means selecting rows that satisfy a condition.

## Example

Suppose we want products where:

```text
unit_price >= 30000
```

### Code

```python
result = df[df['unit_price'] >= 30000]

print(result)
```

### Explanation

```python
df['unit_price'] >= 30000
```

creates a Boolean condition:

```text
True
False
True
False
...
```

Then:

```python
df[condition]
```

returns only the matching rows.

---

# ⚠️ Important Difference

This:

```python
result = df['unit_price'] >= 30000
```

returns a Boolean Series.

Example:

```text
0     True
1     False
2     True
3     False
```

But this:

```python
result = df[df['unit_price'] >= 30000]
```

returns the actual filtered DataFrame.

### Remember

```text
Condition only
      ↓
df['unit_price'] >= 30000

Filtered DataFrame
      ↓
df[df['unit_price'] >= 30000]
```

---

# 🎯 4. Filtering Multiple Conditions

We can combine multiple conditions using:

```text
&   → AND
|   → OR
~   → NOT
```

## Example

Find customers who:

* live in Hyderabad
* AND are Premium customers

### Code

```python
result = df[
    (df['city'] == 'Hyderabad') &
    (df['customer_type'] == 'Premium')
]

print(result)
```

### Explanation

```python
df['city'] == 'Hyderabad'
```

means:

```text
City must be Hyderabad
```

And:

```python
df['customer_type'] == 'Premium'
```

means:

```text
Customer type must be Premium
```

`&` means both conditions must be true.

---

# 📌 5. `.head()`

`head()` displays the first rows.

## Syntax

```python
df.head()
```

By default:

```text
first 5 rows
```

## Example

```python
result = df[
    (df['city'] == 'Hyderabad') &
    (df['customer_type'] == 'Premium')
].head()

print(result)
```

---

# 🔢 6. `.count()`

`count()` counts non-null values.

Example:

```python
result = df[
    (df['city'] == 'Hyderabad') &
    (df['customer_type'] == 'Premium')
].head().count()

print(result)
```

⚠️ Important:

This does **not directly mean "number of rows"**.

It counts non-null values for each column.

If you want the number of matching rows, a clearer approach is:

```python
result = df[
    (df['city'] == 'Hyderabad') &
    (df['customer_type'] == 'Premium')
]

print(len(result))
```

---

# 📈 7. Sorting Data

Sorting means arranging data in ascending or descending order.

## Syntax

```python
df.sort_values(
    by='column_name',
    ascending=True
)
```

### Ascending

```python
df.sort_values(
    by='unit_price',
    ascending=True
)
```

Small → Large

### Descending

```python
df.sort_values(
    by='unit_price',
    ascending=False
)
```

Large → Small

---

# 💰 8. Find Highest-Priced Orders

Your code:

```python
result = df.sort_values(
    by='unit_price',
    ascending=False
)

res = result[
    ['order_id', 'city', 'unit_price']
].head()

print(res)
```

This gives the highest unit-price orders.

### Business Question

> Which orders have the highest unit price?

---

# 🧮 9. Calculate Total Price

One of the most important business calculations.

## Formula

```text
Total Price = Quantity × Unit Price
```

## Pandas Code

```python
df['Total_Price'] = (
    df['quantity'] *
    df['unit_price']
)
```

### Example

Suppose:

```text
quantity   = 3
unit_price = ₹20,000
```

Then:

```text
Total Price
= 3 × 20,000
= ₹60,000
```

---

# 🏷️ 10. Calculate Discount Amount

Suppose the DataFrame contains:

```text
discount = 10
```

This means:

```text
10%
```

## Formula

```text
Discount Amount
=
Total Price × Discount / 100
```

## Code

```python
df['discount_amount'] = (
    df['Total_Price'] *
    df['discount'] /
    100
)
```

### Example

```text
Total Price = ₹60,000
Discount    = 10%
```

Calculation:

```text
60,000 × 10 / 100

= ₹6,000
```

So:

```text
Discount Amount = ₹6,000
```

---

# 💵 11. Calculate Total Price After Discount

Now calculate the final sales value.

## Formula

```text
Total Price After Discount
=
Total Price - Discount Amount
```

## Code

```python
df['total_price_after_discount'] = (
    df['Total_Price'] -
    df['discount_amount']
)
```

### Example

```text
Total Price       = ₹60,000
Discount Amount   = ₹6,000
--------------------------------
Final Price       = ₹54,000
```

---

# 🔄 Complete Sales Calculation

The complete process is:

```text
Quantity
   ×
Unit Price
   ↓
Total Price
   ↓
Discount
   ↓
Discount Amount
   ↓
Total Price - Discount Amount
   ↓
Total Price After Discount
```

### Code

```python
df['Total_Price'] = (
    df['quantity'] *
    df['unit_price']
)

df['discount_amount'] = (
    df['Total_Price'] *
    df['discount'] /
    100
)

df['total_price_after_discount'] = (
    df['Total_Price'] -
    df['discount_amount']
)
```

---

# 🏆 12. Find Top 10 Orders

Now we can identify the orders that generated the highest final sales.

## Code

```python
top_10_orders = df.sort_values(
    by='total_price_after_discount',
    ascending=False
)[
    [
        'order_id',
        'city',
        'product',
        'quantity',
        'total_price_after_discount'
    ]
].head(10)

print(top_10_orders)
```

### Business Question

> What are the top 10 orders based on sales after discount?

---

# 🏙️ 13. City-Wise Sales Analysis

A company may want to know:

> Which city generates the highest sales?

We can use:

```python
groupby()
```

## Code

```python
city_sales = (
    df.groupby('city')
      ['total_price_after_discount']
      .sum()
      .sort_values(ascending=False)
)

print(city_sales)
```

---

# 🧠 Understanding `groupby()`

Suppose our data is:

```text
City          Sales
---------------------
Hyderabad     50000
Hyderabad     30000
Chennai       40000
Chennai       20000
Mumbai        60000
```

After:

```python
df.groupby('city')['total_price_after_discount'].sum()
```

we get:

```text
Mumbai        60000
Hyderabad     80000
Chennai       60000
```

After sorting descending:

```text
Hyderabad     80000
Mumbai        60000
Chennai       60000
```

---

# 📦 14. City + Category + Product Analysis

We can perform more detailed analysis using multiple grouping columns.

## Code

```python
city_sales = (
    df.groupby(
        ['city', 'category', 'product']
    )['total_price_after_discount']
    .sum()
    .sort_values(ascending=False)
)

print(city_sales)
```

This answers:

> Which city + category + product combination generates the highest sales?

---

# 🔍 Understanding Multi-Level GroupBy

Suppose:

```text
City       Category       Product       Sales
------------------------------------------------
Hyderabad  Electronics    Laptop        100000
Hyderabad  Electronics    Mobile         50000
Chennai    Electronics    Laptop         80000
Mumbai     Furniture      Chair          60000
```

Grouping by:

```python
['city', 'category', 'product']
```

creates groups like:

```text
Hyderabad
   └── Electronics
          ├── Laptop
          └── Mobile

Chennai
   └── Electronics
          └── Laptop

Mumbai
   └── Furniture
          └── Chair
```

---

# 📊 15. Business Case Study Questions

Using this sales dataset, we can answer:

### Question 1

Which orders have:

```text
unit_price >= 30000?
```

```python
df[df['unit_price'] >= 30000]
```

---

### Question 2

Which Premium customers are from Hyderabad?

```python
df[
    (df['city'] == 'Hyderabad') &
    (df['customer_type'] == 'Premium')
]
```

---

### Question 3

Which orders have the highest unit price?

```python
df.sort_values(
    by='unit_price',
    ascending=False
).head(10)
```

---

### Question 4

What is the total price of every order?

```python
df['Total_Price'] = (
    df['quantity'] *
    df['unit_price']
)
```

---

### Question 5

How much discount was given?

```python
df['discount_amount'] = (
    df['Total_Price'] *
    df['discount'] /
    100
)
```

---

### Question 6

What is the final price after discount?

```python
df['total_price_after_discount'] = (
    df['Total_Price'] -
    df['discount_amount']
)
```

---

### Question 7

What are the top 10 orders?

```python
df.sort_values(
    by='total_price_after_discount',
    ascending=False
).head(10)
```

---

### Question 8

Which city has the highest sales?

```python
df.groupby('city')[
    'total_price_after_discount'
].sum().sort_values(
    ascending=False
)
```

---

### Question 9

Which city/category/product combination has the highest sales?

```python
df.groupby(
    ['city', 'category', 'product']
)['total_price_after_discount'].sum().sort_values(
    ascending=False
)
```

---

# 🚨 16. What is an Outlier?

An **outlier** is a value that is unusually high or unusually low compared with most other values.

Example:

```text
10
12
11
13
12
14
15
200
```

Here:

```text
200
```

is potentially an outlier.

---

# 🏢 17. Business Example of an Outlier

Suppose product prices are:

```text
₹20,000
₹22,000
₹25,000
₹21,000
₹23,000
₹3,50,000
```

`₹3,50,000` looks unusual compared with the other values.

But we should **not immediately delete it**.

It could be:

```text
❌ Data entry mistake
OR
✅ Genuine expensive product
```

Therefore:

```text
Outlier ≠ Automatically Wrong Data
```

---

# 📌 18. Why Do We Handle Outliers?

Outliers can affect:

* Mean
* Standard deviation
* Correlation
* Machine learning models
* Business reports
* Sales analysis

Example:

```text
Normal sales:

10000
12000
15000
11000
13000
```

Add one extreme value:

```text
500000
```

The average can change significantly.

---

# 📐 19. IQR Method

One common method for detecting outliers is the **Interquartile Range (IQR)** method.

### Formula

```text
IQR = Q3 - Q1
```

Where:

```text
Q1 = 25th percentile
Q3 = 75th percentile
```

Outlier boundaries:

```text
Lower Limit = Q1 - 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR
```

---

# 🧮 20. Detect Outliers Using Pandas

Example using `unit_price`:

```python
Q1 = df['unit_price'].quantile(0.25)

Q3 = df['unit_price'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR
```

Now find the outliers:

```python
outliers = df[
    (df['unit_price'] < lower_limit) |
    (df['unit_price'] > upper_limit)
]

print(outliers)
```

---

# 🔍 21. Understanding the IQR Code

### Step 1

```python
Q1 = df['unit_price'].quantile(0.25)
```

Finds the 25th percentile.

### Step 2

```python
Q3 = df['unit_price'].quantile(0.75)
```

Finds the 75th percentile.

### Step 3

```python
IQR = Q3 - Q1
```

Finds the middle 50% range.

### Step 4

```python
lower_limit = Q1 - 1.5 * IQR
```

Values below this may be outliers.

### Step 5

```python
upper_limit = Q3 + 1.5 * IQR
```

Values above this may be outliers.

---

# 📊 22. Find Outliers in Total Sales

We can also check:

```python
Q1 = df['total_price_after_discount'].quantile(0.25)

Q3 = df['total_price_after_discount'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df['total_price_after_discount'] < lower_limit) |
    (df['total_price_after_discount'] > upper_limit)
]

print(outliers)
```

---

# ⚠️ 23. Should We Remove Outliers?

Do **not** automatically remove every outlier.

First investigate.

### Case 1 — Data Entry Error

```text
unit_price = ₹5,000,000
```

But the actual product price should be:

```text
₹50,000
```

Then it may be an error.

---

### Case 2 — Genuine Business Transaction

Suppose:

```text
unit_price = ₹500,000
```

and the product is an expensive machine.

This could be a genuine transaction.

Therefore, it should not automatically be removed.

---

# 🛠️ 24. Common Outlier Handling Methods

Depending on the business problem, we can:

```text
1. Keep the value
2. Remove the value
3. Correct the value
4. Replace the value
5. Cap/Winsorize the value
6. Investigate the source
```

The correct method depends on **why the outlier exists**.

---

# 📦 25. Complete Business Analysis Flow

A real Data Analyst workflow can look like this:

```text
                 SALES DATA
                     ↓
              Load CSV File
                     ↓
             Inspect the Data
                     ↓
             Clean the Data
                     ↓
             Check Missing Values
                     ↓
             Calculate Total Price
                     ↓
             Calculate Discount
                     ↓
          Calculate Final Sales
                     ↓
              Filter Data
                     ↓
              Sort Data
                     ↓
             GroupBy Analysis
                     ↓
            Find Top Products
                     ↓
             City-wise Sales
                     ↓
       Category/Product Analysis
                     ↓
             Detect Outliers
                     ↓
         Investigate Outliers
                     ↓
             Business Insights
```

---

# 💻 26. Complete VS Code Example

```python
import pandas as pd


# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv("sales_data.csv")

print(df)


# ============================================================
# 2. FILTER UNIT PRICE
# ============================================================

result = df[df['unit_price'] >= 30000]

print("\nProducts with unit price >= 30000:")
print(result)


# ============================================================
# 3. HYDERABAD PREMIUM CUSTOMERS
# ============================================================

result = df[
    (df['city'] == 'Hyderabad') &
    (df['customer_type'] == 'Premium')
]

print("\nHyderabad Premium Customers:")
print(result)


# ============================================================
# 4. TOP UNIT PRICE ORDERS
# ============================================================

result = df.sort_values(
    by='unit_price',
    ascending=False
)

res = result[
    ['order_id', 'city', 'unit_price']
].head(10)

print("\nTop 10 Unit Price Orders:")
print(res)


# ============================================================
# 5. CALCULATE TOTAL PRICE
# ============================================================

df['Total_Price'] = (
    df['quantity'] *
    df['unit_price']
)

print("\nTotal Price:")
print(df[['order_id', 'quantity',
          'unit_price', 'Total_Price']])


# ============================================================
# 6. CALCULATE DISCOUNT AMOUNT
# ============================================================

df['discount_amount'] = (
    df['Total_Price'] *
    df['discount'] /
    100
)

print("\nDiscount Amount:")
print(
    df[
        [
            'order_id',
            'Total_Price',
            'discount',
            'discount_amount'
        ]
    ]
)


# ============================================================
# 7. CALCULATE FINAL SALES
# ============================================================

df['total_price_after_discount'] = (
    df['Total_Price'] -
    df['discount_amount']
)

print("\nFinal Sales:")
print(
    df[
        [
            'order_id',
            'Total_Price',
            'discount_amount',
            'total_price_after_discount'
        ]
    ]
)


# ============================================================
# 8. TOP 10 ORDERS
# ============================================================

top_10_orders = df.sort_values(
    by='total_price_after_discount',
    ascending=False
)[
    [
        'order_id',
        'city',
        'product',
        'quantity',
        'total_price_after_discount'
    ]
].head(10)

print("\nTop 10 Orders:")
print(top_10_orders)


# ============================================================
# 9. CITY-WISE SALES
# ============================================================

city_sales = (
    df.groupby('city')
      ['total_price_after_discount']
      .sum()
      .sort_values(ascending=False)
)

print("\nCity-wise Sales:")
print(city_sales)


# ============================================================
# 10. CITY + CATEGORY + PRODUCT SALES
# ============================================================

city_category_product_sales = (
    df.groupby(
        ['city', 'category', 'product']
    )['total_price_after_discount']
    .sum()
    .sort_values(ascending=False)
)

print("\nCity + Category + Product Sales:")
print(city_category_product_sales)


# ============================================================
# 11. OUTLIER DETECTION - UNIT PRICE
# ============================================================

Q1 = df['unit_price'].quantile(0.25)

Q3 = df['unit_price'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR


outliers = df[
    (df['unit_price'] < lower_limit) |
    (df['unit_price'] > upper_limit)
]

print("\nUnit Price Outliers:")
print(outliers)


# ============================================================
# 12. OUTLIER DETECTION - FINAL SALES
# ============================================================

Q1 = df['total_price_after_discount'].quantile(0.25)

Q3 = df['total_price_after_discount'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR


sales_outliers = df[
    (df['total_price_after_discount'] < lower_limit) |
    (df['total_price_after_discount'] > upper_limit)
]

print("\nFinal Sales Outliers:")
print(sales_outliers)
```

---

# 📝 27. Quick Revision

```text
read_csv()
    ↓
Load data

df[condition]
    ↓
Filter rows

sort_values()
    ↓
Sort data

head()
    ↓
Get first rows

quantity × unit_price
    ↓
Total Price

Total Price × discount / 100
    ↓
Discount Amount

Total Price - Discount Amount
    ↓
Final Sales

groupby()
    ↓
Business aggregation

quantile()
    ↓
Calculate Q1/Q3

IQR = Q3 - Q1
    ↓
Detect potential outliers
```

---

# 🎯 Interview Questions

## Q1. What is Pandas?

**Answer:**

Pandas is a Python library used for data manipulation, cleaning, analysis and business data processing.

---

## Q2. How do you filter rows in Pandas?

```python
df[df['unit_price'] >= 30000]
```

---

## Q3. How do you apply multiple conditions?

```python
df[
    (df['city'] == 'Hyderabad') &
    (df['customer_type'] == 'Premium')
]
```

---

## Q4. What does `&` mean?

`&` represents **AND** when combining Pandas Boolean conditions.

---

## Q5. How do you calculate total sales?

```python
df['Total_Price'] = (
    df['quantity'] *
    df['unit_price']
)
```

---

## Q6. How do you calculate discount amount?

```python
df['discount_amount'] = (
    df['Total_Price'] *
    df['discount'] /
    100
)
```

---

## Q7. How do you find the top 10 orders?

```python
df.sort_values(
    by='total_price_after_discount',
    ascending=False
).head(10)
```

---

## Q8. What is `groupby()` used for?

`groupby()` is used to divide data into groups and perform aggregation such as:

```text
sum()
mean()
count()
min()
max()
```

---

## Q9. What is an outlier?

An outlier is a value that is unusually far from the general pattern of the data.

---

## Q10. What is IQR?

```text
IQR = Q3 - Q1
```

It represents the range containing the middle 50% of the data.

---

## Q11. What are the IQR outlier limits?

```text
Lower Limit = Q1 - 1.5 × IQR

Upper Limit = Q3 + 1.5 × IQR
```

---

## Q12. Should every outlier be removed?

**No.**

An outlier can be either:

```text
❌ Data error
or
✅ Genuine business value
```

We should investigate before removing it.

---

# ⭐ Final Summary

The main goal of Pandas business analysis is not just writing code.

The goal is:

```text
DATA
 ↓
QUESTION
 ↓
PANDAS ANALYSIS
 ↓
INSIGHT
 ↓
BUSINESS DECISION
```

For this sales case study, you learned:

```text
✅ CSV loading
✅ Data filtering
✅ Multiple conditions
✅ Sorting
✅ head()
✅ Total price calculation
✅ Discount calculation
✅ Final sales calculation
✅ Top 10 orders
✅ City-wise sales
✅ Multi-column groupby
✅ Outlier concept
✅ IQR method
✅ Outlier investigation
```

### 🚀 Next Level

After this, the natural next Pandas business-analysis topics are:

```text
1. Missing Values
2. Duplicate Data
3. Outlier Handling
4. Advanced GroupBy
5. Pivot Tables
6. Aggregation with agg()
7. `apply()` and Lambda
8. Time-Series Sales Analysis
9. Customer Analysis
10. Product Performance Analysis
11. Monthly/Yearly Sales Trends
12. Business Dashboard Preparation
```

These topics take you from **basic Pandas → practical Data Analyst-level Pandas**.
