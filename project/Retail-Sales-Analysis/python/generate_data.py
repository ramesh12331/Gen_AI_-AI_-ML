import pandas as pd
import numpy as np


np.random.seed(42)


number_of_records = 1000


customers = [
    "Ramesh",
    "Suresh",
    "Anjali",
    "Vijay",
    "Kiran",
    "Priya",
    "Rahul",
    "Sneha"
]


genders = [
    "Male",
    "Female"
]


cities = [
    "Hyderabad",
    "Bangalore",
    "Chennai",
    "Mumbai",
    "Delhi",
    "Pune"
]


regions = [
    "South",
    "West",
    "North"
]


categories = [
    "Electronics",
    "Furniture",
    "Grocery",
    "Clothing"
]


products = [
    "Laptop",
    "Mobile",
    "Chair",
    "Table",
    "Rice",
    "Oil",
    "Shirt",
    "Shoes"
]


df = pd.DataFrame({

    "Order_ID": range(
        1001,
        1001 + number_of_records
    ),

    "Order_Date": pd.date_range(
        start="2026-01-01",
        periods=number_of_records,
        freq="D"
    ),

    "Customer": np.random.choice(
        customers,
        number_of_records
    ),

    "Gender": np.random.choice(
        genders,
        number_of_records
    ),

    "City": np.random.choice(
        cities,
        number_of_records
    ),

    "Region": np.random.choice(
        regions,
        number_of_records
    ),

    "Category": np.random.choice(
        categories,
        number_of_records
    ),

    "Product": np.random.choice(
        products,
        number_of_records
    ),

    "Quantity": np.random.randint(
        1,
        6,
        number_of_records
    ),

    "Unit_Price": np.random.randint(
        500,
        50000,
        number_of_records
    ),

    "Discount": np.random.choice(
        [0, 0.05, 0.10, 0.15],
        number_of_records
    )
})


df["Sales_Amount"] = (
    df["Quantity"]
    * df["Unit_Price"]
    * (1 - df["Discount"])
)


file_path = (
    "data/raw/retail_sales.xlsx"
)


df.to_excel(
    file_path,
    index=False
)


print(
    f"Data generated successfully: {file_path}"
)

print(
    f"Total records: {len(df)}"
)