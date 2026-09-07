from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    name : str
    age : int
    address : Optional[str] = None

info = {"name" : "Ramesh", "age": 25}

customer = Customer(**info)

print(customer)