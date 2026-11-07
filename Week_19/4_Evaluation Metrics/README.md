# 📊 Classification Metrics → ROC Curve

<p align="center">
  <b>Beginner-Friendly Machine Learning Study Notes</b>
</p>

<p align="center">
  ![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
  ![Scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white)
  ![Topic](https://img.shields.io/badge/Topic-Classification%20Metrics-blue)
  ![Level](https://img.shields.io/badge/Level-Beginner-green)
</p>

> 💡 **Learning tip:** Read one topic at a time. Expand the interactive sections in GitHub to see additional explanations, examples and dry runs.

---

# 🧭 Table of Contents

| Icon | Topic |
|---|---|
| 📖 | [Introduction](#1-introduction) |
| 🎯 | [Precision, Recall and F1-score](#2-precision-recall-and-f1-score) |
| 🐶 | [Multiclass Classification Example](#3-multiclass-classification-example) |
| ⚖️ | [Macro and Weighted Average](#4-macro-and-weighted-average) |
| 📈 | [From Linear Equation to Probability](#5-from-linear-equation-to-probability) |
| 🔢 | [Sigmoid Function](#6-sigmoid-function) |
| 🎚️ | [Classification Threshold](#7-classification-threshold) |
| 🚦 | [TPR, FPR and ROC Curve](#8-tpr-fpr-and-roc-curve) |
| 💻 | [Complete Python Code](#9-complete-python-code) |
| 🧮 | [Complete Dry Run](#10-complete-dry-run) |
| 📝 | [Quick Reference](#11-quick-reference) |
| 🎤 | [Interview Questions](#12-interview-questions) |
| ✅ | [Final Summary](#13-final-summary) |

---

# 1. Introduction

## 📖 What are Classification Evaluation Metrics?

**Definition:**

Classification Evaluation Metrics are measurements used to evaluate how well a Machine Learning classification model predicts the correct classes.

**Simple meaning:**

They help us understand:
- How many predictions are correct.
- How many predictions are incorrect.
- How many actual positive cases the model identifies.
- How many negative cases are wrongly predicted as positive.

### 💡 Real-world example

Imagine an email spam detection model.

- `1` → Spam
- `0` → Not Spam

The model predicts whether an email is spam or not spam.

We compare actual email categories with predicted categories to evaluate the model.

<details>
<summary>💡 Why do we need different evaluation metrics?</summary>

Imagine two models have the same accuracy.

One model may correctly identify most spam emails, while another may miss many spam emails.

Accuracy alone cannot explain every type of model mistake.

Therefore, we use Precision, Recall, F1-score and other metrics.

</details>

---

# 2. Precision, Recall and F1-score

## 🎯 A. Precision

### Definition

Precision measures how many predicted positive cases are actually positive.

**Simple meaning:** Out of everything the model predicted as positive, how many predictions were correct?

### Formula

$$
Precision = \frac{TP}{TP+FP}
$$

Where:

- TP = True Positive
- FP = False Positive

### Example

Suppose a model predicts 10 emails as spam.

Out of those 10 emails:
- 8 are actually spam.
- 2 are normal emails.

$$
Precision = \frac{8}{8+2}
$$

$$
Precision = \frac{8}{10}=0.80
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

Example: An important normal email should not be incorrectly marked as spam.

</details>

## 🎣 B. Recall

### Definition

Recall measures how many actual positive cases are correctly identified by the model.

**Simple meaning:** Out of all actual positive cases, how many did the model find?

### Formula

$$
Recall = \frac{TP}{TP+FN}
$$

Where:

- TP = True Positive
- FN = False Negative

### Example

Suppose there are 10 actual spam emails.

The model correctly identifies 8 spam emails and misses 2.

$$
Recall = \frac{8}{8+2}
$$

$$
Recall = \frac{8}{10}=0.80
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

Example: In disease screening, failing to identify a person who has a disease can be dangerous.

</details>

## ⚖️ C. F1-score

### Definition

F1-score is the harmonic mean of Precision and Recall.

It combines both metrics into one score.

**Simple meaning:** F1-score helps us understand the balance between Precision and Recall.

### Formula

$$
F1 = 2 \times
\frac{Precision \times Recall}
{Precision + Recall}
$$

### Example 1: Precision = 60%, Recall = 100%

Arithmetic mean:

$$
\frac{60+100}{2}=80\%
$$

F1-score:

$$
F1 = 2 \times
\frac{60 \times 100}{60+100}
$$

$$
F1 = \frac{12000}{160}=75\%
$$

### Example 2: Precision = 80%, Recall = 80%

$$
F1 = 2 \times
\frac{80 \times 80}{80+80}
$$

$$
F1 = 80\%
$$

### Comparison

| Precision | Recall | Arithmetic Mean | F1-score |
|---:|---:|---:|---:|
| 80% | 80% | 80% | 80% |
| 60% | 100% | 80% | 75% |

**Important:** F1-score penalizes imbalance between Precision and Recall.

### Python syntax

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_actual, y_predicted)

print("F1-score:", f1)
```

<details>
<summary>🧠 Why harmonic mean instead of arithmetic mean?</summary>

The arithmetic mean can hide a low value.

For example:

- Precision = 60%
- Recall = 100%

The arithmetic mean is 80%, but F1-score is 75%.

The harmonic mean gives a lower score when one of the two metrics is much lower.

</details>

---

# 3. Multiclass Classification Example

## 🐶 Dog / Cat / Rabbit

### Definition

Multiclass classification means predicting one class from more than two possible classes.

Example:

- Dog
- Cat
- Rabbit

### Confusion Matrix

Rows are **Actual** values.

Columns are **Predicted** values.

| Actual / Predicted | Dog | Cat | Rabbit | Total |
|---|---:|---:|---:|---:|
| Dog | **25** | 5 | 10 | 40 |
| Cat | 0 | **30** | 4 | 34 |
| Rabbit | 4 | 10 | **20** | 34 |
| **Total** | **29** | **45** | **34** | **108** |

### Understand the matrix

- Diagonal values represent correct predictions.
- Other values represent incorrect predictions.

Example:

Dog row:

- 25 dogs predicted as Dog.
- 5 dogs predicted as Cat.
- 10 dogs predicted as Rabbit.

### Per-class Precision and Recall

For each class:

$$
Precision = \frac{Diagonal\ Value}{Column\ Total}
$$

$$
Recall = \frac{Diagonal\ Value}{Row\ Total}
$$

### Dog calculation

Precision:

$$
Precision = \frac{25}{29}=0.862
$$

Recall:

$$
Recall = \frac{25}{40}=0.625
$$

F1-score:

$$
F1 = 2 \times \frac{0.862 \times 0.625}{0.862+0.625}
$$

$$
F1 \approx 0.725
$$

### Cat calculation

Precision:

$$
Precision = \frac{30}{45}=0.667
$$

Recall:

$$
Recall = \frac{30}{34}=0.882
$$

F1-score:

$$
F1 \approx 0.762
$$

### Rabbit calculation

Precision:

$$
Precision = \frac{20}{34}=0.588
$$

Recall:

$$
Recall = \frac{20}{34}=0.588
$$

F1-score:

$$
F1 \approx 0.588
$$

### Complete results

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Dog | 0.862 | 0.625 | 0.725 |
| Cat | 0.667 | 0.882 | 0.762 |
| Rabbit | 0.588 | 0.588 | 0.588 |

<details>
<summary>🧮 Understand why Precision uses column totals and Recall uses row totals</summary>

**Precision:** Look at the predicted class column.

For Dog, the model predicted 29 samples as Dog. Of these, 25 were actually Dog.

$$
Precision_{Dog}=\frac{25}{29}
$$

**Recall:** Look at the actual class row.

There were 40 actual Dog samples. The model correctly identified 25.

$$
Recall_{Dog}=\frac{25}{40}
$$

</details>

---

# 4. Macro and Weighted Average

## ⚖️ A. Macro Average

### Definition

Macro Average calculates the metric for each class and takes the simple average.

Every class gets equal importance.

### Formula

$$
Macro\ Average =
\frac{M_1+M_2+\cdots+M_k}{k}
$$

Where:

- $M_i$ = Metric for class i.
- $k$ = Number of classes.

### Example: Macro Precision

$$
Macro\ Precision =
\frac{0.862+0.667+0.588}{3}
$$

$$
Macro\ Precision \approx 0.706
$$

## 🟧 B. Weighted Average

### Definition

Weighted Average calculates the metric for every class and weights it according to the number of actual samples in that class.

### Formula

$$
Weighted\ Average =
\frac{\sum_{i=1}^{k} n_i M_i}
{\sum_{i=1}^{k} n_i}
$$

Where:

- $n_i$ = Number of actual samples in class i.
- $M_i$ = Metric for class i.
- $k$ = Number of classes.

### Example: Weighted Precision

$$
=
\frac{
40(0.862)+34(0.667)+34(0.588)
}{108}
$$

$$
\approx 0.711
$$

### Comparison

| Average | How it works | Result (P / R / F1) |
|---|---|---|
| Macro | Equal importance for each class | ≈ 0.71 / 0.70 / 0.69 |
| Weighted | Weighted by actual class size | ≈ 0.71 / 0.69 / 0.69 |

*Values are rounded. Macro and weighted averages are different ways of summarizing per-class metrics.*

### Python syntax

```python
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

# Macro average
macro_precision = precision_score(
    y_true, y_pred, average="macro"
)

macro_recall = recall_score(
    y_true, y_pred, average="macro"
)

macro_f1 = f1_score(
    y_true, y_pred, average="macro"
)

# Weighted average
weighted_precision = precision_score(
    y_true, y_pred, average="weighted"
)

weighted_recall = recall_score(
    y_true, y_pred, average="weighted"
)

weighted_f1 = f1_score(
    y_true, y_pred, average="weighted"
)
```

### Get class counts using Pandas

```python
print(df["target"].value_counts())
```

<details>
<summary>💡 When should we use Macro and Weighted Average?</summary>

- **Macro:** Use when every class should have equal importance, especially when minority-class performance matters.
- **Weighted:** Use when you want the overall metric to reflect the actual number of samples in each class.

</details>

---

# 5. From Linear Equation to Probability

## 📈 Step 1 — Linear equation

A linear combination of input features produces a numerical score.

$$
z = \theta_0+\theta_1x_1+\theta_2x_2+\cdots+\theta_nx_n
$$

Where:

- $z$ = Model score.
- $\theta_0$ = Intercept.
- $\theta_1,\theta_2,\ldots$ = Model coefficients.
- $x_1,x_2,\ldots$ = Input features.

### Example

Suppose:

$$
z = -2 + 0.8x
$$

If $x=5$:

$$
z=-2+0.8(5)=2
$$

The score is 2.

**Problem:** The score can be any number. It is not necessarily between 0 and 1.

We need a function that converts it into a probability.

## Important mathematical clarification

The normal equation:

$$
\theta=(X^TX)^{-1}X^Ty
$$

is used in ordinary least-squares Linear Regression under suitable matrix conditions.

It is not the standard method for fitting Logistic Regression.

Logistic Regression generally learns coefficients by optimizing a classification loss function.

---

# 6. Sigmoid Function

## 📈 Definition

The Sigmoid function converts a numerical score into a probability between 0 and 1.

### Formula

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Where:

- $z$ = Model score.
- $e$ = Mathematical constant.
- $\sigma(z)$ = Predicted probability.

### Example

Suppose:

$$
z=2
$$

Then:

$$
\sigma(2)=\frac{1}{1+e^{-2}}
$$

$$
\sigma(2)\approx 0.881
$$

Probability = 88.1%.

### Understand the output

| Score (z) | Sigmoid output |
|---:|---:|
| -3 | 0.047 |
| -2 | 0.119 |
| -1 | 0.269 |
| 0 | 0.500 |
| 1 | 0.731 |
| 2 | 0.881 |
| 3 | 0.953 |

**Remember:** Sigmoid outputs values between 0 and 1.

---

# 7. Classification Threshold

## 🎚️ Definition

A classification threshold is a cutoff value used to convert predicted probabilities into class labels.

Default threshold = 0.5.

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
Prediction =
\begin{cases}
1 & P \geq Threshold \\
0 & P < Threshold
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

Suppose we reduce the threshold from 0.50 to 0.30.

More observations will be predicted as positive.

Usually:

- Recall increases or stays the same.
- False Positive Rate increases or stays the same.

The exact results depend on the dataset and predicted probabilities.

</details>

---

# 8. TPR, FPR and ROC Curve

## 🚦 A. Confusion Matrix

| Actual / Predicted | 1 (Positive) | 0 (Negative) |
|---|---|---|
| **1 (Positive)** | TP | FN |
| **0 (Negative)** | FP | TN |

## 🟢 B. TPR — True Positive Rate

### Definition

TPR measures the percentage of actual positive cases correctly identified by the model.

It is also called Recall.

### Formula

$$
TPR=\frac{TP}{TP+FN}
$$

**Simple meaning:** Out of all actual positive cases, how many did the model catch?

## 🔴 C. FPR — False Positive Rate

### Definition

FPR measures the percentage of actual negative cases incorrectly predicted as positive.

### Formula

$$
FPR=\frac{FP}{FP+TN}
$$

**Simple meaning:** Out of all actual negative cases, how many did the model wrongly mark as positive?

### Dry Run

Suppose:

- TP = 40
- FN = 10
- FP = 5
- TN = 45

TPR:

$$
TPR=\frac{40}{40+10}=0.80
$$

FPR:

$$
FPR=\frac{5}{5+45}=0.10
$$

Results:

- TPR = 80%.
- FPR = 10%.

## 📈 D. What is ROC Curve?

ROC stands for **Receiver Operating Characteristic**.

### Definition

A ROC Curve is a graph that plots:

- X-axis = False Positive Rate (FPR).
- Y-axis = True Positive Rate (TPR).

It shows the trade-off between identifying actual positives and generating false alarms at different thresholds.

### How is ROC Curve created?

1. The model predicts probabilities.
2. Choose a threshold.
3. Calculate TPR and FPR.
4. Change the threshold.
5. Calculate TPR and FPR again.
6. Plot all the points on a graph.

### Important observation

Lower threshold:

- More positive cases are detected.
- TPR generally increases.
- FPR generally increases.

Higher threshold:

- Fewer positive cases are detected.
- TPR generally decreases.
- FPR generally decreases.

---

# 9. Complete Python Code

## 💻 A. Reproduce the Multiclass Example

```python
# ==========================================
# MULTICLASS CLASSIFICATION METRICS
# Dog / Cat / Rabbit
# ==========================================

import numpy as np

from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

# ------------------------------------------
# STEP 1: Create confusion matrix
# ------------------------------------------

# Rows = Actual
# Columns = Predicted

cm = np.array([
    [25, 5, 10],
    [0, 30, 4],
    [4, 10, 20]
])

# Class names
labels = ["Dog", "Cat", "Rabbit"]

# ------------------------------------------
# STEP 2: Convert confusion matrix
# into actual and predicted arrays
# ------------------------------------------

y_true = []
y_pred = []

# Visit every matrix cell
for i in range(3):

    for j in range(3):

        # Add actual class i
        y_true += [i] * cm[i, j]

        # Add predicted class j
        y_pred += [j] * cm[i, j]

# ------------------------------------------
# STEP 3: Print classification report
# ------------------------------------------

print(
    classification_report(
        y_true,
        y_pred,
        labels=[0, 1, 2],
        target_names=labels,
        digits=3
    )
)

# ------------------------------------------
# STEP 4: Print confusion matrix
# ------------------------------------------

print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))
```

## 💻 B. Plot ROC Curve

```python
# ==========================================
# ROC CURVE USING LOGISTIC REGRESSION
# ==========================================

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    roc_curve,
    auc
)

from sklearn.model_selection import train_test_split

# ------------------------------------------
# STEP 1: Create sample dataset
# ------------------------------------------

X, y = make_classification(
    n_samples=1000,
    n_features=10,
    random_state=42
)

# ------------------------------------------
# STEP 2: Split the dataset
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    random_state=42
)

# ------------------------------------------
# STEP 3: Create Logistic Regression
# ------------------------------------------

model = LogisticRegression()

# ------------------------------------------
# STEP 4: Train the model
# ------------------------------------------

model.fit(X_train, y_train)

# ------------------------------------------
# STEP 5: Get positive class probabilities
# ------------------------------------------

probs = model.predict_proba(X_test)[:, 1]

# ------------------------------------------
# STEP 6: Calculate ROC values
# ------------------------------------------

fpr, tpr, thresholds = roc_curve(
    y_test,
    probs
)

# ------------------------------------------
# STEP 7: Calculate AUC
# ------------------------------------------

roc_auc = auc(fpr, tpr)

print("AUC:", roc_auc)

# ------------------------------------------
# STEP 8: Plot ROC Curve
# ------------------------------------------

plt.plot(
    fpr,
    tpr,
    label=f"ROC Curve (AUC = {roc_auc:.2f})"
)

# Random classifier reference line
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

```bash
pip install numpy pandas scikit-learn matplotlib
```

---

# 10. Complete Dry Run

## 🧮 Multiclass example

Given:

| Actual / Predicted | Dog | Cat | Rabbit | Total |
|---|---:|---:|---:|---:|
| Dog | 25 | 5 | 10 | 40 |
| Cat | 0 | 30 | 4 | 34 |
| Rabbit | 4 | 10 | 20 | 34 |
| Total | 29 | 45 | 34 | 108 |

Dog:

- Precision = 25 / 29 = 0.862.
- Recall = 25 / 40 = 0.625.
- F1 = 0.725.

Cat:

- Precision = 30 / 45 = 0.667.
- Recall = 30 / 34 = 0.882.
- F1 = 0.762.

Rabbit:

- Precision = 20 / 34 = 0.588.
- Recall = 20 / 34 = 0.588.
- F1 = 0.588.

## 🚦 Binary example

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
| F1 | 2PR / (P + R) | Balance of Precision and Recall |
| TPR | TP / (TP + FN) | True Positive Rate |
| FPR | FP / (FP + TN) | False alarm rate |
| ROC | TPR vs FPR | Classification performance across thresholds |
| AUC | Area under ROC | Positive-negative ranking ability |

### Easy memory trick

- 🎯 Precision → How many predicted positives are correct?
- 🎣 Recall → How many actual positives did we catch?
- ⚖️ F1 → Balance between Precision and Recall.
- 🟢 TPR → Same as Recall.
- 🔴 FPR → How many false alarms?
- 🚦 ROC → TPR against FPR.
- 📈 AUC → Area under ROC.

---

# 12. Interview Questions and Answers

<details>
<summary>Q1. What is Precision?</summary>

Precision measures how many predicted positive cases are actually positive.

</details>

<details>
<summary>Q2. What is Recall?</summary>

Recall measures how many actual positive cases the model correctly identifies.

</details>

<details>
<summary>Q3. What is F1-score?</summary>

F1-score is the harmonic mean of Precision and Recall.

</details>

<details>
<summary>Q4. Why do we use harmonic mean for F1?</summary>

It penalizes a large imbalance between Precision and Recall.

</details>

<details>
<summary>Q5. What is the difference between Precision and Recall?</summary>

Precision focuses on the correctness of positive predictions. Recall focuses on finding actual positive cases.

</details>

<details>
<summary>Q6. What is Multiclass Classification?</summary>

A classification problem involving more than two possible classes.

</details>

<details>
<summary>Q7. What is Macro Average?</summary>

It calculates the metric for every class and takes the simple average.

</details>

<details>
<summary>Q8. What is Weighted Average?</summary>

It calculates the metric for every class and takes an average weighted by the number of actual samples in each class.

</details>

<details>
<summary>Q9. What is the Sigmoid function?</summary>

A mathematical function that converts a score into a probability between 0 and 1.

</details>

<details>
<summary>Q10. What is a classification threshold?</summary>

A cutoff probability used to convert model probabilities into predicted classes.

</details>

<details>
<summary>Q11. What is TPR?</summary>

True Positive Rate. It is the same as Recall.

</details>

<details>
<summary>Q12. What is FPR?</summary>

False Positive Rate. It measures the proportion of actual negative cases wrongly predicted as positive.

</details>

<details>
<summary>Q13. What is ROC Curve?</summary>

A graph plotting True Positive Rate against False Positive Rate at different thresholds.

</details>

<details>
<summary>Q14. What happens when the threshold decreases?</summary>

The model generally predicts more positive cases, increasing or maintaining both TPR and FPR.

</details>

<details>
<summary>Q15. What is AUC?</summary>

AUC is the area under the ROC curve. It summarizes the model's ability to rank positive samples above negative samples.

</details>

---

# 13. Final Summary

## 🎓 What did we learn?

| Chapter | Topic | Main concept |
|---|---|---|
| 1 | Precision | Correct positive predictions |
| 2 | Recall | Identify actual positives |
| 3 | F1-score | Balance of Precision and Recall |
| 4 | Multiclass Metrics | Evaluate multiple classes |
| 5 | Macro Average | Equal class importance |
| 6 | Weighted Average | Class-size-based importance |
| 7 | Linear Equation | Calculate model score |
| 8 | Sigmoid | Convert score into probability |
| 9 | Threshold | Convert probability into class |
| 10 | TPR | True Positive Rate |
| 11 | FPR | False Positive Rate |
| 12 | ROC Curve | TPR vs FPR graph |
| 13 | AUC | Area under ROC |

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
- [ ] Understand ROC Curve.
- [ ] Run the Python programs.
- [ ] Practise interview questions.

**Final learning point:** Classification metrics help us understand different types of model performance. The best metric depends on the problem, the class distribution and the cost of different prediction errors.

⭐ Keep practising these formulas and Python examples until you can explain each metric without looking at your notes.