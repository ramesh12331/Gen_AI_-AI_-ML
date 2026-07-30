# ==========================================================
# SIMPLE CLASS EXAMPLE (WITHOUT INHERITANCE)
# ==========================================================
class Animal:
    def sound(self):
        print("Some Animal Sound")

class Dog:
    def bark(self):
        print("Bow Bow")

class Cat:
    def meow(self):
        print("Meow Meow")

c = Cat()
c.meow()

# c.sound() #AttributeError: 'Cat' object has no attribute 'sound'

# ==========================================================
# SIMPLE INHERITANCE
# ==========================================================

# Syntax

# class Child(Parent):
#     pass

class Animal:
    def sound(self):
        print("animal")

class Dog(Animal):
    def bark(self):
        print("bow")

class Cat(Dog):
    def meow(self):
        print("meow")

c = Cat()
c.meow()
c.sound()
c.bark()

# ==========================================================
# ACCESSING BOTH METHODS
# ==========================================================

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def bark(self):
        print("Dog Sound")

class Cat(Dog):
    def meow(self):
        print("Cat Sound")

d = Dog()
d.bark()
d.sound()

# ==========================================================
# WHY ATTRIBUTE ERROR OCCURS?
# ==========================================================

# Wrong Example
class Animal:
    def sound(self):
        print("sound of animals")

class Dog:
    def bark(self):
        print("Dog sound")

d = Dog()

# d.sound() # AttributeError: 'Dog' object has no attribute 'sound'
# Reason:
# Dog does not inherit Animal.

# ==========================================================
# CORRECT EXAMPLE
# ==========================================================
class Animal:
    def sound(self):
        print("parent Animal sound")

class Dog(Animal):
    def bow(self):
        print("child dog sound")

d = Dog()
d.sound()

# ==========================================================
# SINGLE INHERITANCE
# ==========================================================

# One Parent
# One Child

#
# Animal
#    |
#   Dog
#

class Animal:
    def sound(self):
        print("parent animal animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog Dog")

dog = Dog()
dog.sound()
dog.bark()

# ==========================================================
# PYTHON OOPS - INHERITANCE (PART - 2)
# Multiple Inheritance | Multilevel Inheritance | super()
# ==========================================================


# ==========================================================
# MULTILEVEL INHERITANCE
# ==========================================================

class Animal:
    def sound(self):
        print("Animal Parent class")

class Dog(Animal):
    def bark(self):
        print("Dog first child")


class Cat(Dog):
    def meow(self):
        print("Cat is second child")

c = Cat()
c.sound()
c.bark()
c.meow()

# ==========================================================
# ANOTHER MULTILEVEL EXAMPLE
# ==========================================================
class Grandfather:
    def land(self):
        print("100 Acres Land")

class Father(Grandfather):
    def house(self):
        print("Luxury House")

class Son(Father):
    def bike(self):
        print("Sports Bike")

s = Son()

s.land()
s.house()
s.bike()

# ==========================================================
# MULTIPLE INHERITANCE
# ==========================================================

# Definition:
# One child inherits from more than one parent.

class Animal:
    def sound(self):
        print("Animal sound")

class Dog:
    def bark(self):
        print("Bow bow")

class Cat(Animal,Dog):
    def meow(self):
        print("meow meow")

c = Cat()

c.meow()
c.sound()
c.bark()

print("Dog Object")
d = Dog()

d.bark()
# d.meow()
# d.sound()

# ==========================================================
# METHOD RESOLUTION ORDER (MRO)
# ==========================================================

# Python searches classes
# from Left to Right.

class A:
    def display(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A,B):
    pass

obj = C()

obj.display()

print(C.mro())

# ==========================================================
# super() FUNCTION
# ==========================================================

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def get_inf(self):
        print(self.brand)
        print(self.price)

c = Car("BMW", 4500000)
c.get_inf()

# ==========================================================
# CHILD CLASS USING super()
# ==========================================================

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class NewCar(Car):
    def __init__(self, brand, price, color, model):
        super().__init__(brand,price)

        self.color = color
        self.model = model

    def get_info(self):

        print("Brand :", self.brand)
        print("Price :", self.color)
        print("Model :", self.model)

n = NewCar("BMW", 4500000, "Black", "X5")
n.get_info()

# ==========================================================
# WITHOUT super()
# ==========================================================

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class NewCar:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def get_info(self):
        print("Brand :", self.brand)

n = NewCar("Ferrari", 6000000, "Green")
n.get_info()

# super() avoids duplication.