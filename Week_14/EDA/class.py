# ============================================================
# 🪔 DIWALI SALES DATA ANALYSIS
# ============================================================
# Project: Exploratory Data Analysis (EDA)
#
# Libraries:
# 1. Pandas      -> Data loading, cleaning and analysis
# 2. Matplotlib  -> Data visualization
# 3. Seaborn     -> Advanced and attractive visualizations
#
# Dataset:
# Diwali Sales Data.csv
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

# Pandas is used for:
# - Reading CSV files
# - Data cleaning
# - Data manipulation
# - Data analysis
import pandas as pd

# Matplotlib is used for creating charts
import matplotlib.pyplot as plt

# Seaborn is built on Matplotlib
# and is mainly used for statistical visualization
import seaborn as sns


# ============================================================
# 2. LOAD DATASET
# ============================================================

# Read the CSV file
#
# encoding='latin1' is used because the dataset
# may contain special characters.

df = pd.read_csv(
    "Diwali Sales Data.csv",
    encoding="latin1"
)


# ============================================================
# 3. VIEW FIRST 5 RECORDS
# ============================================================

# head() displays the first 5 rows
#
# It helps us understand what the dataset looks like.

print(df.head())


# ============================================================
# 4. CHECK DATASET SIZE
# ============================================================

# shape returns:
#
# (number_of_rows, number_of_columns)

print(df.shape)


# Example:
# (11251, 15)
#
# means:
# 11251 rows
# 15 columns


# ============================================================
# 5. CHECK COLUMN NAMES
# ============================================================

# Display all column names

print(df.columns)


# ============================================================
# 6. CLEAN COLUMN NAMES
# ============================================================

# Remove extra spaces from the beginning
# and end of column names.

df.columns = df.columns.str.strip()

print(df.columns)


# ============================================================
# 7. CHECK DATA TYPES
# ============================================================

# dtypes shows the data type of every column.

print(df.dtypes)


# ============================================================
# 8. CHECK MISSING VALUES
# ============================================================

# isnull() checks whether values are missing.
#
# sum() counts the number of missing values
# in each column.

print(df.isnull().sum())


# ============================================================
# 9. REMOVE UNWANTED COLUMNS
# ============================================================

# IMPORTANT:
# Column names must exactly match the dataset.
#
# errors='ignore' prevents KeyError if the column
# does not exist.

df.drop(
    columns=["Status", "unnamed1"],
    inplace=True,
    errors="ignore"
)


# Check the dataset again

print(df.head())


# ============================================================
# 10. CHECK MISSING VALUES AGAIN
# ============================================================

print(df.isnull().sum())


# ============================================================
# 11. AMOUNT COLUMN ANALYSIS
# ============================================================

# Check how many missing values are present
# in the Amount column.

print(
    "Missing Amount values:",
    df["Amount"].isnull().sum()
)


# ============================================================
# 12. HISTOGRAM OF AMOUNT
# ============================================================

# Histogram shows the distribution of Amount values.
#
# kde=True adds a smooth distribution curve.

sns.histplot(
    x="Amount",
    data=df,
    kde=True
)

plt.title("Distribution of Sales Amount")
plt.xlabel("Amount")
plt.ylabel("Frequency")

plt.show()


# ============================================================
# 13. BOX PLOT OF AMOUNT
# ============================================================

# Boxplot helps us understand:
#
# - Median
# - Minimum
# - Maximum
# - Data spread
# - Outliers

sns.boxplot(
    x="Amount",
    data=df
)

plt.title("Amount Distribution - Boxplot")

plt.show()


# ============================================================
# 14. FILL MISSING AMOUNT VALUES
# ============================================================

# Calculate the mean Amount.

amount_mean = df["Amount"].mean()

print("Mean Amount:", amount_mean)


# Replace missing Amount values with the mean.

df["Amount"] = df["Amount"].fillna(
    amount_mean
)


# Check missing values again

print(df.isnull().sum())


# ============================================================
# 15. GENDER ANALYSIS
# ============================================================

# value_counts() counts the number of records
# for each gender.

gender_count = df["Gender"].value_counts()

print(gender_count)


# ============================================================
# 16. GENDER COUNT PLOT
# ============================================================

# countplot displays the number of customers
# for each gender.

ax = sns.countplot(
    x="Gender",
    data=df
)


# Add count values on top of the bars.

for bars in ax.containers:
    ax.bar_label(bars)


plt.title("Customer Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.show()


# ============================================================
# 17. TOTAL SALES BY GENDER
# ============================================================

# groupby() groups records based on Gender.
#
# Amount.sum() calculates total revenue
# for each gender.

sales_gender = (
    df.groupby(
        "Gender",
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
)

print(sales_gender)


# ============================================================
# 18. VISUALIZE SALES BY GENDER
# ============================================================

sns.barplot(
    x="Gender",
    y="Amount",
    data=sales_gender
)

plt.title("Total Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")

plt.show()


# ============================================================
# 19. AGE GROUP + GENDER ANALYSIS
# ============================================================

# Count customers based on:
#
# Age Group
# +
# Gender

ax = sns.countplot(
    x="Age Group",
    data=df,
    hue="Gender"
)


# Add values on bars.

for bars in ax.containers:
    ax.bar_label(bars)


plt.title("Customer Count by Age Group and Gender")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")

plt.show()


# ============================================================
# 20. SALES BY AGE GROUP + GENDER
# ============================================================

# Calculate total Amount based on:
#
# Age Group
# +
# Gender

sales_age_gender = (
    df.groupby(
        ["Age Group", "Gender"],
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
)

print(sales_age_gender)


# ============================================================
# 21. VISUALIZE AGE GROUP + GENDER SALES
# ============================================================

sns.barplot(
    x="Age Group",
    y="Amount",
    data=sales_age_gender,
    hue="Gender"
)

plt.title("Sales by Age Group and Gender")
plt.xlabel("Age Group")
plt.ylabel("Total Sales")

plt.show()


# ============================================================
# 22. TOP 5 STATES BY ORDERS
# ============================================================

# Group data by State.
#
# Add all Orders for every state.
#
# sort_values() sorts from highest to lowest.
#
# head(5) selects the top 5 states.

sales_state_orders = (
    df.groupby(
        "State",
        as_index=False
    )["Orders"]
    .sum()
    .sort_values(
        by="Orders",
        ascending=False
    )
    .head(5)
)

print(sales_state_orders)


# ============================================================
# 23. VISUALIZE TOP 5 STATES BY ORDERS
# ============================================================

# Increase figure size.

plt.figure(figsize=(12, 5))

sns.barplot(
    x="State",
    y="Orders",
    data=sales_state_orders
)

plt.title("Top 5 States by Number of Orders")
plt.xlabel("State")
plt.ylabel("Orders")

plt.xticks(rotation=45)

plt.show()


# ============================================================
# 24. TOP 5 STATES BY REVENUE
# ============================================================

# Group data by State
# and calculate total Amount.

sales_state_amount = (
    df.groupby(
        "State",
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
    .head(5)
)

print(sales_state_amount)


# ============================================================
# 25. VISUALIZE TOP 5 STATES BY REVENUE
# ============================================================

plt.figure(figsize=(12, 5))

sns.barplot(
    x="State",
    y="Amount",
    data=sales_state_amount
)

plt.title("Top 5 States by Revenue")
plt.xlabel("State")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)

plt.show()


# ============================================================
# 26. MARITAL STATUS + GENDER ANALYSIS
# ============================================================

# Calculate total sales based on:
#
# Marital Status
# +
# Gender

sales_marital = (
    df.groupby(
        ["Marital_Status", "Gender"],
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
)

print(sales_marital)


# ============================================================
# 27. VISUALIZE MARITAL STATUS + GENDER
# ============================================================

sns.barplot(
    x="Marital_Status",
    y="Amount",
    data=sales_marital,
    hue="Gender"
)

plt.title("Sales by Marital Status and Gender")
plt.xlabel("Marital Status")
plt.ylabel("Total Sales")

plt.show()


# ============================================================
# 28. OCCUPATION + GENDER ANALYSIS
# ============================================================

# Calculate revenue based on:
#
# Occupation
# +
# Gender

sales_occupation = (
    df.groupby(
        ["Occupation", "Gender"],
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
)

print(sales_occupation)


# ============================================================
# 29. TOP 5 OCCUPATION + GENDER COMBINATIONS
# ============================================================

top_occupation = sales_occupation.head(5)

print(top_occupation)


# ============================================================
# 30. VISUALIZE OCCUPATION + GENDER
# ============================================================

plt.figure(figsize=(12, 5))

sns.barplot(
    x="Occupation",
    y="Amount",
    data=top_occupation,
    hue="Gender"
)

plt.title("Top 5 Occupation and Gender Combinations")
plt.xlabel("Occupation")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.show()


# ============================================================
# 31. PRODUCT CATEGORY ANALYSIS
# ============================================================

# Calculate total revenue for every product category.

sales_category = (
    df.groupby(
        "Product_Category",
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
)

print(sales_category)


# ============================================================
# 32. TOP 5 PRODUCT CATEGORIES
# ============================================================

top_categories = sales_category.head(5)

print(top_categories)


# ============================================================
# 33. VISUALIZE PRODUCT CATEGORY SALES
# ============================================================

plt.figure(figsize=(12, 5))

sns.barplot(
    x="Product_Category",
    y="Amount",
    data=top_categories
)

plt.title("Top 5 Product Categories by Revenue")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")

plt.xticks(rotation=45)

plt.show()


# ============================================================
# 34. COMBINED CUSTOMER ANALYSIS
# ============================================================

# Example:
#
# Find customers who are:
# - Female
# - Age Group 26-35
# - From selected states

filtered_df = df[
    (df["Gender"] == "F") &
    (df["Age Group"] == "26-35") &
    (df["State"].isin([
        "Uttar Pradesh",
        "Maharashtra",
        "Karnataka"
    ]))
]


# Display filtered records

print(filtered_df.head())


# ============================================================
# 35. REVENUE OF FILTERED CUSTOMERS BY STATE
# ============================================================

filtered_state_sales = (
    filtered_df
    .groupby(
        "State",
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
)

print(filtered_state_sales)


# ============================================================
# 36. FILTERED CUSTOMER ANALYSIS
# ============================================================

# Add Marital Status and Occupation
# to the previous analysis.

filtered_analysis = (
    filtered_df
    .groupby(
        ["Marital_Status", "Occupation"],
        as_index=False
    )["Amount"]
    .sum()
    .sort_values(
        by="Amount",
        ascending=False
    )
)

print(filtered_analysis)


# ============================================================
# 37. FINAL DATA CHECK
# ============================================================

# Check the final dataset size.

print("Final Shape:", df.shape)


# Display final columns.

print("Final Columns:")

for column in df.columns:
    print(column)


# Display first 5 records.

print(df.head())


# ============================================================
# 🏁 END OF PROJECT
# ============================================================