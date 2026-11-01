import pandas as pd
from sklearn.model_selection import train_test_split

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

