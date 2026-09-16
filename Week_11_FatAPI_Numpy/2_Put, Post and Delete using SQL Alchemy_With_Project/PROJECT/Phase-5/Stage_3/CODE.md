Great 👍 We have completed **Register + Password Hashing**. Now let's build the next part: **LOGIN + JWT Token**.

We'll do it step-by-step and keep it beginner-friendly.

# 🔐 STEP 14 — Login with JWT

The login flow is:

```text
User
 │
 │ username + password
 ↓
POST /auth/login
 │
 ↓
Find user in database
 │
 ↓
Check password
 │
 ↓
Correct?
 ├── NO  → ❌ Invalid username/password
 │
 └── YES
       ↓
   Create JWT token
       ↓
   Return token
```

---

# 1️⃣ Update `schemas/user.py`

We already created `UserLogin`.

Your file should now be:

```python id="v4d3xk"
from pydantic import BaseModel, Field


class UserRegister(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: str

    password: str = Field(
        min_length=6
    )


class UserLogin(BaseModel):

    username: str

    password: str
```

The login request will be:

```json id="k0x2pk"
{
    "username": "ravi",
    "password": "python123"
}
```

---

# 2️⃣ Add JWT code to `security.py`

Currently we have:

```python id="1c1f5n"
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
```

Now we need to add JWT.

---

## 2.1 Import JWT

At the top add:

```python id="9z2m4v"
from datetime import datetime, timedelta, timezone
from jose import jwt
```

So:

```python id="7z1z0f"
from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext
from jose import jwt
```

---

# 3️⃣ Create JWT settings

Add:

```python id="5nj5kq"
SECRET_KEY = "my-super-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

### What are these?

### `SECRET_KEY`

```python id="v20v1w"
SECRET_KEY = "my-super-secret-key"
```

This is used to **sign the JWT token**.

Think:

```text id="zj7k9f"
User information
      +
 SECRET KEY
      ↓
    JWT
```

⚠️ This is just for learning. In a real application, don't hard-code the secret key.

---

### `ALGORITHM`

```python id="z1j53x"
ALGORITHM = "HS256"
```

This tells JWT which algorithm to use for signing the token.

For now, simply remember:

```text
HS256 = JWT signing algorithm
```

---

### Token expiration

```python id="1s8c7h"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

The token will expire after **30 minutes**.

```text
Login
  ↓
JWT created
  ↓
30 minutes
  ↓
Token expires ❌
```

---

# 4️⃣ Create `create_access_token()`

Add this function:

```python id="b0q3y2"
def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
```

---

# 🧠 Understand this function

We call:

```python id="1pkp3e"
create_access_token({
    "sub": "1",
    "username": "ravi",
    "role": "student"
})
```

The function takes this information:

```text id="08e8o4"
user_id
username
role
```

and creates a JWT.

Conceptually:

```text id="zddz7g"
{
    "sub": "1",
    "username": "ravi",
    "role": "student"
}
             +
        SECRET_KEY
             ↓
          JWT Token
```

---

# 5️⃣ Complete `security.py`

Your file should now be:

```python id="pfy1gd"
from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext
from jose import jwt


# -------------------------
# JWT Settings
# -------------------------

SECRET_KEY = "my-super-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# -------------------------
# Password Hashing
# -------------------------

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
# Create JWT Token
# -------------------------

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
```

---

# 6️⃣ Add Login to `routers/auth.py`

Currently you have registration.

Add this import:

```python id="q0d7wc"
from schemas.user import UserRegister, UserLogin
```

And change:

```python id="a6v6wr"
from security import hash_password
```

to:

```python id="jz7v5h"
from security import (
    hash_password,
    verify_password,
    create_access_token
)
```

---

# 7️⃣ Create Login Endpoint

Add this **below the register endpoint**:

```python id="8cyz4s"
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user is None:

        return {
            "message": "Invalid username or password"
        }

    password_correct = verify_password(
        user.password,
        existing_user.password
    )

    if not password_correct:

        return {
            "message": "Invalid username or password"
        }

    access_token = create_access_token({
        "sub": str(existing_user.user_id),
        "username": existing_user.username,
        "role": existing_user.role
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
```

---

# 🧠 Understand Login Step-by-Step

## Step 1 — User sends login data

```json id="1bdb92"
{
    "username": "ravi",
    "password": "python123"
}
```

FastAPI receives:

```python id="5p9n5c"
user: UserLogin
```

---

## Step 2 — Find the user

```python id="sn6mfw"
existing_user = db.query(User).filter(
    User.username == user.username
).first()
```

Database:

```text
users
--------------------------------
user_id | username | password
--------------------------------
1       | ravi     | $2b$12$...
```

We search:

```text
username = ravi
```

---

## Step 3 — Check if user exists

```python id="jwjw5m"
if existing_user is None:
```

If Ravi doesn't exist:

```json id="6bdh67"
{
    "message": "Invalid username or password"
}
```

---

# 8️⃣ Verify Password

This is the important part:

```python id="8u5g0c"
password_correct = verify_password(
    user.password,
    existing_user.password
)
```

We have:

```text
User enters:

python123
     │
     ↓
user.password
```

Database contains:

```text
$2b$12$........
     │
     ↓
existing_user.password
```

Then:

```text
verify_password()
       ↓
Compare
       ↓
True / False
```

---

# 9️⃣ Wrong Password

If the user enters:

```json id="y4a8pf"
{
    "username": "ravi",
    "password": "wrong123"
}
```

Then:

```python id="jvqgq5"
password_correct
```

will be:

```text
False
```

So:

```python id="9k5m9x"
if not password_correct:
```

returns:

```json id="u9m0vf"
{
    "message": "Invalid username or password"
}
```

---

# 🔑 10️⃣ Correct Password → Create JWT

If password is correct:

```python id="b9gk8k"
access_token = create_access_token({
    "sub": str(existing_user.user_id),
    "username": existing_user.username,
    "role": existing_user.role
})
```

For Ravi, conceptually:

```json id="v1x9l0"
{
    "sub": "1",
    "username": "ravi",
    "role": "student"
}
```

This information is put inside the JWT.

---

# 11️⃣ Return Token

```python id="1v9t6j"
return {
    "access_token": access_token,
    "token_type": "bearer"
}
```

Response will look like:

```json id="j34a2h"
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

The long string is the **JWT token**.

---

# 📄 Complete `routers/auth.py`

Now your file should look like this:

```python id="9xq4mj"
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserRegister, UserLogin

from security import (
    hash_password,
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# -------------------------
# Register
# -------------------------

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:

        return {
            "message": "Username already exists"
        }

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role="student"
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.user_id,
        "username": new_user.username
    }


# -------------------------
# Login
# -------------------------

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user is None:

        return {
            "message": "Invalid username or password"
        }

    password_correct = verify_password(
        user.password,
        existing_user.password
    )

    if not password_correct:

        return {
            "message": "Invalid username or password"
        }

    access_token = create_access_token({
        "sub": str(existing_user.user_id),
        "username": existing_user.username,
        "role": existing_user.role
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
```

---

# 🧪 STEP 15 — Test Login

Restart your server if necessary:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

You should see:

```text
Authentication

POST /auth/register
POST /auth/login
```

Choose:

**POST `/auth/login`**

Send:

```json id="4oyg7k"
{
    "username": "ravi",
    "password": "python123"
}
```

You should receive:

```json id="rj4j1w"
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

🎉 **You have now implemented login + JWT creation.**

---

# 🧠 Remember This Flow

```text
              REGISTER
                 │
                 ↓
        username + password
                 │
                 ↓
         hash_password()
                 │
                 ↓
          hashed password
                 │
                 ↓
             DATABASE
```

Then:

```text
               LOGIN
                 │
                 ↓
        username + password
                 │
                 ↓
          Find user
                 │
                 ↓
       verify_password()
                 │
          ┌──────┴──────┐
          ↓             ↓
        False          True
          ↓             ↓
         ❌         create JWT
                        │
                        ↓
                   JWT Token
                        │
                        ↓
                   Protected API
```

**Next step is the most important part:** we'll create `get_current_user()` so FastAPI can read the JWT token and **protect your Student APIs**.
