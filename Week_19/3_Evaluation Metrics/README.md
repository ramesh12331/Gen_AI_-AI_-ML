# Chapter — Classification Evaluation Metrics

Based on your class screenshots, let's learn Confusion Matrix, Accuracy, Precision, Recall, F1-score, ROC and AUC using one simple Spam Detection example.

We will use:

- `1` = Spam
- `0` = Not Spam

## 1. Confusion Matrix

A Confusion Matrix compares the actual results with the predicted results.

Confusion Matrix structure

| Actual / Predicted | 1 (Spam) | 0 (Not Spam) |
| ------------------ | -------- | ------------ |
| 1 (Spam)           | TP       | FN           |
| 0 (Not Spam)       | FP       | TN           |

TP — True Positive

Actual Spam, predicted Spam.

FN — False Negative

Actual Spam, predicted Not Spam.

FP — False Positive

Actual Not Spam, predicted Spam.

TN — True Negative

Actual Not Spam, predicted Not Spam.

Easy trick to remember:

- True = Prediction is correct.
- False = Prediction is incorrect.
- Positive = Predicted class is 1.
- Negative = Predicted class is 0.

## 2. Simple Python code with comments

First install the required libraries:

```
pip install pandas scikit-learn matplotlib seaborn
```

### Complete beginner-friendly code

```
# ==========================================# CLASSIFICATION EVALUATION METRICS# Spam Detection Example# ==========================================# Import required librariesfrom sklearn.metrics import (    confusion_matrix,    accuracy_score,    precision_score,    recall_score,    f1_score,    classification_report)import seaborn as snsimport matplotlib.pyplot as plt# ------------------------------------------# STEP 1: Actual values# ------------------------------------------# 1 = Spam# 0 = Not Spamy_actual = [    1, 1, 1, 1, 1,    0, 0, 0, 0, 0]# ------------------------------------------# STEP 2: Predicted values# ------------------------------------------# These are predictions made by our ML modely_predicted = [    1, 1, 0, 1, 0,    0, 1, 0, 0, 0]# ------------------------------------------# STEP 3: Create Confusion Matrix# ------------------------------------------cm = confusion_matrix(y_actual, y_predicted)print("Confusion Matrix:")print(cm)# ------------------------------------------# STEP 4: Calculate TP, TN, FP, FN# ------------------------------------------tn, fp, fn, tp = cm.ravel()
```

## 3. Dry run — Understand the output

Our input:

```
y_actual =    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]y_predicted = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
```

Compare each actual value with its prediction:

| No. | Actual | Predicted | Result |
| --- | ------ | --------- | ------ |
| 1   | 1      | 1         | TP     |
| 2   | 1      | 1         | TP     |
| 3   | 1      | 0         | FN     |
| 4   | 1      | 1         | TP     |
| 5   | 1      | 0         | FN     |
| 6   | 0      | 0         | TN     |
| 7   | 0      | 1         | FP     |
| 8   | 0      | 0         | TN     |
| 9   | 0      | 0         | TN     |
| 10  | 0      | 0         | TN     |

Therefore:

- TP = 3
- FN = 2
- FP = 1
- TN = 4

Confusion Matrix:

## Confusion Matrix

Rows = Actual · Columns = Predicted

0

1

Actual 0

# 4

TN

# 1

FP

Actual 1

# 2

FN

# 3

TP

## 4. Accuracy

Meaning: How many total predictions are correct?

Formula:

$$\
Accuracy = \frac\
$$

Substitute our values:

$$\
Accuracy = \frac710\
$$

$$\
\= \frac710 = 0.70\
$$

Accuracy = 70%

## 5. Precision

Meaning: Out of all predicted positive cases, how many are actually positive?

Formula:

$$\
Precision = \frac\
$$

Substitute:

$$\
Precision = \frac34\
\= 0.75\
$$

Precision = 75%

Simple example: The model predicted 4 emails as spam. Only 3 were actually spam.

## 6. Recall

Meaning: Out of all actual positive cases, how many did the model correctly identify?

Formula:

$$\
Recall = \frac\
$$

Substitute:

$$\
Recall = \frac35\
\= 0.60\
$$

Recall = 60%

Simple example: There were 5 actual spam emails. The model correctly identified only 3.

## 7. F1-score

Meaning: Combines Precision and Recall into one score using their harmonic mean.

Formula:

$$\
F1 = 2 \times\
\frac