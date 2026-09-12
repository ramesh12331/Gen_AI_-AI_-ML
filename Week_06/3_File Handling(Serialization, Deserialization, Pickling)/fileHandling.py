# ==========================================================
# FILE HANDLING
# SERIALIZATION & DESERIALIZATION
# ==========================================================

# ==========================================================
# Example to work with other data types
# ==========================================================
# d = {
#     "name": "abc",
#     "age": 40
# }

# with open("new.txt", "w") as f:
#     f.write(d)
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

with open("new.txt", "w") as f:
    json.dump(l,f)

# ==========================================================
# Deserialize List
# ==========================================================
with open("new.txt", "r") as f:
    d = json.load(f)
print(d)
print(type(d))

# ==========================================================
# Serialize & Deserialize Dictionary
# ==========================================================
d = {
    "name": "abc",
    "age": 40
}

with open("new.json", "w") as f:
    json.dump(d,f)

# ==========================================================
# Writing JSON into TXT file
# (Same JSON format but file extension is .txt)
# ==========================================================

with open("new.txt", "w") as f:
    json.dump(d,f)

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
    json.dump(d,f,indent = 4)


# ==========================================================
# Serialize & Deserialize Custom Objects
# ==========================================================
class Bank:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
a = Bank("Ramesh", 30, 4000000)

# with open("new.json", "w") as f:
#     json.dump(a,f)

# Output
# TypeError: Object of type Bank is not JSON serializable

# ==========================================================
# Note
# ==========================================================

# JSON cannot directly serialize custom Python objects.
# We must first convert the object into a dictionary
# before using json.dump().

