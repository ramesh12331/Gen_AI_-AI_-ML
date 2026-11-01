import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [25, 30, 40, 45, 50, 60, 65, 75, 80, 90]
}

df = pd.DataFrame(data)
print("Complete Dataset:")
print(df)

X = df[["Study_Hours"]]
y = df["Marks"]

print("\nInput Feature (X):")
print(X)

print("\nTarget Variable (y):"),
print(y)

# ========================================
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

# =====================================
model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Training Completed!")
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# ======================================
y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

# =======================================
result = pd.DataFrame({
    "Study_Hours": X_test["Study_Hours"].values,
    "Actual_Marks": y_test.values,
    "Predicted_Marks": y_pred
})

print("\nActual vs Predicted Results:")
print(result)

# =======================================
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)

# =======================================
new_student = pd.DataFrame({
    "Study_Hours": [7.5]
})

predicted_marks = model.predict(new_student)

print("\nNew Student Study Hours: 7.5")
print("Predicted Marks:", predicted_marks[0])

# ===========================================
plt.scatter(
    X["Study_Hours"],
    y,
    color = "blue",
    label = "Actual Marks"
)

plt.plot(
    X["Study_Hours"],
    model.predict(X),
    color="red",
    label="Best-Fit Regression Line"
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.title("Simple Linear Regression: Study Hours vs Marks")

plt.legend()
plt.grid(True)

plt.show()