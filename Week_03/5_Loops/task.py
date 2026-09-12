password = input("Enter Password: ")

lower = False
upper = False
special = False

# Check password length
if len(password) > 10:
    for ch in password:
        if ch.islower():
            lower = True
        elif ch.isupper():
            upper = True
        elif ch.isalnum():
            special = True
    if lower and upper and special:
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Password length must be greater than 10")

