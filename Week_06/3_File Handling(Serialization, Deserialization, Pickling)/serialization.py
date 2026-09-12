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
    return{
        "name" : obj.name,
        "age" : obj.age,
        "balance" : obj.balance
    }
# ----------------------------------------------------------
# Create Object
# ----------------------------------------------------------
a = Bank("Ramesh", 30, 60000000)

# ----------------------------------------------------------
# Method 1
# This will give TypeError
# ----------------------------------------------------------


# with open("new.json", "w") as f:
#     json.dump(a, f)

# TypeError:
# Object of type Bank is not JSON serializable

# ==========================================================
# Method 2
# Using default function (Recommended)
# ==========================================================
# with open("new.json", "w") as f:
#     json.dump(a, f, default=get_info, indent=4)

# ==========================================================
# Method 3
# Shortcut using __dict__
# ==========================================================
with open("new.json" ,"w") as f:
    json.dump(a.__dict__, f, indent = 4)

# ==========================================================
# Deserialize
# ==========================================================
with open("new.json", "r") as f:
    data = json.load(f)
print(data)