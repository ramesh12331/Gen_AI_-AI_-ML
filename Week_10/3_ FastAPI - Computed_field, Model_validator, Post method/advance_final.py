from pydantic import BaseModel, Field, computed_field, field_validator
from fastapi import FastAPI, HTTPException
from typing import Annotated
import json
import os


app = FastAPI()


# ============================================================
# 1. FILE PATH
# ============================================================

# data.json file location
FILE_NAME = "main_data.json"


# ============================================================
# 2. CUSTOMER MODEL
# ============================================================

class Customer(BaseModel):

    customer_id: Annotated[str, Field(min_length=3)]
    customer_name: Annotated[str, Field(min_length=2)]
    age: Annotated[int, Field(ge=18, le=100)]
    city: Annotated[str, Field(min_length=2)]
    product: Annotated[str, Field(min_length=2)]
    category: Annotated[str, Field(min_length=2)]
    quantity: Annotated[int, Field(gt=0)]
    price: Annotated[int, Field(gt=0)]


    # --------------------------------------------------------
    # COMPUTED FIELD
    # --------------------------------------------------------

    @computed_field
    @property
    def total_price(self) -> int:

        # Calculate total price automatically
        return self.quantity * self.price


    # --------------------------------------------------------
    # FIELD VALIDATOR
    # --------------------------------------------------------

    @field_validator("customer_name")
    @classmethod
    def name_transform(cls, value):

        # Remove unnecessary spaces
        value = value.strip()

        # Convert name to uppercase
        return value.upper()


    # --------------------------------------------------------
    # CITY VALIDATOR
    # --------------------------------------------------------

    @field_validator("city")
    @classmethod
    def city_transform(cls, value):

        # Remove spaces
        value = value.strip()

        # Convert city to title case
        return value.title()


# ============================================================
# 3. LOAD DATA
# ============================================================

def load_data():

    # If file does not exist,
    # return an empty list.
    if not os.path.exists(FILE_NAME):
        return []


    try:

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:

        # If JSON file is empty or invalid,
        # return empty list.
        return []


# ============================================================
# 4. SAVE DATA
# ============================================================

def save_data(data):

    with open(FILE_NAME, "w") as file:

        # Convert Python list into JSON
        json.dump(data, file, indent=4)


# ============================================================
# 5. FIND CUSTOMER
# ============================================================

def find_customer(customer_id):

    # Load all customers
    data = load_data()

    # Search customer one by one
    for customer in data:

        if customer["customer_id"] == customer_id:
            return customer

    # Customer not found
    return None


# ============================================================
# 6. HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Welcome to Advanced FastAPI"
    }


# ============================================================
# 7. CREATE CUSTOMER
# ============================================================

@app.post("/create")
def create_customer(cust: Customer):

    # Load existing customers
    data = load_data()


    # Check whether customer ID already exists
    if find_customer(cust.customer_id):

        raise HTTPException(
            status_code=400,
            detail="Customer ID already exists"
        )


    # Convert Pydantic object into dictionary
    customer_data = cust.model_dump()


    # Add new customer
    data.append(customer_data)


    # Save data
    save_data(data)


    return {
        "message": "Customer created successfully",
        "customer": customer_data
    }


# ============================================================
# 8. GET ALL CUSTOMERS
# ============================================================

@app.get("/customers")
def get_customers():

    # Read all customers
    data = load_data()

    return {
        "count": len(data),
        "customers": data
    }


# ============================================================
# 9. GET CUSTOMER BY ID
# ============================================================

@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):

    # Find customer
    customer = find_customer(customer_id)


    # If customer doesn't exist
    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )


    return customer


# ============================================================
# 10. DELETE CUSTOMER
# ============================================================

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str):

    # Load existing data
    data = load_data()


    # Find customer
    customer = find_customer(customer_id)


    # Customer doesn't exist
    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )


    # Remove customer
    data.remove(customer)


    # Save updated data
    save_data(data)


    return {
        "message": "Customer deleted successfully"
    }