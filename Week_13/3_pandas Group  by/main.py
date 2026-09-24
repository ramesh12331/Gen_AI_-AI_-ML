import pandas as pd
import numpy as np


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# 2. SET RANDOM SEED
# ============================================================
# np.random.seed(42)
#
# This makes sure that every time we run the program,
# we get the same random values.

np.random.seed(42)


# ============================================================
# 3. NUMBER OF EMPLOYEES
# ============================================================

n = 100


# ============================================================
# 4. CREATE EMPLOYEE DATA
# ============================================================

data = {

    # ========================================================
    # 1. EMPLOYEE ID
    # ========================================================
    "employee_id": range(1001, 1001 + n),


    # ========================================================
    # 2. AGE
    # ========================================================
    "age": np.random.randint(21, 56, n),


    # ========================================================
    # 3. EXPERIENCE
    # ========================================================
    "experience_years": np.random.randint(0, 21, n),


    # ========================================================
    # 4. SALARY
    # ========================================================
    "salary": np.random.randint(25000, 100001, n),


    # ========================================================
    # 5. WORKING HOURS
    # ========================================================
    "working_hours": np.round(
        np.random.normal(8, 1, n),
        1
    ),


    # ========================================================
    # 6. PROJECTS COMPLETED
    # ========================================================
    "projects_completed": np.random.randint(1, 16, n),


    # ========================================================
    # 7. PERFORMANCE SCORE
    # ========================================================
    "performance_score": np.round(
        np.random.normal(7, 1.2, n),
        2
    ),


    # ========================================================
    # 8. TRAINING HOURS
    # ========================================================
    "training_hours": np.random.randint(5, 101, n),


    # ========================================================
    # 9. MONTHLY SALES
    # ========================================================
    "monthly_sales": np.random.randint(
        20000,
        200001,
        n
    ),


    # ========================================================
    # 10. SATISFACTION SCORE
    # ========================================================
    "satisfaction_score": np.round(
        np.random.uniform(1, 10, n),
        2
    ),


    # ========================================================
    # 11. DEPARTMENT
    # ========================================================
    "department": np.random.choice(
        [
            "IT",
            "HR",
            "Sales",
            "Finance",
            "Marketing"
        ],
        n
    ),


    # ========================================================
    # 12. JOB ROLE
    # ========================================================
    "job_role": np.random.choice(
        [
            "Developer",
            "Manager",
            "Analyst",
            "Designer",
            "Tester",
            "HR Executive",
            "Sales Executive"
        ],
        n
    ),


    # ========================================================
    # 13. COUNTRY
    # ========================================================
    "country": np.random.choice(
        [
            "India",
            "USA",
            "UK",
            "Canada"
        ],
        n
    ),


    # ========================================================
    # 14. EMPLOYMENT TYPE
    # ========================================================
    "employment_type": np.random.choice(
        [
            "Full-Time",
            "Part-Time",
            "Contract"
        ],
        n
    ),


    # ========================================================
    # 15. EDUCATION LEVEL
    # ========================================================
    "education_level": np.random.choice(
        [
            "High School",
            "Bachelor",
            "Master",
            "PhD"
        ],
        n
    ),


    # ========================================================
    # 16. GENDER
    # ========================================================
    "gender": np.random.choice(
        [
            "Male",
            "Female"
        ],
        n
    )
}


# ============================================================
# 5. CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(data)


# ============================================================
# 6. CONVERT INTEGER COLUMNS TO FLOAT
# ============================================================
# We are going to insert some extreme values (outliers).
#
# Converting these columns to float avoids dtype assignment
# problems in newer Pandas versions.

columns_to_convert = [
    "age",
    "experience_years",
    "salary",
    "projects_completed",
    "training_hours",
    "monthly_sales"
]

df[columns_to_convert] = df[columns_to_convert].astype(float)


# ============================================================
# 7. ADD INTENTIONAL OUTLIERS
# ============================================================

# ------------------------------------------------------------
# AGE OUTLIERS
# ------------------------------------------------------------
df.loc[[5, 25, 75], "age"] = [70, 75, 80]


# ------------------------------------------------------------
# EXPERIENCE OUTLIERS
# ------------------------------------------------------------
df.loc[[10, 40, 90], "experience_years"] = [35, 40, 45]


# ------------------------------------------------------------
# SALARY OUTLIERS
# ------------------------------------------------------------
df.loc[[15, 50, 85], "salary"] = [250000, 300000, 350000]


# ------------------------------------------------------------
# WORKING HOURS OUTLIERS
# ------------------------------------------------------------
df.loc[[20, 60, 95], "working_hours"] = [15, 16, 18]


# ------------------------------------------------------------
# PROJECTS COMPLETED OUTLIERS
# ------------------------------------------------------------
df.loc[[30, 70, 99], "projects_completed"] = [40, 50, 60]


# ------------------------------------------------------------
# PERFORMANCE SCORE OUTLIERS
# ------------------------------------------------------------
df.loc[[35, 65, 88], "performance_score"] = [0.5, 0.2, 0.1]


# ------------------------------------------------------------
# TRAINING HOURS OUTLIERS
# ------------------------------------------------------------
df.loc[[45, 80, 98], "training_hours"] = [250, 300, 350]


# ------------------------------------------------------------
# MONTHLY SALES OUTLIERS
# ------------------------------------------------------------
df.loc[[55, 77, 93], "monthly_sales"] = [
    500000,
    600000,
    700000
]


# ------------------------------------------------------------
# SATISFACTION SCORE OUTLIERS
# ------------------------------------------------------------
df.loc[[12, 42, 82], "satisfaction_score"] = [
    15,
    18,
    20
]


# ============================================================
# 8. DISPLAY FIRST 5 ROWS
# ============================================================

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 9. DISPLAY DATA TYPES
# ============================================================

print("\nData Types:")
print(df.dtypes)


# ============================================================
# 10. DISPLAY SHAPE
# ============================================================

print("\nShape:")
print(df.shape)


# ============================================================
# 11. DISPLAY BASIC STATISTICS
# ============================================================

print("\nBasic Statistics:")
print(df.describe())

print(df.columns)


print("\nSalary by Country")

print(
    df.groupby("country")["salary"].mean()
)

print("\nExperience by Department")

print(
    df.groupby("department")["experience_years"].mean()
)

print("\nSalary by Department")

print(
    df.groupby("department")["salary"].mean()
)

print("\nSalary by Education Level")

print(
    df.groupby("education_level")["salary"].mean()
)

print("\nSalary by Gender")

print(
    df.groupby("gender")["salary"].mean()
)

print("\nSalary by Job Role")

print(
    df.groupby("job_role")["salary"].mean()
)

# ===========================
# df.groupby("department")["salary"].mean()

# df.groupby("job_role")["salary"].mean()

# df.groupby("country")["salary"].mean()

# df.groupby("employment_type")["salary"].mean()

# df.groupby("education_level")["salary"].mean()

# df.groupby("gender")["salary"].mean()


print(
    df.groupby("department")["experience_years"].mean().sort_values(ascending=False).head(1)
)

print(df.groupby('country')['salary'].sum())

print(df.groupby(['country','department'])['salary'].sum())

print(df.groupby(['country','department'])['salary'].sum().sort_values(ascending=False))
print(df.groupby(['country','department'])['salary'].sum().sort_values(ascending=False).head())

print(df.groupby(['country','department']).agg({'salary':'sum', "experience_years":'mean'}))

def buckets(x):
    if x >= 60:
        return 'high aged'
    elif x>=40:
        return 'moderate age'
    else:
        return 'Below age'

df['age_bucket'] = df['age'].apply(buckets)
print(df.head())

df['age_bucket'] = df['age'].apply(lambda x: 'high aged' if x >= 60 else 'moderate age' if x>=40 else 'Below age')
print(df.head())

print(df[(df['age']==49) & (df['experience_years'] == 13)])

# Syntax

result = df[(df['age']==49) & (df['experience_years']>8)]
print(result)

result = df[(df['age']==50) & (df['experience_years']>8) & (df['country'] == 'USA')]
res = result.loc[:, ['age', 'experience_years', 'country']]
print(res)

# =================================

# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.boxplot(x='age', data=df)
# plt.show()

print(df.select_dtypes(include='number').columns)
print(df.dtypes)