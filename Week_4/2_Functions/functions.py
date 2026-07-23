# ==========================================================
# PYTHON FUNCTIONS
# ==========================================================

# ----------------------------------------------------------
# 1. Simple Function
# ----------------------------------------------------------
def myname():
    print("Something")
print(myname) # Prints function reference
myname()  # Calls the function

# Output:
# <function myname at 0x...>
# Something

# ==========================================================
# 2. Function with Parameters
# ==========================================================
def greet(a,b):
    print("Hello User!")
print("Heyy")
print("Ramesh")
greet(10,12)
print("Bye")

# ==========================================================
# 3. Function with Return Statement
# ==========================================================
def add(a,b):
    return a*b
    print("Hello") # This line will never execute

result = add(10, 30)
print(result)

# ==========================================================
# 4. Default Parameter
# ==========================================================
def shipping(price, brand="Nike"):
    print(brand, ":",price)
shipping(5000)
shipping(5000, "Zara")

# ==========================================================
# 5. Keyword Arguments
# ==========================================================
def shipping(uid, pid, oid):
    print(uid, pid, oid)


shipping(
    oid=1001,
    pid=101,
    uid=10001
)

# ==========================================================
# 6. Shopping Function
# ==========================================================
def shopping(name, product, price):
    print(f"Hey {name}, you bought {product} for ₹{price}")


name = input("Enter Name : ")
product = input("Enter Product : ")
price = int(input("Enter Price : "))

shopping(name, product, price)
# ==========================================================
# 7. Grading System
# ==========================================================

def grading_system(marks):

    if marks >= 90:
        print("Grade A")

    elif marks >= 75:
        print("Grade B")

    elif marks >= 60:
        print("Grade C")

    else:
        print("Fail")


grading_system(92)
grading_system(80)
grading_system(65)
grading_system(45)

# ==========================================================
# 8. *args (Multiple Arguments)
# ==========================================================

def shipping(*items):
    print(items)


shipping("A", "123", 9000, 34)

# ==========================================================
# 9. Sum using *args
# ==========================================================

def add(*nums):
    print(sum(nums))


add(2, 3, 4)
add(10, 20, 30, 40)

# ==========================================================
# 10. **kwargs (Keyword Arguments)
# ==========================================================
def shipping_cart(**cart):
    total = 0
    for product, price in cart.items():
        print(product, ":", price)
        total += price
    print("Total :", total)

    if total>3000:
        discount = total*0.10
        print("Discount :", discount)
        final_price = total - discount
        print("Final Price :", final_price)

shipping_cart(
    Pizza=500,
    Shoes=2000,
    Burger=600,
    Mobile=35000
)