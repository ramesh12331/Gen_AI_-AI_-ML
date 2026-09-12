# ==========================================================
# PYTHON LOOPS - COMPLETE PROGRAM
# Author : Beginner Friendly
# ==========================================================

for ch in "Python":
    print(ch, end=" ")

print("\n")
# ==========================================================
# 2. RANGE FUNCTION
# ==========================================================
for i in range(1, 11, 2):
    print(i, end=" ")

print("\n")

# Example
for i in range(10,0,-1):
    print(i, end=" ")
print("\n")

# Example
for i in range(50,1,-1):
    print(i, end=" ")

print("\n")
# ==========================================================
#looping through list:
# ==========================================================
l = [12,34,56,78]
for element in l:
    print(element, end=" ")
print("\n")

# ==========================================================
#looping through tuple
# ==========================================================
l = (12,34,56,78)
for element in l:
    print(element, end=" ")
print("\n")

# ==========================================================
#looping through dict
# ==========================================================
student = {
    "Name": "Ramesh",
    "City": "Hyderabad",
    "Gender": "Male"
}

#iterating all keys:
for key in student:
    print(key)

print("\n")

#iterating over all values:
for value in student.values():
    print(value)

print("\n")
#iterating all keys and values ate once:

for key, value in student.items():
    print(key, ":", value)

print("\n")
# ==========================================================
#Loops with if statements
# ==========================================================
# EVEN NUMBERS
numbers = [12, 3, 4, 5, 6, 7, 8, 9, 34, 56, 79]
print("Even Numbers:")

for num in numbers:
    if num%2 == 0:
        print(num, end=" ")
print("\n")
# ==========================================================
#looping with operators
# ==========================================================
prices =[200,300,400,450,500,600]

print("Total Price")
Total = 0

for num in prices:
    # Total += num
    Total = Total + num
print(Total)

print("\n")
# ==========================================================
#loop with break,continue,pass
# ==========================================================
print("Break")
for i in range(10):
    if i==3:
        break
    print(i)

print("\n")

print("Continue")

print("\n")

for i in range(10):
    if i == 3:
        continue
    print(i)

print("\n")

print("Pass")

for i in range(5):
    if i==2:
        pass
    print(i)

print("\n")
# ==========================================================
# FOR ELSE
# ==========================================================
for i in range(10):
    if i == 7:
        break
    print(i)
else:
    print("Loop Completed")

print("\n")
# ==========================================================
#nested for loops:
# ==========================================================
l =['A','b']
sub= ['GK','maths','physics']

for i in l:
    for j in sub:
        print(i, ":", j)

print("\n")

# ==========================================================
# SUM OF DIGITS
# ==========================================================
num = 456
total = 0

for i in range(len(str(num))):
    digit = num%10
    total += digit
    num = num//10
print(total)

print("\n")

# Example
num = int(input("Enter Number : "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit
    temp = temp // 10

print("Sum of Digits =", total) 

print("\n")
# ==========================================================
# FIBONACCI SERIES
# ==========================================================
n = int(input("How many terms : "))

a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(1, n):
    c = a+b
    print(c, end=" ")
    a = b
    b = c
# ==========================================================
# FACTORIAL
# ==========================================================
n = 6
fact = 1
for i in range(1,6+1):
    fact = fact * i
    print("Fact",fact)
print("Final Fact: ",fact)

# Example
n = int(input("Enter Number : "))
fact = 1

for i in range(1, n+1):
    fact = fact * i
print("Factorial Number", fact)

# ==========================================================
# character count
# ==========================================================

# s ='JHWERAGRLWEH7834562873@w76E3124hggdfb#@$'
s = input("Enter String : ")

lower = 0
upper = 0
digit = 0
special = 0

for ch in s:
    if ch >='a' and ch<='z':
        lower += 1
    elif ch >= 'A' and ch <= 'Z':
        upper += 1
    elif ch >= '0' and ch <= '9':
        digit += 1
    else:
        special += 1
print('lower : ', lower)
print('upper : ', upper)
print('digit : ', digit)
print('special : ', special)

# ==========================================================
# PALINDROME NUMBER
# ==========================================================
num = int(input("Enter Number : "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# ==========================================================
# MULTIPLICATION TABLE
# ==========================================================
number = int(input("Enter Number : "))

for i in range(1, 11):
    print(number, "x", i, "=", number*i)

# ==========================================================
# COUNT EVEN AND ODD
# ==========================================================
numbers = [12, 15, 22, 35, 44, 51, 60]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Count =", even)
print("Odd Count  =", odd)

# ==========================================================
# LARGEST NUMBER IN LIST
# ==========================================================
numbers = [23, 56, 12, 89, 45, 100, 65]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("Largest Number =", largest)

# ==========================================================
# SMALLEST NUMBER IN LIST
# ==========================================================
numbers = [23, 56, 12, 89, 45, 100, 65]

smallest = numbers[0]

for num in numbers:
    if num<smallest:
        smallest = num
print("Smallest Number =", smallest)

# ==========================================================
# STAR PATTERN
# ==========================================================
rows = 5

for i in range(1, rows+1):
    for j in range(i):
        print("*", end=" ")
    print()

# ==========================================================
# REVERSE STAR PATTERN
# ==========================================================
rows = 5

for i in range(rows,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

# ==========================================================
# String Example
# ==========================================================
a = 'python programming'

for ch in range(0, len(s), 2):
    print(a[ch], end=" ")