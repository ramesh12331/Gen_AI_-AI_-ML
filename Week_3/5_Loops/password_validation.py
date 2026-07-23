# ==========================================================
# PASSWORD VALIDATION
# ==========================================================
password = input("Enter Password : ")

lower = 0
upper = 0
digit = 0
special = 0

for ch in password:
    if 'a' <= ch <= 'z':
        lower += 1
    elif 'A' <= ch <= 'Z':
        upper += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        special +=1

if len(password) > 10 and lower >= 1 and upper >= 1 and digit >= 1 and special >= 1:
    print("Login Successful")
else:
    print("Invalid Password")

    if len(password) <= 10:
        print("- Password length should be greater than 10")
    if lower == 0:
        print("- At least one lowercase letter required")
    if upper == 0:
        print("- At least one uppercase letter required")
    if digit == 0:
        print("- At least one digit required")
    if special == 0:
        print("- At least one special character required")