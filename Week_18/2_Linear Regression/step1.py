import pandas as pd

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

print("\nTarget Variable (y):")
print(y)