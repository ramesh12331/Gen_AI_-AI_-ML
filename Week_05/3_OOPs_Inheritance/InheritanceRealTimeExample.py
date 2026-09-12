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
        if amount>0:
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
        print("Animal Makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog make sound bow")

d = Dog()
d.sound()

# ==========================================================
# CALLING PARENT METHOD USING super()
# ==========================================================

class Animal:
    def sound(self):
        print("Animals makes sound different")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog make differnt sound bow")

d = Dog()
d.sound()

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
        print("Name : ", self.name)
        print("Course : ", self.course)

s = Student("Ramesh", "Python")
s.display()

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
cat.eat()

dog.bark()
cat.meow()

# ==========================================================
# POLYMORPHISM (Introduction)
# ==========================================================
print("POLYMORPHISM")
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
        print("meow meow")

animals = [Dog(), Cat()]

for obj in animals:
    obj.sound()