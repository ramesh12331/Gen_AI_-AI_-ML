import pandas as pd 

#nested dict

data = {
    "student_id": {
        1: 101,
        2: 102,
        3: 103,
        4: 104,
        5: 105,
        6: 106,
        7: 107,
        8: 108,
        9: 109,
        10: 110,
        11: 111,
        12: 112,
        13: 113,
        14: 114,
        15: 115
    },
 
    "name": {
        1: "Rahul",
        2: "Priya",
        3: "Arjun",
        4: "Sneha",
        5: "Kiran",
        6: "Anjali",
        7: "Vijay",
        8: "Pooja",
        9: "Ravi",
        10: "Meena",
        11: "Suresh",
        12: "Divya",
        13: "Naveen",
        14: "Asha",
        15: "Rohit"
    },
 
    "age": {
        1: 21,
        2: 22,
        3: 20,
        4: 23,
        5: 21,
        6: 22,
        7: 24,
        8: 20,
        9: 23,
        10: 21,
        11: 25,
        12: 22,
        13: 24,
        14: 20,
        15: 23
    },
 
    "course": {
        1: "Python",
        2: "Data Science",
        3: "Power BI",
        4: "Python",
        5: "SQL",
        6: "Data Science",
        7: "Power BI",
        8: "Python",
        9: "SQL",
        10: "Data Science",
        11: "Python",
        12: "Power BI",
        13: "SQL",
        14: "Python",
        15: "Data Science"
    },
 
    "marks": {
        1: 85,
        2: 92,
        3: 78,
        4: 88,
        5: 75,
        6: 95,
        7: 82,
        8: 89,
        9: 72,
        10: 91,
        11: 84,
        12: 79,
        13: 87,
        14: 93,
        15: 81
    }
}
 
# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(data)

print("Before Rename:")
print(df.head())


# ============================================================
# RENAME COLUMN
# ============================================================

df.rename(
    columns={"student_id": "id"},
    inplace=True
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\nAfter Rename:")
print(df.head())


# ============================================================
# RENAME INDEX
# ============================================================

df.rename(
    index={2: 20},
    inplace=True
)

print("\nAfter Index Rename:")
print(df.head())

# df.reset_index(inplace=True)

# print(df)

df.reset_index(drop=True, inplace=True)
print(df)

# df.drop(columns=['name'], axis=0, inplace=True)
# print(df)

df.drop(columns=['name', 'age', 'course'], axis=0, inplace=True)
print(df)

df.drop(index=range(1,10),inplace=True)
print(df)

# ==============
df = pd.read_excel("D:/RAMESH/Gen_AI_ AI_ ML/Week_13/2_Pandas - Accessing of data, Handling missing values and outliers/messy_dataset.xlsx")
print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df.dtypes)
print(df.sample(10))

# ======================
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.histplot(x="Age", data=df, kde=True)
# plt.show()

df['Age'] = df['Age'].fillna(df["Age"].median())
print(df['Age'].median())

# =========================
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.histplot(x="Salary", data=df, kde=True)
# plt.show()

print("\n Null Values")
print(df.isnull().sum())

df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print(df["Salary"].median())

print(df.isnull().sum())

# =========================
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.boxplot(x="Rating", data=df)
# plt.show()

df["Rating"] = df["Rating"].fillna(df["Rating"].median())
print(df["Rating"].median())

print(df.isnull().sum())

# # =========================
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.boxplot(x="Rating", data=df)
# plt.show()

df["Department"].value_counts()
# print(df.isnull())
print(df["Department"].value_counts())

df["Department"] = df["Department"].fillna("unknown")

print(df["Department"])

print(df.isnull().sum())

# Access
print(df[["Name","City"]])
print(df.loc[2])
print(df.loc[0:4])

# Access rows, columns
print(df.columns.tolist())
print(df.loc[0:8:2])
result = df.loc[0:8, "EmployeeID":"Rating":2]

print(result)
# result = df.iloc[0:7, 0::2]

# print(result)

# Add column
df['Age1'] = df["Age"] + 20
print(df.head())

df['new_salary'] =df["Salary"].apply(lambda x:x+100000)
print(df.head())