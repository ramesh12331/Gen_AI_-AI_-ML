# 🪔 Diwali Sales Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a Diwali Sales dataset using **Python, Pandas, Matplotlib, and Seaborn**.

The main goal is to understand customer behavior and identify useful **sales and revenue insights** from the dataset.

---

## 🎯 Project Objectives

The analysis focuses on:

- 👥 Customer gender distribution
- 🎂 Age group analysis
- 🗺️ State-wise orders
- 💰 State-wise revenue
- 💍 Marital status analysis
- 💼 Occupation analysis
- 🛍️ Product category analysis
- 📊 Revenue comparison
- 🔎 Identifying important customer segments

---

## 🛠️ Technologies Used

```text
Python
Pandas
Matplotlib
Seaborn
Google Colab
Jupyter Notebook
```

---

# 📂 Dataset

Dataset used:

```text
Diwali Sales Data.csv
```

The dataset contains information about customers, orders, states, occupations, products, and sales amounts.

### Important Columns

| Column | Description |
|---|---|
| User_ID | Unique customer ID |
| Cust_name | Customer name |
| Product_ID | Product ID |
| Gender | Customer gender |
| Age Group | Customer age group |
| Age | Customer age |
| Marital_Status | Marital status |
| State | Customer state |
| Zone | Geographic zone |
| Occupation | Customer occupation |
| Product_Category | Product category |
| Orders | Number of orders |
| Amount | Purchase amount |

---

# 🚀 Project Workflow

```text
📁 Dataset
      ↓
📥 Load Data
      ↓
🔍 Understand Data
      ↓
🧹 Data Cleaning
      ↓
❌ Handle Missing Values
      ↓
📊 Exploratory Data Analysis
      ↓
📈 Data Visualization
      ↓
💡 Generate Business Insights
```

---

# 1️⃣ Import Libraries

```python
from google.colab import files

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# 2️⃣ Upload Dataset

```python
uploaded = files.upload()
```

---

# 3️⃣ Read CSV File

```python
df = pd.read_csv(
    'Diwali Sales Data.csv',
    encoding='latin1'
)

df.head()
```

### Explanation

`pd.read_csv()` is used to load a CSV file into a Pandas DataFrame.

---

# 4️⃣ Understand the Dataset

### View first 5 rows

```python
df.head()
```

### Check missing values

```python
df.isnull().sum()
```

### Check rows and columns

```python
df.shape
```

### Check column names

```python
print(df.columns)
```

---

# 5️⃣ Clean Column Names

Sometimes column names contain unnecessary spaces.

```python
df.columns = df.columns.str.strip()
```

---

# 6️⃣ Remove Unwanted Columns

```python
df.drop(
    columns=['Status', 'unnamed1'],
    inplace=True,
    errors='ignore'
)
```

### Why `errors='ignore'`?

If a column does not exist, Pandas will not throw a `KeyError`.

---

# 7️⃣ Missing Values in Amount

Check missing values:

```python
df['Amount'].isnull().sum()
```

---

# 8️⃣ Amount Distribution

### Histogram

```python
sns.histplot(
    x='Amount',
    data=df,
    kde=True
)

plt.show()
```

### What does Histogram show?

A histogram shows the **distribution of numerical data**.

---

# 9️⃣ Boxplot

```python
sns.boxplot(
    x='Amount',
    data=df
)

plt.show()
```

### Why Boxplot?

A boxplot helps identify:

- Median
- Spread
- Minimum
- Maximum
- Outliers

---

# 🔟 Fill Missing Amount Values

We can replace missing values with the mean.

```python
df['Amount'] = df['Amount'].fillna(
    df['Amount'].mean()
)
```

Check again:

```python
df.isnull().sum()
```

---

# 📊 Exploratory Data Analysis

## 👨‍👩‍👧 Gender Analysis

### Count Male and Female Customers

```python
df['Gender'].value_counts()
```

---

## 📊 Gender Count Plot

```python
ax = sns.countplot(
    x='Gender',
    data=df
)

for bars in ax.containers:
    ax.bar_label(bars)

plt.show()
```

### What are we checking?

We are checking how many records belong to each gender.

---

# 💰 Sales by Gender

```python
sales_gen = (
    df.groupby(
        ['Gender'],
        as_index=False
    )['Amount']
    .sum()
    .sort_values(
        by='Amount',
        ascending=False
    )
)

print(sales_gen)
```

### Visualization

```python
sns.barplot(
    x='Gender',
    y='Amount',
    data=sales_gen
)

plt.show()
```

---

# 🎂 Age Group Analysis

## Age Group + Gender

```python
ax = sns.countplot(
    x='Age Group',
    data=df,
    hue='Gender'
)

for bars in ax.containers:
    ax.bar_label(bars)

plt.show()
```

---

# 💰 Sales by Age Group and Gender

```python
sales_age_gender = (
    df.groupby(
        ['Age Group', 'Gender'],
        as_index=False
    )['Amount']
    .sum()
    .sort_values(
        by='Amount',
        ascending=False
    )
)

print(sales_age_gender)
```

### Visualization

```python
sns.barplot(
    x='Age Group',
    y='Amount',
    data=sales_age_gender,
    hue='Gender'
)

plt.show()
```

---

# 🗺️ State-wise Orders

Find the top 5 states based on orders.

```python
sales_state_orders = (
    df.groupby(
        ['State'],
        as_index=False
    )['Orders']
    .sum()
    .sort_values(
        by='Orders',
        ascending=False
    )
    .head(5)
)

print(sales_state_orders)
```

### Visualization

```python
sns.set(
    rc={'figure.figsize': (18, 4)}
)

sns.barplot(
    x='State',
    y='Orders',
    data=sales_state_orders
)

plt.show()
```

---

# 💰 State-wise Revenue

```python
sales_state_amount = (
    df.groupby(
        ['State'],
        as_index=False
    )['Amount']
    .sum()
    .sort_values(
        by='Amount',
        ascending=False
    )
    .head(5)
)

print(sales_state_amount)
```

### Visualization

```python
sns.barplot(
    x='State',
    y='Amount',
    data=sales_state_amount
)

plt.show()
```

---

# 💍 Marital Status Analysis

Analyze revenue by:

```text
Marital Status
+
Gender
```

```python
sales_marital = (
    df.groupby(
        ['Marital_Status', 'Gender'],
        as_index=False
    )['Amount']
    .sum()
    .sort_values(
        by='Amount',
        ascending=False
    )
)

print(sales_marital)
```

### Visualization

```python
sns.barplot(
    x='Marital_Status',
    y='Amount',
    data=sales_marital,
    hue='Gender'
)

plt.show()
```

---

# 💼 Occupation Analysis

```python
sales_occ = (
    df.groupby(
        ['Occupation', 'Gender'],
        as_index=False
    )['Amount']
    .sum()
    .sort_values(
        by='Amount',
        ascending=False
    )
    .head(5)
)

print(sales_occ)
```

### Visualization

```python
sns.barplot(
    x='Occupation',
    y='Amount',
    data=sales_occ,
    hue='Gender'
)

plt.show()
```

---

# 🛍️ Product Category Analysis

Find the top 5 product categories based on revenue.

```python
sales_category = (
    df.groupby(
        ['Product_Category'],
        as_index=False
    )['Amount']
    .sum()
    .sort_values(
        by='Amount',
        ascending=False
    )
    .head(5)
)

print(sales_category)
```

### Visualization

```python
sns.barplot(
    x='Product_Category',
    y='Amount',
    data=sales_category
)

plt.show()
```

---

# 🔎 Combined Customer Analysis

Instead of analyzing every column separately, we can combine filters.

For example:

```python
filtered_df = df[
    (df['Gender'] == 'F') &
    (df['Age Group'] == '26-35') &
    (df['State'].isin([
        'Uttar Pradesh',
        'Maharashtra',
        'Karnataka'
    ]))
]

print(filtered_df.head())
```

Then calculate revenue:

```python
filtered_df.groupby(
    'State'
)['Amount'].sum().sort_values(
    ascending=False
)
```

---

# 💡 Business Insights

The analysis can be used to identify:

- 👩 Customer distribution by gender
- 🎂 High-performing age groups
- 🗺️ States generating more orders
- 💰 States generating higher revenue
- 💍 Revenue by marital status
- 💼 Revenue by occupation
- 🛍️ Popular product categories
- 👥 Important customer segments

> **Note:** Business conclusions should be based on the actual calculated results rather than assumptions.

---

# 📚 Pandas Concepts Practiced

```text
pd.read_csv()
df.head()
df.shape
df.columns
df.isnull()
df.fillna()
df.drop()
df.groupby()
df.sum()
df.sort_values()
df.head()
df.value_counts()
df.isin()
Boolean filtering
```

---

# 📊 Visualization Concepts Practiced

Using **Seaborn**:

```text
sns.histplot()
sns.boxplot()
sns.countplot()
sns.barplot()
```

Using **Matplotlib**:

```text
plt.show()
```

---

# 🧠 Key Concepts Learned

### Pandas

```text
DataFrame
Data Cleaning
Missing Values
Filtering
Grouping
Aggregation
Sorting
```

### Seaborn

```text
Histogram
Boxplot
Countplot
Barplot
Hue
```

### EDA

```text
Data Understanding
Data Cleaning
Data Exploration
Data Visualization
Business Insights
```

---

# 🎯 Final Project Structure

```text
Diwali-Sales-Analysis/
│
├── Diwali Sales Data.csv
│
├── Diwali_Sales_Analysis.ipynb
│
└── README.md
```

---

# ⭐ Conclusion

This project demonstrates how **Python, Pandas, Matplotlib, and Seaborn** can be used to analyze sales data and discover meaningful patterns.

The project provides practical experience with:

```text
🐍 Python
🐼 Pandas
📊 Matplotlib
🎨 Seaborn
🔍 EDA
🧹 Data Cleaning
📈 Data Visualization
💡 Business Insights
```

---

## 👨‍💻 Author

**Mamidi Ramesh**

### Full-Stack Developer | Python | Pandas | SQL | FastAPI

📍 Hyderabad, Telangana, India

---

## ⭐ If you found this project useful

Give the repository a ⭐ on GitHub!