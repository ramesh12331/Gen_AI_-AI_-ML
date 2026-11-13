# 📘 Adjusted R² Score – Machine Learning

## 📌 1. Adjusted R² Score అంటే ఏమిటి?

**Adjusted R² Score (Adjusted R-Squared)** అనేది Regression Model Evaluation Metric.

ఇది మన Regression Model ఎంత బాగా పనిచేస్తుందో అంచనా వేయడానికి ఉపయోగిస్తాం. ముఖ్యంగా మన modelలో ఎన్ని Independent Variables (Features) ఉపయోగించామో కూడా పరిగణనలోకి తీసుకుంటుంది.

### 🎯 సులభంగా చెప్పాలంటే

Adjusted R² అనేది ఈ రెండు విషయాలను పరిగణనలోకి తీసుకుంటుంది:

1. మన model Target Variableలోని variationను ఎంతవరకు explain చేస్తోంది?
2. మన modelలో ఎన్ని features ఉపయోగించాం?

### ముఖ్యమైన విషయాలు

- Adjusted R² ఎక్కువగా ఉంటే సాధారణంగా model fit మెరుగ్గా ఉన్నట్లు అర్థం.
- ఇది modelలోని features సంఖ్యను పరిగణనలోకి తీసుకుంటుంది.
- కొత్త features add చేసినప్పుడు ఇది పెరగవచ్చు లేదా తగ్గవచ్చు.
- Multiple Linear Regressionలో ఎక్కువగా ఉపయోగిస్తారు.

---

## 🧠 2. Adjusted R² ఎందుకు అవసరం?

ఒక Student Marks Prediction Model తయారుచేస్తున్నామనుకుందాం.

Student Marks predict చేయడానికి ఈ features ఉపయోగిస్తున్నాం.

| Feature | వివరణ |
|---|---|
| Study Hours | విద్యార్థి ఎన్ని గంటలు చదువుతున్నాడు |
| Attendance | విద్యార్థి హాజరు శాతం |
| Sleep Hours | విద్యార్థి ఎన్ని గంటలు నిద్రపోతున్నాడు |
| Favorite Color | విద్యార్థికి ఇష్టమైన రంగు |

ఇక్కడ Study Hours, Attendance, Sleep Hours అనేవి Student Marks predictionకు ఉపయోగపడవచ్చు.

కానీ Favorite Color అనేది Student Marks predictionకు ఉపయోగపడకపోవచ్చు.

అయినా Favorite Colorను modelలో add చేస్తే R² Score పెరగవచ్చు లేదా మారకుండా ఉండవచ్చు.

అందుకే Adjusted R² ఉపయోగిస్తాం.

**Adjusted R² అనేది modelలోని features సంఖ్యను పరిగణనలోకి తీసుకొని model performanceను అంచనా వేయడానికి సహాయపడుతుంది.**

---

## 📐 3. Adjusted R² Mathematical Formula

Adjusted R² Formula:

$$
Adjusted\ R^2 =
1-(1-R^2)\frac{n-1}{n-p-1}
$$

### Formula Explanation

| Symbol | అర్థం |
|---|---|
| R² | R-Squared Score |
| n | మొత్తం observations సంఖ్య |
| p | Independent Variables (Features) సంఖ్య |
| 1 | స్థిరమైన విలువ |

### ముఖ్యమైన విషయాలు

- `n` అంటే Datasetలో మొత్తం ఎన్ని rows ఉన్నాయో.
- `p` అంటే Modelలో ఉపయోగించిన Independent Variables సంఖ్య.
- `R²` అంటే R-Squared Score.

---

## 🔢 4. Step-by-Step Numerical Example

ఇప్పుడు ఒక example ద్వారా Adjusted R² calculate చేద్దాం.

### Given Values

```python
R2 Score = 0.90

n = 100

p = 3
```

ఇక్కడ:

- R² = 0.90
- Observations సంఖ్య = 100
- Features సంఖ్య = 3

### Step 1: Formula రాయాలి

$$
Adjusted\ R^2 =
1-(1-R^2)\frac{n-1}{n-p-1}
$$

### Step 2: Values Substitute చేయాలి

$$
Adjusted\ R^2 =
1-(1-0.90)\frac{100-1}{100-3-1}
$$

### Step 3: Simplify చేయాలి

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

**Observation:** ఇక్కడ Adjusted R², R² కంటే కొద్దిగా తక్కువగా ఉంది. ఎందుకంటే ఇది features సంఖ్యను కూడా పరిగణనలోకి తీసుకుంటుంది.

---

## 📊 5. R² మరియు Adjusted R² మధ్య తేడా

| Feature | R² Score | Adjusted R² |
|---|---|---|
| Full Form | R-Squared | Adjusted R-Squared |
| ఉపయోగం | Explained Variationను కొలుస్తుంది | Features సంఖ్యను పరిగణనలోకి తీసుకొని Explained Variationను అంచనా వేస్తుంది |
| Features సంఖ్యను పరిగణనలోకి తీసుకుంటుందా? | Direct penalty ఉండదు | అవును |
| Unnecessary Features add చేస్తే | తగ్గదు (Ordinary Least Squaresలో) | తగ్గవచ్చు |
| ఉపయోగించే సందర్భం | సాధారణ Regression Evaluation | వేర్వేరు Feature Counts ఉన్న Models Comparison |

### ముఖ్యమైన Concept

**R² Score:**

Ordinary Least-Squares Regressionలో కొత్త Independent Variables add చేసినప్పుడు R² Score తగ్గదు.

అది పెరగవచ్చు లేదా మారకుండా ఉండవచ్చు.

**Adjusted R² Score:**

Adjusted R² అనేది Independent Variables సంఖ్యను కూడా పరిగణనలోకి తీసుకుంటుంది.

- కొత్త Feature వల్ల Model Fit తగినంత మెరుగుపడితే Adjusted R² పెరగవచ్చు.
- కొత్త Feature వల్ల తగినంత improvement లేకపోతే Adjusted R² తగ్గవచ్చు.

---

## 💻 6. Python Implementation – Adjusted R²

ఇప్పుడు Python మరియు Scikit-learn ఉపయోగించి Adjusted R² calculate చేద్దాం.

### Step 1: Required Libraries Install చేయాలి

VS Code Terminalలో ఈ command run చేయాలి.

```bash
pip install numpy pandas scikit-learn
```

### Step 2: Required Libraries Import చేయాలి

```python
import numpy as np

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
```

### Step 3: Dataset Create చేయాలి

```python
# Independent Variables (Features)

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


# Dependent Variable (Target)

y = np.array([
    40, 45, 50, 55, 60,
    65, 70, 75, 80, 85
])
```

### Step 4: Linear Regression Model Train చేయాలి

```python
# Create Linear Regression Model

model = LinearRegression()


# Train the Model

model.fit(X, y)
```

### Step 5: Predictions చేయాలి

```python
# Predict Target Values

y_pred = model.predict(X)
```

### Step 6: R² Score Calculate చేయాలి

```python
# Calculate R² Score

r2 = r2_score(y, y_pred)

print("R2 Score:", r2)
```

### Step 7: Adjusted R² Score Calculate చేయాలి

```python
# Number of Observations

n = X.shape[0]


# Number of Independent Variables

p = X.shape[1]


# Calculate Adjusted R²

adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)


print("R2 Score:", r2)

print("Adjusted R2 Score:", adjusted_r2)
```

### ముఖ్యమైన Python Statements వివరణ

**1. Number of Observations**

```python
n = X.shape[0]
```

ఇది Datasetలో ఎన్ని rows ఉన్నాయో తెలియజేస్తుంది.

**2. Number of Features**

```python
p = X.shape[1]
```

ఇది Datasetలో ఎన్ని Independent Variables (Columns) ఉన్నాయో తెలియజేస్తుంది.

**3. Adjusted R² Calculation**

```python
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
```

ఈ statement Adjusted R² mathematical formulaను ఉపయోగించి score calculate చేస్తుంది.

**గమనిక:** ఈ exampleలో సులభంగా అర్థం చేసుకోవడానికి training dataపైనే scores calculate చేస్తున్నాం. నిజమైన model performance తెలుసుకోవడానికి separate test dataset లేదా cross-validation ఉపయోగించడం మంచిది.

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

# Independent Variables (Features)

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


# Dependent Variable (Target)

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

## 🎯 8. Adjusted R² ఎప్పుడు ఉపయోగిస్తాం?

Adjusted R² ముఖ్యంగా Multiple Linear Regressionలో ఉపయోగపడుతుంది.

### Example

మన దగ్గర రెండు Regression Models ఉన్నాయనుకుందాం.

| Model | Features సంఖ్య | R² | Adjusted R² |
|---|---:|---:|---:|
| Model A | 3 | 0.90 | 0.896 |
| Model B | 8 | 0.91 | 0.901 |

Model Bలో ఎక్కువ Features ఉన్నాయి.

అయితే Model Bకి Adjusted R² కూడా ఎక్కువగా ఉంది.

దీని అర్థం అదనంగా చేర్చిన Features వల్ల Model Fit మెరుగుపడినట్లు కనిపిస్తోంది.

**గుర్తుంచుకోండి:** Model selection కోసం Adjusted R² ఒక్కటే ఉపయోగించకూడదు. Test Performance, Cross-Validation మరియు Domain Knowledge కూడా పరిగణనలోకి తీసుకోవాలి.

---

## 🏢 9. Real-World Applications

Adjusted R² అనేది Multiple Features ఉపయోగించే Regression Problemsలో ఉపయోగపడుతుంది.

| Industry | Application |
|---|---|
| Real Estate | House Price Prediction |
| Education | Student Marks Prediction |
| Finance | Revenue Prediction |
| Healthcare | Numerical Health Measurements Prediction |
| Marketing | Sales Forecasting |
| Business | Demand Prediction |

---

## 🎤 10. Interview Questions and Answers

### Q1. What is Adjusted R²?

Adjusted R² అనేది Independent Variables మరియు Observations సంఖ్యను పరిగణనలోకి తీసుకొని Regression Model Performanceను అంచనా వేసే Metric.

### Q2. Why do we use Adjusted R²?

Modelలో ఉపయోగించిన Features సంఖ్యను పరిగణనలోకి తీసుకొని Regression Modelsను Evaluate చేయడానికి ఉపయోగిస్తాం.

### Q3. What is the difference between R² and Adjusted R²?

R² Score కొత్త Features add చేసినప్పుడు నేరుగా penalty విధించదు. Adjusted R² మాత్రం Features సంఖ్యను పరిగణనలోకి తీసుకుంటుంది.

### Q4. Can Adjusted R² decrease?

అవును. కొత్త Feature వల్ల Modelలో తగినంత improvement లేకపోతే Adjusted R² తగ్గవచ్చు.

### Q5. Can Adjusted R² be negative?

అవును. Adjusted R² Negative Value కూడా కావచ్చు.

### Q6. Where is Adjusted R² commonly used?

Multiple Linear Regressionలో సాధారణంగా ఉపయోగిస్తారు.

### Q7. What are n and p in the Adjusted R² formula?

- n = Number of Observations.
- p = Number of Independent Variables.

### Q8. Which is better: R² or Adjusted R²?

రెండింటికీ వాటి ఉపయోగాలు ఉన్నాయి. వేర్వేరు Features సంఖ్య కలిగిన Regression Modelsను compare చేసేటప్పుడు Adjusted R² ఉపయోగపడుతుంది.

---

## 📝 11. Practice Questions

నీకు అర్థమైందో లేదో పరీక్షించుకో.

**Q1. Adjusted R² Formulaలో `p` అంటే ఏమిటి?**

- A) Number of Rows
- B) Number of Features
- C) Number of Predictions
- D) Number of Targets

**Q2. Ordinary Least-Squares Regressionలో Additional Features add చేస్తే R² Score ఏమవుతుంది?**

- A) Always Decreases
- B) Always Becomes Zero
- C) Can Increase or Remain Unchanged
- D) Always Becomes Negative

**Q3. Adjusted R² ఎందుకు ఉపయోగిస్తాం?**

- A) Missing Values Remove చేయడానికి
- B) Number of Featuresను పరిగణనలోకి తీసుకోవడానికి
- C) Data Visualization కోసం
- D) Classification Accuracy కోసం

**Q4. Adjusted R² తగ్గవచ్చా?**

- A) Yes
- B) No

**Q5. Adjusted R² ఏ Regression Modelలో ఎక్కువగా ఉపయోగపడుతుంది?**

- A) Simple Linear Regression
- B) Multiple Linear Regression
- C) Logistic Regression
- D) Decision Tree Classification

---

## 📚 12. Final Summary

| Concept | వివరణ |
|---|---|
| R² Score | Model ఎంత variation explain చేస్తుందో తెలియజేస్తుంది |
| Adjusted R² | Features సంఖ్యను పరిగణనలోకి తీసుకున్న R² |
| n | Observations సంఖ్య |
| p | Independent Variables సంఖ్య |
| Main Purpose | Features సంఖ్యను పరిగణనలోకి తీసుకొని Model Evaluation చేయడం |
| Maximum Value | 1 |
| Negative Value | రావచ్చు |
| Higher Value | సాధారణంగా మెరుగైన Model Fitను సూచిస్తుంది |

### ⭐ Important Formula to Remember

$$
\boxed{
Adjusted\ R^2 =
1-(1-R^2)\frac{n-1}{n-p-1}
}
$$

### 🎉 Congratulations!

మీరు Adjusted R² Score Topic పూర్తి చేశారు.

Regression Evaluation Metricsను ప్రాక్టీస్ చేస్తూ Machine Learning Models Performanceను అర్థం చేసుకోండి.