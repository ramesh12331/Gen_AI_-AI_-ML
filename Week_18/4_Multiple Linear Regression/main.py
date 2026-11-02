import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_marks_2000.csv")

print(df.head())

# ===================================
X = df.drop(columns = "Final_Marks")
y = df["Final_Marks"]
print(X)
print("Final Marks Column",y)

# ==================================
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)
print(X_train[0:5])

# ===================================
mlr = LinearRegression()
mlr.fit(X_train, y_train)

y_pred = mlr.predict(X_test)

print("Actual_Values", y_test[0:5])
print("Y PREDICTION VALUES:", y_pred[0:5])
print("Co-efficient: ", mlr.coef_)
print("INTERCEPT : ", mlr.intercept_)

# ======================================
new_student = pd.DataFrame({
    "Study_Hours" : [6.5],
    "Attendance" : [85],
    "Previous_Marks" : [75]
})

prediction = mlr.predict(new_student)
print("Predicted Final Marks :", prediction[0])
# =======================================
mse = mean_squared_error(y_test, y_pred)
print("MEAN SQUARE ERROR :",mse)


# ========================================
cv_scores = cross_val_score(mlr, X_train, y_train, cv = 5, scoring="r2")
print("Individual fold scores :", cv_scores)
print("Mean R2 : ", cv_scores.mean())
print("Standard Deviation :", cv_scores.std())

# ========================================
plt.figure(figsize=(7,6))
plt.scatter(y_test, y_pred, alpha=0.6)

min_value = min(y_test.min(), y_pred.min())
max_value = max(y_test.max(), y_pred.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value]
    
)

plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted: Multiple Linear Regression")
plt.tight_layout()
plt.show()