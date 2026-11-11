# Machine Learning Class Notes — 11 November 2026

![Machine Learning](https://img.shields.io/badge/Topic-Machine%20Learning-blue)
![Classification](https://img.shields.io/badge/Part-Classification-success)
![Regression](https://img.shields.io/badge/Part-Regression-orange)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen)

> Classroom continuation notes covering **Softmax Regression**, **Polynomial Features**, **Polynomial Regression**, **Underfitting**, **Overfitting**, and **Optimum Degree Selection**.

---

## 📚 Table of Contents

- [Part 1 — Softmax Regression](#part-1--softmax-regression)
  - [1. Logistic Regression Loss Function](#1-logistic-regression-loss-function-log-loss)
  - [2. Softmax Regression](#2-softmax-regression--multi-class-classification)
  - [3. One-Hot Encoding](#3-one-hot-encoding)
  - [4. Categorical Cross-Entropy Loss](#4-categorical-cross-entropy-loss--detailed-derivation)
  - [5. Model Weights and Bias](#5-softmax-regression--model-weights-and-bias)
- [Part 2 — Polynomial Features](#part-2--polynomial-features)
  - [6. Polynomial Features](#6-what-are-polynomial-features)
  - [7. Linear vs Polynomial Regression](#7-linear-regression-vs-polynomial-regression)
  - [8. Polynomial Degree](#8-polynomial-degree)
  - [9. Two Input Variables](#9-polynomial-features-with-two-input-variables)
  - [10. Degree 3 Model](#10-polynomial-regression-formula--degree-3)
  - [11. Underfitting and Overfitting](#11-underfitting-and-overfitting)
  - [12. Optimum Degree Selection](#12-optimum-degree-selection)
- [Part 3 — Python Practical](#part-3--python-practical)
- [Part 4 — Interview Preparation](#part-4--interview-preparation)
- [Practice Questions](#15-practice-questions)
- [Quick Revision](#16-quick-revision--todays-class)
- [Telugu Meanings](#17-telugu-meanings)

---

# PART 1 — SOFTMAX REGRESSION

## 1. Logistic Regression Loss Function (Log Loss)

### Definition

**Log Loss** measures how far the predicted probability is from the actual class. It is also called **Binary Cross-Entropy Loss**.

- Used for binary classification.
- A smaller loss means the predicted probability is closer to the actual class.
- A larger loss means the model made a more confident incorrect prediction.

### Formula

$$
L=-\\frac{1}{m}\\sum_{i=1}^{m}
\\left[
y_i\\log(\\hat y_i)+(1-y_i)\\log(1-\\hat y_i)
\\right]
$$

Where:

| Symbol | Meaning |
|---|---|
| $L$ | Average Log Loss |
| $m$ | Number of samples |
| $y_i$ | Actual class (0 or 1) |
| $\\hat y_i$ | Predicted probability for class 1 |
| $\\log$ | Natural logarithm |

### Example — Email Spam Detection

- Spam = `1`
- Not Spam = `0`

Actual output:

$$y=1$$

Predicted probability:

$$\\hat y=0.8$$

Substitute the values:

$$
L=-[1\\log(0.8)+(1-1)\\log(1-0.8)]
$$

$$L=-\\log(0.8)$$

$$\\boxed{L\\approx 0.2231}$$

**Interpretation:** The model gives an 80% probability to the correct class, so the loss is relatively low.

> **Remember:** Binary Log Loss is used for binary classification. Softmax Regression for mutually exclusive multi-class classification commonly uses Categorical Cross-Entropy.

---

## 2. Softmax Regression — Multi-Class Classification

### Definition

**Softmax Regression** is a classification algorithm used to predict one class among multiple possible classes. It converts model scores, called **logits**, into probabilities.

### Real-world example — Fruit Classification

Suppose a model must classify an image into one of three classes:

| Class | Fruit |
|---|---|
| Class 1 | Apple |
| Class 2 | Banana |
| Class 3 | Orange |

The model produces:

| Fruit | Probability |
|---|---:|
| Apple | 0.70 |
| Banana | 0.20 |
| Orange | 0.10 |
| **Total** | **1.00** |

The highest probability is `0.70`, so the predicted class is **Apple**.

### Softmax Formula

$$
P(y=k)=\\frac{e^{z_k}}{\\sum_{j=1}^{K}e^{z_j}}
$$

Where:

- $z_k$ = score (logit) for class $k$.
- $K$ = total number of classes.
- $e$ = Euler's number (approximately 2.718).
- $P(y=k)$ = probability of class $k$.

**Important:** All Softmax probabilities add up to 1.

### Simple flow

```text
Input features
     |
     v
Class scores (logits)
     |
     v
Softmax function
     |
     v
Class probabilities
     |
     v
Choose the class with the highest probability
```

---

## 3. One-Hot Encoding

### Definition

**One-Hot Encoding** converts categorical values into binary values (`0` and `1`).

### Example

Suppose we have three classes:

| Sample | Actual Class |
|---|---|
| Student 1 | Class 1 |
| Student 2 | Class 2 |
| Student 3 | Class 3 |

After One-Hot Encoding:

| Sample | Class 1 | Class 2 | Class 3 |
|---|---:|---:|---:|
| Student 1 | 1 | 0 | 0 |
| Student 2 | 0 | 1 | 0 |
| Student 3 | 0 | 0 | 1 |

### Understand each row

- Student 1 → `[1, 0, 0]`
- Student 2 → `[0, 1, 0]`
- Student 3 → `[0, 0, 1]`

Only the position of the actual class contains `1`; all other positions contain `0`.

### Why do we use One-Hot Encoding?

A multi-class classification model needs a numerical representation of the actual class to calculate **Categorical Cross-Entropy Loss**.

---

## 4. Categorical Cross-Entropy Loss — Detailed Derivation

This loss function is commonly used for mutually exclusive multi-class classification.

### Formula

$$
L=-\\frac{1}{m}\\sum_{i=1}^{m}\\sum_{k=1}^{K}
y_k^{(i)}\\log(\\hat y_k^{(i)})
$$

Where:

| Symbol | Meaning |
|---|---|
| $m$ | Number of samples |
| $K$ | Number of classes |
| $y_k^{(i)}$ | Actual one-hot value for sample $i$, class $k$ |
| $\\hat y_k^{(i)}$ | Predicted probability for sample $i$, class $k$ |

### Example setup

For three classes:

$$K=3$$

For three samples:

$$m=3$$

Expanded formula:

$$
\\begin{aligned}
L=-\\frac{1}{3}[&
y_1^{(1)}\\log(\\hat y_1^{(1)})
+y_2^{(1)}\\log(\\hat y_2^{(1)})
+y_3^{(1)}\\log(\\hat y_3^{(1)})\\\\
&+y_1^{(2)}\\log(\\hat y_1^{(2)})
+y_2^{(2)}\\log(\\hat y_2^{(2)})
+y_3^{(2)}\\log(\\hat y_3^{(2)})\\\\
&+y_1^{(3)}\\log(\\hat y_1^{(3)})
+y_2^{(3)}\\log(\\hat y_2^{(3)})
+y_3^{(3)}\\log(\\hat y_3^{(3)})
]
\\end{aligned}
$$

### Simplification using One-Hot Encoding

**Sample 1**

Actual class:

$$y^{(1)}=[1,0,0]$$

Contribution to loss:

$$
1\\log(\\hat y_1^{(1)})
+0\\log(\\hat y_2^{(1)})
+0\\log(\\hat y_3^{(1)})
$$

Therefore:

$$=\\log(\\hat y_1^{(1)})$$

**Sample 2**

$$y^{(2)}=[0,1,0]$$

Contribution:

$$=\\log(\\hat y_2^{(2)})$$

**Sample 3**

$$y^{(3)}=[0,0,1]$$

Contribution:

$$=\\log(\\hat y_3^{(3)})$$

### Final simplified formula

$$
\\boxed{
L=-\\frac{1}{3}\\left[
\\log(\\hat y_1^{(1)})
+\\log(\\hat y_2^{(2)})
+\\log(\\hat y_3^{(3)})
\\right]
}
$$

**Important classroom concept:** Because One-Hot Encoding contains one `1` and all remaining values are `0`, only the predicted probability of the actual class contributes to the loss.

---

## 5. Softmax Regression — Model Weights and Bias

Suppose we have:

- Two input features: $x_1,x_2$
- Three output classes: Class 1, Class 2, Class 3

Each class has its own weights and bias.

### Class 1

$$z_1=w_1^{(1)}x_1+w_2^{(1)}x_2+w_0^{(1)}$$

### Class 2

$$z_2=w_1^{(2)}x_1+w_2^{(2)}x_2+w_0^{(2)}$$

### Class 3

$$z_3=w_1^{(3)}x_1+w_2^{(3)}x_2+w_0^{(3)}$$

Where:

- $w_1,w_2$ = feature weights.
- $w_0$ = bias.
- $x_1,x_2$ = input features.
- $z_1,z_2,z_3$ = class scores (logits).

### Model Architecture

```text
                Input Features
                  x1, x2
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
      Class 1     Class 2     Class 3
    Weights +   Weights +   Weights +
      Bias        Bias        Bias
        |           |           |
        v           v           v
        z1          z2          z3
        |           |           |
        +-----------+-----------+
                    |
                    v
              Softmax Function
                    |
                    v
             P1, P2, P3
                    |
                    v
             Final Prediction
```

### Weight Matrix

The weights and biases can be represented in a matrix:

$$
W=
\\begin{bmatrix}
w_1^{(1)}&w_2^{(1)}&w_0^{(1)}\\\\
w_1^{(2)}&w_2^{(2)}&w_0^{(2)}\\\\
w_1^{(3)}&w_2^{(3)}&w_0^{(3)}
\\end{bmatrix}
$$

During training, **Gradient Descent** updates these weights and biases to minimize Cross-Entropy Loss.

---

# PART 2 — POLYNOMIAL FEATURES

## 6. What are Polynomial Features?

### Definition

**Polynomial Features** are new features created by adding powers and combinations of existing input features.

They help a Machine Learning model learn non-linear relationships between input and output.

**Simple meaning:** We take existing columns and create additional columns using powers and multiplication.

### Why do we need Polynomial Features?

Consider this dataset:

| Hours Studied (X) | Marks (Y) |
|---:|---:|
| 1 | 10 |
| 2 | 25 |
| 3 | 50 |
| 4 | 85 |
| 5 | 130 |

The relationship between study hours and marks may not be a straight line. A simple Linear Regression model might not fit this pattern properly.

We can create additional features:

$$X,\\quad X^2,\\quad X^3$$

Now the model can learn a curved relationship.

---

## 7. Linear Regression vs Polynomial Regression

### Linear Regression

Fits a straight line.

$$y=w_0+w_1x$$

### Polynomial Regression

Can fit a curved relationship.

$$y=w_0+w_1x+w_2x^2$$

### Important Difference

| Linear Regression | Polynomial Regression |
|---|---|
| Straight-line relationship | Can model curved relationships |
| Uses original features | Uses polynomial features |
| Degree 1 | Degree 2, 3, etc. |
| Less flexible for curved patterns | More flexible as degree increases |

> **Important:** Polynomial Regression is still a Linear Regression model in terms of its coefficients. It becomes non-linear with respect to the original input features.

---

## 8. Polynomial Degree

### Definition

**Degree** determines the highest power of the input feature used in Polynomial Regression.

Suppose we have one input feature, $x$.

### Degree 1

Features:

$$x$$

Model:

$$y=w_0+w_1x$$

### Degree 2

Features:

$$x,\\quad x^2$$

Model:

$$y=w_0+w_1x+w_2x^2$$

### Degree 3

Features:

$$x,\\quad x^2,\\quad x^3$$

Model:

$$y=w_0+w_1x+w_2x^2+w_3x^3$$

### Degree Comparison

| Degree | Features | Model type |
|---:|---|---|
| 1 | $x$ | Linear |
| 2 | $x,x^2$ | Quadratic |
| 3 | $x,x^2,x^3$ | Cubic |
| 4 | $x,x^2,x^3,x^4$ | Quartic |
| 5 | $x,x^2,x^3,x^4,x^5$ | Degree 5 |

---

## 9. Polynomial Features with Two Input Variables

Suppose the dataset has two input features:

$$X_1,\\quad X_2$$

### Degree 2 — Full Feature Expansion

$$
1,\\quad X_1,\\quad X_2,\\quad X_1^2,\\quad X_1X_2,\\quad X_2^2
$$

### Degree 3 — Full Feature Expansion

$$
\\begin{aligned}
1,\\ X_1,\\ X_2,\\ X_1^2,\\ X_1X_2,\\ X_2^2,\\\\
X_1^3,\\ X_1^2X_2,\\ X_1X_2^2,\\ X_2^3
\\end{aligned}
$$

### Worked Example

Original dataset:

| $X_1$ | $X_2$ |
|---:|---:|
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |

After creating degree-2 polynomial features (excluding the constant column from this display):

| $X_1$ | $X_2$ | $X_1^2$ | $X_1\\times X_2$ | $X_2^2$ |
|---:|---:|---:|---:|---:|
| 2 | 3 | 4 | 6 | 9 |
| 3 | 4 | 9 | 12 | 16 |
| 4 | 5 | 16 | 20 | 25 |

Notice that the model has created three additional columns: $X_1^2$, $X_1X_2$, and $X_2^2$.

**Why?** These additional features help the model learn more complex patterns.

---

## 10. Polynomial Regression Formula — Degree 3

### One input feature

$$
\\boxed{y=w_0+w_1x+w_2x^2+w_3x^3}
$$

### Two input features — Full degree-3 model

$$
\\begin{aligned}
y={}&w_0+w_1x_1+w_2x_2\\\\
&+w_3x_1^2+w_4x_1x_2+w_5x_2^2\\\\
&+w_6x_1^3+w_7x_1^2x_2\\\\
&+w_8x_1x_2^2+w_9x_2^3
\\end{aligned}
$$

Each newly created feature receives its own weight.

---

## 11. Underfitting and Overfitting

### Underfitting

**Definition:** Underfitting happens when a model is too simple to learn the actual patterns in the training data.

Example: Using a straight line for data that follows a complex curve.

Common signs:

- High training error.
- High testing error.
- The model cannot learn important patterns.

### Overfitting

**Definition:** Overfitting happens when a model learns the training data too closely, including noise and unnecessary patterns.

Example: A degree-15 polynomial creates a very complicated curve that fits training points but performs poorly on new data.

Common signs:

- Very low training error.
- High testing error.
- Poor performance on unseen data.

### Visual Difference

| Underfitting | Overfitting |
|---|---|
| Model is too simple | Model is too complex |
| Does not capture the pattern | Follows training noise |
| High training error | Very low training error |
| High testing error | High testing error |

### Relationship with Polynomial Degree

- Degree increases → overfitting risk can increase.
- Degree decreases → underfitting risk can increase.

This is a **general tendency**, not an absolute rule. The actual result depends on the dataset, noise, amount of data, and regularization.

---

## 12. Optimum Degree Selection

### Definition

**Optimum Degree** is the polynomial degree that provides a good balance between underfitting and overfitting.

### Example

Suppose we test different polynomial degrees:

| Degree | Training Error | Testing Error |
|---:|---|---|
| 1 | High | High |
| 2 | Medium | Medium |
| 3 | Low | Low |
| 4 | Very low | Low |
| 5 | Very low | High |

In this hypothetical example, degree 3 may be a good choice.

> These error descriptions are illustrative, not results from a classroom dataset.

### Hyperparameter Tuning

Polynomial degree is a **hyperparameter** because we choose it before training the model.

Typical process:

1. Select possible degrees.
2. Generate polynomial features.
3. Train the model.
4. Calculate validation error.
5. Compare results.
6. Select a suitable degree.

**Important:** Do not select a degree only because it gives the lowest training error. Check validation performance. Keep the test set for final evaluation.

---

# PART 3 — PYTHON PRACTICAL

## 13. Implement Polynomial Regression using Scikit-learn

### Step 1 — Install the required libraries

```bash
pip install numpy pandas scikit-learn
```

### Step 2 — Import Libraries

```python
import numpy as np
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
```

### Step 3 — Create Dataset

```python
# Input feature
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

# Target variable
y = np.array([
    5, 12, 23, 38, 57,
    80, 107, 138, 173, 212
])
```

### Step 4 — Split Dataset

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Step 5 — Create Polynomial Features

```python
# Create polynomial features of degree 2
poly = PolynomialFeatures(degree=2)

# Learn the feature transformation from training data
X_train_poly = poly.fit_transform(X_train)

# Apply the same transformation to test data
X_test_poly = poly.transform(X_test)
```

### Step 6 — Train Model

```python
model = LinearRegression()
model.fit(X_train_poly, y_train)
```

### Step 7 — Make Predictions

```python
y_pred = model.predict(X_test_poly)

print("Actual:", y_test)
print("Predicted:", y_pred)
```

### Step 8 — Evaluate Model

```python
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("R2 Score:", r2)
```

### Complete Workflow

```text
Dataset
   |
   v
Train-Test Split
   |
   v
PolynomialFeatures(degree=2)
   |
   v
LinearRegression()
   |
   v
Model Prediction
   |
   v
MSE and R² Evaluation
```

### Important Code Notes

- `PolynomialFeatures(degree=2)` creates polynomial features up to degree 2.
- `fit_transform()` learns and applies the transformation to training data.
- `transform()` applies the already learned transformation to test data.
- `LinearRegression()` creates the regression model.
- `fit()` trains the model.
- `predict()` generates predictions.
- `mean_squared_error()` calculates Mean Squared Error.
- `r2_score()` calculates the R² score.

---

# PART 4 — INTERVIEW PREPARATION

## 14. Important Interview Questions

<details>
<summary><strong>Q1. What is Softmax Regression?</strong></summary>

Softmax Regression is a classification algorithm used to predict probabilities for multiple classes.
</details>

<details>
<summary><strong>Q2. What is One-Hot Encoding?</strong></summary>

It converts categorical values into binary representations using 0 and 1.
</details>

<details>
<summary><strong>Q3. What is Categorical Cross-Entropy?</strong></summary>

It is a loss function used to measure the difference between actual and predicted class probabilities in multi-class classification.
</details>

<details>
<summary><strong>Q4. What is the difference between Sigmoid and Softmax?</strong></summary>

- **Sigmoid:** Commonly used for binary classification.
- **Softmax:** Commonly used for mutually exclusive multi-class classification.
</details>

<details>
<summary><strong>Q5. What are Polynomial Features?</strong></summary>

They are additional features created using powers and combinations of existing features.
</details>

<details>
<summary><strong>Q6. What is Polynomial Degree?</strong></summary>

It represents the highest power used to create polynomial features.
</details>

<details>
<summary><strong>Q7. What is Underfitting?</strong></summary>

Underfitting occurs when a model is too simple to learn the underlying data patterns.
</details>

<details>
<summary><strong>Q8. What is Overfitting?</strong></summary>

Overfitting occurs when a model learns the training data too closely and performs poorly on unseen data.
</details>

<details>
<summary><strong>Q9. What is Hyperparameter Tuning?</strong></summary>

It is the process of selecting suitable hyperparameter values to improve model performance.
</details>

<details>
<summary><strong>Q10. How do you select the optimum polynomial degree?</strong></summary>

By comparing validation performance for different polynomial degrees.
</details>

---

## 15. Practice Questions

Try to answer before opening the answers.

<details>
<summary><strong>1. Which loss function is commonly used for multi-class classification?</strong></summary>

- Mean Squared Error
- **Categorical Cross-Entropy**
- MAE
</details>

<details>
<summary><strong>2. What is the purpose of One-Hot Encoding?</strong></summary>

- **Convert categories into binary values**
- Remove missing values
- Scale numerical values
</details>

<details>
<summary><strong>3. For degree 3, which feature is included for a single input x?</strong></summary>

- $x^4$
- **$x^3$**
- $1/x$
</details>

<details>
<summary><strong>4. What happens when a model is too simple?</strong></summary>

- Overfitting
- **Underfitting**
- Perfect fitting
</details>

<details>
<summary><strong>5. Which data should be used to select the optimum degree?</strong></summary>

- Only training data
- **Validation data**
- Only the target column
</details>

---

## 16. Quick Revision — Today's Class

| Topic | Remember |
|---|---|
| Log Loss | Binary classification loss |
| Softmax | Converts logits into probabilities |
| One-Hot Encoding | Categorical to binary representation |
| Categorical Cross-Entropy | Multi-class loss |
| Weights and Bias | Model parameters |
| Polynomial Features | Create additional features |
| Polynomial Degree | Highest power |
| Underfitting | Model too simple |
| Overfitting | Model too complex |
| Optimum Degree | Balance between underfitting and overfitting |
| Hyperparameter Tuning | Find suitable settings |

---

## 17. Telugu Meanings

| English term | Simple Telugu meaning |
|---|---|
| Loss Function | తప్పును కొలిచే విధానం |
| Probability | సంభావ్యత |
| One-Hot Encoding | 0, 1 రూపంలో మార్చడం |
| Weights | లక్షణాలకు ఇచ్చే ప్రాముఖ్యత |
| Bias | అదనపు స్థిర విలువ |
| Polynomial Features | కొత్త గణిత లక్షణాలు సృష్టించడం |
| Degree | గరిష్ఠ ఘాతం |
| Underfitting | డేటాను సరిగ్గా నేర్చుకోలేకపోవడం |
| Overfitting | ట్రైనింగ్ డేటాను అతిగా నేర్చుకోవడం |
| Hyperparameter | ముందుగా నిర్ణయించే సెట్టింగ్ |
| Optimum | సరైన లేదా అనుకూలమైన |

---

## ✅ Today's Learning Checklist

- [ ] Understand Softmax Regression.
- [ ] Practice One-Hot Encoding.
- [ ] Derive Categorical Cross-Entropy.
- [ ] Understand weights and bias.
- [ ] Practice Polynomial Features.
- [ ] Understand degree 1, 2 and 3.
- [ ] Understand underfitting and overfitting.
- [ ] Practice Scikit-learn implementation.

---

**Next:** Continue with the next new topic from the institute classroom notes. Previous concepts are not repeated.
