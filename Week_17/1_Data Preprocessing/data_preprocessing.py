# ============================================================
# DATA PREPROCESSING - CATEGORICAL ENCODING
# VS CODE VERSION
# ============================================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder


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

print("\n1. ORIGINAL DATAFRAME")
print(df.head())


# ============================================================
# 2. LABEL ENCODING - GENDER
# ============================================================

le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])

print("\n2. AFTER LABEL ENCODING - GENDER")
print("Gender mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df.head())

# Expected mapping:
# Female -> 0
# Male   -> 1


# ============================================================
# 3. ENCODE CHURN COLUMN
# ============================================================

df['Churn'] = df['Churn'].apply(
    lambda x: 1 if x == 'Yes' else 0
)

print("\n3. AFTER ENCODING CHURN")
print(df[['Churn']].head())

# Yes -> 1
# No  -> 0


# ============================================================
# 4. ORDINAL ENCODING - SATISFACTION
# ============================================================

df['Satisfaction'] = df['Satisfaction'].apply(
    lambda x: 0 if x == 'Low'
    else 1 if x == 'Medium'
    else 2
)

print("\n4. AFTER ORDINAL ENCODING")
print(df[['Satisfaction']].head())

# Low    -> 0
# Medium -> 1
# High   -> 2


# ============================================================
# 5. ONE-HOT ENCODING - PLAN
# ============================================================

# Create separate binary columns for Plan categories.
# The original Plan column is replaced by encoded columns.

df_onehot = pd.get_dummies(
    df,
    columns=['Plan'],
    dtype='int'
)

print("\n5. AFTER ONE-HOT ENCODING")
print(df_onehot.head())

# Expected new columns:
# Plan_Basic
# Plan_Premium
# Plan_Standard


# ============================================================
# 6. ONE-HOT ENCODING FOR PLAN ONLY
# ============================================================

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

print("\n6. ONE-HOT ENCODING FOR PLAN ONLY")
print(df_plan_encoded)


# ============================================================
# 7. FINAL ENCODED DATAFRAME
# ============================================================

print("\n7. FINAL ENCODED DATAFRAME")
print(df_onehot)

print("\nFinal column names:")
print(df_onehot.columns.tolist())


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