# ==========================================================
# FILE HANDLING
# SERIALIZATION & DESERIALIZATION
# ==========================================================


# ==========================================================
# Example to work with other data types
# ==========================================================

d = {
    "name": "abc",
    "age": 40
}

with open("new.txt", "w") as f:
    f.write(d)

# Output
# TypeError: write() argument must be str, not dict


# ==========================================================
# Working with Dictionaries
# ==========================================================

# Serialization  -> Process of converting Python data types
#                   into JSON format.

# Deserialization -> Process of converting JSON format
#                    back into Python data types.


# ==========================================================
# Example of Serialization using JSON Module
# Starting with List
# ==========================================================

import json

l = [1, 2, 3, 4, 5, "Anwar"]

with open("new.json", "w") as f:
    json.dump(l, f)


# ==========================================================
# Deserialize List
# ==========================================================

with open("new.json") as f:
    d = json.load(f)

print(d)
print(type(d))

# Output
# [1, 2, 3, 4, 5, 'Anwar']
# <class 'list'>


# ==========================================================
# Serialize & Deserialize Dictionary
# ==========================================================

d = {
    "name": "abc",
    "age": 40
}

with open("new.json", "w") as f:
    json.dump(d, f)


# ==========================================================
# Writing JSON into TXT file
# (Same JSON format but file extension is .txt)
# ==========================================================

with open("new.txt", "w") as f:
    json.dump(d, f)


# ==========================================================
# Dictionary with Indent
# ==========================================================

d = {
    101: {
        "name": "abc",
        "age": 40
    },

    102: {
        "name": "rahul",
        "age": 50
    }
}

with open("new.json", "w") as f:
    json.dump(d, f, indent=4)


# ==========================================================
# Serialize & Deserialize Tuple
# ==========================================================

# (Next topic in class)


# ==========================================================
# Serialize & Deserialize Custom Objects
# ==========================================================

class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


a = Bank("annu", 25, 900000)

with open("new.json", "w") as f:
    json.dump(a, f)

# Output
# TypeError:
# Object of type Bank is not JSON serializable


# ==========================================================
# Note
# ==========================================================

# JSON cannot directly serialize custom Python objects.
# We must first convert the object into a dictionary
# before using json.dump().

# (Your trainer explains this in the next screenshots.)

# ==========================================================
# JSON SERIALIZATION OF CLASS OBJECT
# ==========================================================

import json


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance


# ----------------------------------------------------------
# Function used by json.dump() when it encounters
# a custom class object.
# ----------------------------------------------------------

def get_info(obj):
    return {
        "name": obj.name,
        "age": obj.age,
        "balance": obj.balance
    }


# ==========================================================
# Create Object
# ==========================================================

a = Bank("annu", 25, 900000)


# ==========================================================
# Method 1
# This will give TypeError
# ==========================================================

"""
with open("new.json", "w") as f:
    json.dump(a, f)

TypeError:
Object of type Bank is not JSON serializable
"""


# ==========================================================
# Method 2
# Using default function (Recommended)
# ==========================================================

with open("new.json", "w") as f:
    json.dump(a, f, default=get_info, indent=4)


# ==========================================================
# Method 3
# Shortcut using __dict__
# ==========================================================

"""
with open("new.json", "w") as f:
    json.dump(a.__dict__, f, indent=4)
"""


# ==========================================================
# Wrong Examples
# ==========================================================

"""
a.__list__

AttributeError:
'Bank' object has no attribute '__list__'
"""

"""
a.__str__

This returns the method object.
It is not JSON serializable unless called.
"""


# ==========================================================
# Deserialize
# ==========================================================

with open("new.json", "r") as f:
    data = json.load(f)

print(data)