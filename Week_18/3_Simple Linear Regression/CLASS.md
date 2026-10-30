# 📈 Simple Linear Regression

> **Machine Learning — Supervised Learning → Regression**

Simple Linear Regression is one of the most important starting points for understanding **Machine Learning**, because it introduces:

- Best-fit line
- Prediction
- Error / Residual
- Cost Function
- Gradient Descent
- MSE, MAE, RMSE
- R² Score
- Adjusted R² Score
- Feature Selection
- Model Evaluation
- Bias and Variance

---

# 📚 Table of Contents

1. [What is Simple Linear Regression?](#1-what-is-simple-linear-regression)
2. [Real-World Example](#2-real-world-example)
3. [Best-Fit Line](#3-best-fit-line)
4. [Understanding the Formula](#4-understanding-the-formula)
5. [Prediction and Error](#5-prediction-and-error)
6. [Cost Function](#6-cost-function)
7. [Why Do We Need a Cost Function?](#7-why-do-we-need-a-cost-function)
8. [Gradient Descent](#8-gradient-descent)
9. [Partial Derivatives](#9-partial-derivatives)
10. [Learning Rate](#10-learning-rate)
11. [MSE](#11-mean-squared-error-mse)
12. [MAE](#12-mean-absolute-error-mae)
13. [RMSE](#13-root-mean-squared-error-rmse)
14. [MSE vs MAE vs RMSE](#14-mse-vs-mae-vs-rmse)
15. [R² Score](#15-r2-score)
16. [Adjusted R² Score](#16-adjusted-r2-score)
17. [R² vs Adjusted R²](#17-r2-vs-adjusted-r2)
18. [Feature Selection](#18-feature-selection)
19. [Relevant vs Irrelevant Features](#19-relevant-vs-irrelevant-features)
20. [Effect of Adding Independent Variables](#20-effect-of-adding-independent-variables)
21. [Model Evaluation](#21-model-evaluation)
22. [Bias and Variance](#22-bias-and-variance)
23. [Bias-Variance Trade-off](#23-bias-variance-trade-off)
24. [Jupyter Notebook](#24-jupyter-notebook)
25. [Complete Learning Flow](#25-complete-learning-flow)
26. [Interview Questions](#26-interview-questions)
27. [Quick Revision](#27-quick-revision)

---

# 1. What is Simple Linear Regression?

## 📌 Definition

**Simple Linear Regression** is a supervised machine learning algorithm used to predict a **continuous numerical value** using **one independent variable**.

### Example

Suppose we want to predict a student's exam score based on study hours.

| Study Hours | Exam Score |
|---:|---:|
| 1 | 35 |
| 2 | 42 |
| 3 | 50 |
| 4 | 58 |
| 5 | 65 |

Here:

- `Study Hours` → Independent variable ($X$)
- `Exam Score` → Dependent variable ($Y$)

The model tries to find the best line that represents the relationship between them.

---

# 2. Real-World Example

Imagine:

```text
Study Hours  →  Exam Score
     X       →      Y
```

If a student studies more hours, the exam score may increase.

We can use the relationship to predict:

```text
Study Hours = 6
        ↓
Machine Learning Model
        ↓
Predicted Score = 72
```

This is a **regression problem** because the output is numerical.

---

# 3. Best-Fit Line

The main goal of Simple Linear Regression is to find the **best-fit line**.


The best-fit line should be as close as possible to the observed data points.

The equation of the line is:

$$
\hat{y} = mx + b
$$

Where:

| Symbol | Meaning |
|---|---|
| $x$ | Independent variable |
| $\hat{y}$ | Predicted value |
| $m$ | Slope |
| $b$ | Intercept |

---

# 4. Understanding the Formula

## Formula

$$
\hat{y} = mx + b
$$

Let's understand every part.

### $x$

Input / independent variable.

Example:

```text
Study Hours = 5
```

### $\hat{y}$

Predicted output.

Example:

```text
Predicted Score = 65
```

The `hat` symbol means **prediction**.

### $m$

Slope of the line.

It tells us how much the predicted value changes when $x$ increases by one unit.

### $b$

Intercept.

It is the predicted value of $y$ when:

$$
x = 0
$$

---

# 5. Prediction and Error

The model gives a prediction:

$$
\hat{y} = mx + b
$$

But the actual value may be different.

### Example

Actual score:

```text
y = 70
```

Predicted score:

```text
ŷ = 65
```

The error is:

$$
e = y - \hat{y}
$$

Therefore:

$$
e = 70 - 65
$$

$$
e = 5
$$

So the model made an error of `5`.

---

## 🔹 Residual

The difference between the actual value and predicted value is called the **residual**.

$$
e_i = y_i - \hat{y}_i
$$

Where:

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value
- $e_i$ = residual/error

---

# 6. Cost Function

A dataset contains many observations.

Therefore, we don't want to look at only one error.

We need to calculate the total error of the model.

The screenshot uses the idea:

$$
E = d_1^2 + d_2^2 + d_3^2 + \cdots + d_n^2
$$

This represents the **sum of squared errors**.

For Linear Regression, the cost can be written as:

$$
J(m,b) =
\frac{1}{n}
\sum_{i=1}^{n}
\left(y_i-(mx_i+b)\right)^2
$$

### Where:

| Symbol | Meaning |
|---|---|
| $J(m,b)$ | Cost function |
| $n$ | Number of observations |
| $y_i$ | Actual value |
| $x_i$ | Input value |
| $mx_i+b$ | Predicted value |
| $y_i-(mx_i+b)$ | Error |
| $m$ | Slope |
| $b$ | Intercept |

---

# 7. Why Do We Need a Cost Function?

There can be many possible lines.

```text
Line 1 → Large errors
Line 2 → Medium errors
Line 3 → Small errors
```

We want the line with the **smallest overall error**.

Therefore:

$$
\boxed{\text{Best Line} \to \text{Minimum Cost}}
$$

The goal of Linear Regression is to find the values of:

$$
m
$$

and

$$
b
$$

that minimize the cost function.

---

# 8. Gradient Descent

## 📌 Definition

**Gradient Descent** is an optimization algorithm used to find the values of model parameters that minimize the cost function.

In Simple Linear Regression, the parameters are:

```text
m → slope
b → intercept
```

The idea is:

```text
Start with some m and b
        ↓
Calculate cost
        ↓
Calculate gradient
        ↓
Update m and b
        ↓
Calculate cost again
        ↓
Repeat
        ↓
Minimum cost
```

---

## ⛰️ Simple Intuition

Imagine standing on a hill.

Your goal is to reach the lowest point.

```text
        ●
       /
      /
     /
    \       /
     \     /
      \___/
        ↑
     Minimum
```

Gradient Descent repeatedly moves toward the direction where the cost decreases.

---

# 9. Partial Derivatives

To know which direction to move, we calculate derivatives of the cost function.

The cost function is:

$$
J(m,b)=
\frac{1}{n}
\sum_{i=1}^{n}
\left(y_i-(mx_i+b)\right)^2
$$

We calculate the partial derivative with respect to $m$:

$$
\frac{\partial J}{\partial m}
=
-\frac{2}{n}
\sum_{i=1}^{n}
x_i
\left[y_i-(mx_i+b)\right]
$$

And with respect to $b$:

$$
\frac{\partial J}{\partial b}
=
-\frac{2}{n}
\sum_{i=1}^{n}
\left[y_i-(mx_i+b)\right]
$$

These gradients tell us how the cost changes when we change $m$ or $b$.

---

# 10. Learning Rate

Gradient Descent uses a parameter called the **learning rate**.

It is commonly represented by:

$$
\alpha
$$

The update rule for $m$ is:

$$
m := m -
\alpha
\frac{\partial J}{\partial m}
$$

The update rule for $b$ is:

$$
b := b -
\alpha
\frac{\partial J}{\partial b}
$$

### Learning Rate Meaning

The learning rate controls **how large each step is**.

```text
Small α
↓
Small steps
↓
Slow learning

Large α
↓
Large steps
↓
May overshoot minimum
```

So we need an appropriate learning rate.

---

# 11. Mean Squared Error (MSE)

## 📌 Definition

MSE stands for:

> **Mean Squared Error**

It calculates the average of the squared errors.

$$
MSE =
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
$$

### Why square the error?

Suppose:

```text
Error 1 = +5
Error 2 = -5
```

If we simply add them:

$$
5 + (-5) = 0
$$

The errors cancel each other.

Therefore, we square them:

$$
5^2 + (-5)^2
$$

$$
=25+25
$$

$$
=50
$$

So positive and negative errors do not cancel.

---

# 12. Mean Absolute Error (MAE)

## 📌 Definition

MAE stands for:

> **Mean Absolute Error**

It calculates the average absolute error.

$$
MAE =
\frac{1}{n}
\sum_{i=1}^{n}
|y_i-\hat{y}_i|
$$

The absolute value makes all errors positive.

### Example

Errors:

```text
+5
-3
+2
-4
```

Absolute errors:

```text
5
3
2
4
```

MAE:

$$
MAE = \frac{5+3+2+4}{4}
$$

$$
MAE = 3.5
$$

---

# 13. Root Mean Squared Error (RMSE)

RMSE stands for:

> **Root Mean Squared Error**

Formula:

$$
RMSE =
\sqrt{
\frac{1}{n}
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
}
$$

RMSE is simply:

$$
RMSE = \sqrt{MSE}
$$

### Why take the square root?

MSE is expressed in squared units.

If the target is measured in:

```text
₹
```

MSE is approximately in:

```text
₹²
```

RMSE returns the error to the original unit:

```text
₹
```

---

# 14. MSE vs MAE vs RMSE

| Metric | Formula | Main Idea |
|---|---|---|
| MAE | $\frac{1}{n}\sum|y-\hat y|$ | Average absolute error |
| MSE | $\frac{1}{n}\sum(y-\hat y)^2$ | Average squared error |
| RMSE | $\sqrt{MSE}$ | Error in original target units |

### Sensitivity to Outliers

```text
MAE
 ↓
Less sensitive to large errors

MSE
 ↓
More sensitive to large errors

RMSE
 ↓
More sensitive to large errors
```

---

# 15. R² Score

## 📌 Definition

$R^2$ is called the **R-squared score** or **coefficient of determination**.

It tells us how much of the variation in the target variable is explained by the model.

Formula:

$$
R^2 =
1 -
\frac{SS_{res}}{SS_{tot}}
$$

Where:

### Residual Sum of Squares

$$
SS_{res}
=
\sum_{i=1}^{n}
(y_i-\hat{y}_i)^2
$$

### Total Sum of Squares

$$
SS_{tot}
=
\sum_{i=1}^{n}
(y_i-\bar{y})^2
$$

Therefore:

$$
R^2 =
1 -
\frac{
\sum(y_i-\hat{y}_i)^2
}{
\sum(y_i-\bar{y})^2
}
$$

---

## 📊 Interpretation

Suppose:

$$
R^2 = 0.90
$$

This means the model explains approximately:

```text
90% of the variation in the target
```

The remaining variation is not explained by the model.

---

## Typical Interpretation

| $R^2$ | Interpretation |
|---:|---|
| 1.0 | Perfect fit |
| 0.9 | Very strong explanatory fit |
| 0.7 | Reasonably strong |
| 0.5 | Moderate |
| 0 | No improvement over predicting the mean |
| < 0 | Can be worse than the mean baseline |

> **Important:** A high $R^2$ does not automatically mean the model is good for every purpose. We should also evaluate generalization and other metrics.

---

# 16. Adjusted R² Score

## 📌 Why do we need Adjusted R²?

Suppose we have:

```text
Study Hours
```

and we add:

```text
Attendance
```

The new feature may help the model.

But what happens if we add:

```text
Student ID
```

or another irrelevant column?

We don't want irrelevant variables to make the model appear better simply because more variables were added.

Adjusted $R^2$ considers the number of independent variables.

---

## Formula

$$
R^2_{adj}
=
1-
\frac{
(1-R^2)(n-1)
}{
n-k-1
}
$$

Where:

| Symbol | Meaning |
|---|---|
| $R^2$ | R-squared score |
| $n$ | Number of observations |
| $k$ | Number of independent variables/features |
| $R^2_{adj}$ | Adjusted R-squared |

---

## ⭐ Important Point

Adding a feature does **not necessarily increase Adjusted $R^2$**.

If the feature provides enough useful explanatory information:

```text
Adjusted R²
     ↑
```

If the feature is unnecessary:

```text
Adjusted R²
     ↓
```

Therefore, Adjusted $R^2$ can help us identify whether additional predictors are actually useful.

---

# 17. R² vs Adjusted R²

| R² | Adjusted R² |
|---|---|
| Measures explained variation | Measures explained variation while accounting for number of predictors |
| Generally does not decrease when predictors are added | Can increase or decrease |
| More predictors can make R² increase | Penalizes unnecessary predictors |
| Useful for model fit | Useful when comparing models with different numbers of predictors |

### Easy Memory Trick

```text
R²
↓
How much variation is explained?

Adjusted R²
↓
How much variation is explained
after considering the number of features?
```

---

# 18. Feature Selection

## 📌 What is a Feature?

A **feature** is an input variable used by the model.

Example:

| Study Hours | Attendance | Age | Student ID | Exam Score |
|---:|---:|---:|---:|---:|
| 2 | 80 | 20 | 101 | 45 |
| 4 | 90 | 21 | 102 | 65 |
| 6 | 95 | 22 | 103 | 80 |

Here:

```text
Features:
Study Hours
Attendance
Age
Student ID

Target:
Exam Score
```

---

## 🎯 Feature Selection

Feature selection means choosing the **useful input variables** for the model.

Example:

```text
Original features

Study Hours
Attendance
Age
Student ID
Random Column
       ↓
Feature Selection
       ↓
Study Hours
Attendance
Age
```

---

# 19. Relevant vs Irrelevant Features

## ✅ Relevant Feature

A relevant feature has useful information related to the target.

Example:

```text
Study Hours → Exam Score
```

Study hours may help predict exam score.

---

## ❌ Irrelevant Feature

An irrelevant feature provides little or no useful information.

Example:

```text
Student ID → Exam Score
```

A student ID is generally an identifier, not a meaningful predictor of academic performance.

---

## Example

Suppose:

```text
Model 1:
Study Hours
        ↓
Exam Score

R² = 0.80
```

Now add an irrelevant column:

```text
Model 2:
Study Hours
Student ID
        ↓
Exam Score
```

The model may show a slightly different $R^2$, but that does not mean Student ID is genuinely useful.

Adjusted $R^2$ helps account for the additional predictor.

---

# 20. Effect of Adding Independent Variables

Consider:

### Model 1

```text
X1 → Y

R² = 0.80
Adjusted R² = 0.79
```

Add a useful feature:

```text
X1 + X2 → Y

R² = 0.88
Adjusted R² = 0.87
```

This is a good sign.

---

Now add an unnecessary feature:

```text
X1 + X2 + X3 → Y
```

Possible result:

```text
R²
↑ slightly

Adjusted R²
↓
```

This tells us that the additional variable may not provide enough useful explanatory power.

---

# 21. Model Evaluation

After training a regression model, we need to evaluate it.

A typical workflow is:

```text
Dataset
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Train Model
   ↓
Make Predictions
   ↓
Calculate Metrics
   ↓
Interpret Results
```

---

## Important Regression Metrics

### 1. MAE

$$
MAE =
\frac{1}{n}
\sum|y_i-\hat{y}_i|
$$

### 2. MSE

$$
MSE =
\frac{1}{n}
\sum(y_i-\hat{y}_i)^2
$$

### 3. RMSE

$$
RMSE = \sqrt{MSE}
$$

### 4. R²

$$
R^2 =
1-\frac{SS_{res}}{SS_{tot}}
$$

### 5. Adjusted R²

$$
R^2_{adj}
=
1-
\frac{(1-R^2)(n-1)}
{n-k-1}
$$

---

# 22. Bias and Variance

Two important concepts in Machine Learning are:

```text
Bias
Variance
```

They help us understand why a model may not generalize well.

---

## 🔵 Bias

**Bias** is error caused by a model being too simple or making strong assumptions.

### High Bias

```text
Model too simple
      ↓
Misses important patterns
      ↓
Underfitting
```

Example:

Trying to represent a complex relationship with an overly simple model.

---

## 🔴 Variance

**Variance** is related to how sensitive a model is to the particular training data.

### High Variance

```text
Model learns training data too closely
          ↓
Learns noise
          ↓
Excellent training performance
          ↓
Poor test performance
          ↓
Overfitting
```

---

# 23. Bias-Variance Trade-off

The goal is not:

```text
Minimum bias only
```

or:

```text
Minimum variance only
```

The goal is to find a good balance.

```text
High Bias
   ↓
Underfitting

        GOOD BALANCE

   ↓
Generalizes well

High Variance
   ↓
Overfitting
```

### Simple Table

| Situation | Bias | Variance | Problem |
|---|---|---|---|
| Too simple | High | Low | Underfitting |
| Good model | Balanced | Balanced | Good generalization |
| Too complex | Low | High | Overfitting |

---

## 🎯 Main Goal

The ultimate goal of Machine Learning is:

> **Good generalization to unseen data.**

A model should not simply memorize the training data.

It should learn meaningful patterns that also work on new data.

---

# 24. Jupyter Notebook

The screenshots also introduce the use of **Jupyter Notebook** for Machine Learning experiments.

Jupyter Notebook allows us to:

- Write Python code
- Execute code cell-by-cell
- Display outputs
- Create graphs
- Experiment with Machine Learning models
- Document explanations beside code

Typical workflow:

```text
Jupyter Notebook
      ↓
Import Libraries
      ↓
Load Dataset
      ↓
Explore Data
      ↓
Select Features
      ↓
Train Model
      ↓
Predict
      ↓
Evaluate
      ↓
Visualize Results
```

---

## Example

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

For Linear Regression:

```python
from sklearn.linear_model import LinearRegression
```

Create the model:

```python
model = LinearRegression()
```

Train:

```python
model.fit(X_train, y_train)
```

Predict:

```python
y_pred = model.predict(X_test)
```

Evaluate:

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```

---

# 25. Complete Learning Flow

The concepts from the screenshots can be connected as follows:

```text
                 Simple Linear Regression
                           │
                           ↓
                    Best-Fit Line
                           │
                           ↓
                    Prediction
                           │
                           ↓
                    Calculate Error
                           │
                           ↓
                     Cost Function
                           │
                           ↓
                    Gradient Descent
                           │
                           ↓
                    Find Best m and b
                           │
                           ↓
                     Make Predictions
                           │
                           ↓
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
            MAE           MSE           RMSE
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                       R² Score
                           ↓
                   Adjusted R² Score
                           ↓
                  Feature Selection
                           ↓
                Model Evaluation
                           ↓
                  Bias / Variance
                           ↓
                  Generalization
```

---

# 🧠 26. Important Concepts to Remember

## 1️⃣ Best-Fit Line

Find the line that minimizes prediction errors.

$$
\hat{y}=mx+b
$$

---

## 2️⃣ Error

Difference between actual and predicted value.

$$
e=y-\hat{y}
$$

---

## 3️⃣ Cost

Measures the overall model error.

$$
J(m,b)=
\frac{1}{n}
\sum
(y_i-(mx_i+b))^2
$$

---

## 4️⃣ Gradient Descent

Used to minimize the cost function.

$$
m := m-\alpha\frac{\partial J}{\partial m}
$$

$$
b := b-\alpha\frac{\partial J}{\partial b}
$$

---

## 5️⃣ MSE

Penalizes large errors more strongly because errors are squared.

$$
MSE=
\frac{1}{n}
\sum(y_i-\hat{y}_i)^2
$$

---

## 6️⃣ MAE

Average absolute error.

$$
MAE=
\frac{1}{n}
\sum|y_i-\hat{y}_i|
$$

---

## 7️⃣ RMSE

Square root of MSE.

$$
RMSE=\sqrt{MSE}
$$

---

## 8️⃣ R²

Measures explained variation.

$$
R^2=
1-\frac{SS_{res}}{SS_{tot}}
$$

---

## 9️⃣ Adjusted R²

Considers the number of independent variables.

$$
R^2_{adj}
=
1-
\frac{(1-R^2)(n-1)}
{n-k-1}
$$

---

## 🔟 Feature Selection

Choose useful features and avoid unnecessary variables.

---

## 1️⃣1️⃣ Bias

```text
High Bias → Underfitting
```

---

## 1️⃣2️⃣ Variance

```text
High Variance → Overfitting
```

---

# 🎤 27. Interview Questions

## Q1. What is Simple Linear Regression?

Simple Linear Regression is a supervised learning algorithm used to predict a continuous numerical target using one independent variable.

---

## Q2. What is the equation of Simple Linear Regression?

$$
\hat{y}=mx+b
$$

Where $m$ is the slope and $b$ is the intercept.

---

## Q3. What is a residual?

A residual is the difference between the actual and predicted value.

$$
e=y-\hat{y}
$$

---

## Q4. What is the purpose of the cost function?

The cost function measures the overall error of the model. Training tries to minimize this cost.

---

## Q5. What is Gradient Descent?

Gradient Descent is an optimization algorithm used to minimize the cost function by repeatedly updating model parameters in the direction that reduces the cost.

---

## Q6. What is the learning rate?

The learning rate $\alpha$ controls the size of each update made during Gradient Descent.

---

## Q7. What is MSE?

MSE is the average of squared prediction errors.

$$
MSE=
\frac{1}{n}
\sum(y_i-\hat{y}_i)^2
$$

---

## Q8. What is MAE?

MAE is the average absolute prediction error.

$$
MAE=
\frac{1}{n}
\sum|y_i-\hat{y}_i|
$$

---

## Q9. What is RMSE?

RMSE is the square root of MSE.

$$
RMSE=\sqrt{MSE}
$$

---

## Q10. What is R²?

R² measures the proportion of variation in the target explained by the regression model.

---

## Q11. What is Adjusted R²?

Adjusted R² is a modified version of R² that accounts for the number of independent variables in the model.

---

## Q12. Can R² increase when we add a feature?

Yes. R² generally does not decrease when additional predictors are added.

However, the added feature may not be useful.

---

## Q13. Can Adjusted R² decrease after adding a feature?

Yes.

If the new feature does not provide enough explanatory value, Adjusted R² can decrease.

---

## Q14. What is feature selection?

Feature selection is the process of selecting useful input variables and removing unnecessary or irrelevant variables.

---

## Q15. What is high bias?

High bias usually means the model is too simple and may underfit the data.

---

## Q16. What is high variance?

High variance means the model is too sensitive to the training data and may overfit.

---

# ⚡ 28. One-Minute Revision

```text
Simple Linear Regression
        ↓
Predict continuous value
        ↓
ŷ = mx + b
        ↓
Calculate Error
        ↓
e = y - ŷ
        ↓
Cost Function
        ↓
Minimize Cost
        ↓
Gradient Descent
        ↓
Find best m and b
        ↓
Evaluate Model
        ↓
MAE
MSE
RMSE
R²
Adjusted R²
        ↓
Check Features
        ↓
Relevant / Irrelevant
        ↓
Check Bias & Variance
        ↓
Generalization
```

---

# ✅ Final Checklist

Before moving to **Multiple Linear Regression**, make sure you understand:

- [ ] What is Simple Linear Regression?
- [ ] What is supervised learning?
- [ ] What is regression?
- [ ] What is an independent variable?
- [ ] What is a dependent variable?
- [ ] What is the best-fit line?
- [ ] What does $m$ represent?
- [ ] What does $b$ represent?
- [ ] What is prediction?
- [ ] What is residual/error?
- [ ] What is the cost function?
- [ ] Why do we square errors?
- [ ] What is Gradient Descent?
- [ ] What is a partial derivative?
- [ ] What is learning rate?
- [ ] What is MSE?
- [ ] What is MAE?
- [ ] What is RMSE?
- [ ] What is R²?
- [ ] What is Adjusted R²?
- [ ] Why can Adjusted R² decrease?
- [ ] What is feature selection?
- [ ] What is a relevant feature?
- [ ] What is an irrelevant feature?
- [ ] What is bias?
- [ ] What is variance?
- [ ] What is underfitting?
- [ ] What is overfitting?
- [ ] What is generalization?
- [ ] How do we evaluate a regression model?

---

# 🎯 Key Takeaway

The most important idea from this chapter is:

> **Simple Linear Regression tries to find the best values of $m$ and $b$ so that the prediction error is minimized.**

The complete idea is:

$$
\boxed{
\text{Data}
\to
\text{Best-Fit Line}
\to
\text{Prediction}
\to
\text{Error}
\to
\text{Cost}
\to
\text{Gradient Descent}
\to
\text{Evaluation}
}
$$

And after fitting the model, we should not look only at one metric. We should consider:

$$
\boxed{
MAE,\ MSE,\ RMSE,\ R^2,\ Adjusted\ R^2
}
$$

and also consider:

$$
\boxed{
\text{Features}
+
\text{Bias}
+
\text{Variance}
+
\text{Generalization}
}
$$

---

## 🚀 Next Chapter

### Multiple Linear Regression

We will extend:

$$
\hat{y}=mx+b
$$

to:

$$
\hat{y}
=
b_0+b_1x_1+b_2x_2+\cdots+b_kx_k
$$

where the model uses **multiple independent variables** to predict one target.