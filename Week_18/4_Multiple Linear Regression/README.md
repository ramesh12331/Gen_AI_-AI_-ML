Ramesh, let's learn **Multiple Linear Regression (MLR)** in simple English, step by step, based on your screenshots. I'll explain each concept from the basics, including formulas, examples, and Python code for VS Code.

# 📘 Multiple Linear Regression — Complete Explanation

## Topic 1: What Is Regression?

### 1.1 Understanding Regression

**Regression is a supervised machine learning technique used to predict numerical values.**

Examples:
- Predicting a student's marks based on study hours.
- Predicting a house price based on its size.
- Predicting an employee's salary based on experience.
- Predicting sales based on advertising expenditure.

For example, suppose we want to predict a student's marks based on the number of hours they study.

```text
Input: Study Hours
        |
        v
Machine Learning Model
        |
        v
Output: Predicted Marks
```

Here, the model learns the relationship between study hours and marks from historical data.

---

## Topic 2: Simple Linear Regression (SLR)

**Simple Linear Regression uses one independent variable to predict one dependent variable.**

Consider the following dataset:

| Study Hours (X) | Marks (Y) |
|---:|---:|
| 1 | 30 |
| 2 | 40 |
| 3 | 50 |
| 4 | 60 |
| 5 | 70 |

Here:
- `X` = Study Hours
- `Y` = Marks

We want to predict marks using study hours.

### Simple Linear Regression Equation

\[
\boxed{\hat{Y}=\beta_0+\beta_1X}
\]

This is equivalent to the familiar equation:

\[
Y=mX+b
\]

Where:

| Symbol | Meaning |
|---|---|
| \(\hat{Y}\) | Predicted output |
| \(X\) | Independent variable |
| \(\beta_0\) | Intercept |
| \(\beta_1\) | Regression coefficient or slope |

**Remember:** Simple Linear Regression uses one independent variable.

---

# Topic 3: Multiple Linear Regression (MLR)

This is the main topic in your first screenshot.

**Multiple Linear Regression uses two or more independent variables to predict one dependent variable.**

For example, suppose we want to predict an employee's salary.

Salary may be related to:
- Experience
- Skills
- Education
- Performance

We can represent this relationship as follows:

```text
Experience ──────┐
                 |
Skills ──────────┤
                 |
Education ───────┼──> Multiple Linear Regression
                 |              |
Performance ─────┘              v
                         Predicted Salary
```

All these variables are inputs to the model, and salary is the output we want to predict.

### 3.1 Multiple Linear Regression Equation

The general equation is:

\[
\boxed{
\hat{Y}=\beta_0+\beta_1X_1+\beta_2X_2+\cdots+\beta_nX_n
}
\]

Where:

- \(\hat{Y}\) = Predicted output.
- \(\beta_0\) = Intercept.
- \(\beta_1\) = Coefficient of the first feature.
- \(\beta_2\) = Coefficient of the second feature.
- \(X_1\) = First independent variable.
- \(X_2\) = Second independent variable.
- \(n\) = Number of independent variables.

### 3.2 Practical Example

Suppose a model predicts salary using two features:

- \(X_1\) = Years of experience.
- \(X_2\) = Skills score.

Assume the model has learned this equation:

\[
\hat{Y}=10000+5000X_1+200X_2
\]

An employee has:
- Experience = 3 years.
- Skills score = 80.

Substitute these values into the equation:

\[
\hat{Y}=10000+5000(3)+200(80)
\]

Calculate each term:

\[
=10000+15000+16000
\]

Therefore:

\[
\boxed{\hat{Y}=41000}
\]

The model predicts a salary of **₹41,000**.

These coefficients are hypothetical values used for learning. In a real project, the model estimates them from training data.

---

# Topic 4: Independent and Dependent Variables

Your first screenshot mentions:

"More than one input, independent → MLR."

Let's understand this statement.

### 4.1 Independent Variables

Independent variables are the input features used by the model to predict an output.

For example:

- Experience
- Education score
- Skills score

These are represented by `X`.

### 4.2 Dependent Variable

The dependent variable is the output we want to predict.

For example:

- Salary

This is represented by `y`.

Consider the following dataset:

| Experience | Education Score | Skills Score | Salary |
|---:|---:|---:|---:|
| 1 | 60 | 50 | 20,000 |
| 2 | 70 | 65 | 30,000 |
| 3 | 80 | 75 | 40,000 |
| 4 | 90 | 90 | 55,000 |

Here:

**Independent variables (`X`):**
- Experience
- Education Score
- Skills Score

**Dependent variable (`y`):**
- Salary

In Python:

```python
X = df[["Experience", "Education_Score", "Skills_Score"]]

y = df["Salary"]
```

Notice that `X` contains three columns, while `y` contains the target values.

**Important:** Independent variables are not necessarily statistically independent of each other. The term identifies their role as input features in the model.

---

# Topic 5: 2D, 3D, and Multiple Linear Regression

Your second screenshot contains 2D and 3D diagrams.

These diagrams help us visualize regression.

## 5.1 Simple Linear Regression — 2D

When we have one input feature and one output, we can visualize them using two axes.

For example:
- X-axis = Study Hours.
- Y-axis = Marks.

Each star represents one observation.

```text
Marks (Y)
   |
100|                  *
   |              *
   |          *        /
   |       *         /
   |    *          /
   |  *          /
   |________________________ Study Hours (X)
```

The line represents the relationship estimated by the regression model.

It is called the **regression line** or **best-fit line**.

The line is selected to minimize the sum of squared residuals in ordinary least squares regression.

## 5.2 Multiple Linear Regression — 3D

Suppose we have two input features:

- Study Hours.
- Sleep Hours.

And one output:

- Marks.

We can visualize the data using three axes.

```text
                 Marks (Z)
                    |
                    |      *   *
                    |   *---------
                    |  /        /
                    | /________/
                    |
                    +---------------- Study Hours (X)
                   /
                  /
          Sleep Hours (Y)
```

In this case, the best-fit line becomes a **best-fit plane**.

### What if we have more than two input features?

Suppose we use five features to predict salary.

We cannot visualize all five features and the output in an ordinary 2D or 3D graph.

However, the regression model can still use all five features to make predictions.

**Important:** Having multiple features does not automatically make a model nonlinear. Multiple Linear Regression remains linear in its coefficients.

---

# Topic 6: Best-Fit Line and Regression Coefficients

Your third screenshot contains:

- Best-fit line.
- \(m,b\).
- \(y=mx+b\).
- Multiple regression coefficients.

Let's understand them.

### 6.1 Simple Linear Regression

The equation is:

\[
y=mx+b
\]

Where:

- \(m\) = Slope.
- \(b\) = Intercept.

In machine learning notation, we write:

\[
\hat{y}=\beta_0+\beta_1x
\]

Here:

\[
\beta_0=b
\]

\[
\beta_1=m
\]

### 6.2 Multiple Linear Regression

When we have two independent variables:

\[
\boxed{\hat{y}=\beta_0+\beta_1x_1+\beta_2x_2}
\]

Where:
- \(\beta_0\) = Intercept.
- \(\beta_1\) = Coefficient of feature 1.
- \(\beta_2\) = Coefficient of feature 2.

Consider this example:

\[
\text{Marks}=10+5(\text{Study Hours})+2(\text{Practice Tests})
\]

Interpretation:

- If Study Hours increase by one hour, predicted marks increase by 5, assuming the number of practice tests stays constant.
- If Practice Tests increase by one, predicted marks increase by 2, assuming Study Hours stay constant.

This interpretation assumes that the model's linear relationship is appropriate for the data.

---

# Topic 7: The CGPA, IQ, and LPA Example

Your fourth screenshot contains three columns:

- CGPA
- IQ
- LPA

LPA means **Lakhs Per Annum**, a common way of expressing annual salary in India.

The dataset appears to contain values similar to these:

| CGPA | IQ | LPA |
|---:|---:|---:|
| 8 | 7 | 80 |
| 9 | 8 | 90 |
| 5 | 5 | 70 |
| 4 | 2 | 20 |

The screenshot is handwritten, so the exact values and intended units are not entirely clear. Treat this as an illustrative dataset rather than real salary data.

We want to predict LPA using CGPA and IQ.

The equation is:

\[
\boxed{
\widehat{\text{LPA}}=
\beta_0+\beta_1(\text{CGPA})+\beta_2(\text{IQ})
}
\]

The model needs to estimate three parameters:

\[
\boxed{\beta_0,\beta_1,\beta_2}
\]

These represent:
1. Intercept.
2. CGPA coefficient.
3. IQ coefficient.

The next question is: **How does the model find the best coefficients?**

That brings us to Ordinary Least Squares.

---

# Topic 8: Ordinary Least Squares (OLS)

Your screenshot mentions OLS.

OLS stands for **Ordinary Least Squares**.

It is a method used to estimate regression coefficients by minimizing the sum of squared residuals.

### 8.1 What is a residual?

A residual is the difference between an actual value and the model's predicted value.

\[
\boxed{\text{Residual}=y-\hat{y}}
\]

Where:
- \(y\) = Actual value.
- \(\hat{y}\) = Predicted value.

For example:

| Actual Marks | Predicted Marks | Residual |
|---:|---:|---:|
| 50 | 48 | 2 |
| 60 | 63 | -3 |
| 70 | 68 | 2 |

The residuals are:

\[
50-48=2
\]

\[
60-63=-3
\]

\[
70-68=2
\]

### 8.2 Sum of Squared Errors

OLS minimizes the sum of squared residuals.

\[
\boxed{SSE=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
\]

Squaring the residuals has two important effects:

1. Positive and negative residuals cannot cancel each other out.
2. Larger residuals receive a greater penalty.

The goal is to find the coefficients that produce the smallest possible SSE.

**Remember:** OLS estimates coefficients by minimizing squared residuals. It does not simply minimize the ordinary sum of residuals.

---

# Topic 9: Matrix Representation of Multiple Linear Regression

Your next screenshots introduce matrices, including:

- \(X\)
- \(X^T\)
- \(y\)
- \(\beta\)

These are the mathematical foundations of Multiple Linear Regression.

Let's use a small example with two features.

Suppose our dataset contains three observations:

| CGPA | IQ | Target |
|---:|---:|---:|
| 1 | 3 | 3 |
| 2 | 2 | 6 |
| 3 | 6 | 8 |

These values are illustrative.

### 9.1 Design Matrix — X

To include the intercept, we add a column containing ones.

\[
\boxed{
X=
\begin{bmatrix}
1&1&3\\
1&2&2\\
1&3&6
\end{bmatrix}
}
\]

The columns represent:

- First column: Intercept.
- Second column: First feature.
- Third column: Second feature.

There are three rows because we have three observations.

There are three columns because we have two features plus the intercept.

### 9.2 Target Vector — y

Our actual target values are:

\[
\boxed{
y=
\begin{bmatrix}
3\\
6\\
8
\end{bmatrix}
}
\]

This vector contains the values we want the model to predict.

### 9.3 Coefficient Vector — β

The coefficient vector is:

\[
\boxed{
\beta=
\begin{bmatrix}
\beta_0\\
\beta_1\\
\beta_2
\end{bmatrix}
}
\]

It contains the parameters that the model must estimate.

### 9.4 Matrix Equation

Instead of writing the regression equation separately for each observation, we can represent all predictions using matrix multiplication.

The familiar equation is:

\[
\hat{y}=\beta_0+\beta_1x_1+\beta_2x_2
\]

In matrix form:

\[
\boxed{\hat{y}=X\beta}
\]

Where:
- \(X\) = Input matrix.
- \(\beta\) = Coefficient vector.
- \(\hat{y}\) = Predicted output vector.

This representation makes it easier to perform regression calculations for many observations at once.

---

# Topic 10: Transpose of a Matrix — \(X^T\)

Your screenshots show the expression \(X^T\).

The transpose of a matrix is obtained by converting its rows into columns and its columns into rows.

Consider:

\[
X=
\begin{bmatrix}
1&1&3\\
1&2&2\\
1&3&6
\end{bmatrix}
\]

Its transpose is:

\[
\boxed{
X^T=
\begin{bmatrix}
1&1&1\\
1&2&3\\
3&2&6
\end{bmatrix}
}
\]

Notice that the first row of \(X\), which is \([1,1,3]\), becomes the first column of \(X^T\).

### Python Example

```python
import numpy as np

X = np.array([
    [1, 1, 3],
    [1, 2, 2],
    [1, 3, 6]
])

# Calculate the transpose
X_T = X.T

print("Original Matrix:")
print(X)

print("\nTranspose Matrix:")
print(X_T)
```

Output:

```text
Original Matrix:
[[1 1 3]
 [1 2 2]
 [1 3 6]]

Transpose Matrix:
[[1 1 1]
 [1 2 3]
 [3 2 6]]
```

**Key point:** In NumPy, `.T` returns the transpose of a two-dimensional array.

---

# Topic 11: Matrix Inverse — \(A^{-1}\)

Your screenshot contains:

\[
(X^TX)^{-1}
\]

The exponent \(-1\) represents the matrix inverse, not a negative number.

### 11.1 Understanding Matrix Inverse

For ordinary numbers:

\[
5\times\frac{1}{5}=1
\]

Similarly, for an invertible square matrix \(A\):

\[
\boxed{AA^{-1}=I}
\]

Here, \(I\) is the identity matrix.

For example:

\[
I=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
\]

Multiplying a matrix by its inverse produces the identity matrix.

### 11.2 Python Example

```python
import numpy as np

A = np.array([
    [2, 1],
    [1, 2]
], dtype=float)

A_inverse = np.linalg.inv(A)

print("Inverse:")
print(A_inverse)

print("\nA multiplied by its inverse:")
print(A @ A_inverse)
```

The final result will be approximately:

```text
[[1. 0.]
 [0. 1.]]
```

Tiny floating-point differences may occur.

**Important:** A square matrix has an ordinary inverse only if its determinant is nonzero.

---

# Topic 12: Determinant and Adjugate

Your screenshots also introduce determinants and adjugate matrices.

These concepts help explain how matrix inverses can be calculated.

## 12.1 Determinant

Consider a \(2\times2\) matrix:

\[
A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
\]

Its determinant is:

\[
\boxed{\det(A)=ad-bc}
\]

For example:

\[
A=
\begin{bmatrix}
2&1\\
1&2
\end{bmatrix}
\]

Calculate the determinant:

\[
\det(A)=(2\times2)-(1\times1)
\]

\[
=4-1
\]

Therefore:

\[
\boxed{\det(A)=3}
\]

Because the determinant is nonzero, this matrix has an inverse.

## 12.2 Adjugate

For an invertible square matrix:

\[
\boxed{
A^{-1}=\frac{\operatorname{adj}(A)}{\det(A)}
}
\]

Where:
- \(\operatorname{adj}(A)\) = Adjugate matrix.
- \(\det(A)\) = Determinant.

This formula is one way to calculate a matrix inverse mathematically.

In practical machine learning, you generally do not need to calculate the determinant and adjugate manually. NumPy and other numerical libraries can handle matrix operations.

---

# Topic 13: Normal Equation — The Most Important Formula

Now let's understand the main formula shown in your screenshots.

\[
\boxed{
\hat{\beta}=(X^TX)^{-1}X^Ty
}
\]

This is called the **Normal Equation**.

It provides a closed-form solution for estimating coefficients in ordinary least squares regression, provided the required inverse exists.

### 13.1 Understanding Each Part

| Expression | Meaning |
|---|---|
| \(X\) | Input feature matrix |
| \(X^T\) | Transpose of the input matrix |
| \(X^TX\) | Matrix multiplication of \(X^T\) and \(X\) |
| \((X^TX)^{-1}\) | Inverse of \(X^TX\) |
| \(y\) | Actual target values |
| \(\hat{\beta}\) | Estimated regression coefficients |

### 13.2 Why Do We Use This Formula?

We want to find the coefficients that minimize the sum of squared residuals.

The Normal Equation calculates these coefficients directly using matrix operations.

The process is:

```text
Input Matrix (X)
       +
Actual Target (y)
       |
       v
Normal Equation
       |
       v
Estimated Coefficients (β)
       |
       v
Predicted Values (ŷ)
```

### Important Limitation

The formula requires \(X^TX\) to be invertible.

If the features have perfect multicollinearity, or the data does not contain enough independent information, the inverse may not exist.

In such situations, a pseudoinverse or another numerical method can be used.

For larger datasets, numerical solvers are generally preferable to explicitly calculating a matrix inverse.

---

# Topic 14: Implementing the Normal Equation Using NumPy

Let's implement the mathematical formula in Python.

This example uses the same small dataset introduced earlier.

### Complete VS Code Program

```python
# ============================================================
# MULTIPLE LINEAR REGRESSION
# NORMAL EQUATION USING NUMPY
# ============================================================

import numpy as np


# STEP 1: Create the input matrix
# Column 1: Intercept
# Column 2: Feature 1
# Column 3: Feature 2

X = np.array([
    [1, 1, 3],
    [1, 2, 2],
    [1, 3, 6]
], dtype=float)


# STEP 2: Create the target vector

y = np.array([
    [3],
    [6],
    [8]
], dtype=float)


# STEP 3: Calculate the transpose of X

X_T = X.T


# STEP 4: Calculate X transpose multiplied by X

XTX = X_T @ X


# STEP 5: Calculate X transpose multiplied by y

XTy = X_T @ y


# STEP 6: Estimate the coefficients
# Solve the system:
# (X.T @ X) @ beta = X.T @ y

beta = np.linalg.solve(XTX, XTy)


# STEP 7: Display the coefficients

print("Regression Coefficients:")
print(beta)


# STEP 8: Predict the target values

y_predicted = X @ beta

print("\nPredicted Values:")
print(y_predicted)
```

### Understanding the Important Code

**`X.T`**

Calculates the transpose of the input matrix.

**`@`**

Performs matrix multiplication.

For example:

```python
XTX = X.T @ X
```

This calculates \(X^TX\).

**`np.linalg.solve()`**

Solves a system of linear equations.

Here, it solves:

\[
(X^TX)\hat{\beta}=X^Ty
\]

This is mathematically equivalent to the Normal Equation when \(X^TX\) is invertible.

**`X @ beta`**

Uses the estimated coefficients to calculate predictions.

### What Should You Learn from This Example?

The important relationship is:

\[
\boxed{\hat{y}=X\hat{\beta}}
\]

First, we estimate the coefficients. Then, we use those coefficients to make predictions.

This small example is useful for understanding the mathematics, but a model that fits a small training dataset well is not necessarily good at predicting new observations.

---

# Final Revision: Multiple Linear Regression

| Concept | What You Should Remember |
|---|---|
| Simple Linear Regression | Uses one independent variable |
| Multiple Linear Regression | Uses two or more independent variables |
| Independent Variables | Input features |
| Dependent Variable | Target to predict |
| Regression Equation | \(\hat{y}=\beta_0+\beta_1x_1+\cdots+\beta_nx_n\) |
| Regression Coefficients | Values learned from training data |
| Residual | Actual value minus predicted value |
| OLS | Estimates coefficients by minimizing squared residuals |
| Design Matrix | \(X\) |
| Target Vector | \(y\) |
| Coefficient Vector | \(\beta\) |
| Transpose | \(X^T\) |
| Matrix Inverse | \(A^{-1}\) |
| Determinant | Helps determine whether a square matrix is invertible |
| Normal Equation | \(\hat{\beta}=(X^TX)^{-1}X^Ty\) |
| Prediction Equation | \(\hat{y}=X\hat{\beta}\) |

## Recommended Learning Order

To build a strong understanding of Multiple Linear Regression, study these topics in order:

1. Simple Linear Regression.
2. Multiple Linear Regression.
3. Cost Function and Mean Squared Error.
4. Ordinary Least Squares.
5. Matrix Operations.
6. Normal Equation derivation.
7. Multiple Linear Regression using Scikit-learn.
8. Model evaluation using MAE, MSE, RMSE, and \(R^2\).

**Your main takeaway:** Multiple Linear Regression predicts a numerical output using multiple input features. OLS finds coefficients that minimize squared prediction errors, and the Normal Equation provides a mathematical method for calculating those coefficients. 