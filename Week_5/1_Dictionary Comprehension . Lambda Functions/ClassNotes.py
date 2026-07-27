# ==========================================================
# PYTHON DICTIONARY
# ==========================================================

# ----------------------------------------------------------
# What is Dictionary?
# ----------------------------------------------------------
# A Dictionary is a collection of key-value pairs.
#
# Real-Time Examples:
# -> Student Details
# -> Employee Details
# -> Product Information
# -> JSON Data from APIs
#
# Syntax:
# {
#     key : value
# }

# ==========================================================
# Creating Dictionary
# ==========================================================

d = {
    "name": "Rahul",
    "age": 40,
    "salary": 600000
}

print(d)

# Output:
# {'name': 'Rahul', 'age': 40, 'salary': 600000}


# ==========================================================
# Characteristics of Dictionary
# ==========================================================

# ✔ Stores data in Key-Value pairs
# ✔ Mutable (Can be modified)
# ✔ Ordered (Python 3.7+)
# ✔ Keys are unique
# ✔ Values can be duplicated
# ✔ Does not support indexing


# ==========================================================
# Accessing Dictionary Values
# ==========================================================

print(d["name"])
print(d["salary"])

# Output:
# Rahul
# 600000


# ----------------------------------------------------------
# Drawback of Direct Access
# ----------------------------------------------------------
# If the key does not exist,
# it raises KeyError.

# print(d["gender"])
# KeyError


# ==========================================================
# get() Method
# ==========================================================
# Returns None if key is not found.
# No error is generated.

print(d.get("gender"))

# Output:
# None


# ==========================================================
# Adding New Items
# ==========================================================

d["city"] = "Hyderabad"

print(d)

# Output:
# {'name':'Rahul','age':40,'salary':600000,'city':'Hyderabad'}


# ==========================================================
# Updating Existing Values
# ==========================================================

d["name"] = "Ajay"

print(d)

# Output:
# {'name':'Ajay','age':40,'salary':600000,'city':'Hyderabad'}


# ==========================================================
# Removing Item using pop()
# ==========================================================

d.pop("salary")

print(d)

# Output:
# {'name':'Ajay','age':40,'city':'Hyderabad'}


# ==========================================================
# popitem()
# ==========================================================
# Removes the last inserted key-value pair.

d.popitem()

print(d)


# ==========================================================
# Delete using del
# ==========================================================

d = {
    "name": "Rahul",
    "age": 40,
    "salary": 600000
}

del d["age"]

print(d)

# Output:
# {'name':'Rahul','salary':600000}


# Delete entire dictionary

# del d


# ==========================================================
# clear()
# ==========================================================

d.clear()

print(d)

# Output:
# {}


# ==========================================================
# keys()
# ==========================================================

d = {
    "name": "Rahul",
    "age": 40,
    "salary": 600000
}

print(d.keys())

# Output:
# dict_keys(['name','age','salary'])


# ==========================================================
# values()
# ==========================================================

print(d.values())

# Output:
# dict_values(['Rahul',40,600000])


# ==========================================================
# items()
# ==========================================================

for key, value in d.items():
    print(key, ":", value)

# Output:
# name : Rahul
# age : 40
# salary : 600000


# ==========================================================
# Dictionary with List
# ==========================================================

students = {
    "names": ["Annu", "Rahul", "Venky", "Ajay"],
    "ages": [25, 30, 40, 50]
}

print(students["names"])
print(students["ages"])


# ==========================================================
# Dictionary with if Condition
# ==========================================================

student = {
    "name": "A",
    "marks": 90
}

for key, value in student.items():
    print(key, ":", value)

if student["marks"] == 90:
    print("Excellent")


# ==========================================================
# Check if Key Exists
# ==========================================================

if "name" in student:
    print("Key Found")
else:
    print("Key Not Found")


# ==========================================================
# setdefault()
# ==========================================================
# Adds key only if it doesn't already exist.

student.setdefault("grade", "A")

print(student)

# Existing value will not be overwritten.


# ==========================================================
# Nested Dictionary
# ==========================================================

products = {

    101: {
        "name": "Rahul",
        "product": "ABC",
        "price": 900
    },

    102: {
        "name": "Ajay",
        "product": "XYZ",
        "price": 6000
    }

}

print(products[102]["price"])

# Output:
# 6000


# ==========================================================
# Dictionary of Lists
# ==========================================================

employee = {
    "names": ["A", "B", "C"],
    "salary": [1000, 2000, 3000]
}

print(employee)


# ==========================================================
# List of Dictionaries
# ==========================================================

employees = [
    {"id": 101, "name": "Rahul"},
    {"id": 102, "name": "Ajay"},
    {"id": 103, "name": "Annu"}
]

print(employees[1]["name"])

# Output:
# Ajay


# ==========================================================
# Dictionary Comprehension
# ==========================================================

result = {
    ch: ch.upper()
    for ch in "apple"
}

print(result)

# Output:
# {'a':'A','p':'P','l':'L','e':'E'}


# ==========================================================
# Dictionary Comprehension with if
# ==========================================================

result = {
    ch: ch.upper()
    for ch in "apple"
    if ch.upper() == "P"
}

print(result)

# Output:
# {'p':'P'}


# ==========================================================
# Dictionary Comprehension with if-else
# ==========================================================

numbers = {
    i: "Even" if i % 2 == 0 else "Odd"
    for i in range(1, 6)
}

print(numbers)

# Output:
# {1:'Odd',2:'Even',3:'Odd',4:'Even',5:'Odd'}


# ==========================================================
# LAMBDA FUNCTIONS
# ==========================================================

# ----------------------------------------------------------
# What is Lambda Function?
# ----------------------------------------------------------
# Lambda is an anonymous (nameless) function.
#
# Why do we use Lambda?
# -> Short programs
# -> One-line functions
# -> Used with map(), filter(), sorted()
#
# Syntax:
# lambda arguments : expression
#
# A lambda function automatically returns the result.


# ==========================================================
# Lambda Example - Square
# ==========================================================

square = lambda x: x * x

print(square(3))

# Output:
# 9


# ==========================================================
# Lambda Example - Length
# ==========================================================

length = lambda text: len(text)

print(length("Apple"))

# Output:
# 5


# ==========================================================
# Lambda with Two Arguments
# ==========================================================

add = lambda a, b: a + b

print(add(10, 20))

# Output:
# 30


# ==========================================================
# Lambda with Three Arguments
# ==========================================================

total = lambda a, b, c: a + b + c

print(total(12, 13, 2))

# Output:
# 27


# ==========================================================
# Lambda with No Arguments
# ==========================================================

greet = lambda: "Hello"

print(greet())

# Output:
# Hello


# ==========================================================
# Lambda with Conditional Expression
# ==========================================================

grade = lambda marks: "Pass" if marks >= 35 else "Fail"

print(grade(90))
print(grade(20))

# Output:
# Pass
# Fail


# ==========================================================
# Lambda with String
# ==========================================================

upper = lambda text: text.upper()

print(upper("python"))

# Output:
# PYTHON


# ==========================================================
# Lambda with List using map()
# ==========================================================

numbers = [12, 34, 56]

result = list(map(lambda x: x + 2, numbers))

print(result)

# Output:
# [14, 36, 58]


# ==========================================================
# Lambda with filter()
# ==========================================================

numbers = [10, 15, 20, 25, 30]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# Output:
# [10, 20, 30]


# ==========================================================
# Lambda with sorted()
# ==========================================================

names = ["Rahul", "Ajay", "Venky", "Annu"]

result = sorted(names, key=lambda x: len(x))

print(result)


# ==========================================================
# Common Mistake
# ==========================================================

def func(l):
    return l + 2

numbers = [12, 34, 56]

# print(func(numbers))
# TypeError:
# can only concatenate list (not "int") to list


# ==========================================================
# Correct Solution
# ==========================================================

result = list(map(lambda x: x + 2, numbers))

print(result)

# Output:
# [14, 36, 58]


# ==========================================================
# Lambda with Comparison Operators
# ==========================================================

# Greater Than (>)

greater = lambda x: x > 10

print(greater(15))
print(greater(5))

# Output:
# True
# False


# ==========================================================
# Less Than (<)
# ==========================================================

less = lambda x: x < 50

print(less(40))
print(less(60))

# Output:
# True
# False


# ==========================================================
# Equal To (==)
# ==========================================================

equal = lambda x: x == 100

print(equal(100))
print(equal(50))

# Output:
# True
# False


# ==========================================================
# Not Equal To (!=)
# ==========================================================

not_equal = lambda x: x != 10

print(not_equal(5))
print(not_equal(10))

# Output:
# True
# False


# ==========================================================
# Greater Than or Equal To (>=)
# ==========================================================

eligible = lambda age: age >= 18

print(eligible(20))
print(eligible(15))

# Output:
# True
# False


# ==========================================================
# Less Than or Equal To (<=)
# ==========================================================

discount = lambda amount: amount <= 5000

print(discount(4500))
print(discount(7000))

# Output:
# True
# False


# ==========================================================
# Lambda with if-else (Ternary Operator)
# ==========================================================

result = lambda marks: "Pass" if marks >= 35 else "Fail"

print(result(90))
print(result(20))

# Output:
# Pass
# Fail


# ==========================================================
# Lambda with Multiple Conditions (and)
# ==========================================================

check = lambda age, citizen: "Eligible" if age >= 18 and citizen else "Not Eligible"

print(check(20, True))
print(check(16, True))
print(check(25, False))

# Output:
# Eligible
# Not Eligible
# Not Eligible


# ==========================================================
# Lambda with Multiple Conditions (or)
# ==========================================================

offer = lambda student, employee: "Discount" if student or employee else "No Discount"

print(offer(True, False))
print(offer(False, True))
print(offer(False, False))

# Output:
# Discount
# Discount
# No Discount

# ===================================
# *************************************
# ===================================
# ==========================================================
# Lambda Function with Two Arguments
# ==========================================================

# Normal Function

def add(a, b):
    return a + b

print(add(12, 13))

# Output:
# 25


# Lambda Function

add = lambda a, b: a + b

print(add(12, 13))

# Output:
# 25


# ==========================================================
# Lambda Function with Three Arguments
# ==========================================================

# Normal Function

def total(a, b, c):
    return a + b + c

print(total(12, 13, 2))

# Output:
# 27


# Lambda Function

result = lambda a, b, c: a + b + c

print(result(12, 13, 2))

# Output:
# 27


# ==========================================================
# Lambda Function with Multiple Arguments
# ==========================================================

# Lambda can accept any number of arguments.

calculate = lambda a, b, c, d, e: a + b + c + d + e

print(calculate(10, 20, 30, 40, 50))

# Output:
# 150


# Another Example

student = lambda name, age, city: (
    f"Name: {name}, Age: {age}, City: {city}"
)

print(student("Rahul", 25, "Hyderabad"))

# Output:
# Name: Rahul, Age: 25, City: Hyderabad