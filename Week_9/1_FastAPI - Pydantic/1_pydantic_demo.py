from pydantic import BaseModel 

class Customer(BaseModel):
    name:str
    age:int

customer = Customer(
    name = "Ramesh",
    age = 25
)

print(customer)