from pydantic import BaseModel, computed_field
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

@app.get("/")
def home():
    return{
        "message": "Welcome to FastAPI"
    }

@app.post("/create")
def create_customer(cust:Customer):
    return cust


# ########################COMMENTED EXPLANATION######################################

# ============================================================
# 1. IMPORTS
# ============================================================

# BaseModel:
# Used to create the Pydantic model.
#
# computed_field:
# Used when we want Pydantic to include a calculated
# value in the API response.
from pydantic import BaseModel, computed_field


# FastAPI:
# Used to create our API application.
from fastapi import FastAPI


# ============================================================
# 2. CREATE FASTAPI APPLICATION
# ============================================================

# Create the FastAPI application object.
app = FastAPI()


# ============================================================
# 3. CREATE CUSTOMER PYDANTIC MODEL
# ============================================================

# Customer is our Pydantic model.
#
# Think of Customer as a TEMPLATE.
#
# It defines what customer data we expect from the user.
class Customer(BaseModel):

    # Customer ID must be a string
    customer_id: str

    # Customer name must be a string
    customer_name: str

    # Age must be an integer
    age: int

    # City must be a string
    city: str

    # Product must be a string
    product: str

    # Category must be a string
    category: str

    # Quantity must be an integer
    quantity: int

    # Price of ONE product must be an integer
    price: int


    # ========================================================
    # 4. COMPUTED FIELD
    # ========================================================

    # @property:
    # Allows us to use total_price like an attribute.
    #
    # @computed_field:
    # Tells Pydantic to include this calculated value
    # in the output/response.
    @computed_field
    @property
    def total_price(self) -> int:

        # Calculate total price.
        #
        # Example:
        # quantity = 2
        # price = 50000
        #
        # total_price = 2 * 50000
        #             = 100000
        return self.quantity * self.price


# ============================================================
# 5. GET API
# ============================================================

# @app.get("/")
# Creates a GET endpoint.
#
# URL:
# http://127.0.0.1:8000/
@app.get("/")
def home():

    # Return a JSON response.
    return {
        "message": "Welcome to FastAPI"
    }


# ============================================================
# 6. POST API
# ============================================================

# @app.post("/create")
# Creates a POST endpoint.
#
# URL:
# http://127.0.0.1:8000/create
#
# cust: Customer
#
# Customer = Pydantic model / TEMPLATE
#
# cust = VARIABLE containing the actual data
#        sent by the user.
@app.post("/create")
def create_customer(cust: Customer):

    # Return the customer data.
    #
    # Because total_price is a @computed_field,
    # Pydantic will also include total_price
    # in the response.
    return cust


# ============================================================
# FINAL SUMMARY
# ============================================================

# BaseModel
#     ↓
# Creates our Pydantic model.
#
#
# Customer
#     ↓
# Acts as a TEMPLATE for customer data.
#
#
# cust
#     ↓
# Is the VARIABLE containing actual customer data.
#
#
# quantity
#     ↓
# Number of products purchased.
#
#
# price
#     ↓
# Price of ONE product.
#
#
# total_price
#     ↓
# Automatically calculated field.
#
# Formula:
#
#     total_price = quantity * price
#
#
# ============================================================
# EXAMPLE
# ============================================================
#
# User sends:
#
# {
#     "customer_id": "C001",
#     "customer_name": "Ramesh",
#     "age": 25,
#     "city": "Hyderabad",
#     "product": "Laptop",
#     "category": "Electronics",
#     "quantity": 2,
#     "price": 50000
# }
#
#
# FastAPI receives the data.
#             ↓
# Pydantic validates the data.
#             ↓
# Data is stored in "cust".
#             ↓
# computed_field calculates:
#
#     quantity * price
#
#     2 * 50000
#         ↓
#     100000
#
#             ↓
# API returns:
#
# {
#     "customer_id": "C001",
#     "customer_name": "Ramesh",
#     "age": 25,
#     "city": "Hyderabad",
#     "product": "Laptop",
#     "category": "Electronics",
#     "quantity": 2,
#     "price": 50000,
#     "total_price": 100000
# }
#
#
# ============================================================
# IMPORTANT
# ============================================================
#
# The user DOES NOT need to send total_price.
#
# The user only sends:
#
#     quantity
#     price
#
# FastAPI/Pydantic calculates:
#
#     total_price
#
# automatically.
#
#
# So:
#
# User data
#     ↓
# quantity = 2
# price = 50000
#     ↓
# computed_field
#     ↓
# total_price = 100000
#
# ============================================================

# ============================================================
# FINAL SUMMARY
# ============================================================

# 1. BaseModel
#    ↓
#    Used to create the Pydantic model.
#
#
# 2. Customer
#    ↓
#    This is our Pydantic MODEL / TEMPLATE.
#
#    It defines the fields:
#
#        customer_id
#        customer_name
#        age
#        city
#        product
#        category
#        quantity
#        price
#
#
# 3. cust
#    ↓
#    This is a VARIABLE.
#
#    It contains the actual customer data
#    sent by the user.
#
#
# 4. @computed_field
#    ↓
#    Tells Pydantic that total_price is a
#    calculated field and should be included
#    in the API response.
#
#
# 5. @property
#    ↓
#    Allows us to access total_price like
#    an attribute instead of calling it like
#    a normal function.
#
#
# 6. def total_price(self) -> int:
#
#    Let's understand each part:
#
#    def
#       ↓
#       Used to define/create a Python function.
#
#
#    total_price
#       ↓
#       This is the NAME of our function.
#
#       It represents the calculated total price.
#
#
#    self
#       ↓
#       "self" represents the CURRENT CUSTOMER OBJECT.
#
#       Through self, we can access the values
#       stored inside the Customer object.
#
#       For example:
#
#           self.quantity
#           self.price
#
#
#    -> int
#       ↓
#       This is the RETURN TYPE HINT.
#
#       It tells us that the function is expected
#       to return an integer value.
#
#
#    So:
#
#        def total_price(self) -> int:
#
#    means:
#
#        Create a function called total_price
#        that works with the current Customer object
#        and returns an integer value.
#
#
# 7. return self.quantity * self.price
#    ↓
#    Performs the calculation.
#
#    self.quantity
#       ↓
#       Gets quantity from the current customer.
#
#    self.price
#       ↓
#       Gets price from the current customer.
#
#    *
#       ↓
#       Multiplication operator.
#
#
#    Example:
#
#        quantity = 2
#        price = 50000
#
#        self.quantity * self.price
#
#        2 * 50000
#        ↓
#        100000
#
#
# 8. Complete flow
#
#    User sends:
#
#        quantity = 2
#        price = 50000
#
#             ↓
#
#    Customer model receives the data
#
#             ↓
#
#    cust contains the customer object
#
#             ↓
#
#    total_price is calculated
#
#             ↓
#
#    self.quantity * self.price
#
#             ↓
#
#    2 * 50000
#
#             ↓
#
#    total_price = 100000
#
#
# ============================================================
# VERY IMPORTANT
# ============================================================
#
# User DOES NOT send total_price.
#
# User sends:
#
#     quantity
#     price
#
# The API calculates:
#
#     total_price
#
# automatically.
#
#
# Example input:
#
# {
#     "quantity": 2,
#     "price": 50000
# }
#
#
# Calculated:
#
#     total_price = 2 * 50000
#                 = 100000
#
#
# ============================================================
# SIMPLE MEANING
# ============================================================
#
# def total_price(self) -> int:
#
#     def
#     → create a function
#
#     total_price
#     → function name
#
#     self
#     → current Customer object
#
#     -> int
#     → function returns an integer
#
#
# return self.quantity * self.price
#     → calculate and return total price
#
# ============================================================