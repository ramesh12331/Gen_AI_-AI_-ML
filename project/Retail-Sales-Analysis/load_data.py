import pandas as pd

from database import engine


file_path = (
    "data/processed/retail_sales_cleaned.csv"
)


# Read CSV

df = pd.read_csv(
    file_path
)


print("CSV loaded successfully!")

print(
    "Total rows:",
    len(df)
)


# Rename columns

df = df.rename(
    columns={
        "Order_ID": "order_id",
        "Order_Date": "order_date",
        "Customer": "customer",
        "Gender": "gender",
        "City": "city",
        "Region": "region",
        "Category": "category",
        "Product": "product",
        "Quantity": "quantity",
        "Unit_Price": "unit_price",
        "Discount": "discount",
        "Sales_Amount": "sales_amount"
    }
)


# Convert date

df["order_date"] = pd.to_datetime(
    df["order_date"]
).dt.date


# Insert into PostgreSQL

df.to_sql(
    "retail_sales",
    con=engine,
    if_exists="append",
    index=False,
    method="multi"
)


print(
    "Data inserted into PostgreSQL successfully!"
)