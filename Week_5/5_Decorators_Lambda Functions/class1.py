# ==========================================================
# PYTHON - GENERATORS, FILTER & LAMBDA FUNCTIONS
# Author : Ramesh Notes
# ==========================================================

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

# Output:
# [200]


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

def generate():

    i = 0

    while i <= 200:
        print(i, end=" ")
        i += 1


generate()


# ==========================================================
# 7. GENERATOR FUNCTION
# ==========================================================

def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


print(generate())


# ==========================================================
# 8. GENERATOR USING next()
# ==========================================================

def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

print(next(a))
print(next(a))
print(next(a))


# ==========================================================
# 9. GENERATOR USING FOR LOOP
# ==========================================================

def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

for value in a:
    print(value, end=" ")


# ==========================================================
# 10. CONVERT GENERATOR TO LIST
# ==========================================================

def generate():

    i = 0

    while i <= 200:
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

numbers = [1,2,3,4,5,6,7,8,9]


def even(x):

    return x % 2 == 0


result = filter(even, numbers)

print(result)


# ==========================================================
# 13. FILTER OBJECT TO LIST
# ==========================================================

numbers = [1,2,3,4,5,6,7,8,9]


def even(x):

    return x % 2 == 0


result = list(filter(even, numbers))

print(result)


# ==========================================================
# 14. COMMON MISTAKE
# ==========================================================

list = [1,2,3]

# Wrong
# result = list(filter(even, list))

# TypeError:
# 'list' object is not callable

# Reason:
# Variable name 'list' overrides Python's built-in list() function.


# ==========================================================
# 15. CORRECT WAY
# ==========================================================

numbers = [1,2,3]

result = list(filter(even, numbers))

print(result)


# ==========================================================
# 16. FILTER USING LAMBDA
# ==========================================================

numbers = [1,2,3,4,5,6,7,8,9]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)


# ==========================================================
# OUTPUT
# ==========================================================
# [2, 4, 6, 8]

# ==========================================================
# FILTER FUNCTION
# ==========================================================

# Even Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)


# ==========================================================
# Odd Numbers
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(filter(lambda x: x % 2 != 0, numbers))

print(result)


# ==========================================================
# String Filtering
# ==========================================================

words = ["apple", "America", "andhra", "banana", "cat"]

result = list(filter(lambda x: x.startswith("a"), words))

print(result)


# ==========================================================
# Dictionary Filtering (Ratings > 4.5)
# ==========================================================

restaurants = [
    {"name": "abc", "ratings": 4.8},
    {"name": "efg", "ratings": 3.5},
    {"name": "xyz", "ratings": 4.9},
    {"name": "pqr", "ratings": 4.2}
]

result = list(filter(lambda x: x["ratings"] > 4.5, restaurants))

print(result)