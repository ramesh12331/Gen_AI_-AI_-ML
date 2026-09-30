# 📊 Employee Data Analysis — EDA with Pandas & Seaborn

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on an employee dataset using:

- 🐼 Pandas
- 📊 Matplotlib
- 🎨 Seaborn
- 🐍 Python

The main goal is to understand the employee data using:

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Numerical Analysis
- Categorical Analysis
- Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Feature Selection

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data manipulation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |

---

# 📁 Dataset

The dataset contains information about 20 employees.

### Columns

| Column | Type | Description |
|---|---|---|
| Employee_ID | Numerical | Unique employee ID |
| Age | Numerical | Employee age |
| Gender | Categorical | Male / Female |
| Department | Categorical | IT / HR / Finance / Sales |
| Experience | Numerical | Years of experience |
| Salary | Numerical | Employee salary |
| Performance | Numerical | Performance score |
| Work_Mode | Categorical | Remote / Office / Hybrid |
| City | Categorical | Employee city |
| Joining_Month | Categorical | Month employee joined |

---

# 1️⃣ Import Pandas

```python
import pandas as pd

Sure. Below is a **complete README.md** for your Pandas + Seaborn **EDA (Exploratory Data Analysis)** practice project, including the concepts, code, and insights from your dataset.

````markdown
# 📊 Employee Data Analysis — EDA with Pandas & Seaborn

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on an employee dataset using:

- 🐼 Pandas
- 📊 Matplotlib
- 🎨 Seaborn
- 🐍 Python

The main goal is to understand the employee data using:

- Univariate Analysis
- Bivariate Analysis
- Multivariate Analysis
- Numerical Analysis
- Categorical Analysis
- Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Feature Selection

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data manipulation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |

---

# 📁 Dataset

The dataset contains information about 20 employees.

### Columns

| Column | Type | Description |
|---|---|---|
| Employee_ID | Numerical | Unique employee ID |
| Age | Numerical | Employee age |
| Gender | Categorical | Male / Female |
| Department | Categorical | IT / HR / Finance / Sales |
| Experience | Numerical | Years of experience |
| Salary | Numerical | Employee salary |
| Performance | Numerical | Performance score |
| Work_Mode | Categorical | Remote / Office / Hybrid |
| City | Categorical | Employee city |
| Joining_Month | Categorical | Month employee joined |

---

# 1️⃣ Import Pandas

```python
import pandas as pd
````

Pandas is mainly used for:

* Creating DataFrames
* Data cleaning
* Data filtering
* Data analysis
* Data manipulation

---

# 2️⃣ Create the Dataset

```python
data = {
    "Employee_ID": range(101, 121),

    "Age": [
        22, 25, 28, 30, 24,
        27, 32, 29, 35, 26,
        31, 23, 38, 34, 28,
        25, 40, 33, 29, 36
    ],

    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],

    "Department": [
        "IT", "HR", "Finance", "IT", "Sales",
        "IT", "Finance", "HR", "IT", "Sales",
        "IT", "Finance", "Sales", "IT", "HR",
        "Finance", "IT", "Sales", "HR", "IT"
    ],

    "Experience": [
        1, 2, 4, 6, 2,
        3, 8, 5, 10, 3,
        7, 1, 12, 9, 4,
        2, 11, 6, 5, 13
    ],

    "Salary": [
        28000, 320000, 45000, 60000, 35000,
        42000, 75000, 52000, 95000, 40000,
        68000, 30000, 110000, 85000, 48000,
        36000, 100000, 62000, 55000, 120000
    ],

    "Performance": [
        65, 72, 80, 88, 70,
        78, 91, 85, 95, 74,
        89, 68, 96, 92, 81,
        73, 94, 87, 83, 97
    ],

    "Work_Mode": [
        "Remote", "Office", "Hybrid", "Remote", "Office",
        "Hybrid", "Remote", "Office", "Hybrid", "Remote",
        "Office", "Hybrid", "Remote", "Office", "Hybrid",
        "Remote", "Office", "Hybrid", "Remote", "Office"
    ],

    "City": [
        "Hyderabad", "Bangalore", "Chennai", "Hyderabad", "Pune",
        "Bangalore", "Hyderabad", "Chennai", "Bangalore", "Pune",
        "Hyderabad", "Chennai", "Bangalore", "Hyderabad", "Pune",
        "Bangalore", "Hyderabad", "Chennai", "Bangalore", "Pune"
    ],

    "Joining_Month": [
        "Jan", "Feb", "Mar", "Apr", "May",
        "Jun", "Jul", "Aug", "Sep", "Oct",
        "Nov", "Dec", "Jan", "Feb", "Mar",
        "Apr", "May", "Jun", "Jul", "Aug"
    ]
}

df = pd.DataFrame(data)
```

---

# 3️⃣ View the Dataset

```python
df.head()
```

### Purpose

`head()` displays the first 5 rows.

```python
df.head(10)
```

Displays the first 10 rows.

---

# 4️⃣ Identify Categorical Columns

```python
df.select_dtypes(include='object').columns
```

### Output

```text
Index([
    'Gender',
    'Department',
    'Work_Mode',
    'City',
    'Joining_Month'
], dtype='object')
```

### What are categorical columns?

Categorical columns contain **categories or labels**.

Examples:

```text
Gender
Department
City
Work_Mode
Joining_Month
```

---

# 5️⃣ Identify Numerical Columns

```python
df.select_dtypes(include='number').columns
```

### Output

```text
Employee_ID
Age
Experience
Salary
Performance
```

Numerical columns contain numeric values.

---

# 📊 Exploratory Data Analysis

EDA means:

> **Exploratory Data Analysis is the process of understanding a dataset using statistics and visualizations.**

EDA is generally divided into:

```text
EDA
│
├── Univariate Analysis
│
├── Bivariate Analysis
│
└── Multivariate Analysis
```

---

# 6️⃣ Univariate Analysis

## Definition

Univariate analysis means analyzing **one variable at a time**.

Example:

```text
Salary
```

We study:

* Distribution
* Mean
* Median
* Outliers
* Frequency

---

# 📈 Histogram

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(
    x='Salary',
    data=df,
    kde=True
)

plt.show()
```

### What does a histogram show?

A histogram shows the **distribution of numerical data**.

For example:

```text
Salary Distribution
        █
        █
    █   █
    █   █
█   █   █
█   █ █ █
----------------
 Salary
```

### Insight

The salary distribution can be examined to identify:

* Common salary ranges
* Skewness
* Unusual values
* Possible outliers

---

# 📉 KDE Plot

```python
sns.kdeplot(
    x='Salary',
    data=df,
    fill=True,
    color='red'
)

plt.show()
```

KDE = **Kernel Density Estimate**

It represents the probability density of a numerical variable.

### Simple difference

| Plot      | Purpose                         |
| --------- | ------------------------------- |
| Histogram | Shows frequency                 |
| KDE       | Shows smooth distribution curve |

---

# 📦 Box Plot

```python
sns.boxplot(
    x='Salary',
    data=df
)

plt.show()
```

Box plots are useful for identifying:

* Median
* Quartiles
* Spread
* Outliers

### Box plot structure

```text
        Outlier
           *
           |
---|=======|=======|---
   Q1     Median   Q3
```

---

# 📊 Histograms for All Numerical Columns

```python
for col in df.select_dtypes(include='number').columns:

    sns.histplot(
        x=col,
        data=df,
        kde=True
    )

    plt.show()
```

This automatically creates a histogram for every numerical column.

---

# 🏷️ Univariate Categorical Analysis

Categorical variables can be analyzed using a **count plot**.

```python
sns.countplot(
    x='Department',
    data=df
)

plt.show()
```

A count plot shows the number of observations in each category.

---

# 🎨 Count Plot with Colors

```python
colors = ['red', 'black', 'green', 'yellow']

sns.countplot(
    x='Department',
    data=df,
    palette=colors
)

plt.show()
```

> Note: In newer Seaborn versions, `palette` may require a `hue` assignment depending on the version. For a simple single-color count plot, use `color=`.

---

# 7️⃣ Bivariate Analysis

## Definition

Bivariate analysis means analyzing **two variables together**.

Examples:

```text
City vs Salary
Experience vs Salary
Department vs Salary
```

---

# 📊 Categorical vs Numerical

## City vs Salary

```python
sns.barplot(
    x='City',
    y='Salary',
    data=df,
    estimator='mean'
)

plt.show()
```

### What does this show?

It calculates the **average salary for each city**.

Example:

```text
Hyderabad → Average Salary
Bangalore → Average Salary
Chennai   → Average Salary
Pune      → Average Salary
```

---

# 👥 City vs Salary by Gender

```python
sns.barplot(
    x='City',
    y='Salary',
    data=df,
    estimator='mean',
    hue='Gender'
)

plt.show()
```

This becomes a **multivariate analysis** because we are considering:

```text
City
Salary
Gender
```

---

# 🔵 Numerical vs Numerical

## Experience vs Salary

```python
sns.scatterplot(
    x='Experience',
    y='Salary',
    data=df
)

plt.show()
```

A scatter plot helps identify relationships between two numerical variables.

### Possible question

> Does salary increase as experience increases?

The scatter plot helps us visually investigate this relationship.

---

# 📈 Experience vs Performance

```python
sns.scatterplot(
    x='Experience',
    y='Performance',
    data=df
)

plt.show()
```

This helps examine whether experience and performance appear to have a relationship.

---

# 📈 Regression Plot

```python
sns.regplot(
    x='Experience',
    y='Performance',
    data=df
)

plt.show()
```

A regression plot contains:

```text
Scatter points
      +
Regression line
```

It helps visualize the general trend between two numerical variables.

---

# 8️⃣ Numerical vs Categorical

## Department vs Salary

```python
sns.boxplot(
    x='Department',
    y='Salary',
    data=df
)

plt.show()
```

This helps compare salary distributions across departments.

---

# 🎻 Violin Plot

```python
sns.violinplot(
    x='Department',
    y='Salary',
    data=df
)

plt.show()
```

A violin plot combines information about:

* Distribution
* Density
* Median
* Spread

It is useful when comparing numerical distributions across categories.

---

# 9️⃣ Multivariate Analysis

## Definition

Multivariate analysis means analyzing **three or more variables simultaneously**.

Example:

```text
Experience
Salary
Gender
Performance
```

---

# 🔵 Scatter Plot with Multiple Variables

```python
sns.scatterplot(
    data=df,
    x='Experience',
    y='Salary',
    hue='Gender',
    size='Performance'
)

plt.legend(loc='upper right')

plt.show()
```

Here:

| Visual Property | Variable    |
| --------------- | ----------- |
| X-axis          | Experience  |
| Y-axis          | Salary      |
| Color           | Gender      |
| Size            | Performance |

This allows us to analyze multiple variables in one visualization.

---

# 🔟 Pair Plot

```python
sns.pairplot(
    df[
        [
            'Age',
            'Experience',
            'Salary',
            'Performance',
            'Gender'
        ]
    ],
    hue='Gender'
)

plt.show()
```

A pair plot creates multiple plots between numerical variables.

It can help identify:

* Relationships
* Trends
* Distributions
* Possible correlations
* Group differences

---

# 🔗 Correlation Analysis

Correlation measures the relationship between numerical variables.

First calculate correlation:

```python
corr = df.select_dtypes(
    include='number'
).corr()

print(corr)
```

---

# 🔥 Correlation Heatmap

```python
sns.heatmap(
    corr,
    annot=True
)

plt.show()
```

### What does correlation mean?

Correlation values range from:

```text
-1 → 0 → +1
```

| Value | Meaning                       |
| ----: | ----------------------------- |
|    +1 | Perfect positive relationship |
|  +0.7 | Strong positive relationship  |
|  +0.3 | Weak positive relationship    |
|     0 | No linear relationship        |
|  -0.3 | Weak negative relationship    |
|  -0.7 | Strong negative relationship  |
|    -1 | Perfect negative relationship |

---

# 📌 Positive Correlation

Example:

```text
Experience ↑
     ↓
Salary ↑
```

If experience increases and salary also tends to increase, they have a positive correlation.

---

# 📌 Negative Correlation

Example:

```text
X ↑
Y ↓
```

If one variable increases while another decreases, they have a negative correlation.

---

# ⚠️ Important: Correlation ≠ Causation

A high correlation does **not automatically mean** that one variable causes another.

For example:

```text
Experience ↔ Salary
```

A strong correlation may exist, but additional analysis is required before making causal claims.

---

# 🚨 Why Remove Highly Correlated Features?

Suppose we have:

```text
Feature A
Feature B
```

and:

```text
Correlation = 0.95
```

These features contain very similar information.

Keeping both may cause problems for some machine-learning models.

This issue is commonly called:

## Multicollinearity

---

# 🎯 Feature Selection

Feature selection means choosing the most useful features for a machine-learning model.

Example:

```text
Age
Experience
Salary
Performance
```

We may remove redundant features when they provide overlapping information.

Common approaches include:

```text
Feature Selection
│
├── Correlation Analysis
├── Statistical Tests
├── Recursive Feature Elimination
├── Feature Importance
└── Domain Knowledge
```

---

# 🧠 Curse of Dimensionality

The **curse of dimensionality** occurs when the number of features/dimensions becomes very large.

More features can cause:

* More computational cost
* Sparse data
* Difficulty finding meaningful patterns
* Higher risk of overfitting in some situations

However:

> Having two highly correlated columns alone is not the same thing as the curse of dimensionality.

Highly correlated features are more directly related to **redundancy and multicollinearity**.

---

# 🔧 PCA

PCA = **Principal Component Analysis**

PCA is a dimensionality-reduction technique.

It transforms many correlated features into a smaller number of new components.

Example:

```text
Feature 1 ─┐
Feature 2 ─┤
Feature 3 ─┼──→ PCA ──→ PC1
Feature 4 ─┤          └→ PC2
Feature 5 ─┘
```

The goal is to preserve as much of the important variation in the data as possible using fewer dimensions.

---

# 🔬 LDA

LDA = **Linear Discriminant Analysis**

LDA can be used for:

* Dimensionality reduction
* Classification-related feature transformation

Unlike PCA, which focuses on preserving variance, LDA uses class information to find directions that help separate classes.

---

# 🆚 PCA vs LDA

| PCA                                 | LDA                                                        |
| ----------------------------------- | ---------------------------------------------------------- |
| Unsupervised                        | Supervised                                                 |
| Does not require target classes     | Uses class labels                                          |
| Maximizes variance                  | Maximizes class separability                               |
| Useful for dimensionality reduction | Useful for classification-related dimensionality reduction |

---

# 📚 EDA Workflow

A common EDA workflow is:

```text
Load Data
    ↓
Understand Data
    ↓
Check Data Types
    ↓
Check Missing Values
    ↓
Check Duplicates
    ↓
Univariate Analysis
    ↓
Bivariate Analysis
    ↓
Multivariate Analysis
    ↓
Outlier Detection
    ↓
Correlation Analysis
    ↓
Feature Selection
    ↓
Prepare Data for ML
```

---

# 🧪 Useful Commands

## Shape

```python
df.shape
```

Returns:

```text
(rows, columns)
```

---

## Data Types

```python
df.dtypes
```

---

## Dataset Information

```python
df.info()
```

---

## Statistical Summary

```python
df.describe()
```

---

## Missing Values

```python
df.isnull().sum()
```

---

## Duplicate Rows

```python
df.duplicated().sum()
```

---

## Unique Values

```python
df['Department'].unique()
```

---

## Number of Unique Values

```python
df['Department'].nunique()
```

---

# ⚠️ Data Quality Observation

This practice dataset contains a salary value of:

```text
320000
```

while most other salaries are much lower.

This may be an intentional outlier for EDA practice, or it may represent a data-entry issue.

Always investigate unusual values before automatically removing them.

---

# 📊 Analysis Types Summary

| Analysis     | Variables | Common Plots                                 |
| ------------ | --------- | -------------------------------------------- |
| Univariate   | 1         | Histogram, KDE, Boxplot, Countplot           |
| Bivariate    | 2         | Scatterplot, Barplot, Boxplot                |
| Multivariate | 3+        | Pairplot, Heatmap, Scatterplot with hue/size |

---

# 🎯 Main Learning Outcomes

After completing this project, you should understand:

* How to identify numerical columns
* How to identify categorical columns
* How to perform univariate analysis
* How to perform bivariate analysis
* How to perform multivariate analysis
* How to create histograms
* How to create KDE plots
* How to identify outliers using boxplots
* How to compare categories using barplots
* How to analyze numerical relationships using scatterplots
* How to use regression plots
* How to create violin plots
* How to create pair plots
* How to calculate correlation
* How to create correlation heatmaps
* What multicollinearity means
* What feature selection means
* What PCA and LDA are
* What the curse of dimensionality means

---

# 🚀 Next Steps

After completing this EDA project, continue with:

```text
EDA
 ↓
Data Cleaning
 ↓
Outlier Treatment
 ↓
Encoding
 ↓
Feature Engineering
 ↓
Feature Selection
 ↓
Scaling
 ↓
Train/Test Split
 ↓
Machine Learning
```

---

# 👨‍💻 Author

**Ramesh**

Learning:

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Data Analysis
* Data Science
* Machine Learning

---

# ⭐ Conclusion

This project demonstrates how **Pandas, Matplotlib, and Seaborn** can be used to explore an employee dataset.

EDA is an important step before machine learning because it helps us understand:

```text
What data do we have?
        ↓
What patterns exist?
        ↓
Are there outliers?
        ↓
Are variables related?
        ↓
Are there redundant features?
        ↓
Can we prepare the data for ML?
```

EDA helps convert raw data into useful information for further analysis and machine-learning workflows.

````

### One important correction in your code

You currently have:

```python
corr

sns.heatmap(corr, annot=True)
````

You need to **create `corr` first**:

```python
corr = df.select_dtypes(include='number').corr()

sns.heatmap(corr, annot=True)
plt.show()
```

Also, your comment:

```python
# curse of dimensionality: where it leads to overfitting of models
```

is better understood as **high dimensionality can make models harder to train and can contribute to overfitting**, while highly correlated columns specifically relate more directly to **multicollinearity/redundancy**.
