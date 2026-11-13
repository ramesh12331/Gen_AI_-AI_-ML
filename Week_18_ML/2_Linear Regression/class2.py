# ============================================================
# MACHINE LEARNING
# LINEAR REGRESSION - COMPLETE VS CODE NOTES
# Topic: Study Hours vs Student Marks
# ============================================================

# Linear Regression is a supervised machine learning algorithm.
#
# It learns the relationship between an input (X) and an output (y).
#
# Example:
# X = Study Hours
# y = Student Marks
#
# Goal:
# Predict a student's marks based on the number of hours studied.
#
# Workflow:
# 1. Import libraries
# 2. Create the dataset
# 3. Separate X and y
# 4. Split data into training and testing sets
# 5. Create the Linear Regression model
# 6. Train the model
# 7. Find the slope and intercept
# 8. Predict marks
# 9. Compare actual and predicted marks
# 10. Calculate residuals and Mean Squared Error (MSE)


# ============================================================
# 1. IMPORT REQUIRED LIBRARIES
# ============================================================

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# ============================================================
# 2. CREATE THE DATASET
# ============================================================

# Study_Hours represents the number of hours studied.
# Marks represents the marks obtained by students.

df = pd.DataFrame({
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [25, 30, 40, 45, 50, 60, 65, 75, 80, 90]
})

print("Complete Dataset:")
print(df)

# Expected output:
#
#    Study_Hours  Marks
# 0            1     25
# 1            2     30
# 2            3     40
# 3            4     45
# 4            5     50
# 5            6     60
# 6            7     65
# 7            8     75
# 8            9     80
# 9           10     90


# ============================================================
# 3. SEPARATE INPUT (X) AND OUTPUT (y)
# ============================================================

# X = Independent variable / Input feature
# y = Dependent variable / Target output
#
# Here:
# X = Study_Hours
# y = Marks
#
# Double brackets [[]] select a DataFrame with 2 dimensions.
# Single brackets [] select a Series with 1 dimension.

X = df[["Study_Hours"]]
y = df["Marks"]

print("\nInput Feature X:")
print(X)

print("\nTarget Variable y:")
print(y)

print("\nShape of X:", X.shape)
print("Shape of y:", y.shape)

# Expected output:
#
# Shape of X: (10, 1)
# Shape of y: (10,)


# ============================================================
# 4. TRAIN-TEST SPLIT
# ============================================================

# train_test_split() divides data into training and testing sets.
#
# X_train = Input data used to train the model
# X_test  = Input data used to test the model
# y_train = Actual target values used for training
# y_test  = Actual target values used for testing
#
# test_size=0.2 means:
# 80% of records are used for training.
# 20% of records are used for testing.
#
# For 10 records:
# Training records = 8
# Testing records  = 2
#
# random_state=42 makes the split reproducible.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Input:")
print(X_train)

print("\nTesting Input:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)

print("\nNumber of training records:", len(X_train))
print("Number of testing records:", len(X_test))

# With this dataset and random_state=42, the test records are:
#
# X_test:
#    Study_Hours
# 8            9
# 1            2
#
# y_test:
# 8    80
# 1    30
#
# Training records: 8
# Testing records: 2


# ============================================================
# 5. CREATE THE LINEAR REGRESSION MODEL
# ============================================================

# Importing LinearRegression gives us the model.
#
# LinearRegression() creates a model object.
# At this stage, the model has not learned from the dataset.

model = LinearRegression()

print("\nLinear Regression Model Created:")
print(model)


# ============================================================
# 6. TRAIN THE MODEL
# ============================================================

# fit() trains the model using the training data.
#
# X_train contains the input feature: Study_Hours.
# y_train contains the corresponding actual marks.
#
# The model learns the best-fitting straight line.

model.fit(X_train, y_train)

print("\nModel Training Completed!")


# ============================================================
# 7. FIND THE SLOPE AND INTERCEPT
# ============================================================

# Linear Regression equation:
#
# y = mx + b
#
# y = Predicted output
# x = Input value
# m = Slope
# b = Intercept
#
# model.coef_[0] gives the slope for our single input feature.
# model.intercept_ gives the intercept.

slope = model.coef_[0]
intercept = model.intercept_

print("\nSlope:", slope)
print("Intercept:", intercept)

# Expected output (approximately):
#
# Slope: 7.155172413793104
# Intercept: 16.89655172413793
#
# Learned equation:
#
# Predicted Marks = 7.1551724 * Study_Hours + 16.8965517
#
# Interpretation:
# The slope represents the predicted change in marks for
# one additional study hour, according to the learned model.
#
# The intercept is the model's predicted marks when Study_Hours = 0.


# ============================================================
# 8. PREDICT MARKS
# ============================================================

# predict() uses the trained model to estimate output values.
#
# X_test contains the study hours of the test records.
# y_pred contains the model's predicted marks.

y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

# Expected output (approximately):
#
# Actual Marks:
# [80 30]
#
# Predicted Marks:
# [81.29310345 31.20689655]


# ============================================================
# 9. COMPARE ACTUAL AND PREDICTED MARKS
# ============================================================

# A DataFrame helps us compare the actual marks with
# the marks predicted by the model.

results = pd.DataFrame({
    "Study_Hours": X_test["Study_Hours"].values,
    "Actual_Marks": y_test.values,
    "Predicted_Marks": y_pred
})

print("\nPrediction Results:")
print(results)

# Expected output (approximately):
#
#    Study_Hours  Actual_Marks  Predicted_Marks
# 0            9            80        81.293103
# 1            2            30        31.206897
#
# Note:
# The displayed row order follows X_test.
# Your DataFrame's index may differ depending on how you display it.


# ============================================================
# 10. CALCULATE RESIDUALS
# ============================================================

# Residual = Actual value - Predicted value
#
# Residual tells us how far a prediction is from the actual value.
#
# Residual = y - y_pred
#
# Positive residual:
# Actual value is greater than predicted value.
#
# Negative residual:
# Actual value is less than predicted value.
#
# Zero residual:
# Prediction exactly matches the actual value.

results["Residual"] = (
    results["Actual_Marks"] - results["Predicted_Marks"]
)

print("\nResults with Residuals:")
print(results)

# Expected residuals (approximately):
#
# For 9 study hours:
# Residual = 80 - 81.29310345
#          = -1.29310345
#
# For 2 study hours:
# Residual = 30 - 31.20689655
#          = -1.20689655


# ============================================================
# 11. UNDERSTAND SUM OF SQUARED ERRORS (SSE)
# ============================================================

# First, square each residual.
#
# Squared Error = (Actual - Predicted) ** 2
#
# Then add all the squared errors.
#
# SSE = Sum of Squared Errors
#
# SSE = (y1 - predicted_y1)^2
#     + (y2 - predicted_y2)^2
#     + ...
#     + (yn - predicted_yn)^2
#
# Squaring makes the errors non-negative and penalizes
# larger errors more heavily.

results["Squared_Error"] = results["Residual"] ** 2

sse = results["Squared_Error"].sum()

print("\nResults with Squared Errors:")
print(results)

print("\nSum of Squared Errors (SSE):", sse)


# ============================================================
# 12. MEAN SQUARED ERROR (MSE)
# ============================================================

# MSE = Mean Squared Error
#
# Formula:
#
# MSE = (1 / n) * SUM((Actual - Predicted) ** 2)
#
# n = Number of test records
#
# MSE is the average of all squared prediction errors.
#
# Lower MSE generally indicates better predictions when
# comparing models on the same target and evaluation dataset.

mse = mean_squared_error(y_test, y_pred)

print("\nMean Squared Error (MSE):", mse)

# For this particular test split, MSE is approximately:
# 1.5689655172


# ============================================================
# 13. PREDICT MARKS FOR A NEW STUDENT
# ============================================================

# Suppose a new student studies for 5 hours.
# We can use the trained model to predict the student's marks.
#
# Keep the input in a 2D format because X was trained as
# a DataFrame with one feature column.

new_student = pd.DataFrame({
    "Study_Hours": [5]
})

predicted_marks = model.predict(new_student)

print("\nNew Student Study Hours:")
print(new_student)

print("\nPredicted Marks for 5 Study Hours:")
print(predicted_marks)

# The prediction depends on the line learned by the model.
# It is an estimate, not a guarantee of the student's result.


# ============================================================
# 14. IMPORTANT CONCEPTS - QUICK REVISION
# ============================================================

# X:
# Input feature(s), such as Study_Hours.
#
# y:
# Actual target values, such as Marks.
#
# X_train:
# Input data used to train the model.
#
# X_test:
# Input data used to evaluate the model.
#
# y_train:
# Actual target values used during training.
#
# y_test:
# Actual target values used for evaluation.
#
# model.fit(X_train, y_train):
# Trains the Linear Regression model.
#
# model.coef_:
# Stores the learned slope coefficient(s).
#
# model.intercept_:
# Stores the learned intercept.
#
# model.predict(X_test):
# Generates predictions for the testing inputs.
#
# Residual:
# Actual value - Predicted value.
#
# SSE:
# Sum of squared residuals.
#
# MSE:
# Average of squared residuals.


# ============================================================
# 15. COMPLETE LINEAR REGRESSION WORKFLOW
# ============================================================

# Dataset
#    |
#    v
# Separate X and y
#    |
#    v
# Train-Test Split
#    |
#    +--------------------+
#    |                    |
#    v                    v
# X_train, y_train     X_test, y_test
#    |
#    v
# Create LinearRegression()
#    |
#    v
# model.fit(X_train, y_train)
#    |
#    v
# Learn slope and intercept
#    |
#    v
# model.predict(X_test)
#    |
#    v
# Compare predictions with y_test
#    |
#    v
# Calculate residuals and MSE


# ============================================================
# END OF LINEAR REGRESSION NOTES
# ============================================================