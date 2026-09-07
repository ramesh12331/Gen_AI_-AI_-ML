import pandas as pd

from database import engine


query = """
SELECT *
FROM retail_sales
"""


df = pd.read_sql(
    query,
    engine
)


print("\n========== RETAIL SALES ANALYSIS ==========\n")


print(
    "Total Sales:",
    df["sales_amount"].sum()
)


print(
    "Total Orders:",
    df["order_id"].nunique()
)


print(
    "Total Quantity:",
    df["quantity"].sum()
)


print("\nCategory-wise Sales:")

category_sales = (
    df.groupby("category")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)


print(category_sales)


print("\nCity-wise Sales:")

city_sales = (
    df.groupby("city")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)


print(city_sales)