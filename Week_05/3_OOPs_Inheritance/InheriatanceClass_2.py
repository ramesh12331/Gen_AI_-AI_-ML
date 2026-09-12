# ==========================================================
# PYTHON OOPS - INHERITANCE (PART - 2)
# Multiple Inheritance | Multilevel Inheritance | super()
# ==========================================================


# ==========================================================
# MULTILEVEL INHERITANCE
# ==========================================================

# Definition:
# One class inherits another class,
# and another class inherits that child class.

#
#        Animal
#           │
#         Dog
#           │
#         Cat
#

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Bow Bow")


class Cat(Dog):

    def meow(self):
        print("Meow Meow")


c = Cat()

c.sound()
c.bark()
c.meow()

# Output
# Animal Sound
# Bow Bow
# Meow Meow


# ==========================================================
# DRY RUN
# ==========================================================

# Step 1
# Animal class is created.

# Step 2
# Dog inherits Animal.

# Step 3
# Cat inherits Dog.

# Step 4
# c = Cat()

# Python creates Cat object.

# Step 5

# c.sound()

# Python searches

# Cat → Not Found

# Dog → Not Found

# Animal → Found

# Output
# Animal Sound


# Step 6

# c.bark()

# Cat → Not Found

# Dog → Found

# Output
# Bow Bow


# Step 7

# c.meow()

# Found in Cat

# Output
# Meow Meow


# ==========================================================
# ANOTHER MULTILEVEL EXAMPLE
# ==========================================================

class GrandFather:

    def land(self):
        print("100 Acres Land")


class Father(GrandFather):

    def house(self):
        print("Luxury House")


class Son(Father):

    def bike(self):
        print("Sports Bike")


s = Son()

s.land()
s.house()
s.bike()

# Output
# 100 Acres Land
# Luxury House
# Sports Bike


# ==========================================================
# MULTIPLE INHERITANCE
# ==========================================================

# Definition:
# One child inherits from more than one parent.

#
#     Animal      Dog
#         \        /
#          \      /
#             Cat
#

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog:

    def bark(self):
        print("Bow Bow")


class Cat(Dog, Animal):

    def meow(self):
        print("Meow Meow")


c = Cat()

c.sound()
c.bark()
c.meow()

# Output
# Animal Sound
# Bow Bow
# Meow Meow


# ==========================================================
# DRY RUN
# ==========================================================

# Python first checks Cat.

# If method not found,
# it checks Dog.

# If still not found,
# it checks Animal.


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


class C(A, B):
    pass


obj = C()

obj.display()

# Output
# Class A


# Because
# A is searched first.


print(C.mro())

# Output
# [C, A, B, object]


# ==========================================================
# super() FUNCTION
# ==========================================================

# super() calls the parent class constructor.

class Car:

    def __init__(self, brand, price):

        self.brand = brand
        self.price = price

    def get_info(self):

        print(self.brand)
        print(self.price)


c = Car("BMW", 4500000)

c.get_info()

# Output
# BMW
# 4500000


# ==========================================================
# CHILD CLASS USING super()
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

    def get_info(self):

        print("Brand :", self.brand)
        print("Price :", self.price)
        print("Color :", self.color)
        print("Model :", self.model)


n = NewCar("BMW", 4500000, "Black", "X5")

n.get_info()

# Output
# Brand : BMW
# Price : 4500000
# Color : Black
# Model : X5


# ==========================================================
# WITHOUT super()
# ==========================================================

class Car:

    def __init__(self, brand, price):

        self.brand = brand
        self.price = price


class NewCar(Car):

    def __init__(self, brand, price, color):

        self.brand = brand
        self.price = price
        self.color = color


# Here we repeat code.

# super() avoids duplication.


# ==========================================================
# ADVANTAGES OF super()
# ==========================================================

# ✔ Reuses parent constructor
# ✔ Reduces duplicate code
# ✔ Easy to maintain
# ✔ Cleaner code


# ==========================================================
# TYPES OF INHERITANCE
# ==========================================================

# 1. Single Inheritance

# Animal
#    │
#   Dog


# 2. Multilevel Inheritance

# Animal
#    │
#   Dog
#    │
#   Cat


# 3. Multiple Inheritance

# Animal      Bird
#      \      /
#        Duck


# 4. Hierarchical Inheritance

#      Animal
#      /   |   \
#    Dog  Cat  Cow


# 5. Hybrid Inheritance

# Combination of two or more
# inheritance types.


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

# Q1. What is Multilevel Inheritance?

# When one child class inherits another child class.


# Q2. What is Multiple Inheritance?

# One child inherits from
# multiple parent classes.


# Q3. What is super()?

# super() is used to call
# the parent class constructor or methods.


# Q4. Why do we use super()?

# To avoid duplicate code
# and reuse parent class initialization.


# Q5. What is MRO?

# Method Resolution Order.

# Python searches classes
# from left to right.