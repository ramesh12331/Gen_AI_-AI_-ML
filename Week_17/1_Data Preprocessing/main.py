import pandas as pd

data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55],
    "Salary": [25000, 30000, 45000, 50000, 60000, 75000, 90000, 120000],
    "Monthly_Spend": [1000, 1500, 2000, 2500, 3000, 4000, 5000, 15000],
    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female"
    ],
    "Plan": [
        "Basic", "Standard", "Premium", "Basic",
        "Standard", "Premium", "Basic", "Premium"
    ],
    "Satisfaction": [
        "Low", "Medium", "High", "Medium",
        "Low", "High", "Medium", "High"
    ],
    "Churn": [
        "No", "No", "Yes", "No",
        "Yes", "No", "Yes", "Yes"
    ]
}

df = pd.DataFrame(data)
print(df.head())