# ==========================================================
# PYTHON STRINGS
# ==========================================================

# ----------------------------------------------------------
# What is a String?
# ----------------------------------------------------------
# A string is a sequence of characters enclosed in
# single quotes (' '), double quotes (" "),
# or triple quotes (''' ''' or """ """).

# Why do we use Strings?
# -> Store text data
# -> Manipulate text
# -> Perform searching and formatting

# ==========================================================
# Creating Strings
# ==========================================================
s1 = "Python"
s2 = 'Data Science'
s3 = "'Data Science' is easy to learn"

print(s1)
print(s2)
print(s3)

# ==========================================================
# Indexing
# ==========================================================

s = "Apple"

print(s[0])
print(s[1])
print(s[4])

# ==========================================================
# Negative Indexing
# ==========================================================
print("Negative Indexing")
print(s[-1])
print(s[-2])

# ==========================================================
# String Slicing
# ==========================================================
s = "programming"
print("String Slicing")
print(s[0:2])
print(s[3:7])
print(s[:5])
print(s[::2])

# ==========================================================
# Reverse a String
# ==========================================================

Fruit = "pine apple"
print(Fruit[::-1])

# ==========================================================
# Iterate Through String
# ==========================================================
s = "programming"

for ch in s:
    print(ch, end=" ")

# ==========================================================
# Iterate Using Index
# ==========================================================
print("\n")
for i in range(0,len(s),2):
    print(i,":", s[i], end=" ")

# ==========================================================
# Count Vowels
# ==========================================================
print("\n")
s = "programmingooooooooOOOOO"

vowels = "aeiouAEIOU"

count = 0

for ch in s:
    if ch in vowels:
        # print(ch)
        count += 1
print("Total Vowels :", count)

# ==========================================================
# String with If Condition
# ==========================================================
email = "anwar@gmail.com"

if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")

# ==========================================================
# String Formatting
# ==========================================================
name = "Anwar"
city = "hyd"

print("Hey", name, "You belong to", city)
print("Hey {} You belong to {}".format(name,city))
print(f"Hey {name.upper()} You belong to {city.title()}")

# ==========================================================
# lower()
# ==========================================================
s = "APPLe"
print(s.lower())

# ==========================================================
# upper()
# ==========================================================
print(s.upper())

# ==========================================================
# title()
# ==========================================================

s = "java programming"

print(s.title())

# Output:
# Java Programming

# ==========================================================
# capitalize()
# ==========================================================

print(s.capitalize())
# Output:
# Java programming

# ==========================================================
# strip()
# ==========================================================
s = "    java    "

print(s.strip())
# ==========================================================
# lstrip()
# ==========================================================

print(s.lstrip())
print(len(s))

# ==========================================================
# rstrip()
# ==========================================================

print(s.rstrip())
# Output:
#     java

# ==========================================================
# replace()
# ==========================================================

city = "Hyderabad"

print(city.replace("a","k"))

# Replace only first 2 occurrences

print(city.replace("a", "k", 2))

# ==========================================================
# split()
# ==========================================================

files = [
    "data.csv",
    "demo.xml",
    "sample.json",
    "demo.csv"
]

result = []
count = 0

for file in files:
    if file.split(".")[1] == "csv":
        result.append(file)
        count += 1
print(result)
print("Count :", count)

# Output:
# ['data.csv', 'demo.csv']
# Count : 2

# ==========================================================
# join()
# ==========================================================

fruits = ["apple", "banana", "avocado"]

result = " , ".join(fruits)
print(result)

# ==========================================================
# find()
# ==========================================================
s = "Python Programming"

print(s.find("Pro"))
# Output:
# 7
# ==========================================================
# index()
# ==========================================================

print(s.index("P"))

# ==========================================================
# count()
# ==========================================================

print(s.count("m"))

# ==========================================================
# startswith()
# ==========================================================

print(s.startswith("Python"))

# ==========================================================
# endswith()
# ==========================================================

print(s.endswith("ing"))

# ==========================================================
# isdigit()
# ==========================================================

number = "12345"

print(number.isdigit())

# ==========================================================
# isalpha()
# ==========================================================

word = "Python"

print(word.isalpha())
# ==========================================================
# isalnum()
# ==========================================================

text = "Python123"

print(text.isalnum())
# ==========================================================
# swapcase()
# ==========================================================

s = "PyThOn"

print(s.swapcase())

# ==========================================================
# Practice Programs
# ==========================================================

# Reverse a String

text = "Python"

print(text[::-1])

# Count Uppercase Letters

text = "PyTHon"

count = 0

for ch in text:
    if ch.isupper():
        count += 1
print("Uppercase Letters :", count)

# Count Digits

text = "Python12345"

count = 0

for ch in text:
    if ch.isdigit():
        count += 1
print("Digits: ",count)

# Count Special Characters

text = "Python@123#"

count = 0

for ch in text:
    if ch.isalnum():
        count +=1
print("Special Characters :", count)