# 📊 OUTLIERS — Complete NumPy & Pandas Notes

Chapter: Solving Business Case Studies and Handling Outliers

Ramesh, below are beginner-to-advanced notes based on your classroom screenshots. I've organized everything in VS Code Python format, including definitions, syntax, examples, mathematical calculations, dry runs, visualization, outlier detection, removal, capping, and interview questions.

You can copy the complete code into a file named `outliers.py`.

## 1. What is an Outlier?

Definition: An outlier is a data point that is unusually far away from most other observations in a dataset.

Example:

```
Normal values: 10, 12, 11, 13, 15, 14

Outlier: 100

Dataset: [10, 12, 11, 13, 15, 14, 100]
```

Here, `100` is unusually large compared with the other values.

### Why do we handle outliers?

Outliers can affect the mean, standard deviation, statistical analysis, and machine learning models.

However, not every outlier is an error. For example, a ₹5,00,000 transaction may be a legitimate high-value sale. Always investigate before removing it.

## 2. Methods covered in your class

Method 1 — Boxplot

Visualize the distribution and identify potential outliers.

Method 2 — Z-score / 3-Sigma

Use the mean and standard deviation to identify extreme values.

Method 3 — Percentile Method

Identify values outside selected percentile limits.

Method 4 — IQR Method

Use Q1, Q3, and the interquartile range to identify outliers.

Outlier Treatment

Remove extreme values or cap them at calculated limits.

# Complete VS Code Python Notes

Python

Run

```
# ============================================================
# CHAPTER: OUTLIER DETECTION AND HANDLING
# NumPy | Pandas | Matplotlib | Seaborn
# ============================================================


# ============================================================
# 1. INSTALL REQUIRED LIBRARIES
# ============================================================

# Run this command in VS Code terminal:
#
# pip install numpy pandas matplotlib seaborn


# ============================================================
# 2. IMPORT LIBRARIES
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 3. WHAT IS AN OUTLIER?
# ============================================================

# Definition:
#
# An outlier is a data point that is significantly different
# from most other values in a dataset.
#
# Example:
#
# Normal values:
# 10, 12, 11, 13, 15, 14
#
# Outlier:
# 100
#
# Outliers may occur because of:
#
# 1. Data entry mistakes
# 2. Measurement errors
# 3. Unusual customer behavior
# 4. Genuine extreme observations
# 5. Data processing errors


# ============================================================
# 4. CREATE NUMPY ARRAY
# ============================================================

data = np.array([
    10, 12, 11, 13, 12, 15, 14, 13, 12, 11,
    16, 15, 14, 13, 12, 100, 110, 12, 11, 10
])

print("Original Data:")
print(data)

print("Total Elements:", len(data))


# ============================================================
# 5. UNDERSTAND MEAN
# ============================================================

# Definition:
#
# Mean is the average of all values.
#
# Formula:
#
# Mean = Sum of all values / Number of values

mean = np.mean(data)

print("Mean:", mean)


# ============================================================
# 6. UNDERSTAND MEDIAN
# ============================================================

# Definition:
#
# Median is the middle value after sorting the data.
#
# Median is generally less sensitive to extreme values
# than the mean.

median = np.median(data)

print("Median:", median)


# ============================================================
# 7. UNDERSTAND STANDARD DEVIATION
# ============================================================

# Definition:
#
# Standard deviation measures how spread out the values
# are around the mean.
#
# Small standard deviation:
# Values are relatively close to the mean.
#
# Large standard deviation:
# Values are more spread out.

std = np.std(data)

print("Standard Deviation:", std)


# ============================================================
# 8. VISUALIZE OUTLIERS USING BOXPLOT
# ============================================================

# What is a boxplot?
#
# A boxplot visually displays:
#
# Q1       = 25th percentile
# Median   = 50th percentile
# Q3       = 75th percentile
# Whiskers = Values within the whisker limits
# Points beyond whiskers = Potential outliers

sns.boxplot(x=data)

plt.title("Original Data - Boxplot")

plt.show()


# ============================================================
# 9. METHOD 1: THREE-SIGMA RULE
# ============================================================

# Definition:
#
# The 3-sigma method identifies values more than
# three standard deviations away from the mean.
#
# Formula:
#
# Lower Limit = Mean - (3 * Standard Deviation)
#
# Upper Limit = Mean + (3 * Standard Deviation)
#
# Outlier condition:
#
# value < Lower Limit
#
# OR
#
# value > Upper Limit


# Step 1: Calculate mean

mean = np.mean(data)


# Step 2: Calculate standard deviation

std = np.std(data)


# Step 3: Calculate lower limit

ll = mean - (3 * std)


# Step 4: Calculate upper limit

ul = mean + (3 * std)


print("Mean:", mean)

print("Standard Deviation:", std)

print("Lower Limit:", ll)

print("Upper Limit:", ul)


# ============================================================
# 10. FIND OUTLIERS USING 3-SIGMA
# ============================================================

# Syntax:
#
# data[(data < ll) | (data > ul)]
#
# | means OR
#
# If a value is below the lower limit OR above the
# upper limit, it is identified as an outlier.

outliers = data[
    (data < ll) | (data > ul)
]

print("3-Sigma Outliers:", outliers)


# ============================================================
# 11. REMOVE OUTLIERS USING 3-SIGMA
# ============================================================

# Keep only values inside the calculated limits.
#
# & means AND.

data_without_outliers = data[
    (data >= ll) & (data <= ul)
]

print("Original Data:", data)

print("After Removal:", data_without_outliers)


# ============================================================
# 12. CAP OUTLIERS USING 3-SIGMA
# ============================================================

# Definition:
#
# Capping means replacing extreme values with the
# calculated lower or upper limit.
#
# Values below ll become ll.
#
# Values above ul become ul.
#
# Values inside the limits remain unchanged.
#
# Syntax:
#
# np.clip(array, lower_limit, upper_limit)

capped_data = np.clip(data, ll, ul)

print("Original Data:", data)

print("After Capping:", capped_data)


# ============================================================
# 13. METHOD 2: PERCENTILE METHOD
# ============================================================

# Definition:
#
# A percentile indicates the value below which a given
# percentage of observations falls.
#
# Example:
#
# 25th percentile = Q1
# 50th percentile = Median
# 75th percentile = Q3
#
# Here we use:
#
# 1st percentile  = Lower Limit
# 99th percentile = Upper Limit
#
# These limits are a chosen trimming rule, not a
# universal definition of an outlier.


percentile_data = np.array([
    10, 12, 11, 13, 15, 14, 16, 18, 20, 100
])


# Step 1: Calculate percentile limits

ll = np.percentile(percentile_data, 1)

ul = np.percentile(percentile_data, 99)


print("Lower Limit:", ll)

print("Upper Limit:", ul)


# ============================================================
# 14. FIND OUTLIERS USING PERCENTILES
# ============================================================

outliers = percentile_data[
    (percentile_data < ll) |
    (percentile_data > ul)
]

print("Percentile Outliers:", outliers)


# ============================================================
# 15. REMOVE OUTLIERS USING PERCENTILES
# ============================================================

data_without_outliers = percentile_data[
    (percentile_data >= ll) &
    (percentile_data <= ul)
]

print("After Removal:", data_without_outliers)


# ============================================================
# 16. CAP OUTLIERS USING PERCENTILES
# ============================================================

capped_data = np.clip(
    percentile_data,
    ll,
    ul
)

print("After Capping:", capped_data)


# ============================================================
# 17. METHOD 3: IQR METHOD
# ============================================================

# IQR = Interquartile Range
#
# Definition:
#
# IQR measures the spread of the middle 50% of data.
#
# Formula:
#
# IQR = Q3 - Q1
#
# Q1 = 25th percentile
#
# Q3 = 75th percentile
#
# Lower Limit = Q1 - (1.5 * IQR)
#
# Upper Limit = Q3 + (1.5 * IQR)


iqr_data = np.array([
    10, 12, 11, 13, 15, 14, 16, 18, 20, 100
])


# Step 1: Calculate Q1

Q1 = np.percentile(iqr_data, 25)


# Step 2: Calculate Q3

Q3 = np.percentile(iqr_data, 75)


# Step 3: Calculate IQR

IQR = Q3 - Q1


# Step 4: Calculate limits

ll = Q1 - (1.5 * IQR)

ul = Q3 + (1.5 * IQR)


print("Q1:", Q1)

print("Q3:", Q3)

print("IQR:", IQR)

print("Lower Limit:", ll)

print("Upper Limit:", ul)


# ============================================================
# 18. FIND OUTLIERS USING IQR
# ============================================================

outliers = iqr_data[
    (iqr_data < ll) |
    (iqr_data > ul)
]

print("IQR Outliers:", outliers)


# ============================================================
# 19. REMOVE OUTLIERS USING IQR
# ============================================================

removal = iqr_data[
    (iqr_data >= ll) &
    (iqr_data <= ul)
]

print("After Removal:", removal)


# ============================================================
# 20. CAP OUTLIERS USING IQR
# ============================================================

capped_data = np.clip(
    iqr_data,
    ll,
    ul
)

print("After Capping:", capped_data)


# ============================================================
# 21. VISUALIZE BEFORE AND AFTER REMOVAL
# ============================================================

sns.boxplot(x=iqr_data)

plt.title("Before Outlier Removal")

plt.show()


sns.boxplot(x=removal)

plt.title("After Outlier Removal")

plt.show()


# ============================================================
# 22. VISUALIZE AFTER CAPPING
# ============================================================

sns.boxplot(x=capped_data)

plt.title("After Outlier Capping")

plt.show()


# ============================================================
# 23. OUTLIER HANDLING USING PANDAS
# ============================================================

# Create a DataFrame.

df = pd.DataFrame({
    "salary": [
        25000,
        30000,
        35000,
        40000,
        45000,
        50000,
        55000,
        60000,
        500000
    ]
})

print(df)


# Calculate quartiles.

Q1 = df["salary"].quantile(0.25)

Q3 = df["salary"].quantile(0.75)


# Calculate IQR.

IQR = Q3 - Q1


# Calculate limits.

ll = Q1 - (1.5 * IQR)

ul = Q3 + (1.5 * IQR)


# Find outliers.

outliers = df[
    (df["salary"] < ll) |
    (df["salary"] > ul)
]

print("Outliers:")
print(outliers)


# Remove outliers.

clean_df = df[
    (df["salary"] >= ll) &
    (df["salary"] <= ul)
].copy()

print("Clean DataFrame:")
print(clean_df)


# Cap outliers.
#
# .clip() works with Pandas Series too.

df["capped_salary"] = df["salary"].clip(
    lower=ll,
    upper=ul
)

print("After Capping:")
print(df)


# ============================================================
# 24. INTERVIEW QUESTIONS AND ANSWERS
# ============================================================

# Q1. What is an outlier?
#
# Answer:
# An outlier is an observation unusually far away
# from the majority of the dataset.


# Q2. What is IQR?
#
# Answer:
# IQR stands for Interquartile Range.
#
# IQR = Q3 - Q1


# Q3. What is Q1?
#
# Answer:
# Q1 is the 25th percentile.


# Q4. What is Q3?
#
# Answer:
# Q3 is the 75th percentile.


# Q5. What is the IQR lower limit?
#
# Answer:
# Q1 - 1.5 * IQR


# Q6. What is the IQR upper limit?
#
# Answer:
# Q3 + 1.5 * IQR


# Q7. What is capping?
#
# Answer:
# Replacing extreme values with selected lower
# or upper boundary values.


# Q8. Difference between removal and capping?
#
# Removal:
# Deletes observations outside the selected limits.
#
# Capping:
# Keeps observations but replaces extreme values
# with boundary values.


# Q9. Which function is used for capping in NumPy?
#
# Answer:
# np.clip()


# Q10. Which function calculates percentiles?
#
# Answer:
# np.percentile()


# ============================================================
# END OF CHAPTER
# ============================================================
```

## 3. Important correction from your classroom screenshots

One screenshot shows the following removal logic:

Python

Run

```
removal = data[~(data < ll) & (data > ul)]
```

This is not the correct condition for retaining all non-outlier values.

Use:

Python

Run

```
removal = data[
    (data >= ll) & (data <= ul)
]
```

Or use the NOT operator on the entire outlier condition:

Python

Run

```
removal = data[
    ~((data < ll) | (data > ul))
]
```

Both retain values within the selected limits.

## 4. Outlier methods — Quick revision

|
Method

|

Formula / Function

|
| --- | --- |
|

Mean

|

`np.mean(data)`

|
|

Standard deviation

|

`np.std(data)`

|
|

Median

|

`np.median(data)`

|
|

Q1

|

`np.percentile(data, 25)`

|
|

Q3

|

`np.percentile(data, 75)`

|
|

IQR

|

`Q3 - Q1`

|
|

3-Sigma lower limit

|

`mean - 3 * std`

|
|

3-Sigma upper limit

|

`mean + 3 * std`

|
|

IQR lower limit

|

`Q1 - 1.5 * IQR`

|
|

IQR upper limit

|

`Q3 + 1.5 * IQR`

|
|

Capping

|

`np.clip(data, ll, ul)`

|

Important: The 3-sigma method can miss outliers in small, heavily skewed datasets because extreme observations influence the mean and standard deviation. IQR is often more robust for such data. Percentile trimming uses a chosen cutoff and may flag valid extreme observations, so select the method based on the dataset and business problem.
