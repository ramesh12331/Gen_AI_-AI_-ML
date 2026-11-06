# 🤖 Chapter — Logistic Regression

## 1. What is Logistic Regression?

### 📖 Definition

Logistic Regression is a supervised Machine Learning algorithm used mainly for classification problems.

It predicts the probability that an input belongs to a particular class.

**Simple meaning:** Logistic Regression helps a computer decide which category something belongs to.

### 💡 Real-world examples

| Problem | Possible classes |
|---|---|
| Email detection | Spam / Not Spam |
| Customer prediction | Buy / Not Buy |
| Disease prediction | Disease / No Disease |
| Flower classification | Setosa / Versicolor / Virginica |
| Loan prediction | Approved / Rejected |

### Important point

Despite the word *Regression* in its name, Logistic Regression is commonly used for classification.

---

## 2. Logistic Regression vs Linear Regression

| Linear Regression | Logistic Regression |
|---|---|
| Used for regression | Used for classification |
| Predicts numerical values | Predicts class probabilities |
| Example: House price | Example: Spam detection |
| Uses a straight-line equation | Uses a sigmoid or softmax function |

---

## 3. Types of Logistic Regression

### 1. Binary Logistic Regression

Used when there are only two possible classes.

Example:

- 0 → Not Spam
- 1 → Spam

### 2. Multinomial Logistic Regression

Used when there are more than two classes.

Example:

- 0 → Setosa
- 1 → Versicolor
- 2 → Virginica

### 3. Ordinal Logistic Regression

Used when classes have a meaningful order.

Example:

- Low
- Medium
- High

**Our Jupyter Notebook uses Multiclass Logistic Regression.**

---

## 4. Understanding the Mathematics

### A. Linear combination

First, the algorithm calculates a score from the input features.

For one feature:

$$
z = wx + b
$$

For multiple features:

$$
z = b + w_1x_1+w_2x_2+\cdots+w_nx_n
$$

Where:

- $z$ = Calculated score
- $x$ = Input feature
- $w$ = Model weight or coefficient
- $b$ = Bias or intercept

### B. Sigmoid Function

For binary Logistic Regression, the sigmoid function converts the score into a probability between 0 and 1.

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

Where:

- $z$ = Model score
- $e$ = Mathematical constant
- $\sigma(z)$ = Predicted probability

**Example:**

Suppose the model predicts:

$$
P(Spam)=0.85
$$

This means the model estimates an 85% probability of Spam.

If the threshold is 0.50:

- Probability >= 0.50 → Class 1
- Probability < 0.50 → Class 0

### C. Softmax Function

Your notebook has three flower classes. Multiclass Logistic Regression can use the Softmax function to calculate probabilities for all classes.

$$
P(y=k|x)=
\frac{e^{z_k}}
{\sum_{j=1}^{K}e^{z_j}}
$$

Where:

- $K$ = Number of classes
- $z_k$ = Score for class k
- $P(y=k|x)$ = Probability of class k

Example of possible model probabilities:

| Flower | Probability |
|---|---:|
| Setosa | 0.90 |
| Versicolor | 0.07 |
| Virginica | 0.03 |

The model selects Setosa because it has the highest probability.

**Remember:** The probabilities add up to 1.

---

## 5. Understanding the Iris Dataset

Your notebook uses the Iris dataset from Seaborn.

### What is the Iris dataset?

It contains flower measurements and their corresponding species.

| Feature | Meaning |
|---|---|
| sepal_length | Sepal length |
| sepal_width | Sepal width |
| petal_length | Petal length |
| petal_width | Petal width |
| species | Flower category |

The target contains three flower categories:

- Setosa
- Versicolor
- Virginica

### Dataset loading

```python
import pandas as pd
import seaborn as sns

# Load Iris dataset
df = sns.load_dataset('iris')

# Display dataset
print(df.head())
```

### Output structure

| sepal_length | sepal_width | petal_length | petal_width | species |
|---:|---:|---:|---:|---|
| 5.1 | 3.5 | 1.4 | 0.2 | setosa |
| 4.9 | 3.0 | 1.4 | 0.2 | setosa |
| 7.0 | 3.2 | 4.7 | 1.4 | versicolor |
| 6.3 | 3.3 | 6.0 | 2.5 | virginica |

These rows are illustrative examples of the dataset structure.

---

## 6. Convert Target Categories into Numbers

Machine Learning models need numerical target labels.

Your notebook uses:

```python
df['species'] = df['species'].apply(
    lambda x: 0 if x == 'setosa'
    else 1 if x == 'virginica'
    else 2
)
```

### Understand the code

The `lambda` function checks the flower name.

| Original species | Encoded value |
|---|---:|
| setosa | 0 |
| virginica | 1 |
| versicolor | 2 |

**Note:** The mapping in your notebook is Setosa = 0, Virginica = 1 and Versicolor = 2.

The notebook comment mentions data leakage when encoding the target. Target encoding using a fixed mapping like this is not automatically data leakage. Leakage happens when information from the test data improperly influences model training or preprocessing.

---

## 7. Check Class Distribution

```python
# Count the number of samples in each class
print(df['species'].value_counts())
```

### Definition

Class distribution tells us how many observations belong to each category.

Why is it important?

Suppose:

| Class | Samples |
|---|---:|
| Setosa | 50 |
| Versicolor | 50 |
| Virginica | 50 |

The classes are balanced.

If one class has many more samples than the others, the dataset may be imbalanced.

---

## 8. Separate Input Features and Target

### Definition

- X = Input features used to make predictions.
- y = Target value that we want to predict.

### Syntax

```python
X = df.drop(columns='species')

y = df['species']
```

### Understand the code

```python
# Input features
X = df.drop(columns='species')

# Target variable
y = df['species']
```

Our X contains:

- sepal_length
- sepal_width
- petal_length
- petal_width

Our y contains:

- 0
- 1
- 2

---

## 9. Train-Test Split

### Definition

Train-test split divides a dataset into two parts:

- Training data: Used to teach the model.
- Testing data: Used to evaluate the trained model.

### Syntax

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

### Understand parameters

| Parameter | Meaning |
|---|---|
| X | Input features |
| y | Target values |
| test_size=0.2 | 20% test data |
| random_state=42 | Reproducible split |
| stratify=y | Preserve class proportions |

### Dry Run

The Iris dataset contains 150 rows.

$$
Training\ Data = 150 \times 0.80 = 120
$$

$$
Testing\ Data = 150 \times 0.20 = 30
$$

Therefore:

- Training samples = 120
- Testing samples = 30

Because `stratify=y` is used and the Iris dataset has 50 samples per class:

- Training samples per class = 40
- Testing samples per class = 10

---

## 10. Feature Scaling — StandardScaler

### Definition

Feature scaling brings numerical features to a comparable scale.

Logistic Regression can benefit from feature scaling because it helps the optimization process and makes regularization behave more consistently across features.

### Formula

$$
z=\frac{x-\mu}{\sigma}
$$

Where:

- $x$ = Original value
- $\mu$ = Mean
- $\sigma$ = Standard deviation
- $z$ = Scaled value

### Syntax

```python
from sklearn.preprocessing import StandardScaler

# Create scaler
sc = StandardScaler()

# Fit and transform training data
X_train_scaled = sc.fit_transform(X_train)

# Transform testing data
X_test_scaled = sc.transform(X_test)
```

### Why fit_transform on training data?

`fit()` learns the mean and standard deviation.

`transform()` applies the learned scaling.

**Important:**

- Training data → `fit_transform()`
- Testing data → `transform()`

Never fit the scaler separately on the test data. That would allow test-data information to influence preprocessing.

---

## 11. Create Logistic Regression Model

### Syntax

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    random_state=42,
    max_iter=200
)
```

### Understand parameters

| Parameter | Meaning |
|---|---|
| random_state=42 | Reproducibility for applicable randomized operations |
| max_iter=200 | Maximum optimization iterations |

The model uses regularization by default in scikit-learn.

---

## 12. Train the Model

### Definition

Training means allowing the algorithm to learn relationships between input features and target classes.

### Syntax

```python
model.fit(X_train_scaled, y_train)
```

### Understand

- `X_train_scaled` → Training input features.
- `y_train` → Correct training labels.
- `fit()` → Learns the model parameters.

After training, the model can predict flower categories.

---

## 13. Make Predictions

### Definition

Prediction means using the trained model to estimate classes for new input data.

### Syntax

```python
y_pred = model.predict(X_test_scaled)

print(y_pred)
```

### Example

```python
y_test[0:5]
```

Displays the first five actual labels.

```python
y_pred[0:5]
```

Displays the first five predicted labels.

### Compare

| Actual | Predicted | Result |
|---:|---:|---|
| 0 | 0 | Correct |
| 1 | 1 | Correct |
| 2 | 1 | Incorrect |
| 0 | 0 | Correct |
| 2 | 2 | Correct |

These are illustrative values to explain comparison, not claimed notebook output.

---

## 14. Predict Probabilities

### Definition

`predict_proba()` returns the probability of each possible class.

### Syntax

```python
y_prob = model.predict_proba(X_test_scaled)

print(y_prob[:5])
```

### Example

```text
[
 [0.90, 0.07, 0.03],
 [0.05, 0.85, 0.10],
 [0.02, 0.08, 0.90]
]
```

Illustrative probabilities:

| Setosa | Versicolor | Virginica | Predicted class |
|---:|---:|---:|---|
| 0.90 | 0.07 | 0.03 | Setosa |
| 0.05 | 0.85 | 0.10 | Versicolor |
| 0.02 | 0.08 | 0.90 | Virginica |

The predicted class is the class with the highest probability.

---

## 15. Model Evaluation

Your notebook uses three main evaluation tools.

### A. Accuracy Score

Definition: Measures the percentage of correct predictions.

$$
Accuracy=\frac{Correct\ Predictions}{Total\ Predictions}
$$

Syntax:

```python
from sklearn.metrics import accuracy_score

acc = accuracy_score(y_test, y_pred)

print(acc)
```

### B. Confusion Matrix

Definition: Compares actual and predicted classes.

Syntax:

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)
```

### C. Classification Report

Definition: Displays Precision, Recall, F1-score and support for each class.

Syntax:

```python
from sklearn.metrics import classification_report

print(classification_report(
    y_test,
    y_pred,
    target_names=[
        'setosa',
        'versicolor',
        'virginica'
    ]
))
```

### Understand the classification report

| Term | Meaning |
|---|---|
| Precision | Correctness of positive predictions for a class |
| Recall | How many actual samples of a class were identified |
| F1-score | Balance between Precision and Recall |
| Support | Number of actual samples in that class |
| Macro avg | Unweighted average across classes |
| Weighted avg | Average weighted by class support |

---

## 16. Confusion Matrix Visualization

Your notebook uses Seaborn to visualize the confusion matrix.

### Syntax

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(
    cm,
    annot=True,
    fmt='d'
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.show()
```

### Why use a heatmap?

A heatmap makes it easier to see:

- Correct predictions along the diagonal.
- Incorrect predictions outside the diagonal.

---

## 17. Actual vs Predicted Visualization

Your notebook also compares actual and predicted labels using a line plot.

### Syntax

```python
import matplotlib.pyplot as plt

plt.plot(
    y_test.values,
    label='Actual',
    marker='o'
)

plt.plot(
    y_pred,
    label='Predicted',
    marker='X'
)

plt.xlabel("Sample Index")
plt.ylabel("Flower Class")
plt.title("Actual vs Predicted")

plt.legend()
plt.show()
```

### Understand

- Actual line → Correct class labels.
- Predicted line → Model predictions.
- Matching points → Correct predictions.
- Different points → Incorrect predictions.

**Note:** This plot is a simple visual comparison in the order of the test samples. A confusion matrix is generally more informative for evaluating classification performance.

---

## 18. Complete Workflow — Dry Run

Follow the complete process:

| Step | Operation | Purpose |
|---:|---|---|
| 1 | Load Iris dataset | Get flower data |
| 2 | Encode species | Convert classes into numbers |
| 3 | Check value counts | Understand class distribution |
| 4 | Separate X and y | Identify features and target |
| 5 | Train-test split | Divide the data |
| 6 | StandardScaler | Scale features |
| 7 | Create model | Initialize Logistic Regression |
| 8 | Fit model | Train the model |
| 9 | Predict | Predict flower classes |
| 10 | Predict probabilities | Get class probabilities |
| 11 | Evaluate | Calculate performance |
| 12 | Visualize | Understand predictions |

### Complete dry run in simple English

1. We load 150 Iris flower records.
2. We convert the species names into numeric labels.
3. We separate four flower measurements into X and species into y.
4. We divide the dataset into 120 training rows and 30 testing rows.
5. We scale the features using training-data statistics.
6. We create the Logistic Regression model.
7. We train the model using the training data.
8. We predict the flower classes for the testing data.
9. We calculate the accuracy and other classification metrics.
10. We visualize the confusion matrix.

---

## 19. Final Summary

| Concept | Simple Meaning |
|---|---|
| Logistic Regression | Classification algorithm |
| Binary Classification | Two classes |
| Multiclass Classification | More than two classes |
| Sigmoid | Converts a score into a binary probability |
| Softmax | Converts class scores into multiclass probabilities |
| X | Input features |
| y | Target variable |
| Train-test split | Divides data into training and testing |
| StandardScaler | Scales numerical features |
| fit() | Trains the model |
| predict() | Predicts class labels |
| predict_proba() | Predicts class probabilities |
| Accuracy | Measures correct predictions |
| Confusion Matrix | Shows correct and incorrect predictions |
| Classification Report | Shows Precision, Recall, F1 and support |

---

## 20. Interview Questions and Answers

**Q1. What is Logistic Regression?**

Logistic Regression is a supervised Machine Learning algorithm mainly used for classification problems.

**Q2. Why is Logistic Regression called Regression?**

Because it models a relationship between input features and the log-odds of a class. It is commonly used for classification.

**Q3. What is the Sigmoid function?**

The Sigmoid function converts a numerical score into a probability between 0 and 1.

**Q4. What is the Softmax function?**

Softmax converts multiple class scores into probabilities that add up to 1.

**Q5. What is Binary Classification?**

Classification involving only two possible classes, such as Spam and Not Spam.

**Q6. What is Multiclass Classification?**

Classification involving more than two classes, such as Setosa, Versicolor and Virginica.

**Q7. What is the difference between predict() and predict_proba()?**

`predict()` returns the predicted class. `predict_proba()` returns the probability for each class.

**Q8. Why do we use StandardScaler?**

It brings features to a comparable scale and helps the optimization and regularization process.

**Q9. Why do we use train_test_split()?**

To train the model on one part of the dataset and evaluate it on unseen data.

**Q10. What is random_state?**

It controls randomness so that applicable random operations can be reproduced.

**Q11. What is max_iter?**

It specifies the maximum number of optimization iterations allowed for model fitting.

**Q12. What is a Confusion Matrix?**

It compares actual and predicted classes and shows the correct and incorrect predictions.

**Q13. What is class imbalance?**

It occurs when some classes have significantly more observations than others.

**Q14. Why do we use stratify=y?**

It helps preserve the class proportions in training and testing datasets.

**Q15. What is regularization in Logistic Regression?**

Regularization penalizes large model coefficients to help reduce overfitting.

**Q16. What is the difference between Logistic Regression and Linear Regression?**

Linear Regression predicts numerical values, while Logistic Regression estimates class probabilities for classification.

---

## ✅ Final Revision Checklist

- [ ] Understand Logistic Regression.
- [ ] Understand Binary and Multiclass Classification.
- [ ] Learn Sigmoid and Softmax.
- [ ] Understand the Iris dataset.
- [ ] Learn target encoding.
- [ ] Understand X and y.
- [ ] Practise train-test split.
- [ ] Learn StandardScaler.
- [ ] Understand model.fit().
- [ ] Understand predict() and predict_proba().
- [ ] Calculate Accuracy.
- [ ] Read a Confusion Matrix.
- [ ] Understand Classification Report.
- [ ] Practise the complete notebook independently.

**Your next goal:** Run your uploaded notebook cell by cell and explain what each line does without looking at these notes.