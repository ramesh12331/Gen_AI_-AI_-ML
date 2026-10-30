# ============================================================
# MACHINE LEARNING
# MULTIPLE LINEAR REGRESSION
# MODEL TRAINING, PREDICTION, COEFFICIENTS, AND EVALUATION
# VS CODE FORMAT WITH COMMENTED EXPLANATIONS
# ============================================================


# ============================================================
# STEP 1: INSTALL REQUIRED LIBRARIES
# ============================================================

# Run this command in the VS Code terminal:
# pip install pandas numpy scikit-learn matplotlib


# ============================================================
# STEP 2: IMPORT REQUIRED LIBRARIES
# ============================================================

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score


# ============================================================
# STEP 3: MULTIPLE LINEAR REGRESSION FORMULA
# ============================================================

# Multiple Linear Regression uses multiple input features
# to predict one numerical output.
#
# Formula:
#
# y = b0 + b1*x1 + b2*x2 + ... + bn*xn
#
# Where:
#
# y  = predicted output
# b0 = intercept
# b1 = coefficient of feature 1
# b2 = coefficient of feature 2
# x1 = first input feature
# x2 = second input feature
#
# Example:
#
# Final_Marks = b0
#               + b1 * Previous_Marks
#               + b2 * Study_Hours
#
# The model learns b0, b1, and b2 from training data.


# ============================================================
# STEP 4: LOAD YOUR DATASET
# ============================================================

# Example:
#
# df = pd.read_csv("student_data.csv")
#
# Display the first five rows:
#
# print(df.head())
#
# Check column names:
#
# print(df.columns)
#
# IMPORTANT:
# Replace the example feature names below with the actual
# column names from your dataset.


# ============================================================
# STEP 5: DEFINE INPUT FEATURES (X) AND TARGET (y)
# ============================================================

# X contains the independent variables (input features).
# y contains the dependent variable (value to predict).
#
# In the example shown in your screenshots:
# The target appears to be Final_Marks.
# The model has two coefficients, suggesting two input features.
#
# Replace these example names with your actual dataset columns.

# Example:
#
# X = df[["Previous_Marks", "Study_Hours"]]
# y = df["Final_Marks"]


# ============================================================
# STEP 6: SPLIT THE DATASET
# ============================================================

# Divide data into training data and testing data.
#
# X_train = input features used to train the model
# X_test  = input features used to test the model
# y_train = actual target values used for training
# y_test  = actual target values used for evaluation
#
# Example:
#
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )
#
# test_size=0.2 means:
# 80% of the data is used for training.
# 20% of the data is used for testing.
#
# random_state=42 makes the split reproducible.


# ============================================================
# STEP 7: CREATE THE MODEL
# ============================================================

# Create an instance of Multiple Linear Regression.

# mlr = LinearRegression()


# ============================================================
# STEP 8: TRAIN THE MODEL
# ============================================================

# The fit() method trains the model.
#
# The model learns the relationship between X_train and y_train.
#
# Example:
#
# mlr.fit(X_train, y_train)
#
# After training, the model learns:
# 1. Coefficients
# 2. Intercept


# ============================================================
# STEP 9: PREDICT VALUES
# ============================================================

# The predict() method generates predictions for test inputs.
#
# Example:
#
# y_pred = mlr.predict(X_test)
#
# y_pred contains the values predicted by the trained model.


# ============================================================
# STEP 10: DISPLAY ACTUAL VALUES
# ============================================================

# y_test contains the actual target values.
#
# Display the first five actual values:
#
# print("Actual values:")
# print(y_test.iloc[0:5])
#
# Example output from your screenshot:
#
# actual_values
# 405      84.74
# 1190     47.21
# 1132     40.94
# 731      51.48
# 1754     85.92
#
# Note:
# The index labels and values depend on your dataset and split.


# ============================================================
# STEP 11: DISPLAY PREDICTED VALUES
# ============================================================

# Display the first five predictions:
#
# print("Predicted values:", y_pred[0:5])
#
# Example output from your screenshot:
#
# predicted_values
# [80.72635948 43.97043052 43.82324411
#  54.77040925 86.6138502]
#
# These are the model's predictions for the first five
# samples in X_test.


# ============================================================
# STEP 12: COMPARE ACTUAL AND PREDICTED VALUES
# ============================================================

# Compare actual values with their corresponding predictions.
#
# Example:
#
# comparison = pd.DataFrame({
#     "Actual": y_test.iloc[:5].to_numpy(),
#     "Predicted": y_pred[:5]
# })
#
# print(comparison)
#
# Interpretation:
#
# Actual   = real value from the dataset
# Predicted = value estimated by the trained model
#
# A smaller difference generally indicates a more accurate
# prediction for that sample.


# ============================================================
# STEP 13: VIEW MODEL COEFFICIENTS
# ============================================================

# The coef_ attribute returns the learned coefficients.
#
# Example:
#
# print(mlr.coef_)
#
# Output from your screenshot:
#
# array([2.44151595, 0.25343069, 0.45208106])
#
# IMPORTANT:
# This screenshot shows three coefficients.
# Therefore, the fitted model appears to use three input features.
#
# Each coefficient corresponds to one feature in X, in the
# same order as the columns used to train the model.
#
# For example, if:
#
# X = df[["Feature_1", "Feature_2", "Feature_3"]]
#
# then:
#
# mlr.coef_[0] corresponds to Feature_1
# mlr.coef_[1] corresponds to Feature_2
# mlr.coef_[2] corresponds to Feature_3
#
# A coefficient represents the estimated change in the
# predicted target for a one-unit increase in that feature,
# holding the other features constant.


# ============================================================
# STEP 14: VIEW THE INTERCEPT
# ============================================================

# The intercept is the constant term in the regression formula.
#
# Example:
#
# print(mlr.intercept_)
#
# Output from your screenshot:
#
# 4.7093666521882595
#
# The intercept is the model's predicted value when all
# input features are zero.
#
# This interpretation may not be practically meaningful if
# zero is outside the realistic range of the features.


# ============================================================
# STEP 15: WRITE THE LEARNED REGRESSION EQUATION
# ============================================================

# Suppose the model returns:
#
# Coefficients:
# [2.44151595, 0.25343069, 0.45208106]
#
# Intercept:
# 4.7093666521882595
#
# Then the estimated equation is:
#
# y_pred = 4.7093666521882595
#          + 2.44151595 * x1
#          + 0.25343069 * x2
#          + 0.45208106 * x3
#
# IMPORTANT:
# x1, x2, and x3 represent your input features in the
# exact order used to train the model.
#
# Use the actual column names to write the equation
# in a meaningful way.


# ============================================================
# STEP 16: CALCULATE MEAN SQUARED ERROR (MSE)
# ============================================================

# MSE measures the average squared difference between
# actual values and predicted values.
#
# Formula:
#
# MSE = (1 / n) * sum((actual - predicted) ** 2)
#
# Smaller MSE generally indicates smaller prediction errors.
#
# Example:
#
# mse = mean_squared_error(y_test, y_pred)
#
# print("Mean Squared Error:", mse)
#
# Output from your screenshot:
#
# Mean Squared Error: 27.94939523427141
#
# Interpretation:
# The model's average squared prediction error is approximately
# 27.95 in squared target units.
#
# MSE is not expressed in the same units as the target because
# the errors are squared.


# ============================================================
# STEP 17: CALCULATE ROOT MEAN SQUARED ERROR (RMSE)
# ============================================================

# RMSE is the square root of MSE.
#
# Formula:
#
# RMSE = sqrt(MSE)
#
# RMSE is expressed in the same units as the target variable.
#
# Example:
#
# rmse = np.sqrt(mse)
#
# print("Root Mean Squared Error:", rmse)
#
# With MSE approximately 27.9494:
#
# RMSE is approximately 5.29.
#
# Interpretation:
# RMSE summarizes the typical size of prediction errors,
# while giving greater weight to larger errors.


# ============================================================
# STEP 18: CALCULATE R-SQUARED (R²) SCORE
# ============================================================

# R² measures how well the model explains variation in
# the target values compared with predicting the mean.
#
# Example:
#
# r2 = r2_score(y_test, y_pred)
#
# print("R² Score:", r2)
#
# General interpretation:
#
# R² = 1.0  -> perfect predictions on the evaluated data
# R² = 0.0  -> no improvement over predicting the test mean
# R² < 0.0  -> worse than predicting the test mean
#
# R² should be interpreted in the context of the dataset.
# It does not prove that the model is suitable for every use.


# ============================================================
# STEP 19: CALCULATE R² USING THE MODEL
# ============================================================

# A trained LinearRegression model also provides score().
#
# Example:
#
# print("Model R² Score:", mlr.score(X_test, y_test))
#
# For standard LinearRegression regression tasks,
# score() returns the R² score.
#
# This should match r2_score(y_test, y_pred), apart from
# possible minor floating-point differences.


# ============================================================
# STEP 20: CROSS-VALIDATION
# ============================================================

# Cross-validation evaluates model performance across
# multiple training/validation splits.
#
# This can provide a more stable view of model performance
# than relying on a single train-test split.
#
# Example:
#
# model = LinearRegression()
#
# cv_scores = cross_val_score(
#     model,
#     X_train,
#     y_train,
#     cv=5,
#     scoring="r2"
# )
#
# print("Individual fold scores:", cv_scores)
# print("Mean R²:", cv_scores.mean())
# print("Standard deviation:", cv_scores.std())
#
# Example output from your screenshot:
#
# Individual fold scores:
# [0.87359722 0.87775172 0.88272099 0.85724245 0.89975773]
#
# Mean R²: approximately 0.8782
#
# Standard deviation: approximately 0.0138
#
# Interpretation:
# The five validation folds produced R² scores around 0.86–0.90.
# The mean score summarizes their average performance.
# The standard deviation shows how much the scores vary.
#
# Important:
# The values above are examples from your screenshot.
# Your results can differ based on the data and preprocessing.


# ============================================================
# STEP 21: COMPLETE WORKFLOW TEMPLATE
# ============================================================

# Use this section after loading your real dataset and
# replacing the feature names with your actual column names.

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

# df = pd.read_csv("student_data.csv")
#
# print(df.head())
# print(df.columns)


# ------------------------------------------------------------
# DEFINE FEATURES AND TARGET
# ------------------------------------------------------------

# X = df[["Feature_1", "Feature_2", "Feature_3"]]
# y = df["Final_Marks"]


# ------------------------------------------------------------
# SPLIT DATA
# ------------------------------------------------------------

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )


# ------------------------------------------------------------
# TRAIN MODEL
# ------------------------------------------------------------

# mlr = LinearRegression()
# mlr.fit(X_train, y_train)


# ------------------------------------------------------------
# PREDICT
# ------------------------------------------------------------

# y_pred = mlr.predict(X_test)


# ------------------------------------------------------------
# EVALUATE
# ------------------------------------------------------------

# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)
# r2 = r2_score(y_test, y_pred)
#
# print("Coefficients:", mlr.coef_)
# print("Intercept:", mlr.intercept_)
# print("MSE:", mse)
# print("RMSE:", rmse)
# print("R² Score:", r2)


# ============================================================
# FINAL REVISION
# ============================================================

# fit()
#     -> Trains the model.
#
# predict()
#     -> Predicts target values.
#
# coef_
#     -> Returns the learned feature coefficients.
#
# intercept_
#     -> Returns the learned intercept.
#
# mean_squared_error()
#     -> Calculates Mean Squared Error.
#
# np.sqrt(mse)
#     -> Calculates Root Mean Squared Error.
#
# r2_score()
#     -> Calculates the R² evaluation score.
#
# cross_val_score()
#     -> Evaluates the model across multiple folds.
#
# ============================================================
# END OF MULTIPLE LINEAR REGRESSION NOTES
# ============================================================