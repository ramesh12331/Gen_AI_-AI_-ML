# ============================================================
# MULTIPLE LINEAR REGRESSION
# Student Final Marks Prediction
# ============================================================


# ============================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================

import pandas as pd

# train_test_split:
# Used to divide the dataset into training data and testing data.
#
# cross_val_score:
# Used to perform Cross Validation.
from sklearn.model_selection import train_test_split, cross_val_score

# LinearRegression:
# This is the Machine Learning algorithm we are using.
from sklearn.linear_model import LinearRegression

# mean_squared_error:
# Used to calculate the Mean Squared Error (MSE).
#
# r2_score:
# Used to calculate the R² score.
from sklearn.metrics import mean_squared_error, r2_score

# matplotlib:
# Used to create graphs and visualizations.
import matplotlib.pyplot as plt


# ============================================================
# STEP 2: LOAD THE CSV DATASET
# ============================================================

# Read the CSV file using pandas.
#
# "df" means DataFrame.
# A DataFrame is a table containing rows and columns.
df = pd.read_csv("student_marks_2000.csv")


# Display the first 5 rows of the dataset.
#
# head() returns the first 5 rows by default.
print("First 5 Rows:")
print(df.head())


# ============================================================
# STEP 3: SEPARATE INPUT FEATURES (X) AND TARGET (y)
# ============================================================

# Our dataset contains:
#
# Study_Hours
# Attendance
# Previous_Marks
# Final_Marks
#
# We want to predict Final_Marks.
#
# Therefore:
#
# X = Input Features
# y = Target / Output


# Remove the Final_Marks column from the DataFrame.
#
# The remaining columns become our input features.
X = df.drop(columns="Final_Marks")


# Select only the Final_Marks column.
#
# This is our target variable.
y = df["Final_Marks"]


# Display the input features.
print("\nInput Features (X):")
print(X)


# Display the target variable.
print("\nTarget Variable (y):")
print(y)


# ============================================================
# STEP 4: SPLIT DATA INTO TRAINING AND TESTING DATA
# ============================================================

# Machine Learning models should not be tested on the
# same data that they used for learning.
#
# Therefore, we divide our dataset into:
#
# Training Data → Used to train the model
# Testing Data  → Used to evaluate the model
#
# test_size=0.2 means:
#
# 80% → Training data
# 20% → Testing data
#
# random_state=0 ensures we get the same split every time.


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)


# Display training input data.
print("\nX_train:")
print(X_train.head())


# Display testing input data.
print("\nX_test:")
print(X_test.head())


# Display training target values.
print("\ny_train:")
print(y_train.head())


# Display testing target values.
print("\ny_test:")
print(y_test.head())


# ============================================================
# STEP 5: CREATE THE MULTIPLE LINEAR REGRESSION MODEL
# ============================================================

# Create a LinearRegression object.
#
# "mlr" means Multiple Linear Regression.
mlr = LinearRegression()


# ============================================================
# STEP 6: TRAIN THE MODEL
# ============================================================

# fit() trains the Machine Learning model.
#
# X_train → Input features
# y_train → Correct answers / target values
#
# The model learns the relationship between:
#
# Study_Hours
# Attendance
# Previous_Marks
#
# and:
#
# Final_Marks

mlr.fit(X_train, y_train)


# ============================================================
# STEP 7: MAKE PREDICTIONS
# ============================================================

# predict() uses the trained model to predict
# Final_Marks for the testing data.

y_pred = mlr.predict(X_test)


# Display the actual values.
print("\nActual Values:")
print(y_test.head())


# Display the predicted values.
print("\nPredicted Values:")
print(y_pred[:5])


# ============================================================
# STEP 8: DISPLAY MODEL COEFFICIENTS
# ============================================================

# coef_ contains the coefficient for every input feature.
#
# We have 3 input features:
#
# Study_Hours
# Attendance
# Previous_Marks
#
# Therefore, we get 3 coefficients.

print("\nCoefficients:")
print(mlr.coef_)


# ============================================================
# STEP 9: DISPLAY INTERCEPT
# ============================================================

# intercept_ represents the starting value of the
# regression equation.

print("\nIntercept:")
print(mlr.intercept_)


# ============================================================
# STEP 10: UNDERSTAND THE REGRESSION EQUATION
# ============================================================

# Multiple Linear Regression equation:
#
# y = b0 + b1*x1 + b2*x2 + b3*x3
#
# In our project:
#
# Final_Marks =
#
# Intercept
# + Study_Hours coefficient × Study_Hours
# + Attendance coefficient × Attendance
# + Previous_Marks coefficient × Previous_Marks


print("\nRegression Equation:")

print(
    f"Final_Marks = "
    f"{mlr.intercept_:.4f} + "
    f"{mlr.coef_[0]:.4f} × Study_Hours + "
    f"{mlr.coef_[1]:.4f} × Attendance + "
    f"{mlr.coef_[2]:.4f} × Previous_Marks"
)


# ============================================================
# STEP 11: PREDICT MARKS FOR A NEW STUDENT
# ============================================================

# Let's create data for a new student.
#
# Study Hours     = 6.5
# Attendance      = 85
# Previous Marks  = 75

new_student = pd.DataFrame({
    "Study_Hours": [6.5],
    "Attendance": [85],
    "Previous_Marks": [75]
})


# Use the trained model to predict the student's
# Final Marks.

prediction = mlr.predict(new_student)


# Display the prediction.
print("\nPredicted Final Marks:")
print(prediction[0])


# ============================================================
# STEP 12: CALCULATE MEAN SQUARED ERROR (MSE)
# ============================================================

# MSE = Mean Squared Error
#
# It measures how far the predicted values are
# from the actual values.
#
# Smaller MSE = Better model
#
# Formula:
#
# MSE = 1/n × Σ(actual - predicted)²

mse = mean_squared_error(y_test, y_pred)


# Display MSE.
print("\nMean Squared Error:")
print(mse)


# ============================================================
# STEP 13: CALCULATE R² SCORE
# ============================================================

# R² tells us how well the model explains the
# variation in the target variable.
#
# R² closer to 1 → Better
#
# R² closer to 0 → Poorer
#
# R² can also be negative for a very poor model.

r2 = r2_score(y_test, y_pred)


# Display R².
print("\nR² Score:")
print(r2)


# ============================================================
# STEP 14: CROSS VALIDATION
# ============================================================

# Instead of testing the model only once,
# Cross Validation tests the model multiple times.
#
# cv=5 means:
#
# The training data is divided into 5 parts.
#
# The model is trained and tested 5 times.
#
# Each time a different part is used for validation.


cv_scores = cross_val_score(
    mlr,
    X_train,
    y_train,
    cv=5,
    scoring="r2"
)


# Display the R² score from each fold.
print("\nIndividual Fold R² Scores:")
print(cv_scores)


# Calculate the average R² score.
#
# mean() calculates the average.
mean_cv = cv_scores.mean()

print("\nMean Cross Validation R²:")
print(mean_cv)


# Calculate the standard deviation.
#
# std() tells us how much the scores vary
# between different folds.

std_cv = cv_scores.std()

print("\nCross Validation Standard Deviation:")
print(std_cv)


# ============================================================
# STEP 15: ACTUAL VS PREDICTED GRAPH
# ============================================================

# Create a new figure.
#
# figsize=(7,6)
# means:
# width = 7
# height = 6

plt.figure(figsize=(7, 6))


# Create a scatter plot.
#
# X-axis → Actual Marks
# Y-axis → Predicted Marks
#
# Each dot represents one student.

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)


# ============================================================
# STEP 16: CREATE PERFECT PREDICTION LINE
# ============================================================

# Find the smallest value between:
#
# Actual Marks
# Predicted Marks

min_value = min(
    y_test.min(),
    y_pred.min()
)


# Find the largest value between:
#
# Actual Marks
# Predicted Marks

max_value = max(
    y_test.max(),
    y_pred.max()
)


# Draw a diagonal line.
#
# This line represents PERFECT prediction.
#
# Example:
#
# Actual = 70
# Predicted = 70
#
# The point would be exactly on this line.

plt.plot(
    [min_value, max_value],
    [min_value, max_value]
)


# ============================================================
# STEP 17: ADD GRAPH LABELS
# ============================================================

# Label for X-axis.
plt.xlabel("Actual Marks")


# Label for Y-axis.
plt.ylabel("Predicted Marks")


# Graph title.
plt.title(
    "Actual vs Predicted: Multiple Linear Regression"
)


# Automatically adjust the spacing.
plt.tight_layout()


# Display the graph.
plt.show()