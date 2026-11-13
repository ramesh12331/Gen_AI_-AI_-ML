# ============================================================
# MACHINE LEARNING
# SIMPLE LINEAR REGRESSION
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
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ============================================================
# STEP 3: CREATE THE DATASET
# ============================================================

# Study_Hours = Input feature (X)
# Marks       = Target variable (y)
#
# The model will learn the relationship between
# study hours and student marks.

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks":       [25, 30, 40, 45, 50, 60, 65, 75, 80, 90]
}

# Convert the dictionary into a Pandas DataFrame.
df = pd.DataFrame(data)

print("Complete Dataset:")
print(df)


# ============================================================
# STEP 4: SEPARATE INPUT (X) AND OUTPUT (y)
# ============================================================

# X contains the input feature.
# Double square brackets keep X as a DataFrame.
X = df[["Study_Hours"]]

# y contains the target/output variable.
y = df["Marks"]

print("\nInput Feature (X):")
print(X)

print("\nTarget Variable (y):")
print(y)


# ============================================================
# STEP 5: SPLIT THE DATA INTO TRAINING AND TESTING SETS
# ============================================================

# Training data is used to teach the model.
# Testing data is used to evaluate its predictions.
#
# test_size=0.2 means:
# 80% of the data -> Training
# 20% of the data -> Testing
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

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))


# ============================================================
# STEP 6: CREATE THE LINEAR REGRESSION MODEL
# ============================================================

# Linear Regression finds the best-fit straight line.
#
# Mathematical equation:
#
# y = mx + c
#
# y = Predicted marks
# x = Study hours
# m = Slope (coefficient)
# c = Intercept
#
# The model learns m and c from the training data.

model = LinearRegression()


# ============================================================
# STEP 7: TRAIN THE MODEL
# ============================================================

# fit() trains the model using the training data.
# The model learns the relationship between study hours
# and marks.

model.fit(X_train, y_train)

print("\nModel Training Completed!")


# Display the learned parameters.
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)


# ============================================================
# STEP 8: MAKE PREDICTIONS ON THE TEST DATA
# ============================================================

# predict() estimates marks for the testing input.

y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)


# ============================================================
# STEP 9: COMPARE ACTUAL AND PREDICTED MARKS
# ============================================================

# Create a DataFrame to compare actual and predicted values.

results = pd.DataFrame({
    "Study_Hours": X_test["Study_Hours"].values,
    "Actual_Marks": y_test.values,
    "Predicted_Marks": y_pred
})

print("\nActual vs Predicted Results:")
print(results)


# ============================================================
# STEP 10: EVALUATE THE MODEL
# ============================================================

# MAE = Mean Absolute Error
# Measures the average absolute difference between
# actual and predicted marks.
# Lower MAE generally indicates better predictions.

mae = mean_absolute_error(y_test, y_pred)


# MSE = Mean Squared Error
# Measures the average squared prediction error.
# Lower MSE generally indicates better predictions.

mse = mean_squared_error(y_test, y_pred)


# R2 Score = Coefficient of Determination
# Measures how well the model explains variation
# in the target values.
# A score closer to 1 generally indicates a better fit.

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)


# ============================================================
# STEP 11: PREDICT MARKS FOR A NEW STUDENT
# ============================================================

# Suppose a new student studies for 7.5 hours.
# We use the trained model to predict their marks.

new_student = pd.DataFrame({
    "Study_Hours": [7.5]
})

predicted_marks = model.predict(new_student)

print("\nNew Student Study Hours: 7.5")
print("Predicted Marks:", predicted_marks[0])


# ============================================================
# STEP 12: VISUALIZE THE DATA AND REGRESSION LINE
# ============================================================

# Scatter plot:
# Displays the actual study-hour and marks observations.

plt.scatter(
    X["Study_Hours"],
    y,
    color="blue",
    label="Actual Marks"
)


# Regression line:
# Displays the model's predicted marks for each
# study-hour value in the dataset.

plt.plot(
    X["Study_Hours"],
    model.predict(X),
    color="red",
    label="Best-Fit Regression Line"
)


# Add labels and a title.

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression: Study Hours vs Marks")


# Display the legend and grid.

plt.legend()
plt.grid(True)


# Display the graph.

plt.show()


# ============================================================
# STEP 13: UNDERSTAND THE COMPLETE WORKFLOW
# ============================================================

# 1. Create the dataset.
# 2. Separate input (X) and target (y).
# 3. Split data into training and testing sets.
# 4. Create the Linear Regression model.
# 5. Train the model using fit().
# 6. Predict values using predict().
# 7. Compare actual values with predictions.
# 8. Evaluate the model using MAE, MSE, and R2.
# 9. Predict marks for a new student.
# 10. Visualize the regression line.
#
# IMPORTANT:
# This is a small educational dataset.
# The predictions show a learned relationship, not
# proof that studying for a particular number of hours
# guarantees a specific mark.
#
# ============================================================
# END OF SIMPLE LINEAR REGRESSION
# ============================================================