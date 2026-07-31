# ==========================================================
# POLYMORPHISM & ABSTRACTION
# Author : Beginner Friendly
# ==========================================================

# ==========================================================
# 1. MAGIC METHOD (__str__)
# ==========================================================

class A:
    def __init__(self):
        pass
    def __str__(self):
        return "Heyy"
a = A()
print(a)

# ==========================================================
# 2. METHOD OVERRIDING
# ==========================================================
class Animal:
    def sound(self):
        print("Sound")
class Dog(Animal):
    def sound(self):
        print("Bow")

d = Dog()
d.sound()

# Output
# Bhoww
# ==========================================================
# Parent Object
# ==========================================================

a = Animal()
a.sound()

# Output
# Sound

# ==========================================================
# 3. METHOD OVERLOADING
# ==========================================================

# Python DOES NOT support method overloading directly.

class A:
    def add(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)

    def add(self, a, b, c, d):
        print(a+b+c+d)

obj = A()
# obj.add(10)

# TypeError: A.add() missing 3 required positional arguments: 'b', 'c', and 'd'

obj.add(10, 20, 30, 40)

# ==========================================================
# 4. USING DEFAULT ARGUMENTS
# ==========================================================

class A:
    def add(self, a, b=0, c=0):
        print(a+b+c)
obj = A()
obj.add(10)

# Output
# 10

obj.add(10, 20)

# Output
# 30

obj.add(10, 20, 30)

# ==========================================================
# 5. USING None
# ==========================================================
class A:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            print(a+b+c)
        elif b is not None:
            print(a+b)
        else:
            print(a)

obj = A()
obj.add(90)
obj.add(90,80)
obj.add(90,80,70)

# ==========================================================
# 6. USING *args
# ==========================================================
class A:
    def add(self,*value):
        print(sum(value))

obj = A()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)

# ==========================================================
# 7. USING **kwargs
# ==========================================================
class A:
    def details(self, **value):
        print(value)

obj = A()
obj.details(name = "Ajay")
obj.details(name = "Ajay", age = 50)
obj.details(name = "Ajay", age = 50, gender = "Male")

# ==========================================================
# 8. ABSTRACTION
# ==========================================================

from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def security(self):
        pass

class Mobile(Bank):
    def mobile(self):
        print("Mobile Application")

    def security(self):
        print("Mobile Security")

m = Mobile()
m.mobile()
m.security()