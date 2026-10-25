# 📘 Data Preprocessing — Categorical Encoding

## 🎯 Learning Objectives

After completing this topic, you will understand:

- What data preprocessing is.
- What categorical data is.
- Why categorical encoding is required.
- Label Encoding.
- Binary Encoding for Yes/No values.
- Ordinal Encoding.
- One-Hot Encoding.
- The difference between encoding and scaling.
- How to implement categorical encoding using Python, Pandas, and Scikit-learn.

---

# 1. 🧠 What Is Data Preprocessing?

**Data preprocessing** is the process of preparing raw data before using it for data analysis or machine learning.

Real-world data may contain:

- Missing values.
- Duplicate records.
- Incorrect data types.
- Categorical values.
- Inconsistent formats.
- Numerical values with different scales.

We clean and transform the data to make it suitable for further analysis.

### Example

Original data:

| Name | Age | Gender | Salary |
|---|---:|---|---:|
| Ravi | 25 | Male | 30000 |
| Sita | 30 | Female | 45000 |
| Raju | 35 | Male | 50000 |

Here, `Age` and `Salary` are numerical columns, while `Name` and `Gender` are categorical columns.

Some machine learning algorithms require categorical information to be converted into a numerical representation.

This process is called **categorical encoding**.

---

# 2. 📊 What Is Categorical Data?

Categorical data represents groups, labels, or categories rather than numerical measurements.

For example:

```python
Gender = ["Male", "Female", "Male"]

Plan = ["Basic", "Standard", "Premium"]

Satisfaction = ["Low", "Medium", "High"]

Churn = ["Yes", "No", "Yes"]
```

These values describe categories.

## Types of Categorical Data

### A. Nominal Data

Nominal data contains categories without a natural order.

Examples:

- Gender
- City
- Country
- Product category
- Subscription plan

For example:

```text
Hyderabad
Chennai
Bengaluru
```

There is no natural ranking between these cities.

### B. Ordinal Data

Ordinal data contains categories with a meaningful order.

Examples:

```text
Low < Medium < High
```

Another example:

```text
Beginner < Intermediate < Advanced
```

The order carries information.

### C. Binary Categorical Data

Binary categorical data has two possible categories.

Examples:

```text
Yes / No
True / False
Active / Inactive
```

For example:

```python
Churn = ["No", "Yes", "No", "Yes"]
```

---

# 3. 🔄 What Is Categorical Encoding?

**Categorical encoding is the process of converting categorical values into a numerical representation.**

Machine learning algorithms often work with numerical features, so categorical data may need to be encoded before training a model.

### Before Encoding

| Gender | Plan |
|---|---|
| Male | Basic |
| Female | Premium |
| Male | Standard |

### After Encoding

| Gender | Plan_Basic | Plan_Premium | Plan_Standard |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 |

The categorical values have been converted into numbers.

There are several encoding techniques. We will learn three common approaches and a simple binary conversion.

---

# 4. 🏷️ Label Encoding

## What Is Label Encoding?

Label Encoding converts each distinct category into an integer.

For example:

```text
Female → 0
Male   → 1
```

### Python Code

```python
from sklearn.preprocessing import LabelEncoder

gender = ["Male", "Female", "Male", "Female"]

le = LabelEncoder()

encoded_gender = le.fit_transform(gender)

print(encoded_gender)
```

### Output

```text
[1 0 1 0]
```

### Explanation

**Step 1: Create the encoder**

```python
le = LabelEncoder()
```

Creates a LabelEncoder object.

**Step 2: Fit and transform the data**

```python
encoded_gender = le.fit_transform(gender)
```

- `fit()` learns the unique categories.
- `transform()` converts the categories into numbers.
- `fit_transform()` performs both operations.

For this example, the categories are sorted alphabetically:

```text
Female → 0
Male   → 1
```

**Step 3: Display the result**

```python
print(encoded_gender)
```

Displays the encoded array.

### When Should You Use Label Encoding?

LabelEncoder is commonly used to encode a classification target containing class labels.

For example:

```text
Spam     → 1
Not Spam → 0
```

However, applying arbitrary integer labels to nominal input features can introduce a misleading numerical order.

For nominal input features, One-Hot Encoding is often more appropriate.

---

# 5. 🔢 Binary Encoding for Yes/No Values

In your project, the `Churn` column contains two categories:

```text
Yes
No
```

We can manually convert them into binary values.

### Python Code

```python
churn = ["No", "No", "Yes", "Yes"]

encoded_churn = [
    1 if value == "Yes" else 0
    for value in churn
]

print(encoded_churn)
```

### Output

```text
[0, 0, 1, 1]
```

### Mapping

| Original Value | Encoded Value |
|---|---:|
| No | 0 |
| Yes | 1 |

### Understanding the Code

```python
1 if value == "Yes" else 0
```

This is a conditional expression.

It means:

- If the value is `"Yes"`, return `1`.
- Otherwise, return `0`.

In your original code:

```python
df['Churn'] = df['Churn'].apply(
    lambda x: 1 if x == 'Yes' else 0
)
```

The `apply()` method applies the conversion to every value in the `Churn` column.

The `lambda` expression defines the conversion rule.

### When Should You Use It?

This approach is useful for binary columns such as:

- Yes / No
- True / False
- Churn / No Churn
- Purchased / Not Purchased

Remember that `0` and `1` are chosen representations. Their meanings depend on your problem.

---

# 6. 📈 Ordinal Encoding

## What Is Ordinal Encoding?

Ordinal Encoding converts ordered categories into numbers while preserving their meaningful order.

For example:

```text
Low    → 0
Medium → 1
High   → 2
```

### Why Do We Need It?

Consider customer satisfaction data:

| Customer | Satisfaction |
|---|---|
| A | Low |
| B | Medium |
| C | High |

We know that:

```text
Low < Medium < High
```

Ordinal Encoding preserves this order.

### Python Code

```python
satisfaction = ["Low", "Medium", "High", "Medium"]

mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

encoded_satisfaction = [
    mapping[value]
    for value in satisfaction
]

print(encoded_satisfaction)
```

### Output

```text
[0, 1, 2, 1]
```

### Understanding the Code

First, we define a dictionary:

```python
mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}
```

Each category is associated with a number.

Next:

```python
mapping[value]
```

Looks up the number corresponding to each category.

Finally, the list comprehension creates the encoded list.

### Your Original Code

```python
df['Satisfaction'] = df['Satisfaction'].apply(
    lambda x: 0 if x == 'Low'
    else 1 if x == 'Medium'
    else 2
)
```

This code performs the same conversion for your DataFrame.

**Important:** The code assigns `2` to every value that is neither `"Low"` nor `"Medium"`. This works for your current data, but an explicit mapping is safer when unexpected values might appear.

### When Should You Use Ordinal Encoding?

Use it for ordered categories such as:

- Satisfaction: Low, Medium, High.
- Education: School, Bachelor's, Master's, Doctorate.
- Priority: Low, Medium, High, Critical.
- Experience: Beginner, Intermediate, Advanced.

Only assign numbers according to a meaningful order.

---

# 7. 🔘 One-Hot Encoding

## What Is One-Hot Encoding?

One-Hot Encoding creates a separate binary column for each category.

It is particularly useful for nominal categorical features that do not have a meaningful order.

### Original Data

| Plan |
|---|
| Basic |
| Standard |
| Premium |
| Basic |

### After One-Hot Encoding

| Plan_Basic | Plan_Premium | Plan_Standard |
|---:|---:|---:|
| 1 | 0 | 0 |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |

### How Does It Work?

For the `Plan` column, we have three unique categories:

```text
Basic
Premium
Standard
```

The encoder creates three columns.

**Plan_Basic**

```text
Basic → 1
Other plans → 0
```

**Plan_Premium**

```text
Premium → 1
Other plans → 0
```

**Plan_Standard**

```text
Standard → 1
Other plans → 0
```

Each row receives a `1` in the column matching its category and `0` in the remaining columns.

### Python Code

```python
import pandas as pd

df_plan = pd.DataFrame({
    "Plan": [
        "Basic",
        "Standard",
        "Premium",
        "Basic"
    ]
})

df_encoded = pd.get_dummies(
    df_plan,
    columns=["Plan"],
    dtype="int"
)

print(df_encoded)
```

### Output

```text
   Plan_Basic  Plan_Premium  Plan_Standard
0           1             0              0
1           0             0              1
2           0             1              0
3           1             0              0
```

### Understanding the Code

```python
pd.get_dummies()
```

Is a Pandas function that performs One-Hot Encoding.

```python
columns=["Plan"]
```

Specifies the column to encode.

```python
dtype="int"
```

Stores the binary values as integers (`0` and `1`).

### When Should You Use One-Hot Encoding?

Use it for nominal categories such as:

- City
- Country
- Product category
- Subscription plan
- Payment method

One-Hot Encoding can create many columns when a feature has numerous unique categories, so consider the number of categories before applying it.

---

# 8. 🧪 Understanding Your Complete Dataset

Your program creates a DataFrame with eight customer records.

```python
import pandas as pd

data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55],
    "Salary": [
        25000, 30000, 45000, 50000,
        60000, 75000, 90000, 120000
    ],
    "Monthly_Spend": [
        1000, 1500, 2000, 2500,
        3000, 4000, 5000, 15000
    ],
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

df = pd.DataFrame(data)

print(df.head())
```

### Understanding the Columns

| Column | Data Type | Meaning |
|---|---|---|
| Age | Numerical | Customer's age |
| Salary | Numerical | Customer's salary |
| Monthly_Spend | Numerical | Customer's monthly spending |
| Gender | Nominal categorical | Customer's gender category |
| Plan | Nominal categorical | Subscription plan |
| Satisfaction | Ordinal categorical | Customer satisfaction level |
| Churn | Binary categorical | Whether the customer left |

### What Is Churn?

In this example:

- `Yes` means the customer left the service.
- `No` means the customer did not leave the service.

This dataset could be used to explore customer behavior or build a customer churn prediction model.

However, eight rows are only enough for a small learning example, not for building a reliable predictive model.

---

# 9. ⚙️ Applying Multiple Encoding Techniques

Your code applies different transformations to different columns.

### Step 1: Encode Gender

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["Gender"] = le.fit_transform(df["Gender"])

print(dict(zip(le.classes_, le.transform(le.classes_))))
```

Expected mapping:

```text
Female → 0
Male   → 1
```

### Step 2: Encode Churn

```python
df["Churn"] = df["Churn"].apply(
    lambda x: 1 if x == "Yes" else 0
)
```

Mapping:

```text
No  → 0
Yes → 1
```

### Step 3: Encode Satisfaction

```python
satisfaction_mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

df["Satisfaction"] = df["Satisfaction"].map(
    satisfaction_mapping
)
```

Mapping:

```text
Low    → 0
Medium → 1
High   → 2
```

### Step 4: Encode Plan

```python
df_onehot = pd.get_dummies(
    df,
    columns=["Plan"],
    dtype="int"
)

print(df_onehot.head())
```

This creates:

```text
Plan_Basic
Plan_Premium
Plan_Standard
```

### Step 5: Display the Final DataFrame

```python
print(df_onehot)
```

The final DataFrame contains numerical columns and the new binary columns created from `Plan`.

**Important:** `df_onehot` is created from `df`. The original `df` still contains the unencoded `Plan` column, while its `Gender`, `Churn`, and `Satisfaction` columns have already been transformed.

---

# 10. 🔍 Difference Between Encoding Techniques

| Feature | Label Encoding | Binary Conversion | Ordinal Encoding | One-Hot Encoding |
|---|---|---|---|---|
| Main purpose | Assign integer labels | Convert two categories into 0/1 | Preserve category order | Create binary columns |
| Example | Class A → 0 | No → 0 | Low → 0 | Plan_Basic → 1 |
| Output | One integer per category | One binary value | One ordered integer | Multiple binary columns |
| Preserves order? | Not necessarily | Not applicable | Yes, if mapped correctly | Does not impose a numerical ranking |
| Typical use | Classification labels | Binary features or targets | Ordered categories | Nominal features |

### Which Technique Should You Choose?

| Data | Suitable Approach |
|---|---|
| Gender or city as an input feature | One-Hot Encoding is often suitable |
| Customer satisfaction | Ordinal Encoding |
| Churn: Yes/No | Binary conversion |
| Machine learning classification target | LabelEncoder can be appropriate |
| Subscription plan | One-Hot Encoding |

The best method depends on the meaning of the categories and the machine learning algorithm you plan to use.

---

# 11. 📏 Encoding vs Scaling

These are two different preprocessing operations.

## Encoding

Encoding converts categorical values into numerical representations.

Example:

```text
Male → 1
Female → 0
```

## Scaling

Scaling adjusts the numerical range of features.

For example, a dataset might contain:

```text
Age: 22 to 55
Salary: 25000 to 120000
```

The values have very different ranges.

A scaling method such as Min-Max Scaling can transform them into a range between `0` and `1`.

### Comparison

| Encoding | Scaling |
|---|---|
| Works primarily with categorical data | Works with numerical features |
| Converts categories into numerical representations | Adjusts numerical feature ranges |
| Example: Low → 0, Medium → 1, High → 2 | Example: Salary → value between 0 and 1 |
| Techniques: One-Hot, Ordinal | Techniques: Min-Max, Standardization |

**Remember:** Encoding and scaling solve different problems. Scaling is not automatically required for every machine learning algorithm.

---

# 12. 🛠️ Installing Required Libraries in VS Code

Open your VS Code terminal.

### Step 1: Create a Project Folder

```text
categorical-encoding/
```

### Step 2: Create a Virtual Environment

On Windows:

```bash
python -m venv .venv
```

### Step 3: Activate the Environment

Command Prompt:

```bash
.venv\Scripts\activate
```

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

```bash
python -m pip install pandas scikit-learn
```

### Step 5: Create a Python File

Create:

```text
categorical_encoding.py
```

Paste your Python program into this file.

### Step 6: Run the Program

```bash
python categorical_encoding.py
```

If your system uses the `py` launcher instead, you can run:

```bash
py categorical_encoding.py
```

Make sure VS Code is using the Python interpreter from your virtual environment.

---

# 13. 📂 Recommended Folder Structure

```text
categorical-encoding/
│
├── .venv/
│
├── categorical_encoding.py
│
├── README.md
│
└── requirements.txt
```

### requirements.txt

```text
pandas
scikit-learn
```

Install the packages listed in this file with:

```bash
python -m pip install -r requirements.txt
```

---

# 14. 📝 Practice Exercises

Try to solve these exercises yourself.

### Task 1: Label Encoding

Create a list:

```python
colors = ["Red", "Blue", "Green", "Red", "Blue"]
```

Use `LabelEncoder` to encode the colors.

**Expected result:** An array of integer labels.

The exact values depend on the sorted category names.

### Task 2: Binary Conversion

Create a list:

```python
purchase = ["Yes", "No", "Yes", "No", "Yes"]
```

Convert:

```text
Yes → 1
No  → 0
```

Expected output:

```text
[1, 0, 1, 0, 1]
```

### Task 3: Ordinal Encoding

Create a list:

```python
priority = [
    "Low",
    "High",
    "Medium",
    "Low",
    "High"
]
```

Use this mapping:

```text
Low    → 0
Medium → 1
High   → 2
```

Expected output:

```text
[0, 2, 1, 0, 2]
```

### Task 4: One-Hot Encoding

Create a DataFrame:

```python
df = pd.DataFrame({
    "Department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "HR"
    ]
})
```

Use `pd.get_dummies()` to encode `Department`.

Expected columns:

```text
Department_Finance
Department_HR
Department_IT
```

### Task 5: Combined Practice

Create a DataFrame containing:

- Age
- Salary
- Gender
- Education
- Purchased

Apply suitable encoding techniques to the categorical columns.

For `Education`, use an ordered mapping only if the categories have a meaningful order.

For `Purchased`, convert `Yes` and `No` into `1` and `0`.

---

# 15. 🎯 Interview Questions

### Q1. What is categorical encoding?

Categorical encoding converts categorical data into a numerical representation that can be used by suitable machine learning algorithms.

### Q2. What is Label Encoding?

Label Encoding assigns an integer to each unique category.

Example:

```text
Apple  → 0
Banana → 1
Mango  → 2
```

### Q3. What is Ordinal Encoding?

Ordinal Encoding assigns numbers to categories according to their meaningful order.

Example:

```text
Low → 0
Medium → 1
High → 2
```

### Q4. What is One-Hot Encoding?

One-Hot Encoding creates separate binary columns for the categories of a feature.

### Q5. Why do we encode categorical data?

Some machine learning algorithms require numerical input, so categorical information must be represented numerically before it can be used by those algorithms.

### Q6. What is the difference between nominal and ordinal data?

- Nominal data has no natural order.
- Ordinal data has a meaningful order.

### Q7. What is `pd.get_dummies()`?

It is a Pandas function that converts categorical columns into indicator columns.

### Q8. What does `fit_transform()` do?

It learns the category mapping from the supplied data and transforms the data using that mapping.

### Q9. Is Label Encoding suitable for every categorical feature?

No. Arbitrary integer labels can introduce a misleading order for nominal features. One-Hot Encoding is often a better choice for nominal input features.

### Q10. What is the difference between encoding and scaling?

Encoding represents categories numerically, while scaling adjusts the ranges of numerical features.

---

# 16. 🧠 Quick Revision

Remember these definitions:

**Data Preprocessing**

Preparing data before analysis or machine learning.

**Categorical Data**

Data representing groups or categories.

**Categorical Encoding**

Converting categorical data into a numerical representation.

**Label Encoding**

Assigning integer labels to categories.

**Binary Conversion**

Representing two categories using values such as `0` and `1`.

**Ordinal Encoding**

Converting ordered categories into numbers while preserving their order.

**One-Hot Encoding**

Creating separate binary columns for categories.

**Scaling**

Adjusting the numerical ranges of features.

---

# ✅ Final Summary

In this lesson, you learned how to transform categorical columns in a customer dataset.

| Column | Original Data | Transformation |
|---|---|---|
| Gender | Male / Female | Label Encoding |
| Churn | Yes / No | Binary Conversion |
| Satisfaction | Low / Medium / High | Ordinal Encoding |
| Plan | Basic / Standard / Premium | One-Hot Encoding |
| Age | Numerical | No encoding needed |
| Salary | Numerical | No encoding needed |
| Monthly_Spend | Numerical | No encoding needed |

**Your main takeaway:**

Choose an encoding technique based on the meaning of the categories, not just because a column contains text.

You are now ready to practise categorical encoding in Python using Pandas and Scikit-learn.