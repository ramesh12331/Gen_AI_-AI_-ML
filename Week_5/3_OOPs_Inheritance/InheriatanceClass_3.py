# ==========================================================
# PYTHON OOPS - INHERITANCE (PART - 3)
# Real Time Examples | Method Overriding | Bank Application
# ==========================================================


# ==========================================================
# REAL-TIME BANK EXAMPLE
# ==========================================================

# Parent Class

class Bank:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def view_balance(self):

        print("Current Balance :", self.balance)


# Child Class

class ATM(Bank):

    def deposit(self, amount):

        self.balance += amount

        print("Amount Deposited Successfully")

    def withdraw(self, amount):

        if amount > 0:

            if amount <= self.balance:

                self.balance -= amount

                print("Withdrawal Successful")

            else:

                print("Insufficient Balance")

        else:

            print("Enter Positive Amount")


# Object

user = ATM("Ramesh", 5000)

user.view_balance()

user.deposit(2000)

user.view_balance()

user.withdraw(3000)

user.view_balance()

# Output
# Current Balance : 5000
# Amount Deposited Successfully
# Current Balance : 7000
# Withdrawal Successful
# Current Balance : 4000


# ==========================================================
# METHOD OVERRIDING
# ==========================================================

# Definition:
# Child class provides its own implementation
# of the parent class method.

class Animal:

    def sound(self):

        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        print("Dog says Bow Bow")


d = Dog()

d.sound()

# Output
# Dog says Bow Bow


# ==========================================================
# CALLING PARENT METHOD USING super()
# ==========================================================

class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        super().sound()

        print("Dog Sound")


d = Dog()

d.sound()

# Output
# Animal Sound
# Dog Sound


# ==========================================================
# CONSTRUCTOR INHERITANCE
# ==========================================================

class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, course):

        super().__init__(name)

        self.course = course

    def display(self):

        print("Name   :", self.name)
        print("Course :", self.course)


s = Student("Ramesh", "Python")

s.display()

# Output
# Name   : Ramesh
# Course : Python


# ==========================================================
# HIERARCHICAL INHERITANCE
# ==========================================================

# One Parent
# Multiple Children

#
#          Animal
#         /   |   \
#      Dog   Cat  Cow
#

class Animal:

    def eat(self):

        print("Animal Eats")


class Dog(Animal):

    def bark(self):

        print("Bow Bow")


class Cat(Animal):

    def meow(self):

        print("Meow Meow")


dog = Dog()

cat = Cat()

dog.eat()

dog.bark()

cat.eat()

cat.meow()

# Output
# Animal Eats
# Bow Bow
# Animal Eats
# Meow Meow


# ==========================================================
# POLYMORPHISM (Introduction)
# ==========================================================

# Same method
# Different behavior

class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Bow Bow")


class Cat(Animal):

    def sound(self):

        print("Meow Meow")


animals = [Dog(), Cat()]

for obj in animals:

    obj.sound()

# Output
# Bow Bow
# Meow Meow


# ==========================================================
# COMPLETE INHERITANCE SUMMARY
# ==========================================================

# 1. Single Inheritance

# Parent
#    │
# Child


# 2. Multilevel Inheritance

# Parent
#    │
# Child
#    │
# Grand Child


# 3. Multiple Inheritance

# Parent1     Parent2
#      \      /
#        Child


# 4. Hierarchical Inheritance

#        Parent
#      /   |   \
#   Child Child Child


# 5. Hybrid Inheritance

# Combination of different
# inheritance types.


# ==========================================================
# ADVANTAGES OF INHERITANCE
# ==========================================================

# ✔ Code Reusability

# ✔ Less Code

# ✔ Easy Maintenance

# ✔ Better Organization

# ✔ Faster Development

# ✔ Supports Method Overriding

# ✔ Easy Extension


# ==========================================================
# DISADVANTAGES
# ==========================================================

# ✔ Wrong design creates tight coupling.

# ✔ Deep inheritance becomes difficult
#    to understand.

# ✔ Debugging becomes harder.


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

# Q1. What is Inheritance?

# Inheritance allows one class
# to acquire the properties and
# methods of another class.


# Q2. What is Parent Class?

# The class whose members
# are inherited.


# Q3. What is Child Class?

# The class that inherits
# another class.


# Q4. What is Method Overriding?

# Redefining the parent method
# inside the child class.


# Q5. What is super()?

# Used to access parent
# class methods and constructor.


# Q6. How many types of inheritance
# are available in Python?

# Five

# 1. Single
# 2. Multiple
# 3. Multilevel
# 4. Hierarchical
# 5. Hybrid


# Q7. Which function tells the
# inheritance order?

# mro()

# Example

# print(Dog.mro())


# ==========================================================
# END OF INHERITANCE
# ==========================================================