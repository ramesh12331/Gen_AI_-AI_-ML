# ==========================================================
# PYTHON ENCAPSULATION
# ==========================================================

# Access Modifiers in Python
#
# 1. Public
# 2. Protected
# 3. Private

# ==========================================================
# PUBLIC MEMBERS
# ==========================================================

class Shop:
    def __init__(self, product, price, pin):
        self.product = product
        self.price = price
        self.pin = pin

    def view(self):
        print("Product :", self.product)
        print("Price   :",self.price)
        print("PIN     :",self.pin)

s = Shop("Santoor", 5000, 1234)

print(s.product)
print(s.price)
print(s.pin)

# OR
s.view()

# ==========================================================
# PROTECTED MEMBERS
# Single Underscore (_)
# ==========================================================
class Shop:
    def __init__(self, product, price, pin):
        self.product = product
        self._price = price
        self._pin = pin

    def view(self):
        print(self.product)
        print(self._price)
        print(self._pin)

shop = Shop("rin", 2000, 1234)
shop.view()

print("Price : ",shop._price)
print("Pin : ",shop._pin)
# ==========================================================
# PROTECTED VARIABLE IN CHILD CLASS
# ==========================================================
class Shop:
    def __init__(self, product, price, pin):
        self.product = product
        self.price = price
        self.pin = pin

class Shop1(Shop):
    def info(self):
        print(self.product)
        print(self.price)
        print(self.pin)

shop = Shop1("Five Star", 50, 1234)
shop.info()
# ==========================================================
# PRIVATE MEMBERS
# Double Underscore (__)
# ==========================================================

class Shop:
    def __init__(self, product, price, pin):
        self.product = product
        self.__price = price
        self.__pin = pin

    def view(self):
        print("Product : ", self.product)
        print("Price : ", self.__price)
        print("Pin : ", self.__pin)

shop = Shop("NatrajPen", 5, 1234)
shop.view()

# print(shop.__price) #'Shop' object has no attribute '__price'
print(shop._Shop__price)