# ============================================================
# DATA PREPROCESSING
# TOPIC: ENCODING CATEGORICAL DATA
# VS CODE NOTES WITH COMMENTED EXPLANATIONS
# ============================================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ============================================================
# 1. WHAT IS DATA PREPROCESSING?
# ============================================================

# Data preprocessing is the process of preparing raw data
# before using it for Machine Learning.
#
# Common preprocessing steps:
# 1. Handling missing values
# 2. Encoding categorical data
# 3. Scaling numerical features
# 4. Splitting data into training and testing sets
#
# Machine Learning algorithms generally need numerical input.
# Therefore, text categories often need to be converted into numbers.


# ============================================================
# 2. WHAT IS ENCODING?
# ============================================================

# Encoding means converting categorical values into numerical values.
#
# Example:
# Gender:
# Male   -> 1
# Female -> 0
#
# Plan:
# Basic    -> [1, 0, 0]
# Standard -> [0, 0, 1]
# Premium  -> [0, 1, 0]
#
# Common encoding techniques:
# 1. Label Encoding
# 2. Ordinal Encoding
# 3. One-Hot Encoding


# ============================================================
# 3. CREATE A SAMPLE DATASET
# ============================================================

# Create a dictionary containing customer information.

data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55],
    "Salary": [25000, 30000, 45000, 50000, 60000, 75000, 90000, 120000],
    "Monthly_Spend": [1000, 1500, 2000, 2500, 3000, 4000, 5000, 15000],
    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female"
    ],
    "Plan": [
        "Basic", "Standard", "Premium", "Basic",
        "Standard", "Premium", "Basic", "Premium"
    ],
    "Satisfaction": [
        "Low", "Medium", "High", "Medium",
        "Low", "High", "Medium", "High"
    ],
    "Churn": [
        "No", "No", "Yes", "No",
        "Yes", "No", "Yes", "Yes"
    ]
}

# Convert the dictionary into a Pandas DataFrame.
df = pd.DataFrame(data)

# Display the first five rows.
print(df.head())

# Expected columns:
# Age, Salary, Monthly_Spend, Gender, Plan, Satisfaction, Churn


# ============================================================
# 4. IDENTIFY CATEGORICAL AND NUMERICAL COLUMNS
# ============================================================

# Numerical columns contain numbers.
numerical_columns = ["Age", "Salary", "Monthly_Spend"]

# Categorical columns contain labels or categories.
categorical_columns = ["Gender", "Plan", "Satisfaction", "Churn"]

print("Numerical Columns:", numerical_columns)
print("Categorical Columns:", categorical_columns)

# Encoding is generally applied to categorical columns,
# not directly to numerical columns such as Age or Salary.


# ============================================================
# 5. LABEL ENCODING
# ============================================================

# LabelEncoder converts each unique category into an integer.
#
# Example:
# Gender:
# Female -> 0
# Male   -> 1
#
# IMPORTANT:
# LabelEncoder assigns numbers according to the sorted
# order of the categories. Do not assume the mapping without
# checking encoder.classes_.

# Create a LabelEncoder object.
le = LabelEncoder()

# Encode the Gender column.
df["Gender"] = le.fit_transform(df["Gender"])

# Display the mapping.
print("Gender Categories:", le.classes_)

# Expected:
# Gender Categories: ['Female' 'Male']

# Display the encoded dataset.
print(df.head())

# Expected Gender values:
# Male   -> 1
# Female -> 0


# ============================================================
# 6. ENCODE THE TARGET COLUMN: CHURN
# ============================================================

# Churn represents whether a customer stopped using a service.
#
# No  -> 0
# Yes -> 1
#
# We can use LabelEncoder for this binary column.

le_churn = LabelEncoder()

df["Churn"] = le_churn.fit_transform(df["Churn"])

print("Churn Categories:", le_churn.classes_)
print(df[["Churn"]].head())

# Expected mapping:
# No  -> 0
# Yes -> 1


# ============================================================
# 7. ORDINAL ENCODING
# ============================================================

# Ordinal encoding is useful when categories have a meaningful order.
#
# Example:
# Satisfaction:
# Low    -> 0
# Medium -> 1
# High   -> 2
#
# The numerical values represent the intended order.
#
# IMPORTANT:
# Use this mapping only when the category order is meaningful.

satisfaction_mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

# Apply the mapping to the Satisfaction column.
df["Satisfaction"] = df["Satisfaction"].map(satisfaction_mapping)

print(df[["Satisfaction"]].head())

# Expected:
# Low    -> 0
# Medium -> 1
# High   -> 2


# ============================================================
# 8. ONE-HOT ENCODING
# ============================================================

# One-Hot Encoding creates a separate column for each category.
#
# Example:
#
# Plan       Plan_Basic  Plan_Premium  Plan_Standard
# Basic          1            0              0
# Premium        0            1              0
# Standard       0            0              1
#
# Each row gets 1 for its category and 0 for the other categories.
#
# One-Hot Encoding is useful for nominal categories where
# the categories do not have a natural ranking.
#
# We will use the original Plan column for this example.
# The original dataset is recreated to keep the example clear.

df_plan = pd.DataFrame({
    "Plan": [
        "Basic", "Standard", "Premium", "Basic",
        "Standard", "Premium", "Basic", "Premium"
    ]
})

# Create one-hot encoded columns.
df_onehot = pd.get_dummies(
    df_plan,
    columns=["Plan"],
    dtype=int
)

print(df_onehot)

# Expected columns:
# Plan_Basic
# Plan_Premium
# Plan_Standard


# ============================================================
# 9. ONE-HOT ENCODING WITH THE COMPLETE DATASET
# ============================================================

# Recreate the original dataset so that every example starts
# with the original categorical values.

df_original = pd.DataFrame(data)

# Convert the Plan column into separate binary columns.
df_onehot = pd.get_dummies(
    df_original,
    columns=["Plan"],
    dtype=int
)

print(df_onehot.head())

# The original Plan column is replaced by:
# Plan_Basic
# Plan_Premium
# Plan_Standard


# ============================================================
# 10. WHY NOT USE LABEL ENCODING FOR EVERY COLUMN?
# ============================================================

# Suppose Plan is encoded as:
#
# Basic    -> 0
# Premium  -> 1
# Standard -> 2
#
# A model might interpret the numbers as if Standard > Premium
# and Premium > Basic.
#
# However, these plans do not necessarily have a meaningful
# numerical order.
#
# One-Hot Encoding avoids assigning an artificial ranking
# to these nominal categories.


# ============================================================
# 11. ENCODING TECHNIQUES COMPARISON
# ============================================================

# Label Encoding:
# Converts categories into integer labels.
# Example: Male -> 1, Female -> 0.
#
# Ordinal Encoding:
# Converts ordered categories into numbers.
# Example: Low -> 0, Medium -> 1, High -> 2.
#
# One-Hot Encoding:
# Creates separate binary columns.
# Example: Basic, Standard, Premium become separate columns.
#
# Choose the technique based on the meaning of the data
# and the requirements of the Machine Learning model.


# ============================================================
# 12. IMPORTANT: AVOID CHANGING THE SAME COLUMN REPEATEDLY
# ============================================================

# If you encode a column and then run another encoding operation
# on that already-encoded column, the result may not be what
# you expect.
#
# Best practice:
# 1. Keep a copy of the original dataset.
# 2. Apply each encoding method to the appropriate column.
# 3. Inspect the resulting DataFrame.
# 4. Confirm the category-to-number mapping.


# ============================================================
# 13. COMBINED EXAMPLE
# ============================================================

# Recreate a fresh DataFrame.
df_encoded = pd.DataFrame(data)

# Encode Gender as binary labels.
df_encoded["Gender"] = df_encoded["Gender"].map({
    "Female": 0,
    "Male": 1
})

# Encode Satisfaction using its natural order.
df_encoded["Satisfaction"] = df_encoded["Satisfaction"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# Encode Churn as a binary target.
df_encoded["Churn"] = df_encoded["Churn"].map({
    "No": 0,
    "Yes": 1
})

# One-Hot Encode Plan.
df_encoded = pd.get_dummies(
    df_encoded,
    columns=["Plan"],
    dtype=int
)

# Display the final encoded dataset.
print(df_encoded)

# Expected column names:
# Age
# Salary
# Monthly_Spend
# Gender
# Satisfaction
# Churn
# Plan_Basic
# Plan_Premium
# Plan_Standard


# ============================================================
# 14. WHAT IS SCALING?
# ============================================================

# Scaling is another data preprocessing technique.
#
# Encoding:
# Converts categories into numerical values.
#
# Scaling:
# Changes the scale or range of numerical features.
#
# Example:
# Age            -> values around 22 to 55
# Salary         -> values around 25000 to 120000
# Monthly_Spend  -> values around 1000 to 15000
#
# These columns have very different numerical ranges.
#
# Some Machine Learning algorithms are sensitive to feature
# scales. Scaling can help those algorithms.
#
# Common scaling techniques:
# 1. Standardization
# 2. Min-Max Scaling
#
# Scaling will be covered separately.


# ============================================================
# 15. QUICK REVISION
# ============================================================

# Data Preprocessing:
# Preparing raw data for analysis or Machine Learning.
#
# Encoding:
# Converting categorical values into numerical representations.
#
# Label Encoding:
# Assigns an integer to each category.
#
# Ordinal Encoding:
# Represents categories with a meaningful order.
#
# One-Hot Encoding:
# Creates separate binary columns for categories.
#
# Scaling:
# Adjusts the numerical range or distribution of features.


# ============================================================
# 16. PRACTICE QUESTIONS
# ============================================================

# 1. What is data preprocessing?
# 2. Why do we encode categorical data?
# 3. What is Label Encoding?
# 4. What is Ordinal Encoding?
# 5. What is One-Hot Encoding?
# 6. What is the difference between encoding and scaling?
# 7. Which encoding method can represent Low, Medium, High?
# 8. Why might One-Hot Encoding be suitable for Plan?
# 9. What does pd.get_dummies() do?
# 10. Why should we keep a copy of the original dataset?


# ============================================================
# END OF DATA PREPROCESSING NOTES
# ============================================================