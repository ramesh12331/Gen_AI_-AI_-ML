# ==========================================================
# PYTHON INHERITANCE
# Parent Constructor + Child Constructor
# ==========================================================
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def get_info(self):
        print("Brand", self.brand)
        print("Price", self.price)
# ----------------------------------------------------------
# Parent Object
# ----------------------------------------------------------

c = Car("BMW", 450000)
c.get_info()

# ==========================================================
# Child Class
# ==========================================================

class NewCar(Car):
    def __init__(self, brand, price, color, model):

        # Call Parent Constructor
        super().__init__(brand, price)

        # Child Variables
        self.color = color
        self.model = model

# ----------------------------------------------------------
# Child Object
# ----------------------------------------------------------

n = NewCar("BMW", 450000, "Red", "Basic Model")

print("\nBrand :", n.brand)
print("Price :", n.price)
print("Color :", n.color)
print("Model :", n.model)

# ==========================================================
# OUTPUT
# ==========================================================
# Brand : BMW
# Price : 450000
# Color : Red
# Model : Basic Model