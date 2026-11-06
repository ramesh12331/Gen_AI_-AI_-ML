# 📊 Chapter — Classification Evaluation Metrics

## 🎯 1. What are Classification Evaluation Metrics?

### 📖 Definition

Classification Evaluation Metrics are measurements used to check how well a Machine Learning classification model predicts the correct classes.

**Simple meaning:** They help us understand how many predictions are correct and what types of mistakes the model makes.

### 💡 Real-world example

Imagine a Machine Learning model that predicts whether a candidate will pass or fail an interview.

- `1` → Pass
- `0` → Fail

We compare the actual results with the model's predictions.

### Why do we need evaluation metrics?

Suppose two models have 90% accuracy. Are both models equally good?

Not necessarily!

One model may identify positive cases correctly, while another may miss many positive cases.

That is why we use different evaluation metrics.

---

## 📊 2. Accuracy

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

print("Accuracy:", accuracy)
```

### 🧮 Dry Run

Assume:

- TP = 3
- TN = 4
- FP = 1
- FN = 2

$$
Accuracy = \frac{3+4}{3+4+1+2}
$$

$$
Accuracy = \frac{7}{10} = 0.70
$$

$$
Accuracy = 70\%
$$

**Result:** The model correctly predicted 70% of all cases.

### ⚠️ Limitation of Accuracy

Suppose a dataset contains:

- 900 normal emails
- 100 spam emails

A model predicts every email as normal.

Its accuracy is:

$$
Accuracy = \frac{900}{1000} = 90\%
$$

But the model identifies zero spam emails!

**Conclusion:** Accuracy can be misleading when the dataset is imbalanced.

---

## 🧩 3. Confusion Matrix

### Definition

A Confusion Matrix is a table that compares actual classes with predicted classes.

It helps us identify four types of predictions.

### Structure

For binary classification:

| Actual / Predicted | 1 (Positive) | 0 (Negative) |
|---|---|---|
| 1 (Positive) | TP | FN |
| 0 (Negative) | FP | TN |

### Understand the four terms

| Term | Meaning | Example |
|---|---|---|
| TP | Actual positive, predicted positive | Spam correctly detected |
| TN | Actual negative, predicted negative | Normal email correctly identified |
| FP | Actual negative, predicted positive | Normal email marked as spam |
| FN | Actual positive, predicted negative | Spam email marked as normal |

### 💡 Easy memory trick

- True = Correct prediction.
- False = Incorrect prediction.
- Positive = Positive class (1).
- Negative = Negative class (0).

### Syntax

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_actual, y_predicted)

print(cm)
```

### Example

```python
from sklearn.metrics import confusion_matrix

# Actual values
y_actual = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Predicted values
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

### 🧮 Dry Run

| No. | Actual | Predicted | Result |
|---:|---:|---:|---|
| 1 | 1 | 1 | TP |
| 2 | 1 | 1 | TP |
| 3 | 1 | 0 | FN |
| 4 | 1 | 1 | TP |
| 5 | 1 | 0 | FN |
| 6 | 0 | 0 | TN |
| 7 | 0 | 1 | FP |
| 8 | 0 | 0 | TN |
| 9 | 0 | 0 | TN |
| 10 | 0 | 0 | TN |

Therefore:

- TP = 3
- TN = 4
- FP = 1
- FN = 2

**Important:** Scikit-learn places rows in actual-class order and columns in predicted-class order. For labels `[0, 1]`, the matrix is `[[TN, FP], [FN, TP]]`.

---

## 🔍 4. Precision

### Definition

Precision measures how many predicted positive cases are actually positive.

**Simple meaning:** The model predicted four emails as spam. How many were really spam?

### Formula

$$
Precision = \frac{TP}{TP + FP}
$$

### Syntax

```python
from sklearn.metrics import precision_score

precision = precision_score(y_actual, y_predicted)

print("Precision:", precision)
```

### 🧮 Dry Run

TP = 3, FP = 1

$$
Precision = \frac{3}{3+1}
$$

$$
Precision = \frac{3}{4} = 0.75
$$

$$
Precision = 75\%
$$

**Result:** Out of four predicted spam emails, three were actually spam.

### When is Precision important?

When false positive predictions are costly.

Example: An important normal email should not be incorrectly moved into the spam folder.

---

## 📢 5. Recall

### Definition

Recall measures how many actual positive cases are correctly identified.

**Simple meaning:** There are five actual spam emails. How many did the model find?

### Formula

$$
Recall = \frac{TP}{TP + FN}
$$

### Syntax

```python
from sklearn.metrics import recall_score

recall = recall_score(y_actual, y_predicted)

print("Recall:", recall)
```

### 🧮 Dry Run

TP = 3, FN = 2

$$
Recall = \frac{3}{3+2}
$$

$$
Recall = \frac{3}{5} = 0.60
$$

$$
Recall = 60\%
$$

**Result:** The model correctly identified three out of five actual spam emails.

### When is Recall important?

When missing a positive case is costly.

Example: In disease screening, failing to identify a person who has a disease can be dangerous.

---

## ⚖️ 6. F1-score

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

Another formula using the confusion matrix:

$$
F1 = \frac{2TP}{2TP + FP + FN}
$$

### Syntax

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_actual, y_predicted)

print("F1-score:", f1)
```

### 🧮 Dry Run

Precision = 0.75

Recall = 0.60

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

**Result:** F1-score is approximately 66.7%.

### Why harmonic mean?

The harmonic mean gives a lower score when either Precision or Recall is low. It rewards a balance between the two.

---

## 📈 7. ROC Curve

### Definition

ROC stands for **Receiver Operating Characteristic**.

A ROC Curve is a graph that shows model performance at different classification thresholds.

It compares:

- TPR — True Positive Rate (Recall).
- FPR — False Positive Rate.

### Formulas

True Positive Rate:

$$
TPR = \frac{TP}{TP+FN}
$$

False Positive Rate:

$$
FPR = \frac{FP}{FP+TN}
$$

### 💡 Understand classification threshold

Suppose the model predicts spam probabilities:

| Email | Actual | Spam Probability |
|---|---:|---:|
| A | 1 | 0.95 |
| B | 1 | 0.80 |
| C | 0 | 0.30 |
| D | 0 | 0.10 |

At threshold `0.50`:

- Probability >= 0.50 → Spam (1).
- Probability < 0.50 → Not Spam (0).

If we change the threshold, the predicted classes can change. Therefore, TPR and FPR also change.

### Syntax

```python
from sklearn.metrics import roc_curve

# Get probability of positive class
y_probability = model.predict_proba(X_test)[:, 1]

# Calculate ROC values
fpr, tpr, thresholds = roc_curve(
    y_test,
    y_probability
)
```

### Plot ROC Curve

```python
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

# Calculate FPR and TPR
fpr, tpr, thresholds = roc_curve(
    y_test,
    y_probability
)

# Draw ROC curve
plt.plot(fpr, tpr, label="ROC Curve")

# Random classifier reference line
plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")

plt.legend()
plt.show()
```

**Remember:** ROC shows the trade-off between identifying positives and incorrectly predicting positives.

---

## 📐 8. AUC

### Definition

AUC stands for **Area Under the Curve**.

It measures how well a model ranks positive cases above negative cases using the ROC curve.

### General interpretation

| AUC | Interpretation |
|---:|---|
| 1.0 | Perfect ranking |
| 0.9–1.0 | Excellent |
| 0.8–0.9 | Good |
| 0.7–0.8 | Fair |
| 0.5 | Random-ranking level |
| Below 0.5 | Worse than random ranking |

These are common guidelines, not strict universal rules.

### Syntax

```python
from sklearn.metrics import roc_auc_score

# Use predicted probabilities
auc = roc_auc_score(y_test, y_probability)

print("AUC:", auc)
```

**Important:** Use predicted probabilities or decision scores, not just predicted class labels, for ROC-AUC.

---

## 🧮 9. Complete Python Example

```python
# ==========================================
# CLASSIFICATION EVALUATION METRICS
# Spam Detection Example
# ==========================================

# Import evaluation metrics
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# ------------------------------------------
# STEP 1: Actual values
# ------------------------------------------

# 1 = Spam
# 0 = Not Spam

y_actual = [
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 0
]

# ------------------------------------------
# STEP 2: Predicted values
# ------------------------------------------

y_predicted = [
    1, 1, 0, 1, 0,
    0, 1, 0, 0, 0
]

# ------------------------------------------
# STEP 3: Confusion Matrix
# ------------------------------------------

cm = confusion_matrix(y_actual, y_predicted)

print("Confusion Matrix:")
print(cm)

# Extract TN, FP, FN, TP
tn, fp, fn, tp = cm.ravel()

print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)

# ------------------------------------------
# STEP 4: Accuracy
# ------------------------------------------

accuracy = accuracy_score(y_actual, y_predicted)

# ------------------------------------------
# STEP 5: Precision
# ------------------------------------------

precision = precision_score(y_actual, y_predicted)

# ------------------------------------------
# STEP 6: Recall
# ------------------------------------------

recall = recall_score(y_actual, y_predicted)

# ------------------------------------------
# STEP 7: F1-score
# ------------------------------------------

f1 = f1_score(y_actual, y_predicted)

# ------------------------------------------
# STEP 8: Display all metrics
# ------------------------------------------

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# ------------------------------------------
# STEP 9: Classification Report
# ------------------------------------------

print(classification_report(y_actual, y_predicted))
```

### Expected output

```text
Confusion Matrix:
[[4 1]
 [2 3]]

TN: 4
FP: 1
FN: 2
TP: 3

Accuracy: 0.7
Precision: 0.75
Recall: 0.6
F1-score: 0.6667
```

---

## 🧩 10. Multiclass Classification Metrics

### Definition

Multiclass classification means predicting one class from more than two possible classes.

### Example from the class notes

Consider flower classification:

- 0 → Setosa
- 1 → Versicolor
- 2 → Virginica

Unlike binary classification, there are three possible classes.

### How do we calculate metrics?

We calculate Precision and Recall for each class by treating that class as positive and all other classes as negative.

For example:

- Setosa vs all other flowers.
- Versicolor vs all other flowers.
- Virginica vs all other flowers.

### Three averaging methods

**1. Macro Average**

Calculate the metric for every class and take the simple average.

$$
Macro\ Average =
\frac{M_1+M_2+\cdots+M_k}{k}
$$

**2. Weighted Average**

Calculate the metric for every class and take the average weighted by the number of actual samples in each class.

$$
Weighted\ Average =
\frac{\sum_{i=1}^{k} n_i M_i}
{\sum_{i=1}^{k} n_i}
$$

Where:

- $M_i$ = Metric for class i.
- $n_i$ = Number of actual samples in class i.
- $k$ = Number of classes.

**3. Micro Average**

Combine the TP, FP and FN counts across all classes, then calculate the metric.

For single-label multiclass classification, micro Precision, Recall and F1 are equal to accuracy.

### Syntax

```python
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

# Macro average
print(precision_score(y_actual, y_predicted,
                      average="macro"))

# Micro average
print(recall_score(y_actual, y_predicted,
                   average="micro"))

# Weighted average
print(f1_score(y_actual, y_predicted,
               average="weighted"))
```

### Understand the difference

| Method | Meaning |
|---|---|
| Macro | Every class gets equal importance |
| Micro | Combines all class predictions |
| Weighted | Gives importance according to class size |

**Important:** The PDF's multiclass notes introduce class-wise precision and weighted precision. These averaging methods help extend that idea.

---

## 📋 11. Complete Dry Run — All Metrics

Our confusion matrix:

```text
[[4 1]
 [2 3]]
```

Values:

- TP = 3
- TN = 4
- FP = 1
- FN = 2
- Total = 10

| Metric | Formula | Result |
|---|---|---:|
| Accuracy | (TP + TN) / Total | 70% |
| Precision | TP / (TP + FP) | 75% |
| Recall | TP / (TP + FN) | 60% |
| F1-score | 2 × (P × R) / (P + R) | 66.7% |

### 🧠 Easy memory trick

- Accuracy → Overall correct predictions.
- Precision → How many predicted positives are correct?
- Recall → How many actual positives were found?
- F1-score → Balance between Precision and Recall.
- ROC → TPR against FPR.
- AUC → Area under ROC curve.

---

## 🎤 12. Interview Questions and Answers

**Q1. What are Classification Evaluation Metrics?**

They measure how well a classification model predicts the correct classes.

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

The area under the ROC curve. It measures how well the model ranks positive cases above negative cases.

**Q13. What is the difference between Precision and Recall?**

Precision focuses on the correctness of positive predictions. Recall focuses on finding actual positive cases.

**Q14. When should we use F1-score?**

When we want to balance Precision and Recall, especially when classes are imbalanced.

**Q15. Can Accuracy be misleading?**

Yes. A model can achieve high accuracy by predicting the majority class while failing to identify the minority class.

**Q16. What is Macro Average?**

It calculates a metric for each class and takes their unweighted average.

**Q17. What is Weighted Average?**

It calculates a metric for each class and takes an average weighted by the number of actual samples in each class.

**Q18. What is Micro Average?**

It combines classification counts across classes before calculating the metric.

---

## ✅ 13. Final Summary

| Topic | Purpose |
|---|---|
| Confusion Matrix | Compare actual vs predicted results |
| Accuracy | Measure overall correct predictions |
| Precision | Measure correctness of positive predictions |
| Recall | Measure identification of actual positives |
| F1-score | Balance Precision and Recall |
| ROC Curve | Compare TPR and FPR at different thresholds |
| AUC | Measure positive-vs-negative ranking ability |
| Macro Average | Equal importance to each class |
| Micro Average | Combine all class counts |
| Weighted Average | Consider class sizes |

### 🎯 Final Learning Point

Accuracy alone is not always enough.

- In disease detection, Recall may be especially important because missing a positive patient can be dangerous.
- In spam detection, Precision may be especially important because normal emails should not be wrongly marked as spam.
- When both Precision and Recall matter, F1-score can be useful.

**The best evaluation metric depends on the real-world problem.**