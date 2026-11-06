# Chapter — Classification Evaluation Metrics

## 1. What are Classification Evaluation Metrics?

### Definition

Classification Evaluation Metrics are techniques used to measure how well a classification Machine Learning model predicts the correct classes.

**Simple meaning:** They help us check how many predictions are correct and how many are wrong.

### Real-World Example

Imagine Gmail has a Spam Detection Machine Learning model.

It predicts whether an email is:

- `1` → Spam
- `0` → Not Spam

We compare the model's predictions with the actual email categories to evaluate its performance.

## 2. Confusion Matrix

### Definition

A Confusion Matrix is a table that compares actual values with predicted values.

It helps us identify four results:

- TP — True Positive
- TN — True Negative
- FP — False Positive
- FN — False Negative

### Syntax

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_actual, y_predicted)

print(cm)
```

### Example

```python
# Actual email categories
y_actual = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Model predicted categories
y_predicted = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]

# Create confusion matrix
cm = confusion_matrix(y_actual, y_predicted)

print(cm)
```

### Output

```text
[[4 1]
 [2 3]]
```

### Understand the Four Terms

| Term | Meaning | Example |
|---|---|---|
| TP | Actual 1, Predicted 1 | Spam correctly detected |
| TN | Actual 0, Predicted 0 | Normal email correctly detected |
| FP | Actual 0, Predicted 1 | Normal email wrongly marked as spam |
| FN | Actual 1, Predicted 0 | Spam email wrongly marked as normal |

**Remember:**

- True = Correct prediction.
- False = Wrong prediction.
- Positive = Class 1.
- Negative = Class 0.

## 3. Accuracy

### Definition

Accuracy measures the percentage of total predictions that are correct.

**Simple meaning:** Out of all predictions, how many did the model get right?

### Formula

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

### Syntax

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_actual, y_predicted)

print(accuracy)
```

### Example

Our values:

- TP = 3
- TN = 4
- FP = 1
- FN = 2

### Dry Run

$$
Accuracy = \frac{3 + 4}{3 + 4 + 1 + 2}
$$

$$
Accuracy = \frac{7}{10} = 0.70
$$

$$
Accuracy = 70\%
$$

**Result:** The model correctly predicted 70% of emails.

## 4. Precision

### Definition

Precision measures how many predicted positive cases are actually positive.

**Simple meaning:** The model predicted 4 emails as spam. How many were really spam?

### Formula

$$
Precision = \frac{TP}{TP + FP}
$$

### Syntax

```python
from sklearn.metrics import precision_score

precision = precision_score(y_actual, y_predicted)

print(precision)
```

### Dry Run

$$
Precision = \frac{3}{3 + 1}
$$

$$
Precision = \frac{3}{4} = 0.75
$$

$$
Precision = 75\%
$$

**Result:** Out of 4 emails predicted as spam, 3 were actually spam.

## 5. Recall

### Definition

Recall measures how many actual positive cases the model correctly identifies.

**Simple meaning:** There are 5 actual spam emails. How many did the model find?

### Formula

$$
Recall = \frac{TP}{TP + FN}
$$

### Syntax

```python
from sklearn.metrics import recall_score

recall = recall_score(y_actual, y_predicted)

print(recall)
```

### Dry Run

$$
Recall = \frac{3}{3 + 2}
$$

$$
Recall = \frac{3}{5} = 0.60
$$

$$
Recall = 60\%
$$

**Result:** The model correctly identified 3 out of 5 spam emails.

## 6. F1-Score

### Definition

F1-score is the harmonic mean of Precision and Recall.

It combines both metrics into one score.

**Simple meaning:** It helps us understand the balance between Precision and Recall.

### Formula

$$
F1 = 2 \times
\frac{Precision \times Recall}
{Precision + Recall}
$$

### Syntax

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_actual, y_predicted)

print(f1)
```

### Dry Run

Our values:

- Precision = 0.75
- Recall = 0.60

$$
F1 = 2 \times
\frac{0.75 \times 0.60}
{0.75 + 0.60}
$$

$$
F1 = 2 \times \frac{0.45}{1.35}
$$

$$
F1 = 0.667 = 66.7\%
$$

**Result:** F1-score = 66.7%.

## 7. ROC Curve

### Definition

ROC stands for Receiver Operating Characteristic.

A ROC Curve is a graph that shows how a classification model performs at different classification thresholds.

It compares:

- TPR (True Positive Rate) — Recall.
- FPR (False Positive Rate) — How many actual negative cases are wrongly predicted as positive.

### Formulas

$$
TPR = \frac{TP}{TP + FN}
$$

$$
FPR = \frac{FP}{FP + TN}
$$

### Syntax

```python
from sklearn.metrics import roc_curve

# Probability of class 1 (Spam)
y_probability = model.predict_proba(X_test)[:, 1]

# Calculate ROC values
fpr, tpr, thresholds = roc_curve(y_test, y_probability)
```

### Simple Example

Suppose a model predicts these spam probabilities:

| Email | Actual | Spam Probability |
|---|---:|---:|
| A | 1 | 0.95 |
| B | 1 | 0.80 |
| C | 0 | 0.30 |
| D | 0 | 0.10 |

At a threshold of `0.50`:

- Probability greater than or equal to 0.50 → Spam (1).
- Probability below 0.50 → Not Spam (0).

Changing the threshold changes the predictions, which changes TPR and FPR.

**Important:** ROC Curve is useful for understanding the trade-off between detecting positive cases and incorrectly marking negative cases as positive.

## 8. AUC

### Definition

AUC stands for Area Under the Curve.

It measures the overall ability of a classification model to distinguish between positive and negative classes using the ROC curve.

### General Interpretation

| AUC Value | Meaning |
|---|---|
| 1.0 | Perfect separation |
| 0.9–1.0 | Excellent |
| 0.8–0.9 | Good |
| 0.7–0.8 | Fair |
| 0.5 | No better than random ranking |
| Below 0.5 | Worse than random ranking |

These are common guidelines, not strict universal rules.

### Syntax

```python
from sklearn.metrics import roc_auc_score

# Use predicted probabilities, not class labels
auc = roc_auc_score(y_test, y_probability)

print("AUC:", auc)
```

## 9. Complete Dry Run — All Metrics

### Our Confusion Matrix

```text
[[4 1]
 [2 3]]
```

| Metric | Formula | Result |
|---|---|---:|
| Accuracy | (TP + TN) / Total | 70% |
| Precision | TP / (TP + FP) | 75% |
| Recall | TP / (TP + FN) | 60% |
| F1-score | 2 × (P × R) / (P + R) | 66.7% |

Where:

- TP = 3
- TN = 4
- FP = 1
- FN = 2
- Total = 10
- P = Precision
- R = Recall

## 10. Final Summary

| Metric | What does it measure? |
|---|---|
| Confusion Matrix | Actual vs predicted results |
| Accuracy | Overall correct predictions |
| Precision | Correctness of predicted positives |
| Recall | Identification of actual positives |
| F1-score | Balance between Precision and Recall |
| ROC Curve | TPR vs FPR at different thresholds |
| AUC | Overall ability to distinguish classes |

### Easy Memory Trick

- Accuracy → Overall correct predictions.
- Precision → How many predicted positives are correct?
- Recall → How many actual positives were found?
- F1-score → Balance between Precision and Recall.
- ROC → Graph of TPR against FPR.
- AUC → Area under the ROC curve.

### Important Interview Point

Accuracy is not always enough.

For example:

In disease detection, missing a patient who actually has a disease can be dangerous. Therefore, Recall may be especially important.

In spam detection, incorrectly marking an important normal email as spam can be a problem. Therefore, Precision may be especially important.

The best metric depends on the real-world problem.

## 11. Interview Questions and Answers

**Q1. What are Classification Evaluation Metrics?**

They are measures used to evaluate how well a classification model predicts the correct classes.

**Q2. What is a Confusion Matrix?**

A table that compares actual and predicted classes using TP, TN, FP and FN.

**Q3. What is True Positive?**

The actual class is positive, and the model also predicts positive.

**Q4. What is True Negative?**

The actual class is negative, and the model also predicts negative.

**Q5. What is False Positive?**

The actual class is negative, but the model predicts positive.

**Q6. What is False Negative?**

The actual class is positive, but the model predicts negative.

**Q7. What is Accuracy?**

The percentage of all predictions that are correct.

**Q8. What is Precision?**

The percentage of predicted positive cases that are actually positive.

**Q9. What is Recall?**

The percentage of actual positive cases correctly identified by the model.

**Q10. What is F1-score?**

The harmonic mean of Precision and Recall.

**Q11. What is ROC Curve?**

A graph that plots True Positive Rate against False Positive Rate at different thresholds.

**Q12. What is AUC?**

AUC is the area under the ROC curve. It measures how well the model separates positive and negative classes.

**Q13. What is the difference between Precision and Recall?**

Precision focuses on the correctness of positive predictions. Recall focuses on finding actual positive cases.

**Q14. When should we use F1-score?**

When we want to balance Precision and Recall, especially when the classes are imbalanced.

**Q15. Can Accuracy be misleading?**

Yes. In an imbalanced dataset, a model can achieve high accuracy by predicting the majority class while failing to identify the minority class.