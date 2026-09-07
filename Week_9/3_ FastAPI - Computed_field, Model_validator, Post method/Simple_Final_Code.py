from pydantic import BaseModel, computed_field, field_validator
from fastapi import FastAPI
import json


app = FastAPI()


# Customer data model
class Customer(BaseModel):

    customer_id: str
    customer_name: str
    age: int
    city: str
    product: str
    category: str
    quantity: int
    price: int

    # Automatically calculate total price
    @computed_field
    @property
    def total_price(self) -> int:
        return self.quantity * self.price

    # Convert customer name to uppercase
    @field_validator("customer_name")
    @classmethod
    def name_transform(cls, value):
        return value.upper()


# Read data from data.json
def load_data():

    try:
        with open("data.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save data into data.json
def save_data(data):

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# Home API
@app.get("/")
def home():

    return {
        "message": "Welcome to FastAPI"
    }


# Create customer API
@app.post("/create")
def create_customer(cust: Customer):

    # Get existing data
    data = load_data()

    # Add new customer
    data.append(cust.model_dump())

    # Save updated data
    save_data(data)

    return {
        "message": "Customer created successfully"
    }