# ==========================================================
# 11. Dictionary Iteration
# ==========================================================
d = {
    "Pizza": 500,
    "Shoes": 2000,
    "Burger": 600
}

for key, value in d.items():
    print(key, ":", value)

# ==========================================================
# 12. Convert Lowercase to Uppercase (Using ASCII)
# ==========================================================
fruit = "apple"

for ch in fruit:
    if 'a' <= ch <= 'z':
        upper = chr(ord(ch) - 32)
        print(upper, end="")
# ==========================================================
# 13. ASCII Value
# ==========================================================
print("\n")
print(ord("A"))

# ==========================================================
# 14. Convert Uppercase to Lowercase
# ==========================================================

course = "PYTHON"

for ch in course:

    if 'A' <= ch <= 'Z':
        lower = chr(ord(ch) + 32)
        print(lower, end=" ")