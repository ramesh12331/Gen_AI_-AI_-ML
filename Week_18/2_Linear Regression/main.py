# ============================================================
# MACHINE LEARNING
# SIMPLE LINEAR REGRESSION
# STUDY HOURS VS STUDENT MARKS
# VS CODE FORMAT WITH COMMENTED EXPLANATION
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
# STEP 3: CREATE THE DATASET
# ============================================================

# Study_Hours represents the number of hours a student studies.
# Marks represents the marks obtained by the student.
#
# This dataset contains 10 student records.

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [25, 30, 40, 45, 50, 60, 65, 75, 80, 90]
}

# Convert the dictionary into a Pandas DataFrame.
df = pd.DataFrame(data)

# Display the complete dataset.
print("Complete Dataset:")
print(df)


# ============================================================
# STEP 4: SEPARATE INPUT (X) AND TARGET (y)
# ============================================================

# X represents the independent variable or input feature.
# Here, the input feature is Study_Hours.
#
# y represents the dependent variable or target.
# Here, the target is Marks.
#
# Double square brackets keep X as a DataFrame.

X = df[["Study_Hours"]]
y = df["Marks"]

print("\nInput Feature (X):")
print(X)

print("\nTarget Variable (y):")
print(y)


# ============================================================
# STEP 5: SPLIT DATA INTO TRAINING AND TESTING SETS
# ============================================================

# train_test_split() divides the dataset into two parts.
#
# X_train: Input features used to train the model.
# X_test: Input features used to test the model.
# y_train: Actual marks used during training.
# y_test: Actual marks used to evaluate predictions.
#
# test_size=0.2 means:
# 80% of the data is used for training.
# 20% of the data is used for testing.
#
# random_state=42 ensures that the split is reproducible.

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

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))


# ============================================================
# STEP 6: CREATE THE LINEAR REGRESSION MODEL
# ============================================================

# Linear Regression finds a straight-line relationship
# between an input feature and a numerical target.
#
# Mathematical equation:
#
# y = mx + c
#
# y = Predicted marks
# x = Study hours
# m = Slope or coefficient
# c = Intercept
#
# LinearRegression() creates the model object.

model = LinearRegression()


# ============================================================
# STEP 7: TRAIN THE MODEL
# ============================================================

# fit() trains the model using the training dataset.
#
# The model learns the relationship between study hours
# and marks by finding suitable coefficient and intercept values.

model.fit(X_train, y_train)

print("\nModel Training Completed!")


# ============================================================
# STEP 8: DISPLAY SLOPE AND INTERCEPT
# ============================================================

# coef_ returns the learned coefficient.
# Because this model has one input feature, we use coef_[0].
#
# intercept_ returns the constant term in the equation.

slope = model.coef_[0]
intercept = model.intercept_

print("\nSlope (Coefficient):", slope)
print("Intercept:", intercept)

print("\nLearned Regression Equation:")
print(f"Predicted Marks = {slope:.4f} * Study_Hours + {intercept:.4f}")


# ============================================================
# STEP 9: PREDICT MARKS FOR THE TEST DATA
# ============================================================

# predict() generates predictions using the trained model.
#
# X_test contains study hours that were not used for training.
# y_pred contains the corresponding predicted marks.

y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)


# ============================================================
# STEP 10: COMPARE ACTUAL AND PREDICTED MARKS
# ============================================================

# Create a DataFrame to compare actual marks with predictions.
#
# X_test.index is preserved so each prediction stays associated
# with the correct original student record.

result = pd.DataFrame({
    "Study_Hours": X_test["Study_Hours"],
    "Actual_Marks": y_test,
    "Predicted_Marks": y_pred
})

print("\nActual vs Predicted Results:")
print(result)


# ============================================================
# STEP 11: CALCULATE MAE, MSE, AND R2 SCORE
# ============================================================

# MAE = Mean Absolute Error.
#
# It calculates the average absolute difference between
# actual and predicted marks.
#
# Lower MAE generally indicates smaller prediction errors.

mae = mean_absolute_error(y_test, y_pred)


# MSE = Mean Squared Error.
#
# It calculates the average squared difference between
# actual and predicted marks.
#
# Larger errors receive a greater penalty because they are squared.

mse = mean_squared_error(y_test, y_pred)


# R2 Score = Coefficient of Determination.
#
# It measures how well the model explains the variation
# in the target values compared with predicting the test mean.
#
# A score closer to 1 generally indicates a better fit.
# A negative score means the model performed worse than
# predicting the test mean on the evaluated data.

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)


# ============================================================
# STEP 12: PREDICT MARKS FOR A NEW STUDENT
# ============================================================

# Suppose a new student studies for 7.5 hours.
#
# Create a DataFrame with the same feature name used
# when training the model.

new_student = pd.DataFrame({
    "Study_Hours": [7.5]
})

# Use the trained model to predict the student's marks.

predicted_marks = model.predict(new_student)

print("\nNew Student Study Hours: 7.5")
print("Predicted Marks:", predicted_marks[0])


# ============================================================
# STEP 13: VISUALIZE THE ACTUAL DATA
# ============================================================

# A scatter plot displays the actual student records.
#
# X-axis: Study hours
# Y-axis: Actual marks
#
# Each blue point represents one observation in the dataset.

plt.scatter(
    X["Study_Hours"],
    y,
    color="blue",
    label="Actual Marks"
)


# ============================================================
# STEP 14: DRAW THE BEST-FIT REGRESSION LINE
# ============================================================

# model.predict(X) predicts marks for all study-hour values.
#
# The red line represents the relationship learned by
# the Linear Regression model.

plt.plot(
    X["Study_Hours"],
    model.predict(X),
    color="red",
    label="Best-Fit Regression Line"
)


# ============================================================
# STEP 15: ADD GRAPH LABELS AND DISPLAY THE PLOT
# ============================================================

# Add labels to the X-axis and Y-axis.

plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Add a title to the graph.

plt.title("Simple Linear Regression: Study Hours vs Marks")

# Display the legend to identify the points and line.

plt.legend()

# Display grid lines to make the graph easier to read.

plt.grid(True)

# Display the completed graph.

plt.show()


# ============================================================
# STEP 16: COMPLETE WORKFLOW REVISION
# ============================================================

# 1. Create the dataset using Pandas.
# 2. Separate the input feature X and target y.
# 3. Split the dataset using train_test_split().
# 4. Create the model using LinearRegression().
# 5. Train the model using model.fit().
# 6. Display the coefficient and intercept.
# 7. Predict marks using model.predict().
# 8. Compare actual and predicted values.
# 9. Evaluate predictions using MAE, MSE, and R2.
# 10. Predict marks for a new student.
# 11. Visualize the actual data and regression line.
#
# ============================================================
# END OF SIMPLE LINEAR REGRESSION
# ============================================================