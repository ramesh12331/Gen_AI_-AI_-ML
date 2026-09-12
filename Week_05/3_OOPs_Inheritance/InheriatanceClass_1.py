# ==========================================================
# PYTHON OOPS - INHERITANCE (PART - 1)
# Author : Beginner Friendly
# ==========================================================

# ==========================================================
# WHAT IS INHERITANCE?
# ==========================================================

# Inheritance means acquiring the properties (variables)
# and behaviors (methods) of one class into another class.

# Parent Class
#      ↓
# Child Class

# Parent Class is also called:
# 1. Base Class
# 2. Super Class

# Child Class is also called:
# 1. Derived Class
# 2. Sub Class


# Real-Time Examples

# Animal
#   ├── Dog
#   ├── Cat
#   └── Cow

# Vehicle
#   ├── Car
#   ├── Bike
#   └── Bus

# Person
#   ├── Student
#   └── Employee


# ==========================================================
# WHY DO WE USE INHERITANCE?
# ==========================================================

# Without inheritance, we write the same code again and again.

# With inheritance,
# we can reuse the existing code.

# Advantages
# ----------
# ✔ Code Reusability
# ✔ Less Code
# ✔ Easy Maintenance
# ✔ Better Organization


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

# Output
# Meow Meow


# ==========================================================
# PROBLEM
# ==========================================================

# Cat cannot use Animal methods.

# Example

# c.sound()

# Output

# AttributeError:
# 'Cat' object has no attribute 'sound'

# Because Cat is NOT inherited from Animal.


# ==========================================================
# SIMPLE INHERITANCE
# ==========================================================

# Syntax

# class Child(Parent):
#     pass


class Animal:

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Bow Bow")


d = Dog()

d.sound()

# Output
# Some Animal Sound

# Dog inherited Animal class.


# ==========================================================
# ACCESSING BOTH METHODS
# ==========================================================

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Bow Bow")


d = Dog()

d.sound()
d.bark()

# Output
# Animal Sound
# Bow Bow


# ==========================================================
# ANOTHER EXAMPLE
# ==========================================================

class Animal:

    def eat(self):
        print("Animal Eats Food")


class Cat(Animal):

    def meow(self):
        print("Meow Meow")


c = Cat()

c.eat()
c.meow()

# Output
# Animal Eats Food
# Meow Meow


# ==========================================================
# WHY ATTRIBUTE ERROR OCCURS?
# ==========================================================

# Wrong Example

class Animal:

    def sound(self):
        print("Sound")


class Dog:

    def bark(self):
        print("Bow")


d = Dog()

# d.sound()

# Output

# AttributeError:
# 'Dog' object has no attribute 'sound'

# Reason:
# Dog does not inherit Animal.


# ==========================================================
# CORRECT EXAMPLE
# ==========================================================

class Animal:

    def sound(self):
        print("Sound")


class Dog(Animal):

    def bark(self):
        print("Bow")


d = Dog()

d.sound()

# Output
# Sound


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
        print("Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Bow Bow")


dog = Dog()

dog.sound()
dog.bark()

# Output
# Animal Sound
# Bow Bow


# ==========================================================
# DRY RUN
# ==========================================================

# Step 1
# Python creates Animal class.

# Step 2
# Python creates Dog class.

# Step 3
# Dog inherits Animal.

# Step 4
# dog = Dog()

# Object created.

# Step 5

# dog.sound()

# Python checks

# Is sound() inside Dog?

# No

# Then it checks Animal.

# Found.

# Executes sound().

# Output

# Animal Sound

# Step 6

# dog.bark()

# bark() found inside Dog.

# Executes bark().

# Output

# Bow Bow


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

# Q1. What is Inheritance?

# Inheritance is a mechanism where one class acquires
# the properties and methods of another class.


# Q2. What is Parent Class?

# A class whose properties are inherited.


# Q3. What is Child Class?

# A class that inherits another class.


# Q4. Syntax of Inheritance?

# class Child(Parent):
#     pass


# Q5. What are the advantages of Inheritance?

# ✔ Code Reusability
# ✔ Less Code
# ✔ Easy Maintenance
# ✔ Faster Development