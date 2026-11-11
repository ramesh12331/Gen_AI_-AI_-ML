# Machine Learning Mathematics — Probability & Standardization

![Machine Learning](https://img.shields.io/badge/Subject-Machine%20Learning-blue)
![Mathematics](https://img.shields.io/badge/Topic-Mathematics-purple)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen)

> Institute class notes — **11 November 2026**  
> Topics: Probability, Independent Events, Dependent Events, Conditional Probability, Bayes' Theorem, Naive Bayes, Feature Scaling and Standardization.

---

## 📚 Table of Contents

- [Part 1 — Probability](#part-1--probability)
- [Part 2 — Types of Events](#part-2--types-of-events)
- [Part 3 — Conditional Probability](#part-3--conditional-probability)
- [Part 4 — Bayes' Theorem](#part-4--bayes-theorem)
- [Part 5 — Naive Bayes Algorithm](#part-5--naive-bayes-algorithm)
- [Part 6 — Feature Scaling](#part-6--feature-scaling)
- [Part 7 — Standardization](#part-7--standardization)
- [Part 8 — Interview Questions](#part-8--interview-questions)
- [Part 9 — Practice Test](#part-9--practice-test)
- [Part 10 — Quick Revision](#part-10--quick-revision)

---

# PART 1 — PROBABILITY

## 1. What is Probability?

### Definition

**Probability** is a mathematical concept used to measure the possibility of an event happening.

**Simple meaning:** ఒక సంఘటన జరిగే అవకాశం ఎంత ఉందో Probability చెబుతుంది.

### Real-world examples

- Tossing a coin → Head or Tail.
- Rolling a dice → Getting 1, 2, 3, 4, 5 or 6.
- Weather → Possibility of rain.
- Machine Learning → Probability of an email being spam.

### Probability Formula

$$
\\boxed{
P(A)=\\frac{\\text{Favourable Outcomes}}{\\text{Total Possible Outcomes}}
}
$$

Where:

- $P$ = Probability.
- $A$ = Event.
- Favourable Outcomes = మనకు కావలసిన ఫలితాలు.
- Total Possible Outcomes = మొత్తం సాధ్యమైన ఫలితాలు.

### Example 1 — Toss a Coin

When we toss a coin, there are two possible outcomes:

1. Head (H)
2. Tail (T)

Probability of getting Head:

$$P(H)=\\frac{1}{2}=0.5=50\\%$$

Probability of getting Tail:

$$P(T)=\\frac{1}{2}=0.5=50\\%$$

### Example 2 — Roll a Dice

A fair dice has six possible outcomes:

$$S=\\{1,2,3,4,5,6\\}$$

Probability of getting 6:

$$P(6)=\\frac{1}{6}$$

Probability of getting 4:

$$P(4)=\\frac{1}{6}$$

Probability of getting 1:

$$P(1)=\\frac{1}{6}$$

**Important:** ఒక fair diceలో ప్రతి సంఖ్య వచ్చే అవకాశం సమానంగా ఉంటుంది.

### Probability Range

$$0\\leq P(A)\\leq 1$$

| Probability | Meaning |
|---:|---|
| 0 | Impossible event |
| 0.25 | 25% chance |
| 0.5 | 50% chance |
| 0.75 | 75% chance |
| 1 | Certain event |

---

# PART 2 — TYPES OF EVENTS

## 2. Independent Events

### Definition

Two events are called **Independent Events** when the occurrence of one event does not affect the probability of another event.

**Simple meaning:** ఒక సంఘటన జరిగిందని రెండవ సంఘటన జరిగే అవకాశం మారదు.

### Example — Tossing a Coin Twice

First toss:

$$P(H_1)=\\frac{1}{2}$$

Second toss:

$$P(H_2)=\\frac{1}{2}$$

Getting Head in the first toss does not affect the second toss. Therefore, these are independent events.

### Independent Events Formula

$$\\boxed{P(A\\cap B)=P(A)\\times P(B)}$$

Where:

- $A$ = First event.
- $B$ = Second event.
- $A\\cap B$ = Both events happen.

### Practical Example — Head in Both Tosses

$$P(H_1)=\\frac{1}{2}$$

$$P(H_2)=\\frac{1}{2}$$

Apply the formula:

$$
P(H_1\\cap H_2)=\\frac{1}{2}\\times\\frac{1}{2}
$$

$$\\boxed{P(H_1\\cap H_2)=\\frac{1}{4}=25\\%}$$

---

## 3. Dependent Events

### Definition

Two events are called **Dependent Events** when the occurrence of one event affects the probability of another event.

**Simple meaning:** మొదటి సంఘటన జరిగిన తర్వాత రెండవ సంఘటన జరిగే అవకాశం మారుతుంది.

### Example — Deck of Cards

A standard deck contains 52 cards:

- 26 Red cards.
- 26 Black cards.

Suppose we draw two cards **without replacement**.

**First draw:** Probability of getting a Red card.

$$P(A)=\\frac{26}{52}=\\frac{1}{2}$$

After taking one Red card, only 51 cards remain.

**Second draw:** Probability of getting another Red card, given that the first card was Red.

$$P(B|A)=\\frac{25}{51}$$

### Dependent Events Formula

$$\\boxed{P(A\\cap B)=P(A)\\times P(B|A)}$$

Substitute the values:

$$
P(A\\cap B)=\\frac{26}{52}\\times\\frac{25}{51}
$$

$$=\\frac{25}{102}$$

**Answer:** Approximately 24.51%.

### Independent vs Dependent Events

| Independent Events | Dependent Events |
|---|---|
| One event does not affect another | One event affects another |
| Example: separate coin tosses | Example: cards without replacement |
| Probability remains unchanged | Probability changes |
| $P(A)P(B)$ | $P(A)P(B\\mid A)$ |

**Important:** Cards drawn with replacement are generally independent, assuming the deck is shuffled randomly each time.

---

# PART 3 — CONDITIONAL PROBABILITY

## 4. What is Conditional Probability?

### Definition

**Conditional Probability** is the probability of an event occurring, given that another event has already occurred.

**Simple meaning:** ఒక సంఘటన ఇప్పటికే జరిగిందని తెలిసినప్పుడు, మరొక సంఘటన జరిగే అవకాశం ఎంత?

### Formula

$$\\boxed{P(A|B)=\\frac{P(A\\cap B)}{P(B)}}$$

Where:

- $P(A|B)$ = Probability of A given B.
- $P(A\\cap B)$ = Probability of both A and B.
- $P(B)$ = Probability of B.

### Example — Students and Exams

Suppose a class has 100 students:

- 60 students passed.
- 40 students failed.
- Out of 60 passed students, 30 have good attendance.
- 50 students have good attendance in total.

Find the probability that a student passed, given that the student has good attendance.

Given:

$$P(Passed\\cap GoodAttendance)=\\frac{30}{100}$$

$$P(GoodAttendance)=\\frac{50}{100}$$

Apply the formula:

$$
P(Passed|GoodAttendance)
=\\frac{30/100}{50/100}
$$

$$=\\frac{30}{50}=0.6$$

**Answer: 60%**

### Important Difference

$$P(A|B)\\neq P(B|A)$$

These two probabilities are not generally equal.

Example:

- $P(Passed|GoodAttendance)$: Probability of passing when attendance is good.
- $P(GoodAttendance|Passed)$: Probability of good attendance when the student passed.

They answer different questions.

---

# PART 4 — BAYES' THEOREM

## 5. What is Bayes' Theorem?

### Definition

**Bayes' Theorem** is a mathematical method used to calculate the probability of an event based on previously known information or evidence.

**Simple meaning:** కొత్త సమాచారం వచ్చినప్పుడు మన probabilityని ఎలా update చేయాలో Bayes' Theorem చెబుతుంది.

### Bayes' Theorem Formula

$$\\boxed{P(A|B)=\\frac{P(A)\\times P(B|A)}{P(B)}}$$

Where:

- $P(A)$ = Prior Probability.
- $P(B|A)$ = Likelihood.
- $P(B)$ = Evidence.
- $P(A|B)$ = Posterior Probability.

### Understanding the Terms

| Term | Meaning |
|---|---|
| Prior | Evidence రాకముందు ఉన్న probability |
| Likelihood | A జరిగినప్పుడు B వచ్చే probability |
| Evidence | B జరిగే మొత్తం probability |
| Posterior | Evidence తర్వాత update అయిన probability |

---

## 6. Bayes' Theorem — Derivation

We already know the conditional probability formula:

$$P(A|B)=\\frac{P(A\\cap B)}{P(B)}$$

We also know:

$$P(A\\cap B)=P(A)\\times P(B|A)$$

Substitute into the first equation:

$$
P(A|B)=\\frac{P(A)\\times P(B|A)}{P(B)}
$$

Therefore:

$$\\boxed{P(A|B)=\\frac{P(A)P(B|A)}{P(B)}}$$

This is **Bayes' Theorem**.

---

## 7. Real-world Example — Medical Test

Suppose:

- 1% of people have a particular disease.
- A test correctly identifies 90% of people who have the disease.
- 5% of healthy people also receive a positive result.

Find the probability that a person actually has the disease given that their test result is positive.

Let:

- $A$ = Person has disease.
- $B$ = Test is positive.

Given:

$$P(A)=0.01$$

$$P(B|A)=0.90$$

$$P(B|A^c)=0.05$$

### Step 1 — Calculate the probability of a positive test

$$
P(B)=P(A)P(B|A)+P(A^c)P(B|A^c)
$$

$$=(0.01\\times0.90)+(0.99\\times0.05)$$

$$=0.009+0.0495$$

$$P(B)=0.0585$$

### Step 2 — Apply Bayes' Theorem

$$
P(A|B)=\\frac{0.01\\times0.90}{0.0585}
$$

$$=\\frac{0.009}{0.0585}$$

$$\\boxed{P(A|B)\\approx0.1538=15.38\\%}$$

**Answer: Approximately 15.38%.**

**Understanding:** Test positive వచ్చినంత మాత్రాన వ్యాధి ఉన్నట్లు నిర్ధారించలేము. ముందుగా వ్యాధి వచ్చే అవకాశం ఎంత తక్కువగా ఉందో కూడా పరిగణించాలి.

---

# PART 5 — NAIVE BAYES ALGORITHM

## 8. What is Naive Bayes?

### Definition

**Naive Bayes** is a supervised Machine Learning classification algorithm based on Bayes' Theorem.

It assumes that features are **conditionally independent of each other given the class**.

**Simple meaning:** ప్రతి featureని మిగతా features నుండి స్వతంత్రంగా పరిగణించి, ఒక class probabilityని calculate చేస్తుంది.

### Real-world Example — Student Result Prediction

Suppose we want to predict whether a student will pass or fail.

Features:

- CGPA
- IQ

Target classes:

- Passed
- Not Passed

Our objective:

$$P(Passed|CGPA,IQ)$$

We want to calculate the probability of passing using CGPA and IQ information.

### Naive Bayes Formula

For two features:

$$
\\boxed{
P(Y|X_1,X_2)=
\\frac{P(Y)\\times P(X_1|Y)\\times P(X_2|Y)}
{P(X_1,X_2)}
}
$$

Where:

- $Y$ = Target class.
- $X_1$ = First feature (CGPA).
- $X_2$ = Second feature (IQ).
- $P(Y)$ = Prior.
- $P(X_1|Y),P(X_2|Y)$ = Conditional probabilities.

For classification, the denominator is common to all classes for the same input. Therefore, we can compare:

$$
\\boxed{
P(Y|X_1,X_2)\\propto P(Y)P(X_1|Y)P(X_2|Y)
}
$$

### Naive Bayes Architecture

```text
Input Features
   |           |
  CGPA         IQ
   |           |
   +-----+-----+
         |
         v
  Naive Bayes Classifier
         |
         v
 Apply Bayes' Theorem and
 conditional independence
         |
     +---+---+
     |       |
     v       v
  Passed   Not Passed
 Probability Probability
     |       |
     +---+---+
         |
         v
 Choose class with highest probability
```

### Why is it called Naive Bayes?

- **Naive** = Assumes conditional independence between features.
- **Bayes** = Uses Bayes' Theorem.

**Important:** Real-world features may be correlated. Naive Bayes still uses this simplifying assumption, which often makes the algorithm computationally efficient.

---

## 9. Naive Bayes — Practical Python Example

### Code

```python
from sklearn.naive_bayes import GaussianNB

# Training data: [CGPA, IQ]
X = [
    [8.5, 120],
    [7.5, 110],
    [5.0, 80],
    [4.0, 70],
    [9.0, 130],
    [3.5, 60]
]

# 1 = Passed, 0 = Not Passed
y = [1, 1, 0, 0, 1, 0]

# Create model
model = GaussianNB()

# Train model
model.fit(X, y)

# New student: CGPA = 8, IQ = 115
prediction = model.predict([[8, 115]])

# Probability of each class
probability = model.predict_proba([[8, 115]])

print("Prediction:", prediction)
print("Probabilities:", probability)
```

> **Note:** These are illustrative training values for learning Python, not a real student dataset.

### Types of Naive Bayes

| Type | Usage |
|---|---|
| Gaussian Naive Bayes | Continuous numerical data |
| Multinomial Naive Bayes | Text counts, word frequencies |
| Bernoulli Naive Bayes | Binary features (0/1) |

Examples:

- Email Spam Detection → Multinomial Naive Bayes.
- Document Classification → Multinomial Naive Bayes.
- Binary feature classification → Bernoulli Naive Bayes.
- Numerical measurements → Gaussian Naive Bayes.

---

# PART 6 — FEATURE SCALING

## 10. What is Feature Scaling?

### Definition

**Feature Scaling** is a preprocessing technique used to bring numerical features into a similar scale or range.

**Simple meaning:** Different columnsలో numbers చాలా పెద్దగా, చిన్నగా ఉన్నప్పుడు వాటిని ఒకే విధమైన scaleలోకి మార్చడం.

### Real-world Example — Credit Score Dataset

| Student | Age | Credit Score | Salary |
|---|---:|---:|---:|
| A | 25 | 750 | 30,000 |
| B | 30 | 800 | 45,000 |
| C | 35 | 850 | 60,000 |

Observe:

- Age values: 25–35.
- Credit Score values: 750–850.
- Salary values: 30,000–60,000.

The numerical ranges are different. Some ML algorithms are sensitive to these differences.

**Feature Scaling** helps make the features comparable.

---

## 11. Types of Feature Scaling

There are two important methods:

1. **Normalization (Min-Max Scaling)**
2. **Standardization (Z-Score Scaling)**

| Normalization | Standardization |
|---|---|
| Usually converts values into 0 to 1 | Uses mean and standard deviation |
| Uses minimum and maximum | Uses mean and standard deviation |
| Formula uses range | Formula uses Z-score |
| Sensitive to outliers | Also affected by outliers |

---

# PART 7 — STANDARDIZATION

## 12. What is Standardization?

### Definition

**Standardization** is a feature scaling technique that transforms numerical data so that it has:

- Mean = 0
- Standard Deviation = 1

**Simple meaning:** Dataలోని valuesని మార్చి, average 0గా మరియు standard deviation 1గా ఉండేలా చేస్తుంది.

### Important Formula

$$\\boxed{Z=\\frac{X-\\mu}{\\sigma}}$$

Where:

- $X$ = Original value.
- $\\mu$ = Mean.
- $\\sigma$ = Standard Deviation.
- $Z$ = Standardized value (Z-score).

### Understanding Each Term

| Symbol | Meaning | Telugu |
|---|---|---|
| $X$ | Original value | అసలు విలువ |
| $\\mu$ | Mean | సగటు |
| $\\sigma$ | Standard Deviation | ప్రామాణిక విచలనం |
| $Z$ | Z-score | Standardized value |

---

## 13. Standardization — Mathematical Example

Suppose we have the following values:

$$X=[10,20,30,40,50]$$

### Step 1 — Calculate Mean

Mean formula:

$$\\mu=\\frac{\\sum X}{N}$$

Substitute:

$$\\mu=\\frac{10+20+30+40+50}{5}$$

$$\\boxed{\\mu=30}$$

### Step 2 — Calculate Standard Deviation

Population Standard Deviation formula:

$$\\sigma=\\sqrt{\\frac{\\sum(X-\\mu)^2}{N}}$$

First calculate deviations:

| X | X − Mean | (X − Mean)² |
|---:|---:|---:|
| 10 | -20 | 400 |
| 20 | -10 | 100 |
| 30 | 0 | 0 |
| 40 | 10 | 100 |
| 50 | 20 | 400 |
| **Total** | **0** | **1000** |

Now:

$$\\sigma=\\sqrt{\\frac{1000}{5}}$$

$$=\\sqrt{200}$$

$$\\boxed{\\sigma\\approx14.142}$$

### Step 3 — Apply Standardization

$$Z=\\frac{X-\\mu}{\\sigma}$$

For $X=10$:

$$Z=\\frac{10-30}{14.142}=-1.414$$

For $X=20$:

$$Z=\\frac{20-30}{14.142}=-0.707$$

For $X=30$:

$$Z=\\frac{30-30}{14.142}=0$$

For $X=40$:

$$Z=\\frac{40-30}{14.142}=0.707$$

For $X=50$:

$$Z=\\frac{50-30}{14.142}=1.414$$

### Final Standardized Dataset

| Original X | Standardized Z |
|---:|---:|
| 10 | -1.414 |
| 20 | -0.707 |
| 30 | 0 |
| 40 | 0.707 |
| 50 | 1.414 |

**Result:** Mean = 0, Standard Deviation = 1 (approximately, subject to rounding).

### How to Understand Z-score?

- $Z=0$ → Value is equal to the mean.
- $Z=+1$ → Value is one standard deviation above the mean.
- $Z=-1$ → Value is one standard deviation below the mean.
- $Z=+2$ → Value is two standard deviations above the mean.

**Remember:** A negative Z-score does not mean a negative original value. It means the value is below the mean.

---

## 14. Standardization Using Python

We use `StandardScaler` from Scikit-learn.

### Code

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Original dataset
X = np.array([
    [10],
    [20],
    [30],
    [40],
    [50]
])

# Create StandardScaler
scaler = StandardScaler()

# Apply standardization
X_scaled = scaler.fit_transform(X)

print("Original Data:")
print(X)

print("Standardized Data:")
print(X_scaled)

print("Mean:")
print(scaler.mean_)

print("Standard Deviation:")
print(scaler.scale_)
```

### Important Methods

| Method | Purpose |
|---|---|
| `StandardScaler()` | Create scaler object |
| `fit()` | Calculate mean and standard deviation |
| `transform()` | Apply standardization |
| `fit_transform()` | Calculate and transform together |

### Important ML Practice — Avoid Data Leakage

When working with training and testing data:

```python
# Fit only on training data
scaler.fit(X_train)

# Transform training data
X_train_scaled = scaler.transform(X_train)

# Transform testing data using the same scaler
X_test_scaled = scaler.transform(X_test)
```

**Why?** We should not use test data to calculate the training mean and standard deviation. Doing so can cause **data leakage**.

### Which Algorithms Benefit from Standardization?

| Algorithm | Standardization |
|---|---|
| Linear Regression | Often useful |
| Logistic Regression | Often useful |
| KNN | Important |
| K-Means | Important |
| SVM | Important |
| PCA | Important |
| Decision Tree | Usually not required |
| Random Forest | Usually not required |

---

# PART 8 — INTERVIEW QUESTIONS

## 15. Important Questions and Answers

<details>
<summary><strong>Q1. What is Probability?</strong></summary>

Probability measures the likelihood of an event occurring.
</details>

<details>
<summary><strong>Q2. What are Independent Events?</strong></summary>

Events where the occurrence of one event does not affect another event.
</details>

<details>
<summary><strong>Q3. What are Dependent Events?</strong></summary>

Events where one event affects the probability of another event.
</details>

<details>
<summary><strong>Q4. What is Conditional Probability?</strong></summary>

Probability of an event occurring when another event has already occurred.
</details>

<details>
<summary><strong>Q5. What is Bayes' Theorem?</strong></summary>

A mathematical theorem used to update probabilities based on new evidence.
</details>

<details>
<summary><strong>Q6. What is Prior Probability?</strong></summary>

The probability of an event before considering new evidence.
</details>

<details>
<summary><strong>Q7. What is Posterior Probability?</strong></summary>

The updated probability after considering new evidence.
</details>

<details>
<summary><strong>Q8. What is Naive Bayes?</strong></summary>

A supervised classification algorithm based on Bayes' Theorem and conditional independence assumptions.
</details>

<details>
<summary><strong>Q9. Why is Naive Bayes called Naive?</strong></summary>

Because it assumes features are conditionally independent given the class.
</details>

<details>
<summary><strong>Q10. What is Feature Scaling?</strong></summary>

A preprocessing technique used to bring numerical features to comparable scales.
</details>

<details>
<summary><strong>Q11. What is Standardization?</strong></summary>

A scaling technique that transforms data to have mean 0 and standard deviation 1.
</details>

<details>
<summary><strong>Q12. What is Z-score?</strong></summary>

It tells us how many standard deviations a value is away from the mean.
</details>

<details>
<summary><strong>Q13. What is the difference between Normalization and Standardization?</strong></summary>

Normalization generally scales values to a fixed range, while standardization uses the mean and standard deviation.
</details>

---

# PART 9 — INTERACTIVE PRACTICE TEST

## 16. Probability & Standardization Quiz

Try to answer before opening the answers.

<details>
<summary><strong>1. What is the probability of getting Head when tossing a fair coin?</strong></summary>

- 1/4
- **1/2**
- 1/6
</details>

<details>
<summary><strong>2. Which formula represents independent events?</strong></summary>

- **P(A) × P(B)**
- P(A) + P(B)
- P(A) / P(B)
</details>

<details>
<summary><strong>3. Which formula is used for dependent events?</strong></summary>

- P(A) × P(B)
- **P(A) × P(B|A)**
- P(A) / P(B)
</details>

<details>
<summary><strong>4. What is the formula for Bayes' Theorem?</strong></summary>

- P(A) × P(B)
- **P(A|B) = P(A)P(B|A)/P(B)**
- (X - Mean) / Std
</details>

<details>
<summary><strong>5. Which algorithm uses Bayes' Theorem?</strong></summary>

- K-Means
- **Naive Bayes**
- Linear Regression
</details>

<details>
<summary><strong>6. What is the mean after standardization?</strong></summary>

- 1
- 100
- **0**
</details>

<details>
<summary><strong>7. What is the standard deviation after standardization?</strong></summary>

- 0
- **1**
- 10
</details>

<details>
<summary><strong>8. Which algorithm generally needs feature scaling?</strong></summary>

- **KNN**
- Decision Tree
- Random Forest
</details>

---

# PART 10 — QUICK REVISION

## 17. Important Formulas

| Topic | Important formula / concept |
|---|---|
| Probability | Favourable Outcomes / Total Possible Outcomes |
| Independent Events | $P(A)P(B)$ |
| Dependent Events | $P(A)P(B\\mid A)$ |
| Conditional Probability | $P(A\\cap B)/P(B)$ |
| Bayes' Theorem | $P(A)P(B\\mid A)/P(B)$ |
| Naive Bayes | Bayes + Conditional Independence |
| Standardization | $(X-\\mu)/\\sigma$ |
| Standardized Mean | 0 |
| Standardized Standard Deviation | 1 |

## 18. Telugu English Vocabulary

| English | Telugu meaning |
|---|---|
| Probability | సంభావ్యత |
| Event | సంఘటన |
| Independent | స్వతంత్రమైన |
| Dependent | ఆధారపడిన |
| Conditional | షరతులతో కూడిన |
| Evidence | ఆధారం |
| Prior | ముందస్తు సంభావ్యత |
| Posterior | నవీకరించిన సంభావ్యత |
| Likelihood | సంభవించే అవకాశం |
| Standardization | ప్రామాణీకరణ |
| Mean | సగటు |
| Standard Deviation | ప్రామాణిక విచలనం |

---

## ✅ Today's Class Checklist

- [ ] Probability basics
- [ ] Independent Events
- [ ] Dependent Events
- [ ] Conditional Probability
- [ ] Bayes' Theorem and derivation
- [ ] Naive Bayes algorithm
- [ ] Feature Scaling
- [ ] Standardization mathematical calculation
- [ ] StandardScaler practical
- [ ] Interview questions

## 🎯 Recommended Formula Practice

Today's class notes recommend practising these three formula groups:

1. **Independent and Dependent Events**
2. **Bayes' Theorem**
3. **Standardization Z-score**

Understanding these gives you a foundation in Probability and Feature Scaling for Machine Learning.
