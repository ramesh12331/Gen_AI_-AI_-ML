# 📘 Regularization in Machine Learning — L1 and L2

## 📚 Table of Contents

1. What is Regularization?
2. Why Do We Need Regularization?
3. Understanding Model Overfitting
4. Loss Function and Regularization
5. Ridge Regression — L2
6. Lasso Regression — L1
7. Difference Between L1 and L2
8. Understanding the Alpha Parameter
9. Polynomial Regression with Regularization
10. Scikit-learn Implementation
11. Cross Validation
12. Bias–Variance Tradeoff
13. Interview Questions
14. Final Revision

---

# 1. What is Regularization?

**Regularization** is a technique used in Machine Learning to reduce overfitting by adding a penalty to the model's loss function.

### Simple example

Imagine you are preparing for an examination.

- You memorize only the practice questions.
- You get good marks in practice tests.
- But you cannot answer new questions.

This is similar to overfitting.

A model should learn the general pattern, not simply memorize training data.

**Regularization helps control model complexity.**

### Remember

Regularization = Original Loss + Penalty

---

# 2. Why Do We Need Regularization?

Consider these model results from the class screenshot:

| Metric | Score |
|---|---:|
| Training R² | 0.9838 |
| Testing R² | 0.5442 |

### What do these scores mean?

**Training R² = 0.9838**

The model explains approximately 98.38% of the variation in the training data.

**Testing R² = 0.5442**

The model explains approximately 54.42% of the variation in the testing data.

There is a large difference between the two scores.

This suggests possible overfitting.

### Goal

We want a model that performs well on both training and testing data.

---

# 3. Understanding Model Overfitting

There are three important situations:

### 1. Underfitting

The model is too simple to learn the important patterns.

- Poor training performance.
- Poor testing performance.

### 2. Good Fit

The model learns the underlying pattern.

- Good training performance.
- Good testing performance.
- Generalizes to unseen data.

### 3. Overfitting

The model learns the training data too closely, including noise.

- Very good training performance.
- Poorer testing performance.
- Poor generalization.

### Model complexity

As model complexity increases:

- Training error generally decreases.
- Testing error may decrease initially.
- Testing error can increase when the model becomes too complex.

**Regularization helps control model complexity.**

---

# 4. Loss Function and Regularization

First, understand the ordinary loss function.

For regression, one common loss function is Sum of Squared Errors (SSE).

$$
SSE = \sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Where:

| Symbol | Meaning |
|---|---|
| $y_i$ | Actual value |
| $\hat{y}_i$ | Predicted value |
| $n$ | Number of observations |
| $y_i-\hat{y}_i$ | Prediction error |

Regularization adds a penalty to this loss.

General idea:

$$
Regularized\ Loss = SSE + Penalty
$$

There are two popular regularization techniques:

1. Ridge Regression — L2 Regularization
2. Lasso Regression — L1 Regularization

---

# 5. Ridge Regression — L2 Regularization

**Ridge Regression uses the square of the model coefficients as its penalty.**

### Formula

$$
J(\theta) =
SSE + \lambda\sum_{j=1}^{p}\theta_j^2
$$

Expanded form:

$$
J(\theta) =
SSE + \lambda(\theta_1^2+\theta_2^2+\cdots+\theta_p^2)
$$

Where:

| Symbol | Meaning |
|---|---|
| $SSE$ | Sum of Squared Errors |
| $\lambda$ | Regularization strength |
| $\theta_j$ | Model coefficient |
| $p$ | Number of coefficients being penalized |

*Note: The standard Ridge formulation does not penalize the intercept.*

### Simple example

Suppose:

$$
\theta_1=2,\quad \theta_2=3,\quad \theta_3=4
$$

Let:

$$
\lambda=0.1
$$

The L2 penalty is:

$$
0.1(2^2+3^2+4^2)
$$

$$
=0.1(4+9+16)
$$

$$
=0.1(29)
$$

$$
=2.9
$$

Therefore:

$$
Regularized\ Loss = SSE+2.9
$$

### Important points

- Ridge reduces large coefficients.
- Coefficients generally become smaller.
- It usually does not make coefficients exactly zero.
- It helps reduce overfitting.

### Python

```python
from sklearn.linear_model import Ridge

ridge_model = Ridge(alpha=100)

ridge_model.fit(X_train, y_train)
```

Here, `alpha=100` controls the strength of regularization.

---

# 6. Lasso Regression — L1 Regularization

**Lasso Regression uses the absolute values of model coefficients as its penalty.**

### Formula

$$
J(\theta) =
SSE+\lambda\sum_{j=1}^{p}|\theta_j|
$$

Expanded form:

$$
J(\theta) =
SSE+\lambda(
|\theta_1|+|\theta_2|+\cdots+|\theta_p|
)
$$

### Example

Suppose:

$$
\theta_1=2,\quad
\theta_2=-3,\quad
\theta_3=4
$$

Let:

$$
\lambda=0.01
$$

The L1 penalty is:

$$
0.01(|2|+|-3|+|4|)
$$

$$
=0.01(2+3+4)
$$

$$
=0.09
$$

Therefore:

$$
Regularized\ Loss=SSE+0.09
$$

### Important points

- Lasso reduces coefficient values.
- It can make some coefficients exactly zero.
- Zero coefficients mean those features are not used by the fitted linear model.
- It can perform automatic feature selection.

### Python

```python
from sklearn.linear_model import Lasso

lasso_model = Lasso(alpha=0.01, max_iter=10000)

lasso_model.fit(X_train, y_train)
```

**Important:** `alpha=0.01` is an example from the lecture. Whether any coefficient becomes zero depends on the dataset, feature scaling and alpha value.

---

# 7. Difference Between L1 and L2

| Feature | L1 — Lasso | L2 — Ridge |
|---|---|---|
| Penalty | Absolute coefficient | Squared coefficient |
| Formula | $\lambda\sum|\theta_j|$ | $\lambda\sum\theta_j^2$ |
| Coefficients | Can become zero | Usually become small |
| Feature selection | Yes, can select features | Usually retains features |
| Useful when | Some features may be unnecessary | Many features contribute |
| Main purpose | Regularization and feature selection | Regularization and coefficient shrinkage |

### Easy way to remember

- **L1 → Can remove features.**
- **L2 → Shrinks coefficients.**

---

# 8. Understanding the Alpha Parameter

In Scikit-learn, `alpha` controls the regularization strength.

It corresponds to the regularization strength represented by $\lambda$ in the formulas.

### Small Alpha

```python
Ridge(alpha=0.01)
```

- Weaker regularization.
- Smaller penalty.
- Coefficients are less restricted.

### Large Alpha

```python
Ridge(alpha=100)
```

- Stronger regularization.
- Larger penalty.
- Coefficients are more strongly restricted.

### Important

If alpha becomes too large, the model may become too simple and underfit.

We should select alpha using validation or cross-validation rather than choosing it randomly.

---

# 9. Polynomial Regression with Regularization

Your class screenshot demonstrates Polynomial Regression.

Polynomial Regression creates additional features from the original input features.

For example, with one input feature $x$ and degree 3:

$$
y=b_0+b_1x+b_2x^2+b_3x^3
$$

With multiple input features, polynomial feature generation also creates interaction terms.

### Why can this cause overfitting?

When we increase the polynomial degree:

- More features are created.
- The model becomes more flexible.
- It can learn complex patterns.
- It may also learn noise.

Your screenshot shows:

```python
PolynomialFeatures(
    degree=3,
    include_bias=False
)
```

This generates polynomial features up to degree 3.

The screenshot also shows:

```text
Number of Coefficients: 164
```

This is an example of how polynomial feature generation can increase model complexity.

Regularization can help control these coefficients.

---

# 10. Scikit-learn Implementation

## A. Polynomial Regression without Regularization

The class screenshot uses a Pipeline:

```python
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

model = Pipeline([
    ("poly", PolynomialFeatures(
        degree=3,
        include_bias=False
    )),

    ("scaler", StandardScaler()),

    ("regressor", LinearRegression())
])

model.fit(X_train, y_train)
```

### Explanation

**Step 1 — PolynomialFeatures**

```python
PolynomialFeatures(degree=3, include_bias=False)
```

Creates polynomial and interaction features up to degree 3.

**Step 2 — StandardScaler**

```python
StandardScaler()
```

Scales the generated features.

**Step 3 — LinearRegression**

```python
LinearRegression()
```

Fits the regression model using the generated features.

**Step 4 — Pipeline**

The pipeline executes these steps in order.

It also ensures that the scaler is fitted using training data when the pipeline is fitted.

## B. Ridge Regression with Polynomial Features

```python
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

ridge_model = Pipeline([
    ("poly", PolynomialFeatures(
        degree=3,
        include_bias=False
    )),

    ("scaler", StandardScaler()),

    ("regressor", Ridge(alpha=100))
])

ridge_model.fit(X_train, y_train)
```

### What happens?

```text
Original Input Features
          |
          v
PolynomialFeatures
          |
          v
Generated Polynomial Features
          |
          v
StandardScaler
          |
          v
Ridge Regression (L2)
          |
          v
Trained Model
```

Ridge penalizes large coefficients and helps control model complexity.

## C. Lasso Regression with Polynomial Features

```python
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

lasso_model = Pipeline([
    ("poly", PolynomialFeatures(
        degree=3,
        include_bias=False
    )),

    ("scaler", StandardScaler()),

    ("regressor", Lasso(
        alpha=0.01,
        max_iter=10000
    ))
])

lasso_model.fit(X_train, y_train)
```

Lasso can shrink some coefficients to exactly zero.

---

# 11. Model Evaluation

After training, compare training and testing performance.

```python
from sklearn.metrics import r2_score, mean_squared_error

# Training predictions
y_train_pred = ridge_model.predict(X_train)

# Testing predictions
y_test_pred = ridge_model.predict(X_test)

# Training R2
print(
    "Training R2:",
    r2_score(y_train, y_train_pred)
)

# Testing R2
print(
    "Testing R2:",
    r2_score(y_test, y_test_pred)
)

# Testing MSE
print(
    "Testing MSE:",
    mean_squared_error(y_test, y_test_pred)
)
```

### Interpretation

| Result | Possible meaning |
|---|---|
| High training R² and high testing R² | Good fit |
| High training R² and low testing R² | Possible overfitting |
| Low training R² and low testing R² | Possible underfitting |

These are diagnostic patterns, not absolute rules. Always consider the dataset and the evaluation metric.

---

# 12. Cross Validation

Cross-validation helps us evaluate a model across different training and validation splits.

It can help select a suitable alpha value.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

pipeline = Pipeline([
    ("poly", PolynomialFeatures(
        degree=3,
        include_bias=False
    )),

    ("scaler", StandardScaler()),

    ("regressor", Ridge())
])

param_grid = {
    "regressor__alpha": [0.01, 0.1, 1, 10, 100, 1000]
}

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="r2"
)

grid_search.fit(X_train, y_train)

print("Best Alpha:", grid_search.best_params_)
print("Best CV R2:", grid_search.best_score_)
```

### Important

`GridSearchCV` tries the given alpha values and evaluates them using 5-fold cross-validation.

The best alpha is selected according to the chosen scoring metric.

The final test dataset should remain separate until the final evaluation.

---

# 13. Bias–Variance Tradeoff

Your screenshots also cover Bias and Variance.

### High Bias

- Model is too simple.
- It fails to learn important patterns.
- Often causes underfitting.

### High Variance

- Model is too sensitive to training data.
- It learns noise and specific patterns.
- Often causes overfitting.

### Goal

Find a balance between bias and variance so that the model generalizes well.

Regularization can reduce variance, but too much regularization can increase bias.

---

# 14. Interview Questions

### Q1. What is Regularization?

Regularization is a technique used to reduce overfitting by adding a penalty to the model's loss function.

### Q2. What are L1 and L2 Regularization?

L1 uses the absolute values of coefficients as a penalty. L2 uses the squared values of coefficients as a penalty.

### Q3. What is Ridge Regression?

Ridge Regression is a linear regression technique that uses L2 regularization to reduce large coefficients.

### Q4. What is Lasso Regression?

Lasso Regression is a linear regression technique that uses L1 regularization and can make some coefficients exactly zero.

### Q5. What is the difference between Ridge and Lasso?

Ridge shrinks coefficients towards zero, whereas Lasso can shrink some coefficients exactly to zero.

### Q6. What is Alpha?

Alpha controls the strength of regularization.

### Q7. What happens when Alpha increases?

The regularization penalty becomes stronger, and coefficients are more strongly restricted.

### Q8. Can Lasso perform feature selection?

Yes. Lasso can make some coefficients zero, effectively removing those features from the fitted model.

### Q9. Why do we use StandardScaler?

Feature scaling is important for regularized models because the penalty depends on coefficient magnitudes. Scaling makes the penalty more comparable across differently measured features.

### Q10. Can Regularization cause Underfitting?

Yes. If regularization is too strong, the model may become too simple and underfit.

---

# ⭐ Final Revision

| Concept | Remember |
|---|---|
| Regularization | Controls model complexity |
| Overfitting | Learns training data too closely |
| Ridge | L2 regularization |
| Lasso | L1 regularization |
| L1 penalty | Absolute coefficients |
| L2 penalty | Squared coefficients |
| Alpha | Regularization strength |
| Ridge coefficients | Usually small, not exactly zero |
| Lasso coefficients | Some can become zero |
| StandardScaler | Scales features |
| Cross Validation | Helps select alpha |

## Most Important Formulas

**Ridge — L2**

$$
J(\theta)=SSE+\lambda\sum_{j=1}^{p}\theta_j^2
$$

**Lasso — L1**

$$
J(\theta)=SSE+\lambda\sum_{j=1}^{p}|\theta_j|
$$

**Mean Squared Error**

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

## One-Line Interview Definition

Regularization is a technique that adds a penalty to the loss function to control model complexity and reduce overfitting. Ridge uses L2 regularization, while Lasso uses L1 regularization.