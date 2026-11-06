# ==========================================
# 1. Import Required Libraries
# ==========================================

import numpy as np
import pandas as pd

# Split dataset into training and testing
from sklearn.model_selection import train_test_split

# Generate polynomial features
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# Import regression algorithms
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Pipeline combines multiple steps
from sklearn.pipeline import Pipeline

# Model evaluation
from sklearn.metrics import mean_squared_error, r2_score


# ==========================================
# 2. Create Dataset
# ==========================================

data = {
    "Study_Hours": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20
    ],

    "Marks": [
        20, 25, 35, 40, 48,
        55, 60, 65, 70, 78,
        80, 85, 88, 90, 92,
        94, 96, 97, 98, 99
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

print("Complete Dataset:")
print(df)


# ==========================================
# 3. Separate Input and Target
# ==========================================

# X = Input feature
X = df[["Study_Hours"]]

# y = Target variable
y = df["Marks"]


# ==========================================
# 4. Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,       # 80% training, 20% testing
    random_state=42
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))


# ==========================================
# 5. Create Linear Regression Model
# ==========================================

linear_model = Pipeline([

    # Generate polynomial features up to degree 5
    ("poly", PolynomialFeatures(
        degree=5,
        include_bias=False
    )),

    # Scale generated features
    ("scaler", StandardScaler()),

    # Ordinary Linear Regression
    ("model", LinearRegression())

])


# ==========================================
# 6. Create Ridge Model (L2)
# ==========================================

ridge_model = Pipeline([

    # Generate polynomial features
    ("poly", PolynomialFeatures(
        degree=5,
        include_bias=False
    )),

    # Scale features
    ("scaler", StandardScaler()),

    # Ridge uses L2 regularization
    ("model", Ridge(alpha=1.0))

])


# ==========================================
# 7. Create Lasso Model (L1)
# ==========================================

lasso_model = Pipeline([

    # Generate polynomial features
    ("poly", PolynomialFeatures(
        degree=5,
        include_bias=False
    )),

    # Scale features
    ("scaler", StandardScaler()),

    # Lasso uses L1 regularization
    ("model", Lasso(
        alpha=0.1,
        max_iter=10000
    ))

])


# ==========================================
# 8. Train All Three Models
# ==========================================

linear_model.fit(X_train, y_train)

ridge_model.fit(X_train, y_train)

lasso_model.fit(X_train, y_train)


# ==========================================
# 9. Make Predictions
# ==========================================

# Predictions using training data
linear_train_pred = linear_model.predict(X_train)
ridge_train_pred = ridge_model.predict(X_train)
lasso_train_pred = lasso_model.predict(X_train)

# Predictions using testing data
linear_test_pred = linear_model.predict(X_test)
ridge_test_pred = ridge_model.predict(X_test)
lasso_test_pred = lasso_model.predict(X_test)


# ==========================================
# 10. Evaluate Models
# ==========================================

models = {
    "Linear Regression": (linear_train_pred, linear_test_pred),
    "Ridge (L2)": (ridge_train_pred, ridge_test_pred),
    "Lasso (L1)": (lasso_train_pred, lasso_test_pred)
}

for name, (train_pred, test_pred) in models.items():

    # Calculate training R2
    train_r2 = r2_score(y_train, train_pred)

    # Calculate testing R2
    test_r2 = r2_score(y_test, test_pred)

    # Calculate testing MSE
    test_mse = mean_squared_error(y_test, test_pred)

    print("\n", name)

    print("Training R2:", round(train_r2, 4))

    print("Testing R2:", round(test_r2, 4))

    print("Testing MSE:", round(test_mse, 4))


# ==========================================
# 11. Check Lasso Coefficients
# ==========================================

# Access the trained Lasso model inside Pipeline
lasso = lasso_model.named_steps["model"]

print("\nLasso Coefficients:")
print(lasso.coef_)

# Check how many coefficients became zero
zero_count = np.sum(lasso.coef_ == 0)

print("Number of Zero Coefficients:", zero_count)


# ==========================================
# 12. Predict Marks for a New Student
# ==========================================

new_student = pd.DataFrame({
    "Study_Hours": [12]
})

# Predict using Ridge
ridge_prediction = ridge_model.predict(new_student)

# Predict using Lasso
lasso_prediction = lasso_model.predict(new_student)

print("\nNew Student Study Hours: 12")

print("Ridge Prediction:", ridge_prediction[0])

print("Lasso Prediction:", lasso_prediction[0])