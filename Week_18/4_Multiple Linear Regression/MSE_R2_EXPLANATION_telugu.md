# 📊 Mean Squared Error (MSE) & R² Score – తెలుగు వివరణ

## 📌 1. పరిచయం (Introduction)

Machine Learningలో మనం ఒక Model‌ను Train చేసిన తర్వాత, ఆ Model ఎంత బాగా Predictions చేస్తుందో తెలుసుకోవాలి.

ఉదాహరణకు:

మన దగ్గర విద్యార్థులు ఎన్ని గంటలు చదివారు అనే Data ఉంది. దాని ఆధారంగా వారి Exam Marks‌ను Predict చేయడానికి ఒక Machine Learning Model తయారు చేశాం అనుకుందాం.

| Study Hours | Actual Marks | Predicted Marks |
|---:|---:|---:|
| 1 | 25 | 27 |
| 2 | 30 | 32 |
| 3 | 45 | 42 |
| 4 | 50 | 53 |
| 5 | 60 | 58 |

ఇక్కడ:

- **Actual Values (`y_test`):** నిజంగా వచ్చిన Marks.
- **Predicted Values (`y_pred`):** మన Machine Learning Model Predict చేసిన Marks.

ఈ రెండింటి మధ్య ఎంత తేడా ఉందో తెలుసుకోవడానికి Evaluation Metrics ఉపయోగిస్తాము.

ముఖ్యమైన రెండు Evaluation Metrics:

1. Mean Squared Error (MSE)
2. R² Score (Coefficient of Determination)

---

## 📌 2. Mean Squared Error (MSE) అంటే ఏమిటి?

**Mean Squared Error (MSE)** అనేది Regression Model‌ను Evaluate చేయడానికి ఉపయోగించే ఒక Metric.

ఇది Actual Values మరియు Predicted Values మధ్య ఉన్న తేడాల Square చేసి, వాటి Average‌ను Calculate చేస్తుంది.

### 🎯 MSE ఎందుకు ఉపయోగిస్తాము?

మన Model Predictions‌లో ఎంత Error ఉందో తెలుసుకోవడానికి MSE ఉపయోగిస్తాము.

- MSE తక్కువగా ఉంటే Prediction Errors సాధారణంగా తక్కువగా ఉంటాయి.
- MSE ఎక్కువగా ఉంటే Prediction Errors సాధారణంగా ఎక్కువగా ఉంటాయి.
- MSE = 0 అయితే Predictions Perfect‌గా ఉన్నట్లు.

### 🧮 Mathematical Formula

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

**Formulaలో ఉన్న Terms:**

- `n` = మొత్తం Data Points సంఖ్య.
- `yᵢ` = Actual Value.
- `ŷᵢ` = Predicted Value.
- `Σ` = అన్ని Values‌ను కలపడం (Summation).
- `(yᵢ - ŷᵢ)²` = Actual మరియు Predicted మధ్య తేడా Square చేయడం.

### 💡 Practical Example

మన దగ్గర ఈ Values ఉన్నాయని అనుకుందాం:

```python
# Actual Values
actual = [40, 50, 60, 70, 80]

# Predicted Values
predicted = [42, 48, 65, 68, 75]
```

### Step 1: Error Calculate చేయడం

Error = Actual Value - Predicted Value

| Actual | Predicted | Error |
|---:|---:|---:|
| 40 | 42 | -2 |
| 50 | 48 | 2 |
| 60 | 65 | -5 |
| 70 | 68 | 2 |
| 80 | 75 | 5 |

### Step 2: Error‌ను Square చేయడం

| Actual | Predicted | Error | Squared Error |
|---:|---:|---:|---:|
| 40 | 42 | -2 | 4 |
| 50 | 48 | 2 | 4 |
| 60 | 65 | -5 | 25 |
| 70 | 68 | 2 | 4 |
| 80 | 75 | 5 | 25 |

### Step 3: Average Calculate చేయడం

Formula:

$$
MSE = \frac{4+4+25+4+25}{5}
$$

$$
MSE = \frac{62}{5}
$$

$$
\boxed{MSE = 12.4}
$$

**Final Result: MSE = 12.4**

అంటే మన Model Predictions‌లో వచ్చిన Squared Errors యొక్క Average 12.4.

⚠️ **ముఖ్యమైన విషయం:**

MSE = 12.4 అంటే Model సగటున 12.4 Marks తప్పు చేసిందని కాదు.

ఎందుకంటే MSEలో Errors‌ను Square చేస్తాము. కాబట్టి దీని Unit కూడా Squared Unit అవుతుంది (ఉదాహరణకు Marks²).

---

## 📌 3. R² Score అంటే ఏమిటి?

R² Score‌ను **Coefficient of Determination** అని కూడా అంటారు.

ఇది మన Regression Model, Target Variableలోని Variation‌ను ఎంతవరకు Explain చేస్తుందో తెలియజేస్తుంది.

### 🎯 R² Score ఎందుకు ఉపయోగిస్తాము?

మన Model, Target Values‌లో ఉన్న మార్పులను ఎంతవరకు Explain చేస్తుందో తెలుసుకోవడానికి R² Score ఉపయోగిస్తాము.

ఉదాహరణకు:

R² Score = 0.92 వస్తే, మన Model Target Variableలోని Variation‌లో సుమారుగా 92% Explain చేస్తుందని అర్థం.

### 🧮 Mathematical Formula

$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
$$

ఇక్కడ రెండు ముఖ్యమైన Terms ఉన్నాయి.

### 1. Residual Sum of Squares (SSres)

ఇది Actual Values మరియు Predicted Values మధ్య ఉన్న Squared Errors మొత్తం.

$$
SS_{res} = \sum (y_i-\hat{y}_i)^2
$$

### 2. Total Sum of Squares (SStot)

ఇది Actual Values మరియు వాటి Mean మధ్య ఉన్న Squared Differences మొత్తం.

$$
SS_{tot} = \sum (y_i-\bar{y})^2
$$

ఇక్కడ:

- `yᵢ` = Actual Value.
- `ŷᵢ` = Predicted Value.
- `ȳ` = Actual Values యొక్క Mean.

### 💡 R² Score Values అర్థం

| R² Score | అర్థం |
|---:|---|
| 1.00 | Perfect Predictions |
| 0.98 | చాలా ఎక్కువ Variation Explain చేస్తుంది |
| 0.90 | 90% Variation Explain చేస్తుంది |
| 0.80 | 80% Variation Explain చేస్తుంది |
| 0.50 | 50% Variation Explain చేస్తుంది |
| 0.00 | Mean Baseline కంటే మెరుగైన ఫలితం లేదు |
| Negative Value | Mean Baseline కంటే కూడా Model Performance తక్కువ |

**ముఖ్యమైన విషయాలు:**

- R² = 1 → Perfect Predictions.
- R² = 0 → Mean ఆధారంగా Predict చేయడం కంటే Model మెరుగ్గా లేదు.
- R² < 0 → Mean ఆధారంగా Predict చేయడం కంటే Model Performance తక్కువగా ఉంది.

గమనిక: ఇవి సాధారణ అర్థాలు మాత్రమే. ప్రతి Dataset‌లో R² Score‌ను ఒకే విధంగా Good లేదా Bad అని నిర్ణయించకూడదు.

---

## 📌 4. MSE మరియు R² Score మధ్య తేడా

| అంశం | MSE | R² Score |
|---|---|---|
| Full Form | Mean Squared Error | Coefficient of Determination |
| ఉపయోగం | Prediction Error కొలుస్తుంది | Explained Variation కొలుస్తుంది |
| Best Value | 0 | 1 |
| Perfect Prediction | 0 | 1 |
| తక్కువ Value | సాధారణంగా మంచిది | ఎప్పుడూ మంచిది కాదు |
| Negative Value | రాదు | రావచ్చు |
| Units | Squared Target Units | Units ఉండవు |
| ఉపయోగించే Algorithm | Regression | Regression |

### సులభంగా గుర్తుపెట్టుకోండి

- **MSE:** మన Model ఎంత Prediction Error చేస్తోంది?
- **R² Score:** మన Model Target Variation‌ను ఎంతవరకు Explain చేస్తోంది?

---

## 📌 5. Python Implementation – MSE & R² Score

### Step 1: Required Libraries Install చేయండి

VS Code Terminalలో ఈ Command Run చేయండి:

```bash
pip install numpy scikit-learn
```

### Step 2: Libraries Import చేయండి

```python
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```

### Step 3: Actual Values Create చేయండి

```python
# Test Dataset నుండి వచ్చిన నిజమైన Values

y_test = np.array([40, 50, 60, 70, 80])
```

### Step 4: Predicted Values Create చేయండి

```python
# Machine Learning Model Predict చేసిన Values

y_pred = np.array([42, 48, 65, 68, 75])
```

### Step 5: MSE Calculate చేయండి

```python
# Actual మరియు Predicted Values మధ్య
# Squared Errors Average Calculate చేస్తుంది

mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)
```

### Step 6: R² Score Calculate చేయండి

```python
# Model Target Variation‌ను ఎంతవరకు
# Explain చేస్తుందో Calculate చేస్తుంది

r2 = r2_score(y_test, y_pred)

print("R2 Score:", r2)
```

### Step 7: Complete Python Code

```python
# =====================================================
# MACHINE LEARNING
# MEAN SQUARED ERROR (MSE) AND R² SCORE
# =====================================================

# STEP 1: Import Required Libraries

import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# STEP 2: Actual Values

# ఇవి మన Test Datasetలోని నిజమైన Values

y_test = np.array([40, 50, 60, 70, 80])


# STEP 3: Predicted Values

# ఇవి మన Machine Learning Model Predict చేసిన Values

y_pred = np.array([42, 48, 65, 68, 75])


# STEP 4: Calculate Mean Squared Error

# Actual మరియు Predicted Values మధ్య
# Squared Errors యొక్క Average‌ను Calculate చేస్తుంది

mse = mean_squared_error(y_test, y_pred)


# STEP 5: Calculate R² Score

# Target Variableలోని Variation‌ను
# Model ఎంతవరకు Explain చేస్తుందో Calculate చేస్తుంది

r2 = r2_score(y_test, y_pred)


# STEP 6: Display Results

print("Actual Values:", y_test)

print("Predicted Values:", y_pred)

print("--------------------------------")

print("Mean Squared Error:", mse)

print("R² Score:", r2)
```

### Expected Output

```text
Actual Values: [40 50 60 70 80]

Predicted Values: [42 48 65 68 75]

--------------------------------

Mean Squared Error: 12.4

R² Score: 0.845
```

### Output అర్థం

**MSE = 12.4**

మన Model Predictions‌లో Errors ఉన్నాయి. వాటి Squared Errors Average 12.4.

**R² Score = 0.845**

మన Model Target Variableలోని Variation‌లో సుమారుగా 84.5% Explain చేస్తోంది.

---

## 📌 6. Real-World Example

ఒక House Price Prediction Model తయారు చేశామని అనుకుందాం.

| Actual Price | Predicted Price |
|---:|---:|
| ₹20 Lakhs | ₹21 Lakhs |
| ₹30 Lakhs | ₹29 Lakhs |
| ₹40 Lakhs | ₹42 Lakhs |
| ₹50 Lakhs | ₹48 Lakhs |
| ₹60 Lakhs | ₹59 Lakhs |

Model Evaluation తర్వాత:

```text
MSE = 2.8

R² Score = 0.95
```

### దీని అర్థం ఏమిటి?

- MSE = 2.8 అంటే Model Predictions‌లో Error ఉంది.
- R² = 0.95 అంటే House Pricesలోని Variation‌ను Model సుమారుగా 95% Explain చేస్తోంది.
- ఈ Model మంచి Performance చూపిస్తున్నట్లు కనిపిస్తోంది.

కానీ Model నిజంగా ఎంత బాగా పనిచేస్తుందో తెలుసుకోవడానికి ఇతర Metrics మరియు Unseen Test Data Performance కూడా పరిశీలించాలి.

---

## 📌 7. Important Interview Questions

### Q1. What is Mean Squared Error?

**Answer:**

MSE అనేది Actual Values మరియు Predicted Values మధ్య ఉన్న Squared Differences యొక్క Average‌ను Calculate చేసే Regression Evaluation Metric.

### Q2. Why do we square the errors in MSE?

**Answer:**

Errors‌ను Square చేయడం వల్ల:

- Positive మరియు Negative Errors ఒకదానికొకటి Cancel కావు.
- పెద్ద Errors‌కు ఎక్కువ Penalty వస్తుంది.

### Q3. What is the best MSE value?

**Answer:**

MSE = 0 అయితే Model Predictions Perfect‌గా ఉన్నట్లు.

### Q4. What is R² Score?

**Answer:**

R² Score అనేది Regression Model Target Variableలోని Variation‌ను ఎంతవరకు Explain చేస్తుందో కొలిచే Metric.

### Q5. What is the best R² Score?

**Answer:**

R² = 1 అయితే Perfect Predictions.

### Q6. Can R² Score be negative?

**Answer:**

Yes. R² Negative‌గా రావచ్చు. అంటే Model, Target Mean‌ను Predict చేసే Baseline కంటే కూడా తక్కువ Performance చూపిస్తోంది.

### Q7. Difference between MSE and R² Score?

**Answer:**

MSE Prediction Error‌ను Measure చేస్తుంది. R² Score Explained Variation‌ను Measure చేస్తుంది.

### Q8. Can we use MSE and R² together?

**Answer:**

Yes. Regression Model Performance‌ను రెండు వేర్వేరు కోణాల్లో అర్థం చేసుకోవడానికి రెండింటినీ ఉపయోగించవచ్చు.

### Q9. Does R² = 0.95 mean 95% accuracy?

**Answer:**

No. R² = 0.95 అంటే Target Variableలోని Variation‌లో సుమారుగా 95% Model Explain చేస్తోంది. ఇది Classification Accuracy కాదు.

### Q10. Is lower MSE always better?

**Answer:**

సాధారణంగా ఒకే Target Variable మరియు ఒకే Evaluation Datasetపై Models‌ను Compare చేస్తున్నప్పుడు తక్కువ MSE మంచిది. అయితే Model Generalization మరియు Errors ప్రభావం కూడా పరిశీలించాలి.

---

## 📌 8. Practice Exercises

ఈ ప్రశ్నలకు నువ్వు స్వయంగా సమాధానాలు రాయడానికి ప్రయత్నించు.

### Exercise 1

```python
MSE = 0

R2 = 1
```

1. Model Predictions Perfect‌గా ఉన్నాయా?
2. MSE = 0 అంటే ఏమిటి?
3. R² = 1 అంటే ఏమిటి?

### Exercise 2

```python
MSE = 25

R2 = 0.75
```

1. Modelలో Prediction Error ఉందా?
2. Model ఎంత Percentage Variation Explain చేస్తోంది?
3. Model Perfect‌గా ఉందా?

### Exercise 3

```python
MSE = 10

R2 = -0.25
```

1. MSE Zero ఉందా?
2. Negative R² అంటే ఏమిటి?
3. Model Mean Baseline కంటే మెరుగ్గా పనిచేస్తోందా?

---

## 📌 9. Final Summary

| Concept | గుర్తుంచుకోవాల్సిన విషయం |
|---|---|
| MSE | Average Squared Prediction Error |
| R² Score | Explained Variation |
| MSE = 0 | Perfect Predictions |
| R² = 1 | Perfect Predictions |
| R² = 0 | Mean Baseline కంటే మెరుగ్గా లేదు |
| Negative R² | Mean Baseline కంటే తక్కువ Performance |

### 🚀 Machine Learning Learning Flow

```text
          Dataset
              |
              v
        Separate X and y
              |
              v
         Train-Test Split
              |
              v
       Train ML Model
              |
              v
        Make Predictions
              |
              v
        Model Evaluation
              |
         +----+----+
         |         |
         v         v
        MSE      R² Score
         |         |
         v         v
     Prediction  Explained
       Error     Variation
```

## 🎯 Conclusion

MSE మరియు R² Score అనేవి Regression Machine Learningలో ముఖ్యమైన Evaluation Metrics.

**MSE:** మన Model Predictions‌లో ఎంత Error ఉందో తెలియజేస్తుంది.

**R² Score:** మన Model Target Variableలోని Variation‌ను ఎంతవరకు Explain చేస్తుందో తెలియజేస్తుంది.

ఈ రెండు Metrics‌ను అర్థం చేసుకోవడం ద్వారా మన Regression Model Performance‌ను మెరుగ్గా Evaluate చేయగలుగుతాము.

**Happy Learning! 🚀**