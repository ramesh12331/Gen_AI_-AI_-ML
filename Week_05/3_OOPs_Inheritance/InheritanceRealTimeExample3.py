# ==========================================================
# METHOD OVERRIDING
# ==========================================================

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        print(self.brand, self.price)

# d = Car("BMW", 100000)
# d.get_info()

class NewCar(Car):
    def __init__(self, brand, price, color, model):
        super().__init__(brand, price)
        self.color = color
        self.model = model
    # Overriding Parent Method
    def get_info(self):
        print("Brand : ", self.brand)
        print("Price : ", self.price)
        print("Color : ", self.color)
        print("Model : ", self.model)

n = NewCar("BMW", 450000, "Red", "Basic Model")
n.get_info()

# ==========================================================
# CLASS VARIABLE
# ==========================================================
class Car:
    wheels = 4      # Class Variable

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_info(self):
        print(self.brand, self.price)

# d = Car("BMW", 100000)
# d.get_info()

class NewCar(Car):
    def __init__(self, brand, price, color, model):
        super().__init__(brand, price)
        self.color = color
        self.model = model
    # Overriding Parent Method
    def get_info(self):
        print("Brand : ", self.brand)
        print("Price : ", self.price)
        print("Color : ", self.color)
        print("Model : ", self.model)

n = NewCar("BMW", 450000, "Red", "Basic Model")
# n.get_info()
print("Wheels", n.wheels)

# ==========================================================
# CHILD METHOD
# ==========================================================
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class NewCar(Car):
    def __init__(self, brand, price, color, model):
        super().__init__(brand, price)
        self.color = color
        self.model = model

    def set_price(self, amount):
        self.price += amount
        print("Updated Price :", self.price)

n = NewCar("BMW", 4500000, "Green", "Basic Model")
n.set_price(5000)
