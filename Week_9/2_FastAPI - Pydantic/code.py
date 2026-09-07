# ============================================================
# IMPORTS
# ============================================================

from pydantic import (
    BaseModel,
    EmailStr,
    AnyUrl,
    Field,
    field_validator,
    model_validator,
    computed_field
)

from typing import (
    List,
    Dict,
    Optional,
    Annotated
)


# ============================================================
# ADDRESS MODEL
# ============================================================

# Address is a separate Pydantic model.
#
# We will use this model INSIDE the Customer model.
#
# This is called a NESTED PYDANTIC MODEL.
class Address(BaseModel):

    # City must be a string
    city: str

    # State must be a string
    state: str


# ============================================================
# CUSTOMER MODEL
# ============================================================

class Customer(BaseModel):

    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    # name must be a string
    #
    # max_length=12
    # means maximum 12 characters are allowed.
    name: Annotated[
        str,
        Field(
            max_length=12,
            title="name of the customer",
            description="heyy give me your name"
        )
    ]


    # --------------------------------------------------------
    # EMAIL
    # --------------------------------------------------------

    # EmailStr checks whether the email format is valid.
    email: EmailStr


    # --------------------------------------------------------
    # LINKEDIN URL
    # --------------------------------------------------------

    # AnyUrl validates that the value is a valid URL.
    linkedin_url: AnyUrl


    # --------------------------------------------------------
    # AGE
    # --------------------------------------------------------

    # age must be an integer
    #
    # gt=20 means:
    # age must be greater than 20
    age: Annotated[
        int,
        Field(gt=20)
    ]


    # --------------------------------------------------------
    # PRICE
    # --------------------------------------------------------

    # price must be an integer
    #
    # gt=15000 means:
    # price must be greater than 15000
    price: Annotated[
        int,
        Field(gt=15000)
    ]


    # --------------------------------------------------------
    # PRODUCTS
    # --------------------------------------------------------

    # products can be:
    #
    # List[str]
    # OR
    # None
    #
    # Example:
    # ["Laptop", "Mobile"]
    #
    # If products are not provided,
    # default value is None.
    products: Optional[List[str]] = None


    # --------------------------------------------------------
    # CONTACT DETAILS
    # --------------------------------------------------------

    # Dictionary where:
    #
    # Key   -> string
    # Value -> string
    #
    # Example:
    #
    # {
    #     "mob": "9390669636",
    #     "emergency": "3475757"
    # }
    contact_details: Dict[str, str]


    # --------------------------------------------------------
    # ADDRESS
    # --------------------------------------------------------

    # Address is another Pydantic model.
    #
    # This means Customer contains an Address object.
    #
    # Address:
    # {
    #     "city": "gnt",
    #     "state": "AP"
    # }
    address: Address


    # ========================================================
    # FIELD VALIDATOR - EMAIL
    # ========================================================

    # This validator runs only for the email field.
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):

        # Only these email domains are allowed.
        valid_domains = [
            "hdfc.com",
            "icici.com"
        ]

        # Get the domain after @
        #
        # abc@hdfc.com
        #       ↓
        # hdfc.com
        domain = value.split("@")[-1]


        # Check whether the domain is allowed.
        if domain not in valid_domains:

            raise ValueError(
                "no domain is matching"
            )


        # Return the original email
        return value


    # ========================================================
    # FIELD VALIDATOR - NAME
    # ========================================================

    # This validator runs only for name.
    @field_validator("name")
    @classmethod
    def name_validator(cls, value):

        # Convert name to uppercase.
        #
        # anwar
        #   ↓
        # ANWAR
        return value.upper()


    # ========================================================
    # FIELD VALIDATOR - AGE
    # ========================================================

    @field_validator("age", mode="after")
    @classmethod
    def age_valid(cls, value):

        # Add 10 to the age AFTER normal validation.
        #
        # Input:
        # age = 70
        #
        # After validator:
        # age = 80
        return value + 10


    # ========================================================
    # MODEL VALIDATOR
    # ========================================================

    # model_validator works with the COMPLETE model.
    #
    # Unlike field_validator(), which works with
    # one field, model_validator() can look at
    # multiple fields together.
    @model_validator(mode="after")
    def emergency_validate(self):

        # After age validator:
        #
        # Input age = 70
        #       ↓
        # age validator adds 10
        #       ↓
        # age = 80
        #
        # Now model_validator checks:
        # Is age > 60?
        #
        # If yes, emergency contact must exist.

        if (
            self.age > 60
            and "emergency" not in self.contact_details
        ):

            raise ValueError(
                "emergency contact is mandatory"
            )


        # Return the validated model.
        return self


    # ========================================================
    # COMPUTED FIELD
    # ========================================================

    # computed_field creates a calculated field.
    @computed_field
    @property
    def calc_values(self) -> int:

        # Calculate:
        #
        # age × price
        #
        # Example:
        #
        # age = 80
        # price = 20000000
        #
        # result = 1600000000

        new_value = self.age * self.price

        return new_value


# ============================================================
# INSERT DATA FUNCTION
# ============================================================

# This function receives a Customer object.
def insert_data(cust: Customer):

    # Print customer name
    print(cust.name)

    # Print age and calculated value
    print(
        cust.age,
        cust.calc_values
    )

    # Print contact, email, LinkedIn URL and address
    print(
        cust.contact_details,
        cust.email,
        cust.linkedin_url,
        cust.address
    )

    # Print products
    print(
        "inserted successfully",
        cust.products
    )


# ============================================================
# CREATE ADDRESS OBJECT
# ============================================================

# Create a normal Python dictionary.
address_dict = {
    "city": "gnt",
    "state": "AP"
}


# Convert dictionary into Address Pydantic object.
address1 = Address(**address_dict)


# ============================================================
# CREATE CUSTOMER DATA
# ============================================================

info = {
    "name": "anwar",

    "email": "abc@hdfc.com",

    "linkedin_url": "http://linkedin.com/annu",

    "age": 70,

    "price": 20000000,

    "contact_details": {
        "mob": "9390669636",
        "emergency": "3475757"
    },

    # Pass Address object here
    "address": address1
}


# ============================================================
# CREATE CUSTOMER OBJECT
# ============================================================

# **info means dictionary unpacking.
#
# The dictionary is passed into Customer.
#
# Pydantic then performs all validation.
cust1 = Customer(**info)


# ============================================================
# INSERT CUSTOMER
# ============================================================

# Pass the Customer object to insert_data().
insert_data(cust1)