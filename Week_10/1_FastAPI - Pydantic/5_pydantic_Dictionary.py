from pydantic import BaseModel
from typing import Optional,List,Dict

class Customer(BaseModel):
    name:str
    age:int
    address:Optional[str] = None
    products:List[str]
    contact:Dict[str,str]

info = {"name":"Ramesh", "age":25, "products":["Laptop","Watch","Mobile"], "contact":{"mobile": "9876543210", "city": "Hyderabad"}}

customer = Customer(**info)
print(customer)

# ##############################COMMENTED CODE EXPLANATION##############################################################
# Import BaseModel from Pydantic
# BaseModel is used to create a Pydantic model
from pydantic import BaseModel


# Import Optional, List, and Dict from typing
#
# Optional → value can be present or None
# List     → used for a list of values
# Dict     → used for key-value pairs
from typing import Optional, List, Dict


# Create a Customer model
# Customer inherits from Pydantic's BaseModel
class Customer(BaseModel):

    # name must be a string
    # Example: "Ramesh"
    name: str

    # age must be an integer
    # Example: 25
    age: int

    # address is optional
    # If address is not provided, the default value is None
    address: Optional[str] = None

    # products must be a list
    # Every item inside the list must be a string
    #
    # Example:
    # ["Laptop", "Watch", "Mobile"]
    products: List[str]

    # contact must be a dictionary
    #
    # Dict[str, str] means:
    # Key   → string
    # Value → string
    #
    # Example:
    # {
    #     "mobile": "9876543210",
    #     "city": "Hyderabad"
    # }
    contact: Dict[str, str]


# Create customer information using a dictionary
info = {
    "name": "Ramesh",
    "age": 25,
    "products": ["Laptop", "Watch", "Mobile"],
    "contact": {
        "mobile": "9876543210",
        "city": "Hyderabad"
    }
}


# Create a Customer object
#
# **info means dictionary unpacking.
#
# Customer(**info) is the same as:
#
# Customer(
#     name="Ramesh",
#     age=25,
#     products=["Laptop", "Watch", "Mobile"],
#     contact={
#         "mobile": "9876543210",
#         "city": "Hyderabad"
#     }
# )
#
# Pydantic checks whether the data matches
# the types defined in the Customer model.
customer = Customer(**info)


# Print the Customer object
print(customer)