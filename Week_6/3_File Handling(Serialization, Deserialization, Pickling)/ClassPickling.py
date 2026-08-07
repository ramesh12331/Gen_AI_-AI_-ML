# ==========================================================
# PICKLING (SERIALIZATION)
# ==========================================================

import pickle


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name},{self.age},{self.balance}"


# Create Object
a = Bank("anwar", 25, 900000)

# Serialize Object
with open("new.pkl", "wb") as f:
    pickle.dump(a, f)

print("Object Stored Successfully")
# ==========================================================
# UNPICKLING (DESERIALIZATION)
# ==========================================================

import pickle


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name},{self.age},{self.balance}"


# Read Object
with open("new.pkl", "rb") as f:
    d = pickle.load(f)

print(d.name)
print(d.age)
print(d.balance)
print(d.get_info())