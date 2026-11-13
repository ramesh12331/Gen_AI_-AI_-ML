# 📊 Multiple Linear Regression — Student Final Marks Prediction

> 🎯 **Goal:** Predict a student's final marks using multiple input features such as **Study Hours, Attendance, and Previous Marks**.

---

# 📚 Table of Contents

1. [What is Multiple Linear Regression?](#1-what-is-multiple-linear-regression)
2. [Real-World Example](#2-real-world-example)
3. [Simple vs Multiple Linear Regression](#3-simple-vs-multiple-linear-regression)
4. [Dataset](#4-dataset)
5. [Input Features and Target](#5-input-features-and-target)
6. [Multiple Linear Regression Formula](#6-multiple-linear-regression-formula)
7. [Project Workflow](#7-project-workflow)
8. [Step-by-Step Code Explanation](#8-step-by-step-code-explanation)
9. [Complete Dry Run](#9-complete-dry-run)
10. [Understanding Coefficients](#10-understanding-coefficients)
11. [Understanding Intercept](#11-understanding-intercept)
12. [Prediction for a New Student](#12-prediction-for-a-new-student)
13. [MSE](#13-mean-squared-error-mse)
14. [R² Score](#14-r2-score)
15. [Cross Validation](#15-cross-validation)
16. [Actual vs Predicted Graph](#16-actual-vs-predicted-graph)
17. [Important Concepts](#17-important-concepts)
18. [Interview Questions](#18-interview-questions)
19. [Final Revision](#19-final-revision)

---

# 1. What is Multiple Linear Regression?

**Multiple Linear Regression (MLR)** is a supervised Machine Learning algorithm used to predict a **continuous numerical value** using **two or more independent variables**.

### Example

We want to predict:

```text
Final Marks
```

Using:

```text
Study Hours
Attendance
Previous Marks
```

So:

```text
Study Hours ──────┐
Attendance ──────┼──> Multiple Linear Regression ──> Final Marks
Previous Marks ───┘
```

### Simple meaning

> Multiple Linear Regression finds the mathematical relationship between **multiple input variables** and **one numerical output**.

---

# 2. Real-World Example

Suppose we have information about students:

| Study Hours | Attendance | Previous Marks | Final Marks |
|---:|---:|---:|---:|
| 2 | 70 | 55 | 60 |
| 4 | 80 | 65 | 70 |
| 6 | 85 | 75 | 80 |
| 8 | 90 | 85 | 92 |

We want the model to learn:

```text
Study Hours
     +
Attendance
     +
Previous Marks
     ↓
Final Marks
```

After training, we can give a new student:

```text
Study Hours = 6.5
Attendance = 85
Previous Marks = 75
```

and ask:

```text
What will be the predicted Final Marks?
```

---

# 3. Simple vs Multiple Linear Regression

## 🟢 Simple Linear Regression

Uses **one independent variable**.

Example:

```text
Study Hours → Marks
```

Formula:

$$
y = b_0 + b_1x
$$

---

## 🔵 Multiple Linear Regression

Uses **two or more independent variables**.

Example:

```text
Study Hours ──────┐
Attendance ──────┼──> Final Marks
Previous Marks ───┘
```

Formula:

$$
y = b_0 + b_1x_1 + b_2x_2 + b_3x_3
$$

---

# 4. Dataset

Our project uses:

```text
student_marks_2000.csv
```

The dataset contains:

```text
Study_Hours
Attendance
Previous_Marks
Final_Marks
```

### Meaning of columns

| Column | Type | Meaning |
|---|---|---|
| Study_Hours | Input | Number of hours student studied |
| Attendance | Input | Attendance percentage |
| Previous_Marks | Input | Marks from previous examination |
| Final_Marks | Target | Final examination marks |

---

# 5. Input Features and Target

Machine Learning normally separates the data into:

```text
X = Input Features
y = Target
```

### Our project

```text
X =
Study_Hours
Attendance
Previous_Marks
```

and:

```text
y =
Final_Marks
```

### Code

```python
X = df.drop(columns="Final_Marks")

y = df["Final_Marks"]
```

### Why?

Because we want to predict:

```text
Final_Marks
```

Therefore, `Final_Marks` should not be given to the model as an input feature.

---

# 6. Multiple Linear Regression Formula

The general formula is:

$$
y = b_0 + b_1x_1 + b_2x_2 + ... + b_kx_k
$$

For our project:

$$
Final\_Marks =
b_0
+
b_1(Study\_Hours)
+
b_2(Attendance)
+
b_3(Previous\_Marks)
$$

### Meaning of each term

| Symbol | Meaning |
|---|---|
| $y$ | Predicted target |
| $b_0$ | Intercept |
| $b_1$ | Study Hours coefficient |
| $b_2$ | Attendance coefficient |
| $b_3$ | Previous Marks coefficient |
| $x_1$ | Study Hours |
| $x_2$ | Attendance |
| $x_3$ | Previous Marks |

---

# 7. Project Workflow

The complete Machine Learning workflow is:

```text
CSV Dataset
     ↓
Load Dataset
     ↓
Separate X and y
     ↓
Train/Test Split
     ↓
Create Linear Regression Model
     ↓
Train Model
     ↓
Learn Coefficients
     ↓
Make Predictions
     ↓
Evaluate Model
     ↓
Cross Validation
     ↓
Visualize Results
```

---

# 8. Step-by-Step Code Explanation

## STEP 1 — Import Libraries

```python
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
```

### Why do we need them?

### Pandas

```python
import pandas as pd
```

Used for:

- Reading CSV
- Creating DataFrames
- Manipulating data

---

### train_test_split

```python
from sklearn.model_selection import train_test_split
```

Used to divide data into:

```text
Training Data
Testing Data
```

---

### cross_val_score

```python
from sklearn.model_selection import cross_val_score
```

Used for:

```text
Cross Validation
```

---

### LinearRegression

```python
from sklearn.linear_model import LinearRegression
```

This is the algorithm used to create our regression model.

---

### Metrics

```python
from sklearn.metrics import mean_squared_error, r2_score
```

Used to calculate:

```text
MSE
R² Score
```

---

### Matplotlib

```python
import matplotlib.pyplot as plt
```

Used to create graphs.

---

# STEP 2 — Load Dataset

```python
df = pd.read_csv("student_marks_2000.csv")
```

This reads the CSV file.

The result is stored in:

```text
df
```

Here:

```text
df = DataFrame
```

A DataFrame looks like a table:

| Study_Hours | Attendance | Previous_Marks | Final_Marks |
|---:|---:|---:|---:|
| 2 | 70 | 55 | 60 |
| 4 | 80 | 65 | 70 |
| 6 | 85 | 75 | 80 |

---

# STEP 3 — View First 5 Rows

```python
print(df.head())
```

`head()` displays the first 5 rows.

Example:

```text
   Study_Hours  Attendance  Previous_Marks  Final_Marks
0            2          70              55           60
1            4          80              65           70
2            6          85              75           80
3            8          90              85           92
```

---

# STEP 4 — Separate X and y

```python
X = df.drop(columns="Final_Marks")

y = df["Final_Marks"]
```

### X

```text
X = Study_Hours
    Attendance
    Previous_Marks
```

### y

```text
y = Final_Marks
```

Think:

```text
X → Questions / Inputs

y → Answer / Target
```

---

# STEP 5 — Train/Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
```

Here:

```text
test_size = 0.2
```

means:

```text
80% → Training
20% → Testing
```

If the dataset contains **2000 rows**:

```text
2000 × 80% = 1600 training rows

2000 × 20% = 400 testing rows
```

So approximately:

```text
2000 rows
    ↓
┌───────────────┬──────────────┐
│ Training 80%  │ Testing 20%  │
│ 1600 rows     │ 400 rows     │
└───────────────┴──────────────┘
```

---

# STEP 6 — Create Model

```python
mlr = LinearRegression()
```

Here:

```text
mlr
```

is our Multiple Linear Regression model.

At this point:

```text
Model created
```

but it has **not learned anything yet**.

---

# STEP 7 — Train the Model

```python
mlr.fit(X_train, y_train)
```

This is one of the most important lines.

`fit()` means:

> Train the model using the training data.

The model looks at:

```text
Study_Hours
Attendance
Previous_Marks
```

and learns how they are related to:

```text
Final_Marks
```

Conceptually:

```text
X_train + y_train
       ↓
     fit()
       ↓
Model learns coefficients
```

---

# STEP 8 — Make Predictions

```python
y_pred = mlr.predict(X_test)
```

The trained model now receives:

```text
X_test
```

and produces:

```text
Predicted Final Marks
```

So:

```text
X_test
   ↓
trained model
   ↓
y_pred
```

---

# STEP 9 — Compare Actual and Predicted Values

```python
print(y_test.head())
print(y_pred[:5])
```

Example:

```text
Actual:
[82, 74, 91, 65, 78]

Predicted:
[81.5, 75.2, 89.8, 66.1, 77.4]
```

The model is trying to make:

```text
Predicted ≈ Actual
```

---

# STEP 10 — Coefficients

```python
print(mlr.coef_)
```

Suppose the model produces:

```text
[2.5, 0.3, 0.6]
```

Then:

```text
Study_Hours coefficient = 2.5

Attendance coefficient = 0.3

Previous_Marks coefficient = 0.6
```

These numbers tell us how each feature contributes to the prediction **while holding the other included features constant**.

---

# STEP 11 — Intercept

```python
print(mlr.intercept_)
```

Suppose:

```text
Intercept = 10
```

Then the equation starts with:

```text
Final_Marks = 10 + ...
```

---

# STEP 12 — Regression Equation

The code creates:

```python
print(
    f"Final_Marks = "
    f"{mlr.intercept_:.4f} + "
    f"{mlr.coef_[0]:.4f} × Study_Hours + "
    f"{mlr.coef_[1]:.4f} × Attendance + "
    f"{mlr.coef_[2]:.4f} × Previous_Marks"
)
```

Suppose:

```text
Intercept = 10
Study_Hours coefficient = 2.5
Attendance coefficient = 0.3
Previous_Marks coefficient = 0.6
```

The equation becomes:

$$
Final\_Marks =
10
+
2.5(Study\_Hours)
+
0.3(Attendance)
+
0.6(Previous\_Marks)
$$

This is the mathematical model learned from the training data.

---

# 9. Complete Dry Run

Let's understand the complete program using a small example.

Suppose we have:

| Student | Study Hours | Attendance | Previous Marks | Final Marks |
|---|---:|---:|---:|---:|
| A | 2 | 70 | 55 | 60 |
| B | 4 | 80 | 65 | 70 |
| C | 6 | 85 | 75 | 80 |
| D | 8 | 90 | 85 | 92 |
| E | 5 | 75 | 70 | 76 |

---

## 🔹 Dry Run — Step 1

Read CSV:

```python
df = pd.read_csv("student_marks_2000.csv")
```

Python creates:

```text
df
```

containing the complete dataset.

---

## 🔹 Dry Run — Step 2

Execute:

```python
X = df.drop(columns="Final_Marks")
```

So:

```text
X
```

contains:

```text
Study_Hours
Attendance
Previous_Marks
```

---

## 🔹 Dry Run — Step 3

Execute:

```python
y = df["Final_Marks"]
```

So:

```text
y
```

contains:

```text
Final_Marks
```

---

## 🔹 Dry Run — Step 4

Split:

```python
test_size=0.2
```

For 2000 records:

```text
Training = 1600
Testing  = 400
```

---

## 🔹 Dry Run — Step 5

Create model:

```python
mlr = LinearRegression()
```

Model exists, but has not learned yet.

---

## 🔹 Dry Run — Step 6

Train:

```python
mlr.fit(X_train, y_train)
```

The model learns:

```text
Intercept
Coefficient 1
Coefficient 2
Coefficient 3
```

For example:

```text
b0 = 10
b1 = 2.5
b2 = 0.3
b3 = 0.6
```

These numbers are only an **illustration**; your actual values come from `student_marks_2000.csv`.

---

## 🔹 Dry Run — Step 7

The model equation becomes:

$$
Final\_Marks =
10
+
2.5(Study\_Hours)
+
0.3(Attendance)
+
0.6(Previous\_Marks)
$$

---

# 10. Understanding Coefficients

Suppose:

```text
Study_Hours coefficient = 2.5
```

Interpretation:

> If Study Hours increases by 1 unit, predicted Final Marks increase by about 2.5 marks, assuming the other features remain constant.

---

Suppose:

```text
Attendance coefficient = 0.3
```

Interpretation:

> If Attendance increases by 1 percentage point, predicted Final Marks increase by about 0.3 marks, assuming the other features remain constant.

---

Suppose:

```text
Previous_Marks coefficient = 0.6
```

Interpretation:

> If Previous Marks increases by 1 mark, predicted Final Marks increase by about 0.6 marks, assuming the other features remain constant.

---

## ⚠️ Important

Do not interpret coefficients without considering:

- feature units
- feature scale
- relationships between features
- multicollinearity
- the data-generating context

A larger coefficient does **not automatically mean** that feature is more important.

---

# 11. Understanding Intercept

Suppose:

```text
Intercept = 10
```

Then:

$$
Final\_Marks =
10
+
...
$$

The intercept is the model's predicted target when all input features are zero.

In real-world datasets, this value may not always have a meaningful practical interpretation.

---

# 12. Prediction for a New Student

The code creates:

```python
new_student = pd.DataFrame({
    "Study_Hours": [6.5],
    "Attendance": [85],
    "Previous_Marks": [75]
})
```

The student has:

```text
Study Hours    = 6.5
Attendance     = 85
Previous Marks = 75
```

Then:

```python
prediction = mlr.predict(new_student)
```

The model calculates:

$$
Final\_Marks =
b_0
+
b_1(6.5)
+
b_2(85)
+
b_3(75)
$$

The result is the predicted Final Marks.

---

# 13. Mean Squared Error — MSE

The code:

```python
mse = mean_squared_error(y_test, y_pred)
```

calculates:

```text
Mean Squared Error
```

Formula:

$$
MSE =
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
$$

Where:

| Symbol | Meaning |
|---|---|
| $n$ | Number of test observations |
| $y_i$ | Actual value |
| $\hat{y}_i$ | Predicted value |
| $y_i-\hat{y}_i$ | Error |
| $(y_i-\hat{y}_i)^2$ | Squared error |

---

## Example

Suppose:

```text
Actual     = 80
Predicted  = 75
```

Error:

$$
80-75=5
$$

Squared error:

$$
5^2=25
$$

MSE calculates the average of these squared errors across all test records.

### Important

```text
Lower MSE → Better
Higher MSE → Worse
```

But MSE is expressed in **squared target units**, so it can be harder to interpret directly.

---

# 14. R² Score

The code:

```python
r2 = r2_score(y_test, y_pred)
```

calculates the:

```text
R² Score
```

Formula:

$$
R^2 =
1-
\frac{SS_{res}}{SS_{tot}}
$$

Where:

# 📊 Multiple Linear Regression — Student Final Marks Prediction

> 🎯 **Goal:** Predict a student's final marks using multiple input features such as **Study Hours, Attendance, and Previous Marks**.

---

# 📚 Table of Contents

1. [What is Multiple Linear Regression?](#1-what-is-multiple-linear-regression)
2. [Real-World Example](#2-real-world-example)
3. [Simple vs Multiple Linear Regression](#3-simple-vs-multiple-linear-regression)
4. [Dataset](#4-dataset)
5. [Input Features and Target](#5-input-features-and-target)
6. [Multiple Linear Regression Formula](#6-multiple-linear-regression-formula)
7. [Project Workflow](#7-project-workflow)
8. [Step-by-Step Code Explanation](#8-step-by-step-code-explanation)
9. [Complete Dry Run](#9-complete-dry-run)
10. [Understanding Coefficients](#10-understanding-coefficients)
11. [Understanding Intercept](#11-understanding-intercept)
12. [Prediction for a New Student](#12-prediction-for-a-new-student)
13. [MSE](#13-mean-squared-error-mse)
14. [R² Score](#14-r2-score)
15. [Cross Validation](#15-cross-validation)
16. [Actual vs Predicted Graph](#16-actual-vs-predicted-graph)
17. [Important Concepts](#17-important-concepts)
18. [Interview Questions](#18-interview-questions)
19. [Final Revision](#19-final-revision)

---

# 1. What is Multiple Linear Regression?

**Multiple Linear Regression (MLR)** is a supervised Machine Learning algorithm used to predict a **continuous numerical value** using **two or more independent variables**.

### Example

We want to predict:

```text
Final Marks
```

Using:

```text
Study Hours
Attendance
Previous Marks
```

So:

```text
Study Hours ──────┐
Attendance ──────┼──> Multiple Linear Regression ──> Final Marks
Previous Marks ───┘
```

### Simple meaning

> Multiple Linear Regression finds the mathematical relationship between **multiple input variables** and **one numerical output**.

---

# 2. Real-World Example

Suppose we have information about students:

| Study Hours | Attendance | Previous Marks | Final Marks |
|---:|---:|---:|---:|
| 2 | 70 | 55 | 60 |
| 4 | 80 | 65 | 70 |
| 6 | 85 | 75 | 80 |
| 8 | 90 | 85 | 92 |

We want the model to learn:

```text
Study Hours
     +
Attendance
     +
Previous Marks
     ↓
Final Marks
```

After training, we can give a new student:

```text
Study Hours = 6.5
Attendance = 85
Previous Marks = 75
```

and ask:

```text
What will be the predicted Final Marks?
```

---

# 3. Simple vs Multiple Linear Regression

## 🟢 Simple Linear Regression

Uses **one independent variable**.

Example:

```text
Study Hours → Marks
```

Formula:

$$
y = b_0 + b_1x
$$

---

## 🔵 Multiple Linear Regression

Uses **two or more independent variables**.

Example:

```text
Study Hours ──────┐
Attendance ──────┼──> Final Marks
Previous Marks ───┘
```

Formula:

$$
y = b_0 + b_1x_1 + b_2x_2 + b_3x_3
$$

---

# 4. Dataset

Our project uses:

```text
student_marks_2000.csv
```

The dataset contains:

```text
Study_Hours
Attendance
Previous_Marks
Final_Marks
```

### Meaning of columns

| Column | Type | Meaning |
|---|---|---|
| Study_Hours | Input | Number of hours student studied |
| Attendance | Input | Attendance percentage |
| Previous_Marks | Input | Marks from previous examination |
| Final_Marks | Target | Final examination marks |

---

# 5. Input Features and Target

Machine Learning normally separates the data into:

```text
X = Input Features
y = Target
```

### Our project

```text
X =
Study_Hours
Attendance
Previous_Marks
```

and:

```text
y =
Final_Marks
```

### Code

```python
X = df.drop(columns="Final_Marks")

y = df["Final_Marks"]
```

### Why?

Because we want to predict:

```text
Final_Marks
```

Therefore, `Final_Marks` should not be given to the model as an input feature.

---

# 6. Multiple Linear Regression Formula

The general formula is:

$$
y = b_0 + b_1x_1 + b_2x_2 + ... + b_kx_k
$$

For our project:

$$
Final\_Marks =
b_0
+
b_1(Study\_Hours)
+
b_2(Attendance)
+
b_3(Previous\_Marks)
$$

### Meaning of each term

| Symbol | Meaning |
|---|---|
| $y$ | Predicted target |
| $b_0$ | Intercept |
| $b_1$ | Study Hours coefficient |
| $b_2$ | Attendance coefficient |
| $b_3$ | Previous Marks coefficient |
| $x_1$ | Study Hours |
| $x_2$ | Attendance |
| $x_3$ | Previous Marks |

---

# 7. Project Workflow

The complete Machine Learning workflow is:

```text
CSV Dataset
     ↓
Load Dataset
     ↓
Separate X and y
     ↓
Train/Test Split
     ↓
Create Linear Regression Model
     ↓
Train Model
     ↓
Learn Coefficients
     ↓
Make Predictions
     ↓
Evaluate Model
     ↓
Cross Validation
     ↓
Visualize Results
```

---

# 8. Step-by-Step Code Explanation

## STEP 1 — Import Libraries

```python
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
```

### Why do we need them?

### Pandas

```python
import pandas as pd
```

Used for:

- Reading CSV
- Creating DataFrames
- Manipulating data

---

### train_test_split

```python
from sklearn.model_selection import train_test_split
```

Used to divide data into:

```text
Training Data
Testing Data
```

---

### cross_val_score

```python
from sklearn.model_selection import cross_val_score
```

Used for:

```text
Cross Validation
```

---

### LinearRegression

```python
from sklearn.linear_model import LinearRegression
```

This is the algorithm used to create our regression model.

---

### Metrics

```python
from sklearn.metrics import mean_squared_error, r2_score
```

Used to calculate:

```text
MSE
R² Score
```

---

### Matplotlib

```python
import matplotlib.pyplot as plt
```

Used to create graphs.

---

# STEP 2 — Load Dataset

```python
df = pd.read_csv("student_marks_2000.csv")
```

This reads the CSV file.

The result is stored in:

```text
df
```

Here:

```text
df = DataFrame
```

A DataFrame looks like a table:

| Study_Hours | Attendance | Previous_Marks | Final_Marks |
|---:|---:|---:|---:|
| 2 | 70 | 55 | 60 |
| 4 | 80 | 65 | 70 |
| 6 | 85 | 75 | 80 |

---

# STEP 3 — View First 5 Rows

```python
print(df.head())
```

`head()` displays the first 5 rows.

Example:

```text
   Study_Hours  Attendance  Previous_Marks  Final_Marks
0            2          70              55           60
1            4          80              65           70
2            6          85              75           80
3            8          90              85           92
```

---

# STEP 4 — Separate X and y

```python
X = df.drop(columns="Final_Marks")

y = df["Final_Marks"]
```

### X

```text
X = Study_Hours
    Attendance
    Previous_Marks
```

### y

```text
y = Final_Marks
```

Think:

```text
X → Questions / Inputs

y → Answer / Target
```

---

# STEP 5 — Train/Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
```

Here:

```text
test_size = 0.2
```

means:

```text
80% → Training
20% → Testing
```

If the dataset contains **2000 rows**:

```text
2000 × 80% = 1600 training rows

2000 × 20% = 400 testing rows
```

So approximately:

```text
2000 rows
    ↓
┌───────────────┬──────────────┐
│ Training 80%  │ Testing 20%  │
│ 1600 rows     │ 400 rows     │
└───────────────┴──────────────┘
```

---

# STEP 6 — Create Model

```python
mlr = LinearRegression()
```

Here:

```text
mlr
```

is our Multiple Linear Regression model.

At this point:

```text
Model created
```

but it has **not learned anything yet**.

---

# STEP 7 — Train the Model

```python
mlr.fit(X_train, y_train)
```

This is one of the most important lines.

`fit()` means:

> Train the model using the training data.

The model looks at:

```text
Study_Hours
Attendance
Previous_Marks
```

and learns how they are related to:

```text
Final_Marks
```

Conceptually:

```text
X_train + y_train
       ↓
     fit()
       ↓
Model learns coefficients
```

---

# STEP 8 — Make Predictions

```python
y_pred = mlr.predict(X_test)
```

The trained model now receives:

```text
X_test
```

and produces:

```text
Predicted Final Marks
```

So:

```text
X_test
   ↓
trained model
   ↓
y_pred
```

---

# STEP 9 — Compare Actual and Predicted Values

```python
print(y_test.head())
print(y_pred[:5])
```

Example:

```text
Actual:
[82, 74, 91, 65, 78]

Predicted:
[81.5, 75.2, 89.8, 66.1, 77.4]
```

The model is trying to make:

```text
Predicted ≈ Actual
```

---

# STEP 10 — Coefficients

```python
print(mlr.coef_)
```

Suppose the model produces:

```text
[2.5, 0.3, 0.6]
```

Then:

```text
Study_Hours coefficient = 2.5

Attendance coefficient = 0.3

Previous_Marks coefficient = 0.6
```

These numbers tell us how each feature contributes to the prediction **while holding the other included features constant**.

---

# STEP 11 — Intercept

```python
print(mlr.intercept_)
```

Suppose:

```text
Intercept = 10
```

Then the equation starts with:

```text
Final_Marks = 10 + ...
```

---

# STEP 12 — Regression Equation

The code creates:

```python
print(
    f"Final_Marks = "
    f"{mlr.intercept_:.4f} + "
    f"{mlr.coef_[0]:.4f} × Study_Hours + "
    f"{mlr.coef_[1]:.4f} × Attendance + "
    f"{mlr.coef_[2]:.4f} × Previous_Marks"
)
```

Suppose:

```text
Intercept = 10
Study_Hours coefficient = 2.5
Attendance coefficient = 0.3
Previous_Marks coefficient = 0.6
```

The equation becomes:

$$
Final\_Marks =
10
+
2.5(Study\_Hours)
+
0.3(Attendance)
+
0.6(Previous\_Marks)
$$

This is the mathematical model learned from the training data.

---

# 9. Complete Dry Run

Let's understand the complete program using a small example.

Suppose we have:

| Student | Study Hours | Attendance | Previous Marks | Final Marks |
|---|---:|---:|---:|---:|
| A | 2 | 70 | 55 | 60 |
| B | 4 | 80 | 65 | 70 |
| C | 6 | 85 | 75 | 80 |
| D | 8 | 90 | 85 | 92 |
| E | 5 | 75 | 70 | 76 |

---

## 🔹 Dry Run — Step 1

Read CSV:

```python
df = pd.read_csv("student_marks_2000.csv")
```

Python creates:

```text
df
```

containing the complete dataset.

---

## 🔹 Dry Run — Step 2

Execute:

```python
X = df.drop(columns="Final_Marks")
```

So:

```text
X
```

contains:

```text
Study_Hours
Attendance
Previous_Marks
```

---

## 🔹 Dry Run — Step 3

Execute:

```python
y = df["Final_Marks"]
```

So:

```text
y
```

contains:

```text
Final_Marks
```

---

## 🔹 Dry Run — Step 4

Split:

```python
test_size=0.2
```

For 2000 records:

```text
Training = 1600
Testing  = 400
```

---

## 🔹 Dry Run — Step 5

Create model:

```python
mlr = LinearRegression()
```

Model exists, but has not learned yet.

---

## 🔹 Dry Run — Step 6

Train:

```python
mlr.fit(X_train, y_train)
```

The model learns:

```text
Intercept
Coefficient 1
Coefficient 2
Coefficient 3
```

For example:

```text
b0 = 10
b1 = 2.5
b2 = 0.3
b3 = 0.6
```

These numbers are only an **illustration**; your actual values come from `student_marks_2000.csv`.

---

## 🔹 Dry Run — Step 7

The model equation becomes:

$$
Final\_Marks =
10
+
2.5(Study\_Hours)
+
0.3(Attendance)
+
0.6(Previous\_Marks)
$$

---

# 10. Understanding Coefficients

Suppose:

```text
Study_Hours coefficient = 2.5
```

Interpretation:

> If Study Hours increases by 1 unit, predicted Final Marks increase by about 2.5 marks, assuming the other features remain constant.

---

Suppose:

```text
Attendance coefficient = 0.3
```

Interpretation:

> If Attendance increases by 1 percentage point, predicted Final Marks increase by about 0.3 marks, assuming the other features remain constant.

---

Suppose:

```text
Previous_Marks coefficient = 0.6
```

Interpretation:

> If Previous Marks increases by 1 mark, predicted Final Marks increase by about 0.6 marks, assuming the other features remain constant.

---

## ⚠️ Important

Do not interpret coefficients without considering:

- feature units
- feature scale
- relationships between features
- multicollinearity
- the data-generating context

A larger coefficient does **not automatically mean** that feature is more important.

---

# 11. Understanding Intercept

Suppose:

```text
Intercept = 10
```

Then:

$$
Final\_Marks =
10
+
...
$$

The intercept is the model's predicted target when all input features are zero.

In real-world datasets, this value may not always have a meaningful practical interpretation.

---

# 12. Prediction for a New Student

The code creates:

```python
new_student = pd.DataFrame({
    "Study_Hours": [6.5],
    "Attendance": [85],
    "Previous_Marks": [75]
})
```

The student has:

```text
Study Hours    = 6.5
Attendance     = 85
Previous Marks = 75
```

Then:

```python
prediction = mlr.predict(new_student)
```

The model calculates:

$$
Final\_Marks =
b_0
+
b_1(6.5)
+
b_2(85)
+
b_3(75)
$$

The result is the predicted Final Marks.

---

# 13. Mean Squared Error — MSE

The code:

```python
mse = mean_squared_error(y_test, y_pred)
```

calculates:

```text
Mean Squared Error
```

Formula:

$$
MSE =
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
$$

Where:

| Symbol | Meaning |
|---|---|
| $n$ | Number of test observations |
| $y_i$ | Actual value |
| $\hat{y}_i$ | Predicted value |
| $y_i-\hat{y}_i$ | Error |
| $(y_i-\hat{y}_i)^2$ | Squared error |

---

## Example

Suppose:

```text
Actual     = 80
Predicted  = 75
```

Error:

$$
80-75=5
$$

Squared error:

$$
5^2=25
$$

MSE calculates the average of these squared errors across all test records.

### Important

```text
Lower MSE → Better
Higher MSE → Worse
```

But MSE is expressed in **squared target units**, so it can be harder to interpret directly.

---

# 14. R² Score

The code:

```python
r2 = r2_score(y_test, y_pred)
```

calculates the:

```text
R² Score
```

Formula:

$$
R^2 =
1-
\frac{SS_{res}}{SS_{tot}}
$$

Where:

### Residual Sum of Squares

$$
SS_{res}
=
\sum(y_i-\hat{y}_i)^2
$$

### Total Sum of Squares

$$
SS_{tot}
=
\sum(y_i-\bar{y})^2
$$

### General interpretation

```text
R² close to 1 → strong explanatory performance

R² close to 0 → weak explanatory performance

R² < 0       → model can be worse than a baseline
```

---

# 15. Cross Validation

The code:

```python
cv_scores = cross_val_score(
    mlr,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)
```

uses:

```text
5-Fold Cross Validation
```

---

## How 5-Fold Cross Validation Works

Suppose training data contains:

```text
1600 rows
```

It is divided into approximately:

```text
Fold 1 → 320
Fold 2 → 320
Fold 3 → 320
Fold 4 → 320
Fold 5 → 320
```

The model is trained and validated 5 times.

### Round 1

```text
Train → Fold 2 + 3 + 4 + 5
Test  → Fold 1
```

### Round 2

```text
Train → Fold 1 + 3 + 4 + 5
Test  → Fold 2
```

### Round 3

```text
Train → Fold 1 + 2 + 4 + 5
Test  → Fold 3
```

### Round 4

```text
Train → Fold 1 + 2 + 3 + 5
Test  → Fold 4
```

### Round 5

```text
Train → Fold 1 + 2 + 3 + 4
Test  → Fold 5
```

---

## Individual Fold Scores

```python
print(cv_scores)
```

Example:

```text
[0.82, 0.85, 0.80, 0.84, 0.83]
```

These are illustrative values.

---

## Mean Cross Validation R²

```python
mean_cv = cv_scores.mean()
```

Example:

```text
Mean CV R² = 0.828
```

This gives an overall average of the five validation scores.

---

## Standard Deviation

```python
std_cv = cv_scores.std()
```

Standard deviation tells us how much the fold scores vary.

### Lower standard deviation

Usually means:

```text
More consistent performance across folds
```

### Higher standard deviation

Means:

```text
Performance varies more between folds
```

---

# 16. Actual vs Predicted Graph

The code creates:

```python
plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)
```

The graph contains:

```text
X-axis → Actual Marks
Y-axis → Predicted Marks
```

Each point represents one student.

---

# Perfect Prediction Line

The code creates:

```python
plt.plot(
    [min_value, max_value],
    [min_value, max_value]
)
```

This represents:

$$
Actual = Predicted
$$

For example:

```text
Actual = 80
Predicted = 80
```

The point lies exactly on the diagonal line.

---

## Good Model

Points are close to:

```text
Perfect Prediction Line
```

Conceptually:

```text
Predicted
   ↑
100|                 •
 90|              •
 80|           •
 70|        •
 60|     •
   +----------------------→ Actual
```

---

## Poorer Predictions

If points are far away from the diagonal:

```text
Actual ≠ Predicted
```

which means prediction errors are larger.

---

# 17. Important Concepts

## 🟢 1. Relevant Features

A relevant feature provides useful information for predicting the target.

Example:

```text
Study_Hours
```

may be useful for predicting:

```text
Final_Marks
```

---

## 🔴 2. Irrelevant Features

An irrelevant feature does not provide useful information about the target.

Example:

```text
Student_ID
```

may not help predict marks.

Adding unnecessary variables can:

- increase model complexity
- make interpretation harder
- potentially increase overfitting risk
- affect adjusted R²

---

# Adjusted R²

For a regression model with multiple features:

$$
R^2_{adj}
=
1-
\frac{(1-R^2)(n-1)}
{n-k-1}
$$

Where:

| Symbol | Meaning |
|---|---|
| $R^2$ | R-squared |
| $n$ | Number of observations |
| $k$ | Number of independent variables |

### Important idea

Adding a feature can increase ordinary $R^2$ even if the feature contributes very little.

Adjusted $R^2$ applies a penalty for adding predictors.

Therefore:

```text
Useful feature
     ↓
Adjusted R² may increase

Unnecessary feature
     ↓
Adjusted R² may decrease
```

---

# Bias and Variance

## 🔵 High Bias

Model is too simple.

```text
High Bias
   ↓
Underfitting
```

The model fails to capture important patterns.

---

## 🔴 High Variance

Model is too sensitive to the training data.

```text
High Variance
   ↓
Overfitting
```

The model performs very well on training data but may perform poorly on unseen data.

---

## 🟢 Good Balance

The goal is:

```text
Low enough Bias
       +
Low enough Variance
       ↓
Good Generalization
```

---

# 18. Interview Questions

## Q1. What is Multiple Linear Regression?

**Answer:**

Multiple Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical target using two or more independent variables.

---

## Q2. What is the formula for Multiple Linear Regression?

**Answer:**

$$
y=b_0+b_1x_1+b_2x_2+\cdots+b_kx_k
$$

---

## Q3. What is the difference between Simple and Multiple Linear Regression?

**Answer:**

| Simple Linear Regression | Multiple Linear Regression |
|---|---|
| One independent variable | Two or more independent variables |
| $y=b_0+b_1x$ | $y=b_0+b_1x_1+\cdots+b_kx_k$ |
| Example: Study Hours → Marks | Study Hours + Attendance → Marks |

---

## Q4. What does `fit()` do?

**Answer:**

```python
model.fit(X_train, y_train)
```

trains the model and estimates the regression parameters from the training data.

---

## Q5. What does `predict()` do?

**Answer:**

```python
model.predict(X_test)
```

uses the trained model to generate predictions for new input data.

---

## Q6. What is a coefficient?

**Answer:**

A coefficient represents the estimated change in the predicted target for a one-unit increase in a feature, while the other included features are held constant.

---

## Q7. What is an intercept?

**Answer:**

The intercept is the predicted target value when all input features are zero.

---

## Q8. What is MSE?

**Answer:**

MSE is the average of squared prediction errors.

$$
MSE=
\frac{1}{n}
\sum(y_i-\hat{y}_i)^2
$$

Lower MSE generally indicates smaller squared prediction errors.

---

## Q9. What is R²?

**Answer:**

R² measures the proportion of variation in the target that is explained by the regression model relative to the mean-baseline model.

---

## Q10. Why do we use Train/Test Split?

**Answer:**

To evaluate the model on data that was not used to train it.

---

## Q11. Why is Cross Validation used?

**Answer:**

Cross Validation evaluates the model across multiple train/validation splits, giving a more stable estimate of performance than relying on one split alone.

---

## Q12. What is `cv=5`?

**Answer:**

It means the training data is divided into 5 folds and the model is evaluated 5 times, with a different fold used for validation each time.

---

## Q13. What is overfitting?

**Answer:**

Overfitting occurs when a model learns the training data too closely, including noise or specific patterns, and performs poorly on unseen data.

---

## Q14. Can adding a feature reduce Adjusted R²?

**Answer:**

Yes.

If the new feature does not provide enough additional explanatory value, Adjusted R² can decrease.

---

# 19. Final Revision

### 🧠 Remember this flow:

```text
                 DATASET
                    ↓
              Load CSV
                    ↓
             Separate X / y
                    ↓
             Train/Test Split
                    ↓
          Create LinearRegression
                    ↓
                 fit()
                    ↓
          Learn Coefficients
                    ↓
               predict()
                    ↓
        ┌───────────┴───────────┐
        ↓                       ↓
       MSE                      R²
        ↓                       ↓
   Error Measure        Model Explanation
        └───────────┬───────────┘
                    ↓
            Cross Validation
                    ↓
             Visualization
```

---

# ⭐ Complete Concept Summary

```text
Multiple Linear Regression
        ↓
Multiple Input Features
        ↓
One Continuous Target
        ↓
Learn Coefficients
        ↓
Create Regression Equation
        ↓
Predict New Values
        ↓
Evaluate Predictions
        ↓
MSE + R²
        ↓
Cross Validation
        ↓
Check Generalization
```

### Most important commands

```python
df = pd.read_csv("student_marks_2000.csv")
```

```python
X = df.drop(columns="Final_Marks")
```

```python
y = df["Final_Marks"]
```

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
```

```python
mlr = LinearRegression()
```

```python
mlr.fit(X_train, y_train)
```

```python
y_pred = mlr.predict(X_test)
```

```python
mse = mean_squared_error(y_test, y_pred)
```

```python
r2 = r2_score(y_test, y_pred)
```

```python
cv_scores = cross_val_score(
    mlr,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)
```

---

# 🎯 One-Line Interview Definition

> **Multiple Linear Regression is a supervised learning algorithm that predicts a continuous numerical target using two or more independent variables by learning their linear relationship with the target.**

---

# ⚠️ Note About This Project Code

Your current code calculates:

```text
✅ MSE
✅ R²
✅ Cross-Validation R²
✅ Mean CV R²
✅ Cross-Validation Standard Deviation
```

It does **not** currently calculate:

```text
❌ MAE
❌ RMSE
❌ Adjusted R²
```

These are related regression evaluation concepts from your Simple/Multiple Linear Regression lessons, but they are not present in the supplied code.

For this particular README, the explanation above stays aligned with what your code actually does.

### General interpretation

```text
R² close to 1 → strong explanatory performance

R² close to 0 → weak explanatory performance

R² < 0       → model can be worse than a baseline
```

---

# 15. Cross Validation

The code:

```python
cv_scores = cross_val_score(
    mlr,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)
```

uses:

```text
5-Fold Cross Validation
```

---

## How 5-Fold Cross Validation Works

Suppose training data contains:

```text
1600 rows
```

It is divided into approximately:

```text
Fold 1 → 320
Fold 2 → 320
Fold 3 → 320
Fold 4 → 320
Fold 5 → 320
```

The model is trained and validated 5 times.

### Round 1

```text
Train → Fold 2 + 3 + 4 + 5
Test  → Fold 1
```

### Round 2

```text
Train → Fold 1 + 3 + 4 + 5
Test  → Fold 2
```

### Round 3

```text
Train → Fold 1 + 2 + 4 + 5
Test  → Fold 3
```

### Round 4

```text
Train → Fold 1 + 2 + 3 + 5
Test  → Fold 4
```

### Round 5

```text
Train → Fold 1 + 2 + 3 + 4
Test  → Fold 5
```

---

## Individual Fold Scores

```python
print(cv_scores)
```

Example:

```text
[0.82, 0.85, 0.80, 0.84, 0.83]
```

These are illustrative values.

---

## Mean Cross Validation R²

```python
mean_cv = cv_scores.mean()
```

Example:

```text
Mean CV R² = 0.828
```

This gives an overall average of the five validation scores.

---

## Standard Deviation

```python
std_cv = cv_scores.std()
```

Standard deviation tells us how much the fold scores vary.

### Lower standard deviation

Usually means:

```text
More consistent performance across folds
```

### Higher standard deviation

Means:

```text
Performance varies more between folds
```

---

# 16. Actual vs Predicted Graph

The code creates:

```python
plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)
```

The graph contains:

```text
X-axis → Actual Marks
Y-axis → Predicted Marks
```

Each point represents one student.

---

# Perfect Prediction Line

The code creates:

```python
plt.plot(
    [min_value, max_value],
    [min_value, max_value]
)
```

This represents:

$$
Actual = Predicted
$$

For example:

```text
Actual = 80
Predicted = 80
```

The point lies exactly on the diagonal line.

---

## Good Model

Points are close to:

```text
Perfect Prediction Line
```

Conceptually:

```text
Predicted
   ↑
100|                 •
 90|              •
 80|           •
 70|        •
 60|     •
   +----------------------→ Actual
```

---

## Poorer Predictions

If points are far away from the diagonal:

```text
Actual ≠ Predicted
```

which means prediction errors are larger.

---

# 17. Important Concepts

## 🟢 1. Relevant Features

A relevant feature provides useful information for predicting the target.

Example:

```text
Study_Hours
```

may be useful for predicting:

```text
Final_Marks
```

---

## 🔴 2. Irrelevant Features

An irrelevant feature does not provide useful information about the target.

Example:

```text
Student_ID
```

may not help predict marks.

Adding unnecessary variables can:

- increase model complexity
- make interpretation harder
- potentially increase overfitting risk
- affect adjusted R²

---

# Adjusted R²

For a regression model with multiple features:

$$
R^2_{adj}
=
1-
\frac{(1-R^2)(n-1)}
{n-k-1}
$$

Where:

| Symbol | Meaning |
|---|---|
| $R^2$ | R-squared |
| $n$ | Number of observations |
| $k$ | Number of independent variables |

### Important idea

Adding a feature can increase ordinary $R^2$ even if the feature contributes very little.

Adjusted $R^2$ applies a penalty for adding predictors.

Therefore:

```text
Useful feature
     ↓
Adjusted R² may increase

Unnecessary feature
     ↓
Adjusted R² may decrease
```

---

# Bias and Variance

## 🔵 High Bias

Model is too simple.

```text
High Bias
   ↓
Underfitting
```

The model fails to capture important patterns.

---

## 🔴 High Variance

Model is too sensitive to the training data.

```text
High Variance
   ↓
Overfitting
```

The model performs very well on training data but may perform poorly on unseen data.

---

## 🟢 Good Balance

The goal is:

```text
Low enough Bias
       +
Low enough Variance
       ↓
Good Generalization
```

---

# 18. Interview Questions

## Q1. What is Multiple Linear Regression?

**Answer:**

Multiple Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical target using two or more independent variables.

---

## Q2. What is the formula for Multiple Linear Regression?

**Answer:**

$$
y=b_0+b_1x_1+b_2x_2+\cdots+b_kx_k
$$

---

## Q3. What is the difference between Simple and Multiple Linear Regression?

**Answer:**

| Simple Linear Regression | Multiple Linear Regression |
|---|---|
| One independent variable | Two or more independent variables |
| $y=b_0+b_1x$ | $y=b_0+b_1x_1+\cdots+b_kx_k$ |
| Example: Study Hours → Marks | Study Hours + Attendance → Marks |

---

## Q4. What does `fit()` do?

**Answer:**

```python
model.fit(X_train, y_train)
```

trains the model and estimates the regression parameters from the training data.

---

## Q5. What does `predict()` do?

**Answer:**

```python
model.predict(X_test)
```

uses the trained model to generate predictions for new input data.

---

## Q6. What is a coefficient?

**Answer:**

A coefficient represents the estimated change in the predicted target for a one-unit increase in a feature, while the other included features are held constant.

---

## Q7. What is an intercept?

**Answer:**

The intercept is the predicted target value when all input features are zero.

---

## Q8. What is MSE?

**Answer:**

MSE is the average of squared prediction errors.

$$
MSE=
\frac{1}{n}
\sum(y_i-\hat{y}_i)^2
$$

Lower MSE generally indicates smaller squared prediction errors.

---

## Q9. What is R²?

**Answer:**

R² measures the proportion of variation in the target that is explained by the regression model relative to the mean-baseline model.

---

## Q10. Why do we use Train/Test Split?

**Answer:**

To evaluate the model on data that was not used to train it.

---

## Q11. Why is Cross Validation used?

**Answer:**

Cross Validation evaluates the model across multiple train/validation splits, giving a more stable estimate of performance than relying on one split alone.

---

## Q12. What is `cv=5`?

**Answer:**

It means the training data is divided into 5 folds and the model is evaluated 5 times, with a different fold used for validation each time.

---

## Q13. What is overfitting?

**Answer:**

Overfitting occurs when a model learns the training data too closely, including noise or specific patterns, and performs poorly on unseen data.

---

## Q14. Can adding a feature reduce Adjusted R²?

**Answer:**

Yes.

If the new feature does not provide enough additional explanatory value, Adjusted R² can decrease.

---

# 19. Final Revision

### 🧠 Remember this flow:

```text
                 DATASET
                    ↓
              Load CSV
                    ↓
             Separate X / y
                    ↓
             Train/Test Split
                    ↓
          Create LinearRegression
                    ↓
                 fit()
                    ↓
          Learn Coefficients
                    ↓
               predict()
                    ↓
        ┌───────────┴───────────┐
        ↓                       ↓
       MSE                      R²
        ↓                       ↓
   Error Measure        Model Explanation
        └───────────┬───────────┘
                    ↓
            Cross Validation
                    ↓
             Visualization
```

---

# ⭐ Complete Concept Summary

```text
Multiple Linear Regression
        ↓
Multiple Input Features
        ↓
One Continuous Target
        ↓
Learn Coefficients
        ↓
Create Regression Equation
        ↓
Predict New Values
        ↓
Evaluate Predictions
        ↓
MSE + R²
        ↓
Cross Validation
        ↓
Check Generalization
```

### Most important commands

```python
df = pd.read_csv("student_marks_2000.csv")
```

```python
X = df.drop(columns="Final_Marks")
```

```python
y = df["Final_Marks"]
```

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)
```

```python
mlr = LinearRegression()
```

```python
mlr.fit(X_train, y_train)
```

```python
y_pred = mlr.predict(X_test)
```

```python
mse = mean_squared_error(y_test, y_pred)
```

```python
r2 = r2_score(y_test, y_pred)
```

```python
cv_scores = cross_val_score(
    mlr,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)
```

---

# 🎯 One-Line Interview Definition

> **Multiple Linear Regression is a supervised learning algorithm that predicts a continuous numerical target using two or more independent variables by learning their linear relationship with the target.**

---

# ⚠️ Note About This Project Code

Your current code calculates:

```text
✅ MSE
✅ R²
✅ Cross-Validation R²
✅ Mean CV R²
✅ Cross-Validation Standard Deviation
```

It does **not** currently calculate:

```text
❌ MAE
❌ RMSE
❌ Adjusted R²
```

These are related regression evaluation concepts from your Simple/Multiple Linear Regression lessons, but they are not present in the supplied code.

For this particular README, the explanation above stays aligned with what your code actually does.
