# ==========================================================
# 1. CREATE LIST USING WHILE LOOP
# ==========================================================
numbers = []
i = 0
while i <= 200:
    numbers.append(i)
    i += 1

print(numbers)

# ==========================================================
# 2. MEMORY USED BY LIST
# ==========================================================
import sys

numbers = []
i = 0

while i <= 200:
    numbers.append(i)
    i += 1

print(sys.getsizeof(numbers))

# ==========================================================
# 3. WRONG WAY (LIST CREATED INSIDE LOOP)
# ==========================================================

for i in range(1, 201):
    numbers = []
    numbers.append(i)
print(numbers)

# ==========================================================
# 4. CORRECT WAY
# ==========================================================

numbers = []
for i in range(1, 201):
    numbers.append(i)
print(numbers)

# ==========================================================
# 5. MEMORY CHECK AGAIN
# ==========================================================
import sys

numbers = []
for i in range(1, 201):
    numbers.append(i)

print(sys.getsizeof(numbers))

# ==========================================================
# 6. NORMAL FUNCTION
# ==========================================================
print("Normal Function")
def generate():

    i = 0

    while i<= 200:
        print(i, end=" ")
        i += 1
generate()

# ==========================================================
# 7. GENERATOR FUNCTION
# ==========================================================
print("\nGENERATOR FUNCTION")

def generate():
    i = 0
    while i<=200:
        yield i
        i += 1
print(generate())

# ==========================================================
# 8. GENERATOR USING next()
# ==========================================================
print("\nGENERATOR USING next()")
def generate():
    i = 0

    while i<=200:
        yield i
        i += 1
a = generate()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# ==========================================================
# 9. GENERATOR USING FOR LOOP
# ==========================================================
print("\nGENERATOR USING FOR LOOP")

def generate():
    i=0
    while i<=200:
        yield i
        i += 1
a = generate()

for value in a:
    print(value, end = " ")

# ==========================================================
# 10. CONVERT GENERATOR TO LIST
# ==========================================================
print("\nCONVERT GENERATOR TO LIST")

def generate():

    i = 0
    while i<= 200:
        yield i
        i += 1

a = generate()
numbers = []

for value in a:
    numbers.append(value)
print(numbers)

# ==========================================================
# 11. MEMORY OF GENERATED LIST
# ==========================================================
print("\nMEMORY OF GENERATED LIST")
import sys

def generate():
    i = 0
    while i <= 200:
        yield i
        i += 1

a = generate()
numbers = []

for value in a:
    numbers.append(value)

print(sys.getsizeof(numbers))

# ==========================================================
# 12. FILTER FUNCTION
# ==========================================================
print("\nFILTER FUNCTION")
numbers = [1,2,3,4,5,6,7,8,9]

def even(x):
    return x%2 == 0

result = filter(even, numbers)
print(result)
# ==========================================================
# 13. FILTER OBJECT TO LIST
# ==========================================================
print("\nFILTER OBJECT TO LIST")
numbers = [1,2,3,4,5,6,7,8,9]
def even(x):
    return x%2 == 0

result = list(filter(even, numbers))
print(result)

# ==========================================================
# 14. COMMON MISTAKE
# ==========================================================
print("\nCOMMON MISTAKE")
# list = [1,2,3]

# Wrong
# result = list(filter(even, list))

# TypeError:
# 'list' object is not callable

# Reason:
# Variable name 'list' overrides Python's built-in list() function.

# ==========================================================
# 15. CORRECT WAY
# ==========================================================
print("\nCORRECT WAY")
numbers = [1,2,3]

result = list(filter(even, numbers))

print(result)

# ==========================================================
# 16. FILTER USING LAMBDA
# ==========================================================
numbers = [1,2,3,4,5,6,7,8,9]

result = list(filter(lambda x:x%2 == 0, numbers))
print(result)

# ==========================================================
# ODD NUMBERS
# ==========================================================
print("\nODD NUMBERS")
numbers = [1,2,3,4,5,6,7,8,9]

result = list(filter(lambda x:x%2 != 0, numbers))
print(result)

# ==========================================================
# String Filtering
# ==========================================================
print("\n String Filtering")
words = ["apple", "America", "andhra", "banana", "cat"]

result = list(filter(lambda x:x.startswith("a"), words))
print(result)

# ==========================================================
# Dictionary Filtering (Ratings > 4.5)
# ==========================================================
print("\nDictionary Filtering (Ratings > 4.5)")
restaurants = [
    {"name": "abc", "ratings": 4.8},
    {"name": "efg", "ratings": 3.5},
    {"name": "xyz", "ratings": 4.9},
    {"name": "pqr", "ratings": 4.2}
]

result = list(filter(lambda x:x["ratings"]>4.5, restaurants))
print(result)

# ==========================================================
# Python Functions are First Class Citizens
# ==========================================================
def fun():
    a = 10
    b = 20

    def add(x,y):
        print(x+y)

    return add

a = fun()
a(10,20)

# ==========================================================
# FUNCTION RETURNING ANOTHER FUNCTION
# ==========================================================
print("\n FUNCTION RETURNING ANOTHER FUNCTION")
def add(a,b):
    print(a+b)
    def mul(e,f):
        print(e*f)

    return mul

a = add(30,40)
a(3,4)

# Example 1
print("\nExample 1")

def add(a,b):
    print("Addition", a+b)
    
    def mul(e,f):
        print("Multiplacation", e*f)

    return mul

a = add(30,40)
a(3,4)

# ==========================================================
# 2. SIMPLE DECORATOR
# ==========================================================

print("\n========== 2. SIMPLE DECORATOR ==========\n")

def dec(func):
    def wrap():
        print("****************************************")
        func()
        print("****************************************")
    return wrap

def greet():
    print("Hello User!!!")
greet()

# -------------------
# 3. MANUAL DECORATOR
# -------------------

print("\n========== 3. MANUAL DECORATOR ==========\n")

a = dec(greet)
a()

# -------------------
# 4. USING @ DECORATOR
# -------------------

print("\n========== 4. USING @ DECORATOR ==========\n")

@dec
def message():
    print("Welcome to Python Decorators")
message()

# -------------------
# 5. MULTIPLE FUNCTIONS USING SAME DECORATOR
# -------------------
print("\n========== 5. MULTIPLE FUNCTIONS ==========\n")

@dec
def display():
    print("Displaying...")

display()
greet()

# ==========================================================
# 6. TIMER DECORATOR
# ==========================================================
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(
            "Time taken to execute",
            func.__name__,
            ":",
            end - start,
            "seconds",
        )
    return wrapper
@timer
def message():
    print("Message Function")
    time.sleep(3)

message()

# ==========================================================
# 8. DECORATOR WITH ARGUMENTS (*args, **kwargs)
# ==========================================================

print("\n========== 8. DECORATOR WITH ARGUMENTS ==========\n")

def timer_args(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(
            "Time taken to execute",
            func.__name__,
            ":",
            end - start,
            "seconds",
        )
        return result
    return wrapper

@timer_args
def add(a,b):
    print("Sum:",a+b)
add(2,4)

# ==========================================================
# 9. DECORATOR WITH RETURN VALUE
# ==========================================================
print("\n========== 9. RETURN VALUE ==========\n")

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before Function")
        result = func(*args, **kwargs)
        print("After Function")
        return result
    return wrapper

@decorator
def square(num):
    return num * num
print("Square :", square(5))

# ==========================================================
# 10. SUMMARY
# ==========================================================

print("\n========== SUMMARY ==========\n")

print("1. Functions are first-class objects.")
print("2. Functions can return another function.")
print("3. Decorators add extra functionality.")
print("4. Manual Decoration : a = dec(func)")
print("5. @dec is shortcut for a = dec(func)")
print("6. Timer Decorator measures execution time.")
print("7. *args and **kwargs make decorators reusable.")

print("\n========== END ==========")