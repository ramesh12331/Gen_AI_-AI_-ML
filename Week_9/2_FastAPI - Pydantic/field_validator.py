from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional,Annotated

class Customer(BaseModel):
    name : Annotated[str, Field(max_length=10)]
    email : EmailStr
    age : Annotated[int, Field(gt=20, lt=60)]

    @field_validator("email")
    @classmethod
    def email_valid(cls, value):
        valid_domains = [
            "hdfc.com",
            "icici.com"
        ]

        domain = value.split("@")[-1]

        if domain not in valid_domains:
            raise ValueError(
                "Email must belong to HDFC or ICICI domain"
            )

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator("age")
    @classmethod
    def transform_age(cls, value):
        return value+10

data = {
    "name": "anwar",
    "email": "anwar@hdfc.com",
    "age": 35
}

customer = Customer(**data)
print(customer)


# #####################COMMENTED CODE EXPLANATION#################################
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Annotated


# ============================================================
# CUSTOMER MODEL
# ============================================================

class Customer(BaseModel):

    # name must be a string
    # Maximum 10 characters allowed
    name: Annotated[
        str,
        Field(max_length=10)
    ]


    # EmailStr checks whether the email
    # has a valid email format
    email: EmailStr


    # age must be:
    # greater than 20
    # less than 60
    age: Annotated[
        int,
        Field(gt=20, lt=60)
    ]


    # ========================================================
    # EMAIL VALIDATOR
    # ========================================================

    @field_validator("email")
    @classmethod
    def email_valid(cls, value):

        # Only these domains are allowed
        valid_domains = [
            "hdfc.com",
            "icici.com"
        ]

        # Get the domain part from the email
        #
        # "anwar@hdfc.com"
        #          ↓
        #       hdfc.com
        domain = value.split("@")[-1]


        # Check whether the domain is allowed
        if domain not in valid_domains:

            raise ValueError(
                "Email must belong to HDFC or ICICI domain"
            )


        # IMPORTANT:
        # Return the value after validation
        return value


    # ========================================================
    # NAME VALIDATOR
    # ========================================================

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):

        # Convert the name to uppercase
        #
        # "anwar"
        #    ↓
        # "ANWAR"
        return value.upper()


    # ========================================================
    # AGE VALIDATOR
    # ========================================================

    @field_validator("age")
    @classmethod
    def transform_age(cls, value):

        # Add 10 years to the given age
        #
        # 35 + 10
        #    ↓
        # 45
        return value + 10


# ============================================================
# INPUT DATA
# ============================================================

data = {
    "name": "anwar",
    "email": "anwar@hdfc.com",
    "age": 35
}


# ============================================================
# CREATE CUSTOMER OBJECT
# ============================================================

customer = Customer(**data)


# Print the final customer object
print(customer)


# ============================================================
# FINAL SUMMARY
# ============================================================

# @field_validator("email")
#     ↓
# Used to create a custom validator for the email field.
#
#
# @field_validator("name")
#     ↓
# Used to create a custom validator for the name field.
#
#
# @field_validator("age")
#     ↓
# Used to create a custom validator for the age field.
#
#
# @classmethod
#     ↓
# Allows the validator method to receive the class (cls).
#
#
# email_valid()
#     ↓
# Checks whether the email domain is:
#     hdfc.com
#     OR
#     icici.com
#
#
# transform_name()
#     ↓
# Converts the name to uppercase.
#
# "anwar" → "ANWAR"
#
#
# transform_age()
#     ↓
# Adds 10 to the age.
#
# 35 → 45
#
#
# IMPORTANT:
# Every validator that keeps the value must return the value.
#
# return value
#
# Otherwise the field can become None.
#
#
# ALSO:
# Every validator method should have a unique name.
#
# ❌ Wrong:
# def transform_age(...)
# def transform_age(...)
#
# ✅ Correct:
# def transform_name(...)
# def transform_age(...)


# ============================================================
# VALIDATION FLOW
# ============================================================

# data
#   ↓
# Customer(**data)
#   ↓
# Pydantic built-in validation
#   ↓
# name → str + max_length=10
# email → EmailStr
# age → int + 20 < age < 60
#   ↓
# Custom field validators
#   ↓
# email → check HDFC / ICICI
# name  → convert to uppercase
# age   → add 10
#   ↓
# Final Customer object