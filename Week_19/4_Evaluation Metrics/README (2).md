# 📊 Classification Metrics → ROC Curve

**Beginner-Friendly Machine Learning Study Notes**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-Machine_Learning-F7931E?logo=scikitlearn&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Classification_Metrics-blue)
![Level](https://img.shields.io/badge/Level-Beginner-green)

> 💡 **Learning tip:** Study one section at a time. Open the expandable sections to see extra explanations and practice.

---

## 🧭 Table of Contents

1. [Introduction](#1-introduction)
2. [Precision, Recall and F1-score](#2-precision-recall-and-f1-score)
3. [Multiclass Classification Example](#3-multiclass-classification-example)
4. [Macro and Weighted Average](#4-macro-and-weighted-average)
5. [From Linear Equation to Probability](#5-from-linear-equation-to-probability)
6. [Sigmoid Function](#6-sigmoid-function)
7. [Classification Threshold](#7-classification-threshold)
8. [TPR, FPR and ROC Curve](#8-tpr-fpr-and-roc-curve)
9. [Complete Python Code](#9-complete-python-code)
10. [Complete Dry Run](#10-complete-dry-run)
11. [Quick Reference](#11-quick-reference)
12. [Interview Questions](#12-interview-questions)
13. [Final Summary](#13-final-summary)

---

# 1. Introduction

## 📖 What are Classification Evaluation Metrics?

**Definition:** Classification evaluation metrics are measurements used to evaluate how well a Machine Learning classification model predicts the correct classes.

They help us understand:

- How many predictions are correct.
- How many predictions are incorrect.
- How many actual positive cases the model identifies.
- How many negative cases are wrongly predicted as positive.

### 💡 Real-world example

Imagine an email spam detection model:

- `1` → Spam
- `0` → Not Spam

The model predicts whether an email is spam or not spam. We compare the actual email categories with the predicted categories to evaluate the model.

<details>
<summary>🔍 Why do we need different evaluation metrics?</summary>

One metric cannot explain every type of model error.

For example:

- A spam filter should avoid marking important emails as spam.
- A disease screening model should avoid missing people who may have a disease.
- A fraud detection model should identify suspicious transactions without creating too many false alarms.

Precision, Recall, F1-score, TPR, FPR and ROC help us understand different aspects of classification performance.

</details>

---

# 2. Precision, Recall and F1-score

## 🎯 A. Precision

### Definition

Precision measures how many predicted positive cases are actually positive.

**Simple meaning:** Out of everything the model predicted as positive, how many predictions were correct?

### Formula

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

Where:

- `TP` = True Positive
- `FP` = False Positive

### Example

Suppose a model predicts 10 emails as spam.

- 8 are actually spam.
- 2 are normal emails.

$$
\text{Precision} = \frac{8}{8+2} = \frac{8}{10} = 0.80
$$

**Precision = 80%**

### Python syntax

```python
from sklearn.metrics import precision_score

precision = precision_score(y_actual, y_predicted)

print("Precision:", precision)
```

<details>
<summary>🔍 When is Precision important?</summary>

Precision is important when false positive predictions are costly.

Example: If a legitimate email is incorrectly marked as spam, the user may miss an important message. A spam filter therefore benefits from high precision.

</details>

## 🎣 B. Recall

### Definition

Recall measures how many actual positive cases are correctly identified by the model.

**Simple meaning:** Out of all actual positive cases, how many did the model find?

### Formula

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

Where:

- `TP` = True Positive
- `FN` = False Negative

### Example

Suppose there are 10 actual spam emails.

- The model correctly identifies 8 spam emails.
- The model misses 2 spam emails.

$$
\text{Recall} = \frac{8}{8+2} = \frac{8}{10} = 0.80
$$

**Recall = 80%**

### Python syntax

```python
from sklearn.metrics import recall_score

recall = recall_score(y_actual, y_predicted)

print("Recall:", recall)
```

<details>
<summary>🔍 When is Recall important?</summary>

Recall is important when missing an actual positive case is costly.

Example: In a disease screening system, missing a person who may have a disease can be dangerous. High recall helps identify more of the actual positive cases.

</details>

## ⚖️ C. F1-score

### Definition

F1-score is the harmonic mean of Precision and Recall. It combines both metrics into one score.

**Simple meaning:** F1-score helps us understand the balance between Precision and Recall.

### Formula

$$
F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}
{\text{Precision} + \text{Recall}}
$$

### Example 1: Precision = 60%, Recall = 100%

Arithmetic mean:

$$
\frac{60 + 100}{2} = 80
$$

F1-score:

$$
F1 = 2 \times \frac{60 \times 100}{60 + 100}
= \frac{12000}{160} = 75
$$

**F1-score = 75%**

### Example 2: Precision = 80%, Recall = 80%

$$
F1 = 2 \times \frac{80 \times 80}{80 + 80} = 80
$$

**F1-score = 80%**

### Comparison

| Precision | Recall | Arithmetic Mean | F1-score |
|---:|---:|---:|---:|
| 80% | 80% | 80% | 80% |
| 60% | 100% | 80% | 75% |

> **Important:** F1-score penalizes an imbalance between Precision and Recall. It is lower when one of the two values is much lower than the other.

### Python syntax

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_actual, y_predicted)

print("F1-score:", f1)
```

<details>
<summary>🧠 Why harmonic mean instead of arithmetic mean?</summary>

The arithmetic mean can hide an imbalance. For example, Precision = 60% and Recall = 100% produce an arithmetic mean of 80%, but the F1-score is 75%.

The harmonic mean gives more influence to the smaller value. This makes F1 useful when we want both Precision and Recall to be reasonably high.

</details>

---

# 3. Multiclass Classification Example

## 🐶 Dog / Cat / Rabbit

**Definition:** Multiclass classification means predicting one class from more than two possible classes.

Example classes:

- Dog
- Cat
- Rabbit

## Confusion Matrix

Rows are **Actual** values. Columns are **Predicted** values.

| Actual / Predicted | Dog | Cat | Rabbit | Total |
|---|---:|---:|---:|---:|
| Dog | 25 | 5 | 10 | 40 |
| Cat | 0 | 30 | 4 | 34 |
| Rabbit | 4 | 10 | 20 | 34 |
| **Total** | **29** | **45** | **34** | **108** |

### Understand the matrix

- Diagonal values represent correct predictions.
- Other values represent incorrect predictions.

Example — Dog row:

- 25 dogs were predicted as Dog.
- 5 dogs were predicted as Cat.
- 10 dogs were predicted as Rabbit.

## Per-class Precision and Recall

For each class:

$$
\text{Precision} = \frac{\text{Diagonal Value}}{\text{Column Total}}
$$

$$
\text{Recall} = \frac{\text{Diagonal Value}}{\text{Row Total}}
$$

### 🐶 Dog calculation

Precision:

$$
\text{Precision} = \frac{25}{29} \approx 0.862
$$

Recall:

$$
\text{Recall} = \frac{25}{40} = 0.625
$$

F1-score:

$$
F1 = 2 \times \frac{0.862 \times 0.625}{0.862 + 0.625}
\approx 0.725
$$

### 🐱 Cat calculation

Precision:

$$
\text{Precision} = \frac{30}{45} \approx 0.667
$$

Recall:

$$
\text{Recall} = \frac{30}{34} \approx 0.882
$$

F1-score:

$$
F1 = 2 \times \frac{0.667 \times 0.882}{0.667 + 0.882}
\approx 0.759
$$

### 🐰 Rabbit calculation

Precision:

$$
\text{Precision} = \frac{20}{34} \approx 0.588
$$

Recall:

$$
\text{Recall} = \frac{20}{34} \approx 0.588
$$

F1-score:

$$
F1 \approx 0.588
$$

### Complete results

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Dog | 0.862 | 0.625 | 0.725 |
| Cat | 0.667 | 0.882 | 0.759 |
| Rabbit | 0.588 | 0.588 | 0.588 |

<details>
<summary>🧮 Why does Precision use column totals and Recall use row totals?</summary>

Think about the questions:

- **Precision:** Of all items predicted as Dog, how many really were Dog? Look down the Dog prediction column. The column total is 29.
- **Recall:** Of all actual Dogs, how many were correctly predicted as Dog? Look across the actual Dog row. The row total is 40.

Therefore, Precision uses the predicted-class column total, while Recall uses the actual-class row total.

</details>

---

# 4. Macro and Weighted Average

## ⚖️ A. Macro Average

### Definition

Macro Average calculates the metric for each class and takes the simple average. Every class gets equal importance.

### Formula

$$
\text{Macro Average} = \frac{M_1 + M_2 + \cdots + M_k}{k}
$$

Where:

- `M_i` = Metric for class `i`.
- `k` = Number of classes.

### Example: Macro Precision

$$
\text{Macro Precision} =
\frac{0.862 + 0.667 + 0.588}{3}
\approx 0.706
$$

## 🟧 B. Weighted Average

### Definition

Weighted Average calculates the metric for every class and weights it according to the number of actual samples in that class.

### Formula

$$
\text{Weighted Average} =
\frac{\sum_{i=1}^{k} n_i M_i}{\sum_{i=1}^{k} n_i}
$$

Where:

- `n_i` = Number of actual samples in class `i`.
- `M_i` = Metric for class `i`.
- `k` = Number of classes.

### Example: Weighted Precision

$$
\frac{40(0.862) + 34(0.667) + 34(0.588)}{108}
\approx 0.711
$$

### Comparison

| Average | How it works | Approximate result (P / R / F1) |
|---|---|---:|
| Macro | Equal importance for each class | 0.71 / 0.70 / 0.69 |
| Weighted | Weighted by actual class size | 0.71 / 0.69 / 0.69 |

Values are rounded. Macro and weighted averages are different ways of summarizing per-class metrics.

### Python syntax

```python
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

# Macro average: every class has equal weight
macro_precision = precision_score(
    y_true, y_pred, average="macro"
)

macro_recall = recall_score(
    y_true, y_pred, average="macro"
)

macro_f1 = f1_score(
    y_true, y_pred, average="macro"
)

# Weighted average: class support determines the weight
weighted_precision = precision_score(
    y_true, y_pred, average="weighted"
)

weighted_recall = recall_score(
    y_true, y_pred, average="weighted"
)

weighted_f1 = f1_score(
    y_true, y_pred, average="weighted"
)

print("Macro:", macro_precision, macro_recall, macro_f1)
print("Weighted:", weighted_precision, weighted_recall, weighted_f1)
```

Get class counts using Pandas:

```python
print(df["target"].value_counts())
```

<details>
<summary>💡 When should we use Macro and Weighted Average?</summary>

- Use **Macro Average** when every class should have equal importance, including minority classes.
- Use **Weighted Average** when you want each class's contribution to reflect how many actual samples it contains.

</details>

---

# 5. From Linear Equation to Probability

## 📈 Step 1 — Linear equation

A linear combination of input features produces a numerical score.

$$
z = \theta_0 + \theta_1x_1 + \theta_2x_2 + \cdots + \theta_nx_n
$$

Where:

- `z` = Model score.
- `θ₀` = Intercept.
- `θ₁, θ₂, ...` = Model coefficients.
- `x₁, x₂, ...` = Input features.

### Example

Suppose:

$$
z = -2 + 0.8x
$$

If `x = 5`:

$$
z = -2 + 0.8(5) = 2
$$

The score is **2**.

**Problem:** The score can be any number. It is not necessarily between 0 and 1. We need a function that converts it into a probability.

> ⚠️ **Mathematical clarification:** The Normal Equation
>
> $$
> \theta = (X^T X)^{-1}X^T y
> $$
>
> is used in ordinary least-squares Linear Regression under suitable matrix conditions. It is not the standard method for fitting Logistic Regression. Logistic Regression generally learns coefficients by optimizing a classification loss function.

---

# 6. Sigmoid Function

## 📈 Definition

The Sigmoid function converts a numerical score into a probability between 0 and 1.

### Formula

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Where:

- `z` = Model score.
- `e` = Mathematical constant.
- `σ(z)` = Predicted probability.

### Example

Suppose:

$$
z = 2
$$

Then:

$$
\sigma(2) = \frac{1}{1 + e^{-2}} \approx 0.881
$$

**Probability = 88.1%**

### Understand the output

| Score (`z`) | Sigmoid output |
|---:|---:|
| -3 | 0.047 |
| -2 | 0.119 |
| -1 | 0.269 |
| 0 | 0.500 |
| 1 | 0.731 |
| 2 | 0.881 |
| 3 | 0.953 |

> **Remember:** Sigmoid outputs values between 0 and 1.

---

# 7. Classification Threshold

## 🎚️ Definition

A classification threshold is a cutoff value used to convert predicted probabilities into class labels.

A common default threshold is **0.5**.

### Example

| Probability | Prediction |
|---:|---|
| 0.85 | 1 (Positive) |
| 0.70 | 1 (Positive) |
| 0.50 | 1 (Positive) |
| 0.40 | 0 (Negative) |
| 0.10 | 0 (Negative) |

### Formula

$$
\text{Prediction} =
\begin{cases}
1 & \text{if } P \geq \text{Threshold} \\
0 & \text{if } P < \text{Threshold}
\end{cases}
$$

### Python example

```python
# Predicted probabilities
probabilities = [0.85, 0.70, 0.40, 0.10]

# Classification threshold
threshold = 0.50

# Convert probabilities into classes
predictions = [
    1 if p >= threshold else 0
    for p in probabilities
]

print(predictions)
```

Output:

```text
[1, 1, 0, 0]
```

<details>
<summary>💡 What happens when we change the threshold?</summary>

- **Lower threshold:** More cases are predicted as positive. TPR generally increases, and FPR generally increases.
- **Higher threshold:** Fewer cases are predicted as positive. TPR generally decreases, and FPR generally decreases.

The best threshold depends on the problem and the cost of false positives and false negatives.

</details>

---

# 8. TPR, FPR and ROC Curve

## 🚦 A. Confusion Matrix

| Actual / Predicted | 1 (Positive) | 0 (Negative) |
|---|---:|---:|
| 1 (Positive) | TP | FN |
| 0 (Negative) | FP | TN |

## 🟢 B. TPR — True Positive Rate

### Definition

TPR measures the percentage of actual positive cases correctly identified by the model. It is also called **Recall**.

### Formula

$$
TPR = \frac{TP}{TP + FN}
$$

**Simple meaning:** Out of all actual positive cases, how many did the model catch?

## 🔴 C. FPR — False Positive Rate

### Definition

FPR measures the percentage of actual negative cases incorrectly predicted as positive.

### Formula

$$
FPR = \frac{FP}{FP + TN}
$$

**Simple meaning:** Out of all actual negative cases, how many did the model wrongly mark as positive?

## 🧮 Dry Run

Suppose:

- TP = 40
- FN = 10
- FP = 5
- TN = 45

TPR:

$$
TPR = \frac{40}{40 + 10} = 0.80 = 80\%
$$

FPR:

$$
FPR = \frac{5}{5 + 45} = 0.10 = 10\%
$$

**Results:**

- TPR = 80%
- FPR = 10%

## 📈 D. What is ROC Curve?

ROC stands for **Receiver Operating Characteristic**.

A ROC Curve is a graph that plots:

- **X-axis:** False Positive Rate (FPR).
- **Y-axis:** True Positive Rate (TPR).

It shows the trade-off between identifying actual positives and generating false alarms at different thresholds.

### How is a ROC Curve created?

1. The model predicts probabilities.
2. Choose a threshold.
3. Calculate TPR and FPR.
4. Change the threshold.
5. Calculate TPR and FPR again.
6. Plot all the points on a graph.

### Important observation

| Threshold change | TPR | FPR |
|---|---|---|
| Lower threshold | Generally increases | Generally increases |
| Higher threshold | Generally decreases | Generally decreases |

---

# 9. Complete Python Code

## 💻 A. Reproduce the Multiclass Example

This program reconstructs actual and predicted labels from the Dog/Cat/Rabbit confusion matrix and prints the classification report.

```python
# ==========================================================
# MULTICLASS CLASSIFICATION METRICS
# Dog / Cat / Rabbit
# ==========================================================

import numpy as np

from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

# STEP 1: Create the confusion matrix
# Rows = Actual
# Columns = Predicted

cm = np.array([
    [25, 5, 10],
    [0, 30, 4],
    [4, 10, 20]
])

# STEP 2: Define class names
labels = ["Dog", "Cat", "Rabbit"]

# STEP 3: Convert the confusion matrix
# into actual and predicted arrays

y_true = []
y_pred = []

# Visit every cell in the confusion matrix
for i in range(3):
    for j in range(3):

        # Add actual class i, cm[i, j] times
        y_true += [i] * cm[i, j]

        # Add predicted class j, cm[i, j] times
        y_pred += [j] * cm[i, j]

# STEP 4: Print the classification report
print(
    classification_report(
        y_true,
        y_pred,
        labels=[0, 1, 2],
        target_names=labels,
        digits=3
    )
)

# STEP 5: Print the confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))
```

## 💻 B. Plot ROC Curve

```python
# ==========================================================
# ROC CURVE USING LOGISTIC REGRESSION
# ==========================================================

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split

# STEP 1: Create a sample binary classification dataset
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    random_state=42
)

# STEP 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    random_state=42
)

# STEP 3: Create the Logistic Regression model
model = LogisticRegression()

# STEP 4: Train the model
model.fit(X_train, y_train)

# STEP 5: Get probabilities for the positive class (class 1)
probs = model.predict_proba(X_test)[:, 1]

# STEP 6: Calculate False Positive Rate, True Positive Rate
# and threshold values
fpr, tpr, thresholds = roc_curve(y_test, probs)

# STEP 7: Calculate Area Under the Curve (AUC)
roc_auc = auc(fpr, tpr)

print("AUC:", roc_auc)

# STEP 8: Plot the ROC curve
plt.plot(
    fpr,
    tpr,
    label=f"ROC Curve (AUC = {roc_auc:.2f})"
)

# Plot the random classifier reference line
plt.plot(
    [0, 1],
    [0, 1],
    "k--",
    label="Random Guess"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
```

### Install required libraries

Run this command in your VS Code terminal:

```bash
pip install numpy pandas scikit-learn matplotlib
```

---

# 10. Complete Dry Run

## 🧮 A. Multiclass example

Given:

| Actual / Predicted | Dog | Cat | Rabbit | Total |
|---|---:|---:|---:|---:|
| Dog | 25 | 5 | 10 | 40 |
| Cat | 0 | 30 | 4 | 34 |
| Rabbit | 4 | 10 | 20 | 34 |
| **Total** | **29** | **45** | **34** | **108** |

**Dog**

- Precision = 25 / 29 = 0.862
- Recall = 25 / 40 = 0.625
- F1-score ≈ 0.725

**Cat**

- Precision = 30 / 45 = 0.667
- Recall = 30 / 34 = 0.882
- F1-score ≈ 0.759

**Rabbit**

- Precision = 20 / 34 = 0.588
- Recall = 20 / 34 = 0.588
- F1-score ≈ 0.588

## 🚦 B. Binary example

Given:

- TP = 40
- FN = 10
- FP = 5
- TN = 45

| Metric | Calculation | Result |
|---|---|---:|
| TPR | 40 / (40 + 10) | 80% |
| FPR | 5 / (5 + 45) | 10% |

---

# 11. Quick Reference

| Metric | Formula | Meaning |
|---|---|---|
| Precision | TP / (TP + FP) | Correctness of positive predictions |
| Recall | TP / (TP + FN) | Coverage of actual positives |
| F1-score | 2 × P × R / (P + R) | Balance of Precision and Recall |
| TPR | TP / (TP + FN) | True Positive Rate; same as Recall |
| FPR | FP / (FP + TN) | False alarm rate |
| ROC | TPR vs. FPR | Performance across classification thresholds |
| AUC | Area under ROC | Summarizes ROC curve performance |

### 🧠 Easy memory trick

- 🎯 **Precision** → How many predicted positives are correct?
- 🎣 **Recall** → How many actual positives did we catch?
- ⚖️ **F1-score** → Balance between Precision and Recall.
- 🟢 **TPR** → Same as Recall.
- 🔴 **FPR** → How many false alarms?
- 🚦 **ROC** → TPR against FPR.
- 📈 **AUC** → Area under ROC.

---

# 12. Interview Questions

<details>
<summary>Q1. What is Precision?</summary>

Precision measures the proportion of predicted positive cases that are actually positive.

$$
Precision = \frac{TP}{TP + FP}
$$

</details>

<details>
<summary>Q2. What is Recall?</summary>

Recall measures the proportion of actual positive cases correctly identified by the model.

$$
Recall = \frac{TP}{TP + FN}
$$

</details>

<details>
<summary>Q3. What is F1-score?</summary>

F1-score is the harmonic mean of Precision and Recall.

$$
F1 = 2 \times \frac{P \times R}{P + R}
$$

</details>

<details>
<summary>Q4. Why do we use harmonic mean for F1?</summary>

The harmonic mean gives more importance to the smaller of Precision and Recall. It penalizes a large imbalance between the two metrics.

</details>

<details>
<summary>Q5. What is the difference between Precision and Recall?</summary>

- Precision asks: Of the cases predicted positive, how many were actually positive?
- Recall asks: Of the actual positive cases, how many did the model identify?

</details>

<details>
<summary>Q6. What is Multiclass Classification?</summary>

Multiclass classification predicts one class from more than two possible classes, such as Dog, Cat or Rabbit.

</details>

<details>
<summary>Q7. What is Macro Average?</summary>

Macro Average calculates a metric for each class and takes the simple average. Every class gets equal importance.

</details>

<details>
<summary>Q8. What is Weighted Average?</summary>

Weighted Average calculates a metric for each class and weights it according to the number of actual samples in that class.

</details>

<details>
<summary>Q9. What is the Sigmoid function?</summary>

The Sigmoid function converts a numerical score into a value between 0 and 1.

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

</details>

<details>
<summary>Q10. What is a classification threshold?</summary>

A threshold is a cutoff used to convert a predicted probability into a class label. A common default is 0.5.

</details>

<details>
<summary>Q11. What is TPR?</summary>

TPR means True Positive Rate. It is the same as Recall.

$$
TPR = \frac{TP}{TP + FN}
$$

</details>

<details>
<summary>Q12. What is FPR?</summary>

FPR means False Positive Rate. It measures the proportion of actual negative cases incorrectly predicted as positive.

$$
FPR = \frac{FP}{FP + TN}
$$

</details>

<details>
<summary>Q13. What is ROC Curve?</summary>

ROC stands for Receiver Operating Characteristic. It plots TPR on the Y-axis against FPR on the X-axis at different classification thresholds.

</details>

<details>
<summary>Q14. What happens when the threshold decreases?</summary>

The model generally predicts more positive cases. TPR generally increases, and FPR generally increases.

</details>

<details>
<summary>Q15. What is AUC?</summary>

AUC means Area Under the ROC Curve. It summarizes the ROC curve. AUC of 1 represents perfect ranking, while 0.5 represents random-ranking performance.

</details>

---

# 13. Final Summary

## 🎓 What did we learn?

| Topic | Main concept |
|---|---|
| Precision | Correct positive predictions |
| Recall | Identify actual positives |
| F1-score | Balance of Precision and Recall |
| Multiclass Metrics | Evaluate multiple classes |
| Macro Average | Equal class importance |
| Weighted Average | Class-size-based importance |
| Linear Equation | Calculate model score |
| Sigmoid | Convert score into probability |
| Threshold | Convert probability into class |
| TPR | True Positive Rate |
| FPR | False Positive Rate |
| ROC Curve | TPR vs. FPR graph |
| AUC | Area under ROC |

## ✅ Learning Checklist

- [ ] Understand Precision.
- [ ] Understand Recall.
- [ ] Calculate F1-score.
- [ ] Read a multiclass confusion matrix.
- [ ] Calculate per-class metrics.
- [ ] Understand Macro Average.
- [ ] Understand Weighted Average.
- [ ] Understand the linear equation.
- [ ] Learn the Sigmoid function.
- [ ] Understand classification thresholds.
- [ ] Calculate TPR and FPR.
- [ ] Understand the ROC Curve.
- [ ] Run the Python programs.
- [ ] Practise the interview questions.

> ⭐ **Final learning point:** Classification metrics help us understand different types of model performance. The best metric depends on the problem, the class distribution and the cost of different prediction errors.
>
> Keep practising these formulas and Python examples until you can explain each metric without looking at your notes.
