# ============================================================
# MACHINE LEARNING
# MULTIPLE LINEAR REGRESSION
# VS CODE FORMAT WITH COMMENTED EXPLANATIONS
# ============================================================

# ============================================================
# STEP 1: INSTALL REQUIRED LIBRARIES
# ============================================================

# Run this command in the VS Code terminal:
# pip install pandas scikit-learn matplotlib

# ============================================================
# STEP 2: IMPORT REQUIRED LIBRARIES
# ============================================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import matplotlib.pyplot as plt


# ============================================================
# STEP 3: LOAD THE DATASET
# ============================================================

# Make sure student_marks_2000.csv is available in your
# project folder, or provide the complete file path.

df = pd.read_csv("student_marks_2000.csv")

# Display the first five rows of the dataset.
print("First Five Rows:")
print(df.head())

# Expected columns:
# Study_Hours
# Attendance
# Previous_Marks
# Final_Marks


# ============================================================
# STEP 4: UNDERSTAND THE DATA
# ============================================================

# X = Independent variables (input features)
# y = Dependent variable (target/output)
#
# Multiple Linear Regression uses multiple input features
# to predict one target value.
#
# Mathematical formula:
#
# y = B0 + B1*X1 + B2*X2 + B3*X3
#
# B0 = Intercept
# B1 = Coefficient for Study_Hours
# B2 = Coefficient for Attendance
# B3 = Coefficient for Previous_Marks
#
# X1 = Study_Hours
# X2 = Attendance
# X3 = Previous_Marks
# y  = Predicted Final_Marks

X = df.drop(columns=["Final_Marks"])

y = df["Final_Marks"]

print("\nInput Features (X):")
print(X.head())

print("\nTarget Variable (y):")
print(y.head())


# ============================================================
# STEP 5: SPLIT DATA INTO TRAINING AND TESTING SETS
# ============================================================

# Training data is used to teach the model.
# Testing data is used to evaluate the trained model.
#
# test_size=0.2 means:
# 80% of the data is used for training.
# 20% of the data is used for testing.
#
# random_state=42 makes the split reproducible.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Input:")
print(X_train.head())

print("\nTesting Input:")
print(X_test.head())

print("\nTotal Dataset Records:", len(df))
print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))


# ============================================================
# STEP 6: CREATE THE MULTIPLE LINEAR REGRESSION MODEL
# ============================================================

# Create the model object.
#
# LinearRegression() creates a linear regression estimator.
# The model learns the relationship between the input
# features and the target variable.

mlr = LinearRegression()

print("\nModel Created Successfully:")
print(mlr)


# ============================================================
# STEP 7: TRAIN THE MODEL
# ============================================================

# fit() trains the model using training data.
#
# X_train = Training input features
# y_train = Actual training target values

mlr.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")


# ============================================================
# STEP 8: UNDERSTAND THE MODEL COEFFICIENTS
# ============================================================

# coef_ contains one coefficient for each input feature.
# intercept_ represents B0 in the regression equation.

print("\nModel Intercept (B0):")
print(mlr.intercept_)

print("\nModel Coefficients:")

# Display the coefficient associated with each feature.
for feature, coefficient in zip(X.columns, mlr.coef_):
    print(f"{feature}: {coefficient}")

# The learned equation has the form:
#
# Final_Marks =
#     Intercept
#     + (Study_Hours coefficient * Study_Hours)
#     + (Attendance coefficient * Attendance)
#     + (Previous_Marks coefficient * Previous_Marks)


# ============================================================
# STEP 9: MAKE PREDICTIONS
# ============================================================

# predict() uses the trained model to predict final marks
# for the input features in X_test.

y_pred = mlr.predict(X_test)

print("\nActual Marks:")
print(y_test.head())

print("\nPredicted Marks:")
print(y_pred[:5])


# ============================================================
# STEP 10: COMPARE ACTUAL AND PREDICTED VALUES
# ============================================================

# Create a DataFrame to compare actual marks with predictions.
#
# X_test.index is retained so that the rows correspond
# to the original dataset records.

results = pd.DataFrame({
    "Study_Hours": X_test["Study_Hours"],
    "Attendance": X_test["Attendance"],
    "Previous_Marks": X_test["Previous_Marks"],
    "Actual_Marks": y_test,
    "Predicted_Marks": y_pred
})

print("\nActual vs Predicted Marks:")
print(results.head())

# Optional: reset the index for easier viewing.
results = results.reset_index(drop=True)


# ============================================================
# STEP 11: EVALUATE THE MODEL
# ============================================================

# MAE = Mean Absolute Error
# Measures the average absolute difference between
# actual and predicted values.
# Lower MAE is generally better.

mae = mean_absolute_error(y_test, y_pred)


# MSE = Mean Squared Error
# Measures the average squared prediction error.
# Lower MSE is generally better.

mse = mean_squared_error(y_test, y_pred)


# RMSE = Root Mean Squared Error
# Expresses the prediction error in the target's units.

rmse = mse ** 0.5


# R2 Score = Coefficient of Determination
# Indicates how well the model explains the variation
# in the target values.
#
# A score closer to 1 generally indicates a better fit.
# R2 can be negative when the model performs poorly.

r2 = r2_score(y_test, y_pred)


print("\nModel Evaluation Metrics:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


# ============================================================
# STEP 12: PREDICT MARKS FOR A NEW STUDENT
# ============================================================

# Create a new student's input data.
#
# IMPORTANT:
# Use the same feature names and order as the training data.
# Values below are examples, not real student records.

new_student = pd.DataFrame({
    "Study_Hours": [7.5],
    "Attendance": [85.0],
    "Previous_Marks": [75.0]
})

# Predict the student's final marks.
predicted_marks = mlr.predict(new_student)

print("\nNew Student Details:")
print(new_student)

print("\nPredicted Final Marks:")
print(predicted_marks[0])


# ============================================================
# STEP 13: VISUALIZE ACTUAL VS PREDICTED MARKS
# ============================================================

# This scatter plot compares actual and predicted marks.
#
# X-axis = Actual final marks
# Y-axis = Predicted final marks
#
# Points closer to the diagonal line represent predictions
# closer to the actual values.

plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    y_pred,
    label="Predictions"
)

# Find the range shared by both axes.
min_value = min(y_test.min(), y_pred.min())
max_value = max(y_test.max(), y_pred.max())

# Perfect predictions would lie on this diagonal line.
plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--",
    label="Perfect Prediction"
)

plt.xlabel("Actual Final Marks")
plt.ylabel("Predicted Final Marks")

plt.title("Multiple Linear Regression: Actual vs Predicted Marks")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# ============================================================
# STEP 14: FEATURE IMPORTANCE THROUGH COEFFICIENTS
# ============================================================

# Display the learned coefficients in a bar chart.
#
# Note:
# Coefficients are not automatically feature importance scores.
# Their magnitudes depend on the units and scales of features.

coefficient_data = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": mlr.coef_
})

plt.figure(figsize=(8, 5))

plt.bar(
    coefficient_data["Feature"],
    coefficient_data["Coefficient"]
)

plt.xlabel("Input Features")
plt.ylabel("Learned Coefficient")

plt.title("Multiple Linear Regression Coefficients")

plt.xticks(rotation=20)
plt.grid(axis="y")

plt.tight_layout()
plt.show()


# ============================================================
# STEP 15: COMPLETE WORKFLOW SUMMARY
# ============================================================

# 1. Load the dataset using pandas.
# 2. Separate input features (X) and target (y).
# 3. Split the data into training and testing sets.
# 4. Create the LinearRegression model.
# 5. Train the model using fit().
# 6. Predict values using predict().
# 7. Compare actual and predicted values.
# 8. Evaluate using MAE, MSE, RMSE, and R2.
# 9. Predict the final marks of a new student.
# 10. Visualize the results.
#
# ============================================================
# END OF MULTIPLE LINEAR REGRESSION
# ============================================================