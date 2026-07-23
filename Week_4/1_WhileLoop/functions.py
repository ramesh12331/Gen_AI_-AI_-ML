# ===========================================================
# 7. Simple Function
# ===========================================================

def greet():
    print("Hello User!")
greet()

# ===========================================================
# 8. Function with Arguments
# ===========================================================
def greet(name, age):
    print("Name : ",  name)
    print("Age : ",  age)
greet("Ramesh", 24)

# ===========================================================
# 9. Return Function
# ===========================================================
def add(a,b):
    return a+b
result = add(10,20)
print(result)

# ===========================================================
# 10. Shipping
# ===========================================================
def shipping(company,price):
    print(company, ":", price)
shipping("Puma",5000)

# ===========================================================
# 11. Address Function
# ===========================================================
def address(pincode, city, house_no):
    print("City : ", city)
    print("Pincode : ", pincode)
    print("House No : ", house_no)

address(500002, "Hyderabad", 321)

# ===========================================================
# 12. Grade System
# ===========================================================
print("\n========== Grade ==========")

def grading_system(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >=60:
        print("Grade C")
    else:
        print("Fail")
grading_system(90)

# ===========================================================
# 13. *args Example
# ===========================================================
def add(*numbers):
    print(sum(numbers))
add(2, 3, 4, 5)

# ===========================================================
# 14. *args Shipping
# ===========================================================
def shipping(*items):
    print(items)
shipping("Rice", "Sugar", "Oil", "Dal")

# ===========================================================
# 15. Multiplication Function
# ===========================================================
def multiply(a, b):
    print(a*b)
multiply(10, 20)

# ===========================================================
# 16. List Examples
# ===========================================================
numbers = [10, 20, 30, 40, 50]
print(numbers)

mixed = [1, 2.5, True, "Python"]
print(mixed)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[1])
print(matrix[2][0])
