# ==========================================================
# PICKLING 10 OBJECTS USING FOR LOOP Using Pickle (Stores Actual Objects)
# ==========================================================

import pickle


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name}, {self.age}, {self.balance}"


customers = []

# Create 10 Objects
for i in range(10):

    print(f"\nEnter Customer {i+1} Details")

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    balance = float(input("Enter Balance : "))

    customers.append(Bank(name, age, balance))


# Serialize Objects
with open("customers.pkl", "wb") as f:
    pickle.dump(customers, f)

print("\n10 Objects Stored Successfully.")

# ==========================================================
# PICKLING 10 OBJECTS USING FOR LOOP Using Pickle (Read the Objects Back)
# ==========================================================

import pickle


class Bank:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_info(self):
        return f"{self.name}, {self.age}, {self.balance}"


with open("customers.pkl", "rb") as f:
    data = pickle.load(f)

print("\nCustomer Details\n")

for customer in data:
    print(customer.get_info())