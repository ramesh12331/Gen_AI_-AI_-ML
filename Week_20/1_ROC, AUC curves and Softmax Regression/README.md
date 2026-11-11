# 📊 Machine Learning Class Notes — ROC, AUC & Softmax Regression

**Beginner-Friendly Notes | Based on classroom screenshots | Class date: 10-11-2026**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine_Learning-F7931E?logo=scikitlearn&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Classification-blue)
![Level](https://img.shields.io/badge/Level-Beginner-green)

> 💡 These notes follow the topics, terminology, examples and sequence visible in the supplied classroom material. Expand the sections for extra explanations.

---

## 🧭 Table of Contents

- [Part 1 — ROC Curve and AUC](#part-1--roc-curve-and-auc)
  - [1. ROC and AUC Introduction](#1-roc-and-auc-introduction)
  - [2. Threshold](#2-threshold)
  - [3. ROC Components](#3-roc-components)
  - [4. TPR](#4-tpr--true-positive-rate)
  - [5. FPR](#5-fpr--false-positive-rate)
  - [6. Threshold Impact](#6-threshold-impact)
  - [7. ROC Curve](#7-roc-curve)
  - [8. AUC](#8-auc--area-under-the-curve)
- [Part 2 — Softmax Regression](#part-2--softmax-regression)
  - [9. Introduction](#9-introduction-to-softmax-regression)
  - [10. Softmax Function](#10-softmax-function)
  - [11. Linear Scores and Class Weights](#11-linear-scores-and-class-weights)
  - [12. Softmax Calculation](#12-step-by-step-softmax-calculation)
  - [13. Multiclass Student Example](#13-multi-class-classification-student-example)
  - [14. One-Hot Encoding](#14-training-data-and-one-hot-encoding)
  - [15. Final Prediction and Argmax](#15-final-prediction-using-softmax)
  - [16. Loss Function](#16-loss-function)
  - [17. Binary Cross-Entropy](#17-binary-cross-entropy-loss-log-loss)
  - [18. Categorical Cross-Entropy](#18-categorical-cross-entropy-loss)
  - [19. Gradient Descent](#19-gradient-descent)
  - [20. Scikit-learn and Deep Learning](#20-scikit-learn-and-deep-learning)
  - [21. Complete Workflow](#21-complete-softmax-workflow)
- [Quick Revision](#quick-revision)
- [Interview Questions](#interview-questions)
- [Practice Questions](#practice-questions)

---

# PART 1 — ROC CURVE AND AUC

## 1. ROC and AUC Introduction

- **ROC** → Receiver Operating Characteristic
- **AUC** → Area Under the Curve

ROC and AUC are evaluation techniques used to measure the performance of a classification model.

---

## 2. Threshold

### 📖 Definition

A **threshold** is a cutoff value used to convert predicted probabilities into class labels (`0` or `1`).

### Faculty's example

Threshold = `0.5`

- If probability ≥ 0.5 → Class 1
- If probability < 0.5 → Class 0

### Example

| Predicted Probability | Threshold | Prediction |
|---:|---:|---:|
| 0.8 | 0.5 | 1 |
| 0.9 | 0.5 | 1 |
| 0.3 | 0.5 | 0 |
| 0.2 | 0.5 | 0 |

> **Important:** Changing the threshold changes the classification results.

---

## 3. ROC Components

ROC is based on two important metrics:

1. **TPR** — True Positive Rate
2. **FPR** — False Positive Rate

---

## 4. TPR — True Positive Rate

### 🟢 Benefit

**Definition:** TPR measures how many actual positive cases are correctly predicted as positive.

### Formula

$$
TPR = \frac{TP}{TP + FN}
$$

Where:

- `TP` = True Positive
- `FN` = False Negative

### Example — Email Spam Classifier

Consider this confusion matrix:

| Actual / Predicted | Spam (1) | Not Spam (0) |
|---|---:|---:|
| Spam (1) | TP = 80 | FN = 20 |
| Not Spam (0) | FP = 20 | TN = 80 |

### Calculation

$$
TPR = \frac{80}{80 + 20}
$$

$$
TPR = \frac{80}{100} = 0.8 = 80\%
$$

**Meaning:** Out of 100 actual spam emails, the model correctly identifies 80 emails as spam.

---

## 5. FPR — False Positive Rate

### 🔴 Cost

**Definition:** FPR measures how many actual negative cases are incorrectly predicted as positive.

### Formula

$$
FPR = \frac{FP}{FP + TN}
$$

Where:

- `FP` = False Positive
- `TN` = True Negative

### Calculation using the same confusion matrix

$$
FPR = \frac{20}{20 + 80}
$$

$$
FPR = \frac{20}{100} = 0.2 = 20\%
$$

**Meaning:** Out of 100 non-spam emails, the model incorrectly identifies 20 emails as spam.

---

## 6. Threshold Impact

Your faculty explained how changing the threshold affects TPR and FPR.

| Threshold | TPR | FPR |
|---|---|---|
| Small threshold | Increases | Increases |
| Large threshold | Decreases | Decreases |

### Important observations

- Small threshold → More emails classified as spam.
- Large threshold → Fewer emails classified as spam.
- TPR generally increases when the threshold decreases.
- FPR generally increases when the threshold decreases.

---

## 7. ROC Curve

A **ROC curve** is a graph plotted using:

- **X-axis** → FPR
- **Y-axis** → TPR

### Important points

| Point | Meaning |
|---|---|
| (0, 0) | TPR = 0, FPR = 0 |
| (1, 1) | TPR = 1, FPR = 1 |
| (0, 1) | Perfect classification |

**Best ROC curve:** A curve closer to the top-left corner indicates better classification performance.

---

## 8. AUC — Area Under the Curve

AUC represents the area under the ROC curve.

### Interpretation

| AUC value | Model performance |
|---:|---|
| 1.0 | Perfect |
| 0.9 – 1.0 | Excellent |
| 0.8 – 0.9 | Good |
| 0.7 – 0.8 | Fair |
| 0.5 | Random prediction |
| Below 0.5 | Worse than random ranking |

---

# PART 2 — SOFTMAX REGRESSION

## 9. Introduction to Softmax Regression

### Why Softmax Regression?

Your faculty connected Softmax Regression with:

- Deep Learning
- Multi-class Classification

**Binary classification:** Two classes (`0`, `1`).

**Multi-class classification:** More than two classes (`0`, `1`, `2`, `3`, ..., `n`).

### Example — Image Classification

An image classification model identifies:

| Class label | Image class |
|---:|---|
| 0 | Cat |
| 1 | Dog |
| 2 | Horse |
| 3 | Elephant |

Softmax converts raw model scores into probabilities for multiple classes.

---

## 10. Softmax Function

### 📖 Definition

Softmax is an activation function used to convert a vector of raw scores (logits) into a probability distribution across multiple classes.

### Formula

$$
P(y_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$

Where:

- `z_i` = Score of the current class.
- `e` = Exponential constant.
- `K` = Number of classes.
- `j` = Index of each class.
- `i` = Current class.
- `P(y_i)` = Probability of the current class.

---

## 11. Linear Scores and Class Weights

Your faculty wrote the linear score equation:

$$
Z = w_0 + w_1x_1 + w_2x_2 + \cdots + w_nx_n
$$

Where:

- `w₀` = Bias
- `w₁, w₂, ..., wₙ` = Weights
- `x₁, x₂, ..., xₙ` = Input features

For multi-class classification, each class gets its own score.

### Three classes — three equations

**Class 1 — Yes**

$$
Z_1 = w_0^{(1)} + w_1^{(1)}x_1 + w_2^{(1)}x_2
$$

**Class 2 — No**

$$
Z_2 = w_0^{(2)} + w_1^{(2)}x_1 + w_2^{(2)}x_2
$$

**Class 3 — Optional**

$$
Z_3 = w_0^{(3)} + w_1^{(3)}x_1 + w_2^{(3)}x_2
$$

Each class has different weights and bias. The model learns these weights during training.

---

## 12. Step-by-Step Softmax Calculation

Suppose a model predicts three class scores:

- Class 1 → `z₁`
- Class 2 → `z₂`
- Class 3 → `z₃`

### Step 1 — Calculate the exponential of each score

$$
e^{z_1}, \quad e^{z_2}, \quad e^{z_3}
$$

### Step 2 — Calculate the total

$$
D = e^{z_1} + e^{z_2} + e^{z_3}
$$

### Step 3 — Calculate individual probabilities

**Class 1**

$$
P(y_1) = \frac{e^{z_1}}{e^{z_1} + e^{z_2} + e^{z_3}}
$$

**Class 2**

$$
P(y_2) = \frac{e^{z_2}}{e^{z_1} + e^{z_2} + e^{z_3}}
$$

**Class 3**

$$
P(y_3) = \frac{e^{z_3}}{e^{z_1} + e^{z_2} + e^{z_3}}
$$

### Important rule

$$
P(y_1) + P(y_2) + P(y_3) = 1
$$

All class probabilities together must equal `1` (100%).

---

## 13. Multi-Class Classification — Student Example

Your faculty used a GPA / IQ / Result example.

Suppose we want to predict whether a student will get:

| Result | Class label |
|---|---:|
| Yes | 1 |
| No | 2 |
| Optional | 3 |

The model has three possible output classes.

### Input features

- GPA
- IQ

These are the input features used by the model to predict the student's result.

### Model output

The model calculates three scores:

- `Z₁` → Yes
- `Z₂` → No
- `Z₃` → Optional

### Faculty's numerical example

Input values:

- GPA = `6.8`
- IQ = `7.2`

Substitute these values into the three equations.

**Class 1**

$$
Z_1 = 6.8w_1^{(1)} + 7.2w_2^{(1)} + w_0^{(1)}
$$

**Class 2**

$$
Z_2 = 6.8w_1^{(2)} + 7.2w_2^{(2)} + w_0^{(2)}
$$

**Class 3**

$$
Z_3 = 6.8w_1^{(3)} + 7.2w_2^{(3)} + w_0^{(3)}
$$

> **Important observation:** Each class has different weights and bias. The model learns these weights during training.

---

## 14. Training Data and One-Hot Encoding

Your faculty demonstrated how the Result column is converted into separate class columns.

### Original training data

| GPA | IQ | Result |
|---:|---:|---|
| 6.8 | 7.2 | Yes |
| 7.0 | 6.5 | No |
| 8.0 | 8.5 | Optional |

### After One-Hot Encoding

| Result | Yes | No | Optional |
|---|---:|---:|---:|
| Yes | 1 | 0 | 0 |
| No | 0 | 1 | 0 |
| Optional | 0 | 0 | 1 |

### 📖 What is One-Hot Encoding?

One-Hot Encoding converts categorical values into separate binary columns containing `0` and `1`.

Examples:

- Yes → `[1, 0, 0]`
- No → `[0, 1, 0]`
- Optional → `[0, 0, 1]`

### Why is it needed?

It represents categorical class labels in a numerical format that can be used for multi-class model training.

---

## 15. Final Prediction Using Softmax

After calculating the logits:

$$
Z_1,\quad Z_2,\quad Z_3
$$

We apply the Softmax function.

Suppose the resulting probabilities are:

| Class | Probability |
|---|---:|
| Yes | 0.60 |
| No | 0.30 |
| Optional | 0.10 |
| **Total** | **1.00** |

### How does the model select the final class?

The model selects the class with the highest probability.

$$
\text{Prediction} = \operatorname{argmax}(P)
$$

Here:

- Yes = 0.60
- No = 0.30
- Optional = 0.10

**Final prediction: Yes**, because Yes has the highest probability.

> ℹ️ The probabilities `0.60`, `0.30` and `0.10` are an illustrative example from the notes to explain final prediction.

---

## 16. Loss Function

### 📖 Definition

A **Loss Function** measures the difference between the actual output and the predicted output of a Machine Learning model.

**Simple meaning:** It tells us how wrong our model's predictions are.

### Why is Loss Function needed?

Suppose a model predicts a student's result:

- Actual result = Yes
- Predicted probability for Yes = 0.4

The prediction is not good because the model gives only 40% probability to the correct class.

The Loss Function measures this prediction error.

### Main objective

**Minimize Loss.**

When loss decreases, the model's predictions generally improve.

### Faculty's board explanation

The board connects Loss Function with:

- Modifying coefficients (weights and bias).
- Applying Gradient Descent.
- Model training.
- Scikit-learn.
- LLMs and Deep Learning.

The model adjusts its coefficients during training to reduce the loss.

---

## 17. Binary Cross-Entropy Loss (Log Loss)

Your first formula is **Binary Cross-Entropy Loss**.

### Formula

$$
L = -\frac{1}{m}\sum_{i=1}^{m}
\left[
y_i\log(\hat{y}_i)
+
(1-y_i)\log(1-\hat{y}_i)
\right]
$$

### Symbols and meanings

| Symbol | Meaning |
|---|---|
| `L` | Average Loss |
| `m` | Total number of samples |
| `i` | Sample index |
| `yᵢ` | Actual value (0 or 1) |
| `ŷᵢ` | Predicted probability |
| `log` | Natural logarithm |

### Understanding the formula

There are two parts:

**Part 1**

$$
y_i\log(\hat{y}_i)
$$

This part calculates the loss contribution when the actual class is `1`.

**Part 2**

$$
(1-y_i)\log(1-\hat{y}_i)
$$

This part calculates the loss contribution when the actual class is `0`.

The negative sign makes the final loss non-negative.

### Example 1 — Actual output is 1

Suppose:

$$
y = 1,\quad \hat{y} = 0.8
$$

Substitute:

$$
L = -[1\log(0.8) + (1-1)\log(1-0.8)]
$$

$$
L = -\log(0.8) \approx 0.2231
$$

**Low loss:** The model predicted 80% probability for the correct class.

### Example 2 — Actual output is 1

Suppose:

$$
y = 1,\quad \hat{y} = 0.2
$$

$$
L = -\log(0.2) \approx 1.6094
$$

**High loss:** The model predicted only 20% probability for the correct class.

> **Conclusion:** A correct prediction with high confidence produces a low loss. A wrong prediction with high confidence produces a high loss.

---

## 18. Categorical Cross-Entropy Loss

Your faculty's second formula is for multi-class classification.

When we have more than two classes, we use **Categorical Cross-Entropy Loss**.

### Formula

$$
L = -\frac{1}{m}\sum_{i=1}^{m}\sum_{k=1}^{K}
y_k^{(i)}\log(\hat{y}_k^{(i)})
$$

### Symbols and meanings

| Symbol | Meaning |
|---|---|
| `L` | Average Loss |
| `m` | Number of training samples |
| `K` | Number of classes |
| `i` | Sample number |
| `k` | Class number |
| `yₖ⁽ⁱ⁾` | Actual class value |
| `ŷₖ⁽ⁱ⁾` | Predicted probability |

### Example — Student Result Prediction

Suppose we have three classes:

- Yes
- No
- Optional

Actual output:

$$
y = [1, 0, 0]
$$

Predicted probabilities:

$$
\hat{y} = [0.6, 0.3, 0.1]
$$

Apply the formula:

$$
L = -[1\log(0.6) + 0\log(0.3) + 0\log(0.1)]
$$

$$
L = -\log(0.6) \approx 0.5108
$$

**Meaning:** The model assigned 60% probability to the correct class, so the loss is approximately `0.5108`.

### Important Difference

| Binary Cross-Entropy | Categorical Cross-Entropy |
|---|---|
| Binary classification | Multi-class classification |
| Two classes | Multiple classes |
| Actual output 0 or 1 | One-hot encoded target |
| Uses two probability terms | Uses summation across classes |

---

## 19. Gradient Descent

### 📖 Definition

Gradient Descent is an optimization algorithm used to minimize the Loss Function by updating model parameters (weights and bias).

**Simple meaning:** It helps the model find better weights so that prediction errors decrease.

### Why is it needed?

Suppose our model has high loss. We need to modify its coefficients to reduce that loss.

Gradient Descent helps determine:

- Which direction to change weights.
- How much to change weights.
- How to reduce the loss.

### Weight Update Formula

$$
w_{\text{new}} =
w_{\text{old}} -
\alpha\frac{\partial L}{\partial w}
$$

Where:

- `w_new` = Updated weight
- `w_old` = Previous weight
- `α` = Learning rate
- `∂L/∂w` = Gradient of loss with respect to weight

Similarly, bias is updated:

$$
b_{\text{new}} =
b_{\text{old}} -
\alpha\frac{\partial L}{\partial b}
$$

### Simple Example

Suppose:

- Old weight = 5
- Learning rate = 0.1
- Gradient = 2

Substitute:

$$
w_{\text{new}} = 5 - (0.1 \times 2)
$$

$$
w_{\text{new}} = 5 - 0.2 = 4.8
$$

The weight changes from `5` to `4.8`.

This process repeats during training to minimize the loss.

---

## 20. Scikit-learn and Deep Learning

Your faculty also mentioned that Scikit-learn performs optimization during model training.

| Technology | Application |
|---|---|
| Scikit-learn | Machine Learning algorithms and optimization |
| Deep Learning | Neural network training |
| LLM | Large Language Model training |

The common idea is that model parameters are adjusted using optimization techniques to minimize a suitable loss function.

---

## 21. Complete Softmax Workflow

1. **Training Data** — GPA, IQ, Result.
2. **One-Hot Encoding** — Convert categories into 0 and 1.
3. **Calculate Logits** — `Z₁`, `Z₂`, `Z₃`.
4. **Softmax Function** — Convert scores into probabilities.
5. **Calculate Loss** — Categorical Cross-Entropy.
6. **Gradient Descent** — Update weights and bias.
7. **Repeat Training** — Reduce the loss.

```text
Training Data
     |
     v
One-Hot Encoding
     |
     v
Training the Model
(Learn weights and bias)
     |
     v
Calculate Logits
(Z1, Z2, Z3)
     |
     v
Softmax Function
(Convert scores into probabilities)
     |
     v
Calculate Loss
(Categorical Cross-Entropy)
     |
     v
Gradient Descent
(Update weights and bias)
     |
     v
Repeat Training
(Reduce the loss)
     |
     v
Final Prediction
(Select highest probability using Argmax)
```

---

# Quick Revision

| Concept | Meaning |
|---|---|
| ROC | Receiver Operating Characteristic |
| AUC | Area Under the Curve |
| Threshold | Cutoff used to convert probability into a class |
| TPR | True Positive Rate; actual positives correctly identified |
| FPR | False Positive Rate; actual negatives incorrectly predicted positive |
| Logits | Raw scores generated by the model |
| Weights | Values learned during training |
| Bias | Additional parameter in the equation |
| Softmax | Converts logits into probabilities |
| One-Hot Encoding | Converts class labels into binary columns |
| Multi-class Classification | Predicts one class from multiple classes |
| Argmax | Selects the class with the highest probability |
| Loss Function | Measures prediction error |
| Binary Cross-Entropy | Loss used for binary classification |
| Categorical Cross-Entropy | Loss used for multi-class classification |
| Gradient Descent | Minimizes loss by updating parameters |
| Learning Rate | Controls the size of a parameter update |

### 🧠 Remember

- ROC plots TPR against FPR.
- A curve closer to the top-left corner indicates better classification performance.
- Softmax converts logits into probabilities.
- The sum of Softmax probabilities is 1.
- Each class has its own weights and bias.
- One-Hot Encoding represents class labels using 0 and 1.
- Argmax selects the class with the highest probability.
- Binary Cross-Entropy is for binary classification.
- Categorical Cross-Entropy is for multi-class classification.
- Gradient Descent minimizes the loss.
- Weights and bias are updated during training.

---

# Interview Questions

<details>
<summary>Q1. What is ROC?</summary>

ROC stands for Receiver Operating Characteristic. It is a graph that plots True Positive Rate (TPR) against False Positive Rate (FPR) at different thresholds.

</details>

<details>
<summary>Q2. What is AUC?</summary>

AUC means Area Under the Curve. It represents the area under the ROC curve.

</details>

<details>
<summary>Q3. What is a threshold?</summary>

A threshold is a cutoff value used to convert predicted probabilities into class labels.

</details>

<details>
<summary>Q4. What is TPR?</summary>

TPR means True Positive Rate. It measures how many actual positive cases are correctly predicted as positive.

$$
TPR = \frac{TP}{TP + FN}
$$

</details>

<details>
<summary>Q5. What is FPR?</summary>

FPR means False Positive Rate. It measures how many actual negative cases are incorrectly predicted as positive.

$$
FPR = \frac{FP}{FP + TN}
$$

</details>

<details>
<summary>Q6. What is Softmax?</summary>

Softmax is an activation function that converts raw class scores (logits) into probabilities across multiple classes.

</details>

<details>
<summary>Q7. What are logits?</summary>

Logits are the raw scores generated by the model before applying Softmax.

</details>

<details>
<summary>Q8. What is One-Hot Encoding?</summary>

One-Hot Encoding converts categorical values into separate binary columns containing 0 and 1.

</details>

<details>
<summary>Q9. What does Argmax do?</summary>

Argmax selects the class with the highest probability.

</details>

<details>
<summary>Q10. What is a Loss Function?</summary>

A Loss Function measures the difference between the actual output and the predicted output.

</details>

<details>
<summary>Q11. Why do we use Cross-Entropy Loss?</summary>

Cross-Entropy Loss measures the prediction error using the predicted probability assigned to the actual class.

</details>

<details>
<summary>Q12. What is the difference between Binary and Categorical Cross-Entropy?</summary>

Binary Cross-Entropy is used for binary classification. Categorical Cross-Entropy is used for multi-class classification.

</details>

<details>
<summary>Q13. What is Gradient Descent?</summary>

Gradient Descent is an optimization algorithm that minimizes the loss by updating model parameters.

</details>

<details>
<summary>Q14. What is a learning rate?</summary>

The learning rate (`α`) controls the size of each parameter update in Gradient Descent.

</details>

<details>
<summary>Q15. Why do we update weights and bias?</summary>

Weights and bias are updated during training to reduce the loss.

</details>

<details>
<summary>Q16. What is the relationship between Softmax and Categorical Cross-Entropy?</summary>

Softmax converts class logits into probabilities. Categorical Cross-Entropy measures the loss using those probabilities and the actual class labels.

</details>

---

# Practice Questions

Try answering these questions before opening your class notes.

1. If TP = 80 and FN = 20, calculate TPR.
2. If FP = 20 and TN = 80, calculate FPR.
3. What happens to TPR and FPR when the threshold becomes smaller?
4. What does a point near the top-left corner of an ROC graph indicate?
5. What does Softmax do with logits?
6. What is the sum of all Softmax probabilities?
7. Write the One-Hot Encoding for Yes, No and Optional.
8. Which class is selected when probabilities are `[0.60, 0.30, 0.10]`?
9. Calculate Binary Cross-Entropy when `y = 1` and predicted probability is `0.8`.
10. If old weight = 5, learning rate = 0.1 and gradient = 2, calculate the new weight.

---

## ✅ Learning Checklist

- [ ] Understand ROC and AUC.
- [ ] Understand threshold.
- [ ] Calculate TPR and FPR.
- [ ] Understand the threshold impact.
- [ ] Interpret the ROC curve.
- [ ] Understand Softmax Regression.
- [ ] Calculate linear scores for classes.
- [ ] Understand logits and weights.
- [ ] Understand One-Hot Encoding.
- [ ] Calculate Softmax probabilities.
- [ ] Understand Argmax.
- [ ] Understand the Loss Function.
- [ ] Understand Binary Cross-Entropy.
- [ ] Understand Categorical Cross-Entropy.
- [ ] Understand Gradient Descent.
- [ ] Revise the complete workflow.
- [ ] Practise interview questions.

> ⭐ **Final learning point:** In the Softmax workflow, the model calculates class scores, converts them into probabilities, measures prediction error using a suitable loss, and updates weights and bias through optimization during training.
