# 📈 Simple Linear Regression

> **Machine Learning — Supervised Learning — Regression**

Simple Linear Regression is one of the most important Machine Learning algorithms.

It is used to predict a **continuous numerical value** using **one independent variable (feature)**.

### 🎯 Example

We want to predict a student's **Marks** based on **Study Hours**.

```text
Study Hours  →  Machine Learning Model  →  Predicted Marks
```

Example:

```text
7.5 hours → Model → 70.56 Marks
```

---

# 📚 Table of Contents

1. [What is Simple Linear Regression?](#1-what-is-simple-linear-regression)
2. [Real-World Example](#2-real-world-example)
3. [Important Terminology](#3-important-terminology)
4. [Regression Equation](#4-regression-equation)
5. [Best-Fit Line](#5-best-fit-line)
6. [Error / Residual](#6-error--residual)
7. [Cost Function](#7-cost-function)
8. [Gradient Descent](#8-gradient-descent)
9. [Train and Test Data](#9-train-and-test-data)
10. [Model Training](#10-model-training)
11. [Prediction](#11-prediction)
12. [Model Evaluation](#12-model-evaluation)
13. [MAE](#13-mae)
14. [MSE](#14-mse)
15. [RMSE](#15-rmse)
16. [R² Score](#16-r²-score)
17. [Adjusted R² Score](#17-adjusted-r²-score)
18. [Feature Selection](#18-feature-selection)
19. [Relevant vs Irrelevant Features](#19-relevant-vs-irrelevant-features)
20. [Bias and Variance](#20-bias-and-variance)
21. [Complete Python Code](#21-complete-python-code)
22. [Complete Dry Run](#22-complete-dry-run)
23. [Output Explanation](#23-output-explanation)
24. [Prediction for New Student](#24-prediction-for-new-student)
25. [Graph Explanation](#25-graph-explanation)
26. [Advantages](#26-advantages)
27. [Limitations](#27-limitations)
28. [Interview Questions](#28-interview-questions)
29. [Quick Revision](#29-quick-revision)

---

# 1. What is Simple Linear Regression?

Simple Linear Regression is a **supervised learning algorithm** used to predict a continuous numerical target using **one independent variable**.

### Simple meaning

We have:

```text
Input X → Model → Output y
```

For our example:

```text
Study Hours → Linear Regression → Marks
```

### Example

| Study Hours | Marks |
|---:|---:|
| 1 | 25 |
| 2 | 30 |
| 3 | 40 |
| 4 | 45 |
| 5 | 50 |
| 6 | 60 |
| 7 | 65 |
| 8 | 75 |
| 9 | 80 |
| 10 | 90 |

The model learns the relationship between:

```text
Study Hours ↔ Marks
```

Then it can predict marks for a new student.

---

# 2. Real-World Example

Simple Linear Regression can be used for:

### 🏠 House Price

```text
Area → House Price
```

### 💰 Salary

```text
Experience → Salary
```

### 📚 Student Marks

```text
Study Hours → Marks
```

### 📈 Sales

```text
Advertising Spend → Sales
```

---

# 3. Important Terminology

| Term | Meaning |
|---|---|
| X | Independent variable / Feature |
| y | Actual target |
| ŷ | Predicted target |
| m | Slope / Coefficient |
| c | Intercept |
| Error | Difference between actual and predicted value |
| Model | Learned mathematical relationship |
| Residual | Actual − Predicted |
| Training data | Data used to learn |
| Testing data | Data used to evaluate |

---

# 4. Regression Equation

The basic equation is:

$$
\hat{y} = mx + c
$$

Where:

- $\hat{y}$ = predicted value
- $x$ = input feature
- $m$ = slope
- $c$ = intercept

---

## 🔍 Example

Suppose:

```text
m = 7
c = 17
x = 5
```

Then:

$$
\hat{y} = 7(5) + 17
$$

$$
\hat{y} = 35 + 17
$$

$$
\hat{y} = 52
$$

So the predicted value is:

```text
52
```

---

# 5. Best-Fit Line

The goal of Linear Regression is to find the **best-fit line** through the data points.

```text
Marks
  |
90|                         ●
80|                      ●
70|                   ●
60|                ●
50|             ●
40|          ●
30|       ●
20|    ●
  |
  +---------------------------- Study Hours
     1  2  3  4  5  6  7  8  9 10
```

The actual points are represented by:

```text
●
```

The model tries to find a line that stays as close as possible to these points.

### 🎯 Goal

> Find the line that produces the smallest overall prediction error.

---

# 6. Error / Residual

The difference between the actual value and predicted value is called **error** or **residual**.

$$
e = y - \hat{y}
$$

Where:

- $y$ = actual value
- $\hat{y}$ = predicted value
- $e$ = error

---

## Example

Actual marks:

```text
80
```

Predicted marks:

```text
81
```

Then:

$$
e = 80 - 81
$$

$$
e = -1
$$

The model prediction is 1 mark higher than the actual value.

---

# 7. Cost Function

The model needs a way to measure how much error it is making.

A common cost function for Linear Regression is **Mean Squared Error (MSE)**.

$$
J(m,c)
=
\frac{1}{n}
\sum_{i=1}^{n}
\left(y_i-(mx_i+c)\right)^2
$$

### Terms

| Symbol | Meaning |
|---|---|
| $J$ | Cost function |
| $m$ | Slope |
| $c$ | Intercept |
| $n$ | Number of observations |
| $x_i$ | Input value |
| $y_i$ | Actual value |
| $mx_i+c$ | Predicted value |

### 🎯 Goal

```text
Minimize Cost
      ↓
Reduce Prediction Error
      ↓
Find Better m and c
      ↓
Find Best-Fit Line
```

---

# 8. Gradient Descent

Gradient Descent is an optimization technique used to find better values for model parameters.

For Simple Linear Regression, the parameters are:

```text
m → slope
c → intercept
```

The idea is:

```text
Start with m and c
       ↓
Calculate cost
       ↓
Calculate gradient
       ↓
Update m and c
       ↓
Calculate cost again
       ↓
Repeat
       ↓
Reach minimum cost
```

---

## Gradient Descent Update

$$
m := m-\alpha\frac{\partial J}{\partial m}
$$

$$
c := c-\alpha\frac{\partial J}{\partial c}
$$

Where:

- $\alpha$ = learning rate
- $J$ = cost function
- $\frac{\partial J}{\partial m}$ = gradient with respect to $m$
- $\frac{\partial J}{\partial c}$ = gradient with respect to $c$

---

## 🧠 Simple Understanding

Think of a person standing on a hill.

```text
        Start
          ●
         /
        /
       /
      /       \
     /         \
----/-----------\----
             Minimum
```

The person wants to reach the lowest point.

Gradient Descent does something similar:

```text
High Cost
   ↓
Move toward lower Cost
   ↓
Lower Cost
   ↓
Move again
   ↓
Minimum Cost
```

---

# 9. Train and Test Data

Before training the model, we divide the dataset into:

```text
Training Data
+
Testing Data
```

In our code:

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### `test_size=0.2`

Means:

```text
20% → Testing
80% → Training
```

Our dataset contains:

```text
10 records
```

Therefore:

```text
80% of 10 = 8 records
20% of 10 = 2 records
```

So:

```text
Training = 8 records
Testing  = 2 records
```

---

# 10. Model Training

We create the model:

```python
model = LinearRegression()
```

Then train it:

```python
model.fit(X_train, y_train)
```

The model learns:

```text
Study Hours → Marks
```

During training, the model learns:

```text
Slope (m)
Intercept (c)
```

---

# 11. Prediction

After training:

```python
y_pred = model.predict(X_test)
```

The model takes the testing input and predicts the marks.

```text
X_test
  ↓
Trained Model
  ↓
y_pred
```

---

# 12. Model Evaluation

We compare:

```text
Actual Values
      VS
Predicted Values
```

Our code calculates:

```python
mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)
```

Important regression metrics:

1. MAE
2. MSE
3. RMSE
4. R²
5. Adjusted R²

---

# 13. MAE

## Mean Absolute Error

MAE calculates the average absolute error.

$$
MAE =
\frac{1}{n}
\sum_{i=1}^{n}
|y_i-\hat{y}_i|
$$

### Why absolute value?

Because errors can be:

```text
+5
-5
```

Without absolute value:

```text
+5 + (-5) = 0
```

This could incorrectly look like zero error.

Absolute value makes both errors positive:

```text
|+5| = 5
|-5| = 5
```

### Interpretation

If:

```text
MAE = 1.25
```

It means the model is wrong by about:

```text
1.25 marks on average
```

---

# 14. MSE

## Mean Squared Error

$$
MSE =
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
$$

MSE squares every error.

Example:

```text
Error = 2

2² = 4
```

```text
Error = -3

(-3)² = 9
```

Therefore, large errors receive a larger penalty.

### Important

```text
Small MSE → Better model
Large MSE → More error
```

---

# 15. RMSE

## Root Mean Squared Error

RMSE is the square root of MSE.

$$
RMSE = \sqrt{MSE}
$$

### Why use RMSE?

MSE is squared, so its unit is also squared.

RMSE brings the result back to the original target unit.

For example:

```text
Target = Marks

RMSE = Marks
```

This makes interpretation easier.

---

# 16. R² Score

R² tells us how much variation in the target variable is explained by the model.

$$
R^2 =
1-
\frac{SS_{res}}{SS_{tot}}
$$

Where:

- $SS_{res}$ = residual sum of squares
- $SS_{tot}$ = total sum of squares

### Simple meaning

If:

```text
R² = 0.9975
```

Then the model explains approximately:

```text
99.75%
```

of the variation in the target for this test set.

### General interpretation

```text
R² close to 1 → Strong fit
R² close to 0 → Weak explanatory power
```

> R² should be interpreted in context; a high R² does not by itself prove that a model is good or causal.

---

# 17. Adjusted R² Score

Adjusted R² is useful when we have multiple independent variables.

Formula:

$$
R^2_{adj}
=
1-
\frac{(1-R^2)(n-1)}
{n-k-1}
$$

Where:

- $R^2$ = R-squared
- $n$ = number of observations
- $k$ = number of independent variables

---

## Why Adjusted R²?

Normal R² generally does not decrease when we add another feature.

For example:

```text
Model 1

Study Hours
     ↓
Marks

R² = 0.90
```

Now add:

```text
Study Hours
Sleep Hours
Random Column
     ↓
Marks
```

R² might increase even if the random column is useless.

Adjusted R² applies a penalty for adding unnecessary predictors.

### Important

```text
Useful feature
      ↓
Adjusted R² may increase
```

```text
Useless feature
      ↓
Adjusted R² may decrease
```

---

# 18. Feature Selection

A **feature** is an input variable used by the model.

Our current feature is:

```text
Study_Hours
```

Target:

```text
Marks
```

So:

```text
X = Study_Hours
y = Marks
```

---

## Example

Suppose our dataset contains:

| Study Hours | Sleep Hours | Marks |
|---:|---:|---:|
| 2 | 7 | 30 |
| 4 | 8 | 45 |
| 6 | 6 | 60 |
| 8 | 7 | 75 |

Potential features:

```text
Study Hours
Sleep Hours
```

Target:

```text
Marks
```

Feature selection asks:

> Which independent variables are actually useful for predicting the target?

---

# 19. Relevant vs Irrelevant Features

## ✅ Relevant Feature

A feature that contains useful information for predicting the target.

Example:

```text
Study Hours → Marks
```

Study hours are likely related to marks.

---

## ❌ Irrelevant Feature

A feature that does not provide useful information.

Example:

```text
Student ID → Marks
```

A Student ID such as:

```text
101
102
103
```

does not necessarily explain marks.

Adding irrelevant variables can:

- increase model complexity
- make interpretation harder
- sometimes hurt generalization
- reduce Adjusted R²

### 🎯 Goal

Use meaningful features rather than adding columns just because they are available.

---

# 20. Bias and Variance

Bias and variance help us understand model generalization.

---

## 🔵 High Bias

The model is too simple.

```text
High Bias
    ↓
Underfitting
```

The model may perform poorly on:

```text
Training Data
Testing Data
```

---

## 🔴 High Variance

The model is too sensitive to training data.

```text
High Variance
      ↓
Overfitting
```

Typical pattern:

```text
Training Performance → Very Good
Testing Performance  → Poor
```

---

## 🟢 Good Balance

The goal is to find a balance.

```text
Too Simple
   ↓
High Bias
   ↓
Underfitting

        ⭐ Good Model

   ↑
High Variance
   ↑
Overfitting
```

### Bias–Variance Trade-off

The goal is not:

```text
Minimum Bias only
```

or:

```text
Minimum Variance only
```

The goal is:

```text
Good Bias + Good Variance
        ↓
Good Generalization
```

---

# 21. Complete Python Code

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import matplotlib.pyplot as plt


# ========================================
# 1. Create Dataset
# ========================================

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [25, 30, 40, 45, 50, 60, 65, 75, 80, 90]
}

df = pd.DataFrame(data)

print("Complete Dataset:")
print(df)


# ========================================
# 2. Separate Input and Target
# ========================================

X = df[["Study_Hours"]]
y = df["Marks"]

print("\nInput Feature (X):")
print(X)

print("\nTarget Variable (y):")
print(y)


# ========================================
# 3. Train-Test Split
# ========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Input:")
print(X_train)

print("\nTesting Input:")
print(X_test)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))


# ========================================
# 4. Create and Train Model
# ========================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Training Completed!")

print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)


# ========================================
# 5. Make Predictions
# ========================================

y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)


# ========================================
# 6. Actual vs Predicted
# ========================================

result = pd.DataFrame({
    "Study_Hours": X_test["Study_Hours"].values,
    "Actual_Marks": y_test.values,
    "Predicted_Marks": y_pred
})

print("\nActual vs Predicted Results:")
print(result)


# ========================================
# 7. Model Evaluation
# ========================================

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)


# ========================================
# 8. Predict New Student
# ========================================

new_student = pd.DataFrame({
    "Study_Hours": [7.5]
})

predicted_marks = model.predict(new_student)

print("\nNew Student Study Hours: 7.5")
print("Predicted Marks:", predicted_marks[0])


# ========================================
# 9. Visualization
# ========================================

plt.scatter(
    X["Study_Hours"],
    y,
    color="blue",
    label="Actual Marks"
)

plt.plot(
    X["Study_Hours"],
    model.predict(X),
    color="red",
    label="Best-Fit Regression Line"
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.title(
    "Simple Linear Regression: Study Hours vs Marks"
)

plt.legend()
plt.grid(True)

plt.show()
```

---

# 22. Complete Dry Run

Now let's understand the program **line by line**.

---

## STEP 1 — Import Libraries

```python
import pandas as pd
```

Pandas is used to work with tabular data.

```python
from sklearn.model_selection import train_test_split
```

Used to divide data into training and testing sets.

```python
from sklearn.linear_model import LinearRegression
```

Imports the Linear Regression algorithm.

```python
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
```

Used to calculate evaluation metrics.

```python
import matplotlib.pyplot as plt
```

Used to create graphs.

---

# STEP 2 — Create Dataset

```python
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8,9,10],
    "Marks": [25,30,40,45,50,60,65,75,80,90]
}
```

We have 10 students.

| Student | Study Hours | Marks |
|---:|---:|---:|
| 1 | 1 | 25 |
| 2 | 2 | 30 |
| 3 | 3 | 40 |
| 4 | 4 | 45 |
| 5 | 5 | 50 |
| 6 | 6 | 60 |
| 7 | 7 | 65 |
| 8 | 8 | 75 |
| 9 | 9 | 80 |
| 10 | 10 | 90 |

---

# STEP 3 — Create DataFrame

```python
df = pd.DataFrame(data)
```

Now Python creates a DataFrame:

```text
   Study_Hours  Marks
0            1     25
1            2     30
2            3     40
3            4     45
4            5     50
5            6     60
6            7     65
7            8     75
8            9     80
9           10     90
```

---

# STEP 4 — Separate X and y

```python
X = df[["Study_Hours"]]
```

`X` contains the input feature.

```text
X = Study_Hours
```

---

```python
y = df["Marks"]
```

`y` contains the target.

```text
y = Marks
```

Therefore:

```text
X → Study Hours
y → Marks
```

---

# STEP 5 — Train-Test Split

```python
test_size=0.2
```

There are 10 records.

```text
80% → 8 training records
20% → 2 testing records
```

With:

```python
random_state=42
```

the split is reproducible.

For this exact code, the test records are:

| Study Hours | Marks |
|---:|---:|
| 9 | 80 |
| 2 | 30 |

Therefore:

```text
X_test = [9, 2]
y_test = [80, 30]
```

The remaining records are used for training.

---

# STEP 6 — Create Model

```python
model = LinearRegression()
```

At this point we have created the Linear Regression model.

But it has not learned anything yet.

```text
model = created
model ≠ trained
```

---

# STEP 7 — Train Model

```python
model.fit(X_train, y_train)
```

Now the model learns the relationship:

```text
Study Hours → Marks
```

It learns two important parameters:

```text
m → slope
c → intercept
```

For this exact dataset and split, approximately:

```text
Slope = 7.1552

Intercept = 16.8966
```

Therefore the learned equation is approximately:

$$
\hat{y}=7.1552x+16.8966
$$

---

# STEP 8 — Predict Test Data

Test inputs:

```text
Study Hours = 9
Study Hours = 2
```

The model applies:

$$
\hat{y}=7.1552x+16.8966
$$

---

## For Study Hours = 9

$$
\hat{y}
=
7.1552(9)+16.8966
$$

Approximately:

```text
81.29
```

Actual:

```text
80
```

Error:

$$
80-81.29\approx-1.29
$$

---

## For Study Hours = 2

$$
\hat{y}
=
7.1552(2)+16.8966
$$

Approximately:

```text
31.21
```

Actual:

```text
30
```

Error:

$$
30-31.21\approx-1.21
$$

---

# STEP 9 — Actual vs Predicted

The result becomes approximately:

| Study Hours | Actual Marks | Predicted Marks |
|---:|---:|---:|
| 9 | 80 | 81.29 |
| 2 | 30 | 31.21 |

This table is extremely useful because it directly shows model performance.

---

# STEP 10 — Calculate MAE

Errors are approximately:

```text
-1.29
-1.21
```

Absolute errors:

```text
1.29
1.21
```

Average:

$$
MAE
\approx
\frac{1.29+1.21}{2}
$$

$$
MAE \approx 1.25
$$

So:

```text
MAE ≈ 1.25
```

### Meaning

The predictions are off by approximately:

```text
1.25 marks on average
```

---

# STEP 11 — Calculate MSE

Square the errors:

```text
(-1.29)²
(-1.21)²
```

Then take the average.

The result for this exact split is approximately:

```text
MSE = 1.5644
```

---

# STEP 12 — Calculate RMSE

Your current code does **not** calculate RMSE, but we can calculate it from MSE:

$$
RMSE=\sqrt{MSE}
$$

Approximately:

```text
RMSE ≈ 1.25
```

---

# STEP 13 — Calculate R²

Your code calculates:

```python
r2 = r2_score(y_test, y_pred)
```

For this exact split:

```text
R² ≈ 0.9975
```

That is approximately:

```text
99.75%
```

of the test-set variation explained by the fitted model.

---

# STEP 14 — Predict a New Student

The code creates:

```python
new_student = pd.DataFrame({
    "Study_Hours": [7.5]
})
```

The model receives:

```text
7.5 study hours
```

The learned equation is approximately:

$$
\hat{y}=7.1552(7.5)+16.8966
$$

Therefore:

```text
Predicted Marks ≈ 70.56
```

### Final prediction

```text
Study Hours = 7.5
Predicted Marks ≈ 70.56
```

---

# 23. Output Explanation

The important output values for this exact code are approximately:

```text
Slope (Coefficient): 7.15517241

Intercept: 16.89655172

Predicted Marks:
[81.29310345 31.20689655]

MAE:
1.25

MSE:
1.56435791

R2 Score:
0.99749703

New Student Study Hours: 7.5

Predicted Marks:
70.56034483
```

---

# 24. Prediction for New Student

The most important practical part is:

```python
new_student = pd.DataFrame({
    "Study_Hours": [7.5]
})

predicted_marks = model.predict(new_student)
```

The trained model predicts:

```text
7.5 Study Hours
        ↓
Linear Regression
        ↓
70.56 Marks
```

This demonstrates the actual purpose of Machine Learning:

> Learn from existing data and use the learned pattern to make predictions on new data.

---

# 25. Graph Explanation

The code:

```python
plt.scatter(
    X["Study_Hours"],
    y
)
```

creates the actual data points.

```text
● = Actual student data
```

Then:

```python
plt.plot(
    X["Study_Hours"],
    model.predict(X)
)
```

creates the regression line.

Conceptually:

```text
Marks
  |
90|                         ●
80|                      ●
70|                   ●
60|                ●
50|             ●
40|          ●
30|       ●
20|    ●
  |       ╱
  |     ╱   ← Best-Fit Line
  |   ╱
  +-------------------------- Study Hours
```

The red line in your code represents the:

```text
Best-Fit Regression Line
```

---

# 26. Advantages

### ✅ 1. Simple

Easy to understand.

### ✅ 2. Fast

Training is generally fast for small/simple problems.

### ✅ 3. Interpretable

The coefficient gives information about the relationship between the feature and target.

### ✅ 4. Good baseline

Linear Regression is often a useful first model for regression problems.

### ✅ 5. Easy to visualize

With one feature, we can easily plot:

```text
X vs y
```

---

# 27. Limitations

### ❌ 1. Assumes a linear relationship

If the true relationship is strongly nonlinear, a simple straight line may not work well.

### ❌ 2. Sensitive to outliers

Extreme observations can influence the fitted line.

### ❌ 3. Only one feature

Simple Linear Regression uses one independent variable.

For multiple features, use:

```text
Multiple Linear Regression
```

### ❌ 4. Correlation is not causation

A strong relationship does not automatically mean that one variable causes another.

---

# 28. Interview Questions

## Q1. What is Simple Linear Regression?

Simple Linear Regression is a supervised learning algorithm used to predict a continuous numerical target using one independent variable.

---

## Q2. What is the equation of Linear Regression?

$$
\hat{y}=mx+c
$$

Where:

- $\hat{y}$ = predicted value
- $m$ = slope
- $x$ = input
- $c$ = intercept

---

## Q3. What is the purpose of the best-fit line?

The best-fit line represents the relationship between the independent variable and target while minimizing the overall prediction error according to the chosen objective.

---

## Q4. What is residual/error?

Residual is the difference between actual and predicted values.

$$
e=y-\hat{y}
$$

---

## Q5. What is MSE?

MSE is Mean Squared Error.

$$
MSE=
\frac{1}{n}
\sum(y_i-\hat{y}_i)^2
$$

It penalizes larger errors more strongly because errors are squared.

---

## Q6. What is MAE?

MAE is Mean Absolute Error.

$$
MAE=
\frac{1}{n}
\sum|y_i-\hat{y}_i|
$$

It represents the average absolute prediction error.

---

## Q7. What is RMSE?

RMSE is the square root of MSE.

$$
RMSE=\sqrt{MSE}
$$

---

## Q8. What is R²?

R² measures the proportion of target variation explained by the model relative to a mean-only baseline.

$$
R^2=
1-\frac{SS_{res}}{SS_{tot}}
$$

---

## Q9. What is Adjusted R²?

Adjusted R² modifies R² by accounting for the number of predictors and sample size.

$$
R^2_{adj}
=
1-
\frac{(1-R^2)(n-1)}
{n-k-1}
$$

---

## Q10. Why is Adjusted R² useful?

It helps evaluate whether adding predictors provides enough explanatory value to justify their inclusion.

---

## Q11. What is Gradient Descent?

Gradient Descent is an optimization method that repeatedly updates model parameters in the direction that reduces the cost function.

---

## Q12. What is learning rate?

The learning rate controls the size of each update during Gradient Descent.

```text
Small learning rate → Slow learning

Large learning rate → Can overshoot or become unstable
```

---

## Q13. What is overfitting?

Overfitting occurs when a model learns the training data too closely, including noise, and performs poorly on unseen data.

---

## Q14. What is underfitting?

Underfitting occurs when the model is too simple to capture the important patterns in the data.

---

## Q15. What is the difference between R² and Adjusted R²?

| R² | Adjusted R² |
|---|---|
| Measures explained variation | Measures explained variation while accounting for predictors |
| Does not penalize adding predictors | Penalizes unnecessary predictors |
| Can increase when features are added | Can increase or decrease |
| Useful for model fit | Useful when comparing models with different numbers of predictors |

---

# 29. Quick Revision

## 🧠 Simple Linear Regression Flow

```text
Dataset
   ↓
Identify X and y
   ↓
Train-Test Split
   ↓
Create LinearRegression()
   ↓
model.fit()
   ↓
Learn m and c
   ↓
model.predict()
   ↓
Compare Actual vs Predicted
   ↓
Evaluate Model
   ↓
MAE / MSE / RMSE / R²
   ↓
Predict New Data
```

---

# ⭐ Formula Cheat Sheet

### Linear Equation

$$
\hat{y}=mx+c
$$

### Error

$$
e=y-\hat{y}
$$

### MSE

$$
MSE=
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
$$

### MAE

$$
MAE=
\frac{1}{n}
\sum_{i=1}^{n}
|y_i-\hat{y}_i|
$$

### RMSE

$$
RMSE=\sqrt{MSE}
$$

### R²

$$
R^2=
1-\frac{SS_{res}}{SS_{tot}}
$$

### Adjusted R²

$$
R^2_{adj}
=
1-
\frac{(1-R^2)(n-1)}
{n-k-1}
$$

### Gradient Descent

$$
m:=m-\alpha\frac{\partial J}{\partial m}
$$

$$
c:=c-\alpha\frac{\partial J}{\partial c}
$$

---

# 🏆 Final Understanding

For this project:

```text
INPUT
Study Hours
     ↓
     ↓
Linear Regression
     ↓
Learns:
m = slope
c = intercept
     ↓
Best-Fit Line
     ↓
OUTPUT
Predicted Marks
```

Our model learned approximately:

$$
\hat{y}=7.1552x+16.8966
$$

For a new student studying **7.5 hours**:

$$
\hat{y}\approx70.56
$$

So:

```text
📚 Study Hours = 7.5

        ↓

🤖 Linear Regression

        ↓

📊 Predicted Marks ≈ 70.56
```

---

# 🎯 What You Should Learn Next

After Simple Linear Regression, follow this order:

```text
✅ Simple Linear Regression
        ↓
➡️ Multiple Linear Regression
        ↓
➡️ MAE / MSE / RMSE deeply
        ↓
➡️ Gradient Descent
        ↓
➡️ R² / Adjusted R²
        ↓
➡️ Feature Selection
        ↓
➡️ Bias-Variance Trade-off
        ↓
➡️ Logistic Regression
```

> **Important:** Don't just memorize the formulas. Understand the flow:
>
> **Data → Best-Fit Line → Error → Cost → Optimization → Prediction → Evaluation**