# ==========================================================
# PYTHON LISTS
# ==========================================================

# ----------------------------------------------------------
# What is a List?
# ----------------------------------------------------------
# A list is an ordered collection of items.
# It can store multiple values in a single variable.

# Why do we use Lists?
# -> Store multiple values
# -> Easy to access and modify
# -> Supports different data types

# ==========================================================
# Creating a List
# ==========================================================
numbers = [20, 30, 49.0]
print(numbers)

# ==========================================================
# Important Properties of List
# ==========================================================
# 1. Uses square brackets []
# 2. Ordered
# 3. Heterogeneous (Different data types)
# 4. Supports Indexing
# 5. Supports Slicing
# 6. Mutable (Can be modified)


# ==========================================================
# Heterogeneous List
# ==========================================================

data = [12, 34.5, 67 + 8j, "Python", True]
print(data)

# ==========================================================
# Indexing
# ==========================================================

print(data[0])
print(data[3])

# ==========================================================
# Negative Indexing
# ==========================================================

print(data[-1])
print(data[-2])

# ==========================================================
# Slicing
# ==========================================================
data = [12, 34.5, 67 + 8j, "Python", True]
print(data[1:4])
print(data[:3])
print(data[::2])

# ==========================================================
# Reverse List Using Slicing
# ==========================================================
print(data[::-1])

# ==========================================================
# Updating List Elements
# ==========================================================

letters = ["A", "B", "C", "D"]
letters[3] = "E"
print(letters)

# ==========================================================
# Nested List
# ==========================================================

matrix = [
    [1, 3, 2],
    [4, 6, 5],
    [7, 9, 8]
]

print(matrix[0][0])
print(matrix[1][1])

# ==========================================================
# Append Method
# ==========================================================

numbers = [10, 20, 30, 40, 50]
numbers.append(500)
print(numbers)

# ==========================================================
# Insert Method
# ==========================================================
numbers.insert(1,200)
print(numbers)

# ==========================================================
# Extend Method
# ==========================================================
extra = (20, 40, 50)
numbers.extend(extra)
print(numbers)

# ==========================================================
# Remove Method
# ==========================================================
numbers = [10, 20, 30, 40, 50]
numbers.remove(50)
print(numbers)
# ==========================================================
# Pop Method
# ==========================================================
numbers = [10, 20, 30, 40, 50]
numbers.pop()
print(numbers)

# ==========================================================
# Delete Using del
# ==========================================================
numbers = [10, 20, 30, 40, 50]
del numbers[1]
print(numbers)
# ==========================================================
# Clear Method
# ==========================================================
numbers.clear()
print(numbers)

# ==========================================================
# List Operators
# ==========================================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1+list2)

# ==========================================================
# Membership Operators
# ==========================================================

files = ["data.csv", "data.xlsx"]

print("data.csv" in files)
print("data.xlsx" in files)

# ==========================================================
# Loop Through List
# ==========================================================
numbers = [10, 12, 34, 56, 79, 87]

for num in numbers:
    print(num)
# ==========================================================
# Loop Using Index
# ==========================================================
for index in range(len(numbers)):
    print(index, numbers[index])
# ==========================================================
# Print Alternate Elements
# ==========================================================
for index in range(0, len(numbers), 2):
    print(numbers[index], end=" ")

# ==========================================================
# List with If-Else
# ==========================================================

numbers = [12, 34, -56, 90, 0, 87, -65]
for num in numbers:
    if num>0:
        if num%2 == 0:
            print(num, "Even Number")
        else:
            print(num, "Odd Number")
    elif num == 0:
         print(num, "Zero")
    else:
        print(num, "Negative")
# ==========================================================
# Enumerate Function
# ==========================================================

names = ["A", "B", "C", "D"]

for index, name in enumerate(names):
    print(index, name)
# ==========================================================
# Continue Statement
# ==========================================================

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        continue
    print(num)

# ==========================================================
# Break Statement
# ==========================================================
numbers = [10, 20, 30, 40, 50]
print("Break Statement")
for num in numbers:
    if num == 30:
        break
    print(num)
# ==========================================================
# Index Method
# ==========================================================

numbers = [10, 20, 30, 40, 30]
print(numbers.index(30))
# ==========================================================
# Count Method
# ==========================================================
print(numbers.count(30))
# ==========================================================
# Sort Method
# ==========================================================

numbers = [40, 10, 20, 50, 30]
numbers.sort()
print(numbers)

# Descending Order
# numbers.sort(reverse = True)
numbers.reverse()
print(numbers)

# ==========================================================
# Built-in Functions
# ==========================================================

numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

# ==========================================================
# Average of List
# ==========================================================

numbers = [10, 20, 30, 40, 50]

avg = sum(numbers)/len(numbers)
print("Average =",avg)

# ==========================================================
# List Comprehension
# ==========================================================

# Syntax
# [expression for variable in iterable]

# Squares

Squares = [x**2 for x in range(1,6)]
print(Squares)

# Cubes

Cubes = [x**3 for x in range(1,6)]
print(Cubes)

# Uppercase

names = ["python", "java", "c"]

upper = [name.upper() for name in names]
print(upper)

# Lowercase

names = ["PYTHON", "JAVA", "C"]

lower = [name.lower() for name in names]
print(lower)

# String Length

words = ["Python", "Java", "SQL"]
Length = [len(word) for word in words]
print("Length of String:",Length)

# ==========================================================
# List Comprehension with If Condition
# ==========================================================

even = [x for x in range(1,21) if x%2==0]
print(even)

# ==========================================================
# Multiple Conditions
# ==========================================================
numbers = [x for x in range(1,51) if x%2==0 and x%5==0]
print(numbers)

# ==========================================================
# Grading System Using List
# ==========================================================

marks = [95, 82, 76, 63, 45]

grades = []

for mark in marks:
    if mark >= 90:
        grades.append("A")
    elif mark >=75:
        grades.append("B")
    elif mark >=60:
        grades.append("C")
    else:
        grades.append("Fail")
print(grades)

# ==========================================================
# Nested List Comprehension
# ==========================================================
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
print(matrix)

# Output:
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]