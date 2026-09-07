from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated
import json


app = FastAPI()


# ============================================================
# PYDANTIC MODEL
# ============================================================

class Customer(BaseModel):

    customer_id: Annotated[str, Field()]
    customer_name: Annotated[str, Field()]
    age: Annotated[int, Field()]
    city: Annotated[str, Field()]
    product: Annotated[str, Field()]
    category: Annotated[str, Field()]
    quantity: Annotated[int, Field()]
    price: Annotated[int, Field()]

    # --------------------------------------------------------
    # Field Validator
    # --------------------------------------------------------
    @field_validator("customer_name")
    @classmethod
    def name_transform(cls, value):
        return value.upper()

    # --------------------------------------------------------
    # Computed Field
    # --------------------------------------------------------
    @computed_field
    @property
    def total_price(self) -> int:
        return self.quantity * self.price


# ============================================================
# LOAD DATA FROM JSON
# ============================================================

def load_data():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# ============================================================
# SAVE DATA INTO JSON
# ============================================================

def save_data(data):

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# ============================================================
# CREATE CUSTOMER
# ============================================================

@app.post("/create")
def create_customer(cust: Customer):

    # 1. Load existing data
    data = load_data()

    # 2. Check whether customer already exists
    for customer in data:

        if customer["customer_id"] == cust.customer_id:

            raise HTTPException(
                status_code=400,
                detail="Customer already exists"
            )

    # 3. Add new customer
    data.append(cust.model_dump())

    # 4. Save updated data
    save_data(data)

    # 5. Return response
    return JSONResponse(
        status_code=201,
        content={
            "message": "Customer created successfully"
        }
    )