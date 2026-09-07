from pydantic import BaseModel, AnyUrl, Field
from typing import Optional, List, Dict, Annotated

class Customer(BaseModel):
    name : Annotated[str, Field(max_length=10)] 
    age : int = Field(gt=18)
    address : Optional[str] = None
    products : List[str]
    contact : Dict[str,str]
    email : str                 #email : EmailStr
    website : AnyUrl

info = {
    "name" : "Ramesh", 
    "age" : 25, 
    "address" : "Hyderabad", 
    "products" : ["Laptop","Watch","Mobile"],
    "contact":{"mobile": "9876543210", "city": "Hyderabad"},
    "email" : "ramesh@gmail.com",
    "website" : "https://google.com"
    }

customer = Customer(**info)
print(customer)

# ##########################COMMENTED CODE EXPLANATION################################################
# Import required classes from Pydantic
from pydantic import BaseModel, AnyUrl, Field


# Import type hints from typing
from typing import Optional, List, Dict, Annotated


# ============================================================
# CUSTOMER MODEL
# ============================================================

# Create a Customer class
# BaseModel gives us Pydantic data validation
class Customer(BaseModel):

    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    # name must be a string
    # maximum length is 10 characters
    name: Annotated[
        str,
        Field(max_length=10)
    ]


    # --------------------------------------------------------
    # AGE
    # --------------------------------------------------------

    # age must be an integer
    # gt=18 means age must be greater than 18
    #
    # 18 -> Invalid ❌
    # 19 -> Valid ✅
    # 25 -> Valid ✅
    age: int = Field(gt=18)


    # --------------------------------------------------------
    # ADDRESS
    # --------------------------------------------------------

    # address is optional
    # It can contain a string or None
    #
    # If address is not provided,
    # the default value will be None
    address: Optional[str] = None


    # --------------------------------------------------------
    # PRODUCTS
    # --------------------------------------------------------

    # products must be a list
    # Every item inside the list must be a string
    #
    # Example:
    # ["Laptop", "Watch", "Mobile"]
    products: List[str]


    # --------------------------------------------------------
    # CONTACT
    # --------------------------------------------------------

    # contact must be a dictionary
    #
    # Dict[str, str] means:
    #
    # Key   -> string
    # Value -> string
    #
    # Example:
    # {
    #     "mobile": "9876543210",
    #     "city": "Hyderabad"
    # }
    contact: Dict[str, str]


    # --------------------------------------------------------
    # EMAIL
    # --------------------------------------------------------

    # email is a normal string
    #
    # This does NOT perform email validation.
    #
    # If we want email validation,
    # we can use EmailStr:
    #
    # from pydantic import EmailStr
    # email: EmailStr
    email: str


    # --------------------------------------------------------
    # WEBSITE
    # --------------------------------------------------------

    # AnyUrl validates whether the value
    # is a valid URL
    #
    # Example:
    # https://google.com
    website: AnyUrl


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

# Create a dictionary containing customer information
info = {

    "name": "Ramesh",

    "age": 25,

    "address": "Hyderabad",

    "products": [
        "Laptop",
        "Watch",
        "Mobile"
    ],

    "contact": {
        "mobile": "9876543210",
        "city": "Hyderabad"
    },

    "email": "ramesh@gmail.com",

    "website": "https://google.com"
}


# ============================================================
# CREATE CUSTOMER OBJECT
# ============================================================

# **info means dictionary unpacking
#
# Customer(**info)
#
# is the same as:
#
# Customer(
#     name="Ramesh",
#     age=25,
#     address="Hyderabad",
#     products=["Laptop", "Watch", "Mobile"],
#     contact={
#         "mobile": "9876543210",
#         "city": "Hyderabad"
#     },
#     email="ramesh@gmail.com",
#     website="https://google.com"
# )

customer = Customer(**info)


# Print the Customer object
print(customer)


# ============================================================
# FINAL SUMMARY
# ============================================================

# 1. BaseModel
#    -> Used to create a Pydantic model.
#
#    class Customer(BaseModel):
#
#    Pydantic will validate the data
#    according to the fields defined in the model.


# 2. Annotated
#    -> Allows us to add extra information or validation
#       to a type.
#
#    Example:
#
#    name: Annotated[
#        str,
#        Field(max_length=10)
#    ]
#
#    This means:
#    name must be a string
#    AND
#    name can have maximum 10 characters.


# 3. Field()
#    -> Used to add validation rules.
#
#    Example:
#
#    Field(max_length=10)
#    -> Maximum 10 characters
#
#    Field(gt=18)
#    -> Value must be greater than 18


# 4. Optional
#    -> Means a value can be present or None.
#
#    Example:
#
#    address: Optional[str] = None
#
#    This means:
#    address can be a string
#    OR
#    address can be None.


# 5. List[str]
#    -> Means a list containing strings.
#
#    Example:
#
#    products: List[str]
#
#    ["Laptop", "Watch", "Mobile"]  -> Valid ✅


# 6. Dict[str, str]
#    -> Means a dictionary where:
#
#       Key   = string
#       Value = string
#
#    Example:
#
#    {
#        "mobile": "9876543210",
#        "city": "Hyderabad"
#    }


# 7. AnyUrl
#    -> Used to validate URLs.
#
#    Example:
#
#    website: AnyUrl
#
#    "https://google.com" -> Valid ✅


# 8. str
#    -> Normal string type.
#
#    Example:
#
#    email: str
#
#    It only checks that the value is a string.
#    It does NOT check whether it is a valid email.


# 9. EmailStr
#    -> Used when we want Pydantic to validate
#       an email address.
#
#    Example:
#
#    email: EmailStr


# 10. **info
#     -> Dictionary unpacking.
#
#     Customer(**info)
#
#     converts dictionary data into keyword arguments
#     and sends them to the Customer model.


# ============================================================
# COMPLETE FLOW
# ============================================================

# info dictionary
#       ↓
# Customer(**info)
#       ↓
# Pydantic receives the data
#       ↓
# Pydantic checks each field
#       ↓
# name      -> str + max_length=10
# age       -> int + greater than 18
# address   -> str or None
# products  -> List[str]
# contact   -> Dict[str, str]
# email     -> str
# website   -> valid URL
#       ↓
# If everything is valid
#       ↓
# Customer object is created
#       ↓
# print(customer)