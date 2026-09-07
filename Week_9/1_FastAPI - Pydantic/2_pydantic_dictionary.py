from pydantic import BaseModel

class Customer(BaseModel):
    name : str
    age : int

info = {"name":"Ramesh", "age":25}

customer = Customer(**info)
print(customer)