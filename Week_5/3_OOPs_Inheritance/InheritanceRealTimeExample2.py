# ==========================================================
# INHERITING PARENT METHOD
# ==========================================================
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        print("Brand : ", self.brand)
        print("Price : ", self.price)

class NewCar(Car):
    def __init__(self, brand, price, color, model):
        super().__init__(brand, price)
        self.color = color
        self.model = model

n = NewCar("BMW", 450000, "Red", "Basic Model")

# Calling Parent Method
n.get_info()

# ==========================================================
# OUTPUT
# ==========================================================
# Brand : BMW
# Price : 450000