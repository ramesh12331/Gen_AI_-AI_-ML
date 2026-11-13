# 📊 Mean Absolute Error (MAE) – తెలుగు వివరణ

## 📌 1. Introduction (పరిచయం)

Machine Learningలో మనం ఒక Model‌ను Train చేసిన తర్వాత, ఆ Model ఎంత బాగా Predictions చేస్తుందో తెలుసుకోవాలి.

ఉదాహరణకు:

ఒక Machine Learning Model విద్యార్థుల Study Hours ఆధారంగా వారి Exam Marks‌ను Predict చేస్తోందని అనుకుందాం.

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

ఈ రెండు Values మధ్య ఎంత తేడా ఉందో తెలుసుకోవడానికి MAE ఉపయోగిస్తాము.

---

## 📌 2. What is Mean Absolute Error (MAE)?

**Mean Absolute Error (MAE)** అనేది Regression Model‌ను Evaluate చేయడానికి ఉపయోగించే ఒక Evaluation Metric.

ఇది Actual Values మరియు Predicted Values మధ్య ఉన్న Absolute Differences యొక్క Average‌ను Calculate చేస్తుంది.

### 🎯 MAE ఎందుకు ఉపయోగిస్తాము?

మన Machine Learning Model Predictions‌లో సగటున ఎంత Error వస్తుందో తెలుసుకోవడానికి MAE ఉపయోగిస్తాము.

**ముఖ్యమైన విషయాలు:**

- MAE తక్కువగా ఉంటే సాధారణంగా Predictions మెరుగ్గా ఉంటాయి.
- MAE ఎక్కువగా ఉంటే Prediction Errors ఎక్కువగా ఉంటాయి.
- MAE = 0 అయితే Perfect Predictions.
- MAEలో Errors‌ను Square చేయము.
- Error‌కు Absolute Value తీసుకుంటాము.

---

## 📌 3. Mathematical Formula

MAE Formula:

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

### Formula Explanation

| Symbol | Meaning |
|---|---|
| MAE | Mean Absolute Error |
| n | మొత్తం Data Points సంఖ్య |
| yᵢ | Actual Value |
| ŷᵢ | Predicted Value |
| \| \| | Absolute Value |
| Σ | Summation |

### Absolute Value అంటే ఏమిటి?

ఒక Number Positive లేదా Negative అయినా, దాని Absolute Value ఎప్పుడూ Negative‌గా ఉండదు.

**Python Example:**

```python
print(abs(5))
print(abs(-5))
print(abs(10))
print(abs(-10))
```

**Output:**

```text
5
5
10
10
```

ఉదాహరణకు:

```text
Error = -5

Absolute Error = |-5| = 5
```

**గుర్తుంచుకోండి:** MAEలో Error‌ను Square చేయము. Absolute Value మాత్రమే తీసుకుంటాము.

---

## 📌 4. Step-by-Step MAE Calculation

మన దగ్గర ఈ Data ఉందని అనుకుందాం.

```python
# Actual Values
actual = [40, 50, 60, 70, 80]

# Predicted Values
predicted = [42, 48, 65, 68, 75]
```

### Step 1: Calculate Errors

Formula:

$$
Error = Actual - Predicted
$$

| Actual | Predicted | Error |
|---:|---:|---:|
| 40 | 42 | -2 |
| 50 | 48 | 2 |
| 60 | 65 | -5 |
| 70 | 68 | 2 |
| 80 | 75 | 5 |

### Step 2: Calculate Absolute Errors

Formula:

$$
Absolute\ Error = |Actual - Predicted|
$$

| Actual | Predicted | Error | Absolute Error |
|---:|---:|---:|---:|
| 40 | 42 | -2 | 2 |
| 50 | 48 | 2 | 2 |
| 60 | 65 | -5 | 5 |
| 70 | 68 | 2 | 2 |
| 80 | 75 | 5 | 5 |

### Step 3: Calculate Average

Formula:

$$
MAE = \frac{2+2+5+2+5}{5}
$$

$$
MAE = \frac{16}{5}
$$

$$
\boxed{MAE = 3.2}
$$

### Final Result:

**MAE = 3.2**

అంటే మన Model Predictions, Actual Values నుండి సగటున 3.2 Marks దూరంలో ఉన్నాయి.

గమనిక: ఇది Average Absolute Error. ప్రతి Predictionలో తప్పనిసరిగా 3.2 Marks Error ఉందని కాదు.

---

## 📌 5. Python Implementation – MAE

### Step 1: Install Required Libraries

VS Code Terminalలో ఈ Command Run చేయండి.

```bash
pip install numpy scikit-learn
```

### Step 2: Import Required Libraries

```python
import numpy as np

from sklearn.metrics import mean_absolute_error
```

### Step 3: Create Actual Values

```python
# Test Dataset నుండి వచ్చిన నిజమైన Values

y_test = np.array([40, 50, 60, 70, 80])
```

### Step 4: Create Predicted Values

```python
# Machine Learning Model Predict చేసిన Values

y_pred = np.array([42, 48, 65, 68, 75])
```

### Step 5: Calculate Absolute Errors

```python
# Actual మరియు Predicted Values మధ్య Difference

absolute_errors = np.abs(y_test - y_pred)

print("Absolute Errors:", absolute_errors)
```

### Step 6: Calculate MAE

```python
# Absolute Errors యొక్క Average Calculate చేస్తుంది

mae = mean_absolute_error(y_test, y_pred)

print("Mean Absolute Error:", mae)
```

### Step 7: Complete Python Code with Comments

```python
# ============================================================
# MACHINE LEARNING
# MEAN ABSOLUTE ERROR (MAE)
# ============================================================


# STEP 1: Import Required Libraries

import numpy as np

from sklearn.metrics import mean_absolute_error


# STEP 2: Create Actual Values

# ఇవి మన Test Datasetలోని నిజమైన Values

y_test = np.array([40, 50, 60, 70, 80])


# STEP 3: Create Predicted Values

# ఇవి మన Machine Learning Model Predict చేసిన Values

y_pred = np.array([42, 48, 65, 68, 75])


# STEP 4: Calculate Absolute Errors

# Actual మరియు Predicted Values మధ్య Difference Calculate చేస్తాము

absolute_errors = np.abs(y_test - y_pred)


# STEP 5: Calculate MAE

# Absolute Errors యొక్క Average Calculate చేస్తాము

mae = mean_absolute_error(y_test, y_pred)


# STEP 6: Display Results

print("Actual Values:", y_test)

print("Predicted Values:", y_pred)

print("Absolute Errors:", absolute_errors)

print("-----------------------------------")

print("Mean Absolute Error:", mae)
```

### Expected Output

```text
Actual Values: [40 50 60 70 80]

Predicted Values: [42 48 65 68 75]

Absolute Errors: [2 2 5 2 5]

-----------------------------------

Mean Absolute Error: 3.2
```

---

## 📌 6. Difference Between MAE and MSE

ఇప్పుడు MAE మరియు MSE మధ్య ముఖ్యమైన తేడా తెలుసుకుందాం.

### MSE (Mean Squared Error)

MSEలో Error‌ను Square చేస్తాము.

$$
MSE = \frac{1}{n}\sum (Actual-Predicted)^2
$$

### MAE (Mean Absolute Error)

MAEలో Error‌కు Absolute Value తీసుకుంటాము. Square చేయము.

$$
MAE = \frac{1}{n}\sum |Actual-Predicted|
$$

### Example

ఒక Prediction Error = -5 అనుకుందాం.

| Metric | Calculation | Result |
|---|---|---:|
| MSE | (-5)² | 25 |
| MAE | \|-5\| | 5 |

### Comparison Table

| Feature | MAE | MSE |
|---|---|---|
| Full Form | Mean Absolute Error | Mean Squared Error |
| Calculation | Absolute Errors Average | Squared Errors Average |
| Error Treatment | Absolute Value | Square |
| Best Value | 0 | 0 |
| Negative Result | రాదు | రాదు |
| Large Errors | Linear Penalty | Squared Penalty |
| Units | Original Target Units | Squared Target Units |

### Easy Way to Remember

- **MSE:** Error × Error → Average
- **MAE:** Absolute Error → Average

---

## 📌 7. Real-World Example

ఒక Company House Price Prediction Model తయారు చేసిందని అనుకుందాం.

| Actual Price | Predicted Price | Absolute Error |
|---:|---:|---:|
| ₹20 Lakhs | ₹21 Lakhs | ₹1 Lakh |
| ₹30 Lakhs | ₹29 Lakhs | ₹1 Lakh |
| ₹40 Lakhs | ₹42 Lakhs | ₹2 Lakhs |
| ₹50 Lakhs | ₹48 Lakhs | ₹2 Lakhs |
| ₹60 Lakhs | ₹59 Lakhs | ₹1 Lakh |

MAE Calculation:

$$
MAE = \frac{1+1+2+2+1}{5}
$$

$$
MAE = \frac{7}{5}
$$

$$
\boxed{MAE = 1.4\ Lakhs}
$$

**Interpretation:**

మన House Price Prediction Model, Actual House Prices నుండి సగటున ₹1.4 Lakhs తేడాతో Predictions చేస్తోంది.

---

## 📌 8. Advantages and Disadvantages of MAE

### Advantages

1. అర్థం చేసుకోవడం చాలా సులభం.
2. Original Target Unitsలోనే Result వస్తుంది.
3. Errors‌ను Square చేయదు.
4. MSEతో పోలిస్తే పెద్ద Errors‌కు తక్కువ Penalty ఇస్తుంది.
5. Average Prediction Error‌ను సులభంగా అర్థం చేసుకోవచ్చు.

### Disadvantages

1. పెద్ద Errors‌కు MSE అంత ఎక్కువ Penalty ఇవ్వదు.
2. Error Positive లేదా Negative Direction‌ను తెలియజేయదు.
3. MAE ఒక్కటితో మాత్రమే Model Performance పూర్తిగా అర్థం చేసుకోలేము.
4. Outliers వల్ల MAE కూడా ప్రభావితం అవుతుంది.

---

## 📌 9. Important Interview Questions

**Q1. What is Mean Absolute Error?**

MAE అనేది Actual Values మరియు Predicted Values మధ్య ఉన్న Absolute Differences యొక్క Average‌ను Calculate చేసే Regression Evaluation Metric.

**Q2. Why do we use MAE?**

Model Predictions‌లో సగటున ఎంత Error వస్తుందో తెలుసుకోవడానికి MAE ఉపయోగిస్తాము.

**Q3. What is the best MAE value?**

MAE = 0 అయితే Predictions Perfect‌గా ఉన్నట్లు.

**Q4. Does MAE contain negative values?**

లేదు. Absolute Value తీసుకుంటాము కాబట్టి MAE Negative‌గా రాదు.

**Q5. Difference between MAE and MSE?**

MAE Absolute Errors Average‌ను Calculate చేస్తుంది. MSE Squared Errors Average‌ను Calculate చేస్తుంది.

**Q6. Is MAE affected by outliers?**

అవును. MAE కూడా Outliers వల్ల ప్రభావితం అవుతుంది. అయితే MSEతో పోలిస్తే పెద్ద Errors‌కు తక్కువ Penalty ఇస్తుంది.

**Q7. Which is better: MAE or MSE?**

ఇది మన Problem మీద ఆధారపడి ఉంటుంది.

- Errors‌ను సులభంగా అర్థం చేసుకోవాలంటే MAE ఉపయోగపడుతుంది.
- పెద్ద Errors‌కు ఎక్కువ Penalty ఇవ్వాలంటే MSE ఉపయోగపడుతుంది.

**Q8. What is the difference between Error and Absolute Error?**

Error అనేది Actual మరియు Predicted మధ్య Difference. Absolute Error అనేది ఆ Difference యొక్క Positive Magnitude.

---

## 📌 10. Practice Exercises

ఈ ప్రశ్నలకు స్వయంగా సమాధానాలు రాయడానికి ప్రయత్నించండి.

### Exercise 1

```python
Actual Values = [10, 20, 30, 40, 50]

Predicted Values = [12, 18, 32, 38, 55]
```

1. Errors Calculate చేయండి.
2. Absolute Errors Calculate చేయండి.
3. MAE Calculate చేయండి.

### Exercise 2

```python
MAE = 0
```

1. దీని అర్థం ఏమిటి?
2. Model Predictions ఎలా ఉన్నాయి?

### Exercise 3

```python
MAE = 5.5
```

1. Modelలో Prediction Error ఉందా?
2. MAE తక్కువగా ఉంటే మంచిదా?
3. MAE = 5.5 అంటే ప్రతి Predictionలో 5.5 Error ఉందా?

---

## 📌 11. Final Summary

| Metric | Purpose | Best Value |
|---|---|---:|
| MAE | Average Absolute Prediction Error | 0 |
| MSE | Average Squared Prediction Error | 0 |
| R² Score | Explained Variation | 1 |

### Easy Way to Remember

- **MAE:** సగటున Prediction ఎంత దూరంలో ఉంది?
- **MSE:** Squared Prediction Errors Average ఎంత?
- **R² Score:** Model Target Variation‌ను ఎంతవరకు Explain చేస్తోంది?

### 🚀 Machine Learning Evaluation Metrics Flow

```text
          Regression Model
                 |
                 v
          Model Predictions
                 |
                 v
          Model Evaluation
                 |
       +---------+---------+
       |         |         |
       v         v         v
      MAE       MSE       R²
       |         |         |
       v         v         v
    Average   Squared   Explained
     Error     Error    Variation
```

## 🎯 Conclusion

Mean Absolute Error (MAE) అనేది Regression Model Performance‌ను అర్థం చేసుకోవడానికి ఉపయోగించే ముఖ్యమైన Evaluation Metric.

ఇది Actual Values మరియు Predicted Values మధ్య సగటు Absolute Error‌ను తెలియజేస్తుంది.

MAE తక్కువగా ఉంటే సాధారణంగా Model Predictions మెరుగ్గా ఉన్నట్లు.

**Happy Learning! 🚀**