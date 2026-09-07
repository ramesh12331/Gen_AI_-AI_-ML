from pydantic import BaseModel, computed_field, field_validator
from fastapi import FastAPI

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

@app.get("/")
def home():
    return{
        "message": "Welcome to FastAPI"
    }

@app.post("/create")
def create_customer(cust:Customer):
    return cust
