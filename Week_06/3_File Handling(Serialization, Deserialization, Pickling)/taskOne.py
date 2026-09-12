# ==========================================================
# SERIALIZATION OF 10 OBJECTS USING FOR LOOP
# ==========================================================

import json


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name}, {self.age}, {self.balance}"


# Empty List
customers = []

# Take 10 Objects Data
for i in range(10):

    print(f"\nEnter Customer {i+1} Details")

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    balance = float(input("Enter Balance : "))

    obj = Bank(name, age, balance)

    # Convert object into dictionary
    customers.append(obj.__dict__)


# Write into JSON File
with open("customers.json", "w") as f:
    json.dump(customers, f, indent=4)

print("\n10 Customer Records Stored Successfully.")