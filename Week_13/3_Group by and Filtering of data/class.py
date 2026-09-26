import pandas as pd
import numpy as np
 
np.random.seed(42)
 
n = 100
 
data = {
    "employee_id": range(1001, 1001 + n),
 
    "age": np.random.randint(21, 56, n),
 
    "experience_years": np.random.randint(0, 21, n),
 
    "salary": np.random.randint(25000, 100001, n),
 
    "working_hours": np.round(np.random.normal(8, 1, n), 1),
 
    "projects_completed": np.random.randint(1, 16, n),
 
    "performance_score": np.round(
        np.random.normal(7, 1.2, n), 2
    ),
 
    "training_hours": np.random.randint(5, 101, n),
 
    "monthly_sales": np.random.randint(20000, 200001, n),
 
    "satisfaction_score": np.round(
        np.random.uniform(1, 10, n), 2
    )
}
 
df = pd.DataFrame(data)
 
# --------------------------------------------------
# Adding intentional outliers
# --------------------------------------------------
 
df.loc[[5, 25, 75], "age"] = [70, 75, 80]
 
df.loc[[10, 40, 90], "experience_years"] = [35, 40, 45]
 
df.loc[[15, 50, 85], "salary"] = [250000, 300000, 350000]
 
df.loc[[20, 60, 95], "working_hours"] = [15, 16, 18]
 
df.loc[[30, 70, 99], "projects_completed"] = [40, 50, 60]
 
df.loc[[35, 65, 88], "performance_score"] = [0.5, 0.2, 0.1]
 
df.loc[[45, 80, 98], "training_hours"] = [250, 300, 350]
 
df.loc[[55, 77, 93], "monthly_sales"] = [500000, 600000, 700000]
 
df.loc[[12, 42, 82], "satisfaction_score"] = [15, 18, 20]
 
print(df.head())

# df.groupby('country').mean()