from pydantic import BaseModel
from typing import Optional, List

class Customer(BaseModel):
    name : str
    age : int
    address : Optional[str] = None
    products : List[str]
info = {"name":"Ramesh", "age" : 25, "address" : "Hyderabad", "products" : ["Laptop","Mobile", "Watch"]}

customer = Customer(**info)
print(customer)

# ==========================COMMENTED CODE EXPLANATION===========================================

# Import BaseModel from Pydantic
# BaseModel is used to create a Pydantic model
from pydantic import BaseModel


# Import Optional and List from typing
# Optional → a field can have a value or None
# List → used to create a list of values
from typing import Optional, List


# Create a Customer class
# By inheriting from BaseModel, Pydantic will validate our data
class Customer(BaseModel):

    # name must be a string
    # Example: "Ramesh"
    name: str

    # age must be an integer
    # Example: 25
    age: int

    # address is optional
    # We can provide an address or leave it as None
    # Default value is None
    address: Optional[str] = None

    # products must be a list
    # Every item inside the list must be a string
    # Example: ["Laptop", "Mobile", "Watch"]
    products: List[str]


# Create a dictionary containing customer information
info = {
    "name": "Ramesh",
    "age": 25,
    "address": "Hyderabad",
    "products": ["Laptop", "Mobile", "Watch"]
}


# Create a Customer object using the dictionary
# **info means dictionary unpacking
#
# This:
# Customer(**info)
#
# is the same as:
# Customer(
#     name="Ramesh",
#     age=25,
#     address="Hyderabad",
#     products=["Laptop", "Mobile", "Watch"]
# )
#
# Pydantic will check whether the data matches
# the types defined in the Customer model.
customer = Customer(**info)


# Print the Customer object
print(customer)