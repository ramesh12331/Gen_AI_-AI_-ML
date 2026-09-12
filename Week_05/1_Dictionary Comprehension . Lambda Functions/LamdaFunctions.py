# ==========================================================
# Lambda Function with Two Arguments
# ==========================================================

# Normal Function

def add(a,b):
    return a+b
print(add(12,16))

# Lambda Function
add = lambda a,b : a+b
print(add(20,30))

# ==========================================================
# Lambda Function with Three Arguments
# ==========================================================

# Normal Function
def total(a,b,c):
    return a+b+c
print(total(10,20,30))

# Lambda Function
result = lambda a,b,c: a+b+c
print(result(90,80,70))

# ==========================================================
# Lambda Function with Multiple Arguments
# ==========================================================

# Lambda can accept any number of arguments.

calculate = lambda a,b,c,d,e: a+b+c+d+e
print(calculate(90,70,80,60,50))

# Another Example
student = lambda name, age, city: (
    f"Name: {name}, Age: {age}, City: {city}"
)

print(student("Ramesh", 30, "Hyderabad"))