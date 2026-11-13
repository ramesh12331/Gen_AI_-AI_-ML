# ============================================================
# MACHINE LEARNING
# SIMPLE LINEAR REGRESSION
# VS CODE - COMPLETE PYTHON PROGRAM
# ============================================================

# ============================================================
# STEP 0: INSTALL REQUIRED LIBRARIES
# ============================================================

# Open the VS Code terminal and run:
#
# pip install pandas numpy matplotlib scikit-learn
#
# You only need to install these libraries once.


# ============================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Split the dataset into training and testing data
from sklearn.model_selection import train_test_split

# Import the Simple Linear Regression model
from sklearn.linear_model import LinearRegression

# Import evaluation metrics
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# STEP 2: CREATE THE DATASET
# ============================================================

# Study_Hours = Input feature (X)
# Marks       = Output/target (y)
#
# Goal:
# Predict student marks based on study hours.

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks":       [25, 30, 40, 45, 50, 60, 65, 75, 80, 90]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the complete dataset
print("\n========== DATASET ==========")
print(df)


# ============================================================
# STEP 3: UNDERSTAND INPUT (X) AND OUTPUT (y)
# ============================================================

# X = Independent variable / Input feature
# y = Dependent variable / Output target
#
# Here:
# X = Study Hours
# y = Student Marks
#
# Capital X is normally used for input features.
# Lowercase y is normally used for the target.

X = df[["Study_Hours"]]

y = df["Marks"]

print("\n========== INPUT FEATURES (X) ==========")
print(X)

print("\n========== TARGET VALUES (y) ==========")
print(y)


# ============================================================
# STEP 4: SPLIT DATA INTO TRAINING AND TESTING SETS
# ============================================================

# Training data:
# Used by the model to learn the relationship.
#
# Testing data:
# Used to evaluate the model on data it did not train on.
#
# test_size=0.2 means 20% testing data and 80% training data.
#
# random_state=42 makes the split reproducible.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n========== TRAINING INPUTS ==========")
print(X_train)

print("\n========== TESTING INPUTS ==========")
print(X_test)

print("\n========== TRAINING TARGETS ==========")
print(y_train)

print("\n========== TESTING TARGETS ==========")
print(y_test)

print("\nNumber of training samples:", len(X_train))
print("Number of testing samples:", len(X_test))


# ============================================================
# STEP 5: CREATE THE LINEAR REGRESSION MODEL
# ============================================================

# Simple Linear Regression equation:
#
# y = mx + b
#
# y = Predicted output
# x = Input feature
# m = Slope / Coefficient
# b = Intercept / Offset
#
# The model learns the best-fit straight line
# from the training data.

model = LinearRegression()

print("\nLinear Regression model created successfully.")


# ============================================================
# STEP 6: TRAIN THE MODEL
# ============================================================

# fit() trains the model using the training data.
#
# The model learns the slope (m) and intercept (b).

model.fit(X_train, y_train)

print("\n========== MODEL TRAINING ==========")
print("Model trained successfully!")


# ============================================================
# STEP 7: FIND SLOPE (m) AND INTERCEPT (b)
# ============================================================

# coef_[0] gives the slope for our single input feature.
#
# intercept_ gives the intercept.
#
# Equation:
# y = mx + b

m = model.coef_[0]

b = model.intercept_

print("\n========== LINEAR REGRESSION EQUATION ==========")

print("Slope (m):", m)

print("Intercept (b):", b)

print(f"Equation: Marks = {m:.2f} * Study_Hours + {b:.2f}")


# ============================================================
# STEP 8: PREDICT MARKS USING TEST DATA
# ============================================================

# predict() uses the trained model to predict output values.
#
# X_test contains study hours that were not used for training.

y_pred = model.predict(X_test)

print("\n========== ACTUAL VS PREDICTED MARKS ==========")

# Create a DataFrame to compare actual and predicted values
comparison = pd.DataFrame({
    "Study_Hours": X_test["Study_Hours"].values,
    "Actual_Marks": y_test.values,
    "Predicted_Marks": np.round(y_pred, 2)
})

print(comparison)


# ============================================================
# STEP 9: EVALUATE MODEL PERFORMANCE
# ============================================================

# Metrics help us understand how well the model predicts.
#
# MAE = Mean Absolute Error
# MSE = Mean Squared Error
# RMSE = Root Mean Squared Error
# R²  = R-squared score
#
# Lower MAE, MSE, and RMSE generally indicate smaller errors.
# R² closer to 1 generally indicates a better fit.
#
# Always interpret metrics in the context of your dataset.

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")

print(f"Mean Absolute Error (MAE): {mae:.2f}")

print(f"Mean Squared Error (MSE): {mse:.2f}")

print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

print(f"R-squared Score (R2): {r2:.4f}")


# ============================================================
# STEP 10: PREDICT MARKS FOR NEW STUDY HOURS
# ============================================================

# Now use the trained model to predict marks
# for a student who studies for 8 hours.

new_student = pd.DataFrame({
    "Study_Hours": [8]
})

predicted_marks = model.predict(new_student)

print("\n========== NEW STUDENT PREDICTION ==========")

print("Study Hours:", new_student["Study_Hours"].iloc[0])

print(f"Predicted Marks: {predicted_marks[0]:.2f}")


# ============================================================
# STEP 11: PREDICT MARKS FOR MULTIPLE STUDY HOURS
# ============================================================

# Predict marks for students studying
# for 2, 5, 7, and 10 hours.

new_students = pd.DataFrame({
    "Study_Hours": [2, 5, 7, 10]
})

predicted_values = model.predict(new_students)

prediction_results = pd.DataFrame({
    "Study_Hours": new_students["Study_Hours"],
    "Predicted_Marks": np.round(predicted_values, 2)
})

print("\n========== MULTIPLE PREDICTIONS ==========")

print(prediction_results)


# ============================================================
# STEP 12: VISUALIZE THE DATA AND REGRESSION LINE
# ============================================================

# Scatter plot:
# Shows the actual data points.
#
# Regression line:
# Shows the relationship learned by the model.
#
# The model predicts a straight-line relationship
# between study hours and marks.

plt.figure(figsize=(10, 6))

# Plot the actual data points
plt.scatter(
    X["Study_Hours"],
    y,
    color="blue",
    label="Actual Marks",
    s=80
)

# Predict values for the regression line
line_predictions = model.predict(X)

# Plot the best-fit regression line
plt.plot(
    X["Study_Hours"],
    line_predictions,
    color="red",
    linewidth=2,
    label="Regression Line"
)

# Add chart title and labels
plt.title("Simple Linear Regression: Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.legend()

plt.grid(True)

# Display the graph
plt.show()


# ============================================================
# STEP 13: VISUALIZE ACTUAL VS PREDICTED TEST VALUES
# ============================================================

plt.figure(figsize=(10, 6))

# Actual test values
plt.scatter(
    X_test["Study_Hours"],
    y_test,
    color="blue",
    s=100,
    label="Actual Marks"
)

# Predicted test values
plt.scatter(
    X_test["Study_Hours"],
    y_pred,
    color="red",
    marker="x",
    s=100,
    label="Predicted Marks"
)

plt.title("Actual Marks vs Predicted Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.legend()

plt.grid(True)

plt.show()


# ============================================================
# STEP 14: UNDERSTAND THE COMPLETE WORKFLOW
# ============================================================

# 1. Create the dataset.
#
# 2. Separate input (X) and output (y).
#
# 3. Split data using train_test_split().
#
# 4. Create LinearRegression().
#
# 5. Train the model using model.fit().
#
# 6. Learn the slope (m) and intercept (b).
#
# 7. Predict using model.predict().
#
# 8. Evaluate predictions using MAE, MSE, RMSE, and R2.
#
# 9. Visualize the actual data and regression line.
#
# 10. Predict marks for new study-hour values.


# ============================================================
# SIMPLE LINEAR REGRESSION - PROGRAM COMPLETED
# ============================================================