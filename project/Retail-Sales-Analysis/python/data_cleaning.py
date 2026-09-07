import pandas as pd


input_file = (
    "data/raw/retail_sales.xlsx"
)

output_file = (
    "data/processed/retail_sales_cleaned.csv"
)


df = pd.read_excel(
    input_file
)


print("Original rows:", len(df))


# Remove duplicate records

df = df.drop_duplicates()


# Remove rows with missing values

df = df.dropna()


# Convert date

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"]
)


# Convert numeric columns

df["Quantity"] = pd.to_numeric(
    df["Quantity"]
)

df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"]
)

df["Discount"] = pd.to_numeric(
    df["Discount"]
)

df["Sales_Amount"] = pd.to_numeric(
    df["Sales_Amount"]
)


# Save cleaned data

df.to_csv(
    output_file,
    index=False
)


print("Cleaning completed!")

print(
    "Cleaned rows:",
    len(df)
)

print(
    f"File saved: {output_file}"
)