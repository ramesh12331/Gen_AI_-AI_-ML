# Machine Learning Class Notes

## Class Date: 11-11-2026



Classroom screenshots covered

Continuation



Today's class covers two important topics:

1. Softmax Regression — Loss Function and Model Training
2. Polynomial Features — Polynomial Regression and Degree Selection

I will explain the classroom formulas step by step, with simple English, Telugu meanings, examples and Python code.

# PART 1 — SOFTMAX REGRESSION

## 1. Logistic Regression Loss Function (Log Loss)

Your first screenshot shows the Logistic Regression Loss Function.

### Definition

Log Loss measures how far the predicted probability is from the actual class.

It is also called Binary Cross-Entropy Loss.

### Formula

\\[ L=-\frac{1}{m}\sum\_{i=1}^{m} \left[ y_i\log(\hat y_i) +(1-y_i)\log(1-\hat y_i) \right] \\]

### Understanding with an example

Suppose we are building an email spam detection model.

- Spam = 1
- Not Spam = 0

Actual output:

\\[ y=1 \\]

Predicted probability:

\\[ \hat y=0.8 \\]

Then:

\\[ L=-[1\log(0.8)+(1-1)\log(1-0.8)] \\]

\\[ L=-\log(0.8) \\]

\\[ \boxed{L=0.2231} \\]

The model gives 80% probability to the correct class, so the loss is low.

Important: Binary Log Loss is used for binary classification, whereas Softmax Regression uses Categorical Cross-Entropy for multi-class classification.

## 2. Softmax Regression — Multi-Class Classification

### Definition

Softmax Regression is a classification algorithm used to predict one class among multiple possible classes.

It converts model scores (logits) into probabilities.

### Real-world example

Suppose we want to classify fruits:

[Red apple isolated on white background](https://images.openai.com/static-rsc-4/FzVY-DVzU-2KklMMg8WTKJq8lMCKPXmdUxHLLvrGUyC1PP12UBa8mlhfleAieB4lTyWImy0hI6JMxZjGmcjB15_dUFRJgvWrKbX6P8F_kDL5cumjGqkbXgnvSuM3l4u1wI8F07cNgwCvx2vmaf9DVYPeVCI4pxEXVSJFZiMYRKoI6wqhpAJM1HFsciM7vpdE?purpose=inline)

Apple

Class 1

[Ripe banana isolated on white background. full depth of field](https://images.openai.com/static-rsc-4/S13-3RKAIyUoWuvfkukCiglLCu_Px9P_5a196yda4LtNXa3ZP9k6BZ-skr2A7BQKnYwvVqo1Qhk219IuZSmC8DXMXIY51R6k7u1bzRmHPjj25mDvATeBXkUroKn5NWkjLgVskgc94YWTraiB7ren_94DNMeTA0ahYBpfBltmZKZiw_Fo7GDqu2HEcdbjQIFy?purpose=inline)

Banana

Class 2

[Single orange fruit isolated on white background](https://images.openai.com/static-rsc-4/MB4N3kw_R9853sZtP2p-WPY7mabF8L3_R7tr10F2DDMzBswQcH6B9AA2WgUrly9TNR22D16FkMqSu-wPKVsz7dysbn7OKTnU3g6Ab5SV-_9TJtvBc9g0BGCHukpmGtrwjNHN56-CoJSZKEeVPvyDezI_rE1agnxXGFMmizvO90f63iHVRLtQCqvGxssy3mIe?purpose=inline)

Orange

Class 3

The model predicts:

| Fruit  | Probability |
| ------ | ----------- |
| Apple  | 0.70        |
| Banana | 0.20        |
| Orange | 0.10        |
| Total  | 1.00        |

The highest probability is 0.70, so the predicted class is Apple.

### Softmax formula

\\[ P(y=k)=\frac{e^{z_k}}{\sum\_{j=1}^{K}e^{z_j}} \\]

Where:

- \\(z_k\\) = Score (logit) for class k.
- \\(K\\) = Total number of classes.
- \\(e\\) = Euler's number (approximately 2.718).
- \\(P(y=k)\\) = Probability of class k.

Remember: All Softmax probabilities add up to 1.

## 3. One-Hot Encoding

Your faculty shows three outputs:

- Output 1 → Class 1
- Output 2 → Class 2
- Output 3 → Class 3

This is called One-Hot Encoding.

### Definition

One-Hot Encoding converts categorical values into binary values (0 and 1).

### Example

Suppose we have three classes:

| Sample    | Actual Class |
| --------- | ------------ |
| Student 1 | Class 1      |
| Student 2 | Class 2      |
| Student 3 | Class 3      |

One-Hot Encoding:

| Sample    | Class 1 | Class 2 | Class 3 |
| --------- | ------- | ------- | ------- |
| Student 1 | 1       | 0       | 0       |
| Student 2 | 0       | 1       | 0       |
| Student 3 | 0       | 0       | 1       |

### Visual understanding

Student 1

Class 1

### 1

Class 1

### 0

Class 2

### 0

Class 3

Student 2

Class 2

### 0

Class 1

### 1

Class 2

### 0

Class 3

Student 3

Class 3

### 0

Class 1

### 0

Class 2

### 1

Class 3

Why do we use it?

Because a multi-class classification model needs a numerical representation of the actual class to calculate Cross-Entropy Loss.

## 4. Categorical Cross-Entropy Loss — Detailed Derivation

This is the main formula shown in your classroom screenshots.

### Formula

\\[ L=-\frac{1}{m}\sum\_{i=1}^{m} \sum\_{k=1}^{K} y_k^{(i)}\log(\hat y_k^{(i)}) \\]

For three classes:

\\[ K=3 \\]

For three samples:

\\[ m=3 \\]

Expanding the formula:

\\[ \begin{aligned} L=-\frac{1}{3}[& y_1^{(1)}\log(\hat y_1^{(1)}) +y_2^{(1)}\log(\hat y_2^{(1)}) +y_3^{(1)}\log(\hat y_3^{(1)})\\\ +&y_1^{(2)}\log(\hat y_1^{(2)}) +y_2^{(2)}\log(\hat y_2^{(2)}) +y_3^{(2)}\log(\hat y_3^{(2)})\\\ +&y_1^{(3)}\log(\hat y_1^{(3)}) +y_2^{(3)}\log(\hat y_2^{(3)}) +y_3^{(3)}\log(\hat y_3^{(3)}) ] \end{aligned} \\]

### Simplification using One-Hot Encoding

Look at the first sample:

\\[ y^{(1)}=[1,0,0] \\]

Its contribution:

\\[ 1\log(\hat y_1^{(1)}) +0\log(\hat y_2^{(1)}) +0\log(\hat y_3^{(1)}) \\]

Therefore:

\\[ =\log(\hat y_1^{(1)}) \\]

Similarly, second sample:

\\[ y^{(2)}=[0,1,0] \\]

Contribution:

\\[ =\log(\hat y_2^{(2)}) \\]

Third sample:

\\[ y^{(3)}=[0,0,1] \\]

Contribution:

\\[ =\log(\hat y_3^{(3)}) \\]

### Final simplified formula

\\[ \boxed{ L=-\frac{1}{3} [ \log(\hat y_1^{(1)}) +\log(\hat y_2^{(2)}) +\log(\hat y_3^{(3)}) ] } \\]

Important classroom concept: Because One-Hot Encoding contains one 1 and all remaining values are 0, only the predicted probability of the actual class contributes to the loss.

## 5. Softmax Regression — Model Weights and Bias

Your faculty explains how each class gets its own weights and bias.

Suppose we have:

- Two input features: \\(x_1,x_2\\)
- Three output classes: Class 1, Class 2, Class 3

Each class has separate model parameters.

### Class 1

\\[ z_1=w_1^{(1)}x_1+w_2^{(1)}x_2+w_0^{(1)} \\]

### Class 2

\\[ z_2=w_1^{(2)}x_1+w_2^{(2)}x_2+w_0^{(2)} \\]

### Class 3

\\[ z_3=w_1^{(3)}x_1+w_2^{(3)}x_2+w_0^{(3)} \\]

Here:

- \\(w_1,w_2\\) = Feature weights.
- \\(w_0\\) = Bias.
- \\(x_1,x_2\\) = Input features.
- \\(z_1,z_2,z_3\\) = Class scores (logits).

### Model Architecture

Input Features\
\\(x_1,\ x_2\\)

Class 1

Weights + Bias

\\(z_1\\)

Class 2

Weights + Bias

\\(z_2\\)

Class 3

Weights + Bias

\\(z_3\\)

Softmax Function

Convert scores into probabilities

Final Prediction\
\\(P_1,\ P_2,\ P_3\\)

### Weight Matrix

The weights can be represented in a matrix:

\\[ W= \begin{bmatrix} w_1^{(1)}&w_2^{(1)}&w_0^{(1)}\\\ w_1^{(2)}&w_2^{(2)}&w_0^{(2)}\\\ w_1^{(3)}&w_2^{(3)}&w_0^{(3)} \end{bmatrix} \\]

During training, Gradient Descent updates these weights and biases to minimize Cross-Entropy Loss.

# PART 2 — POLYNOMIAL FEATURES

## 6. What are Polynomial Features?

### Definition

Polynomial Features are new features created by adding powers and combinations of existing input features.

They help a Machine Learning model learn non-linear relationships between input and output.

Simple meaning: We take existing columns and create additional columns using multiplication and powers.

### Why do we need Polynomial Features?

Consider a dataset:

| Hours Studied (X) | Marks (Y) |
| ----------------- | --------- |
| 1                 | 10        |
| 2                 | 25        |
| 3                 | 50        |
| 4                 | 85        |
| 5                 | 130       |

The relationship between study hours and marks may not be a straight line.

A simple Linear Regression model might not fit this pattern properly.

We can create additional features:

\\[ X,\quad X^2,\quad X^3 \\]

Now the model can learn a curved relationship.

## 7. Linear Regression vs Polynomial Regression

[Linear Regression: The Straightforward Path to Predicting the Future | by KararHaiderDeepVision | Medium](https://images.openai.com/static-rsc-4/CcpKfrVm0Bo1qFKHlq-rjxTZa2jW3kxW02SenfgNtjjS3ibKKeO6wKDomcmrYoCFcuFzRSpyEBgmeOzIXsVfqwwXCEGouQ_ATry-lifhhpiClp43kwqRXA1vLuJe_tQ8k9D3YFdzfkETWCH4lwnZGuRzfzWnweU7eGhVqr1gqnY?purpose=inline)

Linear Regression

Fits a straight line.

\\[ y=w_0+w_1x \\]

[A powerful machine learning algorithm model-Polynomial Regression | by Gen. Devin DL. | Medium](https://images.openai.com/static-rsc-4/VIowseixEz8lR33yQh7Re5RgKhpfOGTWELJHG-6TOibCmvllxEOJoVEBbS9I3xykhq1oye23P8y7uiQiXbqPKboI6Quf5RvK9CD1fjUdfrg4_0eOpuZkIBvbfJ5jXCKaCVORFo-sjtxEcpVPlYc6p_-B1eOdVWSmZnPzabCPQ4Q?purpose=inline)

Polynomial Regression

Fits a curved relationship.

\\[ y=w_0+w_1x+w_2x^2 \\]

### Important Difference

| Linear Regression          | Polynomial Regression    |
| -------------------------- | ------------------------ |
| Straight-line relationship | Curved relationship      |
| Uses original features     | Uses polynomial features |
| Degree 1                   | Degree 2, 3, etc.        |
| Simple model               | More flexible model      |

Important: Polynomial Regression is still a Linear Regression model in terms of its coefficients. It becomes non-linear with respect to the original input features.

## 8. Polynomial Degree

### Definition

Degree determines the highest power of the input feature used in Polynomial Regression.

### Example

Suppose we have one feature:

\\[ X=2 \\]

Degree 1

\\[ X,\quad 2 \\]

Model:

\\[ y=w_0+w_1x \\]

Degree 2

\\[ X,\quad X^2 \\]

Model:

\\[ y=w_0+w_1x+w_2x^2 \\]

Degree 3

\\[ X,\quad X^2,\quad X^3 \\]

Model:

\\[ y=w_0+w_1x+w_2x^2+w_3x^3 \\]

### Degree Comparison

| Degree | Features                | Model     |
| ------ | ----------------------- | --------- |
| 1      | \\(x\\)                 | Linear    |
| 2      | \\(x,x^2\\)             | Quadratic |
| 3      | \\(x,x^2,x^3\\)         | Cubic     |
| 4      | \\(x,x^2,x^3,x^4\\)     | Quartic   |
| 5      | \\(x,x^2,x^3,x^4,x^5\\) | Degree 5  |

## 9. Polynomial Features with Two Input Variables

Your faculty also shows two input features:

\\[ X_1,\quad X_2 \\]

For degree 2, the full polynomial feature expansion is:

\\[ 1,\quad X_1,\quad X_2,\quad X_1^2,\quad X_1X_2,\quad X_2^2 \\]

For degree 3:

\\[ \begin{aligned} 1,\ X_1,\ X_2,\ X_1^2,\ X_1X_2,\ X_2^2,\\\ X_1^3,\ X_1^2X_2,\ X_1X_2^2,\ X_2^3 \end{aligned} \\]

### Understanding with an example

Original dataset:

| X1 | X2 |
| -- | -- |
| 2  | 3  |
| 3  | 4  |
| 4  | 5  |

After Polynomial Features of degree 2:

| X1 | X2 | X1² | X1 × X2 | X2² |
| -- | -- | --- | ------- | --- |
| 2  | 3  | 4   | 6       | 9   |
| 3  | 4  | 9   | 12      | 16  |
| 4  | 5  | 16  | 20      | 25  |

Notice that the model has created three additional columns.

Why? These additional features help the model learn more complex patterns.

## 10. Polynomial Regression Formula — Degree 3

Your classroom board shows the model equation for degree 3.

For one input feature:

\\[ \boxed{ y=w_0+w_1x+w_2x^2+w_3x^3 } \\]

For two input features, the full degree-3 model is:

\\[ \begin{aligned} y={}&w_0+w_1x_1+w_2x_2\\\ &+w_3x_1^2+w_4x_1x_2+w_5x_2^2\\\ &+w_6x_1^3+w_7x_1^2x_2\\\ &+w_8x_1x_2^2+w_9x_2^3 \end{aligned} \\]

Each newly created feature receives its own weight.

## 11. Underfitting and Overfitting

This is another important topic shown in your screenshots.

### Underfitting

Definition: Underfitting happens when a model is too simple to learn the actual patterns in the training data.

Example: Using a straight line for data that follows a complex curve.

Model is too simple

Common signs:

- High training error.
- High testing error.
- Model cannot learn important patterns.

### Overfitting

Definition: Overfitting happens when a model learns the training data too closely, including noise and unnecessary patterns.

Example: A degree-15 polynomial creates a very complicated curve that fits training points but performs poorly on new data.

Model is too complex

Common signs:

- Very low training error.
- High testing error.
- Poor performance on unseen data.

### Visual Difference

[What is Underfitting? How to Detect and Overcome High Bias in ML Models | DataCamp](https://images.openai.com/static-rsc-4/R5-gJh6MDSuA1kTu_r6e0E6L3Nn4p7MPR8p8uMilVkmJbdOXW5s3xfMHZNbs2XKwl9PuHNb8W0V76bhd2CayfvFM-2-J6F034JcMicsHvZ6aCoq88TpybRaOta8JOqysRVx22CC-BRX13MY6vFjFawb5nRpaB3uLTvAFtqzzLAY?purpose=inline)

Underfitting

Model does not capture the pattern.

[The Ultimate Machine Learning Cheat Sheet for Non-Specialists | ML4Industry energy Blog | ML4Industry](https://images.openai.com/static-rsc-4/ddb7muQVDihWfGScH--e_Uw7EA8kjAQHhyms6MkgE7qkR_kzMNxFAhfSNMWpRkl4UZ7YBuAlaTt4qtw-Qtz0NzW9ZsTbZw1XCa1A5RnVYq-yaVABtEw8KIKR5sPiIQiuga8baG8WVcjO59Up_06RSKtIfGR6gQVL1GCO_OC3cvs?purpose=inline)

Overfitting

Model follows training noise.

### Relationship with Degree

Your faculty explains:

- Degree increases → Overfitting risk increases.
- Degree decreases → Underfitting risk increases.

This is a general tendency, not an absolute rule. The actual result depends on the dataset, noise and regularization.

## 12. Optimum Degree Selection

### Definition

Optimum Degree is the polynomial degree that provides a good balance between underfitting and overfitting.

### Example

Suppose we test different degrees:

| Degree | Training Error | Testing Error |
| ------ | -------------- | ------------- |
| 1      | High           | High          |
| 2      | Medium         | Medium        |
| 3      | Low            | Low           |
| 4      | Very low       | Low           |
| 5      | Very low       | High          |

In this hypothetical example, degree 3 may be a good choice.

The numbers are illustrative, not results from your classroom dataset.

### Hyperparameter Tuning

Polynomial degree is a hyperparameter because we choose it before training the model.

We can try multiple degrees and compare their validation performance.

Typical process:

1. Select possible degrees.
2. Generate polynomial features.
3. Train the model.
4. Calculate validation error.
5. Compare results.
6. Select a suitable degree.

Important: Do not select a degree only because it gives the lowest training error. Check validation or test performance.

# PART 3 — PYTHON PRACTICAL

## 13. Implement Polynomial Regression using Scikit-learn

### Step 1 — Import Libraries

```
import numpy as npimport pandas as pdfrom sklearn.preprocessing import PolynomialFeaturesfrom sklearn.linear_model import LinearRegressionfrom sklearn.model_selection import train_test_splitfrom sklearn.metrics import mean_squared_error, r2_score
```

### Step 2 — Create Dataset

```
# Input featureX = np.array([    [1],    [2],    [3],    [4],    [5],    [6],    [7],    [8],    [9],    [10]])# Target variabley = np.array([    5, 12, 23, 38, 57,    80, 107, 138, 173, 212])
```

### Step 3 — Split Dataset

```
X_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.2,    random_state=42)
```

### Step 4 — Create Polynomial Features

```
# Create polynomial features of degree 2poly = PolynomialFeatures(degree=2)X_train_poly = poly.fit_transform(X_train)X_test_poly = poly.transform(X_test)
```

### Step 5 — Train Model

```
model = LinearRegression()model.fit(X_train_poly, y_train)
```

### Step 6 — Make Predictions

```
y_pred = model.predict(X_test_poly)print("Actual:", y_test)print("Predicted:", y_pred)
```

### Step 7 — Evaluate Model

```
mse = mean_squared_error(y_test, y_pred)r2 = r2_score(y_test, y_pred)print("MSE:", mse)print("R2 Score:", r2)
```

### Complete workflow

Dataset

Train-Test Split

PolynomialFeatures(degree=2)

LinearRegression()

Model Prediction

MSE and R² Evaluation

# PART 4 — INTERVIEW PREPARATION

## 14. Important Interview Questions

Q1. What is Softmax Regression?

Softmax Regression is a classification algorithm used to predict probabilities for multiple classes.

Q2. What is One-Hot Encoding?

It converts categorical values into binary representations using 0 and 1.

Q3. What is Categorical Cross-Entropy?

It is a loss function used to measure the difference between actual and predicted class probabilities in multi-class classification.

Q4. What is the difference between Sigmoid and Softmax?

- Sigmoid: Commonly used for binary classification.
- Softmax: Commonly used for mutually exclusive multi-class classification.

Q5. What are Polynomial Features?

They are additional features created using powers and combinations of existing features.

Q6. What is Polynomial Degree?

It represents the highest power used to create polynomial features.

Q7. What is Underfitting?

When a model is too simple to learn the underlying data patterns.

Q8. What is Overfitting?

When a model learns training data too closely and performs poorly on unseen data.

Q9. What is Hyperparameter Tuning?

It is the process of selecting suitable hyperparameter values to improve model performance.

Q10. How do you select the optimum polynomial degree?

By comparing validation performance for different polynomial degrees.

## 15. Practice Questions

Test your understanding

0/5 answered

1\. Which loss function is commonly used for multi-class classification?

Mean Squared Error

Categorical Cross-Entropy

MAE

2\. What is the purpose of One-Hot Encoding?

Convert categories into binary values

Remove missing values

Scale numerical values

3\. For degree 3, which feature is included for a single input x?

x⁴

x³

1/x

4\. What happens when a model is too simple?

Overfitting

Underfitting

Perfect fitting

5\. Which data should be used to select the optimum degree?

Only training data

Validation data

Only the target column

Submit Answers

## 16. Quick Revision — Today's Class

| Topic                     | Remember                                     |
| ------------------------- | -------------------------------------------- |
| Log Loss                  | Binary classification loss                   |
| Softmax                   | Converts logits into probabilities           |
| One-Hot Encoding          | Categorical to binary representation         |
| Categorical Cross-Entropy | Multi-class loss                             |
| Weights and Bias          | Model parameters                             |
| Polynomial Features       | Create additional features                   |
| Polynomial Degree         | Highest power                                |
| Underfitting              | Model too simple                             |
| Overfitting               | Model too complex                            |
| Optimum Degree            | Balance between underfitting and overfitting |
| Hyperparameter Tuning     | Find suitable settings                       |

## 17. Telugu Meanings

| English term        | Simple Telugu meaning              |
| ------------------- | ---------------------------------- |
| Loss Function       | తప్పును కొలిచే విధానం              |
| Probability         | సంభావ్యత                           |
| One-Hot Encoding    | 0, 1 రూపంలో మార్చడం                |
| Weights             | లక్షణాలకు ఇచ్చే ప్రాముఖ్యత         |
| Bias                | అదనపు స్థిర విలువ                  |
| Polynomial Features | కొత్త గణిత లక్షణాలు సృష్టించడం     |
| Degree              | గరిష్ఠ ఘాతం                        |
| Underfitting        | డేటాను సరిగ్గా నేర్చుకోలేకపోవడం    |
| Overfitting         | ట్రైనింగ్ డేటాను అతిగా నేర్చుకోవడం |
| Hyperparameter      | ముందుగా నిర్ణయించే సెట్టింగ్       |
| Optimum             | సరైన లేదా అనుకూలమైన                |

## Today's learning checklist

- Understand Softmax Regression.
- Practice One-Hot Encoding.
- Derive Categorical Cross-Entropy.
- Understand weights and bias.
- Practice Polynomial Features.
- Understand degree 1, 2 and 3.
- Understand underfitting and overfitting.
- Practice Scikit-learn implementation.

Next: Send your next institute classroom screenshots. I will continue from the next new topic, maintaining this same chapter-wise notes format without repeating today's concepts.