from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# -------------------------
# Testing
# -------------------------

# password = "python123"

# hashed_password = hash_password(password)

# print("Original password:", password)
# print("Hashed password:", hashed_password)

# result = verify_password(
#     password,
#     hashed_password
# )

# print("Password correct:", result)