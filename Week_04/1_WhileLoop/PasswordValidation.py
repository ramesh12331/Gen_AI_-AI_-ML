password = input("Enter Password : ")

has_lower = False
has_upper = False
has_digit = False
has_special = False

for ch in password:

    if 'a' <= ch <= 'z':
        has_lower = True

    elif 'A' <= ch <= 'Z':
        has_upper = True

    elif '0' <= ch <= '9':
        has_digit = True

    else:
        has_special = True


if len(password) < 10:

    print("Password must contain at least 10 characters.")

elif not has_lower:

    print("Password must contain at least one lowercase letter.")

elif not has_upper:

    print("Password must contain at least one uppercase letter.")

elif not has_digit:

    print("Password must contain at least one digit.")

elif not has_special:

    print("Password must contain at least one special character.")

else:

    print("Password is valid. Login Successful.")