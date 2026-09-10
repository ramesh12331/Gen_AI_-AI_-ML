from pydantic import BaseModel
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

@app.get("/")
def home():
    return{
        "message": "Welcome to FastAPI"
    }

@app.post("/create")
def create_customer(cust:Customer):
    return cust


# #####################COMMENTED CODE WITH EXPLANATION#######################################
# ============================================================
# 1. IMPORTS
# ============================================================

# BaseModel is used to create a Pydantic data model.
# Pydantic validates the data sent by the user.
from pydantic import BaseModel


# FastAPI is used to create our API application.
from fastapi import FastAPI


# ============================================================
# 2. CREATE FASTAPI APPLICATION
# ============================================================

# Create the FastAPI application object.
app = FastAPI()


# ============================================================
# 3. CREATE PYDANTIC MODEL
# ============================================================

# Customer is a Pydantic model.
#
# Think of Customer as a TEMPLATE.
#
# It tells FastAPI:
# "Whenever somebody sends customer data,
#  the data should contain these fields."
class Customer(BaseModel):

    # customer_id should be a string
    customer_id: str

    # customer_name should be a string
    customer_name: str

    # age should be an integer
    age: int

    # city should be a string
    city: str

    # product should be a string
    product: str

    # category should be a string
    category: str

    # quantity should be an integer
    quantity: int

    # price should be an integer
    price: int


# ============================================================
# 4. GET API
# ============================================================

# @app.get("/") creates a GET API.
#
# When we open:
# http://127.0.0.1:8000/
#
# FastAPI will execute the home() function.
@app.get("/")
def home():

    # Return a JSON response.
    return {
        "message": "Welcome to FastAPI"
    }


# ============================================================
# 5. POST API
# ============================================================

# @app.post("/create") creates a POST API.
#
# The URL is:
# http://127.0.0.1:8000/create
#
# POST is normally used when we want to SEND/CREATE data.
@app.post("/create")
def create_customer(cust: Customer):

    # cust is a VARIABLE.
    #
    # Customer is the Pydantic MODEL/TEMPLATE.
    #
    # cust contains the actual customer data
    # sent by the user.
    #
    # FastAPI uses the Customer model to validate
    # the data before putting it into cust.

    # Return the customer data.
    return cust


# ============================================================
# FINAL SUMMARY
# ============================================================

# 1. BaseModel
#    |
#    |-- Used to create the Customer data model.
#
#
# 2. Customer
#    |
#    |-- This is the TEMPLATE/STRUCTURE.
#    |
#    |-- It defines:
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
#    |
#    |-- This is a VARIABLE.
#    |
#    |-- It contains the ACTUAL customer data
#        received from the user.
#
#
# 4. @app.post("/create")
#    |
#    |-- Creates a POST endpoint.
#    |
#    |-- User sends customer data to /create.
#
#
# 5. cust: Customer
#    |
#    |-- Means:
#        "The data received in cust must follow
#         the Customer Pydantic model."
#
#
# 6. Pydantic validation
#    |
#    |-- Checks the data types.
#    |
#    |-- Example:
#        age: int
#        means age should be an integer.
#
#
# 7. return cust
#    |
#    |-- Sends the received customer data back
#        as the API response.
#
#
# ============================================================
# DATA FLOW
# ============================================================
#
# User / Swagger
#       |
#       | JSON data
#       ↓
# POST /create
#       |
#       ↓
# Customer Model
#       |
#       | Validation
#       ↓
# cust variable
#       |
#       ↓
# return cust
#       |
#       ↓
# JSON Response
#
#
# IMPORTANT:
#
# This code DOES NOT save data permanently.
#
# There is NO data.json in this code.
#
# The data only comes into the API,
# gets validated,
# is stored temporarily in the cust variable,
# and is returned.
#
# To permanently save the data, we need to add:
#
#     data.json
#
# and use Python's:
#
#     json.load()
#     json.dump()
#
# ============================================================