from pydantic import BaseModel, computed_field, field_validator
from fastapi import FastAPI
import json

app = FastAPI()

class Customer(BaseModel):
    customer_id: str
    customer_name: str
    age: int
    city: str
    product: str
    category: str
    quantity: int
    price: int

    @computed_field
    @property
    def total_price(self) -> int:
        return self.quantity*self.price

    @field_validator("customer_name")
    @classmethod
    def name_transform(cls, value):
        return value.upper()

def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data,file,indent=4)

@app.get("/")
def home():
    return{
        "message": "Welcome to FastAPI"
    }

@app.post("/create")
def create_customer(cust:Customer):
    data = load_data()

    data.append(
        cust.model_dump()
    )

    save_data(data)

    return{
        "message": "Customer created successfully"
    }