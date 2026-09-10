from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field
)

from typing import (
    List,
    Dict,
    Optional,
    Annotated
)


class Customer(BaseModel):

    name: Annotated[
        str,
        Field(
            max_length=12,
            title="name of the customer",
            description="heyy give me your name"
        )
    ]

    email: EmailStr

    linkedin_url: AnyUrl

    age: Annotated[
        int,
        Field(
            gt=20,
            lt=60,
            strict=True
        )
    ]

    price: Annotated[
        int,
        Field(
            gt=15000
        )
    ]

    products: Optional[List[str]] = "kuch nahi liya"

    contact_details: Dict[str, str]

info = {
    "name": "Anwar",
    "email": "anwar@gmail.com",
    "linkedin_url": "https://linkedin.com/in/anwar",
    "age": 43,
    "price": 20000,
    "products": [
        "Laptop",
        "Mobile"
    ],
    "contact_details": {
        "mob": "9390669636",
        "city": "Hyderabad"
    }
}

cust1 = Customer(**info)

print(cust1)

# ######################################################################################
# Import BaseModel from Pydantic
# BaseModel is used to create a Pydantic model
from pydantic import (
    BaseModel,
    EmailStr,       # Used to validate email addresses
    AnyUrl,         # Used to validate URLs
    Field           # Used to add validation rules and metadata
)


# Import different types from typing
from typing import (
    List,           # Used for lists
    Dict,           # Used for dictionaries
    Optional,       # Value can be a specific type or None
    Annotated       # Used to add extra information to a type
)


# Create a Customer model
# Customer inherits from BaseModel
class Customer(BaseModel):

    # ---------------------------------------
    # NAME
    # ---------------------------------------

    # name must be a string
    #
    # Annotated allows us to add extra rules
    # using Field()
    name: Annotated[
        str,

        Field(
            # Maximum length of name is 12 characters
            max_length=12,

            # Title of this field
            title="name of the customer",

            # Description of this field
            description="heyy give me your name"
        )
    ]


    # ---------------------------------------
    # EMAIL
    # ---------------------------------------

    # EmailStr validates whether the value
    # is a valid email address
    #
    # Example:
    # anwar@gmail.com       ✅
    # anwar@gmail           ❌
    email: EmailStr


    # ---------------------------------------
    # LINKEDIN URL
    # ---------------------------------------

    # AnyUrl validates whether the value
    # is a valid URL
    #
    # Example:
    # https://linkedin.com/in/anwar
    linkedin_url: AnyUrl


    # ---------------------------------------
    # AGE
    # ---------------------------------------

    age: Annotated[
        int,

        Field(
            # Age must be greater than 20
            # 20 is NOT allowed
            gt=20,

            # Age must be less than 60
            # 60 is NOT allowed
            lt=60,

            # strict=True means Pydantic will not
            # convert another type into int
            strict=True
        )
    ]


    # ---------------------------------------
    # PRICE
    # ---------------------------------------

    price: Annotated[
        int,

        Field(
            # Price must be greater than 15000
            # 15000 is NOT allowed
            gt=15000
        )
    ]


    # ---------------------------------------
    # PRODUCTS
    # ---------------------------------------

    # products can contain a list of strings
    # OR it can be None
    #
    # Example:
    # ["Laptop", "Mobile"]
    #
    # If products are not provided,
    # the default value will be None.
    products: Optional[List[str]] = None


    # ---------------------------------------
    # CONTACT DETAILS
    # ---------------------------------------

    # contact_details must be a dictionary
    #
    # Dict[str, str] means:
    #
    # Key   → string
    # Value → string
    #
    # Example:
    #
    # {
    #     "mob": "9390669636",
    #     "city": "Hyderabad"
    # }
    contact_details: Dict[str, str]


# ---------------------------------------
# CUSTOMER INFORMATION
# ---------------------------------------

# Create a dictionary containing customer data
info = {

    "name": "Anwar",

    "email": "anwar@gmail.com",

    "linkedin_url": "https://linkedin.com/in/anwar",

    "age": 43,

    "price": 20000,

    "products": [
        "Laptop",
        "Mobile"
    ],

    "contact_details": {
        "mob": "9390669636",
        "city": "Hyderabad"
    }
}


# ---------------------------------------
# CREATE CUSTOMER OBJECT
# ---------------------------------------

# **info means dictionary unpacking
#
# This:
#
# Customer(**info)
#
# is the same as:
#
# Customer(
#     name="Anwar",
#     email="anwar@gmail.com",
#     linkedin_url="https://linkedin.com/in/anwar",
#     age=43,
#     price=20000,
#     products=["Laptop", "Mobile"],
#     contact_details={
#         "mob": "9390669636",
#         "city": "Hyderabad"
#     }
# )

cust1 = Customer(**info)


# Print the customer object
print(cust1)