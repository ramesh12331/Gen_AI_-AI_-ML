# 📘 Adjusted R² Score – Machine Learning

## 📌 1. What is Adjusted R² Score?

**Adjusted R² Score (Adjusted R-Squared)** is a regression model evaluation metric.

It measures how well a regression model explains the variation in the target variable while considering the number of independent variables (features) used in the model.

### 🎯 Simple Definition

Adjusted R² evaluates the performance of a regression model by considering both:

- How well the model explains the target variable.
- How many independent variables are used in the model.

### Important Points

- Higher Adjusted R² generally indicates a better model fit.
- It considers the number of features used by the model.
- It can increase or decrease when new features are added.
- It is commonly used in Multiple Linear Regression.

---

## 🧠 2. Why Do We Need Adjusted R²?

Let's understand with an example.

Suppose we are building a Student Marks Prediction Model.

We use the following features:

| Feature | Description |
|---|---|
| Study Hours | Number of hours a student studies |
| Attendance | Student attendance percentage |
| Sleep Hours | Number of hours a student sleeps |
| Favorite Color | Student's favorite color |

Study Hours, Attendance, and Sleep Hours may help predict student marks.

However, Favorite Color may not have any meaningful relationship with student marks.

If we add unnecessary features to a regression model, the R² Score may increase or remain unchanged even when the new features do not meaningfully improve the model.

**Adjusted R² helps account for the number of features when evaluating the model.**

---

## 📐 3. Adjusted R² Mathematical Formula

The formula for Adjusted R² is:

$$
Adjusted\ R^2 =
1-(1-R^2)\frac{n-1}{n-p-1}
$$

### Formula Explanation

| Symbol | Meaning |
|---|---|
| R² | R-Squared Score |
| n | Number of observations |
| p | Number of independent variables (features) |
| 1 | Constant value |

### Important

- `n` represents the total number of rows in the dataset.
- `p` represents the total number of independent variables used in the model.
- `R²` represents the R-Squared Score.

---

## 🔢 4. Step-by-Step Numerical Example

Let's calculate Adjusted R² using the following values.

### Given Values

```python
R2 Score = 0.90

n = 100

p = 3
```

Where:

- R² = 0.90
- Number of observations = 100
- Number of independent variables = 3

### Step 1: Write the Formula

$$
Adjusted\ R^2 =
1-(1-R^2)\frac{n-1}{n-p-1}
$$

### Step 2: Substitute the Values

$$
Adjusted\ R^2 =
1-(1-0.90)\frac{100-1}{100-3-1}
$$

### Step 3: Simplify

$$
=1-(0.10)\frac{99}{96}
$$

$$
=1-(0.10 \times 1.03125)
$$

$$
=1-0.103125
$$

### Final Answer

$$
\boxed{Adjusted\ R^2=0.896875}
$$

### Result Comparison

| Metric | Value |
|---|---:|
| R² Score | 0.9000 |
| Adjusted R² Score | 0.8969 |

**Observation:** Adjusted R² is slightly lower than R² because it accounts for the number of independent variables.

---

## 📊 5. Difference Between R² and Adjusted R²

| Feature | R² Score | Adjusted R² |
|---|---|---|
| Full Form | R-Squared | Adjusted R-Squared |
| Measures | Explained variation | Explained variation with feature-count adjustment |
| Considers number of features | No direct penalty | Yes |
| Adding unnecessary features | Never decreases in ordinary least squares | Can decrease |
| Common Use | General regression evaluation | Comparing models with different feature counts |

### Important Concept

**R² Score:**

In ordinary least-squares regression, adding more independent variables cannot decrease the R² Score. It may increase or remain unchanged.

**Adjusted R² Score:**

Adjusted R² considers the number of independent variables.

- If a new feature improves the model sufficiently, Adjusted R² may increase.
- If a new feature does not improve the model sufficiently, Adjusted R² may decrease.

---

## 💻 6. Python Implementation of Adjusted R²

Let's calculate Adjusted R² using Python and Scikit-learn.

### Step 1: Install Required Libraries

Run this command in the VS Code terminal:

```bash
pip install numpy pandas scikit-learn
```

### Step 2: Import Required Libraries

```python
import numpy as np

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
```

### Step 3: Create Dataset

```python
# Independent variables (Features)

X = np.array([
    [2, 70, 8],
    [3, 75, 7],
    [4, 80, 8],
    [5, 85, 6],
    [6, 90, 7],
    [7, 95, 8],
    [8, 92, 7],
    [9, 88, 6],
    [10, 96, 8],
    [11, 98, 7]
])


# Dependent variable (Target)

y = np.array([
    40, 45, 50, 55, 60,
    65, 70, 75, 80, 85
])
```

### Step 4: Train Linear Regression Model

```python
# Create Linear Regression model

model = LinearRegression()


# Train the model

model.fit(X, y)
```

### Step 5: Make Predictions

```python
# Predict target values

y_pred = model.predict(X)
```

### Step 6: Calculate R² Score

```python
# Calculate R² Score

r2 = r2_score(y, y_pred)

print("R2 Score:", r2)
```

### Step 7: Calculate Adjusted R² Score

```python
# Number of observations

n = X.shape[0]


# Number of independent variables

p = X.shape[1]


# Calculate Adjusted R²

adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)


print("R2 Score:", r2)

print("Adjusted R2 Score:", adjusted_r2)
```

### Understanding Important Python Statements

**1. Number of observations**

```python
n = X.shape[0]
```

Returns the number of rows in the dataset.

**2. Number of features**

```python
p = X.shape[1]
```

Returns the number of independent variables (columns).

**3. Adjusted R² calculation**

```python
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
```

Uses the Adjusted R² mathematical formula.

**Note:** This example calculates scores on the training dataset for demonstration. For a realistic performance evaluation, use a separate test dataset or cross-validation.

---

## 🚀 7. Complete Python Program

File Name: `adjusted_r2.py`

```python
# ============================================================
# MACHINE LEARNING
# ADJUSTED R-SQUARED SCORE
# ============================================================

# STEP 1: Import Required Libraries

import numpy as np

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression


# STEP 2: Create Dataset

# Independent variables (Features)

X = np.array([
    [2, 70, 8],
    [3, 75, 7],
    [4, 80, 8],
    [5, 85, 6],
    [6, 90, 7],
    [7, 95, 8],
    [8, 92, 7],
    [9, 88, 6],
    [10, 96, 8],
    [11, 98, 7]
])


# Dependent variable (Target)

y = np.array([
    40, 45, 50, 55, 60,
    65, 70, 75, 80, 85
])


# STEP 3: Create Linear Regression Model

model = LinearRegression()


# STEP 4: Train the Model

model.fit(X, y)


# STEP 5: Make Predictions

y_pred = model.predict(X)


# STEP 6: Calculate R² Score

r2 = r2_score(y, y_pred)


# STEP 7: Calculate Number of Observations

n = X.shape[0]


# STEP 8: Calculate Number of Features

p = X.shape[1]


# STEP 9: Calculate Adjusted R² Score

adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)


# STEP 10: Display Results

print("R2 Score:", r2)

print("Adjusted R2 Score:", adjusted_r2)


# ============================================================
# END OF PROGRAM
# ============================================================
```

---

## 🎯 8. When Do We Use Adjusted R²?

Adjusted R² is especially useful in Multiple Linear Regression.

### Example

Suppose we have two regression models:

| Model | Number of Features | R² | Adjusted R² |
|---|---:|---:|---:|
| Model A | 3 | 0.90 | 0.896 |
| Model B | 8 | 0.91 | 0.901 |

Model B uses more features than Model A.

However, Model B also has a higher Adjusted R².

This suggests that the additional features improve the model fit sufficiently to offset the feature-count adjustment.

**Remember:** Adjusted R² should not be the only criterion for selecting a model. Also consider test performance, cross-validation, and domain knowledge.

---

## 🏢 9. Real-World Applications

Adjusted R² can be useful in regression problems involving multiple features.

| Industry | Application |
|---|---|
| Real Estate | House price prediction |
| Education | Student marks prediction |
| Finance | Revenue prediction |
| Healthcare | Predicting numerical health measurements |
| Marketing | Sales forecasting |
| Business | Demand prediction |

---

## 🎤 10. Interview Questions and Answers

### Q1. What is Adjusted R²?

Adjusted R² is a regression evaluation metric that adjusts the R² Score based on the number of independent variables and observations.

### Q2. Why do we use Adjusted R²?

We use Adjusted R² to evaluate regression models while accounting for the number of features used.

### Q3. What is the difference between R² and Adjusted R²?

R² does not directly penalize adding more features, whereas Adjusted R² accounts for the number of features.

### Q4. Can Adjusted R² decrease?

Yes. Adjusted R² can decrease when an additional feature does not improve the model sufficiently.

### Q5. Can Adjusted R² be negative?

Yes. Adjusted R² can be negative.

### Q6. Where is Adjusted R² commonly used?

It is commonly used in Multiple Linear Regression.

### Q7. What are n and p in the Adjusted R² formula?

- n = Number of observations.
- p = Number of independent variables.

### Q8. Which is better: R² or Adjusted R²?

Neither is universally better. Adjusted R² is especially useful when comparing regression models with different numbers of features.

---

## 📝 11. Practice Questions

Test your understanding.

**Q1. What does `p` represent in the Adjusted R² formula?**

- A) Number of rows
- B) Number of features
- C) Number of predictions
- D) Number of targets

**Q2. What happens to R² when additional features are added in ordinary least-squares regression?**

- A) It always decreases
- B) It always becomes zero
- C) It can increase or remain unchanged
- D) It always becomes negative

**Q3. Why do we use Adjusted R²?**

- A) To remove missing values
- B) To account for the number of features
- C) For data visualization
- D) To calculate classification accuracy

**Q4. Can Adjusted R² decrease?**

- A) Yes
- B) No

**Q5. In which regression model is Adjusted R² especially useful?**

- A) Simple Linear Regression
- B) Multiple Linear Regression
- C) Logistic Regression
- D) Decision Tree Classification

---

## 📚 12. Final Summary

| Concept | Explanation |
|---|---|
| R² Score | Measures explained variation |
| Adjusted R² | R² adjusted for feature count |
| n | Number of observations |
| p | Number of independent variables |
| Main Purpose | Evaluate models considering the number of features |
| Maximum Value | 1 |
| Negative Value | Possible |
| Higher Value | Generally indicates a better fit |

### ⭐ Important Formula to Remember

$$
\boxed{
Adjusted\ R^2 =
1-(1-R^2)\frac{n-1}{n-p-1}
}
$$

**Congratulations! 🎉 You have completed the Adjusted R² Score topic.**

Keep practising regression evaluation metrics to understand how machine learning models perform.
```

---

## 📂 Suggested GitHub Folder Structure

```text
Regression/
│
├── 01_Simple_Linear_Regression/
│
├── 02_Model_Evaluation/
│   │
│   ├── 01_MSE_R2_Score/
│   │   ├── README.md
│   │   └── README_TELUGU.md
│   │
│   ├── 02_MAE/
│   │   ├── README.md
│   │   ├── README_TELUGU.md
│   │   └── mae.py
│   │
│   ├── 03_RMSE/
│   │   ├── README.md
│   │   └── rmse.py
│   │
│   └── 04_Adjusted_R2/
│       ├── README.md
│       └── adjusted_r2.py
```

**Next topic:** MAPE (Mean Absolute Percentage Error).