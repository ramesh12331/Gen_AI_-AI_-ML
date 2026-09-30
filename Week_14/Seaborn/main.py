import pandas as pd

data = {
    "Employee_ID": range(101, 121),

    "Age": [
        22, 25, 28, 30, 24,
        27, 32, 29, 35, 26,
        31, 23, 38, 34, 28,
        25, 40, 33, 29, 36
    ],

    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],

    "Department": [
        "IT", "HR", "Finance", "IT", "Sales",
        "IT", "Finance", "HR", "IT", "Sales",
        "IT", "Finance", "Sales", "IT", "HR",
        "Finance", "IT", "Sales", "HR", "IT"
    ],

    "Experience": [
        1, 2, 4, 6, 2,
        3, 8, 5, 10, 3,
        7, 1, 12, 9, 4,
        2, 11, 6, 5, 13
    ],

    "Salary": [
        28000, 320000, 45000, 60000, 35000,
        42000, 75000, 52000, 95000, 40000,
        68000, 30000, 110000, 85000, 48000,
        36000, 100000, 62000, 55000, 120000
    ],

    "Performance": [
        65, 72, 80, 88, 70,
        78, 91, 85, 95, 74,
        89, 68, 96, 92, 81,
        73, 94, 87, 83, 97
    ],

    "Work_Mode": [
        "Remote", "Office", "Hybrid", "Remote", "Office",
        "Hybrid", "Remote", "Office", "Hybrid", "Remote",
        "Office", "Hybrid", "Remote", "Office", "Hybrid",
        "Remote", "Office", "Hybrid", "Remote", "Office"
    ],

    "City": [
        "Hyderabad", "Bangalore", "Chennai", "Hyderabad", "Pune",
        "Bangalore", "Hyderabad", "Chennai", "Bangalore", "Pune",
        "Hyderabad", "Chennai", "Bangalore", "Hyderabad", "Pune",
        "Bangalore", "Hyderabad", "Chennai", "Bangalore", "Pune"
    ],

    "Joining_Month": [
        "Jan", "Feb", "Mar", "Apr", "May",
        "Jun", "Jul", "Aug", "Sep", "Oct",
        "Nov", "Dec", "Jan", "Feb", "Mar",
        "Apr", "May", "Jun", "Jul", "Aug"
    ]
}

df = pd.DataFrame(data)

# print(df.head())

#categorical columns:
result = df.select_dtypes(include='object').columns
print(result)

result = df.select_dtypes(include='number').columns
print(result)

# ===================================================

import matplotlib.pyplot as plt
import seaborn as sns

# sns.histplot(x='Salary',data = df,kde=True)
# plt.show()

# sns.kdeplot(x='Salary',data = df, fill=True, color='red')
# sns.boxplot(x='Salary',data = df)

# for col in df.select_dtypes(include='number').columns:
#     sns.histplot(x=col, data=df, kde=True)
#     plt.show()
# =====================================
# for col in df.select_dtypes(include='number').columns:
#     print("Current column:", col)

#     sns.histplot(x=col, data=df, kde=True)
#     plt.show()

# ======================================
# print(df.head())
# col = ['red','black','green','yellow']
# sns.countplot(x='Department', data=df,palette=col, hue='Department', legend=False)
# plt.show()

# ======================================
# sns.barplot(x='City', y='Salary', data = df, estimator='median', hue='Gender')
# sns.scatterplot(x='Experience',y='Salary',data = df)
# sns.scatterplot(x='Experience',y='Performance',data = df)
# sns.regplot(x='Experience',y='Performance',data = df)
# sns.boxplot(x='Department',y='Salary',data = df)
# sns.violinplot(x='Department',y='Salary',data=df)
# plt.show()
# ===============================================
# sns.scatterplot(
#     data = df,
#     x='Experience',
#     y='Salary',
#     hue = "Gender",
#     #style='Department'
#     size = 'Performance'
# )
# plt.legend(loc="upper right")
# plt.show()
# ================================================
# sns.pairplot(df[['Age','Experience','Salary','Performance','Gender']],hue ='Gender')
# plt.show()
# ===============================================
print('\n Corroletion')
corr = df.select_dtypes(include='number').corr()
print(corr)

sns.heatmap(corr, annot=True)
plt.show()