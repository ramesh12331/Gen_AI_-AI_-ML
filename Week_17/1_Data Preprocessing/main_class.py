# ============================================================
# DATA PREPROCESSING
# CATEGORICAL ENCODING
# ============================================================

import pandas as pd

# ============================================================
# 1. CREATE DATAFRAME
# ============================================================

data = {
    'Age': [22, 25, 30, 35, 40, 45, 50, 55],
    'Salary': [25000, 30000, 45000, 50000, 60000, 75000, 90000, 120000],
    'Monthly_Spend': [1000, 1500, 2000, 2500, 3000, 4000, 5000, 15000],
    'Gender': [
        'Male', 'Female', 'Male', 'Female',
        'Male', 'Female', 'Male', 'Female'
    ],
    'Plan': [
        'Basic', 'Standard', 'Premium', 'Basic',
        'Standard', 'Premium', 'Basic', 'Premium'
    ],
    'Satisfaction': [
        'Low', 'Medium', 'High', 'Medium',
        'Low', 'High', 'Medium', 'High'
    ],
    'Churn': ['No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Display the first five rows
df.head()


# ============================================================
# 2. LABEL ENCODING
# ============================================================

from sklearn.preprocessing import LabelEncoder

# Create LabelEncoder object
le = LabelEncoder()

# Encode Gender column
df['Gender'] = le.fit_transform(df['Gender'])

# Display the first five rows
df.head()

# Gender mapping:
# Female -> 0
# Male   -> 1


# ============================================================
# 3. ENCODE CHURN COLUMN
# ============================================================

# Convert Churn values into numerical values
df['Churn'] = df['Churn'].apply(
    lambda x: 1 if x == 'Yes' else 0
)

# Churn mapping:
# Yes -> 1
# No  -> 0

df.head()


# ============================================================
# 4. ORDINAL ENCODING
# ============================================================

# Satisfaction has an order:
# Low -> 0
# Medium -> 1
# High -> 2

df['Satisfaction'] = df['Satisfaction'].apply(
    lambda x: 0 if x == 'Low'
    else 1 if x == 'Medium'
    else 2
)

df.head()


# ============================================================
# 5. ONE-HOT ENCODING
# ============================================================

# Convert Plan categories into separate columns.
#
# Basic    -> Plan_Basic
# Standard -> Plan_Standard
# Premium  -> Plan_Premium
#
# The matching category gets 1; other categories get 0.

df_onehot = pd.get_dummies(
    df,
    columns=['Plan'],
    dtype='int'
)

# Display the encoded DataFrame
df_onehot

# Expected new columns:
# Plan_Basic
# Plan_Premium
# Plan_Standard


# ============================================================
# 6. ONE-HOT ENCODING FOR PLAN ONLY
# ============================================================

# If you want to encode only the Plan column,
# use the original Plan values.

df_plan = pd.DataFrame({
    'Plan': [
        'Basic', 'Standard', 'Premium', 'Basic',
        'Standard', 'Premium', 'Basic', 'Premium'
    ]
})

df_plan_encoded = pd.get_dummies(
    df_plan,
    columns=['Plan'],
    dtype='int'
)

df_plan_encoded


# ============================================================
# 7. ONE-HOT ENCODING WITH THE ORIGINAL DATAFRAME
# ============================================================

# Recreate the original DataFrame because the previous
# encoding steps modified df.

df = pd.DataFrame(data)

# Encode Gender
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Encode Churn
df['Churn'] = df['Churn'].apply(
    lambda x: 1 if x == 'Yes' else 0
)

# Ordinal encoding for Satisfaction
df['Satisfaction'] = df['Satisfaction'].apply(
    lambda x: 0 if x == 'Low'
    else 1 if x == 'Medium'
    else 2
)

# One-hot encoding for Plan
df_onehot = pd.get_dummies(
    df,
    columns=['Plan'],
    dtype='int'
)

# Display the final DataFrame
df_onehot.head()


# ============================================================
# 8. IMPORTANT NOTES
# ============================================================

# Label Encoding:
# Converts categories into integer labels.
#
# Ordinal Encoding:
# Converts ordered categories into numbers.
#
# One-Hot Encoding:
# Creates separate binary columns for categories.
#
# Encoding:
# Converting categorical values into numerical values.
#
# Scaling:
# Adjusting the scale of numerical features.
# ============================================================